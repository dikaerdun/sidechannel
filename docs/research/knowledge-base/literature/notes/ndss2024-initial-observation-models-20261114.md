# NDSS 2024 初筛与观察模型的保证范围

日期：2026-11-14。完整逐题阅读官方目录的 140 条标题；21 条候选、37 条不确定、82 条暂列标题范围外。后者仍待摘要复核，不是最终排除。

本批仅读六篇完整官方摘要，纳入五篇通用研究，一篇列相邻主题。没有正文、证明或参考列表阅读。其余 134 篇摘要、独立目录对应与前后向引用仍待处理。没有新增 PQC 侧信道卡片，不等于本年度没有相关论文。

| 论文 | 阅读所得 | 不能据此主张 |
|---|---|---|
| [BliMe](https://www.ndss-symposium.org/ndss-paper/blime-verifiably-secure-outsourced-computation-with-hardware-enforced-taint-tracking/) | ISA 污点扩展、BOOM RTL 和简化 ISA 的机器检查证明；HSM 与原子加解密/污点操作是架构条件 | 小功耗开销不是小泄漏；简化模型证明不是任意功耗、EM 与微架构通道的保证 |
| [IdleLeak](https://www.ndss-symposium.org/ndss-paper/idleleak-exploiting-idle-state-side-effects-for-information-leakage/) | C0.1/C0.2 的空闲状态效应用于活动观察与隐蔽通道 | 7.1 Mbit/s 原生性能增强型、46.3 kbit/s 跨 VM 及 656.37 kbit/s 原生中断型为不同情景，均不是密钥恢复速率；不证明清理后的 PQC 留痕 |
| [SENSE](https://www.ndss-symposium.org/ndss-paper/sense-enhancing-microarchitectural-awareness-for-tees-via-subscription-based-notification/) | TEE 订阅微架构事件；gem5 原型及良性条件下 1.2% 性能开销 | 模拟器结果不是芯片实测；通知不增加泄漏的证明条件和攻击范围尚未阅读全文核对 |
| [TEE-SHirT](https://www.ndss-symposium.org/ndss-paper/tee-shirt-scalable-leakage-free-cache-hierarchies-for-tees/) | 分区 LLC/L2、刷新的非分区 L1、元数据虚拟化、多线程一致性和形式化模型 | 标题 leakage-free 不扩展为整机全部观察无泄漏 |
| [Timing Channels in Adaptive Neural Networks](https://www.ndss-symposium.org/ndss-paper/timing-channels-in-adaptive-neural-networks/) | 六类 ADNN、四数据集及两个虚构公网示范应用中的输入属性时序推断 | 9.89 倍是猜测概率的相对提升，不是绝对准确率；示范应用不是被入侵的真实医疗或人事系统 |
| [When Cryptography Needs a Hand](https://www.ndss-symposium.org/ndss-paper/when-cryptography-needs-a-hand-practical-post-quantum-authentication-for-v2v-communications/) | PQC/V2V 混合认证、证书传输调度与性能；列相邻主题 | 摘要中的协议安全与性能实验不证明物理侧信道保护；93% 冗余和 0.39 ms 增量需保留原情景 |

本轮没有新增引用或版本边。五篇新卡片的十项前后向任务均为 pending。候选标题中未读的声学、EM、流量、指纹及加密访问模式研究应继续补读，不能因本轮挑选的是观察模型与架构方向而忽略它们。

[来源与哈希](../provenance/ndss2024-initial-20261114.json)保存原始获取信息；[逐篇阅读批次](../screening/batches/ndss2024-initial-20261114.jsonl)保存完整摘要的规范化哈希。本次阅读与新增的[大胆研究目标](../../brainstorms/2026-11-14-algorithm-first-echoes-and-model-discovery.md)分别记录：文献摘要不证明那些假设。
