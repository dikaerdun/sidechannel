"""更正 H008 判据语义：协议 M5/V3-2 的“冷”= y ~ 1 + col，不含 final。

原 exp_h006.py 的 cold_t_m 实为 y ~ 1 + final + col（条件模型），名实不符。
本脚本同时给两版，确认 H008 按协议应判不通过。
只读，不重跑确认数据选择，不改选点。
"""
import json
import os
import numpy as np
import scipy.io as sio
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from h006_site_split import load, cols, cold, t_of  # noqa: E402

PS, PF = 30705, 14559
out = {}


def run(split, tag):
    tr, n = load(split, tag)
    c = cols(n)
    r = {}
    for name, s in (("P_sign", PS), ("P_final", PF)):
        y = tr[:, s]
        d = {}
        for key in ("m", "lo", "hi"):
            d[f"cold_{key}_R2"] = cold(y, c[key])[1]
            d[f"cold_{key}_t"] = cold(y, c[key])[0]
            d[f"cond_{key}_t"] = t_of(y, np.column_stack([c["final"]]), c[key])[0]
            d[f"cond_{key}_dR2"] = t_of(y, np.column_stack([c["final"]]), c[key])[1]
        r[name] = d
    return r


res = {}
for split, tags in (("development", ("99", "199")), ("holdout", ("699", "799"))):
    for t in tags:
        res[f"{split}/{t}"] = run(split, t)
out["by_file"] = res
out["verdict_H008_cold"] = {
    k: all(abs(v[p][f"cold_{x}_t"]) < 2 and v[p][f"cold_{x}_R2"] < 0.01
           for p in ("P_final",) for x in ("m", "lo", "hi"))
    for k, v in res.items() if k.startswith("holdout")
}
print(json.dumps(out, indent=1))
