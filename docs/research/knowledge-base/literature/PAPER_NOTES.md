# 已阅读论文卡片

状态：持续整理，尚未覆盖全部相关论文。按每篇实际阅读层级报告；作者报告不等于本地复现。

当前 139 篇；按 DOI 或官方页面关联目录，边界论文继续保留。

## Share-slicing: Friend or Foe?

- 来源：[TCHES 2020](https://doi.org/10.46586/tches.v2020.i1.152-174)；时间标记：foundation outside rolling window; TCHES volume 2020(1), online 2019-11-19。
- 作者：Si Gao; Ben Marshall; Dan Page; Elisabeth Oswald
- 对象：software masking, share slicing, ISW, bit interaction, ARM Cortex-M0/M3；类型：leakage_model_and_evaluation。
- 核心想法：检验同一机器字内份额的逐位独立假设，研究微架构位交互如何降低预期掩码阶数。
- 作者报告：作者在 NXP LPC Cortex-M0/M3 上报告位交互和安全阶数下降；结论指出具体物理原因仍难唯一定位。
- 限制与下一步：证明的前提与实现不匹配不等于证明本身错误；器件、指令方向、重复与平均条件不可省略。正文讨论重复带来的观测成本，README 另述不同测试设置，不能合并为同一组实验或任意平台结论。
- 阅读层级：selected_full_text_sections；来源：https://tches.iacr.org/index.php/TCHES/article/download/8396/7780。
- 已读章节：TCHES landing-page abstract; PDF pp.16–17 (printed pp.167–168): repetition/SNR limitations, sections 5–6
- [详细阅读记录](notes/power-observation-and-pqc-boundaries-20261113.md)
- 代码/数据核查：author README fully read; explicit no security claim for the supplied AES implementation and distinct supplemental setup; source/data files and build not verified；引用追踪：forward citation observed; exhaustive backward/forward closure pending。

## Red Alert for Power Leakage: Exploiting Intel RAPL-Induced Side Channels

- 来源：[ASIACCS 2021](https://doi.org/10.1145/3433210.3437517)；时间标记：before rolling window; online 2021-05-24; retained as cited 2021 boundary paper。
- 作者：Zhenkai Zhang; Sisheng Liang; Fan Yao; Xing Gao
- 对象：RAPL, software power observation, website fingerprinting, covert channel；类型：attack。
- 核心想法：利用软件可读的 RAPL 能量信息构造跨隔离隐蔽通道并进行网站指纹识别。
- 作者报告：作者报告跨软件/硬件边界通信及普通浏览器、Tor 场景下的页面辨识。
- 限制与下一步：不是密码密钥恢复；依赖可访问相应 RAPL 读数，2021 年接口条件不能外推为当前系统默认权限。正式上线 2021-05-24，早于滚动窗口，作为边界引用保留。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://zhenkai-zhang.github.io/papers/rapl.pdf。
- 代码/数据核查：not checked；引用追踪：forward citation observed; exhaustive backward/forward closure pending。

## A Systematic Approach and Analysis of Key Mismatch Attacks on Lattice-Based NIST Candidate KEMs

- 来源：[ASIACRYPT 2021](https://doi.org/10.1007/978-3-030-92068-5_4)；时间标记：formal publication within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Yue Qin; Chi Cheng; Xiaohan Zhang; Yanbin Pan; Lei Hu; Jintai Ding
- 对象：lattice KEMs, key mismatch, PC oracle；类型：method。
- 核心想法：把最少平均查询问题组织为最优二叉恢复树，用 Shannon 熵解释查询下界并改进策略。
- 作者报告：作者报告查询策略实验，并讨论改进 CCA KEM 侧信道攻击的应用。
- 限制与下一步：预言机查询效率不自动给出物理预言机实现；正式版 2021-12 上线，预印本首次为 2021-02，窗口标记分开。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://eprint.iacr.org/2021/123。
- 代码/数据核查：not checked；引用追踪：forward edge observed; backward and exhaustive forward search pending。

## Single-Trace Side-Channel Attacks on ω-Small Polynomial Sampling: With Applications to NTRU, NTRU Prime, and CRYSTALS-DILITHIUM

- 来源：[HOST 2021](https://doi.org/10.1109/host49136.2021.9702284)；时间标记：inside rolling window; HOST 2021-12-12。
- 作者：Emre Karabulut; Erdem Alkim; Aydin Aysu
- 对象：NTRU, NTRU Prime, Dilithium；类型：attack。
- 核心想法：研究固定重量小多项式采样中的排序/打乱过程泄漏。
- 作者报告：摘要报告 Cortex-M4 单迹读出：NTRU/NTRU Prime 的系数信息，以及 Dilithium 被拒绝挑战多项式的符号信息。
- 限制与下一步：不能把 Dilithium 挑战熵减少写成单迹完整私钥恢复；剖析预算、剩余搜索与实际完整恢复条件待精读。会议为 2021 年，ePrint 上传于 2022 年。
- 阅读层级：abstract_and_bibliographic_metadata；来源：ePrint abstract with explicit HOST publication DOI: https://eprint.iacr.org/2022/494。
- 代码/数据核查：not checked；引用追踪：forward edge observed; backward and exhaustive forward search pending。

## An Efficient Non-Profiled Side-Channel Attack on the CRYSTALS-Dilithium Post-Quantum Signature

- 来源：[ICCD 2021](https://doi.org/10.1109/iccd53106.2021.00094)；时间标记：earlier boundary paper; ICCD October 2021。
- 作者：Zhaohui Chen; Emre Karabulut; Aydin Aysu; Yuan Ma; Jiwu Jing
- 对象：Dilithium；类型：attack。
- 核心想法：针对多项式逐点乘法设计缩小猜测空间的 CPA，结合两阶段筛选与保守恢复方案。
- 作者报告：摘要与引言报告参考实现的功耗实验及混合策略的计算加速。
- 限制与下一步：单个系数的统计置信度不等于完整密钥恢复概率；总恢复成本、固件版本与跨设备条件待正文核查。
- 阅读层级：selected_full_text_sections；来源：author PDF abstract and introduction: https://research.ece.ncsu.edu/wp-content/uploads/sites/8/Dilithium_SCA_cameraready.pdf。
- 已读章节：author PDF pages 1–2: abstract and introduction/contributions; other sections not fully read
- 代码/数据核查：not checked；引用追踪：forward edge observed; backward and exhaustive forward search pending。

## Opening Pandora’s Box: A Systematic Study of New Ways Microarchitecture Can Leak Private Data

- 来源：[ISCA 2021](https://doi.org/10.1109/isca52012.2021.00035)；时间标记：earlier boundary paper。
- 作者：Jose Rodrigo Sanchez Vicarte; Pradyumna Shome; Nandeeka Nayak; Caroline Trippel; Adam Morrison; David Kohlbrenner; Christopher W. Fletcher
- 对象：microarchitectural optimizations, data-dependent prefetchers；类型：model_analysis。
- 核心想法：从架构文献系统梳理七类优化的泄漏可能性，并提出概念框架。
- 作者报告：作者报告若干 PoC，强调包括非投机机制在内的新型观察通道。
- 限制与下一步：部分对象是文献设计、专利或实现状态不确定的优化；不等于七类均在商业芯片上被实测。2021-06 作为窗口前边界引用保留。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://homes.cs.washington.edu/~dkohlbre/papers/pandora.pdf。
- 代码/数据核查：not checked；引用追踪：forward edge observed; backward and exhaustive forward search pending。

## A Side-Channel Attack on a Masked IND-CCA Secure Saber KEM Implementation

- 来源：[TCHES 2021](https://doi.org/10.46586/tches.v2021.i4.676-707)；时间标记：earlier boundary paper。
- 作者：Kalle Ngo; Elena Dubrova; Qian Guo; Thomas Johansson
- 对象：Saber；类型：attack。
- 核心想法：以剖析神经网络学习高阶泄漏，并用容错恢复方法连接消息与长期秘密。
- 作者报告：摘要报告对一阶掩码 Saber 的攻击和逻辑移位泄漏点。
- 限制与下一步：剖析能力、消息误差模型及会话秘密与长期秘密恢复条件需分别核对。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Analysis and Comparison of Table-based Arithmetic to Boolean Masking

- 来源：[TCHES 2021](https://doi.org/10.46586/tches.v2021.i3.275-297)；时间标记：earlier boundary paper。
- 作者：Michiel Van Beirendonck; Jan-Pieter D’Anvers; Ingrid Verbauwhede
- 对象：A2B conversion, lattice-based cryptography；类型：attack_and_countermeasure。
- 核心想法：指出 Debraize 表式 A2B 转换中间量分布不均匀导致泄漏，并提出两种修复。
- 作者报告：作者给出解析与实验分析及 Cortex-M4 测试，比较存储和速度折衷。
- 限制与下一步：有限功耗测试未检出不能当作所有阶数和攻击下的安全证明；通用转换与具体 PQC 集成范围分开。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Attacking and Defending Masked Polynomial Comparison for Lattice-Based Cryptography

- 来源：[TCHES 2021](https://doi.org/10.46586/tches.v2021.i3.334-359)；时间标记：earlier boundary paper。
- 作者：Shivam Bhasin; Jan-Pieter D’Anvers; Daniel Heinz; Thomas Pöppelmann; Michiel Van Beirendonck
- 对象：FO transform, masked polynomial comparison；类型：attack。
- 核心想法：分析两种掩码比较的第一阶泄漏，另指出高阶比较中的无侧信道碰撞攻击。
- 作者报告：作者提出针对 FO 重加密的参数化 t-test 框架，覆盖比较及完整解封装。
- 限制与下一步：必须区分物理泄漏攻击和不需要侧信道的碰撞攻击；不同被攻击方案的条件不能合并。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Batching CSIDH Group Actions using AVX-512

- 来源：[TCHES 2021](https://doi.org/10.46586/tches.v2021.i4.618-649)；时间标记：earlier boundary paper。
- 作者：Hao Cheng; Georgios Fotiadis; Johann Großschädl; Peter Y. A. Ryan; Peter B. Rønne
- 对象：CSIDH, CSIDH-512, AVX-512；类型：constant_time_implementation。
- 核心想法：将恒时 CSIDH-512 群作用批处理并映射到 SIMD，分别优化吞吐率和延迟。
- 作者报告：作者比较混合批处理与双路向量化，在 Intel AVX-512 平台上报告性能。
- 限制与下一步：吞吐与单次延迟不是同一指标；恒时范围、批次状态与物理泄漏需正文核查，CSIDH 不等同于 SIKE。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## CTIDH: faster constant-time CSIDH

- 来源：[TCHES 2021](https://doi.org/10.46586/tches.v2021.i4.351-387)；时间标记：earlier boundary paper。
- 作者：Gustavo Banegas; Daniel J. Bernstein; Fabio Campos; Tung Chou; Tanja Lange; Michael Meyer; Benjamin Smith; Jana Sotáková
- 对象：CSIDH, CTIDH；类型：constant_time_implementation。
- 核心想法：联合设计新的 CSIDH 密钥空间和恒时群作用算法。
- 作者报告：作者报告组合设计相对既有恒时实现的运算和周期改进。
- 限制与下一步：恒时性质不等于功耗或电磁安全；CSIDH 不等同于 SIKE，需保留具体参数与实现。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Chosen Ciphertext k-Trace Attacks on Masked CCA2 Secure Kyber

- 来源：[TCHES 2021](https://doi.org/10.46586/tches.v2021.i4.88-113)；时间标记：earlier boundary paper。
- 作者：Mike Hamburg; Julius Hermelink; Robert Primas; Simona Samardjiska; Thomas Schamberger; Silvan Streit; Emanuele Strieder; Christine Van Vredendaal
- 对象：Kyber, inverse NTT；类型：attack。
- 核心想法：用选择密文制造稀疏逆 NTT 输入，改善针对长期秘密的有噪推断。
- 作者报告：作者在 noisy Hamming weight 模型下比较 k、2k 和单迹变体，包括掩码情况。
- 限制与下一步：摘要的噪声阈值是指定泄漏模型下结果，不能写成真实硬件实测；各变体条件与轨迹数不同。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Classic McEliece on the ARM Cortex-M4

- 来源：[TCHES 2021](https://doi.org/10.46586/tches.v2021.i3.125-148)；时间标记：earlier boundary paper。
- 作者：Ming-Shing Chen; Tung Chou
- 对象：Classic McEliece, Cortex-M4；类型：constant_time_implementation。
- 核心想法：在 SRAM 不足以容纳公钥的 Cortex-M4 上实现恒时 Classic McEliece，使用 flash 存储公钥。
- 作者报告：作者报告多个参数集的封装/解封装周期，以及部分参数集的密钥生成支持。
- 限制与下一步：不同参数集的实现操作覆盖不同；恒时与功耗、电磁、flash 访问的物理安全分开核查。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Compact Dilithium Implementations on Cortex-M3 and Cortex-M4

- 来源：[TCHES 2021](https://doi.org/10.46586/tches.v2021.i1.1-24)；时间标记：earlier boundary paper。
- 作者：Denisa O. C. Greconici; Matthias J. Kannwischer; Daan Sprenkels
- 对象：Dilithium, Kyber, NewHope, Cortex-M3, Cortex-M4；类型：constant_time_implementation。
- 核心想法：实现 Cortex-M3 的恒时 Dilithium，并优化 Cortex-M4 上的 NTT 及速度与栈空间折衷。
- 作者报告：作者报告不同签名调度的资源折衷，并提供 Cortex-M3 的 Kyber/NewHope 实现。
- 限制与下一步：恒时声明不等于功耗安全；其他算法的保护范围不能由 Dilithium 声明外推。2021 卷首期实际于 2020-12 发表，作为窗口外边界条目保留。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Masking Kyber: First- and Higher-Order Implementations

- 来源：[TCHES 2021](https://doi.org/10.46586/tches.v2021.i4.173-214)；时间标记：earlier boundary paper。
- 作者：Joppe W. Bos; Marc Gourjon; Joost Renes; Tobias Schneider; Christine Van Vredendaal
- 对象：Kyber；类型：countermeasure。
- 核心想法：提出高阶压缩与掩码多项式比较方法，构造 Kyber 掩码实现。
- 作者报告：摘要报告 Cortex-M0+/M4F 性能、局部实测评估与 scVerif 验证。
- 限制与下一步：需要全文核对各安全阶数的证明模型和实测覆盖；有限迹线未检出不等于任意攻击安全。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Optimizing BIKE for the Intel Haswell and ARM Cortex-M4

- 来源：[TCHES 2021](https://doi.org/10.46586/tches.v2021.i3.97-124)；时间标记：earlier boundary paper。
- 作者：Ming-Shing Chen; Tung Chou; Markus Krausz
- 对象：BIKE, Intel Haswell, Cortex-M4；类型：constant_time_implementation。
- 核心想法：针对 Haswell 和 Cortex-M4 设计两种恒时 BIKE 实现，结合算法与指令优化。
- 作者报告：作者分别与 BIKE 团队 avx2 和非恒时 portable 实现比较性能。
- 限制与下一步：M4 基线为非恒时实现，不能把跨基线倍率直接当成同安全条件比较；未据摘要认定功耗防护。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Rainbow on Cortex-M4

- 来源：[TCHES 2021](https://doi.org/10.46586/tches.v2021.i4.650-675)；时间标记：earlier boundary paper。
- 作者：Tung Chou; Matthias J. Kannwischer; Bo-Yin Yang
- 对象：Rainbow, bitsliced field arithmetic, Cortex-M4；类型：constant_time_component。
- 核心想法：实现 Rainbow 的恒时位切片有限域乘法，并优化公开映射验证和秘密的位切片表示。
- 作者报告：作者在 Giant Gecko Cortex-M4 平台上比较历史 NIST 候选的签名与验证周期。
- 限制与下一步：摘要明确的是乘法组件恒时，不能提升为整个签名实现的物理安全；历史候选性能不构成今天的部署推荐。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Side-Channel Protections for Picnic Signatures

- 来源：[TCHES 2021](https://doi.org/10.46586/tches.v2021.i4.239-282)；时间标记：earlier boundary paper。
- 作者：Diego F. Aranha; Sebastian Berndt; Thomas Eisenbarth; Okan Seker; Akira Takahashi; Luca Wilke; Greg Zaverucha
- 对象：Picnic, Picnic3, MPC-in-the-head；类型：countermeasure。
- 核心想法：分析带预处理的 MPC-in-the-head 签名掩码，并修补已有保护对 Picnic3 的不足。
- 作者报告：作者给出任意阶非干扰论证及 Cortex-M4 一阶实现，评估不同哈希保护选择。
- 限制与下一步：形式证明阶数与实测实现阶数不同；需逐项核对哈希调用保护范围及互操作条件。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Branch Different - Spectre Attacks on Apple Silicon

- 来源：[DIMVA 2022](https://doi.org/10.1007/978-3-031-09484-2_7)；时间标记：formal publication within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Lorenz Hetterich; Michael Schwarz
- 对象：Apple ARMv8, Spectre-PHT；类型：attack。
- 核心想法：为 Apple 平台构造计时和驱逐集合原语，再建立跨核隐蔽信道及 Spectre-PHT。
- 作者报告：出版商摘要报告非特权应用的驱逐集合生成及 iPhone 演示。
- 限制与下一步：隐蔽信道和真实受害者侧信道分开；平台与补丁时点必须保留，不是 PQC 密钥恢复结果。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://link.springer.com/chapter/10.1007/978-3-031-09484-2_7。
- 代码/数据核查：not checked；引用追踪：forward edge observed; backward and exhaustive forward search pending。

## PACMAN: attacking ARM pointer authentication with speculative execution

- 来源：[ISCA 2022](https://doi.org/10.1145/3470496.3527429)；时间标记：formal publication within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Joseph Ravichandran; Weon Taek Na; Jay Lang; Mengjia Yan
- 对象：ARM pointer authentication, Apple M1；类型：attack。
- 核心想法：将内存破坏能力与投机执行侧信道组合，泄漏 PAC 校验结果而不产生架构级崩溃。
- 作者报告：作者报告 Apple M1 和跨特权层 PoC，并研究 TLB 结构。
- 限制与下一步：绕过 Pointer Authentication 需要相关软件漏洞及攻击原语；不能理解为无前提任意内存入侵，也不是 PQC 攻击。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://dspace.mit.edu/server/api/core/bitstreams/f81a1533-d11a-4483-b921-d98c783830e2/content。
- 代码/数据核查：not checked；引用追踪：forward edge observed; backward and exhaustive forward search pending。

## Profiling Side-Channel Attacks on Dilithium: A Small Bit-Fiddling Leak Breaks It All

- 来源：[SAC 2022](https://doi.org/10.1007/978-3-031-58411-4_1)；时间标记：inside rolling window; SAC 2022, publication online 2024-05-12。
- 作者：Vincent Quentin Ulitzsch; Soundes Marzougui; Mehdi Tibouchi; Jean-Pierre Seifert
- 对象：Dilithium；类型：attack。
- 核心想法：利用签名中的位解包泄漏，将剖析读数与最小二乘、整数线性规划结合。
- 作者报告：作者报告 Cortex-M4 上恢复足以签署任意消息的等价秘密信息。
- 限制与下一步：等价签名能力不等于逐字恢复原始私钥。SAC 2022 的正式章节于 2024 年上线；预印本与正式版作者排序不同，全文等价尚未核对。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher abstract and ePrint 2022/106 abstract: https://link.springer.com/chapter/10.1007/978-3-031-58411-4_1。
- 代码/数据核查：not checked；引用追踪：forward edge observed; backward and exhaustive forward search pending。

## A Constant-time AVX2 Implementation of a Variant of ROLLO

- 来源：[TCHES 2022](https://doi.org/10.46586/tches.v2022.i1.152-174)；时间标记：formal publication within rolling window。
- 作者：Tung Chou; Jin-Han Liou
- 对象：ROLLO+, ROLLO-I；类型：constant_time_implementation。
- 核心想法：提出 ROLLO-I 的 CPA 变体 ROLLO+ 并实现恒时 AVX2 版本，指出先前实现的恒时声明问题。
- 作者报告：作者报告 Skylake 上的性能与已有实现比较。
- 限制与下一步：算法变体及 IND-CPA 目标不能等同原 ROLLO 或 IND-CCA KEM；恒时不等于功耗/电磁安全。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## A Key-Recovery Side-Channel Attack on Classic McEliece Implementations

- 来源：[TCHES 2022](https://doi.org/10.46586/tches.v2022.i4.800-827)；时间标记：formal publication within rolling window。
- 作者：Qian Guo; Andreas Johansson; Thomas Johansson
- 对象：Classic McEliece；类型：attack。
- 核心想法：利用特殊输入和加法 FFT 泄漏识别秘密置换的局部条目，再组合恢复。
- 作者报告：摘要报告 FPGA 与 ARM Cortex-M4 上的功耗实验。
- 限制与下一步：依赖所述输入能力与分类模型；部分恢复和完整恢复需分别记录。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Bitslicing Arithmetic/Boolean Masking Conversions for Fun and Profit: with Application to Lattice-Based KEMs

- 来源：[TCHES 2022](https://doi.org/10.46586/tches.v2022.i4.553-588)；时间标记：formal publication within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Olivier Bronchain; Gaëtan Cassiers
- 对象：Kyber, Saber, bitsliced masking conversion；类型：countermeasure。
- 核心想法：用位切片加速任意阶掩码加法及 A2B/B2A 转换，覆盖模幂次及一般模数。
- 作者报告：作者实现 Cortex-M4 的 Kyber768/Saber，指出掩码 Keccak 成为瓶颈。
- 限制与下一步：支持任意阶的构造与逐阶实测范围不同；完整性能比较须保留随机数和哈希成本。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Complete and Improved FPGA Implementation of Classic McEliece

- 来源：[TCHES 2022](https://doi.org/10.46586/tches.v2022.i3.71-113)；时间标记：formal publication within rolling window。
- 作者：Po-Jen Chen; Tung Chou; Sanjay Deshpande; Norman Lahr; Ruben Niederhagen; Jakub Szefer; Wen Wang
- 对象：Classic McEliece, FPGA, early-abort systemization；类型：constant_time_implementation。
- 核心想法：实现第三轮 Classic McEliece 的种子扩展、密钥生成、封装及解封装，并通过提前中止矩阵系统化减少平均开销。
- 作者报告：作者以失败后重新生成密钥解释提前中止与其恒时要求的相容性；FixedWeight 的恒时描述明确限定成功尝试。
- 限制与下一步：不能写成整个随机重试调用耗时固定；实际 keygen/decap 范围为 systematic 变体。未审计失败种子状态、泄漏独立性或物理测量；修订版勘误仍待取得核对。
- 阅读层级：selected_full_text_sections；来源：https://tches.iacr.org/index.php/TCHES/article/download/9695/9226。
- 已读章节：PDF pp.2–3 (printed pp.72–73): motivation, contributions and systematic-variant scope; PDF p.30 (printed p.100): FixedWeight randomness/retry and successful-attempt constant-time statement
- [详细阅读记录](notes/tches-implementation-evidence-boundaries-20261113.md)
- 代码/数据核查：not checked；引用追踪：pending。

## Curse of Re-encryption: A Generic Power/EM Analysis on Post-Quantum KEMs

- 来源：[TCHES 2022](https://doi.org/10.46586/tches.v2022.i1.296-322)；时间标记：formal publication within rolling window。
- 作者：Rei Ueno; Keita Xagawa; Yutaro Tanaka; Akira Ito; Junko Takahashi; Naofumi Homma
- 对象：Kyber, Saber, FrodoKEM, NTRU, NTRU Prime, HQC, BIKE, SIKE；类型：attack。
- 核心想法：将 FO 重加密阶段 PRF/PRG 的功耗或电磁泄漏用于构造明文检查预言机。
- 作者报告：摘要报告多种 PRF 实现上的实验，并讨论跨 KEM 适用性。
- 限制与下一步：各方案恢复范围不同；BIKE 摘要仅称部分恢复，Classic McEliece 适用性未定，不能概括成全部完整恢复。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Don’t Reject This: Key-Recovery Timing Attacks Due to Rejection-Sampling in HQC and BIKE

- 来源：[TCHES 2022](https://doi.org/10.46586/tches.v2022.i3.223-263)；时间标记：formal publication within rolling window。
- 作者：Qian Guo; Clemens Hlauschek; Thomas Johansson; Norman Lahr; Alexander Nilsson; Robin Leander Schröder
- 对象：HQC, BIKE；类型：attack。
- 核心想法：研究由秘密相关输入驱动的拒绝采样时间，连接到 HQC 恢复及 BIKE 距离谱推断。
- 作者报告：摘要给出理想化计时预言机的攻击分析与实现。
- 限制与下一步：查询数量基于理想化预言机，不能直接转述为端到端实测成本；需核对具体版本。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Efficient Implementations of Rainbow and UOV using AVX2

- 来源：[TCHES 2022](https://doi.org/10.46586/tches.v2022.i1.245-269)；时间标记：formal publication within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Kyung-Ah Shim; Sangyub Lee; Namhun Koo
- 对象：Rainbow, UOV, precomputation；类型：implementation_and_leakage_analysis。
- 核心想法：通过块矩阵求逆与预计算加速签名，并分析预计算值泄漏或复用的秘密恢复风险。
- 作者报告：作者报告 AVX2 性能及预计算值泄漏/复用时的多项式时间完整私钥恢复结论。
- 限制与下一步：给定或复用预计算值的分析，不等于已从真实功耗中获取这些值；与数学方案本身的现行安全状态分开。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Faster Constant-Time Decoder for MDPC Codes and Applications to BIKE KEM

- 来源：[TCHES 2022](https://doi.org/10.46586/tches.v2022.i4.110-134)；时间标记：formal publication within rolling window。
- 作者：Thales B. Paiva; Routo Terada
- 对象：BIKE, QC-MDPC；类型：constant_time_implementation。
- 核心想法：提出 PickyFix 译码器以改进 BGF 的若干限制，并研究恒时实现的译码能力与性能。
- 作者报告：作者比较不同安全级别下的实现速度及纠错能力。
- 限制与下一步：译码失败概率、恒时性质与物理泄漏是不同指标；摘要不足以证明对功耗攻击安全。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## High-order Table-based Conversion Algorithms and Masking Lattice-based Encryption

- 来源：[TCHES 2022](https://doi.org/10.46586/tches.v2022.i2.1-40)；时间标记：formal publication within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Jean-Sébastien Coron; François Gérard; Simon Montoya; Rina Zeitoun
- 对象：Kyber, Saber, masking conversion；类型：countermeasure。
- 核心想法：通过表重计算实现高阶算术与布尔掩码转换。
- 作者报告：作者给出 ISW 探针模型证明，并应用于结构化 LWE 加密的保护。
- 限制与下一步：摘要突出 Kyber IND-CPA 解密性能；不能把该数字直接当作完整 IND-CCA 解封装成本。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Higher-Order Masked Ciphertext Comparison for Lattice-Based Cryptography

- 来源：[TCHES 2022](https://doi.org/10.46586/tches.v2022.i2.115-139)；时间标记：formal publication within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Jan-Pieter D’Anvers; Daniel Heinz; Peter Pessl; Michiel Van Beirendonck; Ingrid Verbauwhede
- 对象：Kyber, Saber, ciphertext comparison；类型：attack_and_countermeasure。
- 核心想法：用碰撞侧信道攻击说明第一阶比较的局限，提出考虑压缩的高阶比较修复。
- 作者报告：作者报告 Kyber512 恢复、二/三阶 Cortex-M4 性能、证明与 TVLA。
- 限制与下一步：作者明确碰撞攻击不推翻原第一阶安全声明；有限 TVLA 与形式模型安全分开。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Masked Accelerators and Instruction Set Extensions for Post-Quantum Cryptography

- 来源：[TCHES 2022](https://doi.org/10.46586/tches.v2022.i1.414-460)；时间标记：formal publication within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Tim Fritzmann; Michiel Van Beirendonck; Debapriya Basu Roy; Patrick Karl; Thomas Schamberger; Ingrid Verbauwhede; Georg Sigl
- 对象：Kyber, Saber, RISC-V；类型：countermeasure。
- 核心想法：结合掩码压缩、NTT 乘法器和非线性指令扩展，设计 PQC 软硬件协同保护。
- 作者报告：作者报告 NIST Level III 参数实现周期和包含随机数生成的一阶解封装开销。
- 限制与下一步：随机生成成本已计入所报基线；安全阶数、受保护操作及硬件/软件边界须对齐比较。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Multi-moduli NTTs for Saber on Cortex-M3 and Cortex-M4

- 来源：[TCHES 2022](https://doi.org/10.46586/tches.v2022.i1.127-151)；时间标记：formal publication within rolling window。
- 作者：Amin Abdulrahman; Jiun-Peng Chen; Yu-Jia Chen; Vincent Hwang; Matthias J. Kannwischer; Bo-Yin Yang
- 对象：Saber, NTT, Cortex-M3, Cortex-M4；类型：masked_implementation_optimization。
- 核心想法：比较多模数 NTT 与 Toom–Cook 在 Saber 掩码及未保护实现中的速度和栈空间。
- 作者报告：作者报告 Cortex-M4 掩码实现相对所比 Toom–Cook 基线提速 16%，并研究 Cortex-M3/M4 的时间与空间折衷。
- 限制与下一步：掩码实现的性能优化不等于新的泄漏安全证明；摘要未给出物理泄漏验证，保护阶数、随机性及基线版本待正文核对。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 代码/数据核查：not checked；引用追踪：pending。

## Post-Quantum Authenticated Encryption against Chosen-Ciphertext Side-Channel Attacks

- 来源：[TCHES 2022](https://doi.org/10.46586/tches.v2022.i4.372-396)；时间标记：formal publication within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Melissa Azouaoui; Yulia Kuzovkova; Tobias Schneider; Christine Van Vredendaal
- 对象：Kyber, Dilithium, Falcon, EtS KEM；类型：countermeasure。
- 核心想法：以 Encrypt-then-Sign 认证 KEM 改变协议结构，降低 FO 选择密文侧信道防护成本。
- 作者报告：作者在 outsider-security 模型下评估实例化、通信和签名验证故障防护开销。
- 限制与下一步：改变了协议和信任/认证条件；不能作为原 FO KEM 的无代价直接替换或同模型速度比较。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Racing BIKE: Improved Polynomial Multiplication and Inversion in Hardware

- 来源：[TCHES 2022](https://doi.org/10.46586/tches.v2022.i1.557-588)；时间标记：formal publication within rolling window。
- 作者：Jan Richter-Brockmann; Ming-Shing Chen; Santosh Ghosh; Tim Güneysu
- 对象：BIKE, sparse polynomial multiplication, FPGA；类型：constant_time_implementation。
- 核心想法：优化 BIKE 的稀疏多项式乘法和求逆，并将各 KEM 操作映射到共享硬件。
- 作者报告：摘要明确声称封装所用稀疏乘法器在非固定汉明重量下保持时间恒定；求逆采用扩展欧几里得算法。
- 限制与下一步：恒时声明的直接对象是所述稀疏乘法器，不能转移给求逆、整套 KEM 或功耗/电磁安全；不同性能配置需分别核对。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 代码/数据核查：not checked；引用追踪：pending。

## SIKE Channels: Zero-Value Side-Channel Attacks on SIKE

- 来源：[TCHES 2022](https://doi.org/10.46586/tches.v2022.i3.264-289)；时间标记：formal publication within rolling window。
- 作者：Luca De Feo; Nadia El Mrabet; Aymeric Genêt; Novak Kaluđerovi´c; Natacha Linard de Guertechin; Simon Pontié; Élise Tasso
- 对象：SIKE；类型：attack。
- 核心想法：分析坐标随机化未覆盖的零值泄漏，并将其用于 SIKE 恢复。
- 作者报告：摘要报告两类实验室验证的零值攻击及防护分析。
- 限制与下一步：历史 SIKE 对象与具体零值条件须保留；不能把同源算法代数破译与本文物理攻击混为一谈。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：forward citation observed; exhaustive backward/forward closure pending。

## Single-Trace Side-Channel Attacks on the Toom-Cook: The Case Study of Saber

- 来源：[TCHES 2022](https://doi.org/10.46586/tches.v2022.i4.285-310)；时间标记：formal publication within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Yanbin Li; Jiajie Zhu; Yuxin Huang; Zhe Liu; Ming Tang
- 对象：Saber, Toom-Cook；类型：attack。
- 核心想法：结合深度学习剖析、优化因子图及信念传播，分析 Toom-Cook 多项式乘法。
- 作者报告：作者报告单攻击迹线 SASCA 的评估实验并讨论防护。
- 限制与下一步：单迹指攻击阶段，不代表无需训练模板；具体平台、训练预算与完整秘密范围须读正文。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## The Hidden Parallelepiped Is Back Again: Power Analysis Attacks on Falcon

- 来源：[TCHES 2022](https://doi.org/10.46586/tches.v2022.i3.141-164)；时间标记：formal publication within rolling window。
- 作者：Morgane Guerreau; Ange Martinelli; Thomas Ricosset; Mélissa Rossi
- 对象：Falcon；类型：attack。
- 核心想法：研究预像计算与基础采样器泄漏，并将采样信息接入几何恢复方法。
- 作者报告：摘要报告 ELMO 模拟和 Cortex-M4/ChipWhisperer 实验。
- 限制与下一步：模拟与实测条件需分开；采样中间量并不直接等同秘密。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Will You Cross the Threshold for Me?: Generic Side-Channel Assisted Chosen-Ciphertext Attacks on NTRU-based KEMs

- 来源：[TCHES 2022](https://doi.org/10.46586/tches.v2022.i1.722-761)；时间标记：formal publication within rolling window。
- 作者：Prasanna Ravi; Martianus Frederic Ezerman; Shivam Bhasin; Anupam Chattopadhyay; Sujoy Sinha Roy
- 对象：NTRU, NTRU Prime；类型：attack。
- 核心想法：把解封装泄漏组织为明文检查、解密失败和完整解密三类预言机，研究选择密文恢复。
- 作者报告：作者在 pqm4 未保护优化实现和 Cortex-M4 电磁测量上验证。
- 限制与下一步：区分三种预言机的能力、底层观测成本和方案参数；不能直接推及有掩码的实现。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Hertzbleed: Turning Power Side-Channel Attacks Into Remote Timing Attacks on x86

- 来源：[USENIX 2022](https://www.usenix.org/conference/usenixsecurity22/presentation/wang-yingchen)；时间标记：exact public date not yet verified。
- 作者：Yingchen Wang, University of Texas at Austin; Riccardo Paccagnella and Elizabeth Tang He, University of Illinois Urbana-Champaign; Hovav Shacham, University of Texas at Austin; Christopher W. Fletcher, University of Illinois Urbana-Champaign; David Kohlbrenner, University of Washington
- 对象：SIKE；类型：attack。
- 核心想法：研究 DVFS 如何把数据相关功耗变化转为可远程观察的执行时间差异。
- 作者报告：摘要报告 x86 上的机制分析及对恒时 SIKE 实现的选择密文攻击。
- 限制与下一步：历史 SIKE 是论文攻击对象；不能据此评价当前其他 PQC 实现的实际成本。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX session abstract。
- 代码/数据核查：not checked；引用追踪：forward citation observed; exhaustive backward/forward closure pending。

## Too Many Hints – When LLL Breaks LWE

- 来源：[ASIACRYPT 2023](https://doi.org/10.1007/978-981-99-8730-6_4)；时间标记：formal publication within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Alexander May; Julian Nowakowski
- 对象：LWE, Kyber, perfect and modular hints；类型：method。
- 核心想法：批量整合完美与模提示，降低构造格基和随后 LLL/BKZ 求解的成本。
- 作者报告：作者评估密码学维度的提示数量与实际约简恢复时间。
- 限制与下一步：提示是给定的正确内积信息，不等于已经从同数量功耗迹线取得；提示获取、分布及误差条件须单独核查。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://eprint.iacr.org/2023/777。
- 代码/数据核查：not checked；引用追踪：forward edge observed; backward and exhaustive forward search pending; forward citation observed; exhaustive backward/forward closure pending。

## AfterImage: Leaking Control Flow Data and Tracking Load Operations via the Hardware Prefetcher

- 来源：[ASPLOS 2023](https://doi.org/10.1145/3575693.3575719)；时间标记：formal publication within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Yun Chen; Lingfeng Pei; Trevor E. Carlson
- 对象：RSA, Intel IP-stride prefetcher；类型：attack。
- 核心想法：通过攻击者训练的预取器状态推断控制流和 load 行为。
- 作者报告：作者摘要报告跨隔离层 PoC、timing-balanced RSA 恢复及作为功耗分析高精度标记的用途。
- 限制与下一步：不依赖投机执行这一条件不意味着不需同机执行或训练能力；具体调度、实现和隔离假设仍需全文。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://www.comp.nus.edu.sg/~tcarlson/pdfs/chen2023lcfivthp.pdf。
- 代码/数据核查：not checked；引用追踪：forward edge observed; backward and exhaustive forward search pending。

## The Finger in the Power: How to Fingerprint PCs by Monitoring Their Power Consumption

- 来源：[DIMVA 2023](https://doi.org/10.1007/978-3-031-35504-2_2)；时间标记：within rolling window; online 2023-06-10; print year 2023。
- 作者：Marina Botvinnik; Tomer Laor; Thomas Rokicki; Clémentine Maurice; Yossi Oren
- 对象：power fingerprinting, device identification, Intel and AMD, WebAssembly；类型：measurement_and_fingerprinting。
- 核心想法：用相同指令的低速功耗响应区分不同机器，包括软硬件配置相同的个体。
- 作者报告：作者摘要报告跨多代处理器的设备研究、温度影响和降低精度的 WebAssembly 概念验证。
- 限制与下一步：设备身份是恢复对象，不是程序秘密。论文明确说明其功耗读取依赖当时的高权限接口；WebAssembly 计算不等于浏览器能够无权限取得功耗。公开仓库链接本轮返回 404，可取得性未确认。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://link.springer.com/chapter/10.1007/978-3-031-35504-2_2。
- [详细阅读记录](notes/power-observation-and-pqc-boundaries-20261113.md)
- 代码/数据核查：publisher-linked repository and README API requests returned 404 on 2026-11-13; no code or dataset retrieved; reason unknown；引用追踪：forward citation observed; exhaustive backward/forward closure pending。

## Exploiting the microarchitectural leakage of prefetching activities for side-channel attacks

- 来源：[Journal of Systems Architecture 2023](https://doi.org/10.1016/j.sysarc.2023.102877)；时间标记：formal publication within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Chong Xiao; Ming Tang; Sylvain Guilley
- 对象：AES-128, Intel IP-stride prefetcher；类型：attack。
- 核心想法：逆向 stride 预取的三类规则，从残留访问模式推断查表 AES 的密钥候选。
- 作者报告：作者出版商摘要与引言报告 AES-128 恢复及把探测推迟到加密后进行的可行性。
- 限制与下一步：对象是 lookup-table-style SubBytes；不能外推为 AES-NI 或所有恒时 AES 均被攻破。
- 阅读层级：selected_full_text_sections；来源：https://www.sciencedirect.com/science/article/pii/S1383762123000565。
- 已读章节：publisher abstract and introduction preview; full article not read
- 代码/数据核查：not checked；引用追踪：forward edge observed; backward and exhaustive forward search pending。

## Breaking and Protecting the Crystal: Side-Channel Analysis of Dilithium in Hardware

- 来源：[PQCrypto 2023](https://doi.org/10.1007/978-3-031-40003-2_25)；时间标记：inside rolling window。
- 作者：Hauke Steffen; Georg Land; Lucie Kogelheide; Tim Güneysu
- 对象：Dilithium；类型：attack and countermeasure。
- 核心想法：分析 FPGA Dilithium 实现的 NTT 相关功耗泄漏与专用防护。
- 作者报告：摘要报告剖析 SPA、CPA 与对应对策的实验评估。
- 限制与下一步：剖析迹线与攻击迹线预算要分开；摘要中的防护有效性只覆盖所评估攻击，不是通用安全证明。
- 阅读层级：abstract_and_bibliographic_metadata；来源：ePrint abstract and explicit publication DOI: https://eprint.iacr.org/2022/1410。
- 代码/数据核查：not checked；引用追踪：forward edge observed; backward and exhaustive forward search pending。

## DVFS Frequently Leaks Secrets: Hertzbleed Attacks Beyond SIKE, Cryptography, and CPU-Only Data

- 来源：[SP 2023](https://doi.org/10.1109/sp46215.2023.10179326)；时间标记：inside rolling window。
- 作者：Yingchen Wang; Riccardo Paccagnella; Alan Wandke; Zhao Gang; Grant Garrett-Grossman; Christopher W. Fletcher; David Kohlbrenner; Hovav Shacham
- 对象：Classic McEliece, ECDSA, GPU/Chrome；类型：attack。
- 核心想法：将 DVFS 功耗—频率通道扩展到 SIKE 之外的密码与集成 GPU 场景。
- 作者报告：摘要报告结合实现中的已有片段与密码分析，攻击恒时 ECDSA、Classic McEliece，并利用 GPU/CPU 功率耦合做像素推断。
- 限制与下一步：待核对各平台、版本和采集预算；不扩展为当前所有 ECDSA/McEliece 或浏览器实现均受影响。
- 阅读层级：abstract_and_bibliographic_metadata；来源：author-institution abstract: https://experts.illinois.edu/en/publications/dvfs-frequently-leaks-secrets-hertzbleed-attacks-beyond-sike-cryp/。
- 代码/数据核查：not checked；引用追踪：forward citation observed; exhaustive backward/forward closure pending。

## Adapting Belief Propagation to Counter Shuffling of NTTs

- 来源：[TCHES 2023](https://doi.org/10.46586/tches.v2023.i1.60-88)；时间标记：formal publication within rolling window。
- 作者：Julius Hermelink; Silvan Streit; Emanuele Strieder; Katharina Thieme
- 对象：Kyber, NTT；类型：method。
- 核心想法：使用 shuffle node 与层间匹配，把排列不确定性纳入信念传播。
- 作者报告：摘要报告扩展攻击模型和对子图推断、匹配策略的评估。
- 限制与下一步：不能从摘要推断对所有打乱方案均有效；能力假设及噪声条件需读全文。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Belief Propagation Meets Lattice Reduction: Security Estimates for Error-Tolerant Key Recovery from Decryption Errors

- 来源：[TCHES 2023](https://doi.org/10.46586/tches.v2023.i4.287-317)；时间标记：formal publication within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Julius Hermelink; Erik Mårtensson; Simona Samardjiska; Peter Pessl; Gabi Dreo Rodosek
- 对象：Kyber, LWE, belief propagation, lattice reduction；类型：method。
- 核心想法：将统计处理与格约简结合，对解密错误产生的不正确不等式进行容错恢复。
- 作者报告：作者以故障诱发的 Kyber 解密错误演示求解改进。
- 限制与下一步：这是物理攻击后处理及故障示例，不能写成被动功耗测量实验；估算和实际求解范围须分开。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Cache-Timing Attack Against HQC

- 来源：[TCHES 2023](https://doi.org/10.46586/tches.v2023.i3.136-163)；时间标记：formal publication within rolling window。
- 作者：Senyang Huang; Rui Qi Sim; Chitchanok Chuengsatiansup; Qian Guo; Thomas Johansson
- 对象：HQC；类型：attack。
- 核心想法：将向量生成过程的缓存行为构造成明文检查预言机，连接密文选择与秘密恢复。
- 作者报告：摘要区分 Flush+Reload 概念验证和 SGX 场景的 Prime+Probe。
- 限制与下一步：两个场景的访问条件不同；平台和实现版本需独立核对。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Exploiting Intermediate Value Leakage in Dilithium: A Template-Based Approach

- 来源：[TCHES 2023](https://doi.org/10.46586/tches.v2023.i4.188-210)；时间标记：formal publication within rolling window。
- 作者：Alexandre Berzati; Andersson Calle Viera; Maya Chartouny; Steven Madec; Damien Vergnaud; David Vigilant
- 对象：Dilithium；类型：attack。
- 核心想法：用模板判别签名中间向量的零系数，再通过线性关系恢复足以伪造的秘密部分。
- 作者报告：摘要报告 ARM Cortex-M4 上的实测泄漏依据。
- 限制与下一步：恢复部分秘密所提供的伪造能力不等于恢复全部私钥；历史 Dilithium 不自动代表最终 ML-DSA 实现。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：forward edge observed; backward and exhaustive forward search pending。

## Find the Bad Apples: An efficient method for perfect key recovery under imperfect SCA oracles – A case study of Kyber

- 来源：[TCHES 2023](https://doi.org/10.46586/tches.v2023.i1.89-112)；时间标记：formal publication within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Muyan Shen; Chi Cheng; Xiaohan Zhang; Qian Guo; Tao Jiang
- 对象：Kyber, FireSaber, PC oracle；类型：attack。
- 核心想法：用自适应检测码定位并修正不完美明文检查预言机造成的错误秘密项。
- 作者报告：作者给出 Kyber512/FireSaber 模拟及 pqm4 Kyber512 在 STM32F407G 上的电磁实验。
- 限制与下一步：相对多数投票的收益在固定原始预言机准确率下比较；需计入额外查询和构造预言机的观测成本。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：forward edge observed; backward and exhaustive forward search pending。

## High-order Polynomial Comparison and Masking Lattice-based Encryption

- 来源：[TCHES 2023](https://doi.org/10.46586/tches.v2023.i1.153-192)；时间标记：formal publication within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Jean-Sébastien Coron; François Gérard; Simon Montoya; Rina Zeitoun
- 对象：Kyber, polynomial comparison；类型：countermeasure。
- 核心想法：提出多种高阶多项式比较方法并集成完整 Kyber 掩码。
- 作者报告：作者给出 ISW 证明、ARM Cortex-M 实现及 t-test 评估。
- 限制与下一步：探针模型结论与真实转换、毛刺及有限噪声条件之间仍需实现映射；不能只凭 t-test 宣称普遍安全。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## High-order masking of NTRU

- 来源：[TCHES 2023](https://doi.org/10.46586/tches.v2023.i2.180-211)；时间标记：formal publication within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Jean-Sébastien Coron; François Gérard; Matthias Trannoy; Rina Zeitoun
- 对象：NTRU；类型：countermeasure。
- 核心想法：构造高阶 NTRU 掩码组件并覆盖包括密钥生成的完整 KEM。
- 作者报告：作者给出 ISW 证明、Cortex-M3 实现和 t-test 评估。
- 限制与下一步：模型内证明和实际泄漏评估范围分别核查；不自动推广至所有 NTRU 参数与编译版本。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Improved Gadgets for the High-Order Masking of Dilithium

- 来源：[TCHES 2023](https://doi.org/10.46586/tches.v2023.i4.110-145)；时间标记：formal publication within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Jean-Sébastien Coron; François Gérard; Matthias Trannoy; Rina Zeitoun
- 对象：Dilithium, ShiftMod, masking conversion；类型：countermeasure。
- 核心想法：改进 ShiftMod、B2A、随机向量生成与 Decompose 等高阶掩码组件。
- 作者报告：作者给出 t-probing 证明及完整高阶掩码 Dilithium C 实现的性能比较。
- 限制与下一步：历史 Dilithium 与最终 ML-DSA 的版本映射未核查；摘要主要是证明与性能，不补猜硬件实测。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Kavach: Lightweight masking techniques for polynomial arithmetic in lattice-based cryptography

- 来源：[TCHES 2023](https://doi.org/10.46586/tches.v2023.i3.366-390)；时间标记：formal publication within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Aikata Aikata; Andrea Basso; Gaetan Cassiers; Ahmet Can Mert; Sujoy Sinha Roy
- 对象：lattice polynomial multiplication, NTT, schoolbook multiplication；类型：countermeasure。
- 核心想法：在掩码多项式乘法中保留小秘密范围，以复用紧凑乘法器。
- 作者报告：作者分别实现 NTT 与 schoolbook 路线并进行一阶 TVLA 评估。
- 限制与下一步：摘要用 guarantee 描述 TVLA；本库仅记录有限泄漏评估，不将其提升为完整安全证明。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## LPN-based Attacks in the White-box Setting

- 来源：[TCHES 2023](https://doi.org/10.46586/tches.v2023.i4.318-343)；时间标记：formal publication within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Alex Charlès; Aleksei Udovenko
- 对象：white-box masking, LPN, DCA, LDA；类型：attack_method。
- 核心想法：将 LPN 求解用于白盒掩码的强线性近似，组合差分计算分析与线性译码思路。
- 作者报告：作者给出理论及实验比较，分析依近似误差变化的复杂度和若干掩码方案。
- 限制与下一步：研究对象是白盒计算踪迹与掩码，不是对 LPN 后量子密码实例的物理攻击；不能混入 PQC 恢复数字。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Multiple-Valued Plaintext-Checking Side-Channel Attacks on Post-Quantum KEMs

- 来源：[TCHES 2023](https://doi.org/10.46586/tches.v2023.i3.473-503)；时间标记：formal publication within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Yutaro Tanaka; Rei Ueno; Keita Xagawa; Akira Ito; Junko Takahashi; Naofumi Homma
- 对象：Kyber, Saber, FrodoKEM, NTRU Prime, SIKE, MV-PC oracle；类型：attack。
- 核心想法：用多分类神经网络实现多值明文检查，结合不完美输出优化恢复查询。
- 作者报告：作者在 SHAKE、SHA3、AES 软件上评估预言机，并分析多个 KEM 的适用性。
- 限制与下一步：对称原语上的测量不等于所有列名 KEM 均做了完整物理恢复；查询数与误差假设须一起记录。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Protecting Dilithium against Leakage: Revisited Sensitivity Analysis and Improved Implementations

- 来源：[TCHES 2023](https://doi.org/10.46586/tches.v2023.i4.58-79)；时间标记：formal publication within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Melissa Azouaoui; Olivier Bronchain; Gaëtan Cassiers; Clément Hoffmann; Yulia Kuzovkova; Joost Renes; Tobias Schneider; Markus Schönauer; François-Xavier Standaert; Christine Van Vredendaal
- 对象：Dilithium；类型：countermeasure。
- 核心想法：重新划分中间计算的物理敏感性，并结合新转换组件改进保护实现。
- 作者报告：作者比较随机化与确定性签名在侧信道防护下的实现成本。
- 限制与下一步：随机化模式更省成本不意味着无需保护；敏感性分类和随机源条件须读全文核查。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Pushing the Limits of Generic Side-Channel Attacks on LWE-based KEMs - Parallel PC Oracle Attacks on Kyber KEM and Beyond

- 来源：[TCHES 2023](https://doi.org/10.46586/tches.v2023.i2.418-446)；时间标记：formal publication within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Gokulnath Rajendran; Prasanna Ravi; Jan-Pieter D’Anvers; Shivam Bhasin; Anupam Chattopadhyay
- 对象：Kyber, PC oracle；类型：attack。
- 核心想法：构造并行明文检查预言机，以多分类器让一次查询提供多比特信息。
- 作者报告：作者在未保护 pqm4 Kyber 上实测至 P=10，并讨论克隆设备、局部恢复及打乱实现。
- 限制与下一步：理论可扩展性不能替代更大 P 的实测；选择密文、剖析与保护配置必须分别说明。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：forward edge observed; backward and exhaustive forward search pending。

## Separating Oil and Vinegar with a Single Trace: Side-Channel Assisted Kipnis-Shamir Attack on UOV

- 来源：[TCHES 2023](https://doi.org/10.46586/tches.v2023.i3.221-245)；时间标记：formal publication within rolling window。
- 作者：Thomas Aulbach; Fabio Campos; Juliane Krämer; Simona Samardjiska; Marc Stöttinger
- 对象：UOV；类型：attack。
- 核心想法：从签名时中央映射求逆的单迹泄漏推断 vinegar 变量，再连接代数恢复方法。
- 作者报告：作者报告 Cortex-M4/ChipWhisperer 实测，并声明公开代码及参考/目标迹线。
- 限制与下一步：不要求控制签名消息仍可能需要参考数据；single trace 指攻击阶段，不能忽略剖析与离线恢复成本。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Single-Trace Side-Channel Attacks on CRYSTALS-Dilithium: Myth or Reality?

- 来源：[ePrint 2023](https://eprint.iacr.org/2023/1931)；时间标记：inside rolling window; preprint。
- 作者：Ruize Wang; Kalle Ngo; Joel Gärtner; Elena Dubrova
- 对象：Dilithium-2；类型：attack。
- 核心想法：从密钥解包的剖析功耗读数恢复部分系数，再以线性关系或格约减补全。
- 作者报告：作者报告 Cortex-M4 两种后处理；其中单迹跨器件结果依赖已知 t0 的第一种变体。
- 限制与下一步：t0 不是标准压缩公钥中自动已知的量；不需要 t0 的另一变体要求更多系数读数。不能将第一变体的单迹成功率转给第二变体。
- 阅读层级：abstract_and_bibliographic_metadata；来源：ePrint abstract: https://eprint.iacr.org/2023/1931; NIST presentation located, not a separate paper。
- 代码/数据核查：not checked；引用追踪：forward edge observed; backward and exhaustive forward search pending。

## PREFETCHX: Cross-Core Cache-Agnostic Prefetcher-based Side-Channel Attacks

- 来源：[HPCA 2024](https://doi.org/10.1109/hpca57654.2024.00037)；时间标记：formal publication within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Yun Chen; Ali Hajiabadi; Lingfeng Pei; Trevor E. Carlson
- 对象：RSA, XPT prefetcher；类型：attack。
- 核心想法：逆向 Intel XPT 预取器并构造跨核心侧信道，研究预取器自身状态泄漏。
- 作者报告：正式版报告 RSA、按键/网络活动案例及两类隐蔽信道；引言限定 RSA 为 square-and-multiply。
- 限制与下一步：GoFetch 引用 2023 预印本；其摘要 1.7 MB/s 与 HPCA 2024 的 122 KiB/s 不同，不能混用。限所测 Xeon/XPT；不推及所有恒时 RSA。
- 阅读层级：selected_full_text_sections；来源：https://www.comp.nus.edu.sg/~tcarlson/pdfs/chen2024nccapsac.pdf。
- 已读章节：PDF page 1: abstract and introduction, including RSA implementation scope
- 代码/数据核查：not checked；引用追踪：forward edge observed; backward and exhaustive forward search pending。

## A Not So Discrete Sampler: Power Analysis Attacks on HAWK signature scheme

- 来源：[TCHES 2024](https://doi.org/10.46586/tches.v2024.i4.156-178)；时间标记：formal publication within rolling window。
- 作者：Morgane Guerreau; Mélissa Rossi
- 对象：HAWK；类型：attack。
- 核心想法：分析离散高斯采样器泄漏，并评估部分采样信息对 Module-LIP 恢复复杂度的影响。
- 作者报告：作者在未声称受保护的参考实现和 STM32F3 上报告 SPA 与恢复结果。
- 限制与下一步：目标是未保护版本；临时修补和剩余复杂度估计不能当作完整掩码证明。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Defeating Low-Cost Countermeasures against Side-Channel Attacks in Lattice-based Encryption: A Case Study on Crystals-Kyber

- 来源：[TCHES 2024](https://doi.org/10.46586/tches.v2024.i2.795-818)；时间标记：formal publication within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Prasanna Ravi; Thales Paiva; Dirmanto Jap; Jan-Pieter D’Anvers; Shivam Bhasin
- 对象：Kyber, chosen ciphertext；类型：attack。
- 核心想法：绕过密文合理性检查与解封装失败检查，并改进不等式恢复求解。
- 作者报告：作者提出只依赖有效选择密文的恢复策略。
- 限制与下一步：有效密文仍是攻击者选择的输入，不等于被动攻击；结论针对所分析的两类低成本防护。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Exploiting Small-Norm Polynomial Multiplication with Physical Attacks: Application to CRYSTALS-Dilithium

- 来源：[TCHES 2024](https://doi.org/10.46586/tches.v2024.i2.359-383)；时间标记：formal publication within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Olivier Bronchain; Melissa Azouaoui; Mohamed ElGhamrawy; Joost Renes; Tobias Schneider
- 对象：Dilithium, belief propagation；类型：attack。
- 核心想法：从多次签名的有噪秘密后验中累积偏置，再用信念传播组织小范数多项式关系。
- 作者报告：作者讨论侧信道、故障及二者结合，也利用接受/拒绝信息并覆盖打乱实现。
- 限制与下一步：这些物理访问能力不是同一个威胁模型；二元接受信息不等于知道每次拒绝尝试的挑战与响应。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Gadget-based Masking of Streamlined NTRU Prime Decapsulation in Hardware

- 来源：[TCHES 2024](https://doi.org/10.46586/tches.v2024.i1.1-26)；时间标记：formal publication within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Georg Land; Adrian Marotzke; Jan Richter-Brockmann; Tim Güneysu
- 对象：Streamlined NTRU Prime, gadget-based masking；类型：countermeasure。
- 核心想法：将硬件门替换为可组合安全组件，构造可配置阶数的 NTRU Prime 解封装。
- 作者报告：作者报告 Artix-7/45nm 综合、形式验证与 TVLA，并讨论向 Kyber/Dilithium 迁移。
- 限制与下一步：迁移讨论不等于完成其他方案实现；任意阶可实例化不代表每阶均经实测。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## HAETAE: Shorter Lattice-Based Fiat-Shamir Signatures

- 来源：[TCHES 2024](https://doi.org/10.46586/tches.v2024.i3.25-75)；时间标记：formal publication within rolling window。
- 作者：Jung Hee Cheon; Hyeongmin Choe; Julien Devevey; Tim Güneysu; Dongyeon Hong; Markus Krausz; Georg Land; Marc Möller; Damien Stehlé; MinJune Yi
- 对象：HAETAE, Fiat-Shamir with Aborts, Cortex-M4, AVX2；类型：countermeasure_and_scheme_design。
- 核心想法：以超球与双峰拒绝采样设计较紧凑的 HAETAE 签名，同时讨论实现攻击防护。
- 作者报告：摘要报告恒时便携参考实现、AVX2 优化及 Cortex-M4 低栈实现，并声称给出高效侧信道保护方法。
- 限制与下一步：本次仅读摘要；具体防护组件、阶数、假设及实测覆盖待正文核对。不能把参考实现的恒时描述或方案紧凑性当作全部优化版本的功耗安全。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 代码/数据核查：not checked；引用追踪：pending。

## High-assurance zeroization

- 来源：[TCHES 2024](https://doi.org/10.46586/tches.v2024.i1.375-397)；时间标记：formal publication within rolling window。
- 作者：Santiago Arranz Olmos; Gilles Barthe; Ruben Gonzalez; Benjamin Grégoire; Vincent Laporte; Jean-Christophe Léchenet; Tiago Oliveira; Peter Schwabe
- 对象：Jasmin, Libjade；类型：countermeasure。
- 核心想法：用经验证编译器扩展保证密码例程返回时清除内存及寄存器中的敏感数据。
- 作者报告：作者扩展 Jasmin 正确性证明，并在具有恒时及 Spectre-v1 防护的 Libjade 中评估开销。
- 限制与下一步：零化发生时刻、调用边界和攻击者模型需要正文核查；不是对所有语言编译器的通用保证。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Hints from Hertz: Dynamic Frequency Scaling Side-Channel Analysis of Number Theoretic Transform in Lattice-Based KEMs

- 来源：[TCHES 2024](https://doi.org/10.46586/tches.v2024.i3.200-223)；时间标记：formal publication within rolling window。
- 作者：Tianrun Yu; Chi Cheng; Zilong Yang; Yingchen Wang; Yanbin Pan; Jian Weng
- 对象：Kyber, NTTRU, NTT；类型：attack。
- 核心想法：研究 NTT 数据活动经动态频率调节形成的频率提示，并评估提示的密码分析价值。
- 作者报告：摘要报告频率/时间测量和基于估计器的安全损失分析。
- 限制与下一步：Kyber 实例在文中去除了压缩/解压且为 CPA 版本；提示与估计不等于标准 ML-KEM 完整密钥恢复。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Improved High-Order Masked Generation of Masking Vector and Rejection Sampling in Dilithium

- 来源：[TCHES 2024](https://doi.org/10.46586/tches.v2024.i4.335-354)；时间标记：formal publication within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Jean-Sébastien Coron; François Gérard; Tancrède Lepoint; Matthias Trannoy; Rina Zeitoun
- 对象：Dilithium, masked rejection sampling；类型：countermeasure。
- 核心想法：改进掩码向量 y 生成及高阶拒绝采样组件，降低模数相关开销。
- 作者报告：作者给出 ISW t-probing 证明及集成完整掩码 Dilithium 的 C 性能比较。
- 限制与下一步：Crossref 摘要开头缺失，当前只据可读正文段落整理；未核查完整论文及硬件泄漏测试。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Masking FALCON’s Floating-Point Multiplication in Hardware

- 来源：[TCHES 2024](https://doi.org/10.46586/tches.v2024.i4.483-508)；时间标记：formal publication within rolling window。
- 作者：Emre Karabulut; Aydin Aysu
- 对象：Falcon；类型：countermeasure。
- 核心想法：设计硬件浮点乘法掩码与相关整数/选择组件，并研究面积吞吐折衷。
- 作者报告：作者给出 PINI 安全论证和 Sakura-X FPGA 一阶泄漏评估。
- 限制与下一步：只保护浮点乘法不等于完整 Falcon 签名安全；与软件浮点工作的比较需对齐阶数与保护范围。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Masking Floating-Point Number Multiplication and Addition of Falcon: First- and Higher-order Implementations and Evaluations

- 来源：[TCHES 2024](https://doi.org/10.46586/tches.v2024.i2.276-303)；时间标记：formal publication within rolling window。
- 作者：Keng-Yu Chen; Jiun-Peng Chen
- 对象：Falcon；类型：countermeasure。
- 核心想法：为浮点乘法和加法构造掩码非零检查、移位及归一化组件。
- 作者报告：作者给出探针模型下非干扰论证、Cortex-M4 性能及选定 TVLA 评估。
- 限制与下一步：不同阶数的实现与泄漏测试需分别记录；有限 TVLA 未检出不证明所有攻击安全。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## MiRitH: Efficient Post-Quantum Signatures from MinRank in the Head

- 来源：[TCHES 2024](https://doi.org/10.46586/tches.v2024.i2.304-328)；时间标记：formal publication within rolling window。
- 作者：Gora Adj; Stefano Barbero; Emanuele Bellini; Andre Esser; Luis Rivera-Zamarripa; Carlo Sanna; Javier Verbel; Floyd Zweydinger
- 对象：MiRitH, MinRank, MPC-in-the-head, AVX2, ARM NEON；类型：constant_time_implementation。
- 核心想法：提出基于 MinRank 的 MiRitH，并给出适用于 Intel AVX2 与 ARM NEON 的优化恒时实现。
- 作者报告：作者同时研究方案参数、量子搜索成本和有限域实现；摘要将两种向量平台实现描述为恒时。
- 限制与下一步：量子安全分析、代码恒时性质与功耗泄漏防护是不同主张；MPC-in-the-head 的多方视图不自动构成物理掩码。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 代码/数据核查：not checked；引用追踪：pending。

## SPA-GPT: General Pulse Tailor for Simple Power Analysis Based on Reinforcement Learning

- 来源：[TCHES 2024](https://doi.org/10.46586/tches.v2024.i4.40-83)；时间标记：formal publication within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Ziyu Wang; Yaoling Ding; An Wang; Yuwei Zhang; Congming Wei; Shaofei Sun; Liehuang Zhu
- 对象：public-key implementations, Kyber, reinforcement learning；类型：method。
- 核心想法：用强化学习自动分割变长功耗片段，并结合聚类与包络处理重建运算序列。
- 作者报告：作者评估九种软硬件场景，另报告 Kyber 中间值恢复并声明公开迹线。
- 限制与下一步：GPT 在题名中指 General Pulse Tailor，不是大语言模型；Kyber 中间值恢复不自动等于完整私钥恢复。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Single trace HQC shared key recovery with SASCA

- 来源：[TCHES 2024](https://doi.org/10.46586/tches.v2024.i2.64-87)；时间标记：formal publication within rolling window。
- 作者：Guillaume Goy; Julien Maillard; Philippe Gaborit; Antoine Loiseau
- 对象：HQC；类型：attack。
- 核心想法：在公开 RS 编解码计算中组合软泄漏和代数约束，研究单迹共享密钥恢复。
- 作者报告：摘要报告仿真及 STM32F407 实验，并比较掩码和打乱。
- 限制与下一步：共享/会话密钥目标不能写成长期私钥恢复；不同防护配置需分别分析。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## TPMScan: A wide-scale study of security-relevant properties of TPM 2.0 chips

- 来源：[TCHES 2024](https://doi.org/10.46586/tches.v2024.i2.714-734)；时间标记：formal publication within rolling window。
- 作者：Petr Svenda; Antonin Dufka; Milan Broz; Roman Lacko; Tomas Jaros; Daniel Zatovic; Josef Pospisil
- 对象：TPM, ECDSA, ECSCHNORR, ECDAA；类型：evaluation。
- 核心想法：系统研究 TPM 实现差异、随机数/nonce 问题、ECC 时序泄漏和修复报告完整性。
- 作者报告：作者调查多厂商版本并报告此前未公开的 nonce 与时序问题。
- 限制与下一步：摘要中最严重的少量签名私钥恢复不需要侧信道；不能把它的签名数当作时序攻击成本。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## GoFetch: Breaking Constant-Time Cryptographic Implementations Using Data Memory-Dependent Prefetchers

- 来源：[USENIX 2024](https://www.usenix.org/conference/usenixsecurity24/presentation/chen-boru)；时间标记：exact public date not yet verified。
- 作者：Boru Chen, University of Illinois Urbana-Champaign; Yingchen Wang, University of Texas at Austin; Pradyumna Shome, Georgia Institute of Technology; Christopher Fletcher, University of California, Berkeley; David Kohlbrenner, University of Washington; Riccardo Paccagnella, Carnegie Mellon University; Daniel Genkin, Georgia Institute of Technology
- 对象：Kyber, Dilithium, RSA, Diffie-Hellman；类型：attack。
- 核心想法：研究 Apple 数据内存依赖预取器如何将数据视为地址，突破恒时软件的原有假设。
- 作者报告：摘要报告对经典密码及 Kyber/Dilithium 的端到端攻击。
- 限制与下一步：主要研究 Apple M1；Kyber-512 reference 与 CIRCL deterministic Dilithium-2 是具体历史目标。其他芯片上观察到 DMP 不等于全部密码攻击已跨平台复现；表 1 时间不含 Dilithium 离线签名收集。
- 阅读层级：selected_full_text_sections；来源：official PDF: https://www.usenix.org/system/files/usenixsecurity24-chen-boru.pdf。
- 已读章节：abstract/introduction; section 3; selected overview/target passages in 7.1 and 7.2; section 8; references [1]–[98]. Tables, complete attack derivations and appendices not fully audited.
- [详细阅读记录](notes/gofetch-2024.md)
- 代码/数据核查：not checked；引用追踪：in_progress; 98 reference entries screened, selected identities resolved; forward search pending; forward citation observed; exhaustive backward/forward closure pending。

## Controlled Preemption: Amplifying Side-Channel Attacks from Userspace

- 来源：[ASPLOS 2025](https://doi.org/10.1145/3676641.3715985)；时间标记：within rolling window; published 2025-03-30。
- 作者：Yongye Zhu; Boru Chen; Zirui Neil Zhao; Christopher W. Fletcher
- 对象：Linux CFS, Linux EEVDF, microarchitectural timing resolution, Intel SGX；类型：attack_primitive。
- 核心想法：利用调度公平性机制细化受害执行与侧信道观察的交错，提高有状态通道的时间分辨率。
- 作者报告：作者研究单个非特权线程、同逻辑核共置及 SGX 内外场景。
- 限制与下一步：需要同机本地攻击能力、相应调度器并能够触发受害程序；正文不要求 SMT。它增强已有泄漏的观察条件，不是无条件制造秘密通道，也不能直接归为远程 PQC 密钥恢复。
- 阅读层级：selected_full_text_sections；来源：https://cwfletcher.github.io/content/research/2025.asplos.controlledpreemption.paper.pdf。
- 已读章节：PDF p.1 abstract and bibliography; PDF p.4 section 3 Threat Model
- [详细阅读记录](notes/power-observation-and-pqc-boundaries-20261113.md)
- 代码/数据核查：not checked；引用追踪：forward citation observed; exhaustive backward/forward closure pending。

## Breaking the Barrier: Post-Barrier Spectre Attacks

- 来源：[SP 2025](https://www.ieee-security.org/TC/SP2025/accepted-papers.html#collapse-70)；时间标记：conference year 2025 within frozen window; exact publication date not verified。
- 作者：Johannes Wikner, Kaveh Razavi ETH Zurich
- 对象：IBPB, Intel and AMD, speculative return prediction, Spectre；类型：attack。
- 核心想法：区分分支预测清理在微码实现和内核使用方式中的缺陷，研究屏障后的返回目标劫持。
- 作者报告：作者分别报告 Intel 跨进程密码哈希读出及 AMD Zen 1(+)/2 特权内存泄漏，并提出对应缓解。
- 限制与下一步：两类攻击的缺陷层次和平台不同；摘要中的论文时点不代表当前系统状态。该工作与 Training Solo 的域内自训练机制不能合并成同一漏洞。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://comsec-files.ethz.ch/papers/ibpb_sp25.pdf。
- 代码/数据核查：not checked；引用追踪：pending。

## Ceviche: Capability-Enhanced Secure Virtualization of Caches

- 来源：[SP 2025](https://www.ieee-security.org/TC/SP2025/accepted-papers.html#collapse-85)；时间标记：conference year 2025 within frozen window; exact publication date not verified。
- 作者：Arnabjyoti Kalita, Yilong Yang, Alenkruth Krishnan Murali, Ashish Venkat University of Virginia
- 对象：cache capabilities, cache partitioning, multicore isolation；类型：countermeasure。
- 核心想法：将地址与安全域映射为缓存访问能力，在缓存行粒度控制资源权限与分配。
- 作者报告：作者给出多级缓存虚拟化设计、策略及性能评估，目标包含保密性、可用性与公平性。
- 限制与下一步：保护范围是所建模的缓存资源与策略；摘要不支持全芯片功耗安全或量产硅片验证。性能代价需要结合正文的配置及基线，不能视为普遍常数。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://www.cs.virginia.edu/~av6ds/papers/sp2025.pdf。
- 代码/数据核查：not checked；引用追踪：pending。

## CipherSteal: Stealing Input Data from TEE-Shielded Neural Networks with Ciphertext Side Channels

- 来源：[SP 2025](https://doi.org/10.1109/sp61157.2025.00079)；时间标记：within rolling window; published 2025-05-12。
- 作者：Yuanyuan Yuan; Zhibo Liu; Sen Deng; Yanzuo Chen; Shuai Wang; Yinqian Zhang; Zhendong Su
- 对象：TEE ciphertext side channels, neural-network inputs, TensorFlow, PyTorch, TVM, Glow；类型：attack。
- 核心想法：把密文侧信道泄露的内存写入模式转换为局部输入信息，再重建神经网络的图像或视频输入。
- 作者报告：作者比较不同先验和执行框架，并报告以恢复输入训练替代网络等后续用途。
- 限制与下一步：攻击者为不可信宿主，输入重建依赖部分泄漏与先验；不等于破解内存加密算法，视觉近似也不保证逐字节一致。模型知识、TEE 实现与采集条件仍需正文核对。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://yuanyuan-yuan.github.io/files/sp25-Cipher-Steal.pdf。
- 代码/数据核查：not checked；引用追踪：pending。

## EUCLEAK

- 来源：[SP 2025](https://www.ieee-security.org/TC/SP2025/accepted-papers.html#collapse-239)；时间标记：conference year 2025 within frozen window; exact publication date not verified。
- 作者：Thomas Roche NinjaLab
- 对象：ECDSA, modular inversion, Infineon secure elements, FIDO；类型：attack。
- 核心想法：通过安全元件的非恒时模逆研究 ECDSA 泄漏，并使用本地电磁观测演示密钥恢复。
- 作者报告：作者 2024 技术报告摘要描述 Feitian A22 上的分析、YubiKey 5Ci 演示以及若干 Infineon 产品的适用性。
- 限制与下一步：本次读的是 2024-10-22 技术报告的封面、修订表与摘要，不是 2025 会议版全文；需要物理访问与相应仪器。版本/产品边界不能扩展成当前所有产品均受影响。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://ninjalab.io/wp-content/uploads/2024/10/20241022_eucleak.pdf。
- 代码/数据核查：not checked; author technical report only；引用追踪：pending。

## Peek-a-Walk: Leaking Secrets via Page Walk Side Channels

- 来源：[SP 2025](https://www.ieee-security.org/TC/SP2025/accepted-papers.html#collapse-76)；时间标记：conference year 2025 within frozen window; exact publication date not verified。
- 作者：Alan Wang1, Boru Chen2, Yingchen Wang3, Christopher W. Fletcher2, Daniel Genkin4, David Kohlbrenner5, Riccardo Paccagnella6 1: University of Illinois at Urbana-Champaign, 2: University of California, Berkeley, 3: University of Texas at Austin, 4: Georgia Institute of Technology, 5: University of Washington, 6: Carnegie Mellon University
- 对象：Dilithium-2, page walks, Spectre-BHI, Intel LAM, data-memory-dependent prefetching；类型：attack。
- 核心想法：以页表遍历为读出通道，使不指向有效映射的秘密值也可能留下可恢复的地址位信息；包含 Dilithium 案例。
- 作者报告：§4.4 结合本机推测执行、签名 nonce 系数泄漏与格提示后处理，报告恢复参考 Dilithium-2 的 s1；另有 LAM 内存读取和 DMP 沙箱案例。
- 限制与下一步：需通过地址规范性检查；42 位是特定读出上限，不是任意 64 位值都可读。Dilithium 案例无需 LAM，但依赖同机与目标地址等条件；不能混同为 DMP 直接攻击 ML-DSA，参考为版本 3.1。公开 README 尚留移植/TODO 说明，端到端材料完整性未核。
- 阅读层级：selected_full_text_sections；来源：https://www.cs.cmu.edu/~rpaccagn/papers/peek-a-walk-sp2025.pdf。
- 已读章节：PDF p.1 abstract; p.7 sections 3.3 and 4.1; pp.10–11 section 4.4 and continuation; p.12 section 5.2; selected references [15] p.14 and [53] p.15
- [详细阅读记录](notes/power-observation-and-pqc-boundaries-20261113.md)
- 代码/数据核查：author README fully read (platform and code overview, incomplete-porting/TODO statements); no build/run or end-to-end artifact completeness audit；引用追踪：selected references 15 and 53 linked; full inventory and forward search pending。

## SLAP: Data Speculation Attacks via Load Address Prediction on Apple Silicon

- 来源：[SP 2025](https://doi.org/10.1109/sp61157.2025.00098)；时间标记：within rolling window; published 2025-05-12。
- 作者：Jason Kim; Daniel Genkin; Yuval Yarom
- 对象：Apple Silicon, load address prediction, data speculation, Safari；类型：attack。
- 核心想法：研究加载地址预测错误造成的数据推测执行，从秘密静态存储读出进一步构造泄漏。
- 作者报告：作者在 M2/A15 及所测更新型号报告地址预测，并演示越界读出、函数调用、ASLR 与 Safari 跨站数据泄漏。
- 限制与下一步：加载地址预测不同于控制流预测、DMP 或加载值预测；不能把所测 Apple 产品外推到全部 Arm 或其他浏览器。已读摘要不能证明当前固件/浏览器仍有相同状态。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://predictors.fail/files/SLAP.pdf。
- 代码/数据核查：not checked；引用追踪：pending。

## Scheduled Disclosure: Turning Power Into Timing Without Frequency Scaling

- 来源：[SP 2025](https://www.ieee-security.org/TC/SP2025/accepted-papers.html#collapse-254)；时间标记：conference year 2025 within frozen window; exact publication date not verified。
- 作者：Inwhan Chun, Isabella Siu, Riccardo Paccagnella Carnegie Mellon University
- 对象：SIKE, Thread Director, Windows scheduler, GPU/Chrome；类型：attack。
- 核心想法：功耗相关的 Thread Director 调度提示改变活跃核心使用，把功耗差异转成远程时间差，毋须依赖频率泄漏。
- 作者报告：作者在 Meteor Lake/Windows 平台报告 SIKE 密钥恢复及跨源像素窃取，并比较默认与受限 P-state 配置。
- 限制与下一步：实测密码对象为 SIKE-751，不是 Kyber/ML-KEM；选择密文、网络拓扑与并发工作量是条件。摘要的约五倍比较跨处理器，不能作为同平台通用倍率。
- 阅读层级：selected_full_text_sections；来源：https://www.hertzbleed.com/scheduled-disclosure-sp2025.pdf。
- 已读章节：PDF pp. 1, 14–15: abstract/introduction and section 6; pp. 17–18: complete printed reference entries 1–79
- [详细阅读记录](notes/sp2025-protection-and-observation-boundaries-20261113.md)
- 代码/数据核查：README read via GitHub connector (blob 14c91f1d5eb761600091b682adefcfeeec2d2108); environment and source layout inspected; no build/run or completeness verification；引用追踪：79 printed references first-pass screened; 15 catalog links, 0 unresolved registered discoveries; 16 foundation records and recursive/forward closure pending。

## Slice+Slice Baby: Generating Last-Level Cache Eviction Sets in the Blink of an Eye

- 来源：[SP 2025](https://www.ieee-security.org/TC/SP2025/accepted-papers.html#collapse-131)；时间标记：conference year 2025 within frozen window; preprint initially 2025-04-15。
- 作者：Bradley Morgan1,2, Gal Horowitz3, Sioli O’Connell1, Stephan van Schaik4, Chitchanok Chuengsatiansup5, Daniel Genkin6, Olaf Maennel1, Paul Montague2, Eyal Ronen3, Yuval Yarom7 1: The University of Adelaide, 2: Defence Science and Technology Group, 3: Tel-Aviv University, 4: University of Michigan, 5: The University of Klagenfurt, 6: Georgia Tech, 7: Ruhr University Bochum
- 对象：LLC eviction sets, cache slice mapping, nonlinear address hash；类型：attack_primitive。
- 核心想法：结合微架构竞速、已知切片哈希和跨页内偏移关系，降低末级缓存逐出集构造成本。
- 作者报告：作者预印本摘要报告在两款 Intel 处理器上生成完整 LLC 逐出集，并与既有方法比较。
- 限制与下一步：评估对象是逐出集构造，不是完整攻击或密钥恢复时间；需要核查地址知识、页面与平台条件。预印本和会议标题、作者对应，全文版本等价未核查。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://arxiv.org/abs/2504.11208。
- 代码/数据核查：not checked；引用追踪：pending。

## TikTag: Breaking ARM's Memory Tagging Extension with Speculative Execution

- 来源：[SP 2025](https://www.ieee-security.org/TC/SP2025/accepted-papers.html#collapse-15)；时间标记：conference year 2025 within frozen window; exact publication date not verified。
- 作者：Juhee Kim1, Jinbum Park2, Sihyeon Roh1, Jaeyoung Chung1, Youngjoo Lee1, Taesoo Kim2,3, Byoungyoung Lee1 1: Seoul National University, 2: Samsung Research, 3: Georgia Institute of Technology
- 对象：ARM MTE, speculative execution, memory tags, Chrome, Linux；类型：attack。
- 核心想法：用推测执行形成的可观察差异推断内存标签，削弱 MTE 对内存破坏利用的概率防护。
- 作者报告：作者摘要报告 Chrome 与 Linux 场景的标签读取及防护绕过，并提出缓解机制。
- 限制与下一步：标签恢复不等于自动获得任意代码执行；还依赖可利用的程序缺陷和执行条件。读取的是作者 PDF 摘要，最终会议版差异与当前修复状态未核查。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://lifeasageek.github.io/papers/tiktag.pdf。
- 代码/数据核查：repository discovered but contents not checked；引用追踪：pending。

## Towards ML-KEM & ML-DSA on OpenTitan

- 来源：[SP 2025](https://doi.org/10.1109/SP61157.2025.00220)；时间标记：conference year 2025 within frozen window; exact publication date not verified。
- 作者：Amin Abdulrahman1, Hoang Nguyen Hien Pham2, Tobias Stelzer3, Felix Oberhansl3, Andreas Zankl3,4, Jade Philipoom5, Peter Schwabe1,6 1: Max Planck Institute for Security and Privacy (MPI-SP), 2: BULL SAS, Université Grenoble Alpes, 3: Fraunhofer Institute for Applied and Integrated Security (AISEC), Garching, Germany, 4: Technical University of Munich (TUM), Munich, Germany, 5: zeroRISC, Boston, USA, 6: Radboud University
- 对象：ML-KEM, ML-DSA, OpenTitan, OTBN, masked KMAC；类型：implementation_security_design。
- 核心想法：为 OTBN 连接现有掩码 KMAC 并扩展向量算术，同时考虑 OpenTitan 原有数据通路与状态保护要求。
- 作者报告：作者报告软件优化、硬件实现及综合/功能测试；正文另讨论同值份额不应在同一宽寄存器中组合的掩码策略。
- 限制与下一步：KMAC 一阶掩码及既有 OTBN 防护不等于完整 ML-KEM/ML-DSA 掩码实现；§5.2.5、§8 明确把完整方案掩码与适当性重评估列为后续工作。份额装载建议不是本文完成的功耗证明。
- 阅读层级：selected_full_text_sections；来源：https://cryptojedi.org/papers/otpqc-20250514.pdf。
- 已读章节：PDF p.1 abstract; relevant protection paragraphs pp.2,4,6,8,11,14–15 (including sections 2.4, 5.2.5, 8); selected reference entries p.17
- [详细阅读记录](notes/sp2025-protection-and-observation-boundaries-20261113.md)
- 代码/数据核查：author README read via GitHub connector (blob 4a797446f26d4e4d8ccf945fdf099dc64fa58fc0); submodule pointers, documented DB archive and platform restrictions inspected in README only; no build/run or data-file verification；引用追踪：selected reference 61 resolved to Share-slicing foundation; complete inventory and forward search pending。

## Training Solo: On the Limitations of Domain Isolation Against Spectre-v2 Attacks

- 来源：[SP 2025](https://www.ieee-security.org/TC/SP2025/accepted-papers.html#collapse-194)；时间标记：conference year 2025 within frozen window; exact publication date not verified。
- 作者：Sander Wiebing, Cristiano Giuffrida Vrije Universiteit Amsterdam
- 对象：Spectre-v2, branch predictor, domain isolation, self-training；类型：attack。
- 核心想法：研究训练与推测控制流劫持都发生在受害域内的自训练机制，检验域隔离策略的边界。
- 作者报告：作者描述三类内核攻击及两个端到端演示，并另外报告破坏域隔离实现的硬件问题。
- 限制与下一步：域内自训练的设计限制与另发现的隔离实现缺陷是不同结论；并非任何代码或任何受保护系统都可攻击，实际构件和配置仍须正文核对。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://download.vusec.net/papers/trainingsolo_sp25.pdf。
- 代码/数据核查：repository discovered but contents not checked；引用追踪：pending。

## Adaptive Template Attacks on the Kyber Binomial Sampler

- 来源：[TCHES 2025](https://doi.org/10.46586/tches.v2025.i3.470-492)；时间标记：formal publication within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Eric Chun-Yu Peng; Markus G. Kuhn
- 对象：Kyber768, CBD sampler, template adaptation；类型：attack。
- 核心想法：用高斯混合与 EM 将剖析模板适配到另一设备或地址布局的无标签泄漏。
- 作者报告：作者在 Cortex-M4 Kyber768 二项采样器上评估，并改进 LDA 选点。
- 限制与下一步：单条最终攻击迹线不消除大量目标无标签适配数据的成本；采样输出与长期私钥的映射须明确。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Avengers assemble! Supervised learning meets lattice reduction: A single power trace attack against CRYSTALS-Kyber Key Generation

- 来源：[TCHES 2025](https://doi.org/10.46586/tches.v2025.i4.409-436)；时间标记：formal publication within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Pierre-Alain Fouque; Damien Marion; Quyen Nguyen; Alexandre Wallet
- 对象：Kyber, CBD sampler, lattice reduction；类型：attack。
- 核心想法：从密钥生成 CBD 泄漏提取高置信系数，再用有限域消元或格约简补全。
- 作者报告：作者报告单攻击迹线监督学习及三档 Kyber 参数的端到端实验，另给块大小估计。
- 限制与下一步：单迹不包含训练成本；理想高置信比例、估计的格难度和实际求解时间需分别记录。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Constant time lattice reduction in dimension 4 with application to SQIsign

- 来源：[TCHES 2025](https://doi.org/10.46586/tches.v2025.i2.511-534)；时间标记：formal publication within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Otto Hanyecz; Alexander Karenin; Elena Kirshanova; Péter Kutas; Sina Schaeffler
- 对象：SQIsign, dimension-4 lattice reduction；类型：constant_time_implementation。
- 核心想法：设计四维整数格的恒时 LLL 类约简，并为输出向量长度给出保证。
- 作者报告：作者用工具检查恒时性质；实验观察实现输出 Minkowski 约简基。
- 限制与下一步：实验中的 Minkowski 性质与已证明的长度保证不同；恒时不自动说明功耗安全。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Full Key-Recovery Cubic-Time Template Attack on Classic McEliece Decapsulation

- 来源：[TCHES 2025](https://doi.org/10.46586/tches.v2025.i1.367-391)；时间标记：formal publication within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Vlad-Florin Drăgoi; Brice Colombier; Nicolas Vallet; Pierre-Louis Cayrel; Vincent Grosso
- 对象：Classic McEliece；类型：attack。
- 核心想法：从解封装 syndrome 计算中辨识置换支持，再用三次时间算法恢复 Goppa 多项式。
- 作者报告：作者在运行参考实现的微控制器上完成实际攻击并声明开放代码。
- 限制与下一步：模板能力、支持元素辨识误差及全恢复后处理需正文核查；三次复杂度不是含采集训练的总成本。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## HADES: Automated Hardware Design Exploration for Cryptographic Primitives

- 来源：[TCHES 2025](https://doi.org/10.46586/tches.v2025.i4.1-45)；时间标记：formal publication within rolling window。
- 作者：Fabian Buschkowski; Georg Land; Niklas Höher; Jan Richter-Brockmann; Pascal Sasdrich; Tim Güneysu
- 对象：HADES, Kyber, ChaCha20, hardware masking；类型：countermeasure_design_tool。
- 核心想法：将安全要求纳入密码硬件设计空间探索，结合性能预测选择可综合 HDL 实现。
- 作者报告：作者展示对称算法及 PQC 案例，并声明为 ChaCha20 与 Kyber 提供支持任意阶掩码的硬件实现。
- 限制与下一步：支持任意阶不等于每阶和每种综合布局均经过实测；性能预测、模型内安全与芯片测量要分开核查。仅读摘要，未运行工具。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 代码/数据核查：not checked；引用追踪：pending。

## HRaccoon: A High-performance Configurable SCA Resilient Raccoon Hardware Accelerator

- 来源：[TCHES 2025](https://doi.org/10.46586/tches.v2025.i3.413-436)；时间标记：formal publication within rolling window。
- 作者：Ziying Ni; Ayesha Khalid; Zhaoyu Zhang; Yijun Cui; Weiqiang Liu; Máire O’Neill
- 对象：Raccoon；类型：countermeasure。
- 核心想法：将内建掩码的 Raccoon 映射为可配置 FPGA 架构，优化算术、采样与存储调度。
- 作者报告：作者报告 Artix-7 性能，并针对 Raccoon-128 的未掩码/一阶配置进行 TVLA。
- 限制与下一步：不能把部分配置的实测扩展到所有安全等级与任意掩码阶数。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Improved Attacks Against Lattice-Based KEMs Using Hints From Hertzbleed

- 来源：[TCHES 2025](https://doi.org/10.46586/tches.v2025.i4.463-485)；时间标记：formal publication within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Zhiwei Li; Jun Xu; Jun Song; Haomeng Xu; Yan Jia; Yanli Zou; Lei Hu
- 对象：simplified CPA Kyber, NTTRU, Hertzbleed hints；类型：attack。
- 核心想法：将 NTT 模提示直接组织为低维格，改进已有 Hertzbleed 提示后处理。
- 作者报告：作者对简化 CPA Kyber 报告实际求解，对 CCA NTTRU 给出复杂度估计。
- 限制与下一步：简化 CPA Kyber 不是最终 ML-KEM；NTTRU 的估算不能写成已经完整恢复。提示获取和求解预算分别核查。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## KyberSlash: Exploiting secret-dependent division timings in Kyber implementations

- 来源：[TCHES 2025](https://doi.org/10.46586/tches.v2025.i2.209-234)；时间标记：formal publication within rolling window。
- 作者：Daniel J. Bernstein; Karthikeyan Bhargavan; Shivam Bhasin; Anupam Chattopadhyay; Tee Kiah Chia; Matthias J. Kannwischer; Franziskus Kiefer; Thales B. Paiva; Prasanna Ravi; Goutam Tamvada
- 对象：Kyber；类型：attack。
- 核心想法：分析秘密相关除法指令时延，并结合动态检测和形式化规避讨论。
- 作者报告：摘要报告 Cortex-A7 与 Cortex-M4 上的攻击及对库维护者的披露修复。
- 限制与下一步：历史受影响实现与修复后版本必须区分；不能把旧漏洞套到全部当前实现。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Leaky McEliece: Secret Key Recovery From Highly Erroneous Side-Channel Information

- 来源：[TCHES 2025](https://doi.org/10.46586/tches.v2025.i2.94-125)；时间标记：formal publication within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Marcus Brinkmann; Chitchanok Chuengsatiansup; Alexander May; Julian Nowakowski; Yuval Yarom
- 对象：Classic McEliece, Botan, Gaussian elimination；类型：attack。
- 核心想法：结合公钥与高斯消元行操作泄漏，用容错译码恢复秘密结构。
- 作者报告：作者报告错误比特模型求解，以及 STM32L592 上恒时参考实现的单迹演示。
- 限制与下一步：位翻转模型容错量不等于实际测量独立同分布误差；密钥生成目标、剖析预算和完整恢复条件须保留。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Masking-Friendly Post-Quantum Signatures in the Threshold-Computation-in-the-Head Framework

- 来源：[TCHES 2025](https://doi.org/10.46586/tches.v2025.i4.667-710)；时间标记：formal publication within rolling window。
- 作者：Thibauld Feneuil; Matthieu Rivain; Auguste Warmé-Janville
- 对象：TCitH, MPC-in-the-head, VOLE-in-the-head；类型：countermeasure。
- 核心想法：调整 TCitH 的树结构、种子公开方式与阈值分享，以降低签名掩码成本。
- 作者报告：作者分析探针安全与复杂度，并在带哈希加速器的 RISC-V 上评估模块化性能。
- 限制与下一步：代价包括签名大小与部分参数下的 soundness 调整；不是对原方案无代价的透明优化。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## MulLeak: Exploiting Multiply Instruction Leakage to Attack the Stack-optimized Kyber Implementation on Cortex-M4

- 来源：[TCHES 2025](https://doi.org/10.46586/tches.v2025.i2.23-68)；时间标记：formal publication within rolling window。
- 作者：Fan Huang; Xiaolin Duan; Chengcong Hu; Mengce Zheng; Honggang Hu
- 对象：Kyber；类型：attack。
- 核心想法：针对栈优化实现中的乘法指令构造周期级回归泄漏模型。
- 作者报告：摘要报告 Cortex-M4 上 pqm4 Kyber-768 的剖析攻击。
- 限制与下一步：已知密文与选择密文两种设定不同；不能把作者结果当成本项目公开数据上的复现。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Multi-Value Plaintext-Checking and Full-Decryption Oracle-Based Attacks on HQC from Offline Templates

- 来源：[TCHES 2025](https://doi.org/10.46586/tches.v2025.i4.254-289)；时间标记：formal publication within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Haiyue Dong; Qian Guo
- 对象：HQC, MV-PC oracle, full-decryption oracle；类型：attack。
- 核心想法：用离线模板将多值明文检查与完整解密预言机扩展到 HQC。
- 作者报告：作者分别报告完美预言机查询界、不完美响应模拟和 Cortex-M4 实验。
- 限制与下一步：hqc-128 两次查询对应完美 FD 预言机，不能写成任意实测条件下两条波形恢复。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## OT-PCA: New Key-Recovery Plaintext-Checking Oracle Based Side-Channel Attacks on HQC with Offline Templates

- 来源：[TCHES 2025](https://doi.org/10.46586/tches.v2025.i1.251-274)；时间标记：formal publication within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Haiyue Dong; Qian Guo
- 对象：HQC, PC oracle, offline templates；类型：attack。
- 核心想法：利用公开译码器建立离线模板，从一次明文检查提取多位置软信息。
- 作者报告：作者结合遗传式优化、模拟及 Cortex-M4 功耗评估不完美预言机下的收益。
- 限制与下一步：离线译码模板不等于无需真实泄漏校准；预言机调用数和波形/训练成本应分别核查。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Optimal Dimensionality Reduction using Conditional Variational AutoEncoder

- 来源：[TCHES 2025](https://doi.org/10.46586/tches.v2025.i3.164-211)；时间标记：formal publication within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Sana Boussam; Mathieu Carbone; Benoît Gérard; Guénaël Renault; Gabriel Zaid
- 对象：conditional VAE, profiled SCA, PQC evaluation；类型：method。
- 核心想法：用条件变分自编码器构造生成式剖析模型，结合信息保持降维和新的评分策略。
- 作者报告：作者给出理论收敛/复杂度分析，并在模拟及多类公开密码数据上评估。
- 限制与下一步：标题中的最优性受理论假设限制；不能把实际有限训练视为已达到全信息最优，PQC 数据具体对象待正文确认。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## PhaseSCA: Exploiting Phase-Modulated Emanations in Side Channels

- 来源：[TCHES 2025](https://doi.org/10.46586/tches.v2025.i1.392-419)；时间标记：formal publication within rolling window。
- 作者：Pierre Ayoub; Aurélien Hernandez; Romain Cayre; Aurélien Francillon; Clémentine Maurice
- 对象：AES；类型：measurement。
- 核心想法：研究电磁辐射中的相位调制，并结合幅度信息改善侧信道利用。
- 作者报告：摘要报告 SDR 测量和 AES 恢复，讨论数字抖动与相位偏移的联系。
- 限制与下一步：属于通用测量机制；尚未证明同样机制在本项目 PQC 实现中存在。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Rejected Signatures’ Challenges Pose New Challenges: Key Recovery of CRYSTALS-Dilithium via Side-Channel Attacks

- 来源：[TCHES 2025](https://doi.org/10.46586/tches.v2025.i4.817-847)；时间标记：formal publication within rolling window。
- 作者：Yuanyuan Zhou; Weijia Wang; Yiteng Sun; Yu Yu
- 对象：Dilithium, ML-DSA family；类型：attack。
- 核心想法：将被拒绝尝试的挑战与响应信息转为整数线性规划约束。
- 作者报告：摘要报告 ARM Cortex-M4 上的真实功耗实验。
- 限制与下一步：需要获知被拒绝尝试的相关内部信息；最终公开签名的挑战不能直接赋给所有拒绝尝试。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Tailorable codes for lattice-based KEMs with applications to compact ML-KEM instantiations

- 来源：[TCHES 2025](https://doi.org/10.46586/tches.v2025.i3.139-163)；时间标记：formal publication within rolling window。
- 作者：Thales B. Paiva; Marcos A. Simplicio Jr; Syed Mahbub Hafiz; Bahattin Yildiz; Eduardo L. Cominetti; Henrique S. Ogawa
- 对象：ML-KEM, error-correction codes, isochronous decoding；类型：constant_time_implementation。
- 核心想法：用可定制纠错码改善格 KEM 公钥或密文压缩，并为新增译码步骤提供等时实现。
- 作者报告：作者在 AVX2、Cortex-M4 和 Cortex-A53 上评估译码开销，并给出不依赖噪声系数独立假设的失败率分析。
- 限制与下一步：修改后的压缩参数/编码并非未经变化的标准 ML-KEM；失败率保证与等时译码不等于整套方案的物理泄漏安全。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 代码/数据核查：not checked；引用追踪：pending。

## dCTIDH: Fast & Deterministic CTIDH

- 来源：[TCHES 2025](https://doi.org/10.46586/tches.v2025.i3.516-541)；时间标记：formal publication within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Fabio Campos; Andreas Hellenbrand; Michael Meyer; Krijn Reijnders
- 对象：CSIDH, CTIDH, dCTIDH；类型：constant_time_implementation。
- 核心想法：将确定性 CSIDH 与 CTIDH 批处理结合，并联合优化素数和方案参数。
- 作者报告：作者实现恒时确定性 dCTIDH 并进行周期及域运算性能比较。
- 限制与下一步：确定性与恒时是不同性质，均不能单独推出功耗/电磁安全；保留实现及参数边界。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Breaking the Blindfold: Deep Learning-based Blind Side-channel Analysis

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/rezaeezade)；时间标记：exact public date not yet verified。
- 作者：Azade Rezaeezade, Delft University of Technology and Digital Security Group, Radboud University; Trevor Yap, Dirmanto Jap, and Shivam Bhasin, Temasek Laboratories and National integrated Centre For Evaluation, Nanyang Technological University; Stjepan Picek, Digital Security Group, Radboud University and University of Zagreb Faculty of Electrical Engineering and Computing
- 对象：AES, Ascon, Kyber；类型：method。
- 核心想法：用多点聚类标签及深度学习研究不知道明文/密文时的盲侧信道分析。
- 作者报告：摘要报告多个真实测量数据集及含失同步防护的场景。
- 限制与下一步：盲分析仍有自身训练与数据条件；不能自动推成完全无先验的非剖析攻击。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX session abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## A Framework for designing High-Order Side-Channel Protected Hardware Implementations of ML-KEM

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i2.272-295)；时间标记：formal publication within rolling window。
- 作者：Eros Camacho-Ruiz; Pablo Navarro-Torrero; Alejandro Cabrera Aldaya
- 对象：ML-KEM；类型：countermeasure。
- 核心想法：提出 HOPE-MLKEM，面向多安全级别及各操作的可配置高阶掩码硬件框架。
- 作者报告：摘要报告 FPGA/ASIC 评估并声明开源。
- 限制与下一步：“支持高阶”不等于每阶、每操作均获实测认证；完整评估矩阵和代码版本仍需核查。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## ABRA-CAPA-DABRA: Full break of CAPA

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i3.334-341)；时间标记：formal publication within rolling window。
- 作者：Paco Azevedo-Oliveira
- 对象：CAPA；类型：attack。
- 核心想法：在组合探测与故障模型中，利用 CAPA 原始 Beaver triples 生成部分的关系提出线性系统攻击。
- 作者报告：作者报告原组合防护在其自身模型下不安全。
- 限制与下一步：属于模型内的组合攻击；摘要没有给出整片器件实测证据，且不代表全部 MPC 型防护被攻破。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## AIPS: AI-Based Power Simulation for Pre-Silicon Side-Channel Security Evaluation

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i2.441-467)；时间标记：formal publication within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Ya Gao; Haocheng Ma; Tanchen Zhang; Jiaji He; Yiqiang Zhao; Mirjana Stojilović; Yier Jin
- 对象：AES, Kyber, RISC-V, pre-silicon power simulation；类型：method。
- 核心想法：用切换活动和工艺库特征条件化扩散模型，生成门级瞬态功耗以加速硅前评估。
- 作者报告：作者以 PrimeTime PX 产生的迹线训练，在五种目标上比较波形和侧信道评估。
- 限制与下一步：参照是 EDA 功耗模拟，不是实测硅片真值；推理加速与含训练的总成本分开。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Adapting AES-Oriented Optimizations to Rijndael-256: Cortex-M4, ARMv8-A, and CUDA

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i4.575-596)；时间标记：formal publication within rolling window。
- 作者：Siwoo Eum; Minho Song; Minjoo Sim; Anupam Chattopadhyay; Hwajeong Seo
- 对象：Rijndael-256, Cortex-M4, ARMv8-A, CUDA, PQC signatures；类型：constant_time_implementation。
- 核心想法：将 AES 优化适配到 Rijndael-256 的较宽状态，并研究其作为 PQC 签名组件时的性能。
- 作者报告：摘要明确限定 Cortex-M4 位切片版本具有秘密无关的控制流和访存；AArch64 重用 AESE，CUDA 使用共享内存 T 表。
- 限制与下一步：不能把 Cortex-M4 的性质推广到另两种实现；PQC 集成性能来自 Apple M2，不能据此宣称这些签名均获恒时或功耗保护。具体四个签名对象待正文核对。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 代码/数据核查：not checked；引用追踪：pending。

## Compressed Key Exchange Protocol from Orientations of Large Discriminant Using AVX-512

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i3.679-718)；时间标记：formal publication within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Yuhao Zheng; Jianming Lin; Yutong Liang; Yanzhen Ren; Huixin Zhang; Chang-An Zhao
- 对象：CSIDH-LDO, AVX-512, public-key compression；类型：constant_time_implementation。
- 核心想法：联合设计大判别式定向群作用的恒时 SIMD 实现与公钥压缩。
- 作者报告：作者在 Tiger Lake 比较含 dummy 和不含 dummy 的调度，并提出公钥压缩框架。
- 限制与下一步：不同调度的物理观测条件及安全证明需分别核查；高速和公钥更小不等于抵抗功耗泄漏。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## DPA-Style Attacks on HQC

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i2.928-952)；时间标记：formal publication within rolling window。
- 作者：Zhuo Huang; Weijia Wang; Xiaogang Zhou; Yu Yu
- 对象：HQC；类型：attack。
- 核心想法：针对解封装稀疏多项式关系构造 DPA，并扩展到一阶掩码下的二阶特征。
- 作者报告：作者区分仿真、剖析与非剖析 STM32F4 实测恢复。
- 限制与下一步：各成本分别依赖输入控制、噪声、剖析和保护配置；摘要中的标准化表述不作为当前 NIST 状态依据。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Efficient High-Order Masking of FrodoKEM’s CDT-Based Gaussian Sampler

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i2.868-892)；时间标记：formal publication within rolling window。
- 作者：Elie Eid; Aurélien Greuet; Nathan Reboud; Rina Zeitoun
- 对象：FrodoKEM, CDT sampling；类型：countermeasure。
- 核心想法：设计更高效的高阶 CDT 高斯采样掩码组件，降低比较与随机性成本。
- 作者报告：作者报告 ISW 探针安全论证、Cortex-M3 一阶完整实现评估及通用高阶 C 代码。
- 限制与下一步：高阶代码支持与一阶实测覆盖分开；性能比例依赖所比基线和采样表。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Efficient and Compact High-order Masking Raccoon on Memory Constrained Devices

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i4.369-396)；时间标记：formal publication within rolling window。
- 作者：Junhao Huang; Yiteng Sun; Jipeng Zhang; Weijia Wang; Donglong Chen; Haiyang Xue; Guoming Yang
- 对象：Raccoon；类型：countermeasure。
- 核心想法：优化多模数 NTT、采样调用和内存布局，使资源受限设备可运行高阶 Raccoon。
- 作者报告：作者报告 Cortex-M4 性能与缓解微架构转换泄漏后的二阶评估。
- 限制与下一步：实现支持的高阶范围不等于每阶均获实测验证；转换泄漏缓解是实测结论的条件。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Efficient and Parallel Implementation of Isogeny-based Deterministic Group Actions

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i3.541-565)；时间标记：formal publication within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Weize Wang; Yi-Fu Lai; Kaizhan Lin; Yunlei Zhao
- 对象：OSIDH-LD, isogeny group actions, AVX-512；类型：constant_time_implementation。
- 核心想法：优化恒时、确定性且无 dummy 的大判别式定向群作用，结合裁尾和并行执行。
- 作者报告：作者提供 C/汇编及线程、AVX-512 实现，报告密钥生成和协商的性能改进。
- 限制与下一步：摘要明确保持确定性与无 dummy 特性；优化后具体二进制的完整恒时保证与功耗表现仍需核查，不能只由算法起点推定。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## From Multiplication to Recovery: A Single-trace Side-Channel Attack on HQC

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i4.890-916)；时间标记：formal publication within rolling window。
- 作者：Yikang Guo; Yuchang Hu; Yanbin Li; Shilin Sun; Geng Chen; Chunpeng Ge; Jiankuo Dong
- 对象：HQC；类型：attack。
- 核心想法：对迭代 Karatsuba 构造适合二进制稀疏结构的因子图，并联合乘法与译码泄漏。
- 作者报告：摘要报告参考实现及 liboqs 扩展上的恢复评估。
- 限制与下一步：摘要不足以确定所有平台、观测条件及恢复对象细节，需全文核查。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## FrozenTRU: Cold Boot Attacks on NTRU-Based Hash-and-Sign Signatures

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i3.1007-1031)；时间标记：formal publication within rolling window。
- 作者：Hiroto Kaihara; Mehdi Tibouchi; Masayuki Abe
- 对象：Falcon, DLP；类型：attack。
- 核心想法：针对浮点表示的 NTRU 型签名秘密，利用有噪内存及近似代数关系进行冷启动恢复。
- 作者报告：作者报告位翻转模型仿真与 Raspberry Pi 上 Falcon 冷启动实验，并提出表示层防护。
- 限制与下一步：单一位翻转模型不代表所有 DRAM；需区分模拟和实际存储噪声、硬件接触条件及方案范围。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Hardness of Learning with Physical Rounding and Noise from Learning With Errors

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i3.1056-1079)；时间标记：formal publication within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Clément Hoffmann; Emeline Repel; Adeline Roux-Langlois; François-Xavier Standaert
- 对象：LWPRN, LWPR, LWE, fresh re-keying；类型：leakage_resilience_theory。
- 核心想法：将有噪物理约舍入问题 LWPRN 的难度归约到 LWE，研究可负担噪声下的泄漏韧性基础。
- 作者报告：作者讨论 fresh re-keying、潜在 PQC 应用及曾使无噪 LWPR 不安全的串行实现情形。
- 限制与下一步：这是特定物理函数和噪声条件下的理论结果；潜在 PQC 应用不是已实现的 ML-KEM/ML-DSA 防护，也未据摘要认定实测。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## How Strong is the FO-Calypse, Really? Instantiating Plaintext-Checking Oracles against Masked Software Implementations of ML-KEM

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i4.759-785)；时间标记：formal publication within rolling window。
- 作者：Brieuc Balon; Gaëtan Cassiers; Thibaud Schoenauen; François-Xavier Standaert
- 对象：ML-KEM, Keccak；类型：attack。
- 核心想法：量化掩码 Keccak 上明文检查预言机的实现精度，并比较软决策与硬决策利用。
- 作者报告：摘要报告三种开源软件实现和 ARM Cortex-M4 上的剖析评估。
- 限制与下一步：份额数、重复执行数、剖析能力与计算预算须联合核对；未核查全文实验细节。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Keep it Simple: Refreshing the NTT of Kyber’s Decapsulation to Prevent Plaintext-Checking Side-Channel Attacks

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i1.472-499)；时间标记：formal publication within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Duyên Pay; François-Xavier Standaert
- 对象：Kyber, NTT, masking, shuffling；类型：countermeasure。
- 核心想法：用线性开销组件刷新 NTT 各层，限制信念传播沿层累积信息。
- 作者报告：作者结合模拟和实测分析低噪声条件，比较参考 C、汇编实现及 lazy reduction 的剖析困难。
- 限制与下一步：结论依赖噪声、刷新和实现；不能把特定评估扩为整个 KEM 任意攻击下的证明。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Key-Recovery Side-Channel Attack on the Berlekamp-Massey Decoding Algorithm in the Classic McEliece KEM

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i4.838-862)；时间标记：formal publication within rolling window。
- 作者：Andrei Alexei; Marios Omar Choudary; Vlad-Florin Drăgoi
- 对象：Classic McEliece；类型：attack。
- 核心想法：利用 Berlekamp-Massey 译码泄漏恢复 Goppa 支持，再接入带提示的代数恢复。
- 作者报告：作者报告未保护参考/嵌入式实现与 Cortex-M4 平台上的模板攻击。
- 限制与下一步：每秘密系数一条攻击迹线不等于完整私钥只需一条；模板训练和后处理成本需单列。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## MAGNET: MAsked Gaussian Now Efficient and Table-less

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i3.769-804)；时间标记：formal publication within rolling window。
- 作者：Mert Yassi; Soundes Marzougui; Raymond K. Zhao; Muhammed F. Esgin; Amin Sakzad; Ron Steinfeld
- 对象：discrete Gaussian sampling；类型：countermeasure。
- 核心想法：将布尔电路型离散高斯采样器实现为掩码友好组件，避免大表或重浮点成本。
- 作者报告：作者给出任意阶 C 及 Cortex-M4 一阶实现，并报告 TVLA 与泄漏组件加固。
- 限制与下一步：性能随标准差与阶数变化；其引用的差分隐私采样基础论文应沿引用核查，不能被 PQC 关键词漏掉。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## ML-DSA masking sweetened with SUCRE: Shuffle-and-Unmask Countermeasure for REjection sampling

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i1.618-659)；时间标记：formal publication within rolling window。
- 作者：Sonia Belaïd; Ryad Benadjila; Julien Devevey; Morgane Guerreau; Thomas Legavre; Ange Martinelli; Thomas Ricosset; Matthieu Rivain; Mélissa Rossi
- 对象：ML-DSA；类型：countermeasure。
- 核心想法：在保持无穷范数的同时打乱并解掩码向量，以降低拒绝采样保护开销。
- 作者报告：摘要报告探针模型证明、额外 MLWR 变体假设和实现性能。
- 限制与下一步：安全论证依赖其新假设与允许泄漏范围；性能结果不等于完整芯片实测安全。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Masked Solving of Linear Equations System and Application to UOV Signatures

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i2.51-72)；时间标记：formal publication within rolling window。
- 作者：Jean-Sébastien Coron; François Gérard; Bowen Zhang
- 对象：UOV；类型：countermeasure。
- 核心想法：改进任意阶掩码线性方程组求解，以求逆方法替代部分掩码高斯消元开销。
- 作者报告：作者给出 t-probing 论证及完整掩码 UOV 签名 C 实现，并与 mUOV 等比较。
- 限制与下一步：摘要主要提供证明与性能；不能自行补充硬件泄漏实验或推广到未覆盖的编译配置。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## NTT-PEEL: Bit Shift Side-Channel in FALCON’s Number Theoretic Transform

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i2.709-735)；时间标记：formal publication within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Jinyi Qiu; Aydin Aysu
- 对象：Falcon, NTT；类型：attack。
- 核心想法：利用原地模约减中的位移泄漏，以前向/后向处理组合 NTT 结构约束。
- 作者报告：作者在 Cortex-M4 上评估 NIST round-3 参考和优化实现，并结合格约简降低搜索空间。
- 限制与下一步：降低剩余搜索空间不等于直接完整私钥恢复；历史实现与最终标准化版本须区分。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Neur-SASCA: High-Noise-Tolerant and Automated Single-Trace Attack against NTT

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i3.908-932)；时间标记：formal publication within rolling window。
- 作者：Yuxuan Wang; Jintong Yu; Yihan Nie; Yubo Zhao; Xiaolin Zhang; Yipeng Shi; Chi Zhang; Zhedong Wang; Dawu Gu
- 对象：NTT, ML-KEM family；类型：method。
- 核心想法：联合端到端神经网络、概率校准与 GPU 信念传播，降低 NTT SASCA 的人工定位需求。
- 作者报告：作者报告 SAM4S 上同设备和跨设备实验以及完整 NTT 输入恢复。
- 限制与下一步：单攻击迹线仍需剖析数据；恢复 NTT 输入不应未经映射就写成完整 KEM 私钥恢复。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Non-supervised SASCA on the VOLEitH Framework

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i2.468-494)；时间标记：formal publication within rolling window。
- 作者：Julie Godard; Nicolas Aragon; Philippe Gaborit; Antoine Loiseau; Julien Maillard
- 对象：VOLEitH, FAEST, SDitH；类型：attack。
- 核心想法：利用 VOLE 相关性和冗余构造单迹 SASCA，并以聚类替代监督标签。
- 作者报告：作者报告 STM32F303RE 实测与多个参数集上的秘密数据恢复。
- 限制与下一步：非监督不等于无结构先验；“秘密数据”的具体对象及端到端私钥范围需正文确认。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Racing against the clock: side-channel leakage from crossing asynchronous clock domains

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i2.28-50)；时间标记：formal publication within rolling window。
- 作者：Martin Thompson; David Oswald
- 对象：AES, RSA；类型：measurement。
- 核心想法：研究异步时钟域跨越的周期变化如何作为功耗的间接观测。
- 作者报告：摘要报告 x86、嵌入式 SoC、仿真与 FPGA 实验，并展示跨线程攻击。
- 限制与下一步：作者对物理原因提出假设并提供证据；各平台结果不能混成同一机制已普遍成立。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Secret Key Recovery of FALCON using Simple Power Analysis in Conditional Calculator

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i2.953-975)；时间标记：formal publication within frozen 2021-11-12 to 2026-11-12 window。
- 作者：GyuSang Kim; JeongHwan Lee; Myeonghoon Lee; Seokhie Hong; HeeSeok Kim
- 对象：Falcon, floating-point conditional calculator；类型：attack。
- 核心想法：从浮点转换及 FFT 浮点加法的条件计算器泄漏组织候选剪枝与容错排序。
- 作者报告：作者比较两种防护并报告多密钥后处理，包含人为破坏部分泄漏条目的评估。
- 限制与下一步：人为注入条目错误不等于真实波形误差分布；摘要未充分说明测量平台和端到端采集预算，不能补猜。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Slicing Bits and Cutting Costs in CDT Sampling: High-Order Masking of FrodoKEM’s Gaussian Sampler, Revisited

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i4.549-574)；时间标记：formal publication within rolling window。
- 作者：Calvin Abou Haida; Thomas Espitau; Clément Hoffmann; Mehdi Tibouchi
- 对象：FrodoKEM, CDT sampling；类型：countermeasure。
- 核心想法：比较掩码 CDT 采样设计并通过位切片、比较器与复用器优化批量生成。
- 作者报告：作者报告 Cortex-M4 上对两条已有采样防护路线的性能改进。
- 限制与下一步：性能改进不能替代独立泄漏验证；需对齐表大小、阶数与代码语言后比较。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Sota Voce: Low-Noise Sampling of Sparse Fixed-Weight Vectors

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i1.353-375)；时间标记：formal publication within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Décio Luiz Gazzoni Filho; Gora Adj; Slim Bettaieb; Alessandro Budroni; Jorge Chávez-Saab; Francisco Rodríguez-Henríquez
- 对象：HQC, sparse fixed-weight sampling；类型：constant_time_implementation。
- 核心想法：优化稀疏固定重量采样的支持映射与向量构造，并应用到 HQC。
- 作者报告：作者论证算法与采样偏差，并给出采样步骤及协议级性能。
- 限制与下一步：题名 low-noise 不应解释成测量噪声；摘要讨论恒时采样流程与统计偏差，未报告功耗防护验证。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## TAME: A Deep Learning-based Blind Side-Channel Analysis Framework

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i4.632-655)；时间标记：formal publication within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Jintong Yu; Yuxuan Wang; Pei Cao; Zixin He; Yubo Zhao; Zhiliang An; Yipeng Shi; Chi Zhang; Dawu Gu
- 对象：AES, ASCON, Kyber, blind SCA；类型：method。
- 核心想法：在低维表示中聚类，并用高置信簇内样本指导元加权，降低盲分析标签噪声。
- 作者报告：作者在三种算法与失同步设置下比较恢复和猜测熵。
- 限制与下一步：盲分析缺少明密文不等于没有结构先验；各算法预算、恢复目标和失同步强度须分别读正文核对。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Tempo: An ML-KEM to PAKE Compiler Resilient to Timing Attacks

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i3.744-768)；时间标记：formal publication within rolling window。
- 作者：Afonso Arriaga; Manuel Barbosa; Stanislaw Jarecki
- 对象：ML-KEM, PAKE；类型：countermeasure。
- 核心想法：指出 PAKE 组合会改变“公钥可公开”的边界，并通过公开矩阵种子设计避免相关变时扩展泄漏。
- 作者报告：作者比较恒时替代方案与 Tempo 编译器，给出 UC 模拟及 Oracle-MLWE 假设关系。
- 限制与下一步：协议级假设、所公开种子和密码口令保护须联合核对；不是对所有 ML-KEM 调用的漏洞声明。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Verified non-recursive calculation of Beneš networks applied to Classic McEliece

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i3.306-333)；时间标记：formal publication within rolling window。
- 作者：Wrenna Robson; Samuel Kelly
- 对象：Classic McEliece, Beneš networks, constant-time permutation, Lean, AVX2；类型：constant_time_implementation_and_verification。
- 核心想法：构造非递归 Beneš 网络控制位算法，针对秘密置换避免依赖秘密的分支与访存。
- 作者报告：正文说明便携 C 与 AVX2 实现遵循恒时规则，并使用 cryptoint、DOIT 指令及 Valgrind 检查；另给出 Lean 数学证明。
- 限制与下一步：Lean 原型不以恒时为目标，FastCycleMin/oSort 存在作者明确的形式验证缺口；Valgrind 只用于其列出的分支和访存检查，不能当作端到端证明或物理泄漏评估。
- 阅读层级：selected_full_text_sections；来源：https://tches.iacr.org/index.php/TCHES/article/download/13094/12645。
- 已读章节：PDF p.1 (printed p.306): abstract and problem statement; PDF p.17 (printed p.322), sections 4.4 and 5: Lean verification gap and constant-time implementation checks
- [详细阅读记录](notes/tches-implementation-evidence-boundaries-20261113.md)
- 代码/数据核查：not checked；引用追踪：pending。

## When Masking Multiplication Isn’t Enough: Exploiting Floating-Point Leakage in Falcon’s Pre-Image Computation

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i2.686-708)；时间标记：formal publication within rolling window。
- 作者：Keng-Yu Chen; Ming Qing Ching; Jiun-Peng Chen; Bo-Yin Yang
- 对象：Falcon；类型：attack。
- 核心想法：研究浮点预像计算中乘法掩码未覆盖的泄漏，并细化尾数和指数恢复分析。
- 作者报告：摘要报告针对已有乘法保护的两组功耗实验。
- 限制与下一步：结论针对所测保护范围；不能推成所有 Falcon 掩码实现不安全。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## t-Probing (In-)Security: Pitfalls on Noise Assumptions

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i2.1-27)；时间标记：formal publication within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Dina Hesse; Jakob Feldtkeller; Tim Güneysu; Julius Hermelink; Georg Land; Markus Krausz; Jan Richter-Brockmann
- 对象：fixed-weight polynomial sampling, t-probing；类型：attack_and_model_analysis。
- 核心想法：研究从 t-probing 证明转移到实际泄漏时的噪声条件，强调非均匀份额的影响。
- 作者报告：作者报告对十阶掩码固定重量采样的无监督单迹攻击，并分析所需额外噪声。
- 限制与下一步：论文不宣称 t-probing 数学证明错误；漏洞在实际模型对应与参数条件，不能概括为所有十阶掩码无效。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher-deposited Crossref abstract。
- 代码/数据核查：not checked；引用追踪：pending。

## Unlocking the True Potential of Decryption Failure Oracles: A Hybrid Adaptive-LDPC Attack on ML-KEM Using Imperfect Oracles

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/guo-qian)；时间标记：exact public date not yet verified。
- 作者：Qian Guo, Denis Nabokov, and Thomas Johansson, Lund University
- 对象：ML-KEM；类型：attack。
- 核心想法：将自适应查询与 LDPC 信念传播结合，利用有误差的解密失败预言机。
- 作者报告：摘要给出预言机模型结果，并报告在 GoFetch 场景下的应用。
- 限制与下一步：抽象预言机查询数与底层测量迹线数分开；引用全文与实测复现仍待补查。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX session abstract。
- 代码/数据核查：not checked；引用追踪：pending。
