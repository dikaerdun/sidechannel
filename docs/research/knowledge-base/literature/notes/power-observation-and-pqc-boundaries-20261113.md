# 功耗观察权限 掩码假设与 PQC 恢复对象

核查日期：2026-11-13。以下区分作者报告、实际阅读范围和材料可得性；未运行论文代码或复现实验。完整卡片见 [PAPER_NOTES](../PAPER_NOTES.md)，来源哈希见[本批记录](../provenance/power-sp2025-followup-20261113.json)。

## Peek-a-Walk 的 PQC 案例

[作者论文](https://www.cs.cmu.edu/~rpaccagn/papers/peek-a-walk-sp2025.pdf)的 §4.4（PDF 第 10–11 页）针对参考 Dilithium-2：先取得签名 nonce 的部分系数，再结合公开签名关系与格提示方法恢复 s1。作者分别报告 115 分钟的提示采集与 81 分钟的格后处理。这些是该实现下不同阶段的成本，不能合并成“若干条功耗迹线即可恢复 ML-DSA”。

§4.1 的同机非特权进程及目标地址条件、地址规范性限制仍适用。无需 LAM 的 Dilithium 实验与 §5 的 DMP 沙箱案例是不同路径。参考文献 [52] 是 Dilithium v3.1 文档；最终 ML-DSA 实现等价性没有在本轮核查。选读 [15] GoFetch、[53] Too Many Hints 后已加入引用边，未筛完整参考文献。

[代码 README](https://github.com/FPSG-UIUC/Peek-a-Walk/blob/master/README.md)列出平台和模块，但仍有高级演示移植中及 TODO 字样；有一处代码概览与末尾 TODO 也未同步。仅据 README 不能确认完整 Dilithium 端到端材料已经齐备。下一步应检查具体文件、提交版本和缺失步骤，不能把仓库存在等同于可复现。

## Share-slicing 的模型边界

[TCHES 论文](https://tches.iacr.org/index.php/TCHES/article/view/8396)编入 2020 卷，实际于 2019-11-19 上线。本轮读摘要和 PDF 第 16–17 页（印刷页 167–168）的限制、讨论与结论：位交互使逐位独立假设在所测器件上不成立，但不能据此否定满足假设的数学证明。

正文强调重复、平均带来的成本和器件差异。[补充代码说明](https://github.com/sca-research/ShareSlicing_AES)明确不为所附 AES 实现作安全保证，而且其测试设置与论文不同。它支持把份额装载、指令和噪声条件纳入 OpenTitan 后续审查；不支持直接断言 OpenTitan 已有相同漏洞。

## 软件功耗读出和调度能力

| 论文 | 实际恢复或增强的对象 | 不能省略的条件 |
|---|---|---|
| [Red Alert](https://doi.org/10.1145/3433210.3437517) | 软件功耗隐蔽通道与网站指纹 | 可访问 RAPL；2021 年系统权限不能外推为当前默认配置；不是密码恢复实验 |
| [The Finger in the Power](https://link.springer.com/chapter/10.1007/978-3-031-35504-2_2) | 不同机器的个体身份 | 摘要明确依赖高权限功耗读取并受温度影响；WebAssembly 计算不自动提供传感器权限 |
| [Controlled Preemption](https://doi.org/10.1145/3676641.3715985) | 细化已有微架构通道的时间观察 | §3 要求本机攻击进程、相应 Linux 调度器并能触发受害程序；不要求 SMT，也不因此成为远程攻击 |

The Finger in the Power 的出版页声称公开工具和数据，链接到 `FingerInThePower/Finger_In_The_Power`。2026-11-13 对该仓库内容及 README 的 GitHub API 请求均返回 404；原因未知，可取得性未确认。作者 PDF 的本地 HTTPS 请求还出现证书错误，因此本轮依据可读的出版商摘要，不把下载失败解释成论文没有材料。

## 其他 S&P 2025 新卡片

SLAP、Breaking the Barrier、Ceviche、CipherSteal、Slice+Slice Baby、TikTag 和 Training Solo 均按实际摘要建立卡片。分别保留加载地址预测、屏障实现、缓存防护、TEE 输入重建、逐出集构造、内存标签和域内自训练的对象差异；没有从摘要升级为完整威胁模型或当前修复状态结论。

SLAP 与 CipherSteal 已用出版商提交的 Crossref 记录升级为 DOI 身份，旧目录 ID 继续保留。Slice+Slice Baby 的 arXiv 标题、作者与会议记录对应，但未宣称全文版本完全相同。来源原始页、PDF 和完整摘要只保存在仓库外缓存。
