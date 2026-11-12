# GoFetch：本轮阅读边界

[官方论文页](https://www.usenix.org/conference/usenixsecurity24/presentation/chen-boru) · [正式 PDF](https://www.usenix.org/system/files/usenixsecurity24-chen-boru.pdf)

阅读日期：2026-11-12。已读摘要/引言、§3、§7.1/7.2 的部分目标与概述、§8，以及参考文献 [1]–[98]。没有完整审计攻击推导、表格、附录或复现代码。

作者采用同机非特权进程与正常密码接口交互的威胁模型，不要求共享内存。主要研究 Apple M1；Kyber 目标是 reference Kyber-512，Dilithium 目标是 CIRCL 的确定性 Dilithium-2。参考文献 [37] 注明 CIRCL v1.3.3。其他芯片的 DMP 行为观察不等于全部端到端攻击均跨平台复现；表 1 不含 Dilithium 离线签名收集时间。历史实现结论不能直接推广到所有最终 ML-KEM/ML-DSA 实现。

本项目没有复现这些攻击。下一次精读需核对完整预算、预处理、实现提交、误差处理与防护条件。

本次引用追踪见[进度表](../CITATION_PROGRESS.md)。每条引用有编号与源 PDF 标识，目标论文是否已读另行标注。PDF 仅保存在仓库外；来源 URL、获取时间与 SHA-256 见[来源记录](../provenance/citation-expansion.json)。
