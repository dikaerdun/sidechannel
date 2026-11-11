"""B07/B02（修订）：副本中心先在开发集选点，再在留出集评估，避免圆心错位。

1) 每副本在名义中心 ±34 内，用开发集（A99/A199）选 |t| 最大的样本；记录选中偏移。
2) 用该点（±2 均值）在留出集（A499..A799）算 sign(b) AUC 与 |r|：无选择偏差的强度。
3) 留出集内做 y ~ 副本 + hw + 副本×hw 的 F 检验（B07 位置效应 / B02 状态相关增益）。
"""
import json
import numpy as np
from scipy.stats import f as fd, rankdata
from common import load_all, detrend, point, hw

bs, ts = load_all()
P = 67.83
NOM = [int(round(29816 - 11 * P + k * P)) for k in range(12)]
R = [detrend(t) for t in ts]
B1 = [b[:, 1] for b in bs]
DEV, HOLD = (0, 1), (2, 3, 4, 5)

def tstat(y, x):
    x = x - x.mean(); b = (x @ y) / (x @ x); res = y - b * x
    return abs(b / np.sqrt((res @ res) / (len(y) - 2) / (x @ x)))

def auc(x, y):
    r = rankdata(x); n1 = y.sum(); n0 = len(y) - n1
    return float((r[y == 1].sum() - n1 * (n1 + 1) / 2) / (n1 * n0))

per = []
for k, c in enumerate(NOM):
    best = (-1, 0)
    for s in range(c - 16, c + 17):
        y = np.concatenate([np.array([point(r, s) for r in R[fi]]) for fi in DEV])
        x = np.concatenate([B1[fi] for fi in DEV])
        t = tstat(y, x)
        if abs(t) > best[0]: best = (abs(t), s)
    sel = best[1]
    yh = np.concatenate([np.array([point(r, sel) for r in R[fi]]) for fi in HOLD])
    bh = np.concatenate([B1[fi] for fi in HOLD])
    per.append({"copy": k, "nominal": c, "sel": sel, "off": sel - c, "dev_t": float(best[0]),
                "hold_auc": auc(yh, (bh > 0).astype(int)), "hold_strength": max(auc(yh, (bh > 0).astype(int)), 1 - auc(yh, (bh > 0).astype(int))), "hold_absr": float(abs(np.corrcoef(yh, bh)[0, 1]))})

SEL = [p["sel"] for p in per]
Y, H, C = [], [], []
for fi in HOLD:
    for r in R[fi]:
        for k, s in enumerate(SEL):
            Y.append(point(r, s)); H.append(hw(np.array([B1[fi][0]]))[0] if False else None); C.append(k)
# H 需按行取值，重建
Y, H, C = [], [], []
for fi in HOLD:
    for i, r in enumerate(R[fi]):
        for k, s in enumerate(SEL):
            Y.append(point(r, s)); H.append(hw(np.array([B1[fi][i]]))[0]); C.append(k)
Y = np.array(Y); H = np.array(H, float); C = np.array(C)
Xc = np.column_stack([np.ones(len(Y)), np.eye(12)[C][:, 1:]])
Xa = np.column_stack([Xc, H])
Xi = np.column_stack([Xa] + [H * (C == k) for k in range(1, 12)])
def r2(X):
    beta, *_ = np.linalg.lstsq(X, Y, rcond=None); res = Y - X @ beta
    return 1 - res @ res / ((Y - Y.mean()) @ (Y - Y.mean()))
r2c, r2a, r2i = r2(Xc), r2(Xa), r2(Xi)
d2 = len(Y) - Xi.shape[1]
Fint = ((r2i - r2a) / 11) / ((1 - r2i) / d2)
Fmain = ((r2a - r2c) / 1) / ((1 - r2a) / (d2 + 11))
out = {"nominal_period": P, "per_copy": per, "offsets": [p["off"] for p in per],
       "offset_range": [int(min(p["off"] for p in per)), int(max(p["off"] for p in per))],
       "hold_auc_min": float(min(p["hold_auc"] for p in per)),
       "hold_auc_max": float(max(p["hold_auc"] for p in per)),
       "n_auc_ge_0.9": int(sum(p["hold_auc"] >= 0.9 for p in per)),
       "r2_copy": float(r2c), "r2_copy_hw": float(r2a), "r2_interact": float(r2i),
       "hw_main_p": float(fd.sf(Fmain, 1, d2 + 11)), "interact_p": float(fd.sf(Fint, 11, d2)),
       "n_hold": int(len(Y)), "all_file_r": [[float(np.corrcoef([point(r, s) for r in R[fi]], B1[fi])[0,1]) for s in [p["sel"] for p in per]] for fi in range(6)]}
print(json.dumps(out, indent=1))
