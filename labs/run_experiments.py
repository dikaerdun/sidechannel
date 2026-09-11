#!/usr/bin/env python3
"""Synthetic side-channel lessons. No device access and no production crypto.

All leakage points and distributions are deliberately chosen teaching models.
Ranks are one-based, with tied hypotheses sharing the optimistic rank.
"""
from pathlib import Path
import argparse
import csv
import json
import math
import platform

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
FIG = ROOT / "figures"
RES = ROOT / "results"
HW = np.array([i.bit_count() for i in range(256)], dtype=np.float64)
SBOX = np.frombuffer(bytes.fromhex(
    "637c777bf26b6fc53001672bfed7ab76"
    "ca82c97dfa5947f0add4a2af9ca472c0"
    "b7fd9326363ff7cc34a5e5f171d83115"
    "04c723c31896059a071280e2eb27b275"
    "09832c1a1b6e5aa0523bd6b329e32f84"
    "53d100ed20fcb15b6acbbe394a4c58cf"
    "d0efaafb434d338545f9027f503c9fa8"
    "51a3408f929d38f5bcb6da2110fff3d2"
    "cd0c13ec5f974417c4a77e3d645d1973"
    "60814fdc222a908846eeb814de5e0bdb"
    "e0323a0a4906245cc2d3ac629195e479"
    "e7c8376d8dd54ea96c56f4ea657aae08"
    "ba78252e1ca6b4c6e8dd741f4bbd8b8a"
    "703eb5664803f60e613557b986c11d9e"
    "e1f8981169d98e949b1e87e9ce5528df"
    "8ca1890dbfe6426841992d0fb054bb16"
), dtype=np.uint8)


def models(p):
    """Only public input and candidate key enter attack hypotheses."""
    return HW[SBOX[np.bitwise_xor(np.arange(256, dtype=np.uint8)[:, None], p)]]


def correlations(hypotheses, observations):
    h = np.asarray(hypotheses, dtype=np.float64)
    l = np.asarray(observations, dtype=np.float64)
    if l.ndim == 1:
        l = l[:, None]
    hc = h - h.mean(axis=1, keepdims=True)
    lc = l - l.mean(axis=0, keepdims=True)
    denom = np.sqrt(np.sum(hc * hc, axis=1)[:, None] * np.sum(lc * lc, axis=0))
    return np.divide(hc @ lc, denom, out=np.zeros_like(denom), where=denom > 0)


def ranked(scores, truth):
    scores = np.asarray(scores)
    wrong = scores.copy()
    wrong[truth] = -np.inf
    return {"best_candidate": int(np.argmax(scores)),
            "true_key": int(truth),
            "true_rank_1_based": int(1 + np.count_nonzero(scores > scores[truth] + 1e-12)),
            "true_score": float(scores[truth]),
            "best_wrong_score": float(np.max(wrong))}


def savefig(name):
    plt.gcf().savefig(FIG / f"{name}.svg", bbox_inches="tight", metadata={"Date": None})
    plt.close()


def cpa_lesson(rng):
    n, points, truth = 2048, 128, 0x2B
    p = rng.integers(0, 256, n, dtype=np.uint8)
    h = models(p)
    time = np.arange(points)
    pulse = np.exp(-0.5 * ((time - 64) / 2.2) ** 2)
    # A common public waveform is irrelevant to between-trace covariance.
    base = 2.0 * np.sin(time / 15)
    traces = base + 0.8 * (h[truth] - 4)[:, None] * pulse + rng.normal(0, 2, (n, points))
    corr = correlations(h, traces)
    scores = np.max(np.abs(corr), axis=1)
    shuffled = correlations(h, traces[rng.permutation(n)])
    bits = (SBOX[np.bitwise_xor(np.arange(256, dtype=np.uint8)[:, None], p)] & 1).astype(float)
    counts = bits.sum(axis=1)
    dpa = bits @ traces / counts[:, None] - (1 - bits) @ traces / (n - counts)[:, None]
    plt.figure(figsize=(11, 7))
    ax = plt.subplot(2, 1, 1)
    ax.plot(time, traces[:3].T, alpha=.6, linewidth=.8)
    ax.set(title="Synthetic power traces: no device was measured", xlabel="Sample index", ylabel="Arbitrary units")
    ax = plt.subplot(2, 1, 2)
    ax.plot(time, np.max(np.abs(corr[np.arange(256) != truth]), axis=0), color="#8893a6", label="Best wrong key at each sample")
    ax.plot(time, np.abs(corr[truth]), color="#076b8e", label="True key 0x2b")
    ax.plot(time, np.max(np.abs(shuffled), axis=0), color="#b07842", linestyle="--", label="Shuffled-label control, all keys")
    ax.set(xlabel="Sample index", ylabel="Absolute correlation", ylim=(0, .65))
    ax.legend(fontsize=9)
    plt.tight_layout()
    savefig("01-cpa-traces")
    result = ranked(scores, truth)
    result.update({"traces": n, "samples_per_trace": points, "injected_center": 64,
                   "peak_sample": int(np.argmax(np.abs(corr[truth]))),
                   "shuffled_max_score": float(np.abs(shuffled).max()),
                   "dpa": ranked(np.max(np.abs(dpa), axis=1), truth)})
    assert result["true_rank_1_based"] == 1
    return result


def wilson(successes, total):
    p, z = successes / total, 1.96
    den = 1 + z*z / total
    center = (p + z*z / (2*total)) / den
    half = z * math.sqrt(p*(1-p)/total + z*z/(4*total*total)) / den
    return max(0, center-half), min(1, center+half)


def noise_lesson(seed, trials):
    sizes = [32, 64, 128, 256, 512, 1024, 2048]
    sigmas = [2., 4., 8.]
    rows = []
    for sigma in sigmas:
        successes = np.zeros(len(sizes), dtype=int)
        ranks = np.zeros(len(sizes))
        for trial in range(trials):
            rng = np.random.default_rng(np.random.SeedSequence([seed, 20, int(sigma), trial]))
            p = rng.integers(0, 256, max(sizes), dtype=np.uint8)
            h = models(p)
            truth = int(rng.integers(0, 256))
            l = h[truth] + rng.normal(0, sigma, len(p))
            for j, n in enumerate(sizes):
                result = ranked(np.abs(correlations(h[:, :n], l[:n])[:, 0]), truth)
                successes[j] += result["best_candidate"] == truth
                ranks[j] += result["true_rank_1_based"]
        for j, n in enumerate(sizes):
            low, high = wilson(int(successes[j]), trials)
            rows.append({"sigma": sigma, "traces": n, "trials": trials,
                         "successes": int(successes[j]), "success_rate": float(successes[j]/trials),
                         "wilson_95_low": low, "wilson_95_high": high,
                         "mean_rank_1_based": float(ranks[j]/trials)})
    with (RES / "noise_sweep.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    plt.figure(figsize=(10, 4.8))
    for sigma, color in zip(sigmas, ["#087e8b", "#b56532", "#6457a6"]):
        selected = [r for r in rows if r["sigma"] == sigma]
        plt.plot(sizes, [r["success_rate"] for r in selected], "o-", color=color, label=f"Noise sigma={sigma:g}")
        plt.fill_between(sizes, [r["wilson_95_low"] for r in selected], [r["wilson_95_high"] for r in selected], color=color, alpha=.12)
    plt.xscale("log", base=2)
    plt.ylim(-.03, 1.03)
    plt.xlabel("Number of synthetic observations")
    plt.ylabel("Single-byte key recovery success rate")
    plt.title(f"Known-point CPA: {trials} independent trials per noise level; 95% Wilson intervals")
    plt.legend()
    plt.grid(alpha=.15)
    savefig("02-noise-samples")
    return {"trials_per_noise": trials, "model": "HW(AES_SBOX(P xor K)) + independent Gaussian noise",
            "attack_feature": "One predetermined leakage sample; no time search", "csv": "noise_sweep.csv"}


def mismatch_lesson(rng):
    n, truth = 12000, 0x2B
    p = rng.integers(0, 256, n, dtype=np.uint8)
    old = rng.integers(0, 256, n, dtype=np.uint8)
    v = SBOX[p ^ truth]
    l = HW[old ^ v] + rng.normal(0, 1.2, n)
    hw = models(p)
    hd = HW[old[None, :] ^ SBOX[np.arange(256, dtype=np.uint8)[:, None] ^ p]]
    score_hw = np.abs(correlations(hw, l)[:, 0])
    score_hd = np.abs(correlations(hd, l)[:, 0])
    p_all = np.arange(256, dtype=np.uint8)
    xor_h = HW[p_all ^ truth]
    xor_complement = HW[p_all ^ (truth ^ 255)]
    assert np.array_equal(xor_h + xor_complement, np.full(256, 8))
    plt.figure(figsize=(10, 4.8))
    plt.plot(score_hw, color="#8893a6", label="Wrong model: new-value HW")
    plt.plot(score_hd, color="#087e8b", label="Correct model: known-old-value HD")
    plt.axvline(truth, color="#b56532", linestyle="--", linewidth=1, label="True key")
    plt.xlabel("Candidate key byte (decimal)")
    plt.ylabel("Absolute correlation")
    plt.title("Independent random old register state: the HW model misses the transition")
    plt.legend()
    savefig("03-model-mismatch")
    result = {"traces": n, "HW": ranked(score_hw, truth), "HD": ranked(score_hd, truth),
              "assumption": "The old register state is public/known in this teaching model",
              "xor_complement_correlation": float(np.corrcoef(xor_h, xor_complement)[0, 1])}
    assert result["HD"]["true_rank_1_based"] == 1
    return result


def masking_lesson(rng):
    truth, n = 0x2B, 40000
    p = rng.integers(0, 256, n, dtype=np.uint8)
    x = SBOX[p ^ truth]
    mask = rng.integers(0, 256, n, dtype=np.uint8)
    a = HW[mask] + rng.normal(0, .7, n)
    b = HW[x ^ mask] + rng.normal(0, .7, n)
    joint = (a-a.mean())*(b-b.mean())
    h = models(p)
    first_a = np.abs(correlations(h, a)[:, 0])
    first_b = np.abs(correlations(h, b)[:, 0])
    second = np.abs(correlations(h, joint)[:, 0])
    exact = []
    all_masks = np.arange(256, dtype=np.uint8)
    for secret in range(256):
        exact.append(np.mean((HW[all_masks]-4)*(HW[all_masks ^ secret]-4)))
    expected = 2 - HW/2
    assert np.array_equal(np.array(exact), expected)
    assert np.array_equal(HW[mask ^ (x ^ mask)], HW[x])
    plt.figure(figsize=(11, 4.8))
    ax = plt.subplot(1, 2, 1)
    ax.plot(first_a, label="Share 0, first order", color="#8b98a9")
    ax.plot(first_b, label="Share 1, first order", color="#c2936e", alpha=.7)
    ax.plot(second, label="Centered product", color="#087e8b")
    ax.set(xlabel="Candidate key byte", ylabel="Absolute correlation", title="Two-share synthetic leakage")
    ax.legend(fontsize=8)
    ax = plt.subplot(1, 2, 2)
    for weight in range(9):
        selected = HW[x] == weight
        ax.scatter(weight, joint[selected].mean(), color="#087e8b", zorder=3)
    ax.plot(range(9), 2 - np.arange(9)/2, color="#b56532", label="Exact expectation: 2 - HW/2")
    ax.set(xlabel="HW of the sensitive byte", ylabel="Mean centered product", title="Joint relation retains the secret")
    ax.legend(fontsize=8)
    plt.tight_layout()
    savefig("04-masking-order")
    result = {"traces": n, "share_0_first_order": ranked(first_a, truth),
              "share_1_first_order": ranked(first_b, truth), "second_order": ranked(second, truth),
              "exact_expectation_verified_for_all_256_bytes": True,
              "transition_identity_verified": True,
              "note": "First-order scores fluctuate under finite sampling; low score is not a proof"}
    assert result["second_order"]["true_rank_1_based"] == 1
    return result


def welch(a, b):
    return float((np.mean(a)-np.mean(b))/np.sqrt(np.var(a, ddof=1)/len(a)+np.var(b, ddof=1)/len(b)))


def tvla_lesson(rng):
    n = 12000
    a = rng.normal(0, 1, n)
    b = rng.normal(0, 2, n)
    mean = np.concatenate([a, b]).mean()
    t1 = welch(a, b)
    t2 = welch((a-mean)**2, (b-mean)**2)
    plt.figure(figsize=(10, 4.8))
    bins = np.linspace(-8, 8, 80)
    plt.hist(a, bins, density=True, alpha=.5, color="#087e8b", label="Group A: mean 0, sigma 1")
    plt.hist(b, bins, density=True, alpha=.5, color="#b56532", label="Group B: mean 0, sigma 2")
    plt.title(f"Equal-mean counterexample: t(first)={t1:.2f}, t(centered square)={t2:.2f}")
    plt.xlabel("Synthetic observation")
    plt.ylabel("Density")
    plt.legend()
    savefig("05-tvla-counterexample")
    return {"samples_per_group": n, "first_order_t": t1, "centered_square_t": t2,
            "note": "A distributional teaching example, not a full TVLA certification procedure"}


def ntt_lesson():
    q, n, root = 17, 4, 4
    a = [1, 2, 3, 4]
    def transform(values, omega):
        return [sum(int(values[i])*pow(omega, i*j, q) for i in range(n)) % q for j in range(n)]
    transformed = transform(a, root)
    recovered = [(v * pow(n, -1, q)) % q for v in transform(transformed, pow(root, -1, q))]
    assert transformed == [10, 7, 15, 6] and recovered == a
    ua, ub, omega = 3, 6, 4
    u, v = (ua+omega*ub)%q, (ua-omega*ub)%q
    inv_a = (u+v)*pow(2, -1, q)%q
    inv_b = (u-v)*pow(2*omega, -1, q)%q
    assert (u, v, inv_a, inv_b) == (10, 13, 3, 6)
    return {"q": q, "n": n, "root": root, "input": a, "ntt": transformed, "inverse": recovered,
            "butterfly": {"input": [ua, ub], "output": [u, v], "inverse": [inv_a, inv_b]},
            "note": "Cyclic length-4 teaching NTT, not the ML-KEM transform"}


def oracle_lesson(rng):
    candidates, truth, q = [-2, -1, 0, 1, 2], 1, 17
    def oracle(u, v, s):
        return int(5 <= (v-u*s)%q <= 12)
    steps = []
    for u, v in [(1, 5), (1, 6)]:
        observed = oracle(u, v, truth)
        candidates = [s for s in candidates if oracle(u, v, s) == observed]
        steps.append({"u": u, "v": v, "observed_bit": observed, "remaining": candidates.copy()})
    assert candidates == [truth]
    # Separate noisy sequence: inputs are fixed in advance and each oracle
    # response is independently flipped with probability epsilon.
    inputs = [(u, v) for u in [1, 2, 3] for v in range(17)] * 4
    epsilon = .1
    flips = rng.random(len(inputs)) < epsilon
    observed = [oracle(u, v, truth) ^ int(flip) for (u, v), flip in zip(inputs, flips)]
    scores = {s: sum(math.log(1-epsilon if o == oracle(u, v, s) else epsilon)
                     for (u, v), o in zip(inputs, observed)) for s in [-2, -1, 0, 1, 2]}
    assert max(scores, key=scores.get) == truth
    return {"noiseless_steps": steps, "noisy_log_scores": scores,
            "noise_model_used_for_scoring": "Independent symmetric error approximation with epsilon=0.1",
            "noise_generation": "Independent Bernoulli flips with epsilon=0.1",
            "number_of_flips": int(flips.sum()),
            "note": "An abstract scalar interval oracle, not an ML-KEM ciphertext attack"}


def signature_lesson():
    q, secret, ephemeral, challenge = 17, 3, 5, 4
    response = (ephemeral + challenge*secret)%q
    recovered = (response-ephemeral)*pow(challenge, -1, q)%q
    assert recovered == secret
    return {"q": q, "secret": secret, "ephemeral": ephemeral, "challenge": challenge,
            "public_response": response, "recovered_secret": recovered,
            "note": "Scalar algebra only; a polynomial challenge need not be invertible"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=20260911)
    parser.add_argument("--trials", type=int, default=40, help="Independent trials per noise level")
    args = parser.parse_args()
    if args.trials < 2 or args.seed < 0:
        parser.error("--trials must be >=2 and --seed must be nonnegative")
    FIG.mkdir(exist_ok=True)
    RES.mkdir(exist_ok=True)
    plt.rcParams.update({"font.family": "DejaVu Sans", "svg.fonttype": "none",
                         "axes.spines.top": False, "axes.spines.right": False,
                         "font.size": 10, "svg.hashsalt": "sidechannel-tutorial-v1"})
    assert len(SBOX) == 256 and len(set(SBOX.tolist())) == 256
    assert SBOX[0] == 0x63 and SBOX[0x53] == 0xED
    sequences = np.random.SeedSequence(args.seed).spawn(5)
    rngs = [np.random.default_rng(s) for s in sequences]
    result = {"seed": args.seed, "data_type": "synthetic",
              "environment": {"python": platform.python_version(), "numpy": np.__version__, "matplotlib": matplotlib.__version__},
              "cpa": cpa_lesson(rngs[0]), "noise": noise_lesson(args.seed, args.trials),
              "model_mismatch": mismatch_lesson(rngs[1]), "masking": masking_lesson(rngs[2]),
              "tvla_counterexample": tvla_lesson(rngs[3]), "toy_ntt": ntt_lesson(),
              "toy_interval_oracle": oracle_lesson(rngs[4]), "toy_signature": signature_lesson()}
    (RES / "summary.json").write_text(json.dumps(result, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
