"""M1/M2/M3 判别实验。用法: python exp_paradigm.py --sites | python exp_paradigm.py --eval <tag>"""
import sys, json, os
import numpy as np, scipy.io as sio
from scipy.stats import rankdata

ROOT = os.environ.get("PQC_ROOT", os.path.expanduser("~/Documents/ChatGPT/侧信道分析/pqc-20261107-local"))
P, NU = 68, 50000 // 68
OUT = os.path.dirname(os.path.abspath(__file__))
W = 34

def split_of(tag):
    return "development" if tag in ("99", "199") else "holdout"

def load(tag, what):
    d = sio.loadmat(f"{ROOT}/inputs/{split_of(tag)}/{what}A{tag}.mat")
    a = d[[k for k in d if not k.startswith("__")][0]]
    return a.astype(np.float64) if what == "traces" else \
        np.ascontiguousarray(a).view("<i2").reshape(100, 6).astype(np.int64)

def detrend(y):
    z = np.arange(y.shape[0], dtype=np.float64)
    Z = np.column_stack([np.ones_like(z), z, z * z])
    return y - Z @ (np.linalg.pinv(Z) @ y)

def tstat(col, b1):
    c = b1 - b1.mean()
    r = detrend(col[:, None])[:, 0]
    tv = (r * c).sum() / max(np.sqrt((r ** 2).sum() * (c ** 2).sum()), 1e-12)
    return tv * np.sqrt((len(b1) - 4) / max(1 - tv ** 2, 1e-12))

def hw16(x):
    return np.array([bin(int(v) & 0xFFFF).count("1") for v in x], dtype=np.float64)

def s16(x):
    return ((np.asarray(x, np.int64) & 0xFFFF) ^ 0x8000) - 0x8000

def bitlen(x):
    return np.array([int(abs(v)).bit_length() for v in x], dtype=np.float64)

class Corr:
    """对固定 (R, REF) 预计算 9 点滑窗相关的全部中间量。"""
    def __init__(self, R, REF):
        def win(a):
            cs = np.concatenate([[0.0], np.cumsum(a)])
            return cs[9:] - cs[:-9]
        self.N = win(R * REF)
        self.A = win(R * R)
        self.B = win(REF * REF)
        csR = np.concatenate([[0.0], np.cumsum(R)]); csT = np.concatenate([[0.0], np.cumsum(REF)])
        mR = (csR[9:] - csR[:-9]) / 9.0; mT = (csT[9:] - csT[:-9]) / 9.0
        self.den = np.sqrt(np.maximum(self.A - 9 * mR ** 2, 1e-9) * np.maximum(self.B - 9 * mT ** 2, 1e-9))
        self.mR, self.mT = mR, mT
    def at(self, starts):
        s = np.clip(starts, 0, len(self.N) - 1)
        return (self.N[s] - 9 * self.mR[s] * self.mT[s]) / self.den[s]

def select_sites():
    y = load("199", "traces"); b1 = load("199", "nonces")[:, 1].astype(np.float64)
    R = detrend(y); c = b1 - b1.mean()
    tv = (R * c[:, None]).sum(0) / np.maximum(np.sqrt((R ** 2).sum(0) * (c ** 2).sum()), 1e-12)
    at = np.abs(tv); order = np.argsort(at)[::-1]; picked = []
    def take(plo, phi, n, sep=250):
        lo, hi = np.percentile(at, plo), np.percentile(at, phi)
        cand = [int(s) for s in order if lo <= at[s] <= hi and
                all(abs(s - q) > sep for q in picked)]
        got = []
        for s in cand:
            if all(abs(s - q) > sep for q in got):
                got.append(s)
                if len(got) == n: break
        picked.extend(got); return got
    sites = {"strong": take(99.8, 100.0, 3), "mid": take(98.0, 99.0, 3), "weak": take(92.0, 95.0, 3),
             "cold": [14559], "hot": [30705]}
    json.dump(sites, open(f"{OUT}/sites.json", "w"), indent=1)
    print(json.dumps(sites))
    print("|t|:", {k: [round(at[s], 2) for s in sites[k]] for k in ("strong", "mid", "weak", "cold", "hot")})

def gen_jitter(rng, level):
    d = np.zeros(NU); cur = 0.0
    for k in range(NU):
        cur += 0.0 if level == 0 else (rng.choice([-1, 0, 1], p=[1/6, 2/3, 1/6]) if level == 1 else rng.choice([-1, 1]))
        d[k] = np.clip(cur, -W, W)
    return d.astype(int)

def arm(Rt, p, delta, mode, ref) -> float:
    base = p + P * np.arange(NU) + delta
    ok = (base - W - 6 >= 0) & (base + W + 12 < 50000)
    base, kk = base[ok], np.arange(NU)[ok]
    if mode == "single":  return Rt[base[0]]
    if mode == "boxcar":  return Rt[(base - W).clip(0) [:, None] + np.arange(2 * W + 1)].mean()
    if mode == "comb":    return Rt.base if False else Rt[base].mean()
    cc = Corr(Rt, ref)
    est = np.array([ (lambda st: st[int(np.nanargmax(cc.at(st)))]) (np.arange(b - W, b + W + 1)) for b in base ])
    fine = np.array([ (lambda st: st[int(np.nanargmax(cc.at(st)))]) (np.arange(e - 3, e + 4)) for e in est ])
    dhat = fine - base
    if mode == "align_shuf":
        dhat = np.random.default_rng(7).permutation(dhat)
    return Rt[(base + dhat).astype(int)].mean()

def run_e1(tag, sites, rng):
    y = load(tag, "traces"); b1 = load(tag, "nonces")[:, 1].astype(np.float64)
    R = detrend(y); REF = (R.sum(0) - R) / (R.shape[0] - 1)
    LOC = np.stack([np.convolve(r, np.ones(5) / 5, mode="same") for r in R])
    modes = ["single", "boxcar", "comb", "align_ext", "align_loc", "align_shuf"]
    res = {}; a0 = {}
    for level, name in ((0, "L0"), (1, "L1"), (3, "L3")):
        dj = np.stack([gen_jitter(rng, level) for _ in range(100)])
        for tier in ("strong", "mid", "weak"):
            for s in sites[tier]:
                for m in modes:
                    v = np.array([arm(R[i], s, dj[i], m, REF[i] if m != "align_loc" else LOC[i]) for i in range(100)])
                    res.setdefault(m, {}).setdefault(name, {}).setdefault(tier, []).append(float(tstat(v, b1)))
        if level in (1, 3):
            cs = []
            for i in range(100):
                s = sites["strong"][0]; b = s + P * np.arange(NU) + dj[i]
                ok = (b - W - 6 >= 0) & (b + W + 12 < 50000); b = b[ok]
                cc = Corr(R[i], REF[i])
                est = np.array([(lambda st: st[int(np.nanargmax(cc.at(st)))]) (np.arange(q - W, q + W + 1)) for q in b])
                cs.append(np.corrcoef(est - b, dj[i][ok])[0, 1])
            a0[name] = float(np.nanmedian(cs))
    return {"t": res, "a0_corr": a0}

def run_m2(tag, sites, rng):
    y = load(tag, "traces"); b1 = load(tag, "nonces")[:, 1].astype(np.float64)
    R = detrend(y); cls = (b1 < 0).astype(int)
    res = []
    for s in sites["strong"] + sites["mid"]:
        p0 = max(0, s - W)
        nu = (49999 - p0 - 67) // P + 1
        prof = np.stack([np.median(R[:, p0 + u + P * np.arange(nu)], 1) for u in range(68)], 1)
        sh = (prof - prof.mean(1, keepdims=True)) / prof.std(1, keepdims=True)
        sc = prof.mean(1)
        def loo_auc(F):
            F = F.reshape(100, -1); s_ = np.empty(100)
            for i in range(100):
                m = np.stack([F[cls == c].mean(0) for c in (0, 1)])
                s_[i] = np.linalg.norm(F[i] - m[0]) - np.linalg.norm(F[i] - m[1])
            rk = rankdata(s_); n1 = cls.sum(); n0 = 100 - n1
            return float((rk[cls == 1].sum() - n1 * (n1 + 1) / 2) / (n1 * n0))
        sup = sh > np.percentile(sh, 75, axis=1, keepdims=True)
        jac = lambda a, b: (a & b).sum() / max((a | b).sum(), 1)
        inter = jac(sup[cls == 0].mean(0) > .5, sup[cls == 1].mean(0) > .5)
        intra = [jac(sup[a], sup[b]) for c in (0, 1)
                 for a, b in (rng.choice(np.where(cls == c)[0], 2, replace=False) for _ in range(20))]
        m0, m1 = sh[cls == 0].mean(0), sh[cls == 1].mean(0)
        res.append({"site": int(s), "jaccard": float(inter), "intra_jac": float(np.median(intra)),
                    "auc_shape": loo_auc(sh), "auc_scale": loo_auc(np.repeat(sc[:, None], 68, 1)),
                    "cos": float(m0 @ m1 / (np.linalg.norm(m0) * np.linalg.norm(m1)))})
    return res

def run_m3(tag, sites):
    y = load(tag, "traces"); b1 = load(tag, "nonces")[:, 1].astype(np.float64)
    R = detrend(y); t = 558 * b1
    H, D = hw16(t), 16 - bitlen(s16(t))
    out = {}
    for name in ("cold", "hot"):
        s = sites[name][0]; col = R[:, s]
        def fit(cols):
            M = np.column_stack([np.ones(100)] + cols); beta, *_ = np.linalg.lstsq(M, col, rcond=None)
            r_ = col - M @ beta; s2 = (r_ ** 2).sum() / (100 - M.shape[1])
            se = np.sqrt(np.diag(s2 * np.linalg.pinv(M.T @ M)))[1:]
            return beta[1:], beta[1:] / se, 1 - (r_ ** 2).sum() / ((col - col.mean()) ** 2).sum()
        _, tH, rH = fit([H]); _, tD, rD = fit([D]); bJ, tJ, _ = fit([H, D])
        out[name] = {"t_HW": tH.tolist(), "t_red": tD.tolist(), "R2_HW": rH, "R2_red": rD,
                     "t_joint": tJ.tolist(), "sign_HW": float(np.sign(bJ[0])), "sign_red": float(np.sign(bJ[1]))}
    out["sym_corr_neg_pos"] = {n: [float(np.corrcoef(np.abs(t[m]), R[m, sites[n][0]])[0, 1])
                                   for m in (b1 < 0, b1 > 0)] for n in ("cold", "hot")}
    return out

if __name__ == "__main__":
    rng = np.random.default_rng(20261111)
    if "--sites" in sys.argv:
        select_sites()
    else:
        tag = sys.argv[sys.argv.index("--eval") + 1]
        sites = json.load(open(f"{OUT}/sites.json"))
        r = {"tag": tag, "E1": run_e1(tag, sites, rng), "M2": run_m2(tag, sites, rng), "M3": run_m3(tag, sites)}
        json.dump(r, open(f"{OUT}/raw_{tag}.json", "w"), indent=1)
        print(tag, "a0_corr", r["E1"]["a0_corr"])
        for m, byL in r["E1"]["t"].items():
            print(f"  {m:11s}", {L: {k: [round(x, 2) for x in v] for k, v in d.items()} for L, d in byL.items()})
