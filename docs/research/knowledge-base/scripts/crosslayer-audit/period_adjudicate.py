"""周期裁决：不预设格点，直接用副本间互相关测间距。

对每条 trace：在包络上取第 0 副本的模板窗，对 k=1..11 在 k*68±12 内搜最大相关，
得到 lag_k；再稳健拟合 lag_k = a + P*k。若 P≈68 且 11P≈748，则 1156 只是 17 个基周期。
同时报 raw/envelope 在 68/340/544/5780 处的自相关符号，解释核验方的 ±0.5/−0.23。
"""
import json
import numpy as np
from scipy.signal import find_peaks
from common import load_all

WIN, SEARCH = 40, 12
bs, ts = load_all()
rows = []
for fi in (0, 1, 2, 3):
    for ti, tr in enumerate(ts[fi][:25]):
        d = np.abs(np.diff(tr)); e = np.convolve(d, np.ones(32) / 32, mode="same")
        e = e - np.convolve(e, np.ones(201) / 201, mode="same")
        seg0 = e[600:4000]
        if len(seg0) < 100: continue
        a0 = 600 + int(np.argmax(seg0)); tpl = e[a0 - WIN:a0 + WIN]
        lags, rs = [], []
        for k in range(1, 12):
            best, bl = -2, None
            for lag in range(k * 68 - SEARCH, k * 68 + SEARCH + 1):
                if a0 + k * 68 + WIN + SEARCH >= len(e): break
                seg = e[a0 + lag - WIN:a0 + lag + WIN]
                if len(seg) < len(tpl): continue
                r = float(np.corrcoef(tpl, seg)[0, 1])
                if r > best: best, bl = r, lag
            if bl is not None: lags.append(bl); rs.append(best)
        if len(lags) < 8: continue
        k = np.arange(1, len(lags) + 1)
        P = float(np.polyfit(k, np.array(lags, float), 1)[0])
        res = np.array(lags, float) - (np.mean(lags) - P * np.mean(k)) - P * k
        # 备择：等间距 1156 只在 k=17 时才有意义，这里同时给 68 的整数倍偏离
        rows.append(dict(file=fi, trace=ti, P=P, med_r=float(np.median(rs)),
                         lag11=int(lags[-1]), drift=float(lags[-1] - 11 * 68),
                         resid=float(np.std(res))))

Ps = np.array([r["P"] for r in rows])
out = {"n": len(rows), "P_median": float(np.median(Ps)), "P_q25": float(np.percentile(Ps, 25)),
       "P_q75": float(np.percentile(Ps, 75)), "P_min": float(Ps.min()), "P_max": float(Ps.max()),
       "lag11_median": float(np.median([r["lag11"] for r in rows])),
       "drift_median": float(np.median([r["drift"] for r in rows])),
       "resid_median": float(np.median([r["resid"] for r in rows])),
       "med_r_median": float(np.median([r["med_r"] for r in rows])),
       "frac_within_1_of_68": float(np.mean(np.abs(Ps - 68) <= 1.0))}
# raw vs envelope 自相关符号
tr = ts[1][0]; d = np.abs(np.diff(tr)); e = np.convolve(d, np.ones(32) / 32, mode="same")
def ac(v, lag):
    v = v - v.mean(); v = v / v.std(); return float(np.mean(v[:-lag] * v[lag:]))
out["ac"] = {str(l): {"raw": round(ac(tr, l), 3), "env": round(ac(e, l), 3)}
             for l in (68, 340, 544, 1156, 5780)}
print(json.dumps(out, indent=1))
