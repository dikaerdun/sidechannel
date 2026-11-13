# TCHES 实现论文：恒时、掩码、功能正确性与性能的边界

日期：2026-11-13。逐条读完冻结候选队列剩余的 86 篇摘要，新增 9 篇纳入卡片、77 条相邻主题判定。对四篇再查看下列正文位置；没有完整读完这些 PDF，没有独立复核证明、审计代码或运行实验。摘要与原始 PDF 缓存在仓库外；[来源与哈希](../provenance/tches-remaining-20261113.json)、[逐条阅读清单](../screening/batches/tches-pqc-remaining-20261113.jsonl)保留在库内。

## 新纳入工作及证据范围

| 工作 | 为什么纳入 | 目前能支持的结论及限制 |
|---|---|---|
| [Multi-moduli NTTs for Saber](https://doi.org/10.46586/tches.v2022.i1.127-151) | 明确包含掩码 Saber 的实现优化 | 摘要报告相对所比 Toom–Cook 基线的性能收益；本次没有得到新增物理泄漏验证的证据 |
| [Racing BIKE](https://doi.org/10.46586/tches.v2022.i1.557-588) | 稀疏乘法器的恒时目标 | 摘要把时间恒定明确关联到封装中的稀疏乘法，不能直接推广到求逆、整套 KEM 或功耗安全 |
| [Classic McEliece FPGA](https://doi.org/10.46586/tches.v2022.i3.71-113) | 恒时实现及提前中止的边界 | 正文需要与随机重试、systematic 变体和成功尝试的范围一起理解，详见下文 |
| [MiRitH](https://doi.org/10.46586/tches.v2024.i2.304-328) | AVX2/NEON 优化实现明确声明恒时 | 摘要未给出物理泄漏验证；MPC-in-the-head 协议参与方不是物理掩码阶数 |
| [HAETAE](https://doi.org/10.46586/tches.v2024.i3.25-75) | 恒时参考实现及侧信道保护设计 | 需继续读防护章节，核对具体组件、假设和实测范围；不能把参考实现的性质转给所有优化版本 |
| [Tailorable codes / ML-KEM](https://doi.org/10.46586/tches.v2025.i3.139-163) | 新压缩译码的等时实现 | 失败率分析、等时译码、物理防护是三类不同证据；修改后的编码不能直接称为未经修改的标准 ML-KEM |
| [HADES](https://doi.org/10.46586/tches.v2025.i4.1-45) | 将安全需求和掩码加入硬件设计空间探索 | 摘要声称支持任意阶掩码；各阶、综合配置和测量覆盖仍待正文与材料核对 |
| [Beneš 网络控制位](https://doi.org/10.46586/tches.v2026.i3.306-333) | 正文明确面向秘密置换的恒时计算 | 摘要没有直接写出恒时目标，正文救回了这一候选；Lean 证明与 C 实现检查的边界必须区分 |
| [Rijndael-256 多平台优化](https://doi.org/10.46586/tches.v2026.i4.575-596) | Cortex-M4 版本明确具有秘密无关控制流与访存 | 摘要同时给出 AArch64、CUDA 性能，但未把相同保证赋予这两个版本；PQC 集成性能是在 Apple M2 上取得 |

## 四次正文范围核查

**Classic McEliece 的提前中止。** 已读[出版商 PDF](https://tches.iacr.org/index.php/TCHES/article/download/9695/9226)第 2–3 页（刊页 72–73）及第 30 页（刊页 100）。作者用失败后重新生成一对密钥解释提前中止；并将 FixedWeight 的恒时表述限定到成功尝试。我们据此记录“有重试边界的实现主张”，不写成“每次完整调用耗时相同”。论文还将 keygen/decap 的实际覆盖限定于 systematic 变体。这里没有独立验证失败状态与最终秘密的关系。

检索到 [ePrint 2022/412](https://eprint.iacr.org/2022/412.pdf) 的修订说明，称 2022 年 9 月版本修正 TCHES 版本勘误；本次下载返回 HTTP 403，勘误内容未读。[NIST 所存另版 PDF](https://csrc.nist.gov/csrc/media/Events/2022/fourth-pqc-standardization-conference/documents/papers/complete-and-improved-fpga-implementation-of-classic-mceliece-pqc2022.pdf)仅检查首页，摘要较短，不能替代修订版，也没有把版本关系标成完成。

**Beneš 网络的数学证明与实现检查。** 已读[出版商 PDF](https://tches.iacr.org/index.php/TCHES/article/download/13094/12645)第 1 页与第 17 页（刊页 306、322）。§4.4 明示 Lean 原型不追求恒时，且 FastCycleMin 经 oSort 实现的部分存在形式验证缺口。§5 的便携 C/AVX2 实现使用 cryptoint、DOIT 指令约束及 Valgrind；其中 Valgrind 对应分支和访存两项检查。不能把这些拼成端到端恒时证明，更不能升级为物理泄漏安全。

**Kyber 功能正确性论文保留在相邻主题。** 已读 [Episode IV PDF](https://tches.iacr.org/index.php/TCHES/article/download/10960/10267)第 4、26 页（刊页 167、189）。作者将恒时及 Spectre v1 防护指向另一篇研究和后续结合；还区分了完全优化与已验证的 AVX2 拒绝采样版本、SHA3 证明边界、内存安全检查与可信基础。仅凭 Jasmin 或“形式化验证”标签，不能把本篇直接纳入为已完成实现侧信道证明。

**Verified NTT 仍是正确性背景。** 已读[出版商 PDF](https://tches.iacr.org/index.php/TCHES/article/download/9838/9341)首页及已存摘要，覆盖 CryptoLine 对六种汇编乘法的代数正确性和范围检查。正文关键词搜索只用于导航，不作为全文阅读或“全文不存在侧信道内容”的证据。

## 保留相邻论文，继续检查潜在遗漏

77 条相邻判定都带有逐篇理由和阅读深度；它们没有被永久排除。尤其需要再读正文的对象包括：

- **Nibbling MAYO、Low-Stack HAETAE：**查表/数据表示变化、提前拒绝和分阶段采样是否保留原实现的安全边界。
- **Hybrid Parallel SHA-3：**跨拒绝轮次预计算改变哪些随机数消费和状态驻留关系；摘要本身没有证明存在泄漏。
- **OpenTitan 向量乘法、PHOENIX、SHARMONY：**优化或共享的是哪些物理资源，原保护边界有没有被改变；不能从平台名称或共享设计本身推定安全或漏洞。
- **RRAM NTT：**实测电阻、量化精度及阵列干扰是计算可靠性证据；是否含秘密相关可观测量，需另行建立变量和测量模型。

另有三个容易误判的词义：TFHE 的 *common mask* 是密文格式中的共享随机部分；*field trace* 是代数域迹；*constant multiplier* 是常数乘法硬件。它们都不能单凭词名转成物理掩码、测量波形或恒时保证。

冻结的 168 条补读队列现在都有摘要及以上判定。这不等于 TCHES 全文筛查完成，更不等于安全顶会与引用扩展没有遗漏。下一步仍需做非关键词候选阅读、重点全文和引用追踪，以及独立目录核对。
