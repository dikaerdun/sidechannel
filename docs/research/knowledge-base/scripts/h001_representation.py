#!/usr/bin/env python3
"""EXP-20261107-01 / PQC-H001 v1 -- published runner.

Published copy of the reviewed (v2) implementation. Usage:
  python h001_representation.py --mode freeze-dev --root <repo-root>
  python h001_representation.py --mode holdout    --root <repo-root>
The b1 covariate CSV export is done by the independent verifier, not here.

Frozen protocol (v1 + clarifications C1-C4), SHA-256
cc4eac9f9ab2ccbb1ca858ee031ea4527b8b22e187413a439af29339ef8d4fe9.
Artifacts are written under <root>/<outdir>/ (default: sidechannel-results/h001).

Changes vs the first runner (kept in the local batch log):
  R1 --freeze-dev writes frozen dev artifacts (point, coefs) to --outdir; --holdout NEVER
     re-runs dev selection or refits, and reads each holdout trace file once.
  R2 rank check now covers B/A/C/W in both dev folds (read-only) and pooled;
     shape/dtype/finiteness checks on every trace array; b1 CSV hashes are
     verified against verification/public-b1/SHA256SUMS before any holdout read.
  R3 unused loader removed; all paths parameterized via --root.
  R4 no verification results are read.

No change to split, sample point, thresholds, models or gates. The confirmatory
holdout read had already happened once before the reviewed version
  was written (timeline recorded in the batch log);
this run is the reviewed plumbing implementation and must reproduce it.
"""
import argparse
import hashlib
import json
import os
import time

import numpy as np
import scipy.io as sio

Q = 3329
QINV = -3327
RANK_REL = 1e-10
DEV = ["A99", "A199"]
HOLD = ["A499", "A599", "A699", "A799"]
GATE = 0.01


def montgomery(a):
    a = np.asarray(a, dtype=np.int32)
    t = ((a & 0xFFFF) * QINV) & 0xFFFF
    t = np.where(t >= 0x8000, t - 0x10000, t).astype(np.int32)
    return ((a - t * Q) >> 16).astype(np.int16)


def hw16(x):
    x = np.asarray(x, dtype=np.int64) & 0xFFFF
    out = np.zeros(x.shape, dtype=np.int64)
    for k in range(16):
        out += (x >> k) & 1
    return out


def check_traces(Y, label):
    if Y.ndim != 2 or Y.shape != (100, 50000):
        raise SystemExit(f"{label}: shape {Y.shape} != (100, 50000)")
    if Y.dtype != np.uint16:
        raise SystemExit(f"{label}: dtype {Y.dtype} != uint16")
    if not np.all(np.isfinite(Y.astype(np.float64))):
        raise SystemExit(f"{label}: non-finite samples")
    return Y.astype(np.float64)


def load_traces(root, split, name, label):
    path = os.path.join(root, "inputs", split, f"traces{name}.mat")
    return check_traces(sio.loadmat(path)["tracesA"], label)


def decode_nonces(root, split, name):
    d = sio.loadmat(os.path.join(root, "inputs", split, f"nonces{name}.mat"))["noncesA"]
    b = d.astype(np.int64)
    w = b[:, 0::2] + 256 * b[:, 1::2]
    return np.where(w >= 32768, w - 65536, w)


def columns(b1, a0, a1, which):
    b1 = np.asarray(b1, dtype=np.int64)
    m1 = montgomery(a1 * b1).astype(np.int64)
    m0 = montgomery(a0 * b1).astype(np.int64)
    if which == "I":
        return np.ones((len(b1), 1), dtype=float)
    cols = [np.ones_like(b1), b1 / Q, (b1 < 0).astype(float),
            hw16(b1), hw16(b1 % Q), hw16(m1), hw16(m1 % Q)]
    extra = {"B": None, "A": hw16(m0), "C": hw16(m0 % Q),
             "W": hw16(montgomery(((a0 + 1) % Q) * b1).astype(np.int64))}[which]
    if extra is not None:
        cols.append(extra)
    return np.column_stack([np.asarray(c, dtype=float) for c in cols])


def rank_report(X, log, label):
    s = np.linalg.svd(X, compute_uv=False)
    thr = float(s[0]) * RANK_REL
    ok = bool(np.all(s > thr))
    log[label] = {"sigma_max": float(s[0]), "sigma_min": float(s[-1]),
                  "threshold": thr, "full_rank": ok}
    return ok


def fit(X, Y):
    W, *_ = np.linalg.lstsq(X, Y, rcond=None)
    return W


def per_point_mse(Xtr, Ytr, Xva, Yva):
    W = fit(Xtr, Ytr)
    R = Yva - Xva @ W
    return np.mean(R.astype(np.float64) ** 2, axis=0)


def freeze_dev(root, outdir):
    t0 = time.time()
    log = {"stage": "dev_freeze", "rank": {}}
    words = {n: decode_nonces(root, "development", n) for n in DEV}
    b1 = {n: words[n][:, 1] for n in DEV}
    cov = {}
    for n in DEV:
        vals, cnt = np.unique(b1[n], return_counts=True)
        cov[n] = {"distinct": int(len(vals)),
                  "within_file_repeats": int(np.sum(cnt > 1)),
                  "max_count": int(cnt.max()),
                  "a_constant": bool(len(set(words[n][:, 0])) == 1 and len(set(words[n][:, 3])) == 1),
                  "word2_eq_word5": bool(np.array_equal(words[n][:, 1], words[n][:, 4]))}
    cov["cross_dev_shared_b1"] = len(set(int(x) for x in b1["A99"]) & set(int(x) for x in b1["A199"]))
    a0, a1 = int(words["A99"][0, 0]), int(words["A99"][0, 3])
    if not (set(int(x) for x in words["A199"][:, 0]) == {a0} and
            set(int(x) for x in words["A199"][:, 3]) == {a1}):
        raise SystemExit("dev a0/a1 not constant across files")

    Y = {n: load_traces(root, "development", n, f"dev:{n}") for n in DEV}
    X = {n: {m: columns(b1[n], a0, a1, m) for m in ("B", "A", "C", "W")} for n in DEV}
    ok = True
    for n in DEV:
        for m in ("B", "A", "C", "W"):
            ok &= rank_report(X[n][m], log["rank"], f"{n}:{m}")
    if not ok:
        log["status"] = "stopped_rank_deficient_on_dev"
        return log

    dirs = {}
    for tr, va in (("A99", "A199"), ("A199", "A99")):
        dirs[f"{tr}->{va}"] = {m: per_point_mse(X[tr][m], Y[tr], X[va][m], Y[va])
                               for m in ("B", "A", "C")}
    gain = 0.5 * sum(dirs[d]["B"] - 0.5 * (dirs[d]["A"] + dirs[d]["C"]) for d in dirs)
    pt = int(np.argmax(gain))
    log.update({"sample_point": pt, "selection_gain": float(gain[pt]),
                "selection_per_direction": {
                    d: {m: float(dirs[d][m][pt]) for m in ("B", "A", "C")} for d in dirs}})
    if gain[pt] <= 0:
        log["status"] = "stopped_nonpositive_dev_gain"
        return log

    Xall = {m: columns(np.concatenate([b1[n] for n in DEV]), a0, a1, m)
            for m in ("I", "B", "A", "C", "W")}
    Yall = np.concatenate([Y[n] for n in DEV], axis=0)
    for m in ("I", "B", "A", "C", "W"):
        ok &= rank_report(Xall[m], log["rank"], f"pooled:{m}")
    if not ok:
        log["status"] = "stopped_rank_deficient_on_pooled"
        return log

    ycol = Yall[:, pt]
    coef = {}
    for m in ("I", "B", "A", "C", "W"):
        w = fit(Xall[m], ycol)
        coef[m] = [float(v) for v in w]
    art = {"sample_point": pt, "a0": a0, "a1": a1, "coefficients": coef,
           "b1_coverage": cov, "selection_gain": float(gain[pt])}
    p = os.path.join(outdir, "h001-frozen-dev.json")
    with open(p, "w") as f:
        json.dump(art, f, indent=2, ensure_ascii=False)
    log.update({"status": "dev_frozen", "frozen_artifact": p,
                "a_constant_ok": cov["A99"]["a_constant"] and cov["A199"]["a_constant"],
                "elapsed_s": round(time.time() - t0, 2)})
    return log


def load_public_b1(root):
    """Verify CSV hashes against the verification SHA256SUMS, then load."""
    sums_path = os.path.join(root, "verification/public-b1/SHA256SUMS")
    expected = {}
    with open(sums_path) as f:
        for line in f:
            h, name = line.split()
            expected[name] = h
    out, hashes = {}, {}
    for n in HOLD:
        name = f"b1_{n}.csv"
        p = os.path.join(root, "verification/public-b1", name)
        with open(p, "rb") as f:
            raw = f.read()
        h = hashlib.sha256(raw).hexdigest()
        if name not in expected or h != expected[name]:
            raise SystemExit(f"{name}: hash {h} != declared {expected.get(name)}")
        vals = np.array([int(x) for x in raw.split()], dtype=np.int64)
        if vals.shape != (100,):
            raise SystemExit(f"{name}: {vals.shape}")
        out[n], hashes[n] = vals, h
    return out, hashes


def holdout(root, outdir):
    t0 = time.time()
    frozen_path = os.path.join(outdir, "h001-frozen-dev.json")
    with open(frozen_path) as f:
        art = json.load(f)
    pt, a0, a1, coef = art["sample_point"], art["a0"], art["a1"], art["coefficients"]
    b1h, bh = load_public_b1(root)
    res = {"stage": "holdout", "frozen_dev_artifact": frozen_path,
           "sample_point": pt, "b1_sha256": bh, "per_file": {}}
    sse, n_rows = {}, {}
    for n in HOLD:
        Y = load_traces(root, "holdout", n, f"holdout:{n}")   # single read
        y = Y[:, pt]
        mse, s = {}, {}
        for m in ("I", "B", "A", "C", "W"):
            R = y - columns(b1h[n], a0, a1, m) @ np.asarray(coef[m])
            s[m] = float(np.sum(R ** 2))
            mse[m] = s[m] / len(y)
        sse[n], n_rows[n] = s, len(y)
        if mse["B"] == 0:
            res["per_file"][n] = {"qualification_failure": "B_mse_zero", "mse": mse}
            continue
        imp = {"A_vs_B": (mse["B"] - mse["A"]) / mse["B"],
               "A_vs_C": (mse["C"] - mse["A"]) / mse["B"],
               "A_vs_W": (mse["W"] - mse["A"]) / mse["B"]}
        res["per_file"][n] = {"mse": mse, "improvement": imp,
                              "gates_pass": bool(all(v >= GATE for v in imp.values()))}
    pooled = {}
    for m in ("I", "B", "A", "C", "W"):
        pooled[m] = sum(sse[n][m] for n in HOLD) / sum(n_rows[n] for n in HOLD)
    res["pooled_mse_sse_over_rows"] = pooled
    res["all_four_files_gate"] = bool(len(res["per_file"]) == 4 and
                                      all(v.get("gates_pass", False) for v in res["per_file"].values()))
    res["status"] = "holdout_complete"
    res["elapsed_s"] = round(time.time() - t0, 2)
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["freeze-dev", "holdout"], required=True)
    ap.add_argument("--root", default=os.getcwd())
    ap.add_argument("--outdir", default="sidechannel-results/h001")
    a = ap.parse_args()
    outdir = os.path.join(a.root, a.outdir)
    os.makedirs(outdir, exist_ok=True)
    out = freeze_dev(a.root, outdir) if a.mode == "freeze-dev" else holdout(a.root, outdir)
    p = os.path.join(outdir, f"h001-{a.mode}.json")
    with open(p, "w") as f:
        json.dump(out, f, indent=2)
    print(json.dumps(out, indent=2)[:3500])
    print("wrote", p)


if __name__ == "__main__":
    main()
