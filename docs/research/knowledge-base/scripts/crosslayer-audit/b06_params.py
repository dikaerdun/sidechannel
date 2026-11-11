"""B06：对齐位移 δ 与幅度增益 g 是否携带 b1 的额外信息。

每 trace 在 29816 附近 400 样本窗对文件均值模板做 ±20 搜索得 δ，窗内标准差比得 g。
基线 = y（29816 点读数）+ 文件固定效应；处理 = δ、g、二者。ΔR² 的 F 检验 + 200 次置换。
"""
import json
import numpy as np
from scipy.stats import f as fd
from common import load_all, detrend, point

bs, ts = load_all()
W, S = 200, 20
C = 29816
R = [detrend(t) for t in ts]
B = np.concatenate([b[:, 1] for b in bs])
FID = np.concatenate([[i] * len(b) for i, b in enumerate(bs)])
n = len(B)
Y, D, G = [], [], []
for fi in range(6):
    tpl = R[fi][:, C - W:C + W].mean(0)
    for r in R[fi]:
        Y.append(point(r, C))
        best = (-2, 0)
        for s in range(-S, S + 1):
            seg = r[C - W + s:C + W + s]
            c = np.corrcoef(seg, tpl)[0, 1]
            if c > best[0]: best = (c, s)
        D.append(best[1]); G.append(float(np.std(r[C - W:C + W]) / np.std(tpl)))
Y = np.array(Y); D = np.array(D, float); G = np.array(G)

def design(cols):
    return np.column_stack([np.ones(n), Y] + cols + [np.eye(6)[FID][:, 1:]])

def r2(X):
    beta, *_ = np.linalg.lstsq(X, B.astype(float), rcond=None)
    res = B - X @ beta
    return 1 - res @ res / ((B - B.mean()) @ (B - B.mean()))

r2b = r2(design([])); df2 = n - design([]).shape[1]
out = {"n": n, "r2_base": float(r2b), "delta_sd": float(D.std()), "gain_sd": float(G.std())}
def add(cols, name):
    rf = r2(design(cols)); k = len(cols)
    Fv = ((rf - r2b) / k) / ((1 - rf) / (df2 - k))
    rng = np.random.default_rng(20261111); null = []
    for _ in range(200):
        idx = np.concatenate([rng.permutation(np.where(FID == i)[0]) for i in range(6)])
        null.append(r2(design([c[idx] for c in cols])) - r2b)
    out[name] = {"dr2": float(rf - r2b), "p": float(fd.sf(Fv, k, df2 - k)),
                 "p_perm": float((np.array(null) >= (rf - r2b)).mean())}
add([D], "delta"); add([G], "gain"); add([D, G], "both")
# 参数自身与 b 的相关
out["corr_delta_b"] = float(np.corrcoef(D, B)[0, 1]); out["corr_gain_b"] = float(np.corrcoef(G, B)[0, 1])
print(json.dumps(out, indent=1))
