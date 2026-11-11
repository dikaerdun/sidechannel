"""E1' 序号分辨：同一相位在 43 个外层序号上分别估计，看效应是否只落在少数序号。
序号轴 = 无 ELF 时的代码位置代理。"""
import sys, json, os
import numpy as np, scipy.io as sio

ROOT = os.environ.get("PQC_ROOT", os.path.expanduser("~/Documents/ChatGPT/侧信道分析/pqc-20261107-local"))
OUT = os.path.dirname(os.path.abspath(__file__))
U = 1153          # 外层单元
NORD = 50000 // U  # 43

def split_of(t): return "development" if t in ("99", "199") else "holdout"
def load(tag, what):
    d = sio.loadmat(f"{ROOT}/inputs/{split_of(tag)}/{what}A{tag}.mat")
    a = d[[k for k in d if not k.startswith("__")][0]]
    return a.astype(np.float64) if what == "traces" else np.ascontiguousarray(a).view("<i2").reshape(100, 6).astype(np.int64)

def detrend(y):
    z = np.arange(y.shape[0], dtype=np.float64); Z = np.column_stack([np.ones_like(z), z, z * z])
    return y - Z @ (np.linalg.pinv(Z) @ y)

def tstat(col, b1):
    c = b1 - b1.mean(); r = detrend(col[:, None])[:, 0]
    tv = (r * c).sum() / max(np.sqrt((r ** 2).sum() * (c ** 2).sum()), 1e-12)
    return tv * np.sqrt((len(b1) - 4) / max(1 - tv ** 2, 1e-12))

def run(tag, sites):
    y = load(tag, "traces"); b1 = load(tag, "nonces")[:, 1].astype(np.float64)
    R = detrend(y)
    out = {}
    for tier in ("strong", "mid"):
        for s in sites[tier]:
            base = s % U
            cols = [base + U * j for j in range(NORD) if base + U * j < 50000]
            tv = np.array([tstat(R[:, c], b1) for c in cols])
            at = np.abs(tv)
            # 对照：随机 43 个绝对偏移的 max|t| 分布
            rng = np.random.default_rng(11)
            null = [np.abs([tstat(R[:, int(rng.integers(0, 49900))], b1) for _ in range(NORD)]).max() for _ in range(40)]
            # 逐序号剖面（供跨文件比对）
            out[f"{tier}_{s}"] = {"t": tv.tolist(), "n_gt3": int((at > 3).sum()),
                                  "top_ord": int(np.argmax(at)), "max_abs_t": float(at.max()),
                                  "median_abs_t": float(np.median(at)),
                                  "null_max_median": float(np.median(null)),
                                  "null_p90": float(np.percentile(null, 90))}
    return out

if __name__ == "__main__":
    sites = json.load(open(f"{OUT}/sites.json"))
    tag = sys.argv[sys.argv.index("--eval") + 1]
    r = {"tag": tag, "E1p": run(tag, sites)}
    json.dump(r, open(f"{OUT}/e1p_{tag}.json", "w"), indent=1)
    for k, v in r["E1p"].items():
        print(f"{k:11s} n_gt3={v['n_gt3']:2d} max|t|={v['max_abs_t']:.2f} med|t|={v['median_abs_t']:.2f} "
              f"top_ord={v['top_ord']} null_med={v['null_max_median']:.2f} null_p90={v['null_p90']:.2f}")
