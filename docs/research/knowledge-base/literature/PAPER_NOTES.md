# 已阅读论文卡片

状态：持续整理，尚未覆盖全部相关论文。按每篇实际阅读层级报告；作者报告不等于本地复现。

当前 225 篇；按 DOI 或官方页面关联目录，边界论文继续保留。

## Jasmin: High-Assurance and High-Speed Cryptography

- 来源：[CCS 2017](https://doi.org/10.1145/3133956.3134078)；时间标记：outside rolling window; cited foundation retained。
- 作者：José Bacelar Almeida; Manuel Barbosa; Gilles Barthe; Arthur Blot; Benjamin Grégoire; Vincent Laporte; Tiago Oliveira; Hugo Pacheco; Benedikt Schmidt; Pierre-Yves Strub
- 对象：Jasmin, constant-time, verified compiler；类型：formal_verification_and_implementation。
- 核心想法：以专用语言和经过证明的编译方法兼顾高保证密码实现与性能。
- 作者报告：机构摘要报告 Coq 编译器证明、内存安全及恒时分析和 x64 性能比较。
- 限制与下一步：恒时与功能证明有指定观察模型；不能将 2017 工作解释为覆盖后来 Spectre 或物理功耗的一般保证。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://researchportal.ip-paris.fr/en/publications/jasmin-high-assurance-and-high-speed-cryptography/。
- 代码/数据核查：not checked；引用追踪：pending。

## Single-Trace Side-Channel Attacks on Masked Lattice-Based Encryption

- 来源：[CHES 2017](https://doi.org/10.1007/978-3-319-66787-4_25)；时间标记：outside rolling window; explicitly cited foundational work。
- 作者：Robert Primas; Peter Pessl; Stefan Mangard
- 对象：lattice encryption, NTT, masking, belief propagation；类型：pqc_single_trace_side_channel。
- 核心想法：将 NTT 模运算的模板匹配、信念传播与格译码组合，研究掩码格加密的一条攻击轨迹恢复。
- 作者报告：作者同时报告通用噪声 HW 模型及 ARM Cortex-M4F 实测轨迹上的恢复。
- 限制与下一步：这是 CHES 2017 的窗口外基础工作；single trace 指攻击观察，不代表没有模板训练、设备或校准成本。掩码阶数、实现及算法迁移范围待全文核对，不能扩展为全部最终 PQC 标准。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://link.springer.com/chapter/10.1007/978-3-319-66787-4_25。
- 代码/数据核查：not checked；引用追踪：pending。

## Masking the GLP Lattice-Based Signature Scheme at Any Order

- 来源：[EUROCRYPT 2018](https://doi.org/10.1007/978-3-319-78375-8_12)；时间标记：outside rolling window; cited foundation retained。
- 作者：Gilles Barthe; Sonia Belaïd; Thomas Espitau; Pierre-Alain Fouque; Benjamin Grégoire; Mélissa Rossi; Mehdi Tibouchi
- 对象：GLP, lattice signatures, masking；类型：countermeasure。
- 核心想法：为无需离散高斯采样的 GLP 格签名构造任意阶掩码，并扩展份额转换组件。
- 作者报告：摘要报告 ISW/探针模型下的保护方法、考虑公开输出的定义及概念实现。
- 限制与下一步：形式探针保证与概念实现不等于真实平台任意阶泄漏验证；与 2024 年期刊版分列并建立版本关系。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://link.springer.com/chapter/10.1007/978-3-319-78375-8_12。
- 代码/数据核查：not checked；引用追踪：pending。

## Masking Dilithium: Efficient Implementation and Side-Channel Evaluation

- 来源：[ACNS 2019](https://doi.org/10.1007/978-3-030-21568-2_17)；时间标记：outside rolling window; cited foundation retained。
- 作者：Vincent Migliore; Benoît Gérard; Mehdi Tibouchi; Pierre-Alain Fouque
- 对象：Dilithium, masking, Cortex-M3；类型：countermeasure_and_evaluation。
- 核心想法：早期 Dilithium 掩码实现及侧信道评价，研究参数和转换操作的保护成本。
- 作者报告：摘要报告 Cortex-M3 上的未保护泄漏与掩码评价；模数变更加速最耗时的掩码操作。
- 限制与下一步：不能把组件加速当成全签名加速或最终 ML-DSA 结果；2023 Protecting 论文修正了其部分敏感性分类。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://link.springer.com/chapter/10.1007/978-3-030-21568-2_17。
- 代码/数据核查：not checked；引用追踪：pending。

## An Efficient and Provable Masked Implementation of qTESLA

- 来源：[CARDIS 2019](https://doi.org/10.1007/978-3-030-42068-0_5)；时间标记：outside rolling window; cited foundation retained。
- 作者：François Gérard; Mélissa Rossi
- 对象：qTESLA, masking；类型：countermeasure。
- 核心想法：将格签名掩码方法推进到 qTESLA，并调整参数和转换组件以改善保护成本。
- 作者报告：摘要报告任意阶构造、专门的一阶组件和不同阶数的实现可行性评价。
- 限制与下一步：CARDIS 2019 论文集章节于 2020-03-09 上线；涉及参数调整，不代表原参数或最终标准的物理安全。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://link.springer.com/chapter/10.1007/978-3-030-42068-0_5。
- 代码/数据核查：not checked；引用追踪：pending。

## A Key-Recovery Timing Attack on Post-quantum Primitives Using the Fujisaki-Okamoto Transformation and Its Application on FrodoKEM

- 来源：[CRYPTO 2020](https://doi.org/10.1007/978-3-030-56880-1_13)；时间标记：outside rolling window; explicitly cited foundational work。
- 作者：Qian Guo; Thomas Johansson; Alexander Nilsson
- 对象：FrodoKEM, Fujisaki-Okamoto, ciphertext comparison；类型：pqc_timing_side_channel。
- 核心想法：研究 FO 转换中密文比较的时序泄漏，说明不能只保护底层 CPA 原语的直接秘密运算。
- 作者报告：作者在当时 FrodoKEM 参考实现上报告密钥恢复，并给出约 2^30 次解封装调用的实验量级。
- 限制与下一步：这是 CRYPTO 2020 的窗口外基础工作；需核对攻击时序精度、实现版本和各参数预算，不能推断当前恒时实现或全部 FO 转换都可攻击。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://link.springer.com/chapter/10.1007/978-3-030-56880-1_13。
- 代码/数据核查：not checked；引用追踪：pending。

## Constant-time foundations for the new spectre era

- 来源：[PLDI 2020](https://doi.org/10.1145/3385412.3385970)；时间标记：outside rolling window; cited foundation retained。
- 作者：Sunjay Cauligi; Craig Disselkoen; Klaus v. Gleissenthall; Dean Tullsen; Deian Stefan; Tamara Rezk; Gilles Barthe
- 对象：constant-time, speculative execution, Pitchfork；类型：formal_model_and_analysis。
- 核心想法：把推测与乱序执行纳入恒时语义及分析，检查传统恒时抽象的遗漏。
- 作者报告：作者摘要报告微架构攻击者模型与 Pitchfork 对密码库的检查。
- 限制与下一步：阅读作者 arXiv v3 摘要并与正式 DOI 核对身份；该观察模型不自动覆盖功耗、EM 或所有硬件实现。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://arxiv.org/abs/1910.01755。
- 代码/数据核查：not checked；引用追踪：pending。

## The Last Mile: High-Assurance and High-Speed Cryptographic Implementations

- 来源：[SP 2020](https://doi.org/10.1109/sp40000.2020.00028)；时间标记：outside rolling window; cited foundation retained。
- 作者：Jose Bacelar Almeida; Manuel Barbosa; Gilles Barthe; Benjamin Gregoire; Adrien Koutsos; Vincent Laporte; Tiago Oliveira; Pierre-Yves Strub
- 对象：Jasmin, EasyCrypt, ChaCha20, Poly1305, constant-time；类型：formal_verification_and_implementation。
- 核心想法：联结参考规格、优化实现和恒时检查，缩小高保证密码代码的最后实现差距。
- 作者报告：摘要及引言说明 Jasmin/EasyCrypt 方法与向量化 ChaCha20/Poly1305 案例，检查控制流和访存的秘密依赖。
- 限制与下一步：指定恒时观察模型不等于功耗或 EM 无泄漏；本批只读方法概述，未核验完整证明或运行工具。
- 阅读层级：selected_full_text_sections；来源：https://conferences.computer.org/sp/pdfs/sp/2020/349700a965.pdf。
- 已读章节：IEEE 18 页 PDF 第 1 页摘要与 §1 方法概述。
- [详细阅读记录](notes/masking-lineage-and-kyber-hardware-evidence-20261113.md)
- 代码/数据核查：not checked；引用追踪：pending。

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

## Mitaka: A Simpler, Parallelizable, Maskable Variant of Falcon

- 来源：[EUROCRYPT 2022](https://doi.org/10.1007/978-3-031-07082-2_9)；时间标记：within frozen 2021-11-12 to 2026-11-12 window; publication/version dates retained。
- 作者：Thomas Espitau; Pierre-Alain Fouque; François Gérard; Mélissa Rossi; Akira Takahashi; Mehdi Tibouchi; Alexandre Wallet; Yang Yu
- 对象：Mitaka, Falcon, Gaussian sampling, masking；类型：algorithm_and_countermeasure。
- 核心想法：重组 Falcon 类签名采样与实现，以支持更简单、可并行和可掩码的构造。
- 作者报告：作者给出探针模型下任意阶方案及初步 C 性能；作者稿 §6 明示初步浮点代码不保证恒时。
- 限制与下一步：形式掩码、初步性能和物理泄漏评价分开；不能把作者稿的性能或模型保证扩展为最终 Falcon/FN-DSA 的安全实现。
- 阅读层级：selected_full_text_sections；来源：https://link.springer.com/chapter/10.1007/978-3-031-07082-2_9。
- 已读章节：作者 52 页稿 PDF 第 1 页摘要、§6–7 指定段落（PDF 17–19）：初步实现的非恒时限制、基准条件及探针掩码；未核对与正式章节的逐字差异。
- [详细阅读记录](notes/masking-lineage-and-kyber-hardware-evidence-20261113.md)
- 代码/数据核查：author manuscript links https://github.com/espitau/Mitaka-EC22 ; repository contents not retrieved；引用追踪：pending。

## PACMAN: attacking ARM pointer authentication with speculative execution

- 来源：[ISCA 2022](https://doi.org/10.1145/3470496.3527429)；时间标记：formal publication within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Joseph Ravichandran; Weon Taek Na; Jay Lang; Mengjia Yan
- 对象：ARM pointer authentication, Apple M1；类型：attack。
- 核心想法：将内存破坏能力与投机执行侧信道组合，泄漏 PAC 校验结果而不产生架构级崩溃。
- 作者报告：作者报告 Apple M1 和跨特权层 PoC，并研究 TLB 结构。
- 限制与下一步：绕过 Pointer Authentication 需要相关软件漏洞及攻击原语；不能理解为无前提任意内存入侵，也不是 PQC 攻击。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://dspace.mit.edu/server/api/core/bitstreams/f81a1533-d11a-4483-b921-d98c783830e2/content。
- 代码/数据核查：not checked；引用追踪：forward edge observed; backward and exhaustive forward search pending。

## Leveling Dilithium against Leakage: Revisited Sensitivity Analysis and Improved Implementations

- 来源：[NIST PQC conference 2022](https://csrc.nist.gov/presentations/2022/leveling-dilithium-against-leakage)；时间标记：within frozen 2021-11-12 to 2026-11-12 window; publication/version dates retained。
- 作者：Melissa Azouaoui; Olivier Bronchain; Gaëtan Cassiers; Clément Hoffmann; Yulia Kuzovkova; Joost Renes; Tobias Schneider; Markus Schönauer; François-Xavier Standaert; Christine van Vredendaal
- 对象：Dilithium, leveled implementations, masking；类型：historical_countermeasure_version。
- 核心想法：保留 Raccoon 实际引用的 2022 年 Leveling 版本，其敏感性分类区别于后来的正式论文。
- 作者报告：旧摘要将计算分为 DPA、SPA 和可无界泄漏部分，并组合组件与打乱；结论把形式充分条件列为开放问题。
- 限制与下一步：2023 Protecting §3.4 明确修正只需 SPA 的推测；不能用今天同号 ePrint 的新标题替代旧引文，旧性能也不能代表修正版保证。
- 阅读层级：selected_full_text_sections；来源：https://csrc.nist.gov/presentations/2022/leveling-dilithium-against-leakage。
- 已读章节：NIST 固定 25 页稿 PDF 第 1 页摘要、第 19 页表 3 说明与 §7 结论；不是对 ePrint 初版字节相同的声明。
- [详细阅读记录](notes/masking-lineage-and-kyber-hardware-evidence-20261113.md)
- 代码/数据核查：not checked；引用追踪：pending。

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

## A Side-Channel Attack on a Masked Hardware Implementation of CRYSTALS-Kyber

- 来源：[ASHES 2023](https://doi.org/10.1145/3605769.3623992)；时间标记：within frozen 2021-11-12 to 2026-11-12 window; publication/version dates retained。
- 作者：Yanning Ji; Elena Dubrova
- 对象：Kyber, masked FPGA, deep learning, message recovery；类型：hardware_side_channel_attack。
- 核心想法：针对一阶掩码 FPGA Kyber-512 的消息解码，利用 HD 泄漏直接推断消息。
- 作者报告：官方摘要报告无需显式恢复各份额的剖析方法，重复同一解封装可提高共享密钥恢复成功率。
- 限制与下一步：共享/会话密钥不同于长期私钥；重复预算与平台迁移条件需读正文，不能把摘要百分比用于跨论文排名。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://www.sigsac.org/ccs/CCS2023/tocs/tocs-ashes23.html。
- 代码/数据核查：not checked；引用追踪：pending。

## Too Many Hints – When LLL Breaks LWE

- 来源：[ASIACRYPT 2023](https://doi.org/10.1007/978-981-99-8730-6_4)；时间标记：formal publication within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Alexander May; Julian Nowakowski
- 对象：LWE, Kyber, perfect and modular hints；类型：method。
- 核心想法：批量整合完美与模提示，降低构造格基和随后 LLL/BKZ 求解的成本。
- 作者报告：作者评估密码学维度的提示数量与实际约简恢复时间。
- 限制与下一步：提示是给定的正确内积信息，不等于已经从同数量功耗迹线取得；提示获取、分布及误差条件须单独核查。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://eprint.iacr.org/2023/777。
- 代码/数据核查：not checked；引用追踪：forward edge observed; backward and exhaustive forward search pending; forward citation observed; exhaustive backward/forward closure pending。

## Evaluating Side-Channel Attack Vulnerabilities in Post-Quantum CRYSTALS-Kyber Hardware Based on Simple Power Analysis

- 来源：[ASID 2023](https://doi.org/10.1109/asid60355.2023.10426450)；时间标记：within frozen 2021-11-12 to 2026-11-12 window; publication/version dates retained。
- 作者：Munkhbaatar Chinbat; Liji Wu; Xiangmin Zhang; Altantsooj Batsukh; Yifan Yang; Le Wu
- 对象：Kyber, FPGA, simple power analysis；类型：hardware_side_channel_evaluation。
- 核心想法：考察 Kyber 硬件解封装期间消息编码的简单功耗分析风险。
- 作者报告：摘要描述 k=3 配置和一条完整执行中 6,072,500 个采样点的分析。
- 限制与下一步：采样点数不能当作 trace 数或密钥恢复预算；摘要不足以核定长期密钥恢复。会议为 2023，Xplore 收录年份不替换会议年。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/10426450/。
- 代码/数据核查：not checked；引用追踪：pending。

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

## A Side-Channel Attack on a Hardware Implementation of CRYSTALS-Kyber

- 来源：[ETS 2023](https://doi.org/10.1109/ets56758.2023.10174000)；时间标记：within frozen 2021-11-12 to 2026-11-12 window; publication/version dates retained。
- 作者：Yanning Ji; Ruize Wang; Kalle Ngo; Elena Dubrova; Linus Backlund
- 对象：Kyber, FPGA, profiling, message recovery；类型：hardware_side_channel_attack。
- 核心想法：利用硬件消息处理泄漏和密文构造进行剖析式消息推断，讨论会话密钥导出。
- 作者报告：接受稿报告 200K 实际训练采集，经 cut-and-join 扩展为 6.4M；十个测试消息中分片方法给出字节排名及最多 2^64 枚举的估算。
- 限制与下一步：6.4M 不是独立实测条数；字节排名加枚举上界不证明已经执行该完整搜索；目标为消息/会话密钥，不是长期私钥。
- 阅读层级：selected_full_text_sections；来源：https://xplorestaging.ieee.org/document/10174000/。
- 已读章节：机构接受稿 PDF 第 1 页版本封面、第 2 页摘要/引言、第 5 页 §VI.C–VII 和第 6 页指定表格段落；非完整复现。
- [详细阅读记录](notes/masking-lineage-and-kyber-hardware-evidence-20261113.md)
- 代码/数据核查：not checked；引用追踪：pending。

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

## A Security RISC: Microarchitectural Attacks on Hardware RISC-V CPUs

- 来源：[SP 2023](https://doi.org/10.1109/sp46215.2023.10179399)；时间标记：within window; SP 2023 publication metadata。
- 作者：Lukas Gerlach; Daniel Weber; Ruiyi Zhang; Michael Schwarz
- 对象：RISC-V, cache, instruction retirement；类型：microarchitectural_side_channel。
- 核心想法：研究两种商用 64 位 RISC-V CPU 的微架构攻击面，提出缓存和指令退休相关观察方法。
- 作者报告：作者在 Linux 系统上给出六个案例，包括 KASLR 与内核活动观察。
- 限制与下一步：结论限所研究 CPU；不能将 ISA 名称当成全部实现的共同泄漏保证。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/10179399/。
- 代码/数据核查：not checked；引用追踪：pending。

## DBREACH: Stealing from Databases Using Compression Side-Channels

- 来源：[SP 2023](https://doi.org/10.1109/sp46215.2023.10179359)；时间标记：within window; SP 2023 publication metadata。
- 作者：Mathew Hogan; Yan Michalevsky; Saba Eskandarian
- 对象：database, compression, ciphertext length；类型：compression_side_channel。
- 核心想法：DBREACH 利用数据库压缩和静态加密共同留下的文件大小差异推断明文。
- 作者报告：作者在 MariaDB/MySQL InnoDB 与 MongoDB WiredTiger 上报告字符串存在性和内容提取。
- 限制与下一步：需间接访问和攻击载荷条件；近似文件大小、字符串检测和完整内容恢复是不同任务。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/10179359/。
- 代码/数据核查：not checked；引用追踪：pending。

## DVFS Frequently Leaks Secrets: Hertzbleed Attacks Beyond SIKE, Cryptography, and CPU-Only Data

- 来源：[SP 2023](https://doi.org/10.1109/sp46215.2023.10179326)；时间标记：inside rolling window。
- 作者：Yingchen Wang; Riccardo Paccagnella; Alan Wandke; Zhao Gang; Grant Garrett-Grossman; Christopher W. Fletcher; David Kohlbrenner; Hovav Shacham
- 对象：Classic McEliece, ECDSA, GPU/Chrome；类型：attack。
- 核心想法：将 DVFS 功耗—频率通道扩展到 SIKE 之外的密码与集成 GPU 场景。
- 作者报告：摘要报告结合实现中的已有片段与密码分析，攻击恒时 ECDSA、Classic McEliece，并利用 GPU/CPU 功率耦合做像素推断。
- 限制与下一步：待核对各平台、版本和采集预算；不扩展为当前所有 ECDSA/McEliece 或浏览器实现均受影响。
- 阅读层级：abstract_and_bibliographic_metadata；来源：author-institution abstract: https://experts.illinois.edu/en/publications/dvfs-frequently-leaks-secrets-hertzbleed-attacks-beyond-sike-cryp/。
- 代码/数据核查：not checked；引用追踪：forward citation observed; exhaustive backward/forward closure pending。

## DeHiREC: Detecting Hidden Voice Recorders via ADC Electromagnetic Radiation

- 来源：[SP 2023](https://doi.org/10.1109/sp46215.2023.10179480)；时间标记：within window; SP 2023 publication metadata。
- 作者：Ruochen Zhou; Xiaoyu Ji; Chen Yan; Yi-Chao Chen; Wenyuan Xu; Chaohao Li
- 对象：ADC, electromagnetic, active stimulation；类型：physical_side_channel_detection。
- 核心想法：DeHiREC 观察 ADC 的非故意 EM 辐射以发现离线隐藏录音设备。
- 作者报告：作者主动激励辐射并结合折叠信号处理，在 13 款录音设备上评估。
- 限制与下一步：包含主动刺激，不能写成纯被动扫描；设备存在性检测不等于录音内容恢复。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/10179480/。
- 代码/数据核查：not checked；引用追踪：pending。

## DevIOus: Device-Driven Side-Channel Attacks on the IOMMU

- 来源：[SP 2023](https://doi.org/10.1109/sp46215.2023.10179283)；时间标记：within window; SP 2023 publication metadata。
- 作者：Taehun Kim; Hyeongjin Park; Seokmin Lee; Seunghee Shin; Junbeom Hur; Youngjoo Shin
- 对象：IOMMU, IOTLB, DMA, RDMA；类型：microarchitectural_side_channel。
- 核心想法：DevIOus 通过 DMA 设备观察 IOMMU 地址转换缓存竞争。
- 作者报告：作者用 GPU 和 RDMA 网卡构造原语，讨论同机 VM 与 RDMA 远端场景。
- 限制与下一步：远端能力依赖 RDMA/设备条件；不等于任意互联网攻击，也不是 CPU 缓存通道。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/10179283/。
- 代码/数据核查：not checked；引用追踪：pending。

## Fashion Faux Pas: Implicit Stylistic Fingerprints for Bypassing Browsers' Anti-Fingerprinting Defenses

- 来源：[SP 2023](https://doi.org/10.1109/sp46215.2023.10179437)；时间标记：within window; SP 2023 publication metadata。
- 作者：Xu Lin; Frederico Araujo; Teryl Taylor; Jiyong Jang; Jason Polakis
- 对象：CSS, browser fingerprinting；类型：browser_side_channel。
- 核心想法：StylisticFP 通过 CSS 和 HTML 元素布局隐式推断设备特征。
- 作者报告：作者在隐私浏览器及扩展上评估，并与 JavaScript 指纹库比较。
- 限制与下一步：试点区分能力和特定浏览器防护绕过不等于跨所有版本持续跟踪成功。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/10179437/。
- 代码/数据核查：not checked；引用追踪：pending。

## From 5G Sniffing to Harvesting Leakages of Privacy-Preserving Messengers

- 来源：[SP 2023](https://doi.org/10.1109/sp46215.2023.10179353)；时间标记：within window; SP 2023 publication metadata。
- 作者：Norbert Ludant; Pieter Robyns; Guevara Noubir
- 对象：5G, traffic analysis, Signal, Telegram；类型：traffic_metadata_side_channel。
- 核心想法：把 5G 控制信道观察与消息服务可触发的流量联系起来，关联号码、临时标识和位置。
- 作者报告：作者报告实时控制信道嗅探与目标用户存在性推断。
- 限制与下一步：需要相应无线观察及目标流量触发条件；定位和流量元数据不是消息解密。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/10179353/。
- 代码/数据核查：not checked；引用追踪：pending。

## Half&Half: Demystifying Intel’s Directional Branch Predictors for Fast, Secure Partitioned Execution

- 来源：[SP 2023](https://xplorestaging.ieee.org/document/10179309/)；时间标记：within window; SP 2023 publication metadata。
- 作者：Hosein Yavarzadeh; Mohammadkazem Taram; Shravan Narayan; Deian Stefan; Dean Tullsen
- 对象：conditional branch predictor, domain isolation；类型：microarchitectural_countermeasure。
- 核心想法：Half&Half 从条件分支预测器结构出发，将两个保护域的影响分区。
- 作者报告：作者实现 LLVM 与 WebAssembly 编译器支持并比较防护开销。
- 限制与下一步：保证依赖所分析 Intel 结构和域划分；有两个相同书目/摘要的 DOI 记录，规范 DOI 待查。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/10179309/。
- 代码/数据核查：not checked；引用追踪：pending。

## Hide and Seek with Spectres: Efficient discovery of speculative vulnerabilities with random testing

- 来源：[SP 2023](https://doi.org/10.1109/sp46215.2023.10179391)；时间标记：within window; SP 2023 publication metadata。
- 作者：Oleksii Oleksenko; Marco Guarnieri; Boris Köpf; Mark Silberstein
- 对象：speculative leakage, random testing；类型：side_channel_discovery。
- 核心想法：通过改善随机测试效率扩大商用 CPU 的推测泄漏探索。
- 作者报告：作者在 Intel/AMD 发现与字符串比较和除法有关的两类泄漏。
- 限制与下一步：测试覆盖扩大不是穷尽证明；需核对实际版本和可利用性。录用与印刷题名存在变化。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/10179391/。
- 代码/数据核查：not checked；引用追踪：pending。

## High-Order Masking of Lattice Signatures in Quasilinear Time

- 来源：[SP 2023](https://doi.org/10.1109/sp46215.2023.10179342)；时间标记：within window; SP 2023 publication metadata。
- 作者：Rafaël del Pino; Thomas Prest; Mélissa Rossi; Markku-Juhani O. Saarinen
- 对象：Raccoon, lattice signatures, masking, randomness；类型：pqc_masking_design。
- 核心想法：Raccoon 从签名设计阶段移除昂贵掩码转换等瓶颈，使份额数开销为准线性。
- 作者报告：作者报告 probing 模型证明、C/FPGA 性能和两份额 FPGA 泄漏评估。
- 限制与下一步：C 性能代码使用测试用非密码随机数；所读 TVLA 仅 d=2、20 万轨迹，不证明所有高阶/物理观察安全。ROM 证明与 QROM 期待需区分。
- 阅读层级：selected_full_text_sections；来源：https://xplorestaging.ieee.org/document/10179342/。
- 已读章节：Publisher abstract; author PDF pp.3 and 14 (contributions/proof model, implementation and leakage assessment); selected bibliography [8,9,13,14,24] on p.15. Not full proof or artifact audit.
- [详细阅读记录](notes/sp2023-masking-speculation-observation-20261113.md)
- 代码/数据核查：URL read in author PDF; repository/archive not retrieved or executed；引用追踪：in_progress。

## Only Pay for What You Leak: Leveraging Sandboxes for a Minimally Invasive Browser Fingerprinting Defense

- 来源：[SP 2023](https://doi.org/10.1109/sp46215.2023.10179385)；时间标记：within window; SP 2023 publication metadata。
- 作者：Ryan Torok; Amit Levy
- 对象：browser fingerprinting, information flow；类型：browser_countermeasure。
- 核心想法：Sandcastle 通过沙箱及可控制的信息释放限制指纹向网络传出。
- 作者报告：摘要允许客户端使用标识信息，并设计不同释放粒度的机制。
- 限制与下一步：信息预算和隔离模型需正文核对；保护指定网络流不等于全部微架构观察均被覆盖。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/10179385/。
- 代码/数据核查：not checked；引用追踪：pending。

## Practical Timing Side-Channel Attacks on Memory Compression

- 来源：[SP 2023](https://doi.org/10.1109/sp46215.2023.10179297)；时间标记：within window; SP 2023 publication metadata。
- 作者：Martin Schwarzl; Pietro Borrello; Gururaj Saileshwar; Hanna Müller; Michael Schwarz; Daniel Gruss
- 对象：compression, timing, ZRAM, database；类型：compression_timing_side_channel。
- 核心想法：Decomp+Time 利用解压延迟而非只看压缩长度，结合载荷搜索增强可辨识差异。
- 作者报告：作者分别给出本地和远程数据库、ZRAM、浏览器案例。
- 限制与下一步：隐蔽信道容量与泄漏攻击吞吐不能混为一谈；本地/远端能力、载荷与噪声条件不同。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/10179297/。
- 代码/数据核查：not checked；引用追踪：pending。

## Privacy Leakage via Unrestricted Motion-Position Sensors in the Age of Virtual Reality: A Study of Snooping Typed Input on Virtual Keyboards

- 来源：[SP 2023](https://doi.org/10.1109/sp46215.2023.10179301)；时间标记：within window; SP 2023 publication metadata。
- 作者：Yi Wu; Cong Shi; Tianfang Zhang; Payton Walker; Jian Liu; Nitesh Saxena; Yingying Chen
- 对象：VR, motion sensors, keystrokes；类型：sensor_side_channel。
- 核心想法：从无需对应权限的 VR 运动/位置传感器数据推断虚拟键盘输入。
- 作者报告：作者以恶意应用和网站研究两个 VR 系统、四种键盘，模型不需要用户标注样本。
- 限制与下一步：无用户标签不代表完全无需训练或设置假设；密码、字符及段落识别指标不可互换。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/10179301/。
- 代码/数据核查：not checked；引用追踪：pending。

## Private Eye: On the Limits of Textual Screen Peeking via Eyeglass Reflections in Video Conferencing

- 来源：[SP 2023](https://doi.org/10.1109/sp46215.2023.10179423)；时间标记：within window; SP 2023 publication metadata。
- 作者：Yan Long; Chen Yan; Shilin Xiao; Shivan Prasad; Wenyuan Xu; Kevin Fu
- 对象：optical reflection, video, screen text；类型：physical_side_channel。
- 核心想法：通过眼镜反射和多帧处理研究视频会议中的屏幕信息泄漏极限。
- 作者报告：作者结合光学模型与受试者实验，分析字体大小、分辨率和网站识别。
- 限制与下一步：4K 推断与 720p 实验需分开；闭集网站识别不等于任意小字体正文恢复。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/10179423/。
- 代码/数据核查：not checked；引用追踪：pending。

## Rethinking Searchable Symmetric Encryption

- 来源：[SP 2023](https://doi.org/10.1109/sp46215.2023.10179460)；时间标记：within window; SP 2023 publication metadata。
- 作者：Zichen Gui; Kenneth G. Paterson; Sikhar Patranabis
- 对象：SSE, access patterns, document retrieval；类型：system_metadata_side_channel。
- 核心想法：重新审视可搜索加密的端到端泄漏，把文档取回纳入观察范围。
- 作者报告：作者报告即使搜索索引隐藏体积，整体系统仍可出现查询重建，并评价全系统防护成本。
- 限制与下一步：分析针对给定访问/辅助信息模型；不意味着全部 SSE 或所有加密数据库都已被攻破。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/10179460/。
- 代码/数据核查：not checked；引用追踪：pending。

## Robust Multi-tab Website Fingerprinting Attacks in the Wild

- 来源：[SP 2023](https://doi.org/10.1109/sp46215.2023.10179464)；时间标记：within window; SP 2023 publication metadata。
- 作者：Xinhao Deng; Qilei Yin; Zhuotao Liu; Xiyuan Zhao; Qi Li; Mingwei Xu; Ke Xu; Jianping Wu
- 对象：Tor, website fingerprinting, multi-tab；类型：traffic_side_channel。
- 核心想法：ARES 将多标签页网站指纹识别组织为多标签学习及局部流量特征问题。
- 作者报告：作者使用跨月数据评估 transformer 分类器及若干流量防护。
- 限制与下一步：F1、闭/开世界与标签页组成需统一比较；不能直接迁移为密码恢复能力。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/10179464/。
- 代码/数据核查：not checked；引用追踪：pending。

## SQUIP: Exploiting the Scheduler Queue Contention Side Channel

- 来源：[SP 2023](https://doi.org/10.1109/sp46215.2023.10179368)；时间标记：within window; SP 2023 publication metadata。
- 作者：Stefan Gast; Jonas Juffinger; Martin Schwarzl; Gururaj Saileshwar; Andreas Kogler; Simone Franza; Markus Köstl; Daniel Gruss
- 对象：scheduler queues, SMT, RSA；类型：microarchitectural_side_channel。
- 核心想法：SQUIP 通过调度队列竞争观察共核活动。
- 作者报告：作者报告逆向队列结构、隐蔽信道及 mbedTLS RSA 案例。
- 限制与下一步：对 Apple M1 的结构观察不等于在其上完成同样 SMT 攻击；轨迹、比特误差与最终密钥后处理需分开核对。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/10179368/。
- 代码/数据核查：not checked；引用追踪：pending。

## Scatter and Split Securely: Defeating Cache Contention and Occupancy Attacks

- 来源：[SP 2023](https://doi.org/10.1109/sp46215.2023.10179440)；时间标记：within window; SP 2023 publication metadata。
- 作者：Lukas Giner; Stefan Steinegger; Antoon Purnal; Maria Eichlseder; Thomas Unterluggauer; Stefan Mangard; Daniel Gruss
- 对象：cache randomization, eviction sets, SassCache；类型：microarchitectural_countermeasure。
- 核心想法：SassCache 通过带密钥映射和安全间距改变攻击者能形成的竞争关系。
- 作者报告：作者分析驱逐集构造并报告基准缓存命中率代价。
- 限制与下一步：摘要中的受保护地址比例和安全分析依赖指定模型；命中率变化不是直接运行时间开销。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/10179440/。
- 代码/数据核查：not checked；引用追踪：pending。

## Side Eye: Characterizing the Limits of POV Acoustic Eavesdropping from Smartphone Cameras with Rolling Shutters and Movable Lenses

- 来源：[SP 2023](https://doi.org/10.1109/sp46215.2023.10179313)；时间标记：within window; SP 2023 publication metadata。
- 作者：Yan Long; Pirouz Naghavi; Blas Kojusner; Kevin Butler; Sara Rampazzi; Kevin Fu
- 对象：rolling shutter, OIS, acoustic；类型：physical_side_channel。
- 核心想法：Side Eye 研究声音通过相机机械结构、滚动快门和镜片运动调制图像的通道。
- 作者报告：作者在十款手机上评价数字、说话者等识别任务。
- 限制与下一步：无需拍摄振动物体不等于没有结构声传播或相机访问前提；分类准确率不代表任意语音逐字重建。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/10179313/。
- 代码/数据核查：not checked；引用追踪：pending。

## SoK: A Critical Evaluation of Efficient Website Fingerprinting Defenses

- 来源：[SP 2023](https://doi.org/10.1109/sp46215.2023.10179289)；时间标记：within window; SP 2023 publication metadata。
- 作者：Nate Mathews; James K Holland; Se Eun Oh; Mohammad Saidur Rahman; Nicholas Hopper; Matthew Wright
- 对象：Tor, website fingerprinting, defense evaluation；类型：side_channel_defense_review。
- 核心想法：重新评价九种低开销网站指纹防护的效果和部署条件。
- 作者报告：作者使用较新深度学习攻击，并实现 DynaFlow 的实际 Tor 网络评估。
- 限制与下一步：九种防护的研究集和测试配置有限；论文重评不等于本项目已复现。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/10179289/。
- 代码/数据核查：not checked；引用追踪：pending。

## Spectre Declassified: Reading from the Right Place at the Wrong Time

- 来源：[SP 2023](https://doi.org/10.1109/sp46215.2023.10179355)；时间标记：within window; SP 2023 publication metadata。
- 作者：Basavesh Ammanaghatta Shivakumar; Jack Barnes; Gilles Barthe; Sunjay Cauligi; Chitchanok Chuengsatiansup; Daniel Genkin; Sioli O’Connell; Peter Schwabe; Rui Qi Sim; Yuval Yarom
- 对象：declassification, Spectre, AES, relative noninterference；类型：formal_and_experimental_side_channel。
- 核心想法：研究公开输出的去密化与推测执行交互，提出相对非干扰防护。
- 作者报告：作者报告 AES PoC 在 SLH 下仍有效，并在 FaCT 实现一种防护；selSLH 为初步性能估计。
- 限制与下一步：该篇未直接实现 selSLH，不能与后继 Jasmin 实现混算；模型内顺序泄漏上界不是所有物理通道的保证。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/10179355/。
- 代码/数据核查：not checked；引用追踪：pending。

## The Leaky Web: Automated Discovery of Cross-Site Information Leaks in Browsers and the Web

- 来源：[SP 2023](https://doi.org/10.1109/sp46215.2023.10179311)；时间标记：within window; SP 2023 publication metadata。
- 作者：Jannis Rautenstrauch; Giancarlo Pellegrino; Ben Stock
- 对象：XS-Leaks, browser observation；类型：side_channel_discovery。
- 核心想法：自动发现浏览器跨站状态观察通道并评价真实网站暴露。
- 作者报告：作者区分访问推断、cookie 接受及登录检测三种任务。
- 限制与下一步：三组网站样本和指标不同，不可把最高比例当作全部网站的共同漏洞率。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/10179311/。
- 代码/数据核查：not checked；引用追踪：pending。

## Typing High-Speed Cryptography against Spectre v1

- 来源：[SP 2023](https://doi.org/10.1109/sp46215.2023.10179418)；时间标记：within window; SP 2023 publication metadata。
- 作者：Basavesh Ammanaghatta Shivakumar; Gilles Barthe; Benjamin Gregoire; Vincent Laporte; Tiago Oliveira; Swarn Priya; Peter Schwabe; Lucas Tabary-Maujean
- 对象：Kyber, Jasmin, Spectre v1, speculative constant time；类型：pqc_formal_countermeasure。
- 核心想法：值相关信息流类型系统跟踪误推测状态，保护高性能密码实现。
- 作者报告：作者在 Jasmin 中改造包括 AVX2 Kyber768 的实现；模型观察分支与访存地址，攻击者控制预测及不安全访存。
- 限制与下一步：同地址空间应用 gadget 仍可泄密；Spectre v2/v4 等另需条件和缓解，且模型不含所有功耗/EM 观察。不是最终 ML-KEM 全部实现保证。
- 阅读层级：selected_full_text_sections；来源：https://xplorestaging.ieee.org/document/10179418/。
- 已读章节：Publisher abstract; author PDF pp.2–3 (limitations and threat model); p.13 comparison paragraph on declassification; selected bibliography [8,9,14,15] on p.14. Not full proof or artifact audit.
- [详细阅读记录](notes/sp2023-masking-speculation-observation-20261113.md)
- 代码/数据核查：URL read in author PDF; repository/archive not retrieved or executed；引用追踪：in_progress。

## Uncovering User Interactions on Smartphones via Contactless Wireless Charging Side Channels

- 来源：[SP 2023](https://doi.org/10.1109/sp46215.2023.10179322)；时间标记：within window; SP 2023 publication metadata。
- 作者：Tao Ni; Xiaokuan Zhang; Chaoshun Zuo; Jianfeng Li; Zhenyu Yan; Wubing Wang; Weitao Xu; Xiapu Luo; Qingchuan Zhao
- 对象：wireless charging, coil whine, magnetic field；类型：physical_side_channel。
- 核心想法：WISERS 联合线圈声音和磁场扰动构造手机交互上下文。
- 作者报告：作者使用商用手机和无线充电器评价界面切换、输入和应用活动推断。
- 限制与下一步：非接触不代表无需充电状态、近距离传感器或上下文模型；识别率限指定用户活动。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/10179322/。
- 代码/数据核查：not checked；引用追踪：pending。

## mmEcho: A mmWave-based Acoustic Eavesdropping Method

- 来源：[SP 2023](https://doi.org/10.1109/sp46215.2023.10179484)；时间标记：within window; SP 2023 publication metadata。
- 作者：Pengfei Hu; Wenhao Li; Riccardo Spolaor; Xiuzhen Cheng
- 对象：mmWave, acoustic vibration；类型：physical_side_channel。
- 核心想法：mmEcho 以毫米波测量声音引起的微小物体振动，重建音频。
- 作者报告：作者在移动声源、不同距离和隔音条件下评价。
- 限制与下一步：无线测振的激励与可见路径条件需正文核对；不能扩张为任意环境或无设备条件的窃听。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/10179484/。
- 代码/数据核查：not checked；引用追踪：pending。

## Side Channel Security Oriented Evaluation and Protection on Hardware Implementations of Kyber

- 来源：[TCAS-I 2023](https://doi.org/10.1109/tcsi.2023.3288600)；时间标记：within frozen 2021-11-12 to 2026-11-12 window; publication/version dates retained。
- 作者：Yiqiang Zhao; Shijian Pan; Haocheng Ma; Ya Gao; Xintong Song; Jiaji He; Yier Jin
- 对象：Kyber, FPGA, power analysis, electromagnetic, masking；类型：hardware_evaluation_and_countermeasure。
- 核心想法：比较 HDL/HLS、流水与并行 Kyber 硬件的功耗/EM 泄漏，并提出保护实现。
- 作者报告：作者评价 FPGA Kyber-768；Point 3 表 V 的局部 MTD 与正文整组密钥恢复预算不同，保护评估覆盖指定点和 10,000 条范围。
- 限制与下一步：保护对象为 IND-CPA 解密，正文明确 FO 变换未保护；LFSR 条件与有限一阶 CPA 结果不构成完整 CCA 实现或最终 ML-KEM 的通用保证。
- 阅读层级：selected_full_text_sections；来源：https://mahaocheng.me/assets/pdf/TCAS_2023_Kyber_SCA.pdf。
- 已读章节：作者 11 页稿 PDF 第 1 页摘要、第 3 页实现条件、第 6 页表 V 与恢复预算、第 8–9 页保护及评价范围；第 6 页已视觉核对。
- [详细阅读记录](notes/masking-lineage-and-kyber-hardware-evidence-20261113.md)
- 代码/数据核查：not checked；引用追踪：pending。

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
- 核心想法：修正早期 Dilithium 的敏感性分析，明确 y、z 的 DPA 保护与接受/拒绝尝试的区别。
- 作者报告：§3.4 撤回旧版仅需 SPA 的类比；随机化实现的显著性能收益使用直接 TRNG 份额采样，作者明确其不遵循当时 Dilithium 的规定采样路径。
- 限制与下一步：拒绝尝试 w1 不保护依赖额外 LWR 假设，另给保守保护选项；表 2 不含拒绝重复次数，不能当作最终签名时延或最终 ML-DSA 的安全保证。
- 阅读层级：selected_full_text_sections；来源：https://tches.iacr.org/index.php/TCHES/article/download/11158/10597。
- 已读章节：正式 22 页 PDF：第 6–8 页 §3.2–3.4、第 14 页 §5.2、第 17 页 §6.1 与表 2、第 19 页结论/代码入口、第 20–21 页 [ABC+22][MGTF19]；表 2 已视觉核对。
- [详细阅读记录](notes/masking-lineage-and-kyber-hardware-evidence-20261113.md)
- 代码/数据核查：paper links https://github.com/uclcrypto/pqm4_masked/tree/master ; contents not retrieved；引用追踪：in_progress; selected references only。

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

## Formally Verifying Kyber: Episode V: Machine-Checked IND-CCA Security and Correctness of ML-KEM in EasyCrypt

- 来源：[CRYPTO 2024](https://doi.org/10.1007/978-3-031-68379-4_12)；时间标记：within window; formal CRYPTO 2024 publication。
- 作者：José Bacelar Almeida; Santiago Arranz Olmos; Manuel Barbosa; Gilles Barthe; François Dupressoir; Benjamin Grégoire; Vincent Laporte; Jean-Christophe Léchenet; Cameron Low; Tiago Oliveira; Hugo Pacheco; Miguel Quaresma; Peter Schwabe; Pierre-Yves Strub
- 对象：ML-KEM, Kyber, Jasmin, constant time；类型：formal_pqc_security_and_constant_time。
- 核心想法：Episode V 将 ML-KEM 的密码学规范证明与两种 Jasmin 实现的功能等价和恒时性质连接起来。
- 作者报告：出版摘要明确 ROM 中 FO 变换和恒时实现；所读作者稿以 ML-KEM-768 给出具体实例，并借 Jasmin 类型系统限制分支、地址和变时运算。
- 限制与下一步：2024-05-29 作者稿明确针对草案和经典攻击者；不涵盖恒时模型以外的功耗/EM 泄漏。复杂度界人工分析，失败概率数字未全形式化；公钥验证及错误长度测试亦有限制。最终 FIPS 203 与作者修订差异待审计。
- 阅读层级：selected_full_text_sections；来源：https://link.springer.com/chapter/10.1007/978-3-031-68379-4_12。
- 已读章节：Publisher abstract; May 29 author PDF p.1 abstract, pp.2–3 contributions/limitations, pp.21–22 section 7 and footnote 26; selected bibliography [8] on p.23, [36–39] on p.24 and [55,57,58] on p.25; ePrint revision metadata. Not full proof/artifact audit.
- [详细阅读记录](notes/kyber-verification-episode-v-20261113.md)
- 代码/数据核查：not checked；引用追踪：in_progress。

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

## Masking the GLP Lattice-Based Signature Scheme at Any Order

- 来源：[Journal of Cryptology 2024](https://doi.org/10.1007/s00145-023-09485-z)；时间标记：within frozen 2021-11-12 to 2026-11-12 window; publication/version dates retained。
- 作者：Gilles Barthe; Sonia Belaïd; Thomas Espitau; Pierre-Alain Fouque; Benjamin Grégoire; Mélissa Rossi; Mehdi Tibouchi
- 对象：GLP, lattice signatures, masking；类型：countermeasure。
- 核心想法：GLP 任意阶掩码工作的期刊版本，保留公开输出和份额转换的模型条件。
- 作者报告：作者页面明确关联 EUROCRYPT 2018；期刊摘要报告形式模型与概念实现。
- 限制与下一步：在线日期为 2023-11-29，卷年为 2024；不能当成与 2018 版无关的新研究或已核验全文等价。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://link.springer.com/article/10.1007/s00145-023-09485-z。
- 代码/数据核查：not checked；引用追踪：in_progress; selected references only。

## Architectural Mimicry: Innovative Instructions to Efficiently Address Control-Flow Leakage in Data-Oblivious Programs

- 来源：[SP 2024](https://www.ieee-security.org/TC/SP2024/accepted-papers.html)；时间标记：formal SP 2024 publication within rolling window; conference/publication dates are distinct metadata。
- 作者：Hans Winderix; Marton Bognar; Job Noorman; Lesly-Ann Daniel; Frank Piessens
- 对象：control flow, RISC-V, data obliviousness；类型：hardware_supported_side_channel_countermeasure。
- 核心想法：AMi 以 mimic execution 执行可观察效果并抑制多数架构效果，为控制流平衡和线性化提供 ISA 支持。
- 作者报告：作者在 32 位乱序 RISC-V 核上研究分支预测、指令时序和数据缓存等控制流观察，并评估硬件开销与软件性能。
- 限制与下一步：低面积或关键路径开销不等于覆盖全部物理通道；需核查可观察效果定义、硬件模型及程序转换前提。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/10646702/。
- 代码/数据核查：not checked；引用追踪：pending。

## BULKOR: Enabling Bulk Loading for Path ORAM

- 来源：[SP 2024](https://www.ieee-security.org/TC/SP2024/accepted-papers.html)；时间标记：formal SP 2024 publication within rolling window; conference/publication dates are distinct metadata。
- 作者：Xiang Li; Yunqian Luo; Mingyu Gao
- 对象：ORAM, Path ORAM, TEE, access patterns；类型：access_pattern_countermeasure。
- 核心想法：BULKOR 改进 Path ORAM 的批量装载，同时处理不可信服务器中 TEE 的访问模式问题。
- 作者报告：摘要提出 doubly-oblivious 要求，并比较外存及内存配置下的复杂度和性能。
- 限制与下一步：数据访问模式保护不能直接扩展为功耗、瞬态执行或所有 TEE 侧信道保护；不同存储配置的性能不可混用。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/10646846/。
- 代码/数据核查：not checked；引用追踪：pending。

## BUSted!!! Microarchitectural Side-Channel Attacks on the MCU Bus Interconnect

- 来源：[SP 2024](https://www.ieee-security.org/TC/SP2024/accepted-papers.html)；时间标记：formal SP 2024 publication within rolling window; conference/publication dates are distinct metadata。
- 作者：Cristiano Rodrigues; Daniel Oliveira; Sandro Pinto
- 对象：MCU, TrustZone-M, DMA, bus arbitration；类型：microarchitectural_timing_side_channel。
- 核心想法：BUSted 利用 MCU 总线仲裁引起的时序差异，通过自主外设组合观察隔离域的活动。
- 作者报告：作者在 Armv8-M 与 TF-M 上报告攻击；所读模型假定攻击者控制一个隔离域及其外设和总线主设备，并知道受害代码。
- 限制与下一步：该模型还要求秘密相关控制流、共享物理存储 bank 及可请求受害执行；不能概括为任意恒时代码或全部 MCU 均已验证。物理故障攻击不在此模型内。
- 阅读层级：selected_full_text_sections；来源：https://xplorestaging.ieee.org/document/10646647/。
- 已读章节：Author PDF pp.2–3, attacker-model passage: isolated-domain/peripheral control, victim-code knowledge, secret-dependent flow, shared physical memory bank and excluded physical attacks.
- [详细阅读记录](notes/sp2024-physical-and-proof-boundaries-20261113.md)
- 代码/数据核查：not checked；引用追踪：pending。

## CONJUNCT: Learning Inductive Invariants to Prove Unbounded Instruction Safety Against Microarchitectural Timing Attacks

- 来源：[SP 2024](https://www.ieee-security.org/TC/SP2024/accepted-papers.html)；时间标记：formal SP 2024 publication within rolling window; conference/publication dates are distinct metadata。
- 作者：Sushant Dinesh; Madhusudan Parthasarathy; Christopher W. Fletcher
- 对象：RTL, RISC-V, constant time, inductive invariants；类型：formal_side_channel_verification。
- 核心想法：ConjunCT 从 RTL 学习归纳不变量，判断 ISA 指令在无界周期执行中的时序安全性。
- 作者报告：摘要描述条件信息流谓词、符号分析和不变量学习，在多个 RISC-V 微架构上提取 safe/unsafe 指令集合。
- 限制与下一步：无界指的是模型内执行长度，不是覆盖所有硬件实现或功耗/电磁观测；设计者注释、RTL 语义与传递器定义仍需正文核对。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/10646711/。
- 代码/数据核查：not checked；引用追踪：pending。

## DeepTheft: Stealing DNN Model Architectures through Power Side Channel

- 来源：[SP 2024](https://www.ieee-security.org/TC/SP2024/accepted-papers.html)；时间标记：formal SP 2024 publication within rolling window; conference/publication dates are distinct metadata。
- 作者：Yansong Gao; Huming Qiu; Zhi Zhang; Binghui Wang; Hua Ma; Alsharif Abuadbba; Minhui Xue; Anmin Fu; Surya Nepal
- 对象：DNN architecture, RAPL, CPU frequency；类型：power_and_frequency_side_channel。
- 核心想法：DeepTheft 从低采样率 RAPL 能量序列恢复 DNN 架构，并另研究 CPU 频率观察。
- 作者报告：作者说明所用 Docker 20.10.18 环境仍允许其取得 RAPL，而裸机无特权 RAPL 已受限；另对频率序列训练对应模型。
- 限制与下一步：权限结论限作者环境，不能当作当前所有容器均可访问；频率实验不是把 RAPL 模型不经训练直接迁移。架构识别不等于模型权重恢复。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/10646681/。
- 代码/数据核查：not checked；引用追踪：pending。

## Distributed & Scalable Oblivious Sorting and Shuffling

- 来源：[SP 2024](https://www.ieee-security.org/TC/SP2024/accepted-papers.html)；时间标记：formal SP 2024 publication within rolling window; conference/publication dates are distinct metadata。
- 作者：Nicholas Ngai; Ioannis Demertzis; Javad Ghareh Chamani; Dimitrios Papadopoulos
- 对象：ORAM, oblivious sorting, oblivious shuffling, multi-enclave；类型：access_pattern_countermeasure。
- 核心想法：在分布式多 enclave 环境中优化 oblivious 排序与打乱，减少数据局部性和网络开销造成的扩展瓶颈。
- 作者报告：作者分别提出多线程 bitonic sort、bucket sort 及其 shuffle 组件，并报告多种 enclave 数量下的比较。
- 限制与下一步：不同数据规模和 enclave 数不能只按一个加速倍数排序；oblivious 访问保证不自动包含全部物理与瞬态通道。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/10646804/。
- 代码/数据核查：not checked；引用追踪：pending。

## Don't Shoot the Messenger: Localization Prevention of Satellite Internet Users

- 来源：[SP 2024](https://www.ieee-security.org/TC/SP2024/accepted-papers.html)；时间标记：formal SP 2024 publication within rolling window; conference/publication dates are distinct metadata。
- 作者：David Koisser; Richard Mitev; Marco Chilese; Ahmad-Reza Sadeghi
- 对象：satellite Internet, RF localization, AnonSat；类型：location_metadata_countermeasure。
- 核心想法：AnonSat 通过本地长距离无线网络在卫星基站间转发流量，降低通信发射位置对用户位置的暴露。
- 作者报告：摘要报告原型实现，并以真实数据驱动的大规模网络仿真评价部署场景。
- 限制与下一步：定位隐私依赖基站分布、可转发范围及观察能力；原型和仿真不能合称所有场景实地验证，也不是通信内容加密的替代。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/10646696/。
- 代码/数据核查：not checked；引用追踪：pending。

## Efficient and Generic Microarchitectural Hash-Function Recovery

- 来源：[SP 2024](https://www.ieee-security.org/TC/SP2024/accepted-papers.html)；时间标记：formal SP 2024 publication within rolling window; conference/publication dates are distinct metadata。
- 作者：Lukas Gerlach; Simon Schwarz; Nicolas Faroß; Michael Schwarz
- 对象：CPU cache, hash function reverse engineering, Prime+Probe；类型：microarchitectural_mapping_and_side_channel。
- 核心想法：从侧信道提供的输入输出样本推断非线性微架构哈希函数，将逻辑化简与计算代数结合。
- 作者报告：作者报告 AMD/Intel 上三种此前未知函数，并通过已知函数复算和依赖映射的攻击评价方法。
- 限制与下一步：推断映射是攻击准备的一部分，不等于同样成本完成秘密恢复；需要核查样本取得权限、目标结构及跨处理器适用性。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/10646827/。
- 代码/数据核查：not checked；引用追踪：pending。

## GPU.zip: On the Side-Channel Implications of Hardware-Based Graphical Data Compression

- 来源：[SP 2024](https://www.ieee-security.org/TC/SP2024/accepted-papers.html)；时间标记：formal SP 2024 publication within rolling window; conference/publication dates are distinct metadata。
- 作者：Yingchen Wang; Riccardo Paccagnella; Zhao Gang; Willy R. Vasquez; David Kohlbrenner; Hovav Shacham; Christopher W. Fletcher
- 对象：GPU, graphical compression, browser, SVG；类型：compression_side_channel。
- 核心想法：GPU.zip 研究软件不可见的图形压缩如何形成数据相关 DRAM 流量和缓存使用。
- 作者报告：作者在 Intel/AMD 集成 GPU 上观察未显式请求的压缩，并展示浏览器跨源 SVG filter 像素窃取。
- 限制与下一步：软件透明压缩不等于任何 GPU 或浏览器都可利用；源隔离、攻击内容能力和设备支持需具体限定。像素泄漏不是直接解密。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/10646718/。
- 代码/数据核查：not checked；引用追踪：pending。

## Group Oblivious Message Retrieval

- 来源：[SP 2024](https://www.ieee-security.org/TC/SP2024/accepted-papers.html)；时间标记：formal SP 2024 publication within rolling window; conference/publication dates are distinct metadata。
- 作者：Zeyu Liu; Eran Tromer; Yunhao Wang
- 对象：recipient metadata, group messaging, FHE, GOMR；类型：metadata_privacy_protocol。
- 核心想法：GOMR 隐藏消息与接收者的关联，改进一条消息有多个接收者时的 oblivious retrieval 成本。
- 作者报告：作者使用 FHE 和格相关技术编码多个接收者线索，并给出协议形式化及实现比较。
- 限制与下一步：按通信元数据防护纳入一般侧信道范围；采用格技术并不等于研究 PQC 实现泄漏。协议隐私不自动覆盖端点物理观察或所有流量行为。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/10646845/。
- 代码/数据核查：not checked；引用追踪：pending。

## Injection Attacks Against End-to-End Encrypted Applications

- 来源：[SP 2024](https://www.ieee-security.org/TC/SP2024/accepted-papers.html)；时间标记：formal SP 2024 publication within rolling window; conference/publication dates are distinct metadata。
- 作者：Andrés Fábrega; Carolina Ortega Pérez; Armin Namavari; Ben Nassi; Rachit Agarwal; Thomas Ristenpart
- 对象：E2E encrypted backups, ciphertext length, chosen content；类型：ciphertext_length_side_channel。
- 核心想法：攻击者注入消息后观察加密备份长度，从密文的可见长度反推消息内容或元数据。
- 作者报告：摘要分别报告 WhatsApp 消息/附件案例及 Signal 联系人和会话数量线索。
- 限制与下一步：WhatsApp 场景假定可访问被攻陷云账号中的加密备份；Signal 场景同样要求取得备份。不能省略备份访问与注入能力，也不是攻破底层加密算法。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/10646849/。
- 代码/数据核查：not checked；引用追踪：pending。

## Leaky Address Masking: Exploiting Unmasked Spectre Gadgets with Noncanonical Address Translation

- 来源：[SP 2024](https://www.ieee-security.org/TC/SP2024/accepted-papers.html)；时间标记：formal SP 2024 publication within rolling window; conference/publication dates are distinct metadata。
- 作者：Mathé Hertogh; Sander Wiebing; Cristiano Giuffrida
- 对象：Spectre, LAM, UAI, TLB, SLAM；类型：transient_execution_side_channel。
- 核心想法：SLAM 利用地址高位忽略与非规范地址转换，将未掩码 Spectre gadget 转为秘密相关访问通道。
- 作者报告：正文模型是本地无特权进程对内核的攻击；附录审稿说明明确其端到端实验以软件模拟 LAM/UAI。
- 限制与下一步：不能把软件模拟的端到端演示写成当时尚未取得的新 CPU 实测。可达 gadget、地址转换及缓解配置均是前提；不外推至所有当前处理器。
- 阅读层级：selected_full_text_sections；来源：https://xplorestaging.ieee.org/document/10646870/。
- 已读章节：Author PDF p.3 section 3, local user-to-kernel threat model; p.16 Appendix A.4, software emulation of LAM/UAI in end-to-end experiments.
- [详细阅读记录](notes/sp2024-physical-and-proof-boundaries-20261113.md)
- 代码/数据核查：not checked；引用追踪：pending。

## Make Revocation Cheaper: Hardware-Based Revocable Attribute-Based Encryption

- 来源：[SP 2024](https://www.ieee-security.org/TC/SP2024/accepted-papers.html)；时间标记：formal SP 2024 publication within rolling window; conference/publication dates are distinct metadata。
- 作者：Xiaoguo Li; Guomin Yang; Tao Xiang; Shengmin Xu; Bowen Zhao; HweeHwa Pang; Robert H. Deng
- 对象：attribute-based encryption, TEE, key leakage；类型：leakage_resilient_protocol。
- 核心想法：HR-ABE 利用 TEE 处理属性加密撤销，并把 TEE 所持秘密可能泄漏纳入设计。
- 作者报告：作者声称在其构造和安全模型下，泄漏 TEE 的秘密不导致用户数据泄漏，并形式化证明和测量性能。
- 限制与下一步：摘要未给出全部泄漏能力和串谋边界；这是针对所定义泄漏的协议保证，不是 TEE 没有侧信道或任意密钥同时泄漏仍安全。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/10646706/。
- 代码/数据核查：not checked；引用追踪：pending。

## Obelix: Mitigating Side-Channels through Dynamic Obfuscation

- 来源：[SP 2024](https://www.ieee-security.org/TC/SP2024/accepted-papers.html)；时间标记：formal SP 2024 publication within rolling window; conference/publication dates are distinct metadata。
- 作者：Jan Wichelmann; Anja Rabich; Anna Pätschke; Thomas Eisenbarth
- 对象：TEE, ORAM, single stepping, code confidentiality；类型：system_side_channel_countermeasure。
- 核心想法：Obelix 将程序分为统一代码块并将代码和数据放入 ORAM，以缓解 TEE 的多种观察通道。
- 作者报告：摘要基于单步工具可达精度，讨论缓存、单步及密文侧信道，并说明存在较大性能开销。
- 限制与下一步：保护范围依赖攻击者精度、统一块性质和 ORAM 模型；不能据 holistic 名称宣称所有物理及未来攻击均被消除。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/10646762/。
- 代码/数据核查：not checked；引用追踪：pending。

## On (the Lack of) Code Confidentiality in Trusted Execution Environments

- 来源：[SP 2024](https://www.ieee-security.org/TC/SP2024/accepted-papers.html)；时间标记：formal SP 2024 publication within rolling window; conference/publication dates are distinct metadata。
- 作者：Ivan Puddu; Moritz Schneider; Daniele Lain; Stefano Boschetto; Srdjan Čapkun
- 对象：SGX, SEV, WASM, instruction extraction；类型：code_confidentiality_side_channel。
- 核心想法：研究 TEE 中原生执行与解释执行的代码保密性差异，指出运行时可能放大 IR 指令泄漏。
- 作者报告：作者评价 SGX/SEV 原生执行，并在 SGX 中对 WAMR、wasmi 上的 WASM 演示指令提取。
- 限制与下一步：原生代码较难提取不是通用零泄漏保证；完整 IR 提取案例与不同 TEE 的原生评价应分开，依赖观察和运行时条件。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/10646767/。
- 代码/数据核查：not checked；引用追踪：pending。

## Practical Obfuscation of BLE Physical-Layer Fingerprints on Mobile Devices

- 来源：[SP 2024](https://www.ieee-security.org/TC/SP2024/accepted-papers.html)；时间标记：formal SP 2024 publication within rolling window; conference/publication dates are distinct metadata。
- 作者：Hadi Givehchian; Nishant Bhaskar; Alexander Redding; Han Zhao; Aaron Schulman; Dinesh Bharadia
- 对象：BLE, RF fingerprints, device tracking；类型：physical_fingerprint_countermeasure。
- 核心想法：通过固件改变 BLE 射频硬件缺陷指纹，补充 MAC 地址随机化无法消除的物理标识。
- 作者报告：作者结合理论、仿真和现场评价，并在商用 BLE 芯片上实现防护。
- 限制与下一步：指定识别器和持续观察时间下攻击效果降低不等于不可链接性的通用证明；新的传感器、联合指纹和校准条件仍需检查。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/10646661/。
- 代码/数据核查：not checked；引用追踪：pending。

## Prune+PlumTree - Finding Eviction Sets at Scale

- 来源：[SP 2024](https://www.ieee-security.org/TC/SP2024/accepted-papers.html)；时间标记：formal SP 2024 publication within rolling window; conference/publication dates are distinct metadata。
- 作者：Tom Kessous; Niv Gilboa
- 对象：cache eviction sets, Prime+Probe, LRU；类型：side_channel_preprocessing。
- 核心想法：Prune+PlumTree 批量寻找大量缓存集合的驱逐集，并给出 LRU 与随机替换条件下的算法界。
- 作者报告：作者报告 Intel 实测及随机化缓存仿真，分别讨论不同替换策略的复杂度。
- 限制与下一步：真实硬件与随机化缓存仿真不能混合报告；LRU 下紧界不自动适用于全部替换策略。驱逐集构造耗时不是端到端密钥攻击耗时。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/10646765/。
- 代码/数据核查：not checked；引用追踪：pending。

## Real-Time Website Fingerprinting Defense via Traffic Cluster Anonymization

- 来源：[SP 2024](https://www.ieee-security.org/TC/SP2024/accepted-papers.html)；时间标记：formal SP 2024 publication within rolling window; conference/publication dates are distinct metadata。
- 作者：Meng Shen; Kexin Ji; Jinhe Wu; Qi Li; Xiangdong Kong; Ke Xu; Liehuang Zhu
- 对象：Tor, website fingerprinting, traffic shaping；类型：traffic_side_channel_countermeasure。
- 核心想法：Palette 通过流量聚类和统一形状隐藏同簇网站差异，提供实时网站指纹防护。
- 作者报告：作者使用公开数据评价，并将防护实现为 Tor 的 Pluggable Transport。
- 限制与下一步：识别准确率下降不等于所有观察者都无法区分；簇组成、站点外推、攻击者适配和实际带宽/等待开销待正文核对。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/10646653/。
- 代码/数据核查：not checked；引用追踪：pending。

## Rethinking IC Layout Vulnerability: Simulation-Based Hardware Trojan Threat Assessment with High Fidelity

- 来源：[SP 2024](https://www.ieee-security.org/TC/SP2024/accepted-papers.html)；时间标记：formal SP 2024 publication within rolling window; conference/publication dates are distinct metadata。
- 作者：Xinming Wei; Jiaxi Zhang; Guojie Luo
- 对象：hardware Trojans, IC layout, timing, power；类型：side_channel_based_trojan_assessment。
- 核心想法：SiliconCritic 用模拟植入前后的时序和功耗参数变化评价硬件木马可检测性。
- 作者报告：作者在 ASIC 设计和已报告木马上比较布局防护，指出纯几何指标忽略木马性质。
- 限制与下一步：按侧信道安全评估纳入；此处结果来自设计与仿真，不是已制造芯片上的秘密恢复或检测率。模型参数偏差与真实制造分布仍待核对。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/10646854/。
- 代码/数据核查：not checked；引用追踪：pending。

## Serberus: Protecting Cryptographic Code from Spectres at Compile-Time

- 来源：[SP 2024](https://www.ieee-security.org/TC/SP2024/accepted-papers.html)；时间标记：formal SP 2024 publication within rolling window; conference/publication dates are distinct metadata。
- 作者：Nicholas Mosier; Hamed Nemati; John C. Mitchell; Caroline Trippel
- 对象：constant time, Spectre, compiler, ASP；类型：formal_transient_execution_countermeasure。
- 核心想法：Serberus 将加强的恒时程序转换为满足抽象推测执行模型保证的代码。
- 作者报告：所读硬件模型依赖 CET、RRSBAD、DOIT 等条件，并选择禁用 PSF；软件处理其他列明推测原语。
- 限制与下一步：保证限符合 ASP 的处理器、CTS 程序及指定传递器，不是任意旧硬件上的全部瞬态/物理侧信道防护；DOIT 不等于功耗与操作数无关。
- 阅读层级：selected_full_text_sections；来源：https://xplorestaging.ieee.org/document/10646752/。
- 已读章节：Author PDF p.4 sections 2.3.1–2.3.2 and ASP introduction: CTS/ASP scope, CET, RRSBAD, DOIT, transmitters and disabled PSF. Not all proofs.
- [详细阅读记录](notes/sp2024-physical-and-proof-boundaries-20261113.md)
- 代码/数据核查：not checked；引用追踪：pending。

## Side-Channel-Assisted Reverse-Engineering of Encrypted DNN Hardware Accelerator IP and Attack Surface Exploration

- 来源：[SP 2024](https://www.ieee-security.org/TC/SP2024/accepted-papers.html)；时间标记：formal SP 2024 publication within rolling window; conference/publication dates are distinct metadata。
- 作者：Cheng Gongye; Yukui Luo; Xiaolin Xu; Yunsi Fei
- 对象：FPGA, DNN accelerator, EM, IP reverse engineering；类型：electromagnetic_side_channel。
- 核心想法：结合原理图分析与电磁观测，逆向商业 FPGA DNN 加速器 IP 的数据流及调度。
- 作者报告：作者以 AMD-Xilinx DPU 为例，并探索架构恢复及模型参数提取的后续攻击面。
- 限制与下一步：不是仅凭一段 EM 波形解密任意 bitstream；应核查设计资料、测量和查询能力以及各恢复任务的独立预算。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/10646839/。
- 代码/数据核查：not checked；引用追踪：pending。

## SoK: SGX.Fail: How Stuff Gets eXposed

- 来源：[SP 2024](https://www.ieee-security.org/TC/SP2024/accepted-papers.html)；时间标记：formal SP 2024 publication within rolling window; conference/publication dates are distinct metadata。
- 作者：Stephan Van Schaik; Alex Seto; Thomas Yurek; Adam Batori; Bader AlBassam; Daniel Genkin; Andrew Miller; Eyal Ronen; Yuval Yarom; Christina Garman
- 对象：SGX, microarchitectural attacks, patch lifecycle；类型：systematization_of_side_channel_security。
- 核心想法：SGX.Fail 分类不同 SGX 架构上的硬件攻击及其泄漏，并研究更新机制在实际部署中的效果。
- 作者报告：摘要讨论 SECRET network 与 PowerDVD 两个案例，以及补丁时序和人工更新的部署取舍。
- 限制与下一步：架构代际、补丁与应用状态是结论边界；不能将历史部署失效直接套到所有当前 SGX 配置。综述分类与案例实测应分别引用。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/10646750/。
- 代码/数据核查：not checked；引用追踪：pending。

## Sticky Tags: Efficient and Deterministic Spatial Memory Error Mitigation using Persistent Memory Tags

- 来源：[SP 2024](https://www.ieee-security.org/TC/SP2024/accepted-papers.html)；时间标记：formal SP 2024 publication within rolling window; conference/publication dates are distinct metadata。
- 作者：Floris Gorter; Taddeus Kroes; Herbert Bos; Cristiano Giuffrida
- 对象：MTE, memory tags, speculative probing；类型：side_channel_analysis_and_memory_safety_defense。
- 核心想法：StickyTags 的动机包含用推测探测推断随机内存标签，并提出不依赖标签保密性的确定性布局防护。
- 作者报告：摘要以按对象大小分区和持久标签减少重标记开销，讨论有界空间内存错误。
- 限制与下一步：纳入依据是随机标签的推测泄漏；有界空间保护不等于覆盖全部越界、时间内存错误或全部 Spectre。案例 CVE 覆盖率不是完整漏洞检出率。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/10646704/。
- 代码/数据核查：not checked；引用追踪：pending。

## TCP Spoofing: Reliable Payload Transmission Past the Spoofed TCP Handshake

- 来源：[SP 2024](https://www.ieee-security.org/TC/SP2024/accepted-papers.html)；时间标记：formal SP 2024 publication within rolling window; conference/publication dates are distinct metadata。
- 作者：Yepeng Pan; Christian Rossow
- 对象：TCP, ISN, feedback channels, spoofing；类型：network_protocol_side_channel。
- 核心想法：通过协议和应用反馈推断服务器初始序列号，使伪造 TCP 连接上的后续负载传输更可靠。
- 作者报告：作者区分暴力发送和反馈引导方式，后者涉及 SYN cookies、邮件与数据库相关反馈。
- 限制与下一步：反馈观察条件、源 IP 伪造和服务端窗口行为需要同时成立；不得把暴力猜测、直接响应与间接反馈的成本混为一项。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/10646838/。
- 代码/数据核查：not checked；引用追踪：pending。

## UnTrustZone: Systematic Accelerated Aging to Expose On-chip Secrets

- 来源：[SP 2024](https://www.ieee-security.org/TC/SP2024/accepted-papers.html)；时间标记：formal SP 2024 publication within rolling window; conference/publication dates are distinct metadata。
- 作者：Jubayer Mahmod; Matthew Hicks
- 对象：SRAM, TrustZone, data remanence, device aging；类型：physical_data_remanence_attack。
- 核心想法：UnTrustZone 研究 SRAM 数据相关老化如何留下模拟域记忆，并从上电状态读出残留。
- 作者报告：作者通过主动加速老化展示 TrustZone AES、固件与缓存数据案例；正文要求可读未被污染的 SRAM 上电状态及加速条件。
- 限制与下一步：这是需要物理接触、应力和持留状态的主动残留攻击，不是被动正常工作功耗读出。高位正确率不能无条件等同全密钥正确恢复，也不证明短时动态 NTT 有同样效果。
- 阅读层级：selected_full_text_sections；来源：https://xplorestaging.ieee.org/document/10646649/。
- 已读章节：Author PDF p.5 section 4 and Figure 4: uncontaminated SRAM power-on state, accelerated aging and physical power-delivery access; project page overview also read.
- [详细阅读记录](notes/sp2024-physical-and-proof-boundaries-20261113.md)
- 代码/数据核查：not checked；引用追踪：pending。

## Video-Based Cryptanalysis: Extracting Cryptographic Keys from Video Footage of a Device's Power LED Captured By Standard Video Cameras

- 来源：[SP 2024](https://www.ieee-security.org/TC/SP2024/accepted-papers.html)；时间标记：formal SP 2024 publication within rolling window; conference/publication dates are distinct metadata。
- 作者：Ben Nassi; Etay Iluz; Or Cohen; Ofek Vayner; Dudi Nassi; Boris Zadov; Yuval Elovici
- 对象：SIKE, ECDSA, power LED, rolling shutter；类型：optical_power_and_timing_side_channel。
- 核心想法：通过功耗相关 LED 亮度与相机滚动快门取得时序观察，演示 ECDSA 和历史 SIKE 实现案例。
- 作者报告：摘要区分远处智能卡读卡器 LED 与同 USB hub 外设 LED 的手机案例；作者项目页说明沿用 Minerva/Hertzbleed 类脆弱实现。
- 限制与下一步：需要可利用的实现泄漏、LED 耦合和足够成像条件；填满画面的 LED 与普通任意录像不同。SIKE 案例不能代表最终 ML-KEM；两种传感与距离条件不能互换。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/10646886/。
- 已读章节：complete publisher abstract and bibliographic metadata; author project-page FAQ on vulnerable implementations, LED coupling and image framing
- 代码/数据核查：not checked；引用追踪：pending。

## mimoCrypt: Multi-User Privacy-Preserving Wi-Fi Sensing via MIMO Encryption

- 来源：[SP 2024](https://www.ieee-security.org/TC/SP2024/accepted-papers.html)；时间标记：formal SP 2024 publication within rolling window; conference/publication dates are distinct metadata。
- 作者：Jun Luo; Hangcheng Cao; Hongbo Jiang; Yanbing Yang; Zhe Chen
- 对象：Wi-Fi sensing, MIMO, human activity privacy；类型：physical_sensing_countermeasure。
- 核心想法：mimoCrypt 用 MIMO 操作改变 Wi-Fi 信道的可观察性，支持合法用户感知并抑制非授权活动推断。
- 作者报告：作者将人体活动称为物理明文，联合优化隐私、感知和通信质量，并在 SDR 上评价手势场景。
- 限制与下一步：物理加密的名称不自动提供标准密码学语义安全；密钥交付、传感器能力及多用户配置需要限定，手势场景不能直接推广至全部环境。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/10646878/。
- 代码/数据核查：not checked；引用追踪：pending。

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

## A side-channel attack on a masked hardware implementation of CRYSTALS-Kyber

- 来源：[Journal of Cryptographic Engineering 2025](https://doi.org/10.1007/s13389-025-00375-7)；时间标记：within frozen 2021-11-12 to 2026-11-12 window; publication/version dates retained。
- 作者：Yanning Ji; Elena Dubrova
- 对象：Kyber, masked FPGA, deep learning, message recovery；类型：hardware_side_channel_attack_and_countermeasure。
- 核心想法：同一掩码硬件攻击研究的期刊记录，摘要还涉及封装过程与对策。
- 作者报告：摘要报告消息解码 HD 泄漏、重复解封装提升共享密钥恢复，并分析封装及保护措施。
- 限制与下一步：与 ASHES 2023 有显式书目关联，但逐项版本增量和实验差异未审计；保留两个出版记录，不计成两个独立攻击发现。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://link.springer.com/article/10.1007/s13389-025-00375-7。
- 代码/数据核查：not checked；引用追踪：pending。

## BPSniff: Continuously Surveilling Private Blood Pressure Information in the Metaverse via Unrestricted Inbuilt Motion Sensors

- 来源：[SP 2025](https://www.ieee-security.org/TC/SP2025/accepted-papers.html#collapse-81)；时间标记：formal publication within rolling window; publisher-deposited date。
- 作者：Zhengkun Ye; Ahmed Tanvir Mahdad; Yan Wang; Cong Shi; Yingying Chen; Nitesh Saxena
- 对象：VR motion sensors, blood pressure, cross-modal inference；类型：sensor_side_channel。
- 核心想法：利用 VR 头显运动传感器中的血流振动线索推断血压，属于非密码目标的物理隐私通道。
- 作者报告：摘要报告以 VAE 重构血流再用 LSTM 估计，研究涉及 37 名参与者、两种头显及八周观测。
- 限制与下一步：无需个人专属校准不等于无需训练；作者的测量误差比较不能写成临床有效性或监管批准。设备、活动和人群外推待正文核对。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://www.winlab.rutgers.edu/~yychen/papers/BPSniff.pdf。
- 代码/数据核查：not checked；引用追踪：pending。

## BadRAM: Practical Memory Aliasing Attacks on Trusted Execution Environments

- 来源：[SP 2025](https://www.ieee-security.org/TC/SP2025/accepted-papers.html#collapse-39)；时间标记：formal publication within rolling window; publisher-deposited date。
- 作者：Jesse De Meulemeester; Luca Wilke; David Oswald; Thomas Eisenbarth; Ingrid Verbauwhede; Jo Van Bulck
- 对象：TEE, classic SGX, SEV-SNP, memory aliasing；类型：physical_memory_attack_and_write_pattern_leakage。
- 核心想法：通过 DRAM 地址别名破坏 TEE 的物理内存假设；其中 classic SGX 案例涉及细粒度写入模式泄漏。
- 作者报告：作者区分 SEV-SNP 的完整性/证明攻击与 classic SGX 的写模式通道，并报告所研究 scalable SGX、TDX 的别名检测阻止该攻击。
- 限制与下一步：所读威胁模型以一次 SPD 操作为前提；论文提到未写保护模块的软件修改可能性，但不能概括为所有平台纯软件攻击。不同 TEE 的结果不能互换；没有本地复现。
- 阅读层级：selected_full_text_sections；来源：https://vanbulck.net/files/oakland25-badram.pdf。
- 已读章节：Author PDF p.4: attacker-model paragraphs on one-time SPD modification and possible unprotected modules; abstract on p.1. Not the complete security analysis.
- [详细阅读记录](notes/sp2025-observation-and-proof-scopes-20261113.md)
- 代码/数据核查：not checked；引用追踪：pending。

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

## CountMamba: A Generalized Website Fingerprinting Attack via Coarse-Grained Representation and Fine-Grained Prediction

- 来源：[SP 2025](https://www.ieee-security.org/TC/SP2025/accepted-papers.html#collapse-250)；时间标记：formal publication within rolling window; publisher-deposited date。
- 作者：Xianwen Deng; Ruijie Zhao; Yanhao Wang; Mingwei Zhan; Zhi Xue; Yijun Wang
- 对象：Tor, website fingerprinting, traffic metadata；类型：traffic_side_channel。
- 核心想法：CountMamba 用窗口流量计数及增量序列预测进行早期和多标签网站指纹识别。
- 作者报告：作者利用包大小、方向和时序，报告跨多种场景的识别及对适度扰动的稳定性，并给出代码数据仓库入口。
- 限制与下一步：流量指纹不等于解密内容；训练和目标站点范围、填充防护及跨会话划分待全文核对。仓库链接可见未代表材料已检查或可运行。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/11023397/。
- 代码/数据核查：author abstract links https://github.com/SJTU-dxw/CountMamba-WF; contents and execution not checked；引用追踪：pending。

## EUCLEAK

- 来源：[SP 2025](https://www.ieee-security.org/TC/SP2025/accepted-papers.html#collapse-239)；时间标记：conference year 2025 within frozen window; exact publication date not verified。
- 作者：Thomas Roche NinjaLab
- 对象：ECDSA, modular inversion, Infineon secure elements, FIDO；类型：attack。
- 核心想法：通过安全元件的非恒时模逆研究 ECDSA 泄漏，并使用本地电磁观测演示密钥恢复。
- 作者报告：作者 2024 技术报告摘要描述 Feitian A22 上的分析、YubiKey 5Ci 演示以及若干 Infineon 产品的适用性。
- 限制与下一步：本次读的是 2024-10-22 技术报告的封面、修订表与摘要，不是 2025 会议版全文；需要物理访问与相应仪器。版本/产品边界不能扩展成当前所有产品均受影响。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://ninjalab.io/wp-content/uploads/2024/10/20241022_eucleak.pdf。
- 代码/数据核查：not checked; author technical report only；引用追踪：pending。

## EveGuard: Defeating Vibration-based Side-Channel Eavesdropping with Audio Adversarial Perturbations

- 来源：[SP 2025](https://www.ieee-security.org/TC/SP2025/accepted-papers.html#collapse-136)；时间标记：formal publication within rolling window; publisher-deposited date。
- 作者：Jung-Woo Chang; Ke Sun; David Xia; Xinyu Zhang; Farinaz Koushanfar
- 对象：vibration eavesdropping, audio perturbation；类型：physical_side_channel_countermeasure。
- 核心想法：EveGuard 利用声音对空气压力与物体振动的不同作用，通过音频扰动干扰振动窃听。
- 作者报告：摘要描述物理引导扰动、EveGAN 传感器转换和少样本适配，并报告用户感知质量及若干自适应攻击评估。
- 限制与下一步：特定识别任务中的防护成绩不是信息论零泄漏；新传感器、采样条件及更强适应性仍需验证，不能把音质指标替代保密指标。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xyzhang.ucsd.edu/papers/Jung-Woo.Chang_SP25_EveGuard.pdf。
- 代码/数据核查：not checked；引用追踪：pending。

## Eyes on Your Typing: Snooping Finger Motions on Virtual Keyboards

- 来源：[SP 2025](https://www.ieee-security.org/TC/SP2025/accepted-papers.html#collapse-106)；时间标记：formal publication within rolling window; publisher-deposited date。
- 作者：Sunwoo Lee; Wonsuk Choi
- 对象：AR/VR, head motion, virtual keyboard；类型：sensor_side_channel。
- 核心想法：SNOOPFINGER 从无需额外权限的头部运动推断手指在虚拟键盘上的输入。
- 作者报告：摘要报告跨模态推断不依赖控制器，在 24 名参与者上取得词与句子层面的识别结果。
- 限制与下一步：不需要大量事先头动数据不等于零训练；词/句子指标不能视为密码恢复率，设备与语言外推未核查。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://pure.korea.ac.kr/en/publications/eyes-on-your-typing-snooping-finger-motions-on-virtual-keyboards/。
- 代码/数据核查：not checked；引用追踪：pending。

## Half Spectre, Full Exploit: Hardening Rowhammer Attacks with Half Spectre Gadgets

- 来源：[SP 2025](https://www.ieee-security.org/TC/SP2025/accepted-papers.html#collapse-174)；时间标记：formal publication within rolling window; publisher-deposited date。
- 作者：Andrea Di Dio; Mathé Hertogh; Cristiano Giuffrida
- 对象：half-Spectre, PRELOAD+TIME, Rowhammer；类型：microarchitectural_side_channel_enabling_fault_attack。
- 核心想法：Half-Spectre 将不能直接披露载入值的推测执行片段用于物理访存活动观测，并辅助定向 Rowhammer。
- 作者报告：作者提出 PRELOAD+TIME 缓存行粒度原语，随后以 ProbeHammer 降低误伤；威胁模型是本地无特权用户进程。
- 限制与下一步：依赖可由系统调用到达的内核 gadget 与物理内存 direct map。时序原语与后续故障利用需分开；不可把特定构造的可靠性推广到所有 CPU、内核和 DIMM。
- 阅读层级：selected_full_text_sections；来源：https://download.vusec.net/papers/halfspectre_sp25.pdf。
- 已读章节：Author PDF p.3, section 3: local unprivileged attacker, reachable kernel gadget and direct-map prerequisites; abstract on p.1.
- [详细阅读记录](notes/sp2025-observation-and-proof-scopes-20261113.md)
- 代码/数据核查：not checked；引用追踪：pending。

## I Know What You Sync: Covert and Side Channel Attacks on File Systems via syncfs

- 来源：[SP 2025](https://www.ieee-security.org/TC/SP2025/accepted-papers.html#collapse-158)；时间标记：formal publication within rolling window; publisher-deposited date。
- 作者：Cheng Gu; Yicheng Zhang; Nael Abu-Ghazaleh
- 对象：syncfs, file systems, containers, Linux, Android；类型：shared_resource_timing_side_channel。
- 核心想法：共享文件系统的刷盘行为使 syncfs 耗时暴露其他隔离域的 I/O 活动。
- 作者报告：作者分别报告 Linux/Windows 隐蔽通道，以及 Linux 网站/视频和 Android 应用识别案例。
- 限制与下一步：共谋隐蔽通道带宽与非共谋指纹攻击是不同指标；需核查共享文件系统、权限及后台负载条件。所读为作者预印本，未证明与正式版逐字等价。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://arxiv.org/abs/2411.10883。
- 代码/数据核查：not checked；引用追踪：pending。

## IncognitOS: A Practical Unikernel Design for Full-System Obfuscation in Confidential Virtual Machines

- 来源：[SP 2025](https://www.ieee-security.org/TC/SP2025/accepted-papers.html#collapse-127)；时间标记：formal publication within rolling window; publisher-deposited date。
- 作者：Kha Dinh Duy; Jaeyoon Kim; Hajeong Lim; Hojoon Lee
- 对象：AMD SEV-SNP, CVM, VMExit, obfuscation；类型：system_side_channel_countermeasure。
- 核心想法：IncognitOS 通过可信自调用调度及基于 VMExit 速率的自适应重随机化缓解机密虚拟机的侧信道。
- 作者报告：正文将恶意 hypervisor 纳入攻击方，将 CPU、整个 CVM 和本系统组件纳入 TCB，并使用同步 ticks 与页级机制。
- 限制与下一步：威胁模型明确不考虑瞬态执行攻击；不能将 full-system 名称理解为覆盖全部物理与微架构通道。仍需核查攻击速率假设和各配置开销。
- 阅读层级：selected_full_text_sections；来源：https://kha-dinh.github.io/assets/pdf/incognitos.pdf。
- 已读章节：Author PDF p.3 section 2.4 through p.4 opening: TCB and exclusion of transient execution; p.4 section 3.1 overview; abstract on p.1.
- [详细阅读记录](notes/sp2025-observation-and-proof-scopes-20261113.md)
- 代码/数据核查：not checked；引用追踪：pending。

## Mind the Location Leakage in LEO Direct-to-Cell Satellite Networks

- 来源：[SP 2025](https://www.ieee-security.org/TC/SP2025/accepted-papers.html#collapse-108)；时间标记：formal publication within rolling window; publisher-deposited date。
- 作者：Weisen Liu; Zeqi Lai; Qian Wu; Hewu Li; Yuxuan Weng; Wei Liu; Qi Zhang; Jihao Li; Yuanjie Li; Jun Liu
- 对象：LEO satellites, direct-to-cell, location metadata；类型：protocol_metadata_location_leakage。
- 核心想法：DCATOR 联合卫星广播信令中的位置线索与随时间变化的轨道，分析直连手机用户的位置隐私。
- 作者报告：摘要分别讨论运行中的 Iridium、开发中的 Starlink DTC 和基于 3GPP NTN 的系统，并报告部分条件下百米量级跟踪。
- 限制与下一步：三种系统的实际采集、建模和标准分析证据不能合并成全部网络实测；依赖持续接收广播及覆盖条件，不是解密用户通信。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/11023341/。
- 代码/数据核查：not checked；引用追踪：pending。

## Mixnets on a tightrope: Quantifying the leakage of mix networks using a provably optimal heuristic adversary

- 来源：[SP 2025](https://www.ieee-security.org/TC/SP2025/accepted-papers.html#collapse-180)；时间标记：formal publication within rolling window; publisher-deposited date。
- 作者：Sebastian Meiser; Debajyoti Das; Moritz Kirschte; Esfandiar Mohammadi; Aniket Kate
- 对象：mixnets, recipient anonymity, privacy loss；类型：traffic_leakage_model_and_evaluation。
- 核心想法：从拓扑与路由分析低延迟 mixnet 的收件人匿名性，以隐私损失分布描述稀有但强的信息暴露。
- 作者报告：作者给出模型内最优攻击策略，并通过采样和隐私损失尾部估计攻击优势下界，研究 Karaoke 与 Atom 的设计选择。
- 限制与下一步：下界不是安全上界；最优性受模型、匿名性定义和观察能力限制，采样误差与真实部署偏离需分别处理。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://research.uni-luebeck.de/de/publications/mixnets-on-a-tightrope-quantifying-the-leakage-of-mix-networks-us/。
- 代码/数据核查：not checked；引用追踪：pending。

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

## Rapid Reversing of Non-Linear CPU Cache Slice Functions: Unlocking Physical Address Leakage

- 来源：[SP 2025](https://www.ieee-security.org/TC/SP2025/accepted-papers.html#collapse-143)；时间标记：formal publication within rolling window; publisher-deposited date。
- 作者：Mikka Rainer; Lorenz Hetterich; Fabian Thomas; Tristan Hornetz; Leon Trampert; Lukas Gerlach; Michael Schwarz
- 对象：CPU cache slice, physical address, Spectre, DRAMA；类型：microarchitectural_mapping_and_side_channel。
- 核心想法：研究非线性 LLC 切片函数的逆向，并将其用于虚拟到物理地址关联及侧信道准备。
- 作者报告：摘要报告逆向 13 个切片函数，并在 Spectre、DRAMA 和驱逐集构造中展示应用。
- 限制与下一步：运行时无特权地址 oracle 不代表离线校准和整条逆向流程无特权；逆向耗时不能当作完整密钥恢复成本。具体硬件和访问条件待正文核查。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://fabianthomas.de/pdfs/rainer2025rapid.pdf。
- 代码/数据核查：not checked；引用追踪：pending。

## SCAD: Towards a Universal and Automated Network Side-Channel Vulnerability Detection

- 来源：[SP 2025](https://www.ieee-security.org/TC/SP2025/accepted-papers.html#collapse-24)；时间标记：formal publication within rolling window; publisher-deposited date。
- 作者：Keyu Man; Zhongjie Wang; Yu Hao; Shenghan Zheng; Xin'an Zhou; Yue Cao; Zhiyun Qian
- 对象：network side channels, non-interference, symbolic execution, TCP, UDP, ICMP；类型：automated_side_channel_detection。
- 核心想法：SCAD 以跨执行的非干扰违例寻找网络协议共享状态泄漏，结合选择性符号执行与路径对分析。
- 作者报告：所读正文要求人工标注秘密、响应可观察量和分析范围；针对可伪造源 IP 的离路径攻击，作者报告 14 个真阳性、其中 7 个此前未知。
- 限制与下一步：允许任意符号状态与不正确具体化会产生不可达状态误报；范围过窄会漏报。检测到模型违例不自动证明实际可利用性、穷尽覆盖或任何随机化下的统计泄漏。
- 阅读层级：selected_full_text_sections；来源：https://www.cs.ucr.edu/~zhiyunq/pub/oakland25_SCAD.pdf。
- 已读章节：Author PDF p.3 sections 3.1–3.2; p.8 sections 5.2–5.4; pp.13–14 section 9 and conclusion: annotations, analysis scope, unreachable states and concretization; abstract on p.1.
- [详细阅读记录](notes/sp2025-observation-and-proof-scopes-20261113.md)
- 代码/数据核查：not checked；引用追踪：pending。

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

## Sniffing Location Privacy of Video Conference Users Using Free Audio Channels

- 来源：[SP 2025](https://www.ieee-security.org/TC/SP2025/accepted-papers.html#collapse-192)；时间标记：formal publication within rolling window; publisher-deposited date。
- 作者：Long Huang; Chen Wang
- 对象：video conferencing, active acoustic sensing, location inference；类型：active_acoustic_privacy_side_channel。
- 核心想法：通过视频会议合法双向音频的回声探测周围环境，并从残余声学响应推断地点或场景。
- 作者报告：摘要区分会内构造探测声和第三方媒体声两类主动感知，并用学习模型处理回声消除后的失真。
- 限制与下一步：关闭摄像头或使用虚拟背景不等于麦克风静音；不能据引言措辞宣称关闭音频输入仍可攻击。地点分类不是精确地理坐标，需核查参考数据和参与者能力。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/11023324/。
- 代码/数据核查：not checked；引用追踪：pending。

## Sparta: Practical Anonymity with Long-Term Resistance to Traffic Analysis

- 来源：[SP 2025](https://www.ieee-security.org/TC/SP2025/accepted-papers.html#collapse-103)；时间标记：formal publication within rolling window; publisher-deposited date。
- 作者：Kyle Fredrickson; Ioannis Demertzis; James P. Hughes; Darrell D.E. Long
- 对象：metadata-private messaging, traffic analysis, deferred retrieval；类型：traffic_analysis_countermeasure。
- 核心想法：Sparta 用延迟取回模型组织元数据私密通信，以减少长期发送与接收流量的关联。
- 作者报告：作者给出不同延迟/吞吐场景的三种构造；所读正文要求用户不按实际收到的流量决定取回，并区分处理、用户等待和服务端等待延迟。
- 限制与下一步：低系统处理延迟不能替代端到端等待；比较图中的数据库大小并不统一。用户行为、定长填充与重加密是模型条件，不能概括为任意通信行为均匿名。
- 阅读层级：selected_full_text_sections；来源：https://idemertzis.com/Papers/sp2025_sparta.pdf。
- 已读章节：Author PDF p.4: Figure 1 caption, latency components and section 3.1 communication-state model; abstract on p.1.
- [详细阅读记录](notes/sp2025-observation-and-proof-scopes-20261113.md)
- 代码/数据核查：not checked；引用追踪：pending。

## Spoofing Eavesdroppers with Audio Misinformation

- 来源：[SP 2025](https://www.ieee-security.org/TC/SP2025/accepted-papers.html#collapse-199)；时间标记：formal publication within rolling window; publisher-deposited date。
- 作者：Zhambyl Shaikhanov; Mahmoud Al-Madi; Hou-Tong Chen; Chun-Chieh Chang; Sadhvikas Addamane; Daniel M. Mittleman; Edward Knightly
- 对象：mmWave vibration sensing, metasurface, audio misinformation；类型：physical_side_channel_countermeasure。
- 核心想法：MiSINFO 通过可重构超表面改变毫米波振动读出，尝试让窃听者接收到合成的错误语音。
- 作者报告：作者报告在其装置和识别条件下抑制原始内容并提高合成内容的可理解度；作用点是物理测量路径。
- 限制与下一步：特定误词率或欺骗效果不保证对所有传感器、距离和自适应检测有效；与音频输入扰动是不同干预，不能只按一个防护百分比排序。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://bpb-us-e1.wpmucdn.com/blogs.rice.edu/dist/d/12661/files/2025/03/MiSINFO-Camera_Ready.pdf。
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

## Your Cable, My Antenna: Eavesdropping Serial Communication via Backscatter Signals

- 来源：[SP 2025](https://www.ieee-security.org/TC/SP2025/accepted-papers.html#collapse-157)；时间标记：formal publication within rolling window; publisher-deposited date。
- 作者：Lina Pu; Yu Luo; Song Han; Junming Diao
- 对象：serial communication, backscatter, impedance, EM；类型：backscatter_side_channel。
- 核心想法：BTC 利用串口位状态对应的阻抗变化调制回散信号，由电缆的非预期天线作用泄漏串行通信。
- 作者报告：摘要报告视距与穿墙条件的实验，并另外以全波模型分析线长、载波与可行性。
- 限制与下一步：摘要未完整说明入射载波的产生与访问条件，不能直接写成纯被动辐射窃听。4 cm 线长的实验与 1 cm 的模拟结论需分开；不改设备不等于没有外部射频条件。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/11023318/。
- 代码/数据核查：not checked；引用追踪：pending。

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

## A Statistical Side-Channel Risk Model for Timing Variability in Lattice-Based Post-Quantum Cryptography

- 来源：[arXiv 2025](https://arxiv.org/abs/2512.22301)；时间标记：within frozen 2021-11-12 to 2026-11-12 window; publication/version dates retained。
- 作者：Aayush Mainali; Sirjan Ghimire
- 对象：Kyber, Saber, Frodo, timing, synthetic traces；类型：synthetic_risk_model。
- 核心想法：用合成时序轨迹和场景噪声比较统计可分辨性，组合多种统计量形成风险分数。
- 作者报告：摘要研究 idle、jitter、loaded 条件，比较 Welch、KS、Cliff、互信息及分布重叠。
- 限制与下一步：算法家族差异来自设定的泄漏模型与合成数据，不是实际恒时实现测量或三种 KEM 的风险排名；需平台验证。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://arxiv.org/abs/2512.22301。
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

## Side-Channel Attack Prevention for Post Quantum Cryptography Algorithms: A 3D-Shield Approach

- 来源：[arXiv 2026](https://arxiv.org/abs/2611.01144)；时间标记：within frozen 2021-11-12 to 2026-11-12 window; publication/version dates retained。
- 作者：Carl Benda; Eren Kurshan; Aydin Aysu; Paul Franzon
- 对象：Kyber, NTT, 3D integration, decoy computation；类型：simulated_countermeasure。
- 核心想法：提出堆叠保护层与诱饵计算；数值评估在 Kyber NTT 的软件 HW 功耗代理中进行。
- 作者报告：作者模型演示公开旋转因子的 CPA 排名转移及指定 TVLA 阈值结果；PDF 明示物理 FPGA 实现为后续工作。
- 限制与下一步：不是实测 3D 芯片或秘密密钥恢复；有限软件 TVLA 通过不能证明通用安全。arXiv comments 列 IEEE 3DIC 2026，正式论文集/DOI 尚未独立核定。
- 阅读层级：selected_full_text_sections；来源：https://arxiv.org/abs/2611.01144。
- 已读章节：arXiv v1 摘要；六页 PDF 第 4 页 §IV、第 5 页限定说明/结论及选读参考 [2][3][4][7][9][10]；第 4–5 页已视觉核对。
- [详细阅读记录](notes/masking-lineage-and-kyber-hardware-evidence-20261113.md)
- 代码/数据核查：not checked；引用追踪：in_progress; selected references only。
