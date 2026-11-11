"""设计集选址 + 复现文件判定。协议见 main/protocol-v1.md。

用法：
  python exp_selfref.py --design          # 仅 A99，写 sites.json
  python exp_selfref.py --eval 499        # 在复现文件上跑三候选
"""
import hashlib
import json
import os
import sys

import numpy as np
import scipy.io as sio

ROOT = os.environ.get("PQC_ROOT", "/Users/dikaerdun/Documents/ChatGPT/侧信道分析/pqc-20261107-local")
TARGETS = ("sign_b1", "sign_r10", "sign_r00")
DEV = ("99", "199")
REPL = ("499", "599", "699", "799")
HERE = os.path.dirname(os.path.abspath(__file__))


def load(tag, what):
    split = "development" if tag in DEV else "holdout"
    d = sio.loadmat(f"{ROOT}/inputs/{split}/{what}A{tag}.mat")
    a = d[f"{what}A"]
    if what == "nonces":
        return np.ascontiguousarray(a).view("<i2").reshape(-1, 6).astype(np.int64)
    return np.asarray(a, dtype=np.float64)


def prep(tag):
    y = load(tag, "traces")
    n = load(tag, "nonces")
    z = np.arange(y.shape[0], dtype=np.float64)
    Z = np.column_stack([np.ones_like(z), z, z * z])
    R = y - Z @ (np.linalg.pinv(Z) @ y)
    tgt = {"sign_b1": (n[:, 1] > 0), "sign_r10": (n[:, 2] > 0), "sign_r00": (n[:, 5] > 0)}
    return R, n, tgt


def tvec(R, lab):
    c = lab.astype(np.float64)
    c = c - c.mean()
    tv = (R * c[:, None]).sum(0) / np.maximum(np.sqrt((R ** 2).sum(0) * (c ** 2).sum()), 1e-12)
    return tv * np.sqrt((R.shape[0] - 4) / np.maximum(1 - tv ** 2, 1e-12))


def auc(score, lab):
    o = np.argsort(score, kind="stable")
    r = np.empty(len(score))
    r[o] = np.arange(1, len(score) + 1)
    p = lab
    npos, nneg = p.sum(), (~p).sum()
    return (r[p].sum() - npos * (npos + 1) / 2) / (npos * nneg)


def aucmap(R, lab):
    """逐样本 AUC：等价于用该样本排序 + Mann-Whitney。向量化。"""
    n = R.shape[0]
    order = np.argsort(R, axis=0, kind="stable")            # 每个样本一列
    rank = np.empty_like(order)
    idx = np.arange(n)[:, None]
    rank[order, np.arange(R.shape[1])[None, :]] = np.broadcast_to(idx + 1, order.shape)
    p = lab[:, None]
    npos, nneg = p.sum(), (~p).sum()
    return (rank[p[:, 0]].sum(0) - npos * (npos + 1) / 2) / (npos * nneg)


def region(amap, center, thr=0.95):
    if amap[center] < thr:
        return center, center
    lo = center
    while lo > 0 and amap[lo - 1] >= thr:
        lo -= 1
    hi = center
    while hi < len(amap) - 1 and amap[hi + 1] >= thr:
        hi += 1
    return lo, hi


def design():
    R, n, tgt = prep("99")
    out = {}
    for k in TARGETS:
        am = aucmap(R, tgt[k])
        tv = tvec(R, tgt[k])
        p = int(np.abs(tv).argmax())
        lo, hi = region(am, p)
        c = int(round((lo + hi) / 2))
        out[k] = {"center": c, "region": [int(lo), int(hi)], "width": int(hi - lo + 1),
                  "copy": c // 1153, "phase": c % 1153, "t_design": float(tv[p]),
                  "auc_design": float(am[c]), "argmax": p}
        print(f"  {k}: argmax {p} |t| {abs(tv[p]):.2f} region [{lo},{hi}] w={hi-lo+1} center {c} copy {c//1153} auc_center {am[c]:.3f}")
    out["_sha_note"] = "frozen on development/A99 only"
    json.dump(out, open(os.path.join(HERE, "sites.json"), "w"), indent=1)
    h = hashlib.sha256(open(os.path.join(HERE, "sites.json"), "rb").read()).hexdigest()
    open("main/sites.sha256", "w").write(h + "\n")
    print("sites sha256", h)


def eval_tag(tag, S):
    R, n, tgt = prep(tag)
    b1 = n[:, 1]
    res = {"tag": tag, "min": float(load(tag, "traces").min()), "max": float(load(tag, "traces").max())}

    # --- H013
    h13 = {}
    for k in TARGETS:
        c = S[k]["center"]
        am = aucmap(R, tgt[k])
        lo, hi = region(am, c)
        d_lo, d_hi = S[k]["region"]
        inter = max(0, min(hi, d_hi) - max(lo, d_lo) + 1)
        union = max(hi, d_hi) - min(lo, d_lo) + 1
        cross = {}
        for k2 in TARGETS:
            if k2 != k:
                cross[k2] = float(auc(R[:, c], tgt[k2]))
        strata = []
        q = np.argsort(np.argsort(b1))
        for s in range(4):
            m = (q * 4 // len(b1)).clip(0, 3) == s
            strata.append(float(auc(R[m, c], tgt[k][m])))
        same_copy = (c // 1153) == S[k]["copy"] and abs(c - S[k]["center"]) <= 400
        h13[k] = {"center": c, "own_auc": float(auc(R[:, c], tgt[k])), "t": float(tvec(R, tgt[k])[c]),
                  "region": [int(lo), int(hi)], "jaccard": inter / union if union else 0.0,
                  "same_copy_near": bool(same_copy), "cross_auc": cross, "strata_auc": strata}
    res["H013"] = h13

    # --- H014 歧义集
    r10 = n[:, 2]
    c = S["sign_r10"]["center"]
    yv = R[:, c]
    hw = np.zeros_like(r10)
    for j in range(16):
        hw += (r10 >> j) & 1
    # 设计拟合（读到 sites.json 同目录的 fit）
    fit = json.load(open(os.path.join(HERE, "h014_fit.json")))
    hhat = np.clip(np.round((yv - fit["a"]) / fit["b"]), 0, 16).astype(int)
    thr = fit["thr"]
    sign_hat = yv > thr
    sign_true = r10 > 0
    pools = {}
    for v, h in zip(r10, hw):
        pools.setdefault(int(h), []).append(int(v))
    sizes, hit = [], []
    for i in range(len(r10)):
        cand = [v for v in pools.get(int(hhat[i]), []) if (v > 0) == bool(sign_hat[i])]
        if not cand:
            cand = [v for v in pools.get(int(hhat[i]), [])]
        hit.append(int(r10[i]) in cand)
        sizes.append(len(cand))
    res["H014"] = {"center": c, "sign_acc": float((sign_hat == sign_true).mean()),
                   "median_set": float(np.median(sizes)), "hit_rate": float(np.mean(hit)),
                   "hw_corr": float(np.corrcoef(yv, hw)[0, 1])}

    # 错配对照
    cm = c + 500
    yv2 = R[:, cm]
    h2 = np.clip(np.round((yv2 - fit["a"]) / fit["b"]), 0, 16).astype(int)
    s2 = yv2 > thr
    sizes2, hit2 = [], []
    for i in range(len(r10)):
        cand = [v for v in pools.get(int(h2[i]), []) if (v > 0) == bool(s2[i])]
        if not cand:
            cand = [v for v in pools.get(int(h2[i]), [])]
        hit2.append(int(r10[i]) in cand)
        sizes2.append(len(cand))
    res["H014_mismatch"] = {"center": cm, "sign_acc": float((s2 == sign_true).mean()),
                            "median_set": float(np.median(sizes2)), "hit_rate": float(np.mean(hit2))}

    # --- H015 局部基线差分 + 增益归一
    p = c
    q = max(0, p - 200)
    s_i = R.std(1)
    d = (R[:, p] - R[:, q]) / s_i
    t_single = abs(float(tvec(R, tgt["sign_r10"])[p]))
    r_d = np.corrcoef(d, tgt["sign_r10"].astype(float))[0, 1]
    t_d = abs(r_d * np.sqrt(96 / max(1 - r_d ** 2, 1e-12)))
    res["H015"] = {"single_t": t_single, "ratio_t": t_d, "ratio": t_d / t_single}

    # --- 对照
    rng = np.random.default_rng(20261111)
    base = S["sign_r10"]["copy"] * 1153
    rnd = [float(np.mean([auc(R[:, base + int(o)], tgt[k]) for k in TARGETS])) for o in rng.integers(50, 1100, 20)]
    res["ctrl_random_auc_mean"] = float(np.mean(rnd))
    res["ctrl_null_maxabsT"] = [float(np.abs(tvec(R, rng.permutation(tgt["sign_r10"]))).max()) for _ in range(10)]
    return res


def main():
    if "--design" in sys.argv:
        design()
        return
    S = json.load(open(os.path.join(HERE, "sites.json")))
    if "--fit" in sys.argv:
        R, n, tgt = prep("99")
        c = S["sign_r10"]["center"]
        yv = R[:, c]
        hw = np.zeros_like(n[:, 2])
        for j in range(16):
            hw += (n[:, 2] >> j) & 1
        A = np.column_stack([np.ones(len(hw)), hw.astype(float)])
        coef = np.linalg.lstsq(A, yv, rcond=None)[0]
        thr = (yv[n[:, 2] > 0].mean() + yv[n[:, 2] <= 0].mean()) / 2
        json.dump({"a": float(coef[0]), "b": float(coef[1]), "thr": float(thr)},
                  open(os.path.join(HERE, "h014_fit.json"), "w"), indent=1)
        print("fit", coef, "thr", thr, "corr", np.corrcoef(yv, hw)[0, 1])
        return
    for tag in sys.argv[sys.argv.index("--eval") + 1:]:
        print(json.dumps(eval_tag(tag, S), indent=1))


if __name__ == "__main__":
    main()
