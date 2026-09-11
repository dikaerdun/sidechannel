# 原始文献、阅读顺序与证据范围

[返回目录](../README.md)

核验日期：2026-09-11。本教程以原理教学为中心，使用标准、作者论文和官方文档。未对所有 2025—2026 年论文做穷尽检索，不给出“当前最优攻击”排名。

## 已核验的主要来源

| 编号 | 文献及入口 | 阅读重点 | 本次核验深度 |
|---|---|---|---|
| R01 | Kocher, 1996, [Timing Attacks on Implementations of Diffie-Hellman, RSA, DSS, and Other Systems](https://paulkocher.com/doc/TimingAttacks.pdf) | 总时间如何约束秘密指数 | 作者 PDF 正文 |
| R02 | Kocher, Jaffe, Jun, 1999, [Differential Power Analysis](https://paulkocher.com/doc/DifferentialPowerAnalysis.pdf) | 选择函数、分组与弱信号积累 | 作者 PDF 正文 |
| R03 | Brier, Clavier, Olivier, 2004, [Correlation Power Analysis with a Leakage Model](https://link.springer.com/chapter/10.1007/978-3-540-28632-5_2)；早期稿 [Optimal Statistical Power Analysis](https://eprint.iacr.org/2003/152) | HD 参考状态与相关评分 | 出版页面、摘要与书目信息；教程公式为教学推导 |
| R04 | Chari, Rao, Rohatgi, CHES 2002, [Template Attacks](https://link.springer.com/chapter/10.1007/3-540-36400-5_3) | 分布、模板设备和单次目标观测 | 出版页面与摘要；书卷于 2003 出版 |
| R05 | Agrawal et al., CHES 2002, [The EM Side—Channel(s)](https://link.springer.com/chapter/10.1007/3-540-36400-5_4) | 多种电磁成分与不同泄漏信息 | 出版页面与摘要；书卷于 2003 出版 |
| R06 | Nikova, Rechberger, Rijmen, 2006, [Threshold Implementations Against Side-Channel Attacks and Glitches](https://link.springer.com/chapter/10.1007/11935308_38) | 把毛刺纳入掩码保护 | 出版页面、摘要和参考文献；未逐条复核完整证明 |
| R07 | Gross, Mangard, Korak, 2016, [Domain-Oriented Masking](https://eprint.iacr.org/2016/486) | 硬件共享、保护阶数和资源开销 | 作者摘要、版本与书目信息；未复现门级实现 |
| R08 | [TVLA Derived Test Requirements with AES](https://www.rambus.com/wp-content/uploads/2015/08/TVLA-DTR-with-AES.pdf) | 采集交错、独立重复、一阶/二阶检验 | PDF 正文；文档流程不是所有认证的统一规则 |
| R09 | Prouff et al., 2018/2020, [Study of Deep Learning Techniques for Side-Channel Analysis and Introduction to ASCAD Database](https://eprint.iacr.org/2018/053) | 掩码 AES、学习与可复现基准 | 作者摘要、版本与期刊信息 |
| R10 | NIST, 2024, [FIPS 203: ML-KEM](https://csrc.nist.gov/pubs/fips/203/final)；[正文](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf) | NTT、K-PKE 解密、内部解封装、保密要求 | 官方页面与正文重点算法 |
| R11 | NIST, 2024, [FIPS 204: ML-DSA](https://csrc.nist.gov/pubs/fips/204/final)；[正文](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf) | 签名、拒绝采样、确定性与 hedged 变体 | 官方页面与正文重点算法 |
| R12 | Bernstein et al., ePrint 2024/1049, TCHES 2025, [KyberSlash](https://eprint.iacr.org/2024/1049) | 秘密相关除法与机器级时序 | 作者摘要、平台、版本及出版信息；未复现实机攻击 |
| R13 | Heinz et al., ePrint 2022/058，2023 修订，[First-Order Masked Kyber on ARM Cortex-M4](https://eprint.iacr.org/2022/058) | 完整掩码解封装与实测证据边界 | 作者摘要、性能与测试声明；未复现实机实现 |
| R14 | [ChipWhisperer 官方文档](https://chipwhisperer.readthedocs.io/en/latest/) | 从合成实验过渡到可控设备与测量流程 | 官方入口与功能目录 |
| R15 | Monfared, Mosavirik, Tajik, 2023, [LeakyOhm: Secret Bits Extraction using Impedance Analysis](https://arxiv.org/abs/2310.07014) | 非侵入式与被动不是同一维度 | 作者摘要；主动阻抗测量仅作扩展边界 |
| R16 | NIST, [FIPS 197: AES](https://csrc.nist.gov/pubs/fips/197/final) | AES 算法规范；合成实验只使用 S 盒 | 官方标准入口 |
| R17 | [The SM4 Blockcipher Algorithm，IETF 草案](https://datatracker.ietf.org/doc/html/draft-ribose-cfrg-sm4-10) | 英文轮函数说明，辅助理解结构 | 草案入口；它不是正式 RFC 或中国标准替代品 |
| R18 | NIST, [FIPS 186-5: Digital Signature Standard](https://csrc.nist.gov/pubs/fips/186-5/final) | ECDSA 背景与签名术语 | 官方标准入口 |
| R19 | Carrera Rodriguez et al., PRIME 2023, [Correlation Electromagnetic Analysis on an FPGA Implementation of CRYSTALS-Kyber](https://eprint.iacr.org/2022/1361) | FPGA 多项式乘法的电磁相关分析 | 作者摘要、实验声明与出版信息 |
| R20 | Marzougui et al., 2022, [Profiling Side-Channel Attacks on Dilithium: A Small Bit-Fiddling Leak Breaks It All](https://eprint.iacr.org/2022/106) | 位解包泄漏、学习与等价签名密钥恢复 | 作者摘要、版本与书目信息 |
| R21 | Steffen et al., PQCrypto 2023, [Breaking and Protecting the Crystal: Side-Channel Analysis of Dilithium in Hardware](https://link.springer.com/chapter/10.1007/978-3-031-40003-2_25) | NTT 硬件 SPA/CPA，区分训练与目标数据 | 出版摘要、数据声明与书目信息 |

## 标准版本注意事项

FIPS 203 官方页面列有 2025-11-17 的后续勘误提示；FIPS 204 官方页面列有 2026-07-31 的勘误提示。本文以 2024 年最终版的核心算法解释原理，没有逐条审查勘误电子表格，不宣称完成最新实现符合性审计。工程实现时应从官方入口下载标准及当前勘误一起核对。

Kyber、Dilithium 的历史提交与 FIPS 标准之间存在差异。标准内的差异说明以及官方历史资料可帮助核对：[Kyber 资源](https://pq-crystals.org/kyber/resources.shtml)、[Dilithium 资源](https://pq-crystals.org/dilithium/resources.shtml)。

## 扩展阅读入口

本仓库已有[系统研究报告](research/nist-pqc-hardware-sidechannel-report.md)和[研究证据索引](research/evidence-matrix.md)，适合在学完原理后进一步查找具体 PQC 实现与攻击论文。两类资料各自标明核验范围；引用时回到原始来源。

Peter Schwabe 的[作者论文目录](https://cryptojedi.org/papers/)列出 *Towards ML-KEM & ML-DSA on OpenTitan*（IEEE S&P 2025）和 *Post-Quantum Implementations*（2025）等资料。本次仅核验目录中的书目信息，未以这些论文的内部数据支持性能或安全结论。

ASCAD 的[官方仓库](https://github.com/ANSSI-FR/ASCAD)可用于从合成模型过渡到真实数据学习。应核对具体数据集版本、标签、许可和训练/测试划分，不宜把其结果直接推广到任意硬件。

## 本教程中哪些内容是原创推导

本教程自行组织了以下教学内容：条件似然与可辨识性的统一说明；CPA 与最小二乘联系；XOR 互补歧义；双射标签互信息不变的反例；字节份额中心化乘积公式；份额连续写入的 HD 反例；q=17 的 NTT、解码与签名手算；安全 IP 的数据生命周期表和研究方向。

这些是用于解释一般机制的数学推导和综合分析，不冒充所引论文中的新实验。代码产生的迹线、数值、图表都来自合成模型，不能作为真实产品的安全测试报告。

## 使用文献的方式

仓库提供链接与原创导读，没有镜像或重新分发论文 PDF。引用的“作者报告”按所能核验的证据层次表述；仅核验摘要的资料，不声称已经审查其所有攻击细节、代码、图表或证明。
