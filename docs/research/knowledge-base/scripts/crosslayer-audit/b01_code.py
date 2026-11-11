"""B01：三位离散码的可分性、码字分布与信息上限。

码字 = (sign b1, sign r10, sign r00)。报：码字数、格大小（命中集）、互信息上界、
分半 BER（A 半定每通道阈值，B 半出码字）、以及“只按码字命中”的残余候选数。
"""
import json
import numpy as np
from common import load_all, detrend, point

bs, ts = load_all()
R = [detrend(t) for t in ts]
RD = np.concatenate([np.array([point(r, c) for r in R[fi]]) for fi, c in [(i, 0) for i in range(6)]])
B = np.concatenate([b[:, 1] for b in bs]); R10 = np.concatenate([b[:, 2] for b in bs])
R00 = np.concatenate([b[:, 5] for b in bs])
FID = np.concatenate([[i] * len(b) for i, b in enumerate(bs)])
def code(x): return (x > 0).astype(int)
CW = code(B) * 4 + code(R10) * 2 + code(R00)
uniq = np.unique(B)
cells = {c: uniq[np.isin(uniq, B[CW == c])] for c in range(8)}
sizes = np.array([len(v) for v in cells.values() if len(v)])
p = sizes / sizes.sum()
out = {"uniq_b": int(len(uniq)), "codewords_nonempty": int(len(sizes)), "cell_mean": float(sizes.mean()),
       "cell_max": int(sizes.max()), "cell_min": int(sizes.min()),
       "mi_bits": float(-(p * np.log2(p)).sum()), "full_range": 3321}

# 分半 BER：每文件随机两半，A 半按通道定阈值（中位数），B 半出码字
rng = np.random.default_rng(20261111); ber = []
for _ in range(200):
    A, Bh = [], []
    for fi in range(6):
        idx = np.where(FID == fi)[0]; rng.shuffle(idx)
        A.append(idx[:50]); Bh.append(idx[50:])
    A = np.concatenate(A); Bh = np.concatenate(Bh)
    bits = []
    for c, lab in ((29816, code(B)), (16456, code(R10)), (33384, code(R00))):
        y = np.concatenate([np.array([point(r, c) for r in R[fi]]) for fi in range(6)])
        m0, m1 = y[A][lab[A] == 0].mean(), y[A][lab[A] == 1].mean()
        thr = (m0 + m1) / 2
        pred = (y[Bh] > thr).astype(int) if m1 > m0 else (y[Bh] < thr).astype(int)
        bits.append(np.mean(pred != lab[Bh]))
    ber.append(float(np.mean(bits)))
out["ber_mean"] = float(np.mean(ber)); out["ber_max"] = float(np.max(ber))

# 命中抑制：真值的码字格大小 vs 随机猜的期望
out["hit_cell_mean"] = float(np.mean([len(cells[c]) for c in CW]))
out["hit_cell_median"] = float(np.median([len(cells[c]) for c in CW]))
out["frac_hit_le_65"] = float(np.mean([len(cells[c]) <= 65 for c in CW]))
print(json.dumps(out, indent=1))
