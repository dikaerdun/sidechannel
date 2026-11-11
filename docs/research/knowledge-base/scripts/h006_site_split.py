"""H006/H007/H008 主实验。协议 v1 + v2 修正。

冷判据只含截距+单列（H006）；控判据用行号二次趋势+全局电平（H007/H008）。
只有 --confirm 才打开 A699/A799。
"""
import json
import os
import sys
import numpy as np
import scipy.io as sio

ROOT = os.environ.get("PQC_ROOT", os.path.expanduser("~/Documents/ChatGPT/侧信道分析/pqc-20261107-local"))
Q = 3329
QINV = -3327
LUT = np.array([bin(i).count("1") for i in range(65536)], dtype=np.float64)


def load(split, tag):
    dt = sio.loadmat(f"{ROOT}/inputs/{split}/tracesA{tag}.mat")
    tr = np.asarray(dt[[x for x in dt if not x.startswith("__")][0]], dtype=np.float64)
    d = sio.loadmat(f"{ROOT}/inputs/{split}/noncesA{tag}.mat")
    k = [x for x in d if not x.startswith("__")][0]
    n = np.ascontiguousarray(d[k]).view("<i2").reshape(100, 6).astype(np.int64)
    return tr, n


def hw(x):
    return LUT[np.asarray(x, np.int64) & 0xFFFF]


def mont(a, b):
    t = np.asarray(a, np.int64) * np.asarray(b, np.int64)
    t16 = ((t & 0xFFFF) ^ 0x8000) - 0x8000
    m = ((t16 * QINV) & 0xFFFF).astype(np.int64)
    m16 = (m ^ 0x8000) - 0x8000
    return ((t - Q * m16) >> 16).astype(np.int64), m16


def cols(n):
    a0, b1, _, a1, _, _ = [n[:, i] for i in range(6)]
    f, m = mont(a0, b1)
    x = a0 * b1
    return dict(a0=a0, a1=a1, b1=b1, final=f, m=m, lo=hw(x & 0xFFFF), hi=hw((x >> 16) & 0xFFFF),
                hw_b1=hw(b1), sign=(b1 < 0).astype(np.float64), sign_r00=(n[:, 5] < 0).astype(np.float64))


def ols(y, X):
    X = np.column_stack([np.ones(len(y)), X])
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    r = y - X @ beta
    ss = float(r @ r)
    return beta, ss, len(y) - X.shape[1], X


def t_of(y, X, col):
    """把 col 追加到 X，返回该列的 t 与 ΔR²。"""
    b0, ss0, _, _ = ols(y, X)
    b1v, ss1, dof, XF = ols(y, np.column_stack([X, col]))
    s2 = ss1 / dof
    cov = s2 * np.linalg.inv(XF.T @ XF)
    se = np.sqrt(max(cov[-1, -1], 0.0))
    t = float(b1v[-1] / se) if se > 0 else np.nan
    tot = float(((y - y.mean()) ** 2).sum())
    return t, (ss0 - ss1) / tot if tot > 0 else np.nan


def cold(y, col):
    b, ss, dof, X = ols(y, np.asarray(col, float)[:, None])
    s2 = ss / dof
    se = np.sqrt(max((s2 * np.linalg.inv(X.T @ X))[-1, -1], 0.0))
    tot = float(((y - y.mean()) ** 2).sum())
    return (float(b[-1] / se) if se > 0 else np.nan), (1.0 - ss / tot) if tot > 0 else np.nan


def ctrl(tr, quiet):
    i = np.arange(len(tr), dtype=np.float64)
    z = (i - i.mean()) / i.std()
    return np.column_stack([z, z ** 2, tr[:, quiet].mean(axis=1)])


def pick(dev):
    acc = [np.zeros(50000), np.zeros(50000)]
    for tr, nn in dev:
        c = cols(nn)
        y = tr - tr.mean(0, keepdims=True)
        for j, key in enumerate(("sign", "final")):
            a = np.asarray(c[key], dtype=np.float64)
            a = a - a.mean()
            num = np.sum(y * a[:, None], axis=0)
            den = np.maximum(np.sqrt(np.sum(y ** 2, axis=0) * np.sum(a ** 2)), 1e-12)
            acc[j] += num / den
    rs, rf = acc[0] / len(dev), acc[1] / len(dev)
    ps = int(np.argmax(np.abs(rs)))
    rf2 = rf.copy(); rf2[max(0, ps - 200):ps + 200] = 0
    return ps, int(np.argmax(np.abs(rf2))), rs, rf


def analyze(split, tag, ps, pf, quiet):
    tr, n = load(split, tag)
    c = cols(n)
    K = ctrl(tr, quiet)
    out = {"file": tag, "sat": [int(tr.min()), int(tr.max())]}
    for name, s in (("P_sign", ps), ("P_final", pf)):
        y = tr[:, s]
        r = {}
        r["cold_t_sign"], r["cold_R2_sign"] = cold(y, c["sign"])
        r["cold_t_final"], r["cold_R2_final"] = cold(y, c["final"])
        r["ratio_sign_over_final"] = abs(r["cold_t_sign"]) / max(abs(r["cold_t_final"]), 1e-9)
        r["ratio_final_over_sign"] = abs(r["cold_t_final"]) / max(abs(r["cold_t_sign"]), 1e-9)
        r["collin_sign_final"] = float(np.corrcoef(c["sign"], c["final"])[0, 1])
        r["collin_sign_hwb1"] = float(np.corrcoef(c["sign"], c["hw_b1"])[0, 1])
        r["ctrl_t_sign"] = t_of(y, K, c["sign"])[0]
        r["ctrl_t_sign_wrong"] = t_of(y, K, c["sign_r00"])[0]
        r["cold_t_m"] = t_of(y, np.column_stack([c["final"]]), c["m"])[0]
        r["cold_dR2_m"] = t_of(y, np.column_stack([c["final"]]), c["m"])[1]
        r["cold_t_lo"] = t_of(y, np.column_stack([c["final"]]), c["lo"])[0]
        r["cold_dR2_lo"] = t_of(y, np.column_stack([c["final"]]), c["lo"])[1]
        r["cold_t_hi"] = t_of(y, np.column_stack([c["final"]]), c["hi"])[0]
        r["cold_t_W_wrongbind"] = cold(y, hw(mont((c["a0"] + 1) % Q, c["b1"])[0]))[0]
        # 配对（描述性）
        idx = {}
        for i, v in enumerate(c["b1"]):
            idx.setdefault(abs(int(v)), []).append(i)
        pairs = [(a_, b_) for ids in idx.values()
                 for a_ in [i for i in ids if c["b1"][i] > 0]
                 for b_ in [i for i in ids if c["b1"][i] < 0]]
        r["pair_n"] = len(pairs)
        if len(pairs) > 2:
            dif = np.array([y[b_] - y[a_] for a_, b_ in pairs])
            r["pair_mean"] = float(dif.mean())
            r["pair_t"] = float(dif.mean() / (dif.std(ddof=1) / np.sqrt(len(dif))))
        r["ctx_r_sign"] = float(np.corrcoef(K[:, 2], c["sign"])[0, 1])
        out[name] = r
    return out


def main():
    out = {"protocol_sha256": ["60186559d76f8d8f8851fb2c76f55323ba475ad3fe47da374d039184f36f2091"],
           "amend_sha256": ["__AMEND__"]}
    dev = [load("development", t) for t in ("99", "199")]
    quiet = np.argsort(np.vstack([d[0] for d in dev]).std(0))[:20]
    ps, pf, rs, rf = pick(dev)
    out["P_sign"], out["P_final"] = ps, pf
    out["sel_r"] = {"sign_at_sign": float(rs[ps]), "final_at_final": float(rf[pf]),
                    "sign_at_final": float(rs[pf]), "final_at_sign": float(rf[ps])}
    out["dev"] = {t: analyze("development", t, ps, pf, quiet) for t in ("99", "199")}
    if "--confirm" in sys.argv:
        out["confirm"] = {t: analyze("holdout", t, ps, pf, quiet) for t in ("699", "799")}
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
