# 增补来源索引

2026-11-13 第四批构思增补：[清理轨迹、编排测量与整体结构](brainstorms/2026-11-12-observation-as-computation.md) 文末记录 OpenSSL RNG 分析、软件掩码实际评估、打乱执行研究、PhaseLift 与拒绝签名攻击的实际阅读范围。仅摘要/元数据与列明的原文搜索片段；未复现、未完成新颖性审查，不改变系统文献库数量。

2026-11-12 第三批构思增补：[模型反例、格的几何与物理同步](brainstorms/2026-11-12-model-breaking-directions.md) 文末记录 Scam-V、DDGR、distribution hints、2026/2654 结构化提示预印本、PhaseSCA 与 RO 注入锁定的定位性阅读范围。摘要阅读、PDF 局部阅读和直接访问失败分开记录；未进行全文普查或结果复现。

2026-11-13 文献更新：系统文献收集统一放在[近五年文献库](literature/README.md)。其中[覆盖表](literature/COVERAGE.md)区分目录提取、标题初筛、摘要及以上判定与引用追踪；[105 篇卡片](literature/PAPER_NOTES.md)记录实际阅读范围；[7 条相邻主题](literature/ADJACENT_NOTES.md)记录未纳入理由；[引用与版本进度](literature/CITATION_PROGRESS.md)记录补漏和版本差异。本批实际来源、缓存哈希和 web 读取边界见[来源记录](literature/provenance/citation-followup-20261113.json)。下列历史 SRC 编号、数据来源和旧阅读层级保留，不因新目录建立而自动升级。

核查日期：2026-11-07。与[既有证据索引](../evidence-matrix.md)互补，不改变原索引的信息截点。核查范围按条目分别标注：SRC-001 已读 §1–4 并下载了发布包中的 12 个成员（波形/标签）与公开加载器，核了归档中央目录元数据；SRC-002 仅摘要页；SRC-003 仅摘要页与图 8(a)。**没有任何一项复现了作者实验**，也没有下载完整 3.6 GB 归档的成员内容。

| ID | 原始来源 | 可从当前阅读范围确认的内容 | 后续必须核查 |
|---|---|---|---|
| SRC-001 | [Side-Channel Power Trace Dataset for Kyber Pair-Pointwise Multiplication on Cortex-M4](https://eprint.iacr.org/2025/811) · [数据](https://doi.org/10.5281/zenodo.15352482) | 作者描述了 PQClean 参考实现中 Kyber 解封装 NTT 域成对逐点乘法的功耗数据；页面修订日期 2025-06-04。**2026-11-07 本地实测核查**：Zenodo 记录 CC BY 4.0；归档中央目录 2001 条 = 1 目录 + 1000 `tracesA*.mat` + 1000 `noncesA*.mat`，无 ELF/反汇编/固件/会话日志/增益元数据；已下载 12 个成员的长度、CRC32、SHA-256 与 manifest 一致；六字格式 LE signed16，a 系数常值，第 2 字=第 5 字，两个 Montgomery 返回与本地编译 PQClean `0586a824` C 逐字匹配；文件号不是会话标识 | 数据实际入口、数据许可证、文件校验、实现提交、标签、会话/密钥/器件组成；与最终 ML-KEM 的对应（已在 2026-11-07 批次完成入口/许可/校验/标签字级核对；会话与采集固件仍未知） |
| SRC-002 | [Template and CPA Side Channel Attacks on the Kyber/ML-KEM Pair-Pointwise Multiplication](https://eprint.iacr.org/2025/1577) | 作者基于 SRC-001 报告模板及 CPA 方法与解封装秘密子密钥恢复；页面最新修订日期 2026-02-05 | 全文的恢复对象、训练和攻击预算、完整实现范围、评价协议及可复现材料 |
| SRC-003 | [Release the Power of Rejected Signatures](https://eprint.iacr.org/2025/582) | 作者报告在统一因子图中结合接受与拒绝尝试的泄漏，并在 Cortex-M4 参考及 ASM 实现上实验；页面最新修订日期 2025-12-15 | 全文变量可观测性、每次尝试的状态绑定、实验预算、实现版本和跨条件表现 |
| SRC-004 | [OpenAI 多代理指导](https://developers.openai.com/api/docs/guides/responses-multi-agent) | 独立任务上下文、委派和协调是工具能力；共享资源需要协调 | 实际使用环境是否支持子代理和上下文控制；记录实际能力，不能以文档替代运行检查 |

标准入口：[FIPS 203 / ML-KEM](https://csrc.nist.gov/pubs/fips/203/final)、[FIPS 204 / ML-DSA](https://csrc.nist.gov/pubs/fips/204/final)。开始实验时固定所用标准版本、勘误和实现；这里未对标准正文重新逐条核验。

补充记录：本批另核了作者公开加载器（912 字节 ZIP，MD5 `1cf6ecb6d3bdbfdeffb6e4ea6b925a58`，与 Zenodo 记录一致）与 SRC-001 的 §1–4；加载器只并列读取两个数组，无会话/随机化/仪器字段。上述实测核查仅限已下载的 12 个成员与归档目录元数据，**不是**对 3.6 GB 归档全部内容的复现。

## 引用纪律
- “作者报告”不等于“本项目已复现”；摘要页没有提供的字段保留未知。
- 历史 Kyber/Dilithium 实现结论不能不经比对就扩展为全部最终 ML-KEM/ML-DSA 实现结论。
- 论文页面许可证不自动证明关联数据集采用同一许可证。
- 不用未经核验的轨迹数字对算法或方法排名；本索引不引入此类数字。
- 后续精读记录版本、页码/章节、原文主张、平台与预算、复现材料位置、反例和适用边界。
- 新论文先查重；更新旧条目的证据范围时保留变更记录。
