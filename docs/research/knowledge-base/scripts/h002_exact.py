#!/usr/bin/env python3
"""EXP-20261107-02 / PQC-H002 v1 -- exact rational enumeration (no waveforms).

Published copy. Set H002_OUTDIR to choose the output directory (default: cwd).

Frozen protocol (SHA-256
cc4eac9f9ab2ccbb1ca858ee031ea4527b8b22e187413a439af29339ef8d4fe9).

All posteriors and expectations are exact Fractions; only natural logs are
float64. MAP ties -> smallest S. Nothing here is fitted to any data.
"""
import argparse
import json
import math
import os
import sys
from fractions import Fraction as F

Q = 7
SSET = list(range(Q))          # S in {0..6}, uniform
BSET = list(range(1, Q))       # B in {1..6}, uniform, independent of S
PRIOR_S = F(1, Q)
PRIOR_B = F(1, len(BSET))

# error-pair tables, order (E1,E2) = 00,01,10,11
TABLES = {
    "indep": {(0, 0): F(9, 16), (0, 1): F(3, 16), (1, 0): F(3, 16), (1, 1): F(1, 16)},
    "corr":  {(0, 0): F(11, 16), (0, 1): F(1, 16), (1, 0): F(1, 16), (1, 1): F(3, 16)},
}
# per-bit marginal flip p=1/4 for both tables (verified in checks below)
P1 = {0: F(3, 4), 1: F(1, 4)}


def h_true(s, b):
    z = (s * b) % Q
    return z % 2, ((3 * z) % Q) % 2


def h_wrong(s, b):
    z = (s * b) % Q
    return z % 2, ((2 * z) % Q) % 2


def lik_joint(table, binding, v, s, b):
    h1, h2 = binding(s, b)
    return table[(v[0] ^ h1, v[1] ^ h2)]


def lik_marg(v, s, b, binding=h_true):
    h1, h2 = binding(s, b)
    return P1[v[0] ^ h1] * P1[v[1] ^ h2]


def posterior(lik, v):
    """Posterior over S given observation v (tuple). lik(v,s,b) -> Fraction."""
    out = {}
    for s in SSET:
        acc = F(0)
        for b in BSET:
            acc += lik(v, s, b) * PRIOR_B
        out[s] = acc * PRIOR_S
    tot = sum(out.values())
    assert tot > 0, (v, tot)
    return {s: p / tot for s, p in out.items()}


def model_uniform(v):
    return {s: PRIOR_S for s in SSET}


def all_v():
    return [(0, 0), (0, 1), (1, 0), (1, 1)]


def metrics(post_fn, truth_table):
    """Expected NLL (nats), MAP accuracy, mean max posterior under truth law."""
    nll = F(0)
    acc = F(0)
    mx = F(0)
    wsum = F(0)
    details = {}
    for b in BSET:
        for s in SSET:
            for e, we in truth_table.items():
                h1, h2 = h_true(s, b)
                v = (h1 ^ e[0], h2 ^ e[1])
                w = PRIOR_B * PRIOR_S * we
                post = post_fn(v)
                ps = post[s]
                assert ps > 0
                assert sum(post.values()) == 1, (v, sum(post.values()))
                best = max(post.values())
                arg = min(k for k in SSET if post[k] == best)
                nll += w * F(-math.log(float(ps)))
                acc += w * (1 if arg == s else 0)
                mx += w * best
                wsum += w
                d = details.setdefault(v, F(0))
                details[v] = d + w
    assert wsum == 1, wsum
    return {
        "nll": float(nll),
        "map_acc": float(acc),
        "mean_max_post": float(mx),
        "per_condition_weight": {str(k): float(x) for k, x in details.items()},
    }


def map_by_condition(post_fn):
    out = {}
    for v in all_v():
        post = post_fn(v)
        best = max(post.values())
        out[str(v)] = min(k for k in SSET if post[k] == best)
    return out


def scenario_pair(truth_name):
    tt = TABLES[truth_name]
    models = {
        "uniform": model_uniform,
        "single_V1": lambda v: posterior(lambda vv, s, b: P1[vv[0] ^ h_true(s, b)[0]], v),
        "joint_correct": lambda v: posterior(lambda vv, s, b: lik_joint(tt, h_true, vv, s, b), v),
        "joint_marginal_indep": lambda v: posterior(lambda vv, s, b: lik_marg(vv, s, b), v),
        "joint_wrong_binding": lambda v: posterior(lambda vv, s, b: lik_joint(tt, h_wrong, vv, s, b), v),
    }
    res = {name: metrics(fn, tt) for name, fn in models.items()}
    # exact identity check: correct joint == marginal-independent in the
    # independent-noise scenario, condition by condition
    ident = {}
    for v in all_v():
        pc = models["joint_correct"](v)
        pm = models["joint_marginal_indep"](v)
        ident[str(v)] = max(abs(float(pc[s] - pm[s])) for s in SSET)
    res["_identity_max_abs_diff_correct_vs_indep"] = max(ident.values())
    res["_map_by_condition"] = {name: map_by_condition(fn) for name, fn in models.items()}
    return res


def scenario_replication():
    """True law: V2 = V1 = h1(S,B) xor E, E ~ Bern(1/4); truth uses it once."""
    tt = {(0,): P1[0], (1,): P1[1]}

    def lik_single(v, s, b):
        return P1[v[0] ^ h_true(s, b)[0]]

    def lik_rep(v, s, b):
        p = lik_single(v, s, b)
        return p * p

    models = {
        "uniform": lambda v: model_uniform(v),
        "single_once": lambda v: posterior(lik_single, v),
        "replication_weighted": lambda v: posterior(lik_rep, v),
    }

    def metrics_rep(post_fn):
        nll = F(0); acc = F(0); mx = F(0); wsum = F(0)
        for b in BSET:
            for s in SSET:
                for ekey, we in tt.items():
                    e = ekey[0]
                    v = (h_true(s, b)[0] ^ e,)
                    v2 = (v[0], v[0])
                    w = PRIOR_B * PRIOR_S * we
                    post = post_fn(v2)
                    ps = post[s]
                    assert ps > 0 and sum(post.values()) == 1
                    best = max(post.values())
                    arg = min(k for k in SSET if post[k] == best)
                    nll += w * F(-math.log(float(ps)))
                    acc += w * (1 if arg == s else 0)
                    mx += w * best
                    wsum += w
        assert wsum == 1
        return {"nll": float(nll), "map_acc": float(acc), "mean_max_post": float(mx)}

    res = {name: metrics_rep(fn) for name, fn in models.items()}
    res["_map_by_condition"] = {
        name: map_by_condition(lambda v: fn((v[0], v[0]))) for name, fn in models.items()
    }
    # MAP identity check per condition (single vs replication)
    a = res["_map_by_condition"]["single_once"]
    b = res["_map_by_condition"]["replication_weighted"]
    res["_map_identical_single_vs_rep"] = (a == b)
    return res


def table_marginals():
    out = {}
    for name, t in TABLES.items():
        m1 = {0: t[(0, 0)] + t[(0, 1)], 1: t[(1, 0)] + t[(1, 1)]}
        m2 = {0: t[(0, 0)] + t[(1, 0)], 1: t[(0, 1)] + t[(1, 1)]}
        assert sum(t.values()) == 1
        assert m1 == m2 == {0: F(3, 4), 1: F(1, 4)}, (name, m1, m2)
        out[name] = {"E1": {str(k): str(v) for k, v in m1.items()},
                     "E2": {str(k): str(v) for k, v in m2.items()},
                     "P(E1=E2=0)": str(t[(0, 0)]), "P(E1=E2=1)": str(t[(1, 1)])}
    return out


def main():
    out = {
        "experiment": "EXP-20261107-02 / PQC-H002 v1",
        "protocol_sha256": "cc4eac9f9ab2ccbb1ca858ee031ea4527b8b22e187413a439af29339ef8d4fe9",
        "q": Q,
        "states": {"indep": 6 * 7 * 4, "corr": 6 * 7 * 4, "replication": 6 * 7 * 2},
        "table_marginals": table_marginals(),
        "scenario_independent_noise": scenario_pair("indep"),
        "scenario_correlated_noise": scenario_pair("corr"),
        "scenario_replication": scenario_replication(),
    }
    out["states"]["total"] = 168 + 168 + 84
    out["predictions"] = {
        "P1_joint_beats_single_indep": (
            out["scenario_independent_noise"]["joint_correct"]["nll"]
            < out["scenario_independent_noise"]["single_V1"]["nll"] - 1e-12),
        "P2_correct_equals_indep_approx_indep": (
            out["scenario_independent_noise"]["_identity_max_abs_diff_correct_vs_indep"] <= 1e-12),
        "P3_correct_beats_indep_approx_corr": (
            out["scenario_correlated_noise"]["joint_correct"]["nll"]
            < out["scenario_correlated_noise"]["joint_marginal_indep"]["nll"] - 1e-12),
        "P4_correct_beats_wrong_binding_corr": (
            out["scenario_correlated_noise"]["joint_correct"]["nll"]
            < out["scenario_correlated_noise"]["joint_wrong_binding"]["nll"] - 1e-12),
        "P5_replication_inflates_nll_and_confidence": (
            out["scenario_replication"]["replication_weighted"]["nll"]
            > out["scenario_replication"]["single_once"]["nll"] + 1e-12
            and out["scenario_replication"]["replication_weighted"]["mean_max_post"]
            > out["scenario_replication"]["single_once"]["mean_max_post"] + 1e-12),
        "P6_replication_map_identical": out["scenario_replication"]["_map_identical_single_vs_rep"],
    }
    outdir = os.environ.get("H002_OUTDIR", ".")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "h002.json"), "w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False, sort_keys=False)

    # human-readable table
    lines = ["| 情景 | 模型 | 期望 NLL (nats) | MAP 正确率 | 平均最大后验 |",
             "|---|---|---:|---:|---:|"]
    for scen, key in (("独立噪声", "scenario_independent_noise"),
                      ("相关噪声", "scenario_correlated_noise"),
                      ("复制观测", "scenario_replication")):
        for mname, m in out[key].items():
            if mname.startswith("_"):
                continue
            lines.append(f"| {scen} | {mname} | {m['nll']:.9f} | {m['map_acc']:.6f} | {m['mean_max_post']:.6f} |")
    txt = "\n".join(lines) + "\n\n预测核验：\n```json\n" + json.dumps(out["predictions"], indent=2) + "\n```\n"
    with open(os.path.join(outdir, "h002-table.md"), "w") as f:
        f.write(txt)
    print(txt)


if __name__ == "__main__":
    main()
