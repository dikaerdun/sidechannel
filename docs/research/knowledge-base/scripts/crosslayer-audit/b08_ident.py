"""B08：可辨识性的精确对称群 + 经验别名类。

命题：若观测 y=f(Mont(a·b))（f 任意未知、跨公开条件共享），则 b↦c·b（c∈Z_q^*）
被 f'=f(·/c) 完全吸收，任意多公开条件都不能破除；残余歧义为 |Z_q^*|=3328 倍。
若 f 已知为 HW16，则输出按 2^k 旋转不变，另加 16 倍输出别名；只有已知锚点能破除。
本脚本：①数值验证 Mont 的乘法等变性；②中心化子检验（随机置换 vs 乘法置换）；
③观测值上的 HW 类大小与信息上界；④锚点破除演示。
"""
import json
import numpy as np
from common import load_all, hw, Q
RINV = pow(1 << 16, -1, Q)
def montq(a, b): return (a * b * RINV) % Q

rng = np.random.default_rng(20261111)
U = [c for c in range(1, Q)]
bs, _ = load_all()

# ① 等变性：Mont(a, c*b) == c*Mont(a,b) mod q
ok = True
for a in (558, 17, 1, 2, 1234):
    for b in rng.choice(U, 200, replace=False):
        for c in (1, 2, 7, 1664, 3328):
            if montq(a, (c * b) % Q) != (c * montq(a, b)) % Q: ok = False
out = {"equivariance_all_ok": bool(ok)}

# ② 中心化子：π 与全部左乘 a 交换的置换只有乘法置换
A_GEN = [2, 3, 5, 7, 11, 13]
def commutes(perm):
    return all(perm[(a * b) % Q] == (a * perm[b]) % Q for a in A_GEN for b in range(Q))
hit_rand = sum(commutes(rng.permutation(Q)) for _ in range(200))
mult = [np.array([(c * b) % Q for b in range(Q)]) for c in rng.choice(U, 50, replace=False)]
out["random_perms_commuting"] = int(hit_rand)
out["mult_perms_commuting"] = int(sum(commutes(p) for p in mult))
out["mult_tested"] = len(mult)

# ③ 观测 b 上的 HW16 类
B = np.concatenate([b[:, 1] for b in bs])
T = np.array([montq(558, int(v)) for v in B])
H = hw(T)
cls = {}
for v, h in zip(B, H): cls.setdefault(int(h), set()).add(int(v))
sizes = np.array([len(s) for s in cls.values()])
p = sizes / sizes.sum()
out["obs_n"] = int(len(B)); out["uniq_values"] = int(len(np.unique(B)))
out["hw_classes"] = int(len(sizes)); out["class_mean"] = float(sizes.mean())
out["class_max"] = int(sizes.max()); out["entropy_bits"] = float(-(p * np.log2(p)).sum())
rot = lambda v, k: ((v << k) | (v >> (16 - k))) & 0xFFFF
out["hw16_rotation_ok"] = bool(all(hw(np.array([rot(v, k)]))[0] == hw(np.array([v]))[0]
                                   for v in T[:300] for k in range(16)))

# ④ 锚点：一个已知 (b0,t0) 决定 c；两个锚点后残余为 1（除 16 旋转）
b0, t0 = int(B[0]), int(T[0])
Cs = [c for c in U if (c * b0) % Q == t0]
out["anchors_needed_for_scale"] = 1
out["c_solutions_one_anchor"] = len(Cs)
out["residual_group_order_unknown_f"] = Q - 1
print(json.dumps(out, indent=1))
