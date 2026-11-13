# MPCitH 与 FAEST 修订及证据范围

阅读日期：2026-11-13。本批新增 16 条卡片，解析 SDitH 的五条发现，并筛查 SDitH、FAEST 攻击与 HQC 有效密文攻击的参考列表。来源时间、哈希和访问状态见[来源记录](../provenance/mpcith-followup-20261113.json)。作者结果没有在本地复现。

## FAEST 当前修订撤回了掩码实现

[ePrint 2025/1261](https://eprint.iacr.org/2025/1261)的当前题名为 *FAEST for Memory-Constrained Devices*。2026-06-29 修订说明明确撤回掩码实现，原因是审稿人发现攻击；低内存优化仍保留。当前摘要描述 FAEST v1.1、Cortex-M4、VOLE 重算与复用以及恒时实现。

SDitH 和 CiC 的参考文献仍使用含 *with Side-Channel Protections* 的历史题名。知识库保留这一别名及被引标题，不把旧防护主张沿用到当前版本。PDF 和历史页返回 403，尚未阅读引言末尾的 Disclaimer 或逐版对照。不能据此认定是哪篇公开攻击导致撤回，也不能自动否定引用它的 SDitH 论文自身结果。

## CiC 单迹线攻击仍有训练与枚举成本

[Side-Channel Attacks on VOLEitH Signature Schemes: Breaking Masked FAEST](https://doi.org/10.62056/aebngyl7s)于 2026-01-08 发表在 IACR CiC。它与库中 TCHES 的 *Fault Attacks on VOLEitH Signature Schemes* 分开登记，不能凭相近题名合并被动测量和主动故障证据。

已读正文指定页包括 2–3、8–9、12–13、17–22 页，表 5 已视读。实验对象为第一轮掩码实现，两个 Cortex-M4 设备分别用于剖析和测试；每种方法使用 5000 条剖析迹线。切出的训练片段数量不等于独立采集数。表 5 无额外加噪列报告两方法成功 998/1000 和 1000/1000，附带候选枚举；其中第二方法最多枚举 32 个不确定比特，对应最多 2^32 个候选，而非枚举 2^32 个比特。

σ=0 表示未额外加入高斯噪声，不能称作无噪硬件。其他噪声列来自给已有迹线加噪。第 18 页明确说明：利用公开的非活动 VOLE 标签开展未知密钥自剖析，是未做实验的策略。第二轮方案的适用性也只作讨论，不能当作第二轮实测恢复。

[作者仓库 README](https://github.com/KTH-HWSEC/breaking-masked-faest/blob/main/README.md)列出训练和测试脚本，但数据与预训练模型需向作者申请。仅读 README，未检查或执行脚本，未下载数据。

## MPCitH 保护需要区分协议与实现

| 条目 | 主要贡献 | 当前证据边界 |
|---|---|---|
| [Picnic DPA](https://doi.org/10.1007/978-3-030-81293-5_10) | 利用 MPC-LowMC 泄漏恢复秘密 | 摘要报告少于 1000 条 LowMC 迹线，来自少于 30 个 Picnic 签名；两个计数单位不同 |
| [Godard 等的单迹线 TCitH](https://doi.org/10.1007/978-3-031-86602-9_10) | 有限域乘法泄漏与多项式约束相结合 | 摘要报告 HW 模拟及 STM32F407；训练预算与正文未核查，不能推广到所有 MPCitH |
| [HYPERSHIELD](https://eprint.iacr.org/2026/081) | 修改 Hypercube 协议的隐藏份额及种子揭示方式 | 差分探测阶数及参数权衡；不是透明实现替换，传统全掩码比较值包含估算 |
| [SNI-in-the-head](https://doi.org/10.1145/3372297.3417889) | 用平衡 SNI 组件构造受保护 ZKBoo 协议 | DPA 演示为模拟，实际实现性能不等于物理采集验证 |

Picnic ePrint 2020/267 和 SNI ePrint 2020/544 有作者显式出版说明。Godard 的 ePrint 2024/1882 与 PQCrypto 2025 标题、作者和摘要匹配，但页面未明示正式关系，保留为推定。任何书目关系都不等于全文完全相同。

## 基础文献和时间边界

补入九条通用基础卡片：CCS 2016 SNI、Keccak 2010 掩码、EUROCRYPT 2020 PRG 掩码、CARDIS 2017 Higher Criticism、TVLA 2011、DSD 2017 Keccak、CRYPTO 2003 Private Circuits、TCHES 2020 单迹线 Keccak，以及 CRYPTO 1999 DPA。它们用于理解新论文的模型和证据，不混入近五年核心会议年度统计。

- [Keccak 2020](https://doi.org/10.46586/tches.v2020.i3.243-268)采用带噪 HW 模拟；不能描述成微控制器实测攻击。
- [TVLA 工作坊论文](https://csrc.nist.gov/CSRC/media/Events/Non-Invasive-Attack-Testing-Workshop/documents/08_Goodwill.pdf)只读前两页。它明确区分检出泄漏与完整恢复，也不保证所有攻击安全；不是正式 NIST 标准。被引卷页未获原始出版物核实，不用 PDF 页数替代。
- [CCS 2016 SNI 作者稿](https://eprint.iacr.org/2015/506)明示经过大幅重写；[DSD 2017 Keccak 作者稿](https://eprint.iacr.org/2017/395)明示小修订；[MQOM 作者稿](https://eprint.iacr.org/2026/078)明示 TCHES 大修订。关系登记与证明核验分开。
- [Higher Criticism 章节](https://doi.org/10.1007/978-3-319-75208-2_7)属于 CARDIS 2017，2018-01-26 上线。Picnic DPA 于 2021-07-15 上线，早于滚动起点 2021-11-12，仍作为 2021 年边界基础文献保留。

## HQC 有效密文攻击形成新的引用分支

[Et tu, Brute?](https://doi.org/10.1007/978-3-031-86602-9_11)研究只使用有效密文的侧信道辅助攻击，分析依靠无效密文检测及密钥刷新进行保护的局限。摘要针对 Reed-Muller 译码的 ExpandAndSum、FindPeaks 以及打乱扩展报告恢复结果。

本批只读出版方摘要和全部 30 条参考文献。具体硬件、采集预算、HQC 版本与全文条件尚未核查；摘要的 100% 成功率属于作者测试配置，不能用于普遍排名或推断最终标准实现均受影响。

## 引用清单与下一步

| 来源 | 已筛查参考条目 | 已连目录 | 新待核查 | 暂列背景 |
|---|---:|---:|---:|---:|
| [SDitH](../citations/sdith2026-reference-screen.jsonl) | 27 | 21 | 0 | 6 |
| [CiC FAEST 攻击](../citations/faest-cic2026-reference-screen.jsonl) | 38 | 7 | 12 | 19 |
| [HQC 有效密文攻击](../citations/hqc-valid2025-reference-screen.jsonl) | 30 | 8 | 11 | 11 |

背景判定仅基于引用条目，不是原文最终排除。本批新增 31 条引用边；表中另有五条此前已对应的 SDitH 引用。旧 USENIX 选读文件仅保留 ML-KEM 的两条，避免重复计算 SDitH。

23 条新发现包括 PQCrypto/CARDIS 的 HQC 攻击、MAYO、FALCON Down、受保护 Kyber/Saber、信息集译码提示和若干早期掩码工作。下一步先核对原始摘要、会议与出版年、版本关系，再补全文。HQC 引用 30 的年份疑点、FPS/CARDIS/SAC 的会议与上线年份差异必须保留。

全库引用闭合、前向追踪及扩展会议目录均未完成。没有运行作者代码、训练或实验；文档一致性检查不能证明论文无遗漏。
