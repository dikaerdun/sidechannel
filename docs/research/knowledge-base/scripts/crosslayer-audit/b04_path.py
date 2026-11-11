"""B04：约减“丢掉”的整数轨迹是否有增量预测力。

对 4 个读数点 × 3 个目标（b1 两处、r10、r00）重复：池化 600 行、文件固定效应。
基线 = sign + hw 低字节 + hw 高字节 + hw16；处理 = 被丢弃的低半字 hw / 商高字 hw。
判据：ΔR² 的 F 检验 + 300 次文件内置换 null。sign 进/出基线各做一次敏感性。
注意：a 恒为 558/17，处理项都是目标的确定性函数；正结果只说明“非标准 HW 模型”。
"""
import json
import numpy as np
from scipy.stats import f as fd
from common import load_all, detrend, point, hw, Q

bs, ts = load_all()
NPERM = 200
B = {v: np.concatenate([b[:, v] for b in bs]).astype(np.int64) for v in (1, 2, 5)}
FID = np.concatenate([[i] * len(b) for i, b in enumerate(bs)])
A = np.concatenate([np.full(len(b), int(b[0, 0])) for b in bs])
n = len(FID)
R = [detrend(t) for t in ts]

def feats(v):
    """qraw = 被 16 位截断丢掉的乘积高字；m = 约减修正乘子（进位/修正轨迹）。"""
    p32 = A * v
    t16 = ((p32 & 0xFFFF) ^ 0x8000) - 0x8000
    m = (t16 * 3327) & 0xFFFF
    return (p32 >> 16) & 0xFFFF, m

def design(cols):
    return np.column_stack([np.ones(n)] + cols + [np.eye(6)[FID][:, 1:]])

def r2(X, y):
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    r = y - X @ beta
    return 1 - (r @ r) / ((y - y.mean()) @ (y - y.mean()))

def run(center, var, sign_in_base=True):
    Y = np.concatenate([np.array([point(r, center) for r in Rf]) for Rf in R])
    v = B[var]
    base = ([np.sign(v).astype(float)] if sign_in_base else []) + [
        hw(v & 0xFF).astype(float), hw((v >> 8) & 0xFF).astype(float), hw(v).astype(float)]
    low, hi = feats(v)
    r2b = r2(design(base), Y); df2 = n - design(base).shape[1]
    r2l = r2(design(base + [hw(low).astype(float)]), Y)
    r2h = r2(design(base + [hw(hi).astype(float)]), Y)
    r2c = r2(design(base + [hw(low).astype(float), hw(hi).astype(float)]), Y)
    def F(rf, k): return float(((rf - r2b) / k) / ((1 - rf) / (df2 - k)))
    rng = np.random.default_rng(20261111)
    T = hw(low).astype(float); null = []
    for _ in range(NPERM):
        idx = np.concatenate([rng.permutation(np.where(FID == i)[0]) for i in range(6)])
        null.append(r2(design(base + [T[idx]]), Y) - r2b)
    return {"center": center, "var": var, "sign_in_base": sign_in_base,
            "r2_base": float(r2b), "qraw_dr2": float(r2l - r2b), "qraw_p": float(fd.sf(F(r2l, 1), 1, df2 - 1)),
            "qraw_p_perm": float((np.array(null) >= (r2l - r2b)).mean()),
            "m_dr2": float(r2h - r2b), "m_p": float(fd.sf(F(r2h, 1), 1, df2 - 1)),
            "both_dr2": float(r2c - r2b), "both_p": float(fd.sf(F(r2c, 2), 2, df2 - 2)),
            "qraw_redundancy_r2": float(r2(design(base), T))}

out = {"n": n, "runs": [run(29816, 1), run(30563, 1), run(16456, 2), run(33384, 5),
                        run(29816, 1, False)],
       "note": "a 恒定；正结果只说明非标准 HW 模型，不证明独立路径自由度"}
print(json.dumps(out, indent=1))
