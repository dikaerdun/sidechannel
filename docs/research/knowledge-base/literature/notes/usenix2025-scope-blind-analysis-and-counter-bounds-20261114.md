# USENIX 2025 的盲分析 计数器防护与目录边界

更新：2026-11-14。已读全部 438 条标题及 103 个候选或不确定项的完整官方摘要，作出 37 条纳入、66 条相邻判定；其余 335 篇仍待摘要复核。新增 36 条卡片，已有 DL-BSCA 卡片升级为指定正文阅读；TEEcorrelate 也补读正文与材料附录。以下区分作者报告、本文来源核查和待解决的问题，没有运行实验或作者代码。

## 目录成员对应与总数差异分别记录

[官方技术议程](https://www.usenix.org/conference/usenixsecurity25/technical-sessions)与[另取的印刷目录](https://www.usenix.org/sites/default/files/sec25_contents.pdf)均有 438 篇，规范化标题逐项唯一对应，438 个起始页也唯一。本批把印刷起始页补入目录，DL-BSCA 为 5777、TEEcorrelate 为 2481。

但[主席致辞](https://www.usenix.org/sites/default/files/sec25_message.pdf)写当前周期录用 407 篇、上一年结转 32 篇，算术合计为 439。[致辞补充](https://www.usenix.org/sites/default/files/sec25_message_addendum.pdf)补充审稿与奖项致谢，没有解释这个差异。**成员对应完成，主席统计仍未对齐**；不能据此补造第 439 篇、猜测撤回或认定某个具体条目遗漏。来源记录的 `count_reconciled` 保留 false。

两份单页勘误也已读取：[Hastings](https://www.usenix.org/system/files/sec25_errata_hastings.pdf)交换 β₀/β₁ 的文字定义并更正 insurer/defender 用词；[Kabir](https://www.usenix.org/system/files/sec25_errata_kabir.pdf)补充 NSF 2442825 致谢。后者勘误页题名开头不完整，不能覆盖目录中的完整论文题名 Disparate Privacy Vulnerability: Targeted Attribute Inference Attacks and Defenses。勘误已读不等于对应论文正文已读，也不改变其筛查状态。

## DL-BSCA 的盲条件与 Kyber 恢复对象

[Breaking the Blindfold: Deep Learning-based Blind Side-channel Analysis](https://www.usenix.org/conference/usenixsecurity25/presentation/rezaeezade)的[正式 PDF](https://www.usenix.org/system/files/usenixsecurity25-rezaeezade.pdf)包含封面；下列 PDF 页从封面计数，印刷页另列。

论文使用多点聚类构造标签，再训练网络学习相关中间变量的联合泄漏。攻击阶段不使用逐条明文或密文，但 PDF 第 6–7 页明确假设知道有用选点，实验按实际目标 HW 与测量的相关性选点。完全无标签的选点仍是限制，不能把“blind”写成没有任何先验、标签或实现知识。

Kyber 实验针对 NTT 域成对逐点乘法中的一个秘密系数 s₀，选择 u₀ 与 s₀u₀ 的关系。它不是完整 KEM 私钥的端到端恢复报告。

| 正文条件 | 作者报告 | 解释边界 |
|---|---|---|
| PDF 第 11 页，印刷 5786 | pqm4 参考 Kyber，STM32F3 Cortex-M4，7.372 MHz，ChipWhisperer 308，LeCroy 500 MS/s | 固定实现与测量配置；不能直接外推最终 ML-KEM 的所有实现 |
| 同页数据与划分 | 固定密钥 100,000 条；50,000 样本压缩为 10,000；80,000 条标注/训练，20,000 条攻击池 | 每次从同一攻击池抽 5,000 条，重复 100 次；不是 100 个独立密钥或采集会话 |
| 表 3，DNN + MC | CNN 的 GE=2.01；MLP 的 GE=9.2 | GE 是正确候选的平均排名，不保证每次进入前十 |
| 表 3，增加 dropout | CNN 的 GE=8.04；MLP 的 GE=16.2 | 不能只报告最佳组合并称所有模型都成功；表内没有 Kyber 的 GE=0 结果 |

PDF 第 6 页脚注 3 也说明，完整密钥仍需要额外枚举或其他恢复步骤。正文把 GE≤10 与稳定进入前十联系起来，但仅有均值不足以推出逐次保证。这里保留指标及其实际统计含义，不自行提高恢复结论。

进一步复核还需检查 100 个随机网络和部分 top-10 选择所使用的评分真值、开发预算及最终评估隔离；本批只记录这一审计需求，不据此认定实验无效。去同步案例与 Kyber 不应混用；真实掩码防护下的攻击仍开放。

附录算法的秘密候选区间写成包含 q 的集合，而 0 与 q 在模 q 下等价；公开系数区间及乘积的约减/机器表示也需和实际数据对应。这是记号和实现语义的待查问题，不是已经证明的程序错误。PDF 第 16 页给出[材料版本 DOI](https://doi.org/10.5281/zenodo.15614359)，正文的父记录文本不完整但链接可定位；本批未读取或执行材料内容。

## TEEcorrelate 的结果属于指定模型下的估计

[TEEcorrelate](https://www.usenix.org/conference/usenixsecurity25/presentation/weissteiner)的[正式 PDF](https://www.usenix.org/system/files/usenixsecurity25-weissteiner.pdf)用时间聚合及模糊增量保留粗粒度性能监控，降低细粒度计数器读出。默认聚合窗口为约一百万条退休指令，偏移窗口 2048，对应最大偏移 1024。

安全评估假定强主机知道除秘密之外的状态，能够控制聚合窗口和计数器偏移，并有完美单步能力。长时间攻击成本主要来自统计样本量与运行成本计算；[材料附录](https://www.usenix.org/system/files/usenixsecurity25-appendix-weissteiner.pdf)明确描述防护行为模拟和 HQC 时间估计。不能写成已经实际持续运行数百天的攻击实验。

PDF 第 9 页对假想 SEV-SNP 硬件实现估计开销：完整聚合窗口的额外 954 周期相对 6061 周期切换基线约为 16%，其他切换的两周期约为 0.03%；在文中聚合与指令假设下摊销估计为 0.09%。比较还排除了其认为其他缓解也需支付的计数器交换成本。**0.09% 不是已部署硬件的全系统实测值。**

### 版本内的数值与单位需要统一

| 位置 | 报告值 | 需要保留的区别 |
|---|---|---|
| 官方摘要 | 0.58–429 秒变为 1–775.6 天 | 与正文表 4 的最大值不同 |
| 引言 PDF 第 3 页 | HQC 至少 108.59 天，比较 800 ms；TOTP 验证 32.6 天 | 不能直接代替后续表格和按 trace 的计费 |
| 表 4，PDF 第 12 页／印刷 2491 | 字符串 18.14 秒→34.7 天；查表 0.58 秒→285.4 天；RSA 7.15 分钟→824.6 天；HQC 6.13 分钟→27.0 天 | 默认窗口 2048；HQC 基线脚注基于理想预言机与单步数量估计 |
| HQC 正文，PDF 第 14 页／印刷 2493 | 窗口 64、2048、32768 对应 43.4 分钟、27.0 天、15.1 年 | 800 ms 是每条 trace 的成本；460 个理想查询给出 6.13 分钟，而 0.95 可靠度使用 664 次查询 |

以上数值是来源间及同一稿件不同位置的记录，未判断哪一项是最终更正值。HQC 离线种子搜索还使用 RTX 3090 上 MD5 的 65,000 MH/s 作为成本代理，不能当成实测 HQC 种子枚举速率。

### 视觉核查确认的印刷表达式问题

PDF 第 11 页／印刷 2490 将标准差写为 σ=√(p(p−1)/n)，第 12 页的样本量式延续 pᵢ(pᵢ−1)。当 0<p<1 时被开方量为负，不是实数标准差。第 12 页另一段又将 p(1−p) 写作标准差，混淆了方差与标准差。这里记录的是印刷公式不一致；是否仅为排版错误、实际计算是否正确，需要材料或修订稿核对。

PDF 第 14 页把总时间写作

\[
T(k)=\frac{1}{F(225,k)R}+\frac{N(k,\alpha)Q_\alpha}{T_t},
\]

同时把 Tₜ 定义为每条 trace 的运行时间 800 ms。按这一定义，第二项的单位为时间的倒数，不能直接与第一项的时间相加。另需检查该式使用的二项分布下尾 CDF 与文字中“至少 k 次快速除法”的事件是否一致。不能私自修公式后把新数值写成论文结果。

从单项 α=0.9 到总置信水平 0.81 的组合，也需要核对联合判决及依赖条件。上述问题都应纳入独立统计和成本审计，**不足以直接证明防护失效、论文数值全部错误或存在可用绕过**。

正文第 14–15 页另明确：秘密造成很大的计数增量时，保护能力下降；跨核、共享性能计数器不在当前防护范围。单个受保护计数器的估计不能替代所有联合观察的安全性。

主文材料 DOI 为 [15592842](https://doi.org/10.5281/zenodo.15592842)，材料附录为 [15699920](https://doi.org/10.5281/zenodo.15699920)，两者版本关系尚未核实，分别保留。网页 BibTeX 的作者重复与显示名单/PDF 不同，目录沿用显示作者，没有复制重复项。

## 摘要范围与关键词误判

| 条目类型 | 本批判定 |
|---|---|
| LLM token 缓存推断中的 Falcon | 语言模型，纳入通用侧信道；不是后量子签名 |
| EMV 的 SCA、Find My 的 rainbow table | 分别是 Strong Customer Authentication 和普通查找表语境；不能凭缩写归入侧信道或 PQC |
| Not so Refreshing | RFM 防护引出的时间侧信道，纳入；其他纯 Rowhammer 故障条目保留相邻项 |
| Achilles、GlitchFHE、GPUHammer、Posthammer、ONEFLIP 等 | 故障或完整性方向；不把故障后的秘密输出或直接失陷写成被动测量 |
| OwlC、Vest | 摘要明确声明侧信道相关保证，纳入；完整观察模型待正文，不能外推功耗与全部微架构 |
| PolySys | 加密查询模式的多项式约束推断，不是 PQC 格求解器 |
| DiskSpy、BarraCUDA | 分别保留合作发送端的隐蔽通信与 DNN 权重推断条件；不是任意受害者密码密钥恢复 |
| PDMEM | 数字识别与语音转录指标分别记录；摘要的 maximum 14% transcription error rate 不擅改为最佳 WER |

相邻判定以已读摘要为依据，正文可能修订。标题初筛中的 335 个未读摘要条目也不视为最终排除。

## 引用追踪与下一步

DL-BSCA 全部 58 条参考文献初筛为九条目录对应、36 条待查、13 条暂列背景。TEEcorrelate 本批仅选读六条，四条对应、两条待查，其余 76 条尚未完整筛查。合计新增 13 条引用边和 38 条待查发现；不表示所有被引摘要已读，也不表示递归引用闭合。

特别保留两项身份边界：DL-BSCA [34] 引用 2023 年 ACM Computing Surveys 的 SoK，与 USENIX 2026 的同题论文作者、年份和刊物不同，不能按题名合并；TEEcorrelate [20] 实际引用 2024 ePrint，虽然库中已有同题 TCHES 2025，预印本身份及版本关系仍需主来源核实。

优先补读 DL-BSCA [35] 的 ICCAD 2023 Kyber 盲分析、[34] SoK、CiC 2024 两项方法；核实 TEEcorrelate [20] 实际版本与 [46] DSN 2024 防护。随后补 TEEcorrelate 其余参考文献、统计表达式与成本定义；继续 USENIX 2025 剩余 335 篇摘要及其他会议，不能只追关键词命中项。

阅读范围：DL-BSCA PDF 第 6–7、9–11、14–16、19–20 页相关选段及第 16–19 页全部 58 条参考文献；TEEcorrelate 第 3、9–15 页相关选段、第 17–19 页六条选读引用，材料附录第 1–3 页。视觉核查 DL-BSCA 表 3、TEEcorrelate 第 11–12、14 页表达式与表格，以及目录/致辞/勘误页。没有完成全文证明、材料代码审计或独立第二读者核验。

[阅读来源与哈希](../provenance/usenix2025-candidates-20261114.json) · [目录来源与差异](../provenance/usenix2025-print-toc-crosscheck-20261114.json) · [DL-BSCA 引用清单](../citations/usenix2025-blind-reference-screen.jsonl) · [TEEcorrelate 六条选读](../citations/usenix2025-tee-reference-screen.jsonl) · [批次记录](../../records/2026-11-14-literature-usenix2025.md)
