"""本批公共层：只读加载、去趋势、t 统计、通道读数。绝对路径统一由 PQC_ROOT 派生。"""
import os
import numpy as np
from scipy.io import loadmat
from scipy.stats import rankdata

PQC_ROOT = os.environ.get("PQC_ROOT", "/Users/dikaerdun/Documents/ChatGPT/侧信道分析/pqc-20261107-local")
FILES = [("development", a) for a in (99, 199)] + [("holdout", a) for a in (499, 599, 699, 799)]
CENT_B1, CENT_R10, CENT_R00 = 30703, 14356, 33141
Q = 3329

def load_all():
    bs, ts = [], []
    for grp, a in FILES:
        t = loadmat(f"{PQC_ROOT}/inputs/{grp}/tracesA{a}.mat")
        tk = [k for k in t if not k.startswith("__")][0]
        n = loadmat(f"{PQC_ROOT}/inputs/{grp}/noncesA{a}.mat")
        nk = [k for k in n if not k.startswith("__")][0]
        b = np.ascontiguousarray(n[nk]).reshape(-1, 12).view("<i2")
        assert b.shape[1] == 6
        bs.append(b.astype(np.int64)); ts.append(t[tk].astype(np.float64))
    return bs, ts

def detrend(Y):
    Y = np.asarray(Y, float); shp = Y.shape; n = shp[-1]
    z = (np.arange(n) - (n - 1) / 2) / n
    Z = np.column_stack([np.ones(n), z, z * z])
    A = np.linalg.pinv(Z).T
    Y2 = Y.reshape(-1, n)
    C = Y2 @ A
    return (Y2 - C @ Z.T).reshape(shp)

def tstat(y, x):
    """去趋势后 x 的 t 值（df=n-3），双精度。"""
    R = detrend(y.reshape(-1, 1))[:, 0]
    xd = detrend(x.reshape(-1, 1))[:, 0]
    sxx = xd @ xd
    if sxx <= 1e-12: return 0.0
    b = (xd @ R) / sxx
    res = R - b * xd
    df = len(R) - 3
    s2 = res @ res / df
    return float(b / np.sqrt(s2 / sxx))

def auc(x, y):
    r = rankdata(x); n1 = y.sum(); n0 = len(y) - n1
    return float((r[y == 1].sum() - n1 * (n1 + 1) / 2) / (n1 * n0))

def zread(tr, c, w=12):
    seg = tr[c - w:c + w]
    return (seg - seg.mean()) / (seg.std() + 1e-12)

def mont(a, b):
    t = (a * b) & 0xFFFF
    t = ((t ^ 0x8000) - 0x8000)
    m = (t * 3327) & 0xFFFF
    return ((t + m * Q) >> 16) & 0xFFFF, t

def hw(x):
    x = np.asarray(x, dtype=np.int64) & 0xFFFF
    return np.array([bin(int(v)).count("1") for v in x.ravel()]).reshape(x.shape)

def point(R, c, w=12):
    """R 为已去趋势的波形；取 c 处相对 ±w 局部均值的标量读数。"""
    return R[c] - R[c - w:c + w].mean()
