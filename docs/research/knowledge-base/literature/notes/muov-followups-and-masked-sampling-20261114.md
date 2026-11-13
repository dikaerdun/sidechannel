# mUOV 引用接续与掩码采样证据边界

记录日期：2026-11-14。冻结截止日仍为 2026-11-12；本批只读文献、整理元数据，不运行作者代码或实验。以下结论来自作者报告，未独立复现。

本批解析 mUOV 的七条待查引用，新增六张阅读卡片和三条相邻理论判定。另新增两个只有元数据的目录条目。2018/2019 基础文献单独标记，不计作近五年成果。出处、HTTP 状态、内容哈希见[来源记录](../provenance/muov-followups-20261114.json)，逐条阅读范围见[卡片](../PAPER_NOTES.md)。

## 七条引用对应

| mUOV 参考位置 | 核定身份 | 本批判定 |
| --- | --- | --- |
| 3 / ACK25 | [UOV 物理安全 SoK，PQCrypto 2025](https://doi.org/10.1007/978-3-031-86599-2_7) | 纳入；正式与作者摘要 |
| 11 / BPT+24 | [FALCON floor 掩码，CiC 1(4)](https://cic.iacr.org/p/1/4/9) | 纳入；正式稿选读 |
| 37 / NKO+25 | [任意阶掩码 Gaussian elimination，CT-RSA 2025](https://doi.org/10.1007/978-3-031-88661-4_11) | 纳入；正式摘要与作者稿选读 |
| 39 / P´24 | [One Vector，PQCrypto 2024](https://doi.org/10.1007/978-3-031-62746-0_5) | 相邻代数理论 |
| 40 / PSKH18 | [MQ 签名 CPA，TCHES 2018](https://doi.org/10.46586/tches.v2018.i3.500-523) | 窗口外基础文献；摘要 |
| 41 / P´e24 | [Singular Points，ePrint 2024/219](https://eprint.iacr.org/2024/219) | 相邻代数理论；保留实际被引版本 |
| 45 / SPOG19 | [任意阶掩码二项采样，PKC 2019](https://doi.org/10.1007/978-3-030-17259-6_18) | 窗口外基础文献；摘要与出版页脚注 |

[mUOV 引用清单](../citations/muov2025-reference-screen.jsonl)现为 18 条对应、10 条待查、24 条暂列背景。正式 ACM 参考列表仍未与 NIST 托管稿对照。

## 证明、计时与物理验证分别记录

**UOV SoK。** 正式摘要将历史攻击重新映射到当时规范，强调压缩密钥、随机化选择会改变物理攻击条件。实测说明涉及 UOV/MAYO 的 Cortex-M4 一阶掩码及部分故障防护；不能推成 QR-UOV/SNOVA 同配置实测，也不能把 t 值下降当成全面安全。本批未取得可读作者 PDF，完整评估条件继续待查。[正式摘要](https://link.springer.com/chapter/10.1007/978-3-031-86599-2_7)

**Gaussian elimination。** 作者稿第 21 页把实现限定为概念验证，明确不覆盖微架构泄漏缓解。表 3 的一至三阶数据是周期基准，包含片上 TRNG 开销，不能升级成三阶功耗检测。保护对象是 GE 与回代；全签名组合仍需另证。正式摘要把约 15 倍开销明确归属一阶，作者稿摘要的阶数表述较含糊。31 页作者稿第 1、21–23 页已选读，第 21 页图像已核对；其余证明和参考文献未完整筛查。[作者稿](https://www.cse.iitk.ac.in/users/angshuman/assets/pdf/Masked_GaussianElimination_PQC.pdf)

**FALCON floor。** 正式稿第 18–19 页的测试使用 i7-11800H、GCC 9.4.0；表 6 不含签名拒绝，不能当完整生产签名时延。作者将除法识别为主要瓶颈，并认为该实现还不适于部署。MIMO-SNI/探针模型论证与功耗、电磁实测保证不同，本批未独立核验完整证明。正式稿第 1、18–23 页已选读，第 19 页图像已核对。[正式 PDF](https://cic.iacr.org/p/1/4/9/pdf)

**历史攻击与采样基线。** TCHES 2018 摘要的实测案例是 AVR 上的 Rainbow；对 UOV 的适用条件涉及简单结构的等价密钥，不能直接套用现行所有实现。[MQ 签名论文](https://doi.org/10.46586/tches.v2018.i3.500-523) PKC 2019 出版页脚注 8 则说明周期数排除了输入比特向量生成；与计入随机输入成本的基准比较时必须统一口径。[二项采样论文](https://link.springer.com/chapter/10.1007/978-3-030-17259-6_18)

## 版本与恢复任务不能混同

- One Vector 讨论已知 oil 子空间向量之后的恢复，不能据此声称波形已经提供该向量。正式摘要写最多 13 秒，ePrint 页面写 15 秒；本批记录差异，不选择一个数替代另一个。[正式版](https://link.springer.com/chapter/10.1007/978-3-031-62746-0_5)、[作者版](https://eprint.iacr.org/2023/1131)
- Singular Points 的 mUOV 引用实际指向 ePrint，故引用边连到该版本；另保留 [EUROCRYPT 2025 正式身份](https://doi.org/10.1007/978-3-031-91095-1_11)。作者历史说明修正了 VOX 的恢复复杂度及技术引理，不能把旧稿与新稿看作内容完全相同，也不能扩大为一般 UOV 全部失效。[修订记录](https://eprint.iacr.org/2024/219)
- CiC floor 被 mUOV 和 Maskaglia 引为 2024 年；出版页与 Crossref 给出的在线日期是 2025-01-13，收稿和录用在 2024 年。这些日期分别保存。22 页作者稿与 23 页正式稿的参考文献不同：IEEE 754 条目由 Kahan 笔记换成 2019 标准，BEARZ 由 ePrint 换成 SCITEPRESS 正式 DOI。正式稿仍将三个 NIST DOI 写成 `.ipd`；清单保留这一草案身份，不自动替换为最终 FIPS。[出版记录](https://cic.iacr.org/p/1/4/9)

## 前向追踪补出的方向

CiC 的引用面板给出 Maskaglia 和 ICCD 2025 浮点转换等后续研究；面板自己说明依赖可匹配的 Crossref 引用，不能作为完整前向覆盖。

[Maskaglia，CRYPTO 2026](https://link.springer.com/chapter/10.1007/978-3-032-35415-0_6)已补读完整正式摘要，并核对其参考 5 确实引用 floor 论文。它从均匀/几何分布组织新的拒绝采样结构，摘要讨论固定中心、固定标准差，比较的是 HAWK 用例中的 masked AND 数量；不能直接换算为完整签名加速或推广到 FALCON 可变中心采样。作者 ePrint 明确标为 CRYPTO 2026 小修订版；全文差异仍待核对。[作者版本](https://eprint.iacr.org/2026/988)

[ICCD 2025 整数与浮点转换](https://doi.org/10.1109/ICCD65941.2025.00078)已核实题名、作者、页码及 DOI，尚未读到完整一手摘要和引用正文。它只进入目录与[前向线索表](../citations/falcon-floor-forward-leads.jsonl)，不计入阅读卡片，也不生成已核实引用边。

## 覆盖变化与下一步

[floor 正式参考清单](../citations/falcon-floor-reference-screen.jsonl)共 31 条：10 条对应、11 条待查、10 条暂列背景；[Maskaglia 清单](../citations/maskaglia-selected-reference-screen.jsonl)仅核对第 5 条，不代表全文引用已筛完。新增待查包括旧版 B2A 转换、PINI、BLISS、BEARZ、Isochronous Gaussian Sampling 和 EUROCRYPT 2023 的 Improved Power Analysis Attacks on Falcon。

优先补 SoK 正文的规范版本与检测配置，GE 的正式/作者稿差异，floor 证明及拒绝流程，Maskaglia 分布范围和成本口径。mUOV 第 51 条 UOV 2018 已定位 DOI，但出版页 HTTP 403，搜索摘录不构成完整摘要阅读，继续待查。两条 Crossref 请求的 429 及 SoK PDF 的 403 均保留为访问记录，不当作论文内容。

扩展会议与核心年份的系统普查仍未完成；本批未提高核心会议目录核对数量，不能以引用清单或一致性检查通过宣称无遗漏。
