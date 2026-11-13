# 已阅读论文卡片

状态：持续整理，尚未覆盖全部相关论文。按每篇实际阅读层级报告；作者报告不等于本地复现。

当前 506 篇；按 DOI 或官方页面关联目录，边界论文继续保留。

## Timing Attacks on Implementations of Diffie-Hellman, RSA, DSS, and Other Systems

- 来源：[CRYPTO 1996](https://doi.org/10.1007/3-540-68697-5_9)；时间标记：pre-window foundational reference。
- 作者：Paul C. Kocher
- 对象：RSA, Diffie-Hellman, DSS, timing；类型：timing attack。
- 核心想法：建立私钥运算耗时与秘密推断的基础研究入口。
- 作者报告：摘要说明准确计时条件下对固定 DH 指数、RSA 等对象的风险，并讨论部分防护。
- 限制与下一步：1996 年基础文献；摘要中的潜在网络应用不等于任意现代实现可远程利用，未读全部算法与实测。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://link.springer.com/chapter/10.1007/3-540-68697-5_9。
- [详细阅读记录](notes/masking-foundations-gaussian-timing-and-falcon-20261114.md)
- 代码/数据核查：no author code or data executed; artifact completeness not inspected；引用追踪：pending except selected verified Gaussian follow-up。

## Differential Power Analysis

- 来源：[CRYPTO 1999](https://doi.org/10.1007/3-540-48405-1_25)；时间标记：outside rolling five-year window; cited foundation。
- 作者：Paul Kocher; Joshua Jaffe; Benjamin Jun
- 对象：DPA, power analysis；类型：foundational_attack。
- 核心想法：研究从设备功耗统计中提取秘密的差分分析方法及防护思路。
- 作者报告：作者讨论具有物理信息泄漏的密码设备。
- 限制与下一步：仅摘要与元数据；CRYPTO 1999 基础来源，不作为本地复现或后量子实测证据。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://link.springer.com/chapter/10.1007/3-540-48405-1_25。
- [详细阅读记录](notes/mpcith-revisions-and-evidence-20261113.md)
- 代码/数据核查：not inspected; no author code executed；引用追踪：pending except explicitly linked references。

## Towards Sound Approaches to Counteract Power-Analysis Attacks

- 来源：[CRYPTO 1999](https://doi.org/10.1007/3-540-48405-1_26)；时间标记：outside rolling five-year window; cited foundation。
- 作者：Suresh Chari; Charanjit S. Jutla; Josyula R. Rao; Pankaj Rohatgi
- 对象：masking, power model；类型：formal_countermeasure。
- 核心想法：在指定物理功耗模型内建立随机化实现与统计攻击实验量下界。
- 作者报告：作者提出满足模型性质且有随机源时的通用防护方法。
- 限制与下一步：证明与下界依赖功耗模型及随机性假设，不是所有物理观察下的普遍安全；仅摘要，窗口外基础来源。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://link.springer.com/chapter/10.1007/3-540-48405-1_26。
- [详细阅读记录](notes/pqc-citation-followups-and-evidence-20261113.md)
- 代码/数据核查：no author code or data executed; artifact contents not inspected；引用追踪：pending except explicitly inventoried citations。

## Private Circuits: Securing Hardware against Probing Attacks

- 来源：[CRYPTO 2003](https://doi.org/10.1007/978-3-540-45146-4_27)；时间标记：outside rolling five-year window; cited foundation。
- 作者：Yuval Ishai; Amit Sahai; David Wagner
- 对象：probing security, private circuits；类型：formal_countermeasure。
- 核心想法：为有限数量电路线探测建立形式化威胁模型并构造私有电路。
- 作者报告：作者提出效率构造和安全证明，作为后续掩码工作的理论基础。
- 限制与下一步：有限线探测模型不是对所有模拟功耗与 EM 观察的无条件保证；正文证明未复核。CRYPTO 2003 窗口外基础文献。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://link.springer.com/chapter/10.1007/978-3-540-45146-4_27。
- [详细阅读记录](notes/mpcith-revisions-and-evidence-20261113.md)
- 代码/数据核查：not inspected; no author code executed；引用追踪：pending except explicitly linked references。

## Provably Secure Higher-Order Masking of AES

- 来源：[CHES 2010](https://doi.org/10.1007/978-3-642-15031-9_28)；时间标记：outside rolling five-year window; cited foundation。
- 作者：Matthieu Rivain; Emmanuel Prouff
- 对象：AES, higher-order masking；类型：formal_countermeasure。
- 核心想法：构造基于 ISW 思路、可软件实现的通用高阶 AES 掩码。
- 作者报告：作者给出阶数参数化构造、安全论证与软件开销讨论。
- 限制与下一步：仅摘要；安全阶数和复杂度结论受论文模型限定，不能推广成所有真实物理攻击的指数复杂度下界。CHES 2010 窗口外基础来源。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://link.springer.com/chapter/10.1007/978-3-642-15031-9_28。
- [详细阅读记录](notes/pqc-citation-followups-and-evidence-20261113.md)
- 代码/数据核查：no author code or data executed; artifact contents not inspected；引用追踪：pending except explicitly inventoried citations。

## Building power analysis resistant implementations of Keccak

- 来源：[SHA-3 Candidate Conference 2010](https://keccak.team/files/KeccakDPA.pdf)；时间标记：outside rolling five-year window; cited foundation。
- 作者：Guido Bertoni; Joan Daemen; Michaël Peeters; Gilles Van Assche
- 对象：Keccak, masking；类型：countermeasure。
- 核心想法：利用 Keccak 步函数的代数结构设计软件和硬件掩码。
- 作者报告：第一页提出软件两份额、硬件三份额的条件性讨论以及两种架构的面积吞吐权衡。
- 限制与下一步：只阅读第一页摘要与引言；没有核查后续证明及模拟章节，不能把历史份额数表述升级为通用物理安全保证。作者页面提示已有更近的实现概述。
- 阅读层级：selected_full_text_sections；来源：https://keccak.team/files/KeccakDPA.pdf; https://keccak.team/papers.html。
- 已读章节：Author PDF page 1: abstract and introduction only; later construction, proofs and simulation sections unread.
- [详细阅读记录](notes/mpcith-revisions-and-evidence-20261113.md)
- 代码/数据核查：not inspected; no author code executed；引用追踪：pending except explicitly linked references。

## A testing methodology for side-channel resistance validation

- 来源：[NIST NIAT Workshop 2011](https://csrc.nist.gov/CSRC/media/Events/Non-Invasive-Attack-Testing-Workshop/documents/08_Goodwill.pdf)；时间标记：outside rolling five-year window; cited foundation。
- 作者：Gilbert Goodwill; Benjamin Jun; Josh Jaffe; Pankaj Rohatgi
- 对象：TVLA, Welch t-test, AES；类型：leakage_detection。
- 核心想法：提出以统计差异检测敏感中间量影响的侧信道测试流程。
- 作者报告：介绍指定 AES 测试及三种实现的作者评估，失败判据不要求完整密钥恢复。
- 限制与下一步：只读前两页；原文明确测试不能保证抵抗所有攻击。这是 NIST 工作坊论文，不能称作正式 NIST 标准。
- 阅读层级：selected_full_text_sections；来源：https://csrc.nist.gov/CSRC/media/Events/Non-Invasive-Attack-Testing-Workshop/documents/08_Goodwill.pdf; https://csrc.nist.gov/Events/2011/Non-Invasive-Attack-Testing-Workshop。
- 已读章节：NIST-hosted workshop PDF pages 1-2: introduction and opening testing-methodology/vendor-information requirements; experimental sections unread.
- [详细阅读记录](notes/mpcith-revisions-and-evidence-20261113.md)
- 代码/数据核查：not inspected; no author code executed；引用追踪：pending except explicitly linked references。

## An architecture-independent instruction shuffler to protect against side-channel attacks

- 来源：[TACO 2012](https://doi.org/10.1145/2086696.2086699)；时间标记：outside rolling five-year window; cited foundation。
- 作者：Ali Galip Bayrak; Nikola Velickovic; Paolo Ienne; Wayne Burleson
- 对象：AES, instruction shuffling；类型：countermeasure。
- 核心想法：在 CPU 与指令缓存/存储器之间加入架构独立的随机指令打乱单元。
- 作者报告：摘要报告 OpenRISC 与 MicroBlaze FPGA 上的 AES 评估：约 2% 面积、1.5% 功耗开销及攻击工作量超过 360 倍。
- 限制与下一步：数值属于作者指定平台和攻击，不是所有处理器的安全倍数；2012 年窗口外通用基础文献。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://api.crossref.org/works/10.1145/2086696.2086699。
- [详细阅读记录](notes/kyber-shuffle-followups-and-evidence-20261113.md)
- 代码/数据核查：not inspected; no author code executed；引用追踪：pending except explicitly linked references。

## On the Cost of Lazy Engineering for Masked Software Implementations

- 来源：[CARDIS 2014](https://doi.org/10.1007/978-3-319-16763-3_5)；时间标记：pre-window foundational reference。
- 作者：Josep Balasch; Benedikt Gierlichs; Vincent Grosso; Oscar Reparaz; François-Xavier Standaert
- 对象：masking, transition leakage, compiler；类型：leakage model and evaluation。
- 核心想法：量化从中间值泄漏模型转到转换泄漏模型时的掩码保证损失。
- 作者报告：摘要给出安全阶数折半的模型归约，并报告两款微控制器上的手写/编译汇编及随机性复用比较。
- 限制与下一步：CARDIS 举办年为 2014，章节出版为 2015；折半结果带有模型与实现条件，不能视为所有掩码必然失效。仅摘要，平台细节未读。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://link.springer.com/chapter/10.1007/978-3-319-16763-3_5。
- [详细阅读记录](notes/masking-foundations-gaussian-timing-and-falcon-20261114.md)
- 代码/数据核查：no author code or data executed; artifact completeness not inspected；引用追踪：pending except selected verified Gaussian follow-up。

## Secure Conversion between Boolean and Arithmetic Masking of Any Order

- 来源：[CHES 2014](https://doi.org/10.1007/978-3-662-44709-3_11)；时间标记：pre-window foundational reference。
- 作者：Jean-Sébastien Coron; Johann Großschädl; Praveen Kumar Vadnala
- 对象：B2A, A2B, HMAC-SHA-1, ISW；类型：masking conversion。
- 核心想法：提出任意阶布尔与算术掩码双向转换。
- 作者报告：摘要给出两方向 O(n²k) 复杂度与 ISW 框架证明，并报告 32 位 AVR 上 HMAC-SHA-1 周期。
- 限制与下一步：窗口外基础文献；复杂度变量 n 为阶数、k 为位宽。模型证明与周期评估不能自动推出功耗实测无泄漏。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://link.springer.com/chapter/10.1007/978-3-662-44709-3_11。
- [详细阅读记录](notes/masking-foundations-gaussian-timing-and-falcon-20261114.md)
- 代码/数据核查：no author code or data executed; artifact completeness not inspected；引用追踪：pending except selected verified Gaussian follow-up。

## Conversion from Arithmetic to Boolean Masking with Logarithmic Complexity

- 来源：[FSE 2015](https://doi.org/10.1007/978-3-662-48116-5_7)；时间标记：pre-window foundational reference。
- 作者：Jean-Sébastien Coron; Johann Großschädl; Mehdi Tibouchi; Praveen Kumar Vadnala
- 对象：A2B, Kogge-Stone, Boolean addition；类型：masking conversion。
- 核心想法：用 Kogge-Stone 进位结构将 A2B 及布尔份额加法的位宽复杂度改为对数级。
- 作者报告：摘要证明一阶保护，报告 k=64 时相对 Goubin 算法约 23% 提升。
- 限制与下一步：本篇摘要的证明范围是一阶，不能因被高阶采样论文引用就标为任意阶转换。窗口外，仅摘要。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://link.springer.com/chapter/10.1007/978-3-662-48116-5_7。
- [详细阅读记录](notes/masking-foundations-gaussian-timing-and-falcon-20261114.md)
- 代码/数据核查：no author code or data executed; artifact completeness not inspected；引用追踪：pending except selected verified Gaussian follow-up。

## Strong Non-Interference and Type-Directed Higher-Order Masking

- 来源：[CCS 2016](https://doi.org/10.1145/2976749.2978427)；时间标记：outside rolling five-year window; cited foundation。
- 作者：Gilles Barthe; Sonia Belaïd; François Dupressoir; Pierre-Alain Fouque; Benjamin Grégoire; Pierre-Yves Strub; Rébecca Zucchini
- 对象：masking, SNI, formal verification；类型：formal_countermeasure。
- 核心想法：用强非干扰与类型系统支持掩码算法的组合安全论证和自动验证。
- 作者报告：扩展版摘要报告可扩展的方法及超出此前规模的例子。
- 限制与下一步：实际阅读为作者明确说明经过大幅重写的扩展版摘要；原会议证明和版本差异未核查。逻辑探测保证不等于任意聚合功耗安全。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://eprint.iacr.org/2015/506; https://api.crossref.org/works/10.1145/2976749.2978427。
- [详细阅读记录](notes/mpcith-revisions-and-evidence-20261113.md)
- 代码/数据核查：not inspected; no author code executed；引用追踪：pending except explicitly linked references。

## Flush, Gauss, and Reload – A Cache Attack on the BLISS Lattice-Based Signature Scheme

- 来源：[CHES 2016](https://doi.org/10.1007/978-3-662-53140-2_16)；时间标记：pre-window foundational reference。
- 作者：Leon Groot Bruinderink; Andreas Hülsing; Tanja Lange; Yuval Yarom
- 对象：BLISS, Flush+Reload, Gaussian sampler；类型：attack。
- 核心想法：从离散 Gaussian 采样器的缓存访问获得辅助信息并恢复 BLISS 密钥。
- 作者报告：正式摘要分别报告理想侧信道 450 签名与真实 Flush+Reload 概念验证不足 3500 签名；理想情形成功率 0.96。
- 限制与下一步：450 与不足 3500 属于不同观察模型，不能只取较小值作为实测预算；摘要为两款 CPU 的证据，不是功耗波形测量。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://link.springer.com/chapter/10.1007/978-3-662-53140-2_16。
- [详细阅读记录](notes/masking-foundations-gaussian-timing-and-falcon-20261114.md)
- 代码/数据核查：no author code or data executed; artifact completeness not inspected；引用追踪：pending except selected verified Gaussian follow-up。

## Domain-Oriented Masking: Compact Masked Hardware Implementations with Arbitrary Protection Order

- 来源：[TIS 2016](https://doi.org/10.1145/2996366.2996426)；时间标记：pre-window foundational reference。
- 作者：Hannes Gross; Stefan Mangard; Thomas Korak
- 对象：DOM, AES, threshold implementations；类型：hardware masking。
- 核心想法：提出 domain-oriented masking 的硬件组织方法；此记录对应 mUOV 实际引用的 TIS 摘要。
- 作者报告：机构摘要报告 AES 综合至第 15 保护阶、至第二保护阶的 t-test 评估，以及一阶每 S-box 18 随机位。
- 限制与下一步：会议摘要报告约 6 kGE，而 ePrint 摘要为 7.1 kGE；不合并面积数字。高阶综合不等于相同阶数物理验证，机构摘要有重复段落。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://tugraz.elsevierpure.com/en/publications/domain-oriented-masking-compact-masked-hardware-implementations-w/。
- [详细阅读记录](notes/masking-foundations-gaussian-timing-and-falcon-20261114.md)
- 代码/数据核查：no author code or data executed; artifact completeness not inspected；引用追踪：pending except selected verified Gaussian follow-up。

## Towards Sound and Optimal Leakage Detection Procedure

- 来源：[CARDIS 2017](https://doi.org/10.1007/978-3-319-75208-2_7)；时间标记：outside rolling five-year window; cited foundation。
- 作者：A. Adam Ding; Liwei Zhang; Francois Durvaux; Francois-Xavier Standaert; Yunsi Fei
- 对象：TVLA, Higher Criticism；类型：leakage_detection。
- 核心想法：将泄漏检测与最小 p 值聚合联系，并引入 Higher Criticism 检测多位置的弱信号。
- 作者报告：作者报告特定统计设置的可检测性结果及数值比较。
- 限制与下一步：最优性依赖论文模型，不是所有泄漏分布下的普遍结论；检出不等于密钥恢复，未检出不等于安全。CARDIS 2017 与 2018 出版分开。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://link.springer.com/chapter/10.1007/978-3-319-75208-2_7。
- [详细阅读记录](notes/mpcith-revisions-and-evidence-20261113.md)
- 代码/数据核查：not inspected; no author code executed；引用追踪：pending except explicitly linked references。

## Jasmin: High-Assurance and High-Speed Cryptography

- 来源：[CCS 2017](https://doi.org/10.1145/3133956.3134078)；时间标记：outside rolling window; cited foundation retained。
- 作者：José Bacelar Almeida; Manuel Barbosa; Gilles Barthe; Arthur Blot; Benjamin Grégoire; Vincent Laporte; Tiago Oliveira; Hugo Pacheco; Benedikt Schmidt; Pierre-Yves Strub
- 对象：Jasmin, constant-time, verified compiler；类型：formal_verification_and_implementation。
- 核心想法：以专用语言和经过证明的编译方法兼顾高保证密码实现与性能。
- 作者报告：机构摘要报告 Coq 编译器证明、内存安全及恒时分析和 x64 性能比较。
- 限制与下一步：恒时与功能证明有指定观察模型；不能将 2017 工作解释为覆盖后来 Spectre 或物理功耗的一般保证。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://researchportal.ip-paris.fr/en/publications/jasmin-high-assurance-and-high-speed-cryptography/。
- 代码/数据核查：not checked；引用追踪：pending。

## Side-Channel Attacks on BLISS Lattice-Based Signatures: Exploiting Branch Tracing against strongSwan and Electromagnetic Emanations in Microcontrollers

- 来源：[CCS 2017](https://doi.org/10.1145/3133956.3134028)；时间标记：pre-window foundational reference。
- 作者：Thomas Espitau; Pierre-Alain Fouque; Benoît Gérard; Mehdi Tibouchi
- 对象：BLISS, strongSwan, branch tracing, EMA, rejection sampling；类型：attack。
- 核心想法：分别利用拒绝采样、Gaussian 采样和稀疏乘法泄漏分析 BLISS。
- 作者报告：摘要报告相对范数路线的因子分解条件、strongSwan 单次执行分支跟踪恢复，以及 AVR 单条 EMA 的整数规划路线。
- 限制与下一步：三条路线的访问能力与密钥条件不能混合；相对范数路线只覆盖满足条件的密钥。历史 BLISS 不等于当前标准化方案。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://eprint.iacr.org/2017/505。
- [详细阅读记录](notes/masking-foundations-gaussian-timing-and-falcon-20261114.md)
- 代码/数据核查：no author code or data executed; artifact completeness not inspected；引用追踪：pending except selected verified Gaussian follow-up。

## To BLISS-B or not to be: Attacking strongSwan's Implementation of Post-Quantum Signatures

- 来源：[CCS 2017](https://doi.org/10.1145/3133956.3134023)；时间标记：pre-window foundational reference。
- 作者：Peter Pessl; Leon Groot Bruinderink; Yuval Yarom
- 对象：BLISS-B, strongSwan, cache, LPN；类型：attack。
- 核心想法：推进 BLISS/BLISS-B 密钥恢复，并在 strongSwan 上研究异步缓存观测。
- 作者报告：作者摘要报告综合 LPN、整数规划、似然与格约简的恢复流程，约观察 6000 次签名生成。
- 限制与下一步：明确区分前作概念验证与本作生产实现；6000 为摘要报告，完整测量/后处理成本未审。历史软件版本不自动适用于当前部署。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://eprint.iacr.org/2017/490。
- [详细阅读记录](notes/masking-foundations-gaussian-timing-and-falcon-20261114.md)
- 代码/数据核查：no author code or data executed; artifact completeness not inspected；引用追踪：pending except selected verified Gaussian follow-up。

## High-Order Conversion from Boolean to Arithmetic Masking

- 来源：[CHES 2017](https://doi.org/10.1007/978-3-319-66787-4_5)；时间标记：pre-window foundational reference。
- 作者：Jean-Sébastien Coron
- 对象：B2A, ISW, Hutter-Tunstall；类型：masking conversion and cryptanalysis。
- 核心想法：给出复杂度不依赖寄存器位宽的高阶 B2A，并分析旧转换算法。
- 作者报告：作者摘要报告小阶数性能提升，并给出针对 Hutter-Tunstall 三阶算法的三阶攻击及 t≥4 算法的四阶攻击。
- 限制与下一步：攻击对象是特定 Hutter-Tunstall 构造，不是对所有高阶转换的否定；仅读正式摘要，未审完整证明。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://link.springer.com/chapter/10.1007/978-3-319-66787-4_5。
- [详细阅读记录](notes/masking-foundations-gaussian-timing-and-falcon-20261114.md)
- 代码/数据核查：no author code or data executed; artifact completeness not inspected；引用追踪：pending except selected verified Gaussian follow-up。

## Single-Trace Side-Channel Attacks on Masked Lattice-Based Encryption

- 来源：[CHES 2017](https://doi.org/10.1007/978-3-319-66787-4_25)；时间标记：outside rolling window; explicitly cited foundational work。
- 作者：Robert Primas; Peter Pessl; Stefan Mangard
- 对象：lattice encryption, NTT, masking, belief propagation；类型：pqc_single_trace_side_channel。
- 核心想法：将 NTT 模运算的模板匹配、信念传播与格译码组合，研究掩码格加密的一条攻击轨迹恢复。
- 作者报告：作者同时报告通用噪声 HW 模型及 ARM Cortex-M4F 实测轨迹上的恢复。
- 限制与下一步：这是 CHES 2017 的窗口外基础工作；single trace 指攻击观察，不代表没有模板训练、设备或校准成本。掩码阶数、实现及算法迁移范围待全文核对，不能扩展为全部最终 PQC 标准。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://link.springer.com/chapter/10.1007/978-3-319-66787-4_25。
- 代码/数据核查：not checked；引用追踪：pending。

## Higher-Order Side-Channel Protected Implementations of KECCAK

- 来源：[DSD 2017](https://doi.org/10.1109/dsd.2017.21)；时间标记：outside rolling five-year window; cited foundation。
- 作者：Hannes Gross; David Schaffenrath; Stefan Mangard
- 对象：Keccak, masking；类型：countermeasure。
- 核心想法：设计可通过参数调整保护阶数的 Keccak 硬件。
- 作者报告：作者修订摘要报告四种 Keccak 变体及最高九阶配置。
- 限制与下一步：配置阶数与所有物理攻击抵抗力不同；具体探测/毛刺模型和实验预算待全文。ePrint 明示为 DSD 2017 的小修订，未核对全文差异。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://eprint.iacr.org/2017/395; https://api.crossref.org/works/10.1109/dsd.2017.21。
- [详细阅读记录](notes/mpcith-revisions-and-evidence-20261113.md)
- 代码/数据核查：not inspected; no author code executed；引用追踪：pending except explicitly linked references。

## Measuring Information Leakage in Website Fingerprinting Attacks and Defenses

- 来源：[CCS 2018](https://doi.org/10.1145/3243734.3243832)；时间标记：pre-window foundational reference。
- 作者：Shuai Li; Huajun Guo; Nicholas Hopper
- 对象：Tor, website fingerprinting, information leakage；类型：evaluation。
- 核心想法：为网站指纹特征与防护构造信息泄漏量的分析方法。
- 作者报告：作者机构摘要报告对多类特征、网站和防护进行信息量评估。
- 限制与下一步：仅完整机构摘要与正式元数据；未核验估计器、依赖处理或全部实验，不能将摘要视为现实 Tor 部署的精确信息量。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://experts.umn.edu/en/publications/measuring-information-leakage-in-website-fingerprinting-attacks-a/。
- [详细阅读记录](notes/ccs2025-second-pass-metrics-transfer-and-access-20261114.md)
- 代码/数据核查：no author code/data executed; completeness not verified；引用追踪：pending except explicit inventory。

## Masking the GLP Lattice-Based Signature Scheme at Any Order

- 来源：[EUROCRYPT 2018](https://doi.org/10.1007/978-3-319-78375-8_12)；时间标记：outside rolling window; cited foundation retained。
- 作者：Gilles Barthe; Sonia Belaïd; Thomas Espitau; Pierre-Alain Fouque; Benjamin Grégoire; Mélissa Rossi; Mehdi Tibouchi
- 对象：GLP, lattice signatures, masking；类型：countermeasure。
- 核心想法：为无需离散高斯采样的 GLP 格签名构造任意阶掩码，并扩展份额转换组件。
- 作者报告：摘要报告 ISW/探针模型下的保护方法、考虑公开输出的定义及概念实现。
- 限制与下一步：形式探针保证与概念实现不等于真实平台任意阶泄漏验证；与 2024 年期刊版分列并建立版本关系。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://link.springer.com/chapter/10.1007/978-3-319-78375-8_12。
- 代码/数据核查：not checked；引用追踪：pending。

## Composable Masking Schemes in the Presence of Physical Defaults & the Robust Probing Model

- 来源：[TCHES 2018](https://doi.org/10.46586/tches.v2018.i3.89-120)；时间标记：pre-window foundational reference。
- 作者：Sebastian Faust; Vincent Grosso; Santos Merino Del Pozo; Clara Paglialonga; François-Xavier Standaert
- 对象：robust probing, glitches, composability；类型：masking theory。
- 核心想法：以 robust probing 模型同时研究物理效应鲁棒性和掩码组合。
- 作者报告：作者构造并证明高阶、鲁棒、可组合乘法部件，强调它们与既有 ISW/TI/DOM 类方案的实现差别。
- 限制与下一步：2018 年模型结果；物理默认效应只在具体形式化范围内覆盖，不能替代部署实现评估。摘要来自出版商提交的 Crossref。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://api.crossref.org/works?query.title=Composable+Masking+Schemes+in+the+Presence+of+Physical+Defaults+and+the+Robust+Probing+Model&rows=3。
- [详细阅读记录](notes/masking-foundations-gaussian-timing-and-falcon-20261114.md)
- 代码/数据核查：no author code or data executed; artifact completeness not inspected；引用追踪：pending except selected verified Gaussian follow-up。

## Generic Low-Latency Masking in Hardware

- 来源：[TCHES 2018](https://doi.org/10.46586/tches.v2018.i2.1-21)；时间标记：pre-window foundational reference。
- 作者：Hannes Gross; Rinat Iusupov; Roderick Bloem
- 对象：DOM, AES, Ascon, latency；类型：hardware masking。
- 核心想法：通过避免非线性份额碰撞及调整份额压缩，交换延迟、面积与随机性。
- 作者报告：摘要报告单周期和双周期一阶 AES S-box 的不同成本，并对 Ascon 部件进行至三阶形式验证。
- 限制与下一步：无在线随机性是特定极端变体，不能与所有压缩输出变体混用；形式验证阶数、综合规模及物理安全是不同证据。旧 DOI 保留。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://api.crossref.org/works/10.46586/tches.v2018.i2.1-21。
- [详细阅读记录](notes/masking-foundations-gaussian-timing-and-falcon-20261114.md)
- 代码/数据核查：no author code or data executed; artifact completeness not inspected；引用追踪：pending except selected verified Gaussian follow-up。

## Improved High-Order Conversion From Boolean to Arithmetic Masking

- 来源：[TCHES 2018](https://doi.org/10.46586/tches.v2018.i2.22-45)；时间标记：pre-window foundational reference。
- 作者：Luk Bettale; Jean-Sébastien Coron; Rina Zeitoun
- 对象：B2A, ISW, mask refreshing；类型：masking conversion。
- 核心想法：简化 2017 年高阶 B2A 的掩码刷新，在 ISW 探针模型下保持证明。
- 作者报告：出版商摘要报告实际实现约快 25%。
- 限制与下一步：窗口外基础论文；25% 为相对所比较转换算法，不能当作完整 PQC 应用提速。被引旧 DOI 与当前 Crossref DOI 均保留。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://api.crossref.org/works/10.46586/tches.v2018.i2.22-45。
- [详细阅读记录](notes/masking-foundations-gaussian-timing-and-falcon-20261114.md)
- 代码/数据核查：no author code or data executed; artifact completeness not inspected；引用追踪：pending except selected verified Gaussian follow-up。

## Practical CCA2-Secure and Masked Ring-LWE Implementation

- 来源：[TCHES 2018](https://doi.org/10.46586/tches.v2018.i1.142-174)；时间标记：outside rolling five-year window; cited foundation。
- 作者：Tobias Oder; Tobias Schneider; Thomas Pöppelmann; Tim Güneysu
- 对象：Ring-LWE, FO, masking；类型：countermeasure。
- 核心想法：结合后量子 FO 变换、一阶掩码和掩码二项采样器保护 RLWE 解密与重加密。
- 作者报告：作者报告 Cortex-M4F 性能与非特定 t 检验的一阶评估。
- 限制与下一步：未检出一阶泄漏不代表任意阶或任意物理观察安全；历史 RLWE 实例不等于最终 ML-KEM。只读出版摘要与元数据。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://doi.org/10.46586/tches.v2018.i1.142-174; https://api.crossref.org/works/10.46586/tches.v2018.i1.142-174。
- [详细阅读记录](notes/pqc-citation-followups-and-evidence-20261113.md)
- 代码/数据核查：no author code or data executed; artifact contents not inspected；引用追踪：pending except explicitly inventoried citations。

## Side-Channel Attacks on Post-Quantum Signature Schemes based on Multivariate Quadratic Equations: - Rainbow and UOV -

- 来源：[TCHES 2018](https://doi.org/10.46586/tches.v2018.i3.500-523)；时间标记：pre-window foundational reference。
- 作者：Aesun Park; Kyung-Ah Shim; Namhun Koo; Dong-Guk Han
- 对象：Rainbow, UOV, CPA, AVR；类型：attack。
- 核心想法：分析仿射映射与矩阵向量乘法泄漏；区分等价密钥结构和 CPA 后接代数恢复的情形。
- 作者报告：出版商摘要报告 8 位 AVR 上 Rainbow 的 CPA 案例，并分析对多层及特定单层 UOV 实现的适用性。
- 限制与下一步：五年窗口外基础文献。实测 Rainbow 不等于 UOV 同配置实测；UOV 结论带有简单结构等价密钥的实现条件，不能自动套用现行规范。仅摘要。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://api.crossref.org/works/10.46586/tches.v2018.i3.500-523。
- [详细阅读记录](notes/muov-followups-and-masked-sampling-20261114.md)
- 代码/数据核查：no author code/data executed; artifact completeness not inspected；引用追踪：pending except explicit inventories。

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

## Practical Evaluation of Masking for NTRUEncrypt on ARM Cortex-M4

- 来源：[COSADE 2019](https://doi.org/10.1007/978-3-030-16350-1_14)；时间标记：outside rolling five-year window; cited foundation。
- 作者：Thomas Schamberger; Oliver Mischke; Johanna Sepulveda
- 对象：NTRUEncrypt, SIMD, masking；类型：countermeasure_evaluation。
- 核心想法：评估 Cortex-M4 三值多项式索引乘法的加性掩码及 SIMD 实现。
- 作者报告：作者在 HW 模型和两百万测量下未见一阶泄漏，但 SIMD 与顺序实现均有成功二阶攻击。
- 限制与下一步：一阶未检出不等于普遍安全；掩码加打乱的折中结论受测试条件限制。COSADE 2019 窗口外引用。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://link.springer.com/chapter/10.1007/978-3-030-16350-1_14。
- [详细阅读记录](notes/pqc-citation-followups-and-evidence-20261113.md)
- 代码/数据核查：no author code or data executed; artifact contents not inspected；引用追踪：pending except explicitly inventoried citations。

## maskVerif: Automated Verification of Higher-Order Masking in Presence of Physical Defaults

- 来源：[ESORICS 2019](https://doi.org/10.1007/978-3-030-29959-0_15)；时间标记：pre-window foundational reference。
- 作者：Gilles Barthe; Sonia Belaïd; Gaëtan Cassiers; Pierre-Alain Fouque; Benjamin Grégoire; Francois-Xavier Standaert
- 对象：masking, glitches, transitions, maskVerif；类型：formal verification。
- 核心想法：自动验证含毛刺或转换泄漏模型下的高阶掩码，并研究组合条件。
- 作者报告：作者以概率信息流方法扩展掩码验证，处理传统独立泄漏假设在物理默认效应下的失效。
- 限制与下一步：窗口外基础论文；工具在指定模型下的验证不等于任意 CMOS 的实测安全。仅读摘要。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://link.springer.com/chapter/10.1007/978-3-030-29959-0_15。
- [详细阅读记录](notes/masking-foundations-gaussian-timing-and-falcon-20261114.md)
- 代码/数据核查：no author code or data executed; artifact completeness not inspected；引用追踪：pending except selected verified Gaussian follow-up。

## FPGA Implementation and Comparison of Protections Against SCAs for RLWE

- 来源：[INDOCRYPT 2019](https://doi.org/10.1007/978-3-030-35423-7_27)；时间标记：outside rolling five-year window; cited foundation。
- 作者：Timo Zijlstra; Karim Bigou; Arnaud Tisserand
- 对象：RLWE；类型：countermeasure。
- 核心想法：实现并比较 RLWE-PKE FPGA 防护，包含环元素冗余表示的随机化。
- 作者报告：Springer 摘要报告既有保护改进与实现成本对比。
- 限制与下一步：RLWE-PKE 不能自动视为 Kyber 或最终 ML-KEM；安全评估预算和硬件模型待全文。2019 年窗口外基础文献。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://link.springer.com/chapter/10.1007/978-3-030-35423-7_27。
- [详细阅读记录](notes/kyber-shuffle-followups-and-evidence-20261113.md)
- 代码/数据核查：not inspected; no author code executed；引用追踪：pending except explicitly linked references。

## Efficiently Masking Binomial Sampling at Arbitrary Orders for Lattice-Based Crypto

- 来源：[PKC 2019](https://doi.org/10.1007/978-3-030-17259-6_18)；时间标记：pre-window foundational reference。
- 作者：Tobias Schneider; Clara Paglialonga; Tobias Oder; Tim Güneysu
- 对象：binomial sampler, B2A, NewHope, Kyber, Saber；类型：masking。
- 核心想法：组合布尔到算术掩码转换与位切片二项采样器，讨论任意阶保护。
- 作者报告：正式摘要给出任意阶方法；出版页脚注 8 明确所报周期不计输入比特向量生成。
- 限制与下一步：五年窗口外基础文献；不能把二项采样当成任意参数精确高斯采样，也不能直接与包含随机输入生成的周期数比较。正文证明与物理评估未完整审读。
- 阅读层级：selected_full_text_sections；来源：https://link.springer.com/chapter/10.1007/978-3-030-17259-6_18。
- 已读章节：Publisher abstract and visible Notes 1-8, especially note 8 excluding input bit-vector generation from cycle counts. Main chapter proofs/evaluation not read.
- [详细阅读记录](notes/muov-followups-and-masked-sampling-20261114.md)
- 代码/数据核查：no author code/data executed; artifact completeness not inspected；引用追踪：pending except explicit inventories。

## A Timing Attack on the HQC Encryption Scheme

- 来源：[SAC 2019](https://doi.org/10.1007/978-3-030-38471-5_22)；时间标记：outside rolling five-year window; cited foundation。
- 作者：Thales Bandiera Paiva; Routo Terada
- 对象：HQC, BCH, timing；类型：attack。
- 核心想法：利用第一轮 HQC 参考实现 BCH 译码时间与纠错数量的关系。
- 作者报告：摘要报告 128 位参数设置约四亿个密文的时间测量需求。
- 限制与下一步：针对第一轮可变时译码器；不是当前 HQC 的统一预算，也不能与后续功耗/EM 的迹线数直接比较。SAC 2019、2020 出版。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://link.springer.com/chapter/10.1007/978-3-030-38471-5_22。
- [详细阅读记录](notes/pqc-citation-followups-and-evidence-20261113.md)
- 代码/数据核查：no author code or data executed; artifact contents not inspected；引用追踪：pending except explicitly inventoried citations。

## A Power Side-Channel Attack on the CCA2-Secure HQC KEM

- 来源：[CARDIS 2020](https://doi.org/10.1007/978-3-030-68487-7_8)；时间标记：outside rolling five-year window; cited foundation。
- 作者：Thomas Schamberger; Julian Renner; Georg Sigl; Antonia Wachter-Zeh
- 对象：HQC, BCH；类型：attack。
- 核心想法：利用第二轮 HQC BCH 译码纠错事件的功耗 oracle 恢复大部分秘密，再用线性代数处理剩余部分。
- 作者报告：作者报告 Cortex-M4 参考实现不足一万次测量。
- 限制与下一步：目标是第二轮 BCH 译码实现；不能直接移用到 RM/RS 或最终版本。CARDIS 2020、2021-01 出版，均在滚动窗口前。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://link.springer.com/chapter/10.1007/978-3-030-68487-7_8。
- [详细阅读记录](notes/pqc-citation-followups-and-evidence-20261113.md)
- 代码/数据核查：no author code or data executed; artifact contents not inspected；引用追踪：pending except explicitly inventoried citations。

## SNI-in-the-head: Protecting MPC-in-the-head Protocols against Side-channel Analysis

- 来源：[CCS 2020](https://doi.org/10.1145/3372297.3417889)；时间标记：outside rolling five-year window; cited foundation。
- 作者：Okan Seker; Sebastian Berndt; Luca Wilke; Thomas Eisenbarth
- 对象：ZKBoo, MPC-in-the-Head, SNI；类型：countermeasure_protocol。
- 核心想法：利用平衡的强非干扰组件把 ZKBoo 扩展为可调探测阶数的协议。
- 作者报告：作者以模拟 DPA 展示原协议问题，并报告防护与实际实现的性能评估。
- 限制与下一步：DPA 演示是模拟，不能用性能实现替代物理采集证据；安全性依赖其探测模型。CCS 2020 为窗口外基础文献。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://eprint.iacr.org/2020/544; https://research.uni-luebeck.de/de/publications/sni-in-the-head-protecting-mpc-in-the-head-protocols-against-side/。
- [详细阅读记录](notes/mpcith-revisions-and-evidence-20261113.md)
- 代码/数据核查：not inspected; no author code executed；引用追踪：pending except explicitly linked references。

## A Key-Recovery Timing Attack on Post-quantum Primitives Using the Fujisaki-Okamoto Transformation and Its Application on FrodoKEM

- 来源：[CRYPTO 2020](https://doi.org/10.1007/978-3-030-56880-1_13)；时间标记：outside rolling window; explicitly cited foundational work。
- 作者：Qian Guo; Thomas Johansson; Alexander Nilsson
- 对象：FrodoKEM, Fujisaki-Okamoto, ciphertext comparison；类型：pqc_timing_side_channel。
- 核心想法：研究 FO 转换中密文比较的时序泄漏，说明不能只保护底层 CPA 原语的直接秘密运算。
- 作者报告：作者在当时 FrodoKEM 参考实现上报告密钥恢复，并给出约 2^30 次解封装调用的实验量级。
- 限制与下一步：这是 CRYPTO 2020 的窗口外基础工作；需核对攻击时序精度、实现版本和各参数预算，不能推断当前恒时实现或全部 FO 转换都可攻击。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://link.springer.com/chapter/10.1007/978-3-030-56880-1_13。
- 代码/数据核查：not checked；引用追踪：pending。

## Side-Channel Masking with Pseudo-Random Generator

- 来源：[EUROCRYPT 2020](https://doi.org/10.1007/978-3-030-45727-3_12)；时间标记：outside rolling five-year window; cited foundation。
- 作者：Jean-Sébastien Coron; Aurélien Greuet; Rina Zeitoun
- 对象：masking, PRG, AES；类型：countermeasure。
- 核心想法：用多个独立 PRG 降低指定 ISW 掩码电路的新鲜随机性成本。
- 作者报告：作者给出探测模型中的构造及 ARM 慢 TRNG 条件下的可行性实现。
- 限制与下一步：不同 PRG 的独立性和电路条件不可省略；不能改写成任意伪随机发生器都能替代安全随机性。仅摘要，未复核证明或实测安全范围。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://link.springer.com/chapter/10.1007/978-3-030-45727-3_12。
- [详细阅读记录](notes/mpcith-revisions-and-evidence-20261113.md)
- 代码/数据核查：not inspected; no author code executed；引用追踪：pending except explicitly linked references。

## Single-Trace Attacks on Message Encoding in Lattice-Based KEMs

- 来源：[IEEE Access 2020](https://doi.org/10.1109/access.2020.3029521)；时间标记：outside rolling five-year window; cited foundation。
- 作者：Bo-Yeon Sim; Jihoon Kwon; Joohee Lee; Il-Ju Kim; Tae-Ho Lee; Jaeseung Han; Hyojin Yoon; Jihoon Cho; Dong-Guk Han
- 对象：Kyber, Saber, FrodoKEM, message encoding；类型：attack。
- 核心想法：针对格 KEM 封装消息编码的单迹线泄漏恢复临时会话密钥。
- 作者报告：作者在 ChipWhisperer STM32F3 上报告 Kyber/Saber 100%、FrodoKEM 超过 79% 的指定实验成功率，并讨论其他候选。
- 限制与下一步：临时会话密钥与长期私钥不同；其他候选的适用性不等于逐项实测。只读明确链接 IEEE Access 的作者摘要，优化与全部攻击预算仍待全文。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://eprint.iacr.org/2020/992; https://api.crossref.org/works/10.1109/ACCESS.2020.3029521。
- [详细阅读记录](notes/pqc-citation-followups-and-evidence-20261113.md)
- 代码/数据核查：no author code or data executed; artifact contents not inspected；引用追踪：pending except explicitly inventoried citations。

## Constant-time foundations for the new spectre era

- 来源：[PLDI 2020](https://doi.org/10.1145/3385412.3385970)；时间标记：outside rolling window; cited foundation retained。
- 作者：Sunjay Cauligi; Craig Disselkoen; Klaus v. Gleissenthall; Dean Tullsen; Deian Stefan; Tamara Rezk; Gilles Barthe
- 对象：constant-time, speculative execution, Pitchfork；类型：formal_model_and_analysis。
- 核心想法：把推测与乱序执行纳入恒时语义及分析，检查传统恒时抽象的遗漏。
- 作者报告：作者摘要报告微架构攻击者模型与 Pitchfork 对密码库的检查。
- 限制与下一步：阅读作者 arXiv v3 摘要并与正式 DOI 核对身份；该观察模型不自动覆盖功耗、EM 或所有硬件实现。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://arxiv.org/abs/1910.01755。
- 代码/数据核查：not checked；引用追踪：pending。

## Defeating NewHope with a Single Trace

- 来源：[PQCrypto 2020](https://doi.org/10.1007/978-3-030-44223-1_11)；时间标记：outside rolling five-year window; cited foundation。
- 作者：Dorian Amiet; Andreas Curiger; Lukas Leuenberger; Paul Zbinden
- 对象：NewHope；类型：attack。
- 核心想法：针对 NewHope C 参考实现的共享秘密，研究 Cortex-M4 单迹线功耗恢复。
- 作者报告：作者报告关闭优化时可直接辨认，开启优化后仍可用更复杂方法恢复共享秘密。
- 限制与下一步：恢复对象是共享秘密，不是长期私钥；只读摘要，具体预处理和预算待全文。历史实现不能直接代表最终标准。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://link.springer.com/chapter/10.1007/978-3-030-44223-1_11。
- [详细阅读记录](notes/pqc-citation-followups-and-evidence-20261113.md)
- 代码/数据核查：no author code or data executed; artifact contents not inspected；引用追踪：pending except explicitly inventoried citations。

## Isochronous Gaussian Sampling: From Inception to Implementation: With Applications to the Falcon Signature Scheme

- 来源：[PQCrypto 2020](https://doi.org/10.1007/978-3-030-44223-1_4)；时间标记：pre-window foundational reference。
- 作者：James Howe; Thomas Prest; Thomas Ricosset; Mélissa Rossi
- 对象：Gaussian sampler, FALCON, SAGA, isochrony；类型：timing countermeasure。
- 核心想法：以 isochrony 描述随机运行时间与指定敏感量独立或统计接近，并提供 SAGA 采样测试。
- 作者报告：作者稿第 4 页给出定义，第 9 页 Theorem 8 在基本整数/浮点运算 isochronous 等前提下论证采样时间分布。
- 限制与下一步：isochrony 不要求每次耗时相等，也不保护功耗/EM。原语时序、σ 范围及散度前提不可省略；作者稿与正式章节未全量比对。
- 阅读层级：selected_full_text_sections；来源：https://link.springer.com/chapter/10.1007/978-3-030-44223-1_4。
- 已读章节：Publisher/ePrint abstracts; author 25-page PDF pages 4 and 9, Definition 4, Theorem 8, Corollary 9 and SAGA introduction. Page 9 visually checked; proofs and full artifact coverage not read.
- [详细阅读记录](notes/masking-foundations-gaussian-timing-and-falcon-20261114.md)
- 代码/数据核查：no author code or data executed; artifact completeness not inspected；引用追踪：One explicit 2022 -> 2020 citation verified; full backward/forward closure pending。

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

## On Configurable SCA Countermeasures Against Single Trace Attacks for the NTT: A Performance Evaluation Study over Kyber and Dilithium on the ARM Cortex-M4

- 来源：[SPACE 2020](https://doi.org/10.1007/978-3-030-66626-2_7)；时间标记：outside rolling five-year window; cited foundation。
- 作者：Prasanna Ravi; Romain Poussier; Shivam Bhasin; Anupam Chattopadhyay
- 对象：Kyber, Dilithium, NTT；类型：countermeasure。
- 核心想法：比较利用旋转因子性质的 NTT 局部掩码与不同粒度打乱。
- 作者报告：摘要报告 pqm4 Cortex-M4 运行时间评价：Kyber 7%–78%，Dilithium 密钥生成 12%–197%、签名 32%–490% 开销。
- 限制与下一步：这是具体实现的性能比较范围；尚未核查全文各配置的泄漏验证，不把开销评测等同于完整实测安全证明。窗口外基础文献。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://link.springer.com/chapter/10.1007/978-3-030-66626-2_7; https://eprint.iacr.org/2020/1038。
- [详细阅读记录](notes/kyber-shuffle-followups-and-evidence-20261113.md)
- 代码/数据核查：not inspected; no author code executed；引用追踪：selected backward/forward relation verified; complete tracing pending。

## Generic Side-channel attacks on CCA-secure lattice-based PKE and KEMs

- 来源：[TCHES 2020](https://doi.org/10.46586/tches.v2020.i3.307-335)；时间标记：outside rolling five-year window; cited foundation。
- 作者：Prasanna Ravi; Sujoy Sinha Roy; Anupam Chattopadhyay; Shivam Bhasin
- 对象：lattice KEM, FO, LWE, LWR；类型：attack。
- 核心想法：利用 ECC 与 FO 的 EM 泄漏建立明文检查 oracle，执行侧信道辅助选择密文分析。
- 作者报告：作者报告六种第二轮格 PKE/KEM 的 pqm4 Cortex-M4 实现完整密钥恢复。
- 限制与下一步：历史候选与最终标准区分；摘要中的分钟级报告不替代逐方案迹线、查询和剖析预算。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://doi.org/10.46586/tches.v2020.i3.307-335; https://api.crossref.org/works/10.46586/tches.v2020.i3.307-335。
- [详细阅读记录](notes/pqc-citation-followups-and-evidence-20261113.md)
- 代码/数据核查：no author code or data executed; artifact contents not inspected；引用追踪：pending except explicitly inventoried citations。

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

## Single-Trace Attacks on Keccak

- 来源：[TCHES 2020](https://doi.org/10.46586/tches.v2020.i3.243-268)；时间标记：outside rolling five-year window; cited foundation。
- 作者：Matthias J. Kannwischer; Peter Pessl; Robert Primas
- 对象：Keccak, SASCA, template attacks；类型：attack。
- 核心想法：结合模板匹配与因子图消息传递，研究 Keccak 临时秘密的单迹线恢复。
- 作者报告：作者在通用微控制器的带噪 HW 模型中模拟评估恢复表现。
- 限制与下一步：这是模拟而非硬件采集；单次目标观察仍有剖析假设。Keccak 是 PQC 构件，不代表完成某个具体 PQC 实现的恢复。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://tches.iacr.org/index.php/TCHES/article/view/8590。
- [详细阅读记录](notes/mpcith-revisions-and-evidence-20261113.md)
- 代码/数据核查：not inspected; no author code executed；引用追踪：pending except explicitly linked references。

## Trivially and Efficiently Composing Masked Gadgets With Probe Isolating Non-Interference

- 来源：[TIFS 2020](https://doi.org/10.1109/tifs.2020.2971153)；时间标记：pre-window foundational reference。
- 作者：Gaetan Cassiers; Francois-Xavier Standaert
- 对象：PINI, SNI, MIMO-SNI, AES；类型：composable masking。
- 核心想法：以份额位置约束定义 PINI，简化部件组合，并讨论多输入多输出组合。
- 作者报告：作者提出组合定理及乘法部件，比较 AES 与轻量密码性能；作者稿引言明确抽象探针安全只是实现分析的一步。
- 限制与下一步：仅读出版摘要及作者稿第 1 页摘要/引言，未完整审查定理；不能从 PINI 自动外推毛刺、转换或其他实际物理效应。
- 阅读层级：selected_full_text_sections；来源：https://ieeexplore.ieee.org/abstract/document/8979162/。
- 已读章节：Publisher full abstract; author 13-page PDF page 1 abstract and introduction only. Formal theorems and benchmarks not fully read.
- [详细阅读记录](notes/masking-foundations-gaussian-timing-and-falcon-20261114.md)
- 代码/数据核查：no author code or data executed; artifact completeness not inspected；引用追踪：pending except selected verified Gaussian follow-up。

## Breaking Masked and Shuffled CCA Secure Saber KEM by Power Analysis

- 来源：[ASHES 2021](https://doi.org/10.1145/3474376.3487277)；时间标记：within rolling five-year window by publication date。
- 作者：Kalle Ngo; Elena Dubrova; Thomas Johansson
- 对象：Saber, masking, shuffling；类型：attack。
- 核心想法：研究用剖析式深度学习功耗分析恢复被掩码和打乱保护的 Saber 消息及长期秘密。
- 作者报告：作者 ePrint 摘要给出会话 257N、长期 24×257N 条迹线，实验 N=10；训练含 80% 剖析设备和 20% 目标设备已知全零/全一消息迹线。
- 限制与下一步：不能忽略目标设备校准数据；ePrint 只写 Preprint，其与 ASHES 正式版本仅原始来源推定。2023 期刊版明确为该会议论文扩展，不能算独立复现。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://eprint.iacr.org/2021/902; https://api.crossref.org/works/10.1145/3474376.3487277; https://link.springer.com/article/10.1007/s13389-023-00315-3。
- [详细阅读记录](notes/pqc-citation-followups-and-evidence-20261113.md)
- 代码/数据核查：no author code or data executed; artifact contents not inspected；引用追踪：pending except explicitly inventoried citations。

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

## Information-Set Decoding with Hints

- 来源：[CBCrypto 2021](https://doi.org/10.1007/978-3-030-98365-9_4)；时间标记：within rolling five-year window by publication date。
- 作者：Anna-Lena Horlemann; Sven Puchinger; Julian Renner; Thomas Schamberger; Antonia Wachter-Zeh
- 对象：HQC, BIKE, Classic McEliece, ISD；类型：side_information_cryptanalysis。
- 核心想法：分析错误或消息的部分知识及子块 HW 提示对信息集译码的影响。
- 作者报告：作者为第三轮三种编码候选分析提示如何降低求解成本，并提出适配的 ISD 方法。
- 限制与下一步：是侧信道提示驱动的密码分析，不是这些候选上的真实波形攻击；摘要动机不能当作提示已可采集的证据。会议 2021、出版 2022。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://link.springer.com/chapter/10.1007/978-3-030-98365-9_4。
- [详细阅读记录](notes/pqc-citation-followups-and-evidence-20261113.md)
- 代码/数据核查：no author code or data executed; artifact contents not inspected；引用追踪：pending except explicitly inventoried citations。

## Secure Wire Shuffling in the Probing Model

- 来源：[CRYPTO 2021](https://doi.org/10.1007/978-3-030-84252-9_8)；时间标记：pre-window foundational reference。
- 作者：Jean-Sébastien Coron; Lorenzo Spignoli
- 对象：wire shuffling, probing, AES；类型：countermeasure theory。
- 核心想法：改进线打乱在最坏情形探针模型中的统计安全构造。
- 作者报告：摘要报告相对于探针数 t 的线性开销，并给出 AES 实现在 t≥6000 时超过所比较掩码实现的条件。
- 限制与下一步：CRYPTO 2021 于五年截点之前；统计安全与传统掩码的完美安全不同，不能将 t≥6000 的比较外推为常见低阶硬件优势。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://link.springer.com/chapter/10.1007/978-3-030-84252-9_8。
- [详细阅读记录](notes/masking-foundations-gaussian-timing-and-falcon-20261114.md)
- 代码/数据核查：no author code or data executed; artifact completeness not inspected；引用追踪：pending except selected verified Gaussian follow-up。

## FALCON Down: Breaking FALCON Post-Quantum Signature Scheme through Side-Channel Attacks

- 来源：[DAC 2021](https://doi.org/10.1109/dac18074.2021.9586131)；时间标记：within rolling five-year window by publication date。
- 作者：Emre Karabulut; Aydin Aysu
- 对象：Falcon, FFT, floating point；类型：attack。
- 核心想法：针对 Falcon 的双精度浮点运算，组合乘法与加法证据排除系数候选歧义。
- 作者报告：作者在 Cortex-M4 的 Falcon-512 上报告约一万条 EM 测量的密钥恢复，使用非剖析差分分析。
- 限制与下一步：实测为 Round-3 参考代码、gcc-arm-none-eabi-4_8-2014q1、-O0、168 MHz；Falcon-1024 是适用性论述。图 4 的 99.99% 是相关性置信水平，不是整密钥成功率。FFT 比 NTT 更安全仅讨论假设，未建立公平比较。
- 阅读层级：selected_full_text_sections；来源：https://research.ece.ncsu.edu/wp-content/uploads/sites/8/DAC_21_FALCON_SCA.pdf; https://eprint.iacr.org/2021/772; https://research.ece.ncsu.edu/aaysu/publication/falcon-down-breaking-falcon-post-quantum-signature-scheme-through-side-channel-attacks/。
- 已读章节：Author PDF selected pages 1 and 4-6: abstract, extend-and-prune overview, evaluation platform and Figure 4, discussion and all 28 reference positions; Figure 4 visually inspected in prior retrieval work. Not a full proof or attack reproduction.
- [详细阅读记录](notes/pqc-citation-followups-and-evidence-20261113.md)
- 代码/数据核查：no author code or data executed; artifact contents not inspected；引用追踪：all 28 positions: five linked, 18 queued, four provisional background, reference 23 duplicates 18; not recursive closure。

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

## Differential Power Analysis of the Picnic Signature Scheme

- 来源：[PQCrypto 2021](https://doi.org/10.1007/978-3-030-81293-5_10)；时间标记：PQCrypto 2021 calendar-year boundary; online 2021-07-15 before rolling start 2021-11-12。
- 作者：Tim Gellersen; Okan Seker; Thomas Eisenbarth
- 对象：Picnic, LowMC, MPC-in-the-Head；类型：attack。
- 核心想法：通过 MPC-LowMC 的两处泄漏恢复秘密，进而影响 Picnic 签名。
- 作者报告：作者在 FRDM-K66F 上报告少于 1000 条 LowMC 迹线，可由少于 30 个 Picnic 签名取得。
- 限制与下一步：LowMC 迹线数与 Picnic 签名数不能互换；仅读摘要。2021-07 上线早于滚动窗口起点，作为边界基础论文保留。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://link.springer.com/chapter/10.1007/978-3-030-81293-5_10; https://eprint.iacr.org/2020/267。
- [详细阅读记录](notes/mpcith-revisions-and-evidence-20261113.md)
- 代码/数据核查：not inspected; no author code executed；引用追踪：pending except explicitly linked references。

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

## Vulnerable PQC against Side Channel Analysis - A Case Study on Kyber

- 来源：[AsianHOST 2022](https://doi.org/10.1109/asianhost56390.2022.10022165)；时间标记：within frozen rolling window; publication and version dates retained。
- 作者：Haocheng Ma; Shijian Pan; Ya Gao; Jiaji He; Yiqiang Zhao; Yier Jin
- 对象：Kyber, FPGA, power, EM, HDL, HLS；类型：hardware_side_channel_evaluation。
- 核心想法：比较 HDL/HLS Kyber 硬件实现的功耗及 EM 观察。
- 作者报告：作者在 SAKURA-G Spartan-6 上评价解密，明确流水/并行和选点条件。
- 限制与下一步：研究解密算术及攻击模型；不能据此声称最终 ML-KEM 全部 CCA 流程恢复。与 TCAS-I 2023 的数据/版本重用待核查。
- 阅读层级：selected_full_text_sections；来源：https://xplorestaging.ieee.org/document/10022165/。
- 已读章节：六页作者 PDF 第 1 页摘要、第 4 页 §IV 指定模型与 §V.A 平台设置；未阅读全文结果表。
- [详细阅读记录](notes/kyber-multiplication-and-shuffling-20261113.md)
- 代码/数据核查：not inspected；引用追踪：pending。

## Generic, efficient and isochronous Gaussian sampling over the integers

- 来源：[Cybersecurity 2022](https://doi.org/10.1186/s42400-022-00113-0)；时间标记：within frozen rolling window。
- 作者：Shuo Sun; Yongbin Zhou; Yunfeng Ji; Rui Zhang; Yang Tao
- 对象：Gaussian sampler, FALCON, PALISADE, COSAC, isochrony；类型：timing countermeasure。
- 核心想法：组合指数 Bernoulli 采样与不同 Gaussian 采样变体，分别定义所保护敏感量。
- 作者报告：正文表 1 区分 Type I/II/III；作者报告 FALCON 已建 LDL 树后的签名提速和 PALISADE 在线阶段收益。
- 限制与下一步：表 1 脚注提醒 COSAC 与 Algorithm 8 的拒绝率可能依赖中心；不能把它们当成保护 σ/c/z 的 Type I。整数及若干浮点原语 isochronous 是前提，除法等需预计算。
- 阅读层级：selected_full_text_sections；来源：https://link.springer.com/article/10.1186/s42400-022-00113-0。
- 已读章节：Publisher full abstract; formal PDF pages 3 and 5 (Table 1, footnotes, contributions, Definition 2 and primitive assumptions), page 21 data-availability statement; HTML reference 22. Pages 3 and 5 visually checked; remaining proofs not fully read.
- [详细阅读记录](notes/masking-foundations-gaussian-timing-and-falcon-20261114.md)
- 代码/数据核查：no author code or data executed; artifact completeness not inspected；引用追踪：One explicit 2022 -> 2020 citation verified; full backward/forward closure pending。

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

## A Masked Pure-Hardware Implementation of Kyber Cryptographic Algorithm

- 来源：[FPT 2022](https://doi.org/10.1109/icfpt56656.2022.9974404)；时间标记：within rolling five-year window。
- 作者：Tendayi Kamucheka; Alexander Nelson; David Andrews; Miaoqing Huang
- 对象：Kyber；类型：countermeasure。
- 核心想法：给出纯硬件掩码 Kyber；相关同题预印本描述 Kyber-512 的隐藏与掩码组合。
- 作者报告：IEEE 摘要报告功耗防护；同题 ePrint 摘要说明采用 TVLA 评价。后续 JCEN 2025 分析了由此设计裁减的消息解码模块。
- 限制与下一步：正式记录页码仅 1-1，不能用预印本补齐冒充正式全文。有限 TVLA 不证明所有攻击安全；ePrint 未显式链接正式 DOI，版本等价未核实。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/9974404/; https://eprint.iacr.org/2022/1547。
- [详细阅读记录](notes/kyber-shuffle-followups-and-evidence-20261113.md)
- 代码/数据核查：not inspected; no author code executed；引用追踪：selected backward/forward relation verified; complete tracing pending。

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

## A New Key Recovery Side-Channel Attack on HQC with Chosen Ciphertext

- 来源：[PQCrypto 2022](https://doi.org/10.1007/978-3-031-17234-2_17)；时间标记：within rolling five-year window by publication date。
- 作者：Guillaume Goy; Antoine Loiseau; Philippe Gaborit
- 对象：HQC, Reed-Muller, Hadamard；类型：attack。
- 核心想法：利用 Reed-Muller 译码中的 Hadamard 响应建立模式判别 oracle。
- 作者报告：摘要报告选择密文和重复静态私钥条件下，不足 20,000 条 EM 攻击迹线恢复完整静态私钥，并提出掩码防护。
- 限制与下一步：摘要仅确定微控制器与物理接触，不补写具体型号；训练、查询与采集预算待全文。不同 HQC 译码器版本的数量不可直接排名。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://link.springer.com/chapter/10.1007/978-3-031-17234-2_17。
- [详细阅读记录](notes/pqc-citation-followups-and-evidence-20261113.md)
- 代码/数据核查：no author code or data executed; artifact contents not inspected；引用追踪：pending except explicitly inventoried citations。

## A Power Side-Channel Attack on the Reed-Muller Reed-Solomon Version of the HQC Cryptosystem

- 来源：[PQCrypto 2022](https://doi.org/10.1007/978-3-031-17234-2_16)；时间标记：within rolling five-year window by publication date。
- 作者：Thomas Schamberger; Lukas Holzbaur; Julian Renner; Antonia Wachter-Zeh; Georg Sigl
- 对象：HQC, Reed-Muller, Reed-Solomon, ISD；类型：attack。
- 核心想法：针对 HQC RM/RS 译码版本重建攻击策略，组合功耗 oracle 与剩余求解成本分析。
- 作者报告：作者报告 Cortex-M4 RS 译码器实测，并称较 Guo 时间攻击减少约 12 倍查询；指出 Ueno 方案忽略 RM 译码边界非固定。
- 限制与下一步：对 Ueno 的批评是本文作者主张，尚未独立裁决；不能写成通用前作撤回。需全文核查概率条件、版本及预算；所引 Curse 论文为 TCHES 2022 卷、2021 在线。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://link.springer.com/chapter/10.1007/978-3-031-17234-2_16。
- [详细阅读记录](notes/pqc-citation-followups-and-evidence-20261113.md)
- 代码/数据核查：no author code or data executed; artifact contents not inspected；引用追踪：all 17 entries: five linked, three queued including thesis/fault scope uncertainty, nine provisional background; not recursive closure。

## Profiling Side-Channel Attacks on Dilithium: A Small Bit-Fiddling Leak Breaks It All

- 来源：[SAC 2022](https://doi.org/10.1007/978-3-031-58411-4_1)；时间标记：inside rolling window; SAC 2022, publication online 2024-05-12。
- 作者：Vincent Quentin Ulitzsch; Soundes Marzougui; Mehdi Tibouchi; Jean-Pierre Seifert
- 对象：Dilithium；类型：attack。
- 核心想法：利用签名中的位解包泄漏，将剖析读数与最小二乘、整数线性规划结合。
- 作者报告：作者报告 Cortex-M4 上恢复足以签署任意消息的等价秘密信息。
- 限制与下一步：等价签名能力不等于逐字恢复原始私钥。SAC 2022 的正式章节于 2024 年上线；预印本与正式版作者排序不同，全文等价尚未核对。
- 阅读层级：abstract_and_bibliographic_metadata；来源：publisher abstract and ePrint 2022/106 abstract: https://link.springer.com/chapter/10.1007/978-3-031-58411-4_1。
- 代码/数据核查：not checked；引用追踪：forward edge observed; backward and exhaustive forward search pending。

## "They're not that hard to mitigate": What Cryptographic Library Developers Think About Timing Attacks

- 来源：[SP 2022](https://doi.org/10.1109/sp46214.2022.9833713)；时间标记：within rolling window; SP 2022 formal date retained。
- 作者：Jan Jancar; Marcel Fourné; Daniel De Almeida Braga; Mohamed Sabt; Peter Schwabe; Gilles Barthe; Pierre-Alain Fouque; Yasemin Acar
- 对象：constant-time, timing, developer survey；类型：developer_study。
- 核心想法：调查密码库开发者如何处理恒时要求及工具使用障碍。
- 作者报告：作者调查 27 个库的 44 位开发者，讨论资源投入与分析工具缺口。
- 限制与下一步：开发者调查不是库实现无泄漏的证明，也不是所有开发者的普查。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/9833713/。
- 代码/数据核查：not inspected；引用追踪：pending。

## A Secret-Free Hypervisor: Rethinking Isolation in the Age of Speculative Vulnerabilities

- 来源：[SP 2022](https://doi.org/10.1109/sp46214.2022.9833726)；时间标记：within rolling window; SP 2022 formal date retained。
- 作者：Hongyan Xia; David Zhang; Wei Liu; Istvan Haller; Bruce Sherwin; David Chisnall
- 对象：Spectre, hypervisor, memory isolation；类型：microarchitectural_countermeasure。
- 核心想法：Secret-Free 通过只公开必要非秘密地址视图重组虚拟化隔离。
- 作者报告：作者在 Xen 等系统实现并评价性能与适配。
- 限制与下一步：指定秘密可见性和推测模型不覆盖所有物理功耗或 EM 通道。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/9833726/。
- 代码/数据核查：not inspected；引用追踪：pending。

## A Systematic Look at Ciphertext Side Channels on AMD SEV-SNP

- 来源：[SP 2022](https://doi.org/10.1109/sp46214.2022.9833768)；时间标记：within rolling window; SP 2022 formal date retained。
- 作者：Mengyuan Li; Luca Wilke; Jan Wichelmann; Thomas Eisenbarth; Radu Teodorescu; Yinqian Zhang
- 对象：AMD SEV-SNP, ciphertext side channel, memory encryption；类型：side_channel_analysis。
- 核心想法：把 AMD SEV 的密文变化观察从 VMSA 扩展到其他内存页。
- 作者报告：作者指出仅随机化 VMSA 的缓解不足，并提出 OS 和密码库软件措施。
- 限制与下一步：反映论文研究的硬件/固件状态；不是当前所有 SEV-SNP 版本的漏洞确认。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/9833768/。
- 代码/数据核查：not inspected；引用追踪：pending。

## AccEar: Accelerometer Acoustic Eavesdropping with Unconstrained Vocabulary

- 来源：[SP 2022](https://doi.org/10.1109/sp46214.2022.9833716)；时间标记：within rolling window; SP 2022 formal date retained。
- 作者：Pengfei Hu; Hui Zhuang; Panneer Selvam Santhalingam; Riccardo Spolaor; Parth Pathak; Guoming Zhang; Xiuzhen Cheng
- 对象：accelerometer, acoustic, audio reconstruction；类型：physical_side_channel。
- 核心想法：AccEar 从手机加速度计响应重建扬声器音频，研究超出固定词表的观察。
- 作者报告：作者使用条件 GAN 与频谱增强，在多种采样率、音量和设备条件评价。
- 限制与下一步：低频输入的生成式重建不等于逐样本精确还原任意语音；访问和训练条件仍需正文核对。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/9833716/。
- 代码/数据核查：not inspected；引用追踪：pending。

## Adversarial Prefetch: New Cross-Core Cache Side Channel Attacks

- 来源：[SP 2022](https://doi.org/10.1109/sp46214.2022.9833692)；时间标记：within rolling window; SP 2022 formal date retained。
- 作者：Yanan Guo; Andrew Zigerelli; Youtao Zhang; Jun Yang
- 对象：PREFETCHW, cache coherence, transient execution；类型：microarchitectural_side_channel。
- 核心想法：利用 PREFETCHW 权限行为和一致性状态计时构造跨核私有缓存通道。
- 作者报告：摘要报告隐蔽通道、真实应用侧信道与瞬态执行用途。
- 限制与下一步：共享缓存行、权限和处理器条件不同；隐蔽信道容量不是密钥恢复速率。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/9833692/。
- 代码/数据核查：not inspected；引用追踪：pending。

## Are We There Yet? Timing and Floating-Point Attacks on Differential Privacy Systems

- 来源：[SP 2022](https://doi.org/10.1109/sp46214.2022.9833672)；时间标记：within rolling window; SP 2022 formal date retained。
- 作者：Jiankai Jin; Eleanor McMurtry; Benjamin I. P. Rubinstein; Olga Ohrimenko
- 对象：differential privacy, floating point, sampling timing；类型：implementation_side_channel。
- 核心想法：研究差分隐私噪声生成中的浮点表示泄漏与离散采样计时泄漏。
- 作者报告：作者通过推断噪声幅度恢复敏感属性，并评价部分缓解。
- 限制与下一步：浮点输出缺陷和运行时间通道分别记录；实验成功率只对应所列 DP 实现与任务。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/9833672/。
- 代码/数据核查：not inspected；引用追踪：pending。

## Attacks on Wireless Coexistence

- 来源：[SP 2022](https://doi.org/10.1109/sp46214.2022.9833639)；时间标记：within rolling window; SP 2022 formal date retained。
- 作者：Jiska Classen; Francesco Gringoli; Michael Hermann; Matthias Hollick
- 对象：wireless coexistence, Bluetooth, keypress timing；类型：cross_chip_metadata_side_channel。
- 核心想法：无线共存协议的包时序与类型元数据可跨 Wi-Fi/Bluetooth 芯片暴露按键活动。
- 作者报告：作者稿 §V.D.5 展示 Wi-Fi 核获得 Bluetooth 键盘事件时序，另有直接读写与权限升级结果。
- 限制与下一步：需控制 Wi-Fi 核；按键时刻观察不等于解出键值或密码。直接内存攻击与元数据侧信道分开。
- 阅读层级：selected_full_text_sections；来源：https://xplorestaging.ieee.org/document/9833639/。
- 已读章节：arXiv author PDF page 4 §III.B and page 9 §V.D.5, alongside publisher abstract; no full bibliography audit
- [详细阅读记录](notes/sp2022-scope-and-identity-20261113.md)
- 代码/数据核查：not inspected；引用追踪：pending。

## Augury: Using Data Memory-Dependent Prefetchers to Leak Data at Rest

- 来源：[SP 2022](https://doi.org/10.1109/sp46214.2022.9833570)；时间标记：within rolling window; SP 2022 formal date retained。
- 作者：Jose Rodrigo Sanchez Vicarte; Michael Flanders; Riccardo Paccagnella; Grant Garrett-Grossman; Adam Morrison; Christopher W. Fletcher; David Kohlbrenner
- 对象：DMP, Apple, prefetcher, data at rest；类型：microarchitectural_side_channel。
- 核心想法：Augury 研究 Apple 数据相关预取器直接检查内存内容产生的泄漏。
- 作者报告：作者在 A14/M1 等研究指针追逐预取器及泄露指针的基本原语。
- 限制与下一步：不是任意值或 PQC 密钥恢复；不能把后来的 GoFetch 能力回写到本篇。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/9833570/。
- 代码/数据核查：not inspected；引用追踪：pending。

## Cats vs. Spectre: An Axiomatic Approach to Modeling Speculative Execution Attacks

- 来源：[SP 2022](https://doi.org/10.1109/sp46214.2022.9833774)；时间标记：within rolling window; SP 2022 formal date retained。
- 作者：Hernán Ponce-de-Leon; Johannes Kinder
- 对象：Spectre, CAT, axiomatic semantics；类型：formal_side_channel_analysis。
- 核心想法：以并发内存模型语言 CAT 表达推测执行规则，并作有界检查。
- 作者报告：作者模型覆盖推测控制流、转发与内存序清除等机制。
- 限制与下一步：模型可扩展不等于覆盖所有微架构；有界验证范围与真实设备证据分开。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/9833774/。
- 代码/数据核查：not inspected；引用追踪：pending。

## DeepCoFFEA: Improved Flow Correlation Attacks on Tor via Metric Learning and Amplification

- 来源：[SP 2022](https://doi.org/10.1109/sp46214.2022.9833801)；时间标记：within rolling window; SP 2022 formal date retained。
- 作者：Se Eun Oh; Taiji Yang; Nate Mathews; James K Holland; Mohammad Saidur Rahman; Nicholas Hopper; Matthew Wright
- 对象：Tor, encrypted traffic, flow correlation；类型：traffic_metadata_side_channel。
- 核心想法：DeepCoFFEA 用嵌入和分窗投票提高 Tor 入口与出口流关联。
- 作者报告：作者评价大规模配对下的计算成本、误报及多种对策。
- 限制与下一步：纳入依据为加密通信元数据到用户关联的具体泄漏；不等于密码内容或密钥恢复。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/9833801/。
- 代码/数据核查：not inspected；引用追踪：pending。

## DeepSteal: Advanced Model Extractions Leveraging Efficient Weight Stealing in Memories

- 来源：[SP 2022](https://doi.org/10.1109/sp46214.2022.9833743)；时间标记：within rolling window; SP 2022 formal date retained。
- 作者：Adnan Siraj Rakin; Md Hafizul Islam Chowdhuryy; Fan Yao; Deliang Fan
- 对象：Rowhammer, memory leakage, DNN weights；类型：combined_fault_and_side_channel。
- 核心想法：DeepSteal 通过 HammerLeak 将 Rowhammer 故障作为权重比特泄漏向量。
- 作者报告：作者结合部分权重信息与替代模型训练，评价模型提取和后续输入攻击。
- 限制与下一步：不是纯故障破坏；目标为 DNN 权重与替代行为，模型精度不代表全部权重逐位恢复。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/9833743/。
- 代码/数据核查：not inspected；引用追踪：pending。

## Device Fingerprinting with Peripheral Timestamps

- 来源：[SP 2022](https://doi.org/10.1109/sp46214.2022.9833612)；时间标记：within rolling window; SP 2022 formal date retained。
- 作者：John V. Monaco
- 对象：peripheral timestamps, browser, fingerprinting；类型：timing_fingerprinting。
- 核心想法：从外设输入事件的轮询与调度节奏形成浏览器设备指纹。
- 作者报告：作者提出双时钟相位模型并评价大量设备事件。
- 限制与下一步：设备识别与融合用户行为后的指标分开；指纹稳定性不等于秘密值恢复。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/9833612/。
- 代码/数据核查：not inspected；引用追踪：pending。

## Evaluating Physical-Layer BLE Location Tracking Attacks on Mobile Devices

- 来源：[SP 2022](https://doi.org/10.1109/sp46214.2022.9833758)；时间标记：within rolling window; SP 2022 formal date retained。
- 作者：Hadi Givehchian; Nishant Bhaskar; Eliana Rodriguez Herrera; Héctor Rodrigo López Soto; Christian Dameff; Dinesh Bharadia; Aaron Schulman
- 对象：BLE, physical-layer fingerprints, location privacy；类型：physical_side_channel。
- 核心想法：BLE 发射硬件缺陷可在标识轮换之外提供设备跟踪线索。
- 作者报告：作者摘要讨论芯片、温度、发射功率和低成本无线接收条件，并作野外评价。
- 限制与下一步：物理识别有时不可靠；不宣称每个设备唯一。出版页获取失败后读取作者 PDF 摘要。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://wcsng.ucsd.edu/files/sp22_paper.pdf。
- 代码/数据核查：not inspected；引用追踪：pending。

## Finding and Exploiting CPU Features using MSR Templating

- 来源：[SP 2022](https://doi.org/10.1109/sp46214.2022.9833599)；时间标记：within rolling window; SP 2022 formal date retained。
- 作者：Andreas Kogler; Daniel Weber; Martin Haubenwallner; Moritz Lipp; Daniel Gruss; Michael Schwarz
- 对象：MSR, AES-NI, SGX, microarchitecture；类型：configuration_assisted_side_channel。
- 核心想法：MSRevelio 检查 MSR 配置如何暴露或改变微架构攻击条件。
- 作者报告：作者展示关闭 AES-NI 后 mbedTLS 回退缓存攻击，以及隐藏计时来源等案例。
- 限制与下一步：需相应 MSR 配置能力；不是无权限普适密钥提取，具体案例边界待全文复核。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/9833599/。
- 代码/数据核查：not inspected；引用追踪：pending。

## Graphics Peeping Unit: Exploiting EM Side-Channel Information of GPUs to Eavesdrop on Your Neighbors

- 来源：[SP 2022](https://doi.org/10.1109/sp46214.2022.9833773)；时间标记：within rolling window; SP 2022 formal date retained。
- 作者：Zihao Zhan; Zhenkai Zhang; Sisheng Liang; Fan Yao; Xenofon Koutsoukos
- 对象：GPU, electromagnetic, DVFS, website fingerprinting；类型：physical_side_channel。
- 核心想法：研究 GPU EM 辐射携带的网站指纹和按键时序信息。
- 作者报告：作者分析 DVFS 关联，并指出关闭 DVFS 后仍可能存在另一种 EM 通道。
- 限制与下一步：面向非共享 GPU 的远距观察仍有传感与环境前提；不能从摘要推定所有 GPU 或任意距离。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/9833773/。
- 代码/数据核查：not inspected；引用追踪：pending。

## IRShield: A Countermeasure Against Adversarial Physical-Layer Wireless Sensing

- 来源：[SP 2022](https://doi.org/10.1109/sp46214.2022.9833676)；时间标记：within rolling window; SP 2022 formal date retained。
- 作者：Paul Staat; Simon Mulzer; Stefan Roth; Veelasha Moonsamy; Markus Heinrichs; Rainer Kronberger; Aydin Sezgin; Christof Paar
- 对象：wireless sensing, IRS, motion privacy；类型：physical_side_channel_countermeasure。
- 核心想法：IRShield 用可重构反射面扰动无线传播，抵御从通信信号推断室内活动。
- 作者报告：作者在商用 Wi-Fi 人体运动检测场景评价通道混淆。
- 限制与下一步：特定运动检测率不代表所有感知任务、位置或观察者均受保护。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/9833676/。
- 代码/数据核查：not inspected；引用追踪：pending。

## IronMask: Versatile Verification of Masking Security

- 来源：[SP 2022](https://doi.org/10.1109/sp46214.2022.9833600)；时间标记：within rolling window; SP 2022 formal date retained。
- 作者：Sonia Belaïd; Darius Mercadier; Matthieu Rivain; Abdul Rahman Taleb
- 对象：masking, probing, random probing, IronMask；类型：formal_verification。
- 核心想法：IronMask 验证指定探针与随机探针模型中的掩码安全及组合性质。
- 作者报告：作者为含非线性随机性的二次组件给出代数刻画，并比较验证性能。
- 限制与下一步：完备性限定于所述组件类别与模型；不是实测无泄漏或任意非线性电路证明。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/9833600/。
- 代码/数据核查：not inspected；引用追踪：pending。

## MeshUp: Stateless Cache Side-channel Attack on CPU Mesh

- 来源：[SP 2022](https://doi.org/10.1109/sp46214.2022.9833794)；时间标记：within rolling window; SP 2022 formal date retained。
- 作者：Junpeng Wan; Yanxiang Bi; Zhe Zhou; Zhou Li
- 对象：CPU mesh, interconnect contention, RSA；类型：microarchitectural_side_channel。
- 核心想法：MeshUp 通过互连拥塞计时观察访问模式，研究缓存隔离之外的共享资源。
- 作者报告：作者展示跨核 RSA 部分恢复和跨 CPU 应用指纹。
- 限制与下一步：stateless 指无需缓存状态持久观察，不等于系统无状态；RSA 结果是部分恢复。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/9833794/。
- 代码/数据核查：not inspected；引用追踪：pending。

## Mind the Gap: Studying the Insecurity of Provably Secure Embedded Trusted Execution Architectures

- 来源：[SP 2022](https://doi.org/10.1109/sp46214.2022.9833735)；时间标记：within rolling window; SP 2022 formal date retained。
- 作者：Marton Bognar; Jo Van Bulck; Frank Piessens
- 对象：embedded TEE, DMA, formal model mismatch；类型：implementation_and_model_analysis。
- 核心想法：对两种有形式证明的嵌入式可信架构检查模型与实现差距。
- 作者报告：摘要报告多种攻击，其中包括 DMA 侧信道，并提出加强证据的建议。
- 限制与下一步：程序错误与模型遗漏分别分析；不能把两个实例推成形式方法普遍无效。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/9833735/。
- 代码/数据核查：not inspected；引用追踪：pending。

## Mitigating Information Leakage Vulnerabilities with Type-based Data Isolation

- 来源：[SP 2022](https://doi.org/10.1109/sp46214.2022.9833675)；时间标记：within rolling window; SP 2022 formal date retained。
- 作者：Alyssa Milburn; Erik Van Der Kouwe; Cristiano Giuffrida
- 对象：type-based data isolation, speculation, compiler；类型：microarchitectural_countermeasure。
- 核心想法：TDI 用类型相关内存区域和指针运算插桩约束架构与推测读取。
- 作者报告：作者报告细粒度隔离性质及基准开销。
- 限制与下一步：侧信道纳入依据为推测域信息读取缓解；不是功耗/EM 或所有信息流保证。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/9833675/。
- 代码/数据核查：not inspected；引用追踪：pending。

## Noise-SDR: Arbitrary Modulation of Electromagnetic Noise from Unprivileged Software and Its Impact on Emission Security

- 来源：[SP 2022](https://doi.org/10.1109/sp46214.2022.9833767)；时间标记：within rolling window; SP 2022 formal date retained。
- 作者：Giovanni Camurati; Aurélien Francillon
- 对象：electromagnetic emission, DRAM, covert channel；类型：physical_channel_construction。
- 核心想法：Noise-SDR 通过普通软件活动塑造设备 EM 辐射，用于通信和信号注入。
- 作者报告：作者在多种 ISA 与设备上实现基于 DRAM 访问的调制。
- 限制与下一步：是有意调制的物理发射原语，不等于被动恢复任意秘密；功率、频带和带宽受平台限制。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/9833767/。
- 代码/数据核查：not inspected；引用追踪：pending。

## Noise: A Library of Verified High-Performance Secure Channel Protocol Implementations

- 来源：[SP 2022](https://doi.org/10.1109/sp46214.2022.9833621)；时间标记：within rolling window; SP 2022 formal date retained。
- 作者：Son Ho; Jonathan Protzenko; Abhishek Bichhawat; Karthikeyan Bhargavan
- 对象：Noise protocols, F*, verified compiler, side-channel resistance；类型：formal_countermeasure。
- 核心想法：Noise 协议编译器把功能、内存安全及一种侧信道保证贯穿到生成 C 代码。
- 作者报告：作者在 F* 中验证编译器并生成多种协议实现。
- 限制与下一步：摘要未精确展开该侧信道观察模型；必须补读，不能称为物理波形安全证明。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/9833621/。
- 代码/数据核查：not inspected；引用追踪：pending。

## SoK: Practical Foundations for Software Spectre Defenses

- 来源：[SP 2022](https://doi.org/10.1109/sp46214.2022.9833707)；时间标记：within rolling window; SP 2022 formal date retained。
- 作者：Sunjay Cauligi; Craig Disselkoen; Daniel Moghimi; Gilles Barthe; Deian Stefan
- 对象：Spectre, software defenses, formal semantics；类型：systematization。
- 核心想法：梳理软件 Spectre 缓解和验证工具的语义、保证与取舍。
- 作者报告：作者用统一框架比较有无形式模型的防护并提出开放问题。
- 限制与下一步：系统化比较的范围为所审查软件防护，不能当作全部处理器攻击的覆盖证明。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/9833707/。
- 代码/数据核查：not inspected；引用追踪：pending。

## SpecHammer: Combining Spectre and Rowhammer for New Speculative Attacks

- 来源：[SP 2022](https://doi.org/10.1109/sp46214.2022.9833802)；时间标记：within rolling window; SP 2022 formal date retained。
- 作者：Youssef Tobah; Andrew Kwong; Ingab Kang; Daniel Genkin; Kang G. Shin
- 对象：Spectre, Rowhammer, taint tracking；类型：combined_fault_and_side_channel。
- 核心想法：SpecHammer 用 Rowhammer 改变受害状态，扩大 Spectre 可用 gadget。
- 作者报告：作者展示用户态和内核样例中的敏感信息泄漏。
- 限制与下一步：纳入依据是故障与泄漏组合；gadget 数量不是实际可恢复秘密数量。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/9833802/。
- 代码/数据核查：not inspected；引用追踪：pending。

## Spook.js: Attacking Chrome Strict Site Isolation via Speculative Execution

- 来源：[SP 2022](https://doi.org/10.1109/sp46214.2022.9833711)；时间标记：within rolling window; SP 2022 formal date retained。
- 作者：Ayush Agarwal; Sioli O’Connell; Jason Kim; Shaked Yehezkel; Daniel Genkin; Eyal Ronen; Yuval Yarom
- 对象：Spook.js, Spectre, Chrome site isolation；类型：browser_microarchitectural_side_channel。
- 核心想法：Spook.js 研究 JavaScript 推测执行如何突破所测浏览器站点隔离边界。
- 作者报告：作者展示跨网页与扩展中敏感信息泄漏。
- 限制与下一步：结果对应论文所研究版本；不是当前 Chrome/Edge/Brave 的通用漏洞确认。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/9833711/。
- 代码/数据核查：not inspected；引用追踪：pending。

## Surakav: Generating Realistic Traces for a Strong Website Fingerprinting Defense

- 来源：[SP 2022](https://doi.org/10.1109/sp46214.2022.9833722)；时间标记：within rolling window; SP 2022 formal date retained。
- 作者：Jiajun Gong; Wuqi Zhang; Charles Zhang; Tao Wang
- 对象：Tor, website fingerprinting, GAN；类型：traffic_metadata_countermeasure。
- 核心想法：Surakav 生成发送模式并调节缓冲流量，抵御加密流量的网站指纹识别。
- 作者报告：作者在实时 Tor 网络评价攻击真阳性率与流量/时间成本。
- 限制与下一步：数据与时间开销、攻击真阳性率分别比较，指定评估不覆盖所有未来攻击。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/9833722/。
- 代码/数据核查：not inspected；引用追踪：pending。

## Time-Print: Authenticating USB Flash Drives with Novel Timing Fingerprints

- 来源：[SP 2022](https://doi.org/10.1109/sp46214.2022.9833595)；时间标记：within rolling window; SP 2022 formal date retained。
- 作者：Patrick Cronin; Xing Gao; Haining Wang; Chase Cotton
- 对象：USB, timing fingerprints, device authentication；类型：timing_fingerprinting。
- 核心想法：Time-Print 利用 USB 存储读取时延形成设备认证指纹。
- 作者报告：作者比较品牌型号识别、同型号识别和分类任务。
- 限制与下一步：作为可观察时间响应方法纳入；不是秘密恢复，三类识别率不能混成一个通用指标。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/9833595/。
- 代码/数据核查：not inspected；引用追踪：pending。

## Timing-Based Browsing Privacy Vulnerabilities Via Site Isolation

- 来源：[SP 2022](https://doi.org/10.1109/sp46214.2022.9833710)；时间标记：within rolling window; SP 2022 formal date retained。
- 作者：Zihao Jin; Ziqiao Kong; Shuo Chen; Haixin Duan
- 对象：browser, site isolation, timing；类型：browser_timing_side_channel。
- 核心想法：研究站点隔离的进程资源与计时关系如何暴露已打开及活跃网站。
- 作者报告：作者在目标站点集合中评价三种浏览行为观察指标。
- 限制与下一步：目标集合可访问性与进程条件待正文核查；论文时代的漏洞比例不是当前浏览器状态。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/9833710/。
- 代码/数据核查：not inspected；引用追踪：pending。

## mmSpy: Spying Phone Calls using mmWave Radars

- 来源：[SP 2022](https://doi.org/10.1109/sp46214.2022.9833568)；时间标记：within rolling window; SP 2022 formal date retained。
- 作者：Suryoday Basak; Mahanth Gowda
- 对象：mmWave radar, earpiece vibration, acoustic；类型：physical_side_channel。
- 核心想法：mmSpy 用毫米波雷达观察电话听筒微振动，研究远程语音信息推断。
- 作者报告：作者评价数字/关键词分类并展示音频重建可行性。
- 限制与下一步：词类识别、声音重建与完整通话转录不同；距离与训练域条件不可省略。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/9833568/。
- 代码/数据核查：not inspected；引用追踪：pending。

## Magnifying Side-Channel Leakage of Lattice-Based Cryptosystems With Chosen Ciphertexts: The Case Study of Kyber

- 来源：[TC 2022](https://doi.org/10.1109/tc.2021.3122997)；时间标记：calendar-year expansion: 2022 volume; early online 2021-10-27 before rolling start 2021-11-12。
- 作者：Zhuang Xu; Owen Pemberton; Sujoy Sinha Roy; David Oswald; Wang Yao; Zhiming Zheng
- 对象：Kyber, chosen ciphertext, EM；类型：attack。
- 核心想法：通过选择密文放大 iNTT 输出或消息处理泄漏，研究非模板式自适应 EM 分析。
- 作者报告：作者机构摘要报告参考实现四条迹线完整密钥恢复；pqm4 实现依优化设置为 8 至 960 条。
- 限制与下一步：四条只对应特定参考实现，不能推广所有 Kyber；2020 是预印本年，TC 卷年 2022、早期在线 2021-10。当前 ePrint 2026 修订提到代码链接更新，未执行。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://research.birmingham.ac.uk/en/publications/magnifying-side-channel-leakage-of-lattice-based-cryptosystems-wi/; https://eprint.iacr.org/2020/912; https://api.crossref.org/works/10.1109/tc.2021.3122997。
- [详细阅读记录](notes/pqc-citation-followups-and-evidence-20261113.md)
- 代码/数据核查：no author code or data executed; artifact contents not inspected；引用追踪：pending except explicitly inventoried citations。

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
- 限制与下一步：各方案恢复范围不同；BIKE 摘要仅称部分恢复，Classic McEliece 适用性未定，不能概括成全部完整恢复。 后续 PQCrypto 2022 RM/RS 论文作者质疑 HQC 分析中的固定 Reed-Muller 译码边界假设；本库只确认该批评存在，尚未独立裁决其适用范围，详见 PQC 引用证据笔记。
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

## On Exploiting Message Leakage in (Few) NIST PQC Candidates for Practical Message Recovery Attacks

- 来源：[TIFS 2022](https://doi.org/10.1109/tifs.2021.3139268)；时间标记：within rolling five-year window by publication date。
- 作者：Prasanna Ravi; Shivam Bhasin; Sujoy Sinha Roy; Anupam Chattopadhyay
- 对象：lattice KEM, LWE, LWR, ciphertext malleability；类型：attack。
- 核心想法：利用密文可塑性扩展格 PKE/KEM 的侧信道消息恢复目标。
- 作者报告：正式版本机构摘要覆盖三个决赛与六个半决赛候选，并讨论掩码和打乱变体。
- 限制与下一步：ePrint 题名另含 key recovery，摘要写三个半决赛候选；版本关联仅推定，不能把其平台和范围直接嫁接到正式版。正式摘要只支持消息恢复范围。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://tugraz.elsevierpure.com/en/publications/on-exploiting-message-leakage-in-few-nist-pqc-candidates-for-prac/; https://api.crossref.org/works/10.1109/tifs.2021.3139268; https://eprint.iacr.org/2020/1559。
- [详细阅读记录](notes/pqc-citation-followups-and-evidence-20261113.md)
- 代码/数据核查：no author code or data executed; artifact contents not inspected；引用追踪：pending except explicitly inventoried citations。

## Hertzbleed: Turning Power Side-Channel Attacks Into Remote Timing Attacks on x86

- 来源：[USENIX 2022](https://www.usenix.org/conference/usenixsecurity22/presentation/wang-yingchen)；时间标记：exact public date not yet verified。
- 作者：Yingchen Wang, University of Texas at Austin; Riccardo Paccagnella and Elizabeth Tang He, University of Illinois Urbana-Champaign; Hovav Shacham, University of Texas at Austin; Christopher W. Fletcher, University of Illinois Urbana-Champaign; David Kohlbrenner, University of Washington
- 对象：SIKE；类型：attack。
- 核心想法：研究 DVFS 如何把数据相关功耗变化转为可远程观察的执行时间差异。
- 作者报告：摘要报告 x86 上的机制分析及对恒时 SIKE 实现的选择密文攻击。
- 限制与下一步：历史 SIKE 是论文攻击对象；不能据此评价当前其他 PQC 实现的实际成本。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX session abstract。
- 代码/数据核查：not checked；引用追踪：forward citation observed; exhaustive backward/forward closure pending。

## SoK: Deep Learning-based Physical Side-channel Analysis

- 来源：[ACM Computing Surveys 2023](https://doi.org/10.1145/3569577)；时间标记：within frozen rolling window by recorded publication or author-upload date。
- 作者：Stjepan Picek; Guilherme Perin; Luca Mariot; Lichao Wu; Lejla Batina
- 对象：deep learning, physical side channels, threat models；类型：systematization。
- 核心想法：按分析阶段整理深度学习物理侧信道方法、威胁模型、弱点与开放问题。
- 作者报告：作者给出各阶段方法映射及评价建议。
- 限制与下一步：仅出版商存入 Crossref 的摘要；与 USENIX 2026 同题 SoK 的作者和出版实体不同，未建立版本关系。全文建议和引用尚待读。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://api.crossref.org/works/10.1145%2F3569577。
- [详细阅读记录](notes/usenix2025-citation-followup-versions-and-defense-20261114.md)
- 代码/数据核查：no author code/data executed; artifacts not inspected；引用追踪：pending except explicit inventories。

## Secret Key Recovery Attack on Masked and Shuffled Implementations of CRYSTALS-Kyber and Saber

- 来源：[ACNS Workshops 2023](https://doi.org/10.1007/978-3-031-41181-6_9)；时间标记：within rolling five-year window by publication date。
- 作者：Linus Backlund; Kalle Ngo; Joel Gärtner; Elena Dubrova
- 对象：Kyber, Saber, shuffling；类型：attack。
- 核心想法：直接利用 Fisher-Yates 索引泄漏恢复被打乱的消息位，并结合选择密文关系恢复长期秘密。
- 作者报告：摘要报告 Saber 长期密钥从 61,680 降至 4,608 条迹线，并演示受掩码和打乱保护的 Kyber。
- 限制与下一步：4,608 是 Saber 报告值，不能转写为 Kyber 预算；完整剖析、设备与重复次数仍待全文。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://link.springer.com/chapter/10.1007/978-3-031-41181-6_9。
- [详细阅读记录](notes/pqc-citation-followups-and-evidence-20261113.md)
- 代码/数据核查：no author code or data executed; artifact contents not inspected；引用追踪：pending except explicitly inventoried citations。

## Breaking a Fifth-Order Masked Implementation of CRYSTALS-Kyber by Copy-Paste

- 来源：[APKC 2023](https://doi.org/10.1145/3591866.3593072)；时间标记：within rolling five-year window by publication date。
- 作者：Elena Dubrova; Kalle Ngo; Joel Gärtner; Ruize Wang
- 对象：Kyber, higher-order masking, deep learning；类型：attack。
- 核心想法：用 recursive learning 从较低阶模型迁移部分权重，研究最高五阶掩码 Kyber 的消息位恢复。
- 作者报告：正式版本的机构索引摘要报告 ARM Cortex-M4 上消息位恢复概率高于 99%。
- 限制与下一步：这是消息位概率，不是完整共享密钥或私钥成功率。正式作者四人，ePrint 三人；版本关联仅推定。机构页面直接访问为挑战页，读到的是完整摘要的搜索索引快照。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://kth.diva-portal.org/smash/person.jsf?faces-redirect=true&language=sv&pid=authority-person%3A60095&searchType=SIMPLE; https://api.crossref.org/works/10.1145/3591866.3593072; https://eprint.iacr.org/2022/1713。
- [详细阅读记录](notes/pqc-citation-followups-and-evidence-20261113.md)
- 代码/数据核查：no author code or data executed; artifact contents not inspected；引用追踪：pending except explicitly inventoried citations。

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

## Improved Power Analysis Attacks on Falcon

- 来源：[EUROCRYPT 2023](https://doi.org/10.1007/978-3-031-30634-1_19)；时间标记：within frozen rolling window。
- 作者：Shiduo Zhang; Xiuhan Lin; Yang Yu; Weijia Wang
- 对象：Falcon-512, Mitaka, Gaussian sampler, covariance, sign leakage；类型：attack。
- 核心想法：以协方差谱分解改进基本采样泄漏利用，并研究整数采样的随机符号泄漏。
- 作者报告：正式摘要分列 220000 traces/约 25% 成功率、170000 traces 的符号路线，以及两泄漏组合的 45000 signature measurements。
- 限制与下一步：三种预算和成功条件不可混合；仅摘要明确了 Cortex-M4 漏点，完整恢复的测量/模拟划分仍待正文。IACR 作者幻灯选读不代替论文全文。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://link.springer.com/chapter/10.1007/978-3-031-30634-1_19。
- [详细阅读记录](notes/masking-foundations-gaussian-timing-and-falcon-20261114.md)
- 代码/数据核查：no author code or data executed; artifact completeness not inspected；引用追踪：pending except selected verified Gaussian follow-up。

## A Shared Key Recovery Attack on a Masked Implementation of CRYSTALS-Kyber’s Encapsulation Algorithm

- 来源：[FPS 2023](https://doi.org/10.1007/978-3-031-57537-2_26)；时间标记：within rolling five-year window by publication date。
- 作者：Ruize Wang; Elena Dubrova
- 对象：Kyber, encapsulation, masking；类型：attack。
- 核心想法：用集成模型聚合和枚举研究一阶掩码 Kyber-768 封装中的共享密钥恢复。
- 作者报告：摘要报告 Cortex-M4 上跨剖析设备的单迹线完整共享密钥恢复平均概率 91%。
- 限制与下一步：封装不是解封装，共享密钥不是长期私钥；单迹线目标观察仍需剖析与枚举。FPS 2023 会议、2024 出版分开记录。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://link.springer.com/chapter/10.1007/978-3-031-57537-2_26。
- [详细阅读记录](notes/pqc-citation-followups-and-evidence-20261113.md)
- 代码/数据核查：no author code or data executed; artifact contents not inspected；引用追踪：pending except explicitly inventoried citations。

## An End-to-end Plaintext-based Side-channel Collision Attack without Trace Segmentation

- 来源：[IACR ePrint 2023](https://eprint.iacr.org/2023/1109)；时间标记：within frozen rolling window by recorded publication or author-upload date。
- 作者：Lichao Wu; Sébastien Tiran; Guilherme Perin; Stjepan Picek
- 对象：collision attacks, plaintext labels, deep learning；类型：attack。
- 核心想法：记录不切割迹线的明文标签碰撞分析预印本。
- 作者报告：预印本摘要报告其考虑设置中成功率 53% 至 100%，训练时间约两小时至十分钟。
- 限制与下一步：与 CiC 2024 标题、作者及方法相近，但没有显式发表链接，只标记推定版本；正式摘要时间数字不同。成功率对象及绝对密钥恢复要求未读。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://eprint.iacr.org/2023/1109。
- [详细阅读记录](notes/usenix2025-citation-followup-versions-and-defense-20261114.md)
- 代码/数据核查：no author code/data executed; artifacts not inspected；引用追踪：pending except explicit inventories。

## Lightweight but Not Easy: Side-channel Analysis of the Ascon Authenticated Cipher on a 32-bit Microcontroller

- 来源：[IACR ePrint 2023](https://eprint.iacr.org/2023/1598)；时间标记：within frozen rolling window by recorded publication or author-upload date。
- 作者：Léo Weissbart; Stjepan Picek
- 对象：Ascon, CPA, DLSCA, multi-task learning；类型：attack。
- 核心想法：比较 32 位微控制器上参考与受保护 Ascon 的潜在泄漏函数和攻击效果。
- 作者报告：摘要报告参考实现完整密钥约需 8000 条 CPA 或 1000 条 DL 迹线；保护实现 DL 用 800 条恢复部分密钥。
- 限制与下一步：保护实现的多任务模型未能泛化到全部部分密钥，不能写成其完整密钥恢复；二阶 CPA 失败也不是普遍安全证明。版本与保护机制细节待正文。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://eprint.iacr.org/2023/1598。
- [详细阅读记录](notes/usenix2025-citation-followup-versions-and-defense-20261114.md)
- 代码/数据核查：no author code/data executed; artifacts not inspected；引用追踪：pending except explicit inventories。

## Invited Paper: Machine Learning Based Blind Side-Channel Attacks on PQC-Based KEMs - A Case Study of Kyber KEM

- 来源：[ICCAD 2023](https://doi.org/10.1109/iccad57390.2023.10323721)；时间标记：within frozen rolling window by recorded publication or author-upload date。
- 作者：Prasanna Ravi; Dirmanto Jap; Shivam Bhasin; Anupam Chattopadhyay
- 对象：Kyber, blind SCA, pointwise multiplication；类型：attack。
- 核心想法：利用解密逐点乘法泄漏，在未知密文的条件下分析 Kyber 秘密。
- 作者报告：作者关联的 ICCAD 小修订摘要报告 Cortex-M4 pqm4 参考实现上，使用足够准确的 HW 分类器，数百至数千条迹线恢复完整密钥。
- 限制与下一步：正式 IEEE 摘要未直接读取；科学内容来自明确关联的作者小修订摘要。分类器准确性、建立成本及完整恢复流程仍待正文，不是无剖析成本或所有 ML-KEM 实现的保证。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://api.crossref.org/works/10.1109%2FICCAD57390.2023.10323721; https://eprint.iacr.org/2024/169。
- [详细阅读记录](notes/usenix2025-citation-followup-versions-and-defense-20261114.md)
- 代码/数据核查：no author code/data executed; artifacts not inspected；引用追踪：pending except explicit inventories。

## A side-channel attack on a masked and shuffled software implementation of Saber

- 来源：[JCEN 2023](https://doi.org/10.1007/s13389-023-00315-3)；时间标记：within rolling five-year window by publication date。
- 作者：Kalle Ngo; Elena Dubrova; Thomas Johansson
- 对象：Saber, masking, shuffling；类型：attack_extension。
- 核心想法：扩展 ASHES 2021 的掩码与打乱 Saber 功耗分析，增加模型解释与泄漏汇编指令分析。
- 作者报告：摘要保留 257N/24×257N、实验 N=10，以及 80% 剖析与 20% 目标设备校准迹线；引言明确扩展关系。
- 限制与下一步：不能把期刊版当作独立复现实验；只读摘要、引言贡献段及参考文献 41，尚未逐项检查新增汇编分析和完整结果。
- 阅读层级：selected_full_text_sections；来源：https://link.springer.com/article/10.1007/s13389-023-00315-3。
- 已读章节：Publisher HTML abstract, introduction Our contributions paragraph and reference 41; remaining 62 references not systematically screened; detailed assembly/results sections not fully reviewed.
- [详细阅读记录](notes/pqc-citation-followups-and-evidence-20261113.md)
- 代码/数据核查：no author code or data executed; artifact contents not inspected；引用追踪：selected reference 41 of 63 linked and explicit conference extension verified; other references and forward tracing pending。

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

## Low-Cost Shuffling Countermeasures Against Side-Channel Attacks for NTT-Based Post-Quantum Cryptography

- 来源：[TCAD 2023](https://doi.org/10.1109/tcad.2022.3174142)；时间标记：within rolling five-year window。
- 作者：Zhaohui Chen; Yuan Ma; Jiwu Jing
- 对象：NTT, lattice-based PQC；类型：countermeasure。
- 核心想法：把嵌套 NTT 循环改为单层控制，打乱系数索引与网络执行顺序。
- 作者报告：IEEE 摘要报告 FPGA 资源开销约 9%，性能影响较小。
- 限制与下一步：当前仅摘要与元数据；具体随机熵、攻击预算和联合/高阶攻击条件待全文。2022 是在线年，卷期为 2023 年 42(1)。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/9772079/。
- [详细阅读记录](notes/kyber-shuffle-followups-and-evidence-20261113.md)
- 代码/数据核查：not inspected; no author code executed；引用追踪：pending except explicitly linked references。

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

## Side-channel Analysis of Lattice-based Post-quantum Cryptography: Exploiting Polynomial Multiplication

- 来源：[ACM TECS 2024](https://doi.org/10.1145/3569420)；时间标记：within frozen rolling window; publication and version dates retained。
- 作者：Catinca Mujdei; Lennert Wouters; Angshuman Karmakar; Arthur Beckers; Jose Maria Bermudo Mera; Ingrid Verbauwhede
- 对象：Kyber, Saber, NTRU, Toom-Cook, NTT, CPA, Cortex-M4；类型：polynomial_multiplication_side_channel。
- 核心想法：比较 Toom-Cook 与 NTT 点乘结构对非剖析 CPA 成本的影响。
- 作者报告：接受稿 §5 在 pqm4/STM32F415 上评价，Kyber 段报告 200 条覆盖多项式乘法的轨迹及每对系数约五分钟。
- 限制与下一步：采集不覆盖完整解封装；不同算法使用不同输入和搜索策略。作者接受稿 26 页，正式版 23 页，作者次序/姓名形式也不同；未声称文本等价。
- 阅读层级：selected_full_text_sections；来源：https://imec-publications.be/entities/publication/b5e5291a-f041-489a-9274-fba6b0da02e3。
- 已读章节：接受稿第 1 页摘要、第 18–20 页 §5.1–5.3 与第 20 页结论开头；不是正式版全文精读。
- [详细阅读记录](notes/kyber-multiplication-and-shuffling-20261113.md)
- 代码/数据核查：not inspected；引用追踪：pending。

## Breaking DPA-Protected Kyber via the Pair-Pointwise Multiplication

- 来源：[ACNS 2024](https://doi.org/10.1007/978-3-031-54773-7_5)；时间标记：within frozen rolling window; publication and version dates retained。
- 作者：Estuardo Alpirez Bock; Gustavo Banegas; Chris Brzuska; Łukasz Chmielewski; Kirthivaasan Puniamurthy; Milan Šorf
- 对象：Kyber, incomplete NTT, masked multiplication, templates, mkm4；类型：template_side_channel。
- 核心想法：研究不完全 NTT 中系数重复使用，比较已知密文模板方法的模拟与实测表现。
- 作者报告：摘要的 13,316 模板和 σ≤0.3 是 HW 模拟；实测原方法未达预期，加入在线模板式扩展后报告单次多项式乘法恢复 128 对系数。
- 限制与下一步：一条轨迹不含剖析成本；单多项式的 128 对系数不自动等于全部 Kyber 私钥。ePrint PDF HTTP 403，本批不声称读到正文。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://link.springer.com/chapter/10.1007/978-3-031-54773-7_5。
- 代码/数据核查：author repository README retrieved: https://github.com/crocs-muni/Attack_Kyber_ACNS2024 ; README declares source, example traces and simulations using mkm4; completeness not checked and nothing executed；引用追踪：pending。

## One for All, All for Ascon: Ensemble-Based Deep Learning Side-Channel Analysis

- 来源：[ACNS Workshops 2024](https://doi.org/10.1007/978-3-031-61486-6_9)；时间标记：within frozen rolling window by recorded publication or author-upload date。
- 作者：Azade Rezaeezade; Abraham Basurto-Becerra; Léo Weissbart; Guilherme Perin
- 对象：Ascon, ensembles, DLSCA；类型：attack。
- 核心想法：将五个 MLP 或 CNN 组成集成，研究两种软件 Ascon 实现。
- 作者报告：作者摘要报告受保护实现少于 3000 条、未保护实现少于 100 条迹线识别秘密密钥。
- 限制与下一步：摘要层级的密钥恢复主张，不能与 2023 预印本的部分密钥结果混并；保护细节、训练预算、完整恢复判据及最终 Ascon 标准对应待正文。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://link.springer.com/chapter/10.1007/978-3-031-61486-6_9; https://api.crossref.org/works/10.1007%2F978-3-031-61486-6_9。
- [详细阅读记录](notes/usenix2025-citation-followup-versions-and-defense-20261114.md)
- 代码/数据核查：no author code/data executed; artifacts not inspected；引用追踪：pending except explicit inventories。

## The Need for MORE: Unsupervised Side-Channel Analysis with Single Network Training and Multi-output Regression

- 来源：[COSADE 2024](https://doi.org/10.1007/978-3-031-57543-3_7)；时间标记：within frozen rolling window by recorded publication or author-upload date。
- 作者：Ioana Savu; Marina Krček; Guilherme Perin; Lichao Wu; Stjepan Picek
- 对象：non-profiling SCA, multi-output regression, ensembles；类型：attack methodology。
- 核心想法：改进 MOR 的损失、区分器与验证集用法，并结合集成和数据增强。
- 作者报告：摘要报告 MORE 改善非剖析攻击表现及候选区分可靠性。
- 限制与下一步：非剖析不等于未知明文/密文的盲分析；验证集如何构造、是否使用评估真值及总选择成本待正文。已初筛全部 27 条出版商参考文献，尚未递归闭合。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://link.springer.com/chapter/10.1007/978-3-031-57543-3_7; https://api.crossref.org/works/10.1007%2F978-3-031-57543-3_7。
- [详细阅读记录](notes/usenix2025-citation-followup-versions-and-defense-20261114.md)
- 代码/数据核查：no author code/data executed; artifacts not inspected；引用追踪：All 27 publisher entries screened: 3 linked, 19 pending discoveries, 5 provisional background. No recursive or forward closure.。

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

## Leakage Model-flexible Deep Learning-based Side-channel Analysis

- 来源：[CiC 2024](https://doi.org/10.62056/ay4c3txol7)；时间标记：within frozen rolling window by recorded publication or author-upload date。
- 作者：Lichao Wu; Azade Rezaeezade; Amir Ali-pour; Guilherme Perin; Stjepan Picek
- 对象：multi-bit labels, DLSCA, profiling；类型：leakage modeling。
- 核心想法：将标签拆成逐比特分类，尝试适配多种泄漏函数，并联合学习多个子密钥字节。
- 作者报告：作者报告在四个数据集恢复全部 16 个密钥字节，常规泄漏标签在这些设置下失败。
- 限制与下一步：需要剖析测量和标签；分别分类不证明比特条件独立；只读摘要，数据集配置、选择预算及完整成功率仍待正文。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://api.crossref.org/works/10.62056%2Fay4c3txol7; https://cic.iacr.org/p/1/3/41。
- [详细阅读记录](notes/usenix2025-citation-followup-versions-and-defense-20261114.md)
- 代码/数据核查：no author code/data executed; artifacts not inspected；引用追踪：pending except explicit inventories。

## Plaintext-based Side-channel Collision Attack

- 来源：[CiC 2024](https://doi.org/10.62056/a36cy7qiu)；时间标记：within frozen rolling window by recorded publication or author-upload date。
- 作者：Lichao Wu; Sébastien Tiran; Guilherme Perin; Stjepan Picek
- 对象：collision attacks, plaintext labels, deep learning；类型：attack。
- 核心想法：用已知明文标签学习泄漏表示，以比较表示取代预先切割迹线来推断密钥差。
- 作者报告：正式摘要报告同时取得密钥差并通过纠错改善结果；所述训练时间例子由约三小时降至五分钟。
- 限制与下一步：密钥差不是自动恢复绝对完整密钥；候选预印本写约两小时到十分钟，版本关联仅推定，差异原因未核。模型训练预算及所需已知输入仍待正文。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://api.crossref.org/works/10.62056%2Fa36cy7qiu; https://doi.org/10.62056/a36cy7qiu; https://eprint.iacr.org/2023/1109。
- [详细阅读记录](notes/usenix2025-citation-followup-versions-and-defense-20261114.md)
- 代码/数据核查：no author code/data executed; artifacts not inspected；引用追踪：pending except explicit inventories。

## Protecting Confidential Virtual Machines from Hardware Performance Counter Side Channels

- 来源：[DSN 2024](https://doi.org/10.1109/DSN58291.2024.00031)；时间标记：within frozen rolling window by recorded publication or author-upload date。
- 作者：Xiaoxuan Lou; Kangjie Chen; Guowen Xu; Han Qiu; Shangwei Guo; Tianwei Zhang
- 对象：HPC, SEV, differential privacy, instruction noise；类型：countermeasure。
- 核心想法：在 SEV VM 内剖析性能事件、搜索指令噪声，并用差分隐私机制指导扰动。
- 作者报告：作者在网站、DNN 模型与按键任务报告准确率由约 90% 降至约 2%；正文所列网站/推断时间开销为 3.18%–4.95%，另有离线剖析成本。
- 限制与下一步：主要威胁模型为被动 HPC 观察及诚实但好奇的主机；细粒度密码密钥窃取防护被列为未来工作。逐时间片保证、完整序列预算及有符号噪声到指令扰动的实现映射需进一步审计；重复观察的固定秘密相关噪声建议未经本库验证。
- 阅读层级：selected_full_text_sections；来源：https://dsn2024uq.github.io/Proceedings/pdfs/DSN2024-6rvE3SSpzFYmysif75Dkid/410500a195/410500a195.pdf。
- 已读章节：Official DSN PDF pages 1-3, 9-10 and 12: abstract, introduction, threat model, DP mechanisms and implementation, profiling costs, discussion and conclusion. Remaining sections, proofs and bibliography not fully reviewed.
- [详细阅读记录](notes/usenix2025-citation-followup-versions-and-defense-20261114.md)
- 代码/数据核查：no author code/data executed; artifacts not inspected；引用追踪：pending except explicit inventories。

## Securing CRYSTALS-Kyber in FPGA Using Duplication and Clock Randomization

- 来源：[Design & Test 2024](https://doi.org/10.1109/mdat.2023.3298805)；时间标记：within rolling five-year window。
- 作者：Michail Moraitis; Yanning Ji; Martin Brisfors; Elena Dubrova; Niklas Lindskog; Håkan Englund
- 对象：Kyber；类型：countermeasure。
- 核心想法：通过复制密码核与时钟随机化保护 FPGA Kyber。
- 作者报告：KTH 作者摘要报告在 Xing 等轻量实现上构建防护，并评价深度学习侧信道抵抗性。
- 限制与下一步：IEEE 摘要字段实际是编辑按语；作者摘要仅经机构页面的搜索索引取得，直接访问受限。攻击预算和全部配置尚未核查，不能推出普遍防护或故障安全。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://kth.diva-portal.org/smash/person.jsf?pid=authority-person%3A80558; https://xplorestaging.ieee.org/document/10193851/。
- [详细阅读记录](notes/kyber-shuffle-followups-and-evidence-20261113.md)
- 代码/数据核查：not inspected; no author code executed；引用追踪：selected backward/forward relation verified; complete tracing pending。

## Breaking SCA-Protected CRYSTALS-Kyber with a Single Trace

- 来源：[HOST 2024](https://doi.org/10.1109/host55342.2024.10545390)；时间标记：within rolling five-year window by publication date。
- 作者：Sönke Jendral; Kalle Ngo; Ruize Wang; Elena Dubrova
- 对象：Kyber, masking, shuffling, fault injection；类型：combined_fault_and_side_channel。
- 核心想法：结合电压故障绕过打乱与剖析式深度学习功耗分析，恢复消息或共享密钥。
- 作者报告：作者报告 ARM Cortex-M4 上跳过打乱后使用 HW 模型和部分枚举改善恢复。
- 限制与下一步：不是纯被动单迹线功耗攻击，恢复对象不是已确认的长期私钥。完整训练与故障预算未读；正式摘要来自机构搜索索引快照，直接页面为挑战页。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://kth.diva-portal.org/smash/person.jsf?pid=authority-person%3A111623; https://api.crossref.org/works/10.1109/HOST55342.2024.10545390。
- [详细阅读记录](notes/pqc-citation-followups-and-evidence-20261113.md)
- 代码/数据核查：no author code or data executed; artifact contents not inspected；引用追踪：pending except explicitly inventoried citations。

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

## Machine Learning based Blind Side-Channel Attacks on PQC-based KEMs - A Case Study of Kyber KEM

- 来源：[IACR ePrint 2024](https://eprint.iacr.org/2024/169)；时间标记：within frozen rolling window by recorded publication or author-upload date。
- 作者：Prasanna Ravi; Dirmanto Jap; Shivam Bhasin; Anupam Chattopadhyay
- 对象：Kyber, blind SCA, pointwise multiplication；类型：attack。
- 核心想法：保存 ICCAD 2023 盲分析的作者小修订版本及其实际能力前提。
- 作者报告：摘要报告在合适 HW 分类器条件下，通过参考 Kyber 的逐点乘法泄漏实现完整密钥恢复。
- 限制与下一步：与正式记录是版本关系，不是独立复现；PDF 403，分类器训练与总测量成本未核。作者 DOI 链接缺少文章后缀，不能直接当作完整 DOI。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://eprint.iacr.org/2024/169。
- [详细阅读记录](notes/usenix2025-citation-followup-versions-and-defense-20261114.md)
- 代码/数据核查：no author code/data executed; artifacts not inspected；引用追踪：pending except explicit inventories。

## OT-PCA: New Key-Recovery Plaintext-Checking Oracle Based Side-Channel Attacks on HQC with Offline Templates

- 来源：[IACR ePrint 2024](https://eprint.iacr.org/2024/1715)；时间标记：within frozen rolling window by recorded publication or author-upload date。
- 作者：Haiyue Dong; Qian Guo
- 对象：HQC, PC oracle, offline templates；类型：attack。
- 核心想法：用公开 HQC 译码器离线建立软信息模板，从单个 PC oracle 输出约束多个秘密位置。
- 作者报告：摘要报告模拟中 hqc-128 查询数降低 2.4 倍，oracle 准确率 95% 时降低 7.6 倍，并有 Cortex-M4 功耗评估。
- 限制与下一步：oracle 调用数不等于迹线、剖析或校准成本；只读摘要，预印本 PDF 403。TEEcorrelate 实际引用此版本，不直接替换成正式 TCHES 条目。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://eprint.iacr.org/2024/1715。
- [详细阅读记录](notes/usenix2025-citation-followup-versions-and-defense-20261114.md)
- 代码/数据核查：no author code/data executed; artifacts not inspected；引用追踪：pending except explicit inventories。

## Single-trace side-channel attacks on MAYO exploiting leaky modular multiplication

- 来源：[IACR ePrint 2024](https://eprint.iacr.org/2024/1850)；时间标记：within rolling five-year window by publication date。
- 作者：Sönke Jendral; Elena Dubrova
- 对象：MAYO, multivariate signatures；类型：attack。
- 核心想法：从模乘功耗恢复 oil space 向量，再结合代数关系恢复 MAYO 秘密。
- 作者报告：当前 ePrint 摘要报告 Cortex-M4 两种单迹线方法的成功率为 99.9% 与 91.6%。
- 限制与下一步：正式版本机构摘要为 99.4% 与 93.1%，两组分别保留，差异原因未核实。单迹线不代表零剖析或零代数求解成本；PDF 403，未读完整预算。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://eprint.iacr.org/2024/1850。
- [详细阅读记录](notes/pqc-citation-followups-and-evidence-20261113.md)
- 代码/数据核查：no author code or data executed; artifact contents not inspected；引用追踪：pending except explicitly inventoried citations。

## Train Wisely: Multifidelity Bayesian Optimization Hyperparameter Tuning in Side-Channel Analysis

- 来源：[IACR ePrint 2024](https://eprint.iacr.org/2024/170)；时间标记：within frozen rolling window by recorded publication or author-upload date。
- 作者：Trevor Yap Hong Eng; Shivam Bhasin; Léo Weissbart
- 对象：BOHB, DLSCA, hyperparameter search；类型：hyperparameter optimization。
- 核心想法：保留 Train Wisely 的作者版本及其预算化搜索目标。
- 作者报告：摘要在四个公开数据集研究 BOHB 与 ge+ntge，并报告 CTF2018 identity 模型成功。
- 限制与下一步：作者明确写 SAC 2024；正式版标题与 Trevor 作者姓名形式不同，不是独立实验。完整搜索成本与正文差异仍待核对。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://eprint.iacr.org/2024/170。
- [详细阅读记录](notes/usenix2025-citation-followup-versions-and-defense-20261114.md)
- 代码/数据核查：no author code/data executed; artifacts not inspected；引用追踪：pending except explicit inventories。

## mUOV: Masking the Unbalanced Oil and Vinegar Digital Signature Scheme at First- and Higher-Order

- 来源：[IACR ePrint 2024](https://eprint.iacr.org/2024/1875)；时间标记：within frozen rolling window by recorded publication or author-upload date。
- 作者：Suparna Kundu; Quinten Norga; Angshuman Karmakar; Uttam Kumar Ojha; Anindya Ganguly; Ingrid Verbauwhede
- 对象：UOV, MQ signatures, masking；类型：masking。
- 核心想法：保存 mUOV 的作者修订版及 CCS 2025 关联。
- 作者报告：作者摘要提出 UOV 任意阶掩码、探针模型证明及 TVLA 评估。
- 限制与下一步：明确声明 CCS 2025 的 minor revision；与正式条目不是独立复现。实测与机械验证边界见正式条目的选读笔记，NIST 稿与最终 ACM 未逐字比对。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://eprint.iacr.org/2024/1875。
- [详细阅读记录](notes/ccs2025-masking-contracts-and-observation-boundaries-20261114.md)
- 代码/数据核查：no author code/data executed; artifact completeness not inspected；引用追踪：pending except explicit inventory。

## OccPoIs: Points of Interest Based on Neural Network’s Key Recovery in Side-Channel Analysis Through Occlusion

- 来源：[INDOCRYPT 2024](https://doi.org/10.1007/978-3-031-80311-6_1)；时间标记：within frozen rolling window by recorded publication or author-upload date。
- 作者：Trevor Yap; Stjepan Picek; Shivam Bhasin
- 对象：DLSCA, occlusion, template attacks, first-order masking；类型：feature selection。
- 核心想法：用 Key Guessing Occlusion 寻找支撑网络密钥推断的采样点，再用于模板分析。
- 作者报告：作者报告在考虑的同步数据集及一阶掩码数据上取得可用点集，ASCADf 中优于所比选点方法。
- 限制与下一步：网络依赖点不自动等于物理因果节点；摘要的 minimal 不构成全局最小或唯一性证明。掩码真值不可见不等于评估密钥真值不可见，选择预算待正文。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://link.springer.com/chapter/10.1007/978-3-031-80311-6_1; https://api.crossref.org/works/10.1007%2F978-3-031-80311-6_1。
- [详细阅读记录](notes/usenix2025-citation-followup-versions-and-defense-20261114.md)
- 代码/数据核查：no author code/data executed; artifacts not inspected；引用追踪：pending except explicit inventories。

## Regularizers to the rescue: fighting overfitting in deep learning-based side-channel analysis

- 来源：[JCEN 2024](https://doi.org/10.1007/s13389-024-00361-5)；时间标记：within frozen rolling window by recorded publication or author-upload date。
- 作者：Azade Rezaeezade; Lejla Batina
- 对象：DLSCA, regularization, overfitting；类型：evaluation methodology。
- 核心想法：比较 L1、L2、dropout 与 early stopping 在八种数据/标签/拓扑组合中的作用。
- 作者报告：作者在其随机选定模型上报告 L1/L2 总体较有效，关注训练时间时 early stopping 较好。
- 限制与下一步：不是任意数据、模型或固定公平预算下的普遍排名；仅摘要，超参数选择与重复统计仍待正文。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://api.crossref.org/works/10.1007%2Fs13389-024-00361-5; https://link.springer.com/article/10.1007/s13389-024-00361-5。
- [详细阅读记录](notes/usenix2025-citation-followup-versions-and-defense-20261114.md)
- 代码/数据核查：no author code/data executed; artifacts not inspected；引用追踪：pending except explicit inventories。

## Masking the GLP Lattice-Based Signature Scheme at Any Order

- 来源：[Journal of Cryptology 2024](https://doi.org/10.1007/s00145-023-09485-z)；时间标记：within frozen 2021-11-12 to 2026-11-12 window; publication/version dates retained。
- 作者：Gilles Barthe; Sonia Belaïd; Thomas Espitau; Pierre-Alain Fouque; Benjamin Grégoire; Mélissa Rossi; Mehdi Tibouchi
- 对象：GLP, lattice signatures, masking；类型：countermeasure。
- 核心想法：GLP 任意阶掩码工作的期刊版本，保留公开输出和份额转换的模型条件。
- 作者报告：作者页面明确关联 EUROCRYPT 2018；期刊摘要报告形式模型与概念实现。
- 限制与下一步：在线日期为 2023-11-29，卷年为 2024；不能当成与 2018 版无关的新研究或已核验全文等价。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://link.springer.com/article/10.1007/s00145-023-09485-z。
- 代码/数据核查：not checked；引用追踪：in_progress; selected references only。

## Train Wisely: Multifidelity Bayesian Optimization Hyperparameter Tuning in Deep Learning-Based Side-Channel Analysis

- 来源：[SAC 2024](https://doi.org/10.1007/978-3-031-82841-6_12)；时间标记：within frozen rolling window by recorded publication or author-upload date。
- 作者：Trevor Yap; Shivam Bhasin; Léo Weissbart
- 对象：BOHB, DLSCA, hyperparameter search；类型：hyperparameter optimization。
- 核心想法：把多保真贝叶斯 HyperBand 与组合 GE 目标用于有预算的超参数搜索。
- 作者报告：正式摘要在四个公开数据集比较，并报告 CTF2018 的 HW/identity 标签实验结果。
- 限制与下一步：最低目标迹线数不能替代总训练、搜索、验证成本；搜索与最终评估隔离及预算定义待全文。SAC 2024 会议、2025 正式出版分别记录。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://link.springer.com/chapter/10.1007/978-3-031-82841-6_12; https://api.crossref.org/works/10.1007%2F978-3-031-82841-6_12; https://eprint.iacr.org/2024/170。
- [详细阅读记录](notes/usenix2025-citation-followup-versions-and-defense-20261114.md)
- 代码/数据核查：no author code/data executed; artifacts not inspected；引用追踪：pending except explicit inventories。

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

## PoMMES: Prevention of Micro-architectural Leakages in Masked Embedded Software

- 来源：[TCHES 2024](https://doi.org/10.46586/tches.v2024.i3.342-376)；时间标记：within frozen rolling window by recorded publication or author-upload date。
- 作者：Jannik Zeitschner; Amir Moradi
- 对象：PoMMES, masking, register allocation, Cortex-M0+；类型：compiler countermeasure。
- 核心想法：用微架构感知的寄存器分配，把高层掩码函数编译为避免份额意外重组合的汇编。
- 作者报告：作者摘要报告任意阶方法面向顺序执行处理器，并提供模拟与 Cortex-M0+ 功耗泄漏评估。
- 限制与下一步：仅读出版商提交的摘要；通用微架构模型及各阶实测范围待正文，不把理论阶数直接当作全部高阶硬件验证。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://api.crossref.org/journals/2569-2925/works?filter=from-pub-date%3A2020-01-01%2Cuntil-pub-date%3A2026-11-12&rows=1000&cursor=%2A。
- [详细阅读记录](notes/ccs2025-masking-contracts-and-observation-boundaries-20261114.md)
- 代码/数据核查：no author code/data executed; artifact completeness not inspected；引用追踪：pending except explicit inventory。

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

## A Configurable CRYSTALS-Kyber Hardware Implementation with Side-Channel Protection

- 来源：[TECS 2024](https://doi.org/10.1145/3587037)；时间标记：within rolling five-year window。
- 作者：Arpan Jati; Naina Gupta; Anupam Chattopadhyay; Somitra Kumar Sanadhya
- 对象：Kyber；类型：countermeasure。
- 核心想法：组合指令随机化、FSM 保护与故障检测哈希，提供可配置 Kyber 硬件。
- 作者报告：正式出版商提交的摘要报告低于 5% 防护开销以及 200K 迹线 TVLA 评估。
- 限制与下一步：该迹线规模下未检出不等于无泄漏；TECS 正文访问 403。同题 ePrint 摘要没有 200K TVLA 表述，不能互换版本证据。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://api.crossref.org/works/10.1145/3587037; https://eprint.iacr.org/2021/1189。
- [详细阅读记录](notes/kyber-shuffle-followups-and-evidence-20261113.md)
- 代码/数据核查：not inspected; no author code executed；引用追踪：pending except explicitly linked references。

## Side-channel and Fault-injection attacks over Lattice-based Post-quantum Schemes (Kyber, Dilithium): Survey and New Results

- 来源：[TECS 2024](https://doi.org/10.1145/3603170)；时间标记：within rolling five-year window by publication date。
- 作者：Prasanna Ravi; Anupam Chattopadhyay; Jan Pieter D’Anvers; Anubhab Baksi
- 对象：Kyber, Dilithium, fault injection；类型：survey_and_countermeasures。
- 核心想法：分类格 PQC 的侧信道与故障攻击，整合多种定制防护。
- 作者报告：作者报告在 pqm4 Cortex-M4 与 liboqs Raspberry Pi 3 Model B Plus/Cortex-A53 上的防护性能。
- 限制与下一步：出版者提交给 Crossref 的摘要可读，ACM 页面 403；性能开销和综合防护主张不等于抵抗所有物理攻击的证明。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://api.crossref.org/works/10.1145/3603170。
- [详细阅读记录](notes/pqc-citation-followups-and-evidence-20261113.md)
- 代码/数据核查：no author code or data executed; artifact contents not inspected；引用追踪：pending except explicitly inventoried citations。

## Zero-Value Filtering for Accelerating Non-Profiled Side-Channel Attack on Incomplete NTT-Based Implementations of Lattice-Based Cryptography

- 来源：[TIFS 2024](https://doi.org/10.1109/tifs.2024.3359890)；时间标记：within rolling five-year window。
- 作者：Tolun Tosun; Erkay Savas
- 对象：Kyber, Dilithium；类型：attack。
- 核心想法：利用零值条件分离不完整 NTT 乘法中的系数假设，并结合逆 NTT 验证与修正。
- 作者报告：在 MAX32520 Cortex-M4F 上采集 EM，作者报告未保护 Kyber 的运行时间最高加速 1915 倍，并评估自建一阶掩码 Kyber。
- 限制与下一步：1915 倍是指定基线下的计算时间加速，不是迹线减少；过滤迹线预算另计。Dilithium 使用载体素数 769 的特定实现；掩码基线仅实测前两个系数、整向量耗时含外推。
- 阅读层级：selected_full_text_sections；来源：https://research.sabanciuniv.edu/id/eprint/49123/1/Zero-Value.pdf; https://research.sabanciuniv.edu/id/eprint/49123/。
- 已读章节：Accepted manuscript PDF p1 abstract; p5 section VI; pp9–12 experimental setup/results/conclusion; tables V–VI visually checked on pp10–11. Algorithm section VII and complete bibliography not read.
- [详细阅读记录](notes/kyber-shuffle-followups-and-evidence-20261113.md)
- 代码/数据核查：not inspected; no author code executed；引用追踪：pending except explicitly linked references。

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

## An Empirical Study Measuring In-The-Wild Cryptographic Microarchitectural Side-Channel Patches

- 来源：[CCS 2025](https://doi.org/10.1145/3719027.3744881)；时间标记：within frozen rolling window by recorded publication or author-upload date。
- 作者：Sen Deng; Zhibo Liu; Shuai Wang; Yinqian Zhang
- 对象：cryptographic libraries, patches, cache, ciphertext leakage；类型：evaluation。
- 核心想法：整理真实密码库的微架构侧信道补丁，并用污点分析与符号执行评估。
- 作者报告：作者报告 SideBench 含 OpenSSL、wolfSSL、MbedTLS 的 165 个补丁，其中 25 个仍有泄漏；不同泄漏模型之间可能发生修复冲突。
- 限制与下一步：仅读作者机构摘要；具体版本、漏洞判据及补丁性能基线尚待读，不能当作当前所有库版本均受影响。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://researchportal.hkust.edu.hk/en/publications/an-empirical-study-measuring-in-the-wild-cryptographic-microarchi/。
- [详细阅读记录](notes/ccs2025-masking-contracts-and-observation-boundaries-20261114.md)
- 代码/数据核查：no author code/data executed; artifact completeness not inspected；引用追踪：pending except explicit inventory。

## BFId: Identity Inference Attacks Utilizing Beamforming Feedback Information

- 来源：[CCS 2025](https://doi.org/10.1145/3719027.3765062)；时间标记：within frozen rolling window。
- 作者：Julian Todt; Felix Morsbach; Thorsten Strufe
- 对象：WiFi, BFI, CSI, identity inference；类型：physical privacy attack。
- 核心想法：研究 WiFi 波束成形反馈中的人体身份信息，以 BFI 感知替代或比较 CSI。
- 作者报告：作者收集 197 人数据；实际可用 BFI/CSI 人数不同。不同视角下的识别成绩不能等同于训练与测试视角不匹配时的迁移能力。
- 限制与下一步：正文中以视角 1 训练、其他视角测试的准确率均低于 5%；softmax 评估不能判断未见身份。数据并非无条件公开；请求共享与实际可用人数需保留。
- 阅读层级：selected_full_text_sections；来源：https://publikationen.bibliothek.kit.edu/1000185756/168100988。
- 已读章节：Author institutional PDF pages 1, 8, 11-12: abstract, collection/usable participants and consent, cross-perspective mismatch, empty-room control, closed-set limitations. Remaining sections and Appendix B not fully reviewed.
- [详细阅读记录](notes/ccs2025-second-pass-metrics-transfer-and-access-20261114.md)
- 代码/数据核查：no author code/data executed; completeness not verified；引用追踪：pending except explicit inventory。

## BLACKOUT: Data-Oblivious Computation with Blinded Capabilities

- 来源：[CCS 2025](https://doi.org/10.1145/3719027.3765169)；时间标记：within frozen rolling window by recorded publication or author-upload date。
- 作者：Hossam ElAtali; Merve Gülmez; Thomas Nyman; N. Asokan
- 对象：CHERI, data-oblivious computation, blinded capabilities；类型：countermeasure。
- 核心想法：扩展 CHERI 能力机制，让违反数据无关操作规则的秘密访问显式触发异常。
- 作者报告：作者在 CHERI-Toooba FPGA 软核及配套编译器、系统上实现 BLACKOUT，所选基准几何平均开销为 1.5%。
- 限制与下一步：作者明确关联的 CCS 预印本摘要；具体观察模型与异常本身的可见性仍待正文，不能推广到功耗、电磁和所有 CHERI 部署。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://arxiv.org/abs/2504.14654。
- [详细阅读记录](notes/ccs2025-masking-contracts-and-observation-boundaries-20261114.md)
- 代码/数据核查：no author code/data executed; artifact completeness not inspected；引用追踪：pending except explicit inventory。

## BOLT: Bandwidth-Optimized Lightning-Fast Oblivious Map powered by Secure HBM Accelerators

- 来源：[CCS 2025](https://doi.org/10.1145/3719027.3765069)；时间标记：within frozen rolling window by recorded publication or author-upload date。
- 作者：Yitong Guo; Hongbo Chen; Haobin Hiroki Chen; Yukui Luo; XiaoFeng Wang; Chenghong Wang
- 对象：OMAP, HBM, access patterns；类型：countermeasure。
- 核心想法：利用隔离的 HBM 作为不可观察缓存，并将执行和内存控制卸载到加速器。
- 作者报告：作者报告在 Xilinx U55C 上实现 BOLT，改善 OMAP 带宽与所选负载的初始化和查询时间。
- 限制与下一步：依赖隔离 HBM 的数据与访问轨迹不可观察这一威胁模型前提；封装困难不等于所有物理信号无泄漏。仅读作者预印本摘要。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://arxiv.org/abs/2509.01742。
- [详细阅读记录](notes/ccs2025-masking-contracts-and-observation-boundaries-20261114.md)
- 代码/数据核查：no author code/data executed; artifact completeness not inspected；引用追踪：pending except explicit inventory。

## Differentially Private Access in Encrypted Search: Achieving Privacy at a Small Cost?

- 来源：[CCS 2025](https://doi.org/10.1145/3719027.3765038)；时间标记：within frozen rolling window。
- 作者：Daniel Pöllmann; Tianxin Tang
- 对象：encrypted search, differentially private access, range queries；类型：leakage analysis。
- 核心想法：研究 DP 访问泄漏保证与查询、数据隐私之间的差别，分析两个加密范围查询方案。
- 作者报告：作者对 DO-Range 与 epsilon-OPE-Range 给出推断评估及通用访问定义，讨论分桶、分区的隐私和带宽代价。
- 限制与下一步：不是推翻 DP 定理。定义的邻接关系与只读 Find 场景有范围；所述直方图和查询恢复受分区粒度限制，不等于恢复分区内每条记录的精确值。
- 阅读层级：selected_full_text_sections；来源：https://www.research-collection.ethz.ch/server/api/core/bitstreams/f6e317c8-6025-4b80-859d-200a8ee12d9d/content。
- 已读章节：ETH-hosted PDF pages 2, 5-6 and 12 (one cover page included): abstract, read-only definition and adjacency, scheme distinctions, partition-granularity recovery and privacy/utility discussion. Full-version proofs not reviewed.
- [详细阅读记录](notes/ccs2025-second-pass-metrics-transfer-and-access-20261114.md)
- 代码/数据核查：no author code/data executed; completeness not verified；引用追踪：pending except explicit inventory。

## ExfilState: Automated Discovery of Timer-Free Cache Side Channels on ARM CPUs

- 来源：[CCS 2025](https://doi.org/10.1145/3719027.3765061)；时间标记：within frozen rolling window by recorded publication or author-upload date。
- 作者：Fabian Thomas; Michael Torres; Daniel Moghimi; Michael Schwarz
- 对象：ARM64, cache, timer-free, AES；类型：automated discovery。
- 核心想法：自动寻找将缓存状态映射到架构状态的指令序列，以绕开计时器限制。
- 作者报告：作者页面报告覆盖 160 台设备、37 种微架构，发现五种未记录通道，展示无计时器 Spectre 与 AES 恢复案例。
- 限制与下一步：仅读作者项目摘要；五种发现不等于全部都可靠可利用，作者区分其中两种的广泛可靠性。芯片条件、权限和恢复预算待正文。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://fabianthomas.de/publications/2025/thomas2025exfilstate/。
- [详细阅读记录](notes/ccs2025-masking-contracts-and-observation-boundaries-20261114.md)
- 代码/数据核查：no author code/data executed; artifact completeness not inspected；引用追踪：pending except explicit inventory。

## GhostCache: Timer- and Counter-Free Cache Attacks Exploiting Weak Coherence on RISC-V and ARM Chips

- 来源：[CCS 2025](https://doi.org/10.1145/3719027.3744833)；时间标记：within frozen rolling window by recorded publication or author-upload date。
- 作者：Yu Jin; Minghong Sun; Dongsheng Wang; Pengfei Qiu; Yinqian Zhang; Shuwen Deng
- 对象：RISC-V, ARM, instruction cache, weak coherence；类型：attack。
- 核心想法：利用一级缓存弱一致性构造无计时器、无计数器的指令缓存观察。
- 作者报告：作者报告商业与开源 RISC 处理器案例，涉及网站指纹、内核泄漏及密码密钥重建。
- 限制与下一步：仅读实验室摘要；隐蔽通道带宽、分类准确率及密钥恢复不是同一个指标，不能相互替代或推广为所有 ARM/RISC-V 芯片。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://www.thu-haslab.org/publication/2025-ghostcache/。
- [详细阅读记录](notes/ccs2025-masking-contracts-and-observation-boundaries-20261114.md)
- 代码/数据核查：no author code/data executed; artifact completeness not inspected；引用追踪：pending except explicit inventory。

## HW-Spy: Handwriting Inference by Tracing Pen-Tail Movements

- 来源：[CCS 2025](https://doi.org/10.1145/3719027.3765109)；时间标记：within frozen rolling window。
- 作者：Long Huang; Kang G. Shin
- 对象：handwriting, video, pen-tail motion；类型：optical inference。
- 核心想法：从可见笔尾的视频运动估计被遮住的笔尖轨迹并推断手写内容。
- 作者报告：作者区分个性化与未见书写者模型，分别报告摘要中最高 84.2% 和 79.5% 的手写推断结果。
- 限制与下一步：论文的 word-level 与 sentence-level 指拼写及语法校正后的字符正确率，并非整词/整句完全恢复率。需要可用笔尾视频；不同字符类别和数据划分不能混合比较。
- 阅读层级：selected_full_text_sections；来源：https://rtcl.eecs.umich.edu/rtclweb/assets/publications/2025/ccs25-huang.pdf。
- 已读章节：Author PDF pages 1, 8 and 12: abstract, Section 5.3 metric definitions and personalization distinction, leave-one-writer-out evaluation. Remaining reconstruction and attack details not fully reviewed.
- [详细阅读记录](notes/ccs2025-second-pass-metrics-transfer-and-access-20261114.md)
- 代码/数据核查：no author code/data executed; completeness not verified；引用追踪：pending except explicit inventory。

## Heracles: Chosen Plaintext Attack on AMD SEV-SNP

- 来源：[CCS 2025](https://doi.org/10.1145/3719027.3765209)；时间标记：within frozen rolling window by recorded publication or author-upload date。
- 作者：Benedict Schlüter; Christoph Wech; Shweta Shinde
- 对象：SEV-SNP, ciphertext side channel, page relocation；类型：attack。
- 核心想法：结合确定性内存重加密与虚拟机页移动能力，建立密文观察关系。
- 作者报告：作者项目摘要报告块与字节级泄漏原语，以及内核、密码密钥、口令和会话案例。
- 限制与下一步：需要恶意管理程序和特定页移动及密文观察能力；不是被动功耗攻击。项目页与论文版本的原语数量及固件适用范围尚待核对。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://heracles-attack.github.io/。
- [详细阅读记录](notes/ccs2025-masking-contracts-and-observation-boundaries-20261114.md)
- 代码/数据核查：no author code/data executed; artifact completeness not inspected；引用追踪：pending except explicit inventory。

## IOValve: Leakage-Free I/O Sandbox for Large-Scale Untrusted Data Processing

- 来源：[CCS 2025](https://doi.org/10.1145/3719027.3765121)；时间标记：within frozen rolling window by recorded publication or author-upload date。
- 作者：Sangho Lee; Jules Drean; Yue Tan; Marcus Peinado
- 对象：covert channels, network I/O, sandbox；类型：countermeasure。
- 核心想法：将 I/O 沙箱放到与计算处理器物理隔离的可编程网络设备，规整并加密网络流量。
- 作者报告：作者机构摘要报告支持 LLM 微调、批量推理和分子模拟，开销较小。
- 限制与下一步：保护依赖全部网络 I/O 被拦截和隔离边界；摘要不证明功耗、电磁等任意外部观察无泄漏。HTTP 抓取失败，完整摘要由网页工具读取并保留提取文本。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://www.microsoft.com/en-us/research/publication/iovalve-leakage-free-i-o-sandbox-for-large-scale-untrusted-data-processing/。
- [详细阅读记录](notes/ccs2025-masking-contracts-and-observation-boundaries-20261114.md)
- 代码/数据核查：no author code/data executed; artifact completeness not inspected；引用追踪：pending except explicit inventory。

## ML-Cube: Accelerating Module-Lattice-Based Cryptography using Machine Learning Accelerators with a Memory-Less Design

- 来源：[CCS 2025](https://doi.org/10.1145/3719027.3765130)；时间标记：within frozen rolling window by recorded publication or author-upload date。
- 作者：Tian Zhou; Fangyu Zheng; Zhuoyu Xie; Wenxu Tang; Guang Fan; Yijing Ning; Yi Bian; Jingqiang Lin; Jiwu Jing
- 对象：ML-KEM, ML-DSA, NTT, Tensor Cores, cache；类型：implementation and countermeasure claim。
- 核心想法：在机器学习加速器内部以寄存器承载主要 NTT 和多项式运算，减少外部内存依赖。
- 作者报告：作者摘要报告 Tensor Core 加速，并明确声称寄存器内核心计算可缓解内存披露和缓存侧信道。
- 限制与下一步：只有作者公开摘要及正式元数据；缓存缓解尚无本库读到的攻击/防护评估，不能由 memory-less 推断恒时、功耗安全或完整实现无泄漏。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://bianyiby.github.io/publications/。
- [详细阅读记录](notes/ccs2025-masking-contracts-and-observation-boundaries-20261114.md)
- 代码/数据核查：no author code/data executed; artifact completeness not inspected；引用追踪：pending except explicit inventory。

## MegaBlocks: Breaking the Logarithmic I/O-Overhead Barrier for Oblivious RAM

- 来源：[CCS 2025](https://doi.org/10.1145/3719027.3765159)；时间标记：within frozen rolling window。
- 作者：Gilad Asharov; Eliran Eiluz; Ilan Komargodski; Wei-Kai Lin
- 对象：ORAM, hierarchical ORAM, asymmetric memory blocks；类型：oblivious computation。
- 核心想法：研究逻辑字渐近小于物理块的非对称 ORAM 模型，构造更低 I/O 开销的层次方案。
- 作者报告：作者摘要声称在该设置达到 O(log N / log log N) I/O，并比较 PathORAM 与 FutORAMa 的实现开销。
- 限制与下一步：改变块/字关系的模型，不是推翻同一模型下的对数下界；性能依赖块尺寸和客户端内存，比较对象原本未针对大块设置设计。ePrint 明示 major revision，未全文比较。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://eprint.iacr.org/2025/1592。
- [详细阅读记录](notes/ccs2025-second-pass-metrics-transfer-and-access-20261114.md)
- 代码/数据核查：no author code/data executed; completeness not verified；引用追踪：pending except explicit inventory。

## MileSan: Detecting Exploitable Microarchitectural Leakage via Differential Hardware-Software Taint Tracking

- 来源：[CCS 2025](https://doi.org/10.1145/3719027.3765066)；时间标记：within frozen rolling window by recorded publication or author-upload date。
- 作者：Tobias Kovats; Flavien Solt; Katharina Ceesay-Seitz; Kaveh Razavi
- 对象：RTL, taint tracking, RISC-V, transient execution；类型：automated discovery。
- 核心想法：比较软件架构污点流与 RTL 微架构污点流，寻找额外且可被架构观察的影响。
- 作者报告：作者报告 RandOS 在五种 RISC-V CPU 上发现 19 个新的恒时违例或瞬态执行问题。
- 限制与下一步：仅论文摘要和作者项目说明；对给定程序的检测、随机程序搜索覆盖与整个 CPU 的无漏洞证明不同，不涵盖未建模模拟功耗。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://comsec-files.ethz.ch/papers/milesan_ccs25.pdf。
- [详细阅读记录](notes/ccs2025-masking-contracts-and-observation-boundaries-20261114.md)
- 代码/数据核查：no author code/data executed; artifact completeness not inspected；引用追踪：pending except explicit inventory。

## MoEcho: Exploiting Side-Channel Attacks to Compromise User Privacy in Mixture-of-Experts LLMs

- 来源：[CCS 2025](https://doi.org/10.1145/3719027.3765174)；时间标记：within frozen rolling window by recorded publication or author-upload date。
- 作者：Ruyi Ding; Tianhong Xu; Xinyi Shen; Aidong Adam Ding; Yunsi Fei
- 对象：MoE, LLM, VLM, CPU, GPU；类型：attack。
- 核心想法：研究专家路由引起的输入相关硬件执行痕迹，并用于用户内容推断。
- 作者报告：作者摘要列出 CPU 缓存占用及 Pageout+Reload、GPU 计数器及 TLB 通道，报告提示、响应和视觉任务。
- 限制与下一步：非密码目标侧信道；四类推断/重建任务的访问条件和准确率未读正文，不解释为任意提示逐字恢复。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://arxiv.org/abs/2508.15036。
- [详细阅读记录](notes/ccs2025-masking-contracts-and-observation-boundaries-20261114.md)
- 代码/数据核查：no author code/data executed; artifact completeness not inspected；引用追踪：pending except explicit inventory。

## Off-Path TCP Exploits: PMTUD Breaks TCP Connection Isolation in IP Address Sharing Scenarios

- 来源：[CCS 2025](https://doi.org/10.1145/3719027.3744888)；时间标记：within frozen rolling window。
- 作者：Xuewei Feng; Zhaoxi Li; Qi Li; Ziqiang Wang; Kun Sun; Ke Xu
- 对象：PMTUD, TCP, shared public IP；类型：network side channel。
- 核心想法：利用同一公网 IP 的路径 MTU 状态跨连接共享，推断另一个设备 TCP 连接的状态。
- 作者报告：作者预印本报告与共享该公网 IP 的恶意设备协作进行离路径推断，并在若干网络和应用中评估后果。
- 限制与下一步：需要协作设备及 IP 共享条件，不能描述成任意远端攻击者无附加条件的能力。预印本与正式记录题名/作者对应，显式版本关系及正式全文差异仍待核。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://arxiv.org/abs/2509.11833。
- [详细阅读记录](notes/ccs2025-second-pass-metrics-transfer-and-access-20261114.md)
- 代码/数据核查：no author code/data executed; completeness not verified；引用追踪：pending except explicit inventory。

## One Video to Steal Them All: 3D-Printing IP Theft through Optical Side-Channels

- 来源：[CCS 2025](https://doi.org/10.1145/3719027.3744837)；时间标记：within frozen rolling window。
- 作者：Twisha Chattopadhyay; Fabricio Ceschin; Marco E. Garza; Dymytriy Zyunkin; Animesh Chhotaray; Aaron P. Stebner; Saman Zonouz; Raheem Beyah
- 对象：3D printing, G-code, video；类型：optical inference。
- 核心想法：从打印喷头轨迹与视频重建可生成相似对象的打印指令及参数。
- 作者报告：作者以几何、外观和内部结构的等价检查比较重建指令，报告平均 90.87% 的所定义准确度。
- 限制与下一步：需要打印过程视频；该数字不是原始 G-code 的逐字节精确恢复率，更不是密码密钥恢复。arXiv 标明扩展版并给出匹配正式 DOI。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://arxiv.org/abs/2506.21897。
- [详细阅读记录](notes/ccs2025-second-pass-metrics-transfer-and-access-20261114.md)
- 代码/数据核查：no author code/data executed; completeness not verified；引用追踪：pending except explicit inventory。

## Peekaboo, I See Your Queries: Passive Attacks Against DSSE Via Intermittent Observations

- 来源：[CCS 2025](https://doi.org/10.1145/3719027.3765075)；时间标记：within frozen rolling window。
- 作者：Hao Nie; Wei Wang; Peng Xu; Wei Chen; Laurence T. Yang; Mauro Conti; Kaitai Liang
- 对象：DSSE, search patterns, intermittent observation；类型：leakage abuse。
- 核心想法：在间歇观察下推断搜索模式，再结合辅助知识与其他泄漏恢复查询。
- 作者报告：作者将框架用于 Sap 和 Jigsaw，分别评估搜索模式聚类与查询推断，报告随观察轮次/查询数变化的结果。
- 限制与下一步：被动是相对于主动文件注入，仍需允许的泄漏观察与辅助知识；ARI 和查询正确率不能混用。全文首页明确为 CCS 2025 论文扩展稿，剩余正文与基线预算待核。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://arxiv.org/abs/2509.03806。
- [详细阅读记录](notes/ccs2025-second-pass-metrics-transfer-and-access-20261114.md)
- 代码/数据核查：no author code/data executed; completeness not verified；引用追踪：pending except explicit inventory。

## Pixnapping: Bringing Pixel Stealing out of the Stone Age

- 来源：[CCS 2025](https://doi.org/10.1145/3719027.3765093)；时间标记：within frozen rolling window by recorded publication or author-upload date。
- 作者：Alan Wang; Pranav Gopalkrishnan; Yingchen Wang; Christopher W. Fletcher; Hovav Shacham; David Kohlbrenner; Riccardo Paccagnella
- 对象：Android, GPU compression, pixel stealing；类型：attack。
- 核心想法：利用 Android 渲染接口与像素相关时间差，在浏览器外重建其他应用显示的内容。
- 作者报告：作者摘要报告 Google 和 Samsung 手机案例，并演示获取 Google Authenticator 显示的短时 2FA 码。
- 限制与下一步：需要运行恶意应用且秘密进入可见渲染流程；不是读取从未显示的任意密钥。具体型号和补丁时点按作者材料限定，不外推当前所有 Android 版本。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://www.pixnapping.com/pixnapping.pdf。
- [详细阅读记录](notes/ccs2025-masking-contracts-and-observation-boundaries-20261114.md)
- 代码/数据核查：no author code/data executed; artifact completeness not inspected；引用追踪：pending except explicit inventory。

## Securing Cryptographic Software via Typed Assembly Language

- 来源：[CCS 2025](https://doi.org/10.1145/3719027.3765116)；时间标记：within frozen rolling window by recorded publication or author-upload date。
- 作者：Shixin Song; Tingzhen Dong; Kosi Nwabueze; Julian Zanders; Andres Erbsen; Adam Chlipala; Mengjia Yan
- 对象：SecSep, Octal, typed assembly, speculation；类型：countermeasure。
- 核心想法：通过汇编类型推断和重写分离秘密与公开栈数据，配合硬件污点跟踪保护推测执行。
- 作者报告：作者报告所测密码程序平均开销 1.2%，并定义软件和硬件两侧的公开非干扰契约。
- 限制与下一步：前提是恒时软件及满足相应契约的硬件（引用 ProSpeCT）；不是单靠汇编变换保护任意现有处理器，也不是功耗安全证明。录用题名比出版/作者 PDF 多出硬件扩展短语。
- 阅读层级：selected_full_text_sections；来源：https://people.csail.mit.edu/mengjia/data/2025.CCS.SecSep.pdf。
- 已读章节：Author CCS-format PDF pages 1 and 3: abstract, threat model, software/hardware public noninterference and stack-rewriting motivation. Remaining proofs and evaluation not fully reviewed.
- [详细阅读记录](notes/ccs2025-masking-contracts-and-observation-boundaries-20261114.md)
- 代码/数据核查：no author code/data executed; artifact completeness not inspected；引用追踪：pending except explicit inventory。

## Styled to Steal: The Overlooked Attack Surface in Email Clients

- 来源：[CCS 2025](https://doi.org/10.1145/3719027.3765189)；时间标记：within frozen rolling window。
- 作者：Leon Trampert; Daniel Weber; Christian Rossow; Michael Schwarz
- 对象：CSS, OpenPGP, S/MIME, email rendering；类型：rendering side channel。
- 核心想法：利用 CSS 渲染条件及字体等特性，将已解密邮件中的字符映射为外部网络请求。
- 作者报告：作者报告无需 JavaScript 的明文外传，并展示 Thunderbird 与 KMail 的特定配置案例。
- 限制与下一步：需要恶意 HTML/CSS 注入、邮件被打开渲染及相关网络行为；无 JavaScript 不等于无攻击输入或无观察条件。版本和缓解按论文时点限定，不能宣称当前全部客户端仍受影响。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://d-we.me/papers/stylemail_ccs25.pdf。
- [详细阅读记录](notes/ccs2025-second-pass-metrics-transfer-and-access-20261114.md)
- 代码/数据核查：no author code/data executed; completeness not verified；引用追踪：pending except explicit inventory。

## Swallow: A Transfer-Robust Website Fingerprinting Attack via Consistent Feature Learning

- 来源：[CCS 2025](https://doi.org/10.1145/3719027.3744795)；时间标记：within frozen rolling window。
- 作者：Meng Shen; Jinhe Wu; Junyu Ai; Qi Li; Chenchen Ren; Ke Xu; Liehuang Zhu
- 对象：Tor, website fingerprinting, transfer learning, CIF；类型：traffic analysis。
- 核心想法：利用一致交互特征和数据增强，研究网站指纹在不同网络条件及防护流量上的迁移。
- 作者报告：作者在十个数据集上比较闭集/开放世界设置；每网站五条有标签样本用于微调，另有预训练数据。
- 限制与下一步：全部受测 WF 防护在未防护轨迹上模拟生成；当前范围为单网站主页，不含多标签页/站内网页。材料只覆盖部分场景；不能将微调样本数当作总训练预算。
- 阅读层级：selected_full_text_sections；来源：https://raw.githubusercontent.com/wujinhe0814/Swallow/main/paper/Swallow.pdf。
- 已读章节：Author repository PDF pages 1 and 13-14: abstract, ablation/pre-training discussion, simulated-defense and single-homepage limitations, all 37 bibliography positions. Repository README inspected; no code/data executed.
- [详细阅读记录](notes/ccs2025-second-pass-metrics-transfer-and-access-20261114.md)
- 代码/数据核查：Author README read: selected closed/open-world scenarios and partial raw traces linked via Zenodo 16607834; no archive download, execution or completeness verification；引用追踪：All 37 author bibliography positions screened: 10 linked, 15 pending, 11 provisional background, one duplicate; no recursive closure。

## Synthesis of Sound and Precise Leakage Contracts for Open-Source RISC-V Processors

- 来源：[CCS 2025](https://doi.org/10.1145/3719027.3765148)；时间标记：within frozen rolling window by recorded publication or author-upload date。
- 作者：Zilong Wang; Gideon Mohr; Klaus von Gleissenthall; Jan Reineke; Marco Guarnieri
- 对象：LeaSyn, leakage contracts, RISC-V, RTL；类型：formal verification。
- 核心想法：在用户给定模板内交替进行经验泄漏表征、契约合成与健全性验证。
- 作者报告：作者报告在六个开源 RISC-V CPU 上生成更精确的契约。
- 限制与下一步：精确性针对模板与探索到的测试对；健全性相对于给定 RTL 和攻击者观察模型，不表示覆盖所有物理功耗/电磁通道。仅读摘要和第 2 节概览。
- 阅读层级：selected_full_text_sections；来源：https://mguarnieri.github.io/publication/ccs2025/ccs2025.pdf。
- 已读章节：Author CCS-format PDF pages 1 and 3: abstract and Section 2 overview, observation example, soundness/precision and template scope. Remaining proof and evaluation sections not reviewed.
- [详细阅读记录](notes/ccs2025-masking-contracts-and-observation-boundaries-20261114.md)
- 代码/数据核查：no author code/data executed; artifact completeness not inspected；引用追踪：pending except explicit inventory。

## TEMPEST-LoRa: Cross-Technology Covert Communication

- 来源：[CCS 2025](https://doi.org/10.1145/3719027.3744817)；时间标记：within frozen rolling window by recorded publication or author-upload date。
- 作者：Xieyang Sun; Yuanqing Zheng; Wei Xi; Zuhao Chen; Zhizhen Chen; Han Hao; Zhiping Jiang; Sheng Zhong
- 对象：electromagnetic, video cable, LoRa；类型：covert channel。
- 核心想法：操控视频线电磁辐射，使其可由商用 LoRa 接收端解码。
- 作者报告：作者摘要报告远距离或较高速率的隐蔽传输案例，并可在显示器关闭时发送。
- 限制与下一步：主动调制的隐蔽通信需要发送端控制与数据获取条件；不是无需执行控制的被动密码能耗泄漏。最大距离与最大速率不能视为同时达到。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://arxiv.org/abs/2506.21069。
- [详细阅读记录](notes/ccs2025-masking-contracts-and-observation-boundaries-20261114.md)
- 代码/数据核查：no author code/data executed; artifact completeness not inspected；引用追踪：pending except explicit inventory。

## Time Tells All: Deanonymization of Blockchain RPC Users with Zero Transaction Fee

- 来源：[CCS 2025](https://doi.org/10.1145/3719027.3765082)；时间标记：within frozen rolling window。
- 作者：Shan Wang; Ming Yang; Yu Liu; Yue Zhang; Shuaiqing Zhang; Zhen Ling; Jiannong Cao; Xinwen Fu
- 对象：blockchain, RPC, TCP timestamps, deanonymization；类型：network timing attack。
- 核心想法：结合公开账本确认时刻与 RPC 轮询流量时刻，关联用户 IP 与链上化名。
- 作者报告：作者预印本报告对多种公链 RPC 用户的时间相关推断，并强调不需交易手续费。
- 限制与下一步：威胁模型是能观察网络边界或交换点的强被动对手；零交易费不等于零观察权限或零总成本。作者预印本与正式版本的显式关系和全文差异待核。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://arxiv.org/abs/2508.21440。
- [详细阅读记录](notes/ccs2025-second-pass-metrics-transfer-and-access-20261114.md)
- 代码/数据核查：no author code/data executed; completeness not verified；引用追踪：pending except explicit inventory。

## Timing Attacks on Differential Privacy are Practical

- 来源：[CCS 2025](https://doi.org/10.1145/3719027.3765146)；时间标记：within frozen rolling window by recorded publication or author-upload date。
- 作者：Zachary Ratliff; Nicolas Berrios; James Mickens
- 对象：differential privacy, timing, preprocessing；类型：evaluation。
- 核心想法：将运行时间和输出联合纳入 DP 实现的隐私审计，包括排序、过滤等预处理。
- 作者报告：作者报告 diffprivlib、OpenDP、PyDP 的计时问题，并给出观察输出和时间时的经验隐私损失下界。
- 限制与下一步：输出分布的 DP 保证不自动覆盖时间；数据库大小是否公开、邻接关系和观测噪声都影响结论。仅读摘要，审计下界不是完备安全证明。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://zacharyratliff.org/files/dp-timing-attacks.pdf。
- [详细阅读记录](notes/ccs2025-masking-contracts-and-observation-boundaries-20261114.md)
- 代码/数据核查：no author code/data executed; artifact completeness not inspected；引用追踪：pending except explicit inventory。

## WireTap: Breaking Server SGX via DRAM Bus Interposition

- 来源：[CCS 2025](https://doi.org/10.1145/3719027.3765204)；时间标记：within frozen rolling window by recorded publication or author-upload date。
- 作者：Alex Seto; Oytun Kuday Duran; Samy Amer; Jalen Chuang; Stephan van Schaik; Daniel Genkin; Christina Garman
- 对象：SGX, DRAM bus, deterministic encryption；类型：physical attack。
- 核心想法：通过物理 DRAM 总线观察与服务器 SGX 的确定性加密行为分析机密执行。
- 作者报告：作者报告提取服务器 SGX 证明密钥及区块链部署的后果。
- 限制与下一步：明确需要物理接触并超出 Intel 所声明的物理攻击保护边界；不能描述为仅远程或软件级攻击。仅读论文摘要。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://wiretap.fail/files/wiretap.pdf。
- [详细阅读记录](notes/ccs2025-masking-contracts-and-observation-boundaries-20261114.md)
- 代码/数据核查：no author code/data executed; artifact completeness not inspected；引用追踪：pending except explicit inventory。

## mUOV: Masking the Unbalanced Oil and Vinegar Digital Signature Scheme at First- and Higher-Order

- 来源：[CCS 2025](https://doi.org/10.1145/3719027.3765188)；时间标记：within frozen rolling window by recorded publication or author-upload date。
- 作者：Suparna Kundu; Quinten Norga; Angshuman Karmakar; Uttam Kumar Ojha; Anindya Ganguly; Ingrid Verbauwhede
- 对象：UOV, MQ signatures, masking, t-probing, Cortex-M4；类型：masking。
- 核心想法：为 UOV 的点积、矩阵运算和签名流程提出掩码部件，并处理实现中的微架构重组合。
- 作者报告：NIST 托管稿给出任意阶探针模型论证；部分 maskVerif 检查为一/二阶；实测为缩小参数 m=4、n=10 的一阶 TVLA。
- 限制与下一步：完整签名组合因 NIo 工具限制未机械验证；Cortex-M4 泄漏测试与 i7 周期基准分开。未超检测阈值不是完整安全证明，正式 ACM 与 NIST 托管稿未逐字比对。
- 阅读层级：selected_full_text_sections；来源：https://eprint.iacr.org/2024/1875。
- 已读章节：NIST-hosted author manuscript: PDF page 1; pages 15-18 (composition caveat, implementation, TVLA, performance); pages 19-22 bibliography and discussion; page 23 Appendix A only. Page 17 table/figure visually checked. Remaining proofs and appendices not fully reviewed.
- [详细阅读记录](notes/ccs2025-masking-contracts-and-observation-boundaries-20261114.md)
- 代码/数据核查：no author code/data executed; artifact completeness not inspected；引用追踪：52 author-manuscript entries: 27 linked, 1 pending, 24 provisional background; final ACM bibliography and recursive/forward closure pending。

## Masking Gaussian Elimination at Arbitrary Order with Application to Multivariate-and Code-Based PQC

- 来源：[CT-RSA 2025](https://doi.org/10.1007/978-3-031-88661-4_11)；时间标记：within frozen rolling window。
- 作者：Quinten Norga; Suparna Kundu; Uttam Kumar Ojha; Anindya Ganguly; Angshuman Karmakar; Ingrid Verbauwhede
- 对象：Gaussian elimination, UOV, MAYO, SNOVA, QR-UOV, MQ-Sign；类型：masking。
- 核心想法：为行阶梯化和回代提出任意阶掩码部件，区分探针模型证明与实现安全。
- 作者报告：作者报告 Cortex-M4 上一至三阶周期基准，计入片上 TRNG；一阶 UOV-I/III/V 开销约 15.1/15.2/15.4 倍。
- 限制与下一步：作者稿第 21 页明确是概念验证，微架构泄漏缓解不在本文范围；并非三阶物理泄漏验证。主要保护 GE 子过程，完整签名防护另需组合；正式版与 major revision 作者稿未全文比对。
- 阅读层级：selected_full_text_sections；来源：https://link.springer.com/chapter/10.1007/978-3-031-88661-4_11。
- 已读章节：Publisher abstract; author-hosted 31-page manuscript PDF pages 1, 21-22 (implementation, Table 3, conclusion), page 23 references only; page 21 visually checked. Remaining proofs and references not fully screened.
- [详细阅读记录](notes/muov-followups-and-masked-sampling-20261114.md)
- 代码/数据核查：no author code/data executed; artifact completeness not inspected；引用追踪：pending except explicit inventories。

## Masked Computation of the Floor Function and Its Application to the FALCON Signature

- 来源：[CiC 2025](https://doi.org/10.62056/ay73zl7s)；时间标记：within frozen rolling window。
- 作者：Pierre-Augustin Berthet; Justine Paillet; Cédric Tavernier; Lilian Bossuet; Brice Colombier
- 对象：FALCON, floating-point, floor, MIMO-SNI；类型：masking。
- 核心想法：补充浮点 floor 与除法掩码部件，并用于 FALCON 采样流程。
- 作者报告：正式稿报告探针模型组合安全论证及 i7-11800H/GCC 9.4.0 性能；表 6 的签名流程计时不含签名拒绝。
- 限制与下一步：秒级表 6 不是完整生产签名时延；作者认为该实现不适于部署。选读没有建立功耗/电磁实测保证，未独立验证全部证明；作者 22 页稿与正式 23 页稿的参考条目存在差异。
- 阅读层级：selected_full_text_sections；来源：https://cic.iacr.org/p/1/4/9。
- 已读章节：Formal publisher PDF pages 1, 18-23: abstract, performance Tables 5-6, conclusion, all 31 bibliography positions; page 19 visually checked. Author 22-page PDF pages 1, 16-22 also consulted, but formal bibliography controls this inventory. Proofs not fully reviewed.
- [详细阅读记录](notes/muov-followups-and-masked-sampling-20261114.md)
- 代码/数据核查：no author code/data executed; artifact completeness not inspected；引用追踪：31 formal reference positions: 21 linked, 0 pending identities, 10 provisional background; target full texts and recursive/forward closure pending。

## A Practical Tutorial on Deep Learning-based Side-channel Analysis

- 来源：[IACR ePrint 2025](https://eprint.iacr.org/2025/471)；时间标记：within rolling five-year window by publication date。
- 作者：Sengim Karayalcin; Marina Krcek; Stjepan Picek
- 对象：DLSCA, deep learning；类型：tutorial。
- 核心想法：介绍利用公开数据集与 Colab 学习深度学习侧信道分析的基本流程。
- 作者报告：作者提供核心流程说明、代码片段和进阶参考，提及标准化需求。
- 限制与下一步：教程不是新的 PQC 攻击实测；只读预印本摘要，PDF 403，没有运行代码或下载数据。不能与同作者其他 SoK 直接合并。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://eprint.iacr.org/2025/471。
- [详细阅读记录](notes/pqc-citation-followups-and-evidence-20261113.md)
- 代码/数据核查：no author code or data executed; artifact contents not inspected；引用追踪：pending except explicitly inventoried citations。

## FAEST for Memory-Constrained Devices

- 来源：[IACR ePrint 2025](https://eprint.iacr.org/2025/1261)；时间标记：within rolling five-year window。
- 作者：Diego F. Aranha; Johan Degn; Jonathan Eilath; Kent Nielsen; Peter Scholl
- 对象：FAEST, VOLEitH；类型：implementation_revision。
- 核心想法：以 VOLE 重算和复用降低 FAEST v1.1 Cortex-M4 实现的内存，并保留恒时实现。
- 作者报告：当前修订明确撤回掩码实现；作者说明审稿人发现攻击，保留低内存优化。
- 限制与下一步：不能继续把旧题名中的防护当作当前已成立结论；PDF Disclaimer 与历史页访问 403，未核查完整版本差异，也未确定撤回与某篇攻击论文的因果对应。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://eprint.iacr.org/2025/1261; https://pascholl.github.io/publications。
- [详细阅读记录](notes/mpcith-revisions-and-evidence-20261113.md)
- 代码/数据核查：not inspected; no author code executed；引用追踪：SDitH and CiC actual citations verified; current author revision retracts masked implementation; no exhaustive forward coverage or causal attribution。

## A side-channel attack on a masked hardware implementation of CRYSTALS-Kyber

- 来源：[Journal of Cryptographic Engineering 2025](https://doi.org/10.1007/s13389-025-00375-7)；时间标记：within rolling five-year window。
- 作者：Yanning Ji; Elena Dubrova
- 对象：Kyber；类型：attack。
- 核心想法：以相邻消息位的汉明距离攻击掩码 Kyber-512 的 FPGA 消息解码，提出降低扇出的寄存器修改。
- 作者报告：作者在裁减设计上报告：399 次重复解封装，同设备剖析消息恢复 99.7%，异设备剖析 94.8%；测试 1000 条消息。
- 限制与下一步：恢复消息及其导出的会话共享密钥；不能写成本研究已实测长期私钥恢复。1000 条原始训练迹线切分成 255000 个片段，不是独立采集。完整原设计超出实验 FPGA 容量，裁减等价性未独立验证。 已有 ASHES 2023 书目版本关系保留，完整版本差异仍待审计。
- 阅读层级：selected_full_text_sections；来源：https://link.springer.com/article/10.1007/s13389-025-00375-7。
- 已读章节：Publisher HTML abstract and sections 1–2, 4, 5 opening, 6, 8–10; reference entries 23/26/33 inspected, only 26/33 linked. Numerical recovery rates read from section 8 prose; tables 3/5 not independently transcribed. Section 7 and full bibliography not completely read.
- [详细阅读记录](notes/kyber-shuffle-followups-and-evidence-20261113.md)
- 代码/数据核查：not inspected; no author code executed；引用追踪：selected backward/forward relation verified; complete tracing pending。

## A Systematic Evaluation of Novel and Existing Cache Side Channels

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/a-systematic-evaluation-of-novel-and-existing-cache-side-channels/)；时间标记：NDSS 2025 within frozen rolling window; earliest online date not independently established。
- 作者：Fabian Rauscher; Carina Fiedler; Andreas Kogler; Daniel Gruss
- 对象：cache, cldemote, AES, power amplification；类型：evaluation and attack。
- 核心想法：系统比较缓存侧信道，并提出基于 cldemote 的三种观察方法。
- 作者报告：作者按九项性质比较四种既有与三种新增通道，另报告 AES T-table、按键时序、KASLR 和功耗放大案例。
- 限制与下一步：摘要中的 15.48 Mbit/s 是通道容量，不能当作密钥恢复速率；非包容 L3、跨核条件和不同 Intel 微架构需分别核对。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official NDSS paper-page abstract; selected formal PDF text only where recorded。
- [详细阅读记录](notes/ndss2025-static-power-quantum-and-scope-20261114.md)
- 代码/数据核查：not checked; official PDF link identified, no author code executed；引用追踪：pending。

## CHAOS: Exploiting Station Time Synchronization in 802.11 Networks

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/chaos-exploiting-station-time-synchronization-in-802-11-networks/)；时间标记：NDSS 2025 within frozen rolling window; earliest online date not independently established。
- 作者：Sirus Shahini (University of Utah), Robert Ricci (University of Utah)
- 对象：Wi-Fi, TSF, covert channel；类型：covert channel。
- 核心想法：在 Wi-Fi 信标顺序和时间同步字段中构造隐蔽通道。
- 作者报告：作者以标准未修改 Wi-Fi 硬件报告建议配置下 520 bit/s，并提出利用时间同步关联客户端和基站的线索。
- 限制与下一步：这是合作发送者的隐蔽通信；关联攻击在摘要中仅为勾勒，不能把吞吐量解释为被动秘密恢复。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official NDSS paper-page abstract; selected formal PDF text only where recorded。
- [详细阅读记录](notes/ndss2025-static-power-quantum-and-scope-20261114.md)
- 代码/数据核查：not checked; official PDF link identified, no author code executed；引用追踪：pending。

## Cascading Spy Sheets: Exploiting the Complexity of Modern CSS for Email and Browser Fingerprinting

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/cascading-spy-sheets-exploiting-the-complexity-of-modern-css-for-email-and-browser-fingerprinting/)；时间标记：NDSS 2025 within frozen rolling window; earliest online date not independently established。
- 作者：Leon Trampert (CISPA Helmholtz Center for Information Security), Daniel Weber (CISPA Helmholtz Center for Information Security), Lukas Gerlach (CISPA Helmholtz Center for Information Security), Christian Rossow (CISPA Helmholtz Center for Information Security), Michael Schwarz (CISPA Helmholtz Center for Information Security)
- 对象：CSS, browser fingerprinting, email；类型：attack and countermeasure。
- 核心想法：利用 CSS 条件资源与动态特性进行无脚本浏览器和邮件指纹识别。
- 作者报告：作者报告可区分所测 1176 种浏览器与系统组合的 97.95%，并在 21 个邮件客户端中的八个展示指纹能力。
- 限制与下一步：组合区分率不是对独立用户的识别率；资源请求可见性、客户端限制和两种防护的覆盖待正文。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official NDSS paper-page abstract; selected formal PDF text only where recorded。
- [详细阅读记录](notes/ndss2025-static-power-quantum-and-scope-20261114.md)
- 代码/数据核查：not checked; official PDF link identified, no author code executed；引用追踪：pending。

## CounterSEVeillance: Performance-Counter Attacks on AMD SEV-SNP

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/counterseveillance-performance-counter-attacks-on-amd-sev-snp/)；时间标记：NDSS 2025 within frozen rolling window; earliest online date not independently established。
- 作者：Stefan Gast; Hannes Weissteiner; Robin Leander Schröder; Daniel Gruss
- 对象：SEV-SNP, performance counters, RSA, TOTP；类型：attack。
- 核心想法：单步执行 SEV-SNP 虚拟机并记录性能计数器，推断控制流和操作数性质。
- 作者报告：作者报告 228 种事件对恶意管理程序可见，在六种事件的四个案例中包含单次签名恢复 RSA-4096 与 TOTP 推断。
- 限制与下一步：需要特权管理程序、APIC 中断及页故障的指令级单步能力；论文所称已补丁系统是当时实验状态，不能推为当前所有版本。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official NDSS paper-page abstract; selected formal PDF text only where recorded。
- [详细阅读记录](notes/ndss2025-static-power-quantum-and-scope-20261114.md)
- 代码/数据核查：not checked; official PDF link identified, no author code executed；引用追踪：pending。

## Crosstalk-induced Side Channel Threats in Multi-Tenant NISQ Computers

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/crosstalk-induced-side-channel-threats-in-multi-tenant-nisq-computers/)；时间标记：NDSS 2025 within frozen rolling window; earliest online date not independently established。
- 作者：Navnil Choudhury; Chaithanya Naik Mude; Sanjay Das; Preetham Chandra Tikkireddi; Swamit Tannu; Kanad Basu
- 对象：quantum computing, crosstalk, CNOT, graph classification；类型：attack。
- 核心想法：以量子硬件串扰识别邻近 CNOT 活动，再用门关系图分类受害者电路。
- 作者报告：正文报告 IBM 硬件上的门检测实验；336 个基准电路及其编译变体上的分类部分采用理想门检测，再人为引入计数误差。
- 限制与下一步：属于量子计算硬件侧信道，不是经典设备上的 PQC 密钥攻击。摘要最高 85.7% 与正文基准 85.6% 分开保留；不能称为 336 类端到端实机恢复。
- 阅读层级：selected_full_text_sections；来源：official NDSS paper-page abstract; selected formal PDF text only where recorded。
- 已读章节：PDF pp.6-7: IBM gate-detector experiments; PDF pp.11-12: graph benchmark evaluation and ideal detection/fuzziness assumptions; p.12 rendered
- [详细阅读记录](notes/ndss2025-static-power-quantum-and-scope-20261114.md)
- 代码/数据核查：not checked; official PDF link identified, no author code executed；引用追踪：pending。

## Deanonymizing Device Identities via Side-channel Attacks in Exclusive-use IoTs & Mitigation

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/deanonymizing-device-identities-via-side-channel-attacks-in-exclusive-use-iots-mitigation/)；时间标记：NDSS 2025 within frozen rolling window; earliest online date not independently established。
- 作者：Christopher Ellis (The Ohio State University), Yue Zhang (Drexel University), Mohit Kumar Jangid (The Ohio State University), Shixuan Zhao (The Ohio State University), Zhiqiang Lin (The Ohio State University)
- 对象：BLE, Wi-Fi, device tracking；类型：attack and countermeasure。
- 核心想法：利用专属配对通信的响应关系，绕过设备地址随机化进行去匿名化。
- 作者报告：IDBleed 在 BLE 与 Wi-Fi 的关联关系上建立布尔观察，作者提出 Anonymization Layer 并评估开销。
- 限制与下一步：摘要中的约 2% 开销限于所测手机与 PC；设备关系暴露、可追踪性及密码明文恢复是不同目标。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official NDSS paper-page abstract; selected formal PDF text only where recorded。
- [详细阅读记录](notes/ndss2025-static-power-quantum-and-scope-20261114.md)
- 代码/数据核查：not checked; official PDF link identified, no author code executed；引用追踪：pending。

## EMIRIS: Eavesdropping on Iris Information via Electromagnetic Side Channel

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/emiris-eavesdropping-on-iris-information-via-electromagnetic-side-channel/)；时间标记：NDSS 2025 within frozen rolling window; earliest online date not independently established。
- 作者：Wenhao Li (Shandong University), Jiahao Wang (Shandong University), Guoming Zhang (Shandong University), Yanni Yang (Shandong University), Riccardo Spolaor (Shandong University), Xiuzhen Cheng (Shandong University), Pengfei Hu (Shandong University)
- 对象：electromagnetic, iris, diffusion reconstruction；类型：attack。
- 核心想法：从近红外传感器数据传输的电磁辐射重建虹膜图像。
- 作者报告：作者将传输映射与逆问题恢复结合，报告 50 位用户、3000 多份虹膜样本上的重建和经典识别模型欺骗。
- 限制与下一步：平均 SSIM 0.511、FID 7.25 和欺骗成功率 53.47% 是不同指标；不等于对全部商用认证系统可用，距离和训练条件待全文。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official NDSS paper-page abstract; selected formal PDF text only where recorded。
- [详细阅读记录](notes/ndss2025-static-power-quantum-and-scope-20261114.md)
- 代码/数据核查：not checked; official PDF link identified, no author code executed；引用追踪：pending。

## Evaluating Machine Learning-Based IoT Device Identification Models for Security Applications

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/evaluating-machine-learning-based-iot-device-identification-models-for-security-applications/)；时间标记：NDSS 2025 within frozen rolling window; earliest online date not independently established。
- 作者：Eman Maali (Imperial College London), Omar Alrawi (Georgia Institute of Technology), Julie McCann (Imperial College London)
- 对象：traffic fingerprinting, IoT, distribution shift；类型：evaluation。
- 核心想法：评估基于网络流量的 IoT 设备识别在模式与时空变化下的可靠性。
- 作者报告：作者按运行模式、时空条件及采样方式整理评估，并用解释工具分析性能退化。
- 限制与下一步：纳入流量指纹的方法评估；不是密码密钥恢复，数据划分、设备迁移及公开特征范围待全文。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official NDSS paper-page abstract; selected formal PDF text only where recorded。
- [详细阅读记录](notes/ndss2025-static-power-quantum-and-scope-20261114.md)
- 代码/数据核查：not checked; official PDF link identified, no author code executed；引用追踪：pending。

## GadgetMeter: Quantitatively and Accurately Gauging the Exploitability of Speculative Gadgets

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/gadgetmeter-quantitatively-and-accurately-gauging-the-exploitability-of-speculative-gadgets/)；时间标记：NDSS 2025 within frozen rolling window; earliest online date not independently established。
- 作者：Qi Ling; Yujun Liang; Yi Ren; Baris Kasikci; Shuwen Deng
- 对象：speculative execution, gadget analysis, timing；类型：automated analysis。
- 核心想法：以推测授权与秘密泄漏之间的时序竞争量化 gadget 可利用性。
- 作者报告：正式 PDF 摘要说将既有工具报告的 471 个 gadget 判为不可利用；结合指令 DAG、静态分析和运行测试。
- 限制与下一步：官方网站摘要省略了 state-of-the-art 一段而语义受损，已对照正式 PDF；特定处理器与攻击能力下的判断不能当作全部推测攻击安全证明。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official NDSS paper-page abstract; selected formal PDF text only where recorded。
- [详细阅读记录](notes/ndss2025-static-power-quantum-and-scope-20261114.md)
- 代码/数据核查：not checked; official PDF link identified, no author code executed；引用追踪：pending。

## I Know What You Asked: Prompt Leakage via KV-Cache Sharing in Multi-Tenant LLM Serving

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/i-know-what-you-asked-prompt-leakage-via-kv-cache-sharing-in-multi-tenant-llm-serving/)；时间标记：NDSS 2025 within frozen rolling window; earliest online date not independently established。
- 作者：Guanlong Wu (Southern University of Science and Technology), Zheng Zhang (ByteDance Inc.), Yao Zhang (ByteDance Inc.), Weili Wang (Southern University of Science and Technolog), Jianyu Niu (Southern University of Science and Technolog), Ye Wu (ByteDance Inc.), Yinqian Zhang (Southern University of Science and Technology (SUSTech))
- 对象：LLM, KV cache, prompt leakage；类型：attack。
- 核心想法：利用多租户 LLM 服务中的共享 KV 缓存重建其他用户提示词。
- 作者报告：PROMPTPEEK 在三种不同先验知识场景下评估共享前缀缓存的泄漏。
- 限制与下一步：需要共享 KV 缓存及相应查询观察能力；三种先验不同，不能把最强先验结果推广为任意提示词盲恢复。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official NDSS paper-page abstract; selected formal PDF text only where recorded。
- [详细阅读记录](notes/ndss2025-static-power-quantum-and-scope-20261114.md)
- 代码/数据核查：not checked; official PDF link identified, no author code executed；引用追踪：pending。

## Iris: Dynamic Privacy Preserving Search in Authenticated Chord Peer-to-Peer Networks

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/iris-dynamic-privacy-preserving-search-in-authenticated-chord-peer-to-peer-networks/)；时间标记：NDSS 2025 within frozen rolling window; earliest online date not independently established。
- 作者：Angeliki Aktypi (University of Oxford), Kasper Rasmussen (University of Oxford)
- 对象：Chord, query privacy, access patterns；类型：countermeasure。
- 核心想法：隐藏 Chord 搜索向中间节点暴露的查询地址，并考虑多轮合谋观察。
- 作者报告：Iris 提出受 k-anonymity 启发的 alpha-delta 隐私定义，报告安全分析与 Matlab 原型的开销权衡。
- 限制与下一步：纳入访问过程隐私防护；特定查询隐私定义不是差分隐私或物理侧信道保证，安全前提仍待全文。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official NDSS paper-page abstract; selected formal PDF text only where recorded。
- [详细阅读记录](notes/ndss2025-static-power-quantum-and-scope-20261114.md)
- 代码/数据核查：not checked; official PDF link identified, no author code executed；引用追踪：pending。

## KernelSnitch: Side Channel-Attacks on Kernel Data Structures

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/kernelsnitch-side-channel-attacks-on-kernel-data-structures/)；时间标记：NDSS 2025 within frozen rolling window; earliest online date not independently established。
- 作者：Lukas Maar (Graz University of Technology), Jonas Juffinger (Graz University of Technology), Thomas Steinbauer (Graz University of Technology), Daniel Gruss (Graz University of Technology), Stefan Mangard (Graz University of Technology)
- 对象：kernel data structures, timing, website fingerprinting；类型：attack。
- 核心想法：利用内核哈希表和树的占用相关查询时间构造软件时序通道。
- 作者报告：KernelSnitch 报告最高 580 kbit/s 隐蔽通道、65 秒内内核堆指针泄漏和网站指纹案例。
- 限制与下一步：不依赖某一种缓存泄漏不等于没有平台约束；通道吞吐量、指针泄漏与网站 F1 不可互换。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official NDSS paper-page abstract; selected formal PDF text only where recorded。
- [详细阅读记录](notes/ndss2025-static-power-quantum-and-scope-20261114.md)
- 代码/数据核查：not checked; official PDF link identified, no author code executed；引用追踪：pending。

## LAMP: Lightweight Approaches for Latency Minimization in Mixnets with Practical Deployment Considerations

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/lamp-lightweight-approaches-for-latency-minimization-in-mixnets-with-practical-deployment-considerations/)；时间标记：NDSS 2025 within frozen rolling window; earliest online date not independently established。
- 作者：Mahdi Rahimi (KU Leuven), Piyush Kumar Sharma (University of Michigan), Claudia Diaz (KU Leuven)
- 对象：mixnets, traffic analysis, routing；类型：countermeasure。
- 核心想法：改进混合网络的路由延迟，同时评估流量观察下的匿名性损失。
- 作者报告：LAMP 使用 Nym 部署延迟数据评估多种路由方案，报告延迟与匿名性的权衡。
- 限制与下一步：属于网络流量分析防护；其传播延迟和计算开销改进不能直接当作端到端匿名保证，串谋与流量模型待全文。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official NDSS paper-page abstract; selected formal PDF text only where recorded。
- [详细阅读记录](notes/ndss2025-static-power-quantum-and-scope-20261114.md)
- 代码/数据核查：not checked; official PDF link identified, no author code executed；引用追踪：pending。

## LeakLess: Selective Data Protection against Memory Leakage Attacks for Serverless Platforms

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/leakless-selective-data-protection-against-memory-leakage-attacks-for-serverless-platforms/)；时间标记：NDSS 2025 within frozen rolling window; earliest online date not independently established。
- 作者：Maryam Rostamipoor (Stony Brook University), Seyedhamed Ghavamnia (University of Connecticut), Michalis Polychronakis (Stony Brook University)
- 对象：serverless, transient execution, memory encryption；类型：countermeasure。
- 核心想法：通过内存加密与隔离 I/O 模块保护 serverless 函数中的敏感数据。
- 作者报告：LeakLess 针对内存披露及瞬态执行威胁，在 Spin 和实际应用上评估同机或异机 I/O 配置。
- 限制与下一步：选择性数据保护依赖 I/O 与密钥边界；不同部署开销分开记录，不推广为功耗或所有共享资源无泄漏。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official NDSS paper-page abstract; selected formal PDF text only where recorded。
- [详细阅读记录](notes/ndss2025-static-power-quantum-and-scope-20261114.md)
- 代码/数据核查：not checked; official PDF link identified, no author code executed；引用追踪：pending。

## Lend Me Your Beam: Privacy Implications of Plaintext Beamforming Feedback in WiFi

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/lend-me-your-beam-privacy-implications-of-plaintext-beamforming-feedback-in-wifi/)；时间标记：NDSS 2025 within frozen rolling window; earliest online date not independently established。
- 作者：Rui Xiao (Zhejiang University), Xiankai Chen (Zhejiang University), Yinghui He (Nanyang Technological University), Jun Han (KAIST), Jinsong Han (Zhejiang University)
- 对象：Wi-Fi, beamforming feedback, occupancy；类型：attack and countermeasure。
- 核心想法：利用明文 Wi-Fi 波束成形反馈推断室内人员活动，并设计反馈混淆。
- 作者报告：LeakyBeam 在作者 20 米实测条件下报告真阳性率 82.7%、真阴性率 96.7%。
- 限制与下一步：两个条件率不是总体准确率；观察依赖未加密 BFI 与环境，硬件变更和防护覆盖尚待全文。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official NDSS paper-page abstract; selected formal PDF text only where recorded。
- [详细阅读记录](notes/ndss2025-static-power-quantum-and-scope-20261114.md)
- 代码/数据核查：not checked; official PDF link identified, no author code executed；引用追踪：pending。

## Non-intrusive and Unconstrained Keystroke Inference in VR Platforms via Infrared Side Channel

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/non-intrusive-and-unconstrained-keystroke-inference-in-vr-platforms-via-infrared-side-channel/)；时间标记：NDSS 2025 within frozen rolling window; earliest online date not independently established。
- 作者：Tao Ni (City University of Hong Kong), Yuefeng Du (City University of Hong Kong), Qingchuan Zhao (City University of Hong Kong), Cong Wang (City University of Hong Kong)
- 对象：VR, infrared, keystroke inference；类型：attack。
- 核心想法：以外部红外传感器阵列观察 VR 控制器的跟踪信号，推断虚拟键盘输入。
- 作者报告：VRecKey 在两个商用设备上报告字符与词级 top-3 识别结果，并测试多种环境因素。
- 限制与下一步：94.2% 和 90.5% 是摘要给出的 top-3 指标，不是 top-1；传感器摆放、轨迹与词先验待全文。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official NDSS paper-page abstract; selected formal PDF text only where recorded。
- [详细阅读记录](notes/ndss2025-static-power-quantum-and-scope-20261114.md)
- 代码/数据核查：not checked; official PDF link identified, no author code executed；引用追踪：pending。

## Off-Path TCP Hijacking in Wi-Fi Networks: A Packet-Size Side Channel Attack

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/off-path-tcp-hijacking-in-wi-fi-networks-a-packet-size-side-channel-attack/)；时间标记：NDSS 2025 within frozen rolling window; earliest online date not independently established。
- 作者：Ziqiang Wang (Southeast University), Xuewei Feng (Tsinghua University), Qi Li (Tsinghua University), Kun Sun (George Mason University), Yuxiang Yang (Tsinghua University), Mengyuan Li (University of Toronto), Ganqiu Du (China Software Testing Center), Ke Xu (Tsinghua University), Jianping Wu (Tsinghua University)
- 对象：Wi-Fi, packet size, TCP；类型：attack。
- 核心想法：利用加密 Wi-Fi 帧大小区分 TCP 响应，辅助离路径连接劫持。
- 作者报告：作者在 30 款路由器和 80 个实际网络上评估，报告 SSH 中断和网页流量操纵案例。
- 限制与下一步：帧大小观察与主动探测能力需同时满足；19/28 秒案例成本与 75/80 网络成功数属于不同评估，不能当作解密能力。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official NDSS paper-page abstract; selected formal PDF text only where recorded。
- [详细阅读记录](notes/ndss2025-static-power-quantum-and-scope-20261114.md)
- 代码/数据核查：not checked; official PDF link identified, no author code executed；引用追踪：pending。

## On Borrowed Time – Preventing Static Side-Channel Analysis

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/on-borrowed-time-preventing-static-side-channel-analysis/)；时间标记：NDSS 2025 within frozen rolling window; earliest online date not independently established。
- 作者：Robert Dumitru; Thorben Moos; Andrew Wabnitz; Yuval Yarom
- 对象：static power, LLSI, impedance, AES, SKINNY, masked clearing；类型：countermeasure。
- 核心想法：检测时钟停顿并随机清理临时敏感寄存器，限制静态观察窗口。
- 作者报告：在 FPGA 上对未保护 AES 和一阶掩码 SKINNY 的静态功耗测试中，作者报告启用防护后百万迹线未恢复子密钥。
- 限制与下一步：假设根密钥存储安全。LLSI/阻抗防护未实测；PLL 与异步方案的门控兼容性不同，功率门控 ASIC 和侵入式电路编辑不在已证覆盖内。
- 阅读层级：selected_full_text_sections；来源：official NDSS paper-page abstract; selected formal PDF text only where recorded。
- 已读章节：PDF p.6: threat model and secure root-key storage; PDF p.9: asynchronous clearing and Table I; rendered; PDF p.14: attack results and limitations; PDF pp.15-16: eight selected references only
- [详细阅读记录](notes/ndss2025-static-power-quantum-and-scope-20261114.md)
- 代码/数据核查：not checked; official PDF link identified, no author code executed；引用追踪：selected backward references in progress。

## Oreo: Protecting ASLR Against Microarchitectural Attacks

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/oreo-protecting-aslr-against-microarchitectural-attacks/)；时间标记：NDSS 2025 within frozen rolling window; earliest online date not independently established。
- 作者：Shixin Song (Massachusetts Institute of Technology), Joseph Zhang (Massachusetts Institute of Technology), Mengjia Yan (Massachusetts Institute of Technology)
- 对象：ASLR, address mapping, microarchitecture, gem5；类型：countermeasure。
- 核心想法：通过新的内存映射接口隐藏 ASLR 随机化位，减少微架构可见的地址秘密。
- 作者报告：Oreo 在虚拟到物理地址转换前移除秘密随机位，并在 Linux 与 gem5 上实现和评估。
- 限制与下一步：摘要明确为硬件模拟器评估，不能当作已生产或实测芯片防护；具体泄漏路径、证明范围和物理功耗不在摘要保证内。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official NDSS paper-page abstract; selected formal PDF text only where recorded。
- [详细阅读记录](notes/ndss2025-static-power-quantum-and-scope-20261114.md)
- 代码/数据核查：not checked; official PDF link identified, no author code executed；引用追踪：pending。

## Power-Related Side-Channel Attacks using the Android Sensor Framework

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/power-related-side-channel-attacks-using-the-android-sensor-framework/)；时间标记：NDSS 2025 within frozen rolling window; earliest online date not independently established。
- 作者：Mathias Oberhuber; Martin Unterguggenberger; Lukas Maar; Andreas Kogler; Stefan Mangard
- 对象：Android, power proxies, geomagnetic rotation, AES；类型：attack。
- 核心想法：研究 Android 传感器对功耗的寄生响应，并展示像素推断与 AES 候选排名降低。
- 作者报告：正文在 Pixel 6a 本地应用条件下分析恒周期 ARM AES；部分字节在 CPA 中出现排名下降，仍有字节不收敛。
- 限制与下一步：没有完整密钥恢复；本地 AES 与浏览器像素场景权限不同。采集 35.6M、过滤后 17.8M 和图示至 300K 样本的预算不能混为 300K 次加密。
- 阅读层级：selected_full_text_sections；来源：official NDSS paper-page abstract; selected formal PDF text only where recorded。
- 已读章节：PDF pp.12-13: local-app AES threat model, acquisition budget and rank reduction; p.13 rendered
- [详细阅读记录](notes/ndss2025-static-power-quantum-and-scope-20261114.md)
- 代码/数据核查：not checked; official PDF link identified, no author code executed；引用追踪：pending。

## RadSee: See Your Handwriting Through Walls Using FMCW Radar

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/radsee-see-your-handwriting-through-walls-using-fmcw-radar/)；时间标记：NDSS 2025 within frozen rolling window; earliest online date not independently established。
- 作者：Shichen Zhang (Michigan State University), Qijun Wang (Michigan State University), Maolin Gan (Michigan State University), Zhichao Cao (Michigan State University), Huacheng Zeng (Michigan State University)
- 对象：radar, handwriting, phase；类型：attack。
- 核心想法：以 6 GHz FMCW 雷达的相位特征推断隔墙手写内容。
- 作者报告：RadSee 将定制高增益天线与 BiLSTM 分类结合，报告随机字符和文章词识别的不同评估。
- 限制与下一步：主动雷达人体动作观察，不是密码芯片辐射；75% 字符与 87% 词识别对应不同输入分布，不能直接比较。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official NDSS paper-page abstract; selected formal PDF text only where recorded。
- [详细阅读记录](notes/ndss2025-static-power-quantum-and-scope-20261114.md)
- 代码/数据核查：not checked; official PDF link identified, no author code executed；引用追踪：pending。

## ReDAN: An Empirical Study on Remote DoS Attacks against NAT Networks

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/redan-an-empirical-study-on-remote-dos-attacks-against-nat-networks/)；时间标记：NDSS 2025 within frozen rolling window; earliest online date not independently established。
- 作者：Xuewei Feng (Tsinghua University), Yuxiang Yang (Tsinghua University), Qi Li (Tsinghua University), Xingxiang Zhan (Zhongguancun Lab), Kun Sun (George Mason University), Ziqiang Wang (Southeast University), Ao Wang (Southeast University), Ganqiu Du (China Software Testing Center), Ke Xu (Tsinghua University)
- 对象：NAT, PMTUD, network side channel；类型：attack。
- 核心想法：利用 PMTUD 相关侧信道辨别 NAT，再研究远程破坏连接映射。
- 作者报告：ReDAN 分开执行 NAT 识别与连接终止，在多种固件、设备和网络环境中评估。
- 限制与下一步：识别侧信道与后续 DoS 漏洞是两层机制；166/180 网络易受攻击不是 NAT 检测准确率，修补状态限论文时点。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official NDSS paper-page abstract; selected formal PDF text only where recorded。
- [详细阅读记录](notes/ndss2025-static-power-quantum-and-scope-20261114.md)
- 代码/数据核查：not checked; official PDF link identified, no author code executed；引用追踪：pending。

## Secret Spilling Drive: Leaking User Behavior through SSD Contention

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/secret-spilling-drive-leaking-user-behavior-through-ssd-contention/)；时间标记：NDSS 2025 within frozen rolling window; earliest online date not independently established。
- 作者：Jonas Juffinger (Graz University of Technology), Fabian Rauscher (Graz University of Technology), Giuseppe La Manna (Amazon), Daniel Gruss (Graz University of Technology)
- 对象：SSD, contention, timing, website fingerprinting；类型：attack。
- 核心想法：以并发 I/O 引起的 SSD 争用时延建立跨进程及跨虚拟机观察。
- 作者报告：作者评估 12 款 SSD，展示最高 1503 bit/s 隐蔽通道及开放世界网站指纹案例。
- 限制与下一步：受害者读取块数、通道容量和网站 F1 对应不同测量；摘要 F1 写作 97.0，单位及拆分需全文确认，不推广为密码恢复。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official NDSS paper-page abstract; selected formal PDF text only where recorded。
- [详细阅读记录](notes/ndss2025-static-power-quantum-and-scope-20261114.md)
- 代码/数据核查：not checked; official PDF link identified, no author code executed；引用追踪：pending。

## Speak Up, I’m Listening: Extracting Speech from Zero-Permission VR Sensors

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/speak-up-im-listening-extracting-speech-from-zero-permission-vr-sensors/)；时间标记：NDSS 2025 within frozen rolling window; earliest online date not independently established。
- 作者：Derin Cayir (Florida International University), Reham Mohamed Aburas (American University of Sharjah), Riccardo Lazzeretti (Sapienza University of Rome), Marco Angelini (Link Campus University of Rome), Abbas Acar (Florida International University), Mauro Conti (University of Padua), Z. Berkay Celik (Purdue University), Selcuk Uluagac (Florida International University)
- 对象：VR, motion sensors, acoustic, speech；类型：attack and countermeasure。
- 核心想法：利用 VR 运动传感器记录扬声器诱发的振动，识别语音数字。
- 作者报告：IMMERSPY 比较有无受害者标签的场景，并使用生成语音构建训练资料，另提出不可闻音调防护。
- 限制与下一步：摘要 74% 四位与 62% 十六位结果需核对对应攻击先验；观察目标是设备扬声器引起的振动，不能泛化为任意环境会话窃听。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official NDSS paper-page abstract; selected formal PDF text only where recorded。
- [详细阅读记录](notes/ndss2025-static-power-quantum-and-scope-20261114.md)
- 代码/数据核查：not checked; official PDF link identified, no author code executed；引用追踪：pending。

## The Discriminative Power of Cross-layer RTTs in Fingerprinting Proxy Traffic

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/the-discriminative-power-of-cross-layer-rtts-in-fingerprinting-proxy-traffic/)；时间标记：NDSS 2025 within frozen rolling window; earliest online date not independently established。
- 作者：Diwen Xue (University of Michigan), Robert Stanley (University of Michigan), Piyush Kumar (University of Michigan), Roya Ensafi (University of Michigan)
- 对象：network timing, RTT, proxy fingerprinting；类型：attack。
- 核心想法：用传输层与应用层 RTT 的差异识别混淆代理流量。
- 作者报告：作者将代理引起的会话错位作为跨协议指纹，在受控网络及合作 ISP 流量上评估。
- 限制与下一步：两层计时的可获得性、路由与背景负载影响待全文；协议无关性不等于任意网络中识别可靠。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official NDSS paper-page abstract; selected formal PDF text only where recorded。
- [详细阅读记录](notes/ndss2025-static-power-quantum-and-scope-20261114.md)
- 代码/数据核查：not checked; official PDF link identified, no author code executed；引用追踪：pending。

## Wallbleed: A Memory Disclosure Vulnerability in the Great Firewall of China

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/wallbleed-a-memory-disclosure-vulnerability-in-the-great-firewall-of-china/)；时间标记：NDSS 2025 within frozen rolling window; earliest online date not independently established。
- 作者：Shencha Fan; Jackson Sippe; Sakamoto San; Jade Sheffey; David Fifield; Amir Houmansadr; Elson Wedwards; Eric Wustrow
- 对象：DNS, sequence side channel, process fingerprinting；类型：measurement and attack。
- 核心想法：分析 DNS 注入器的内存越界读取，同时通过伪造地址返回顺序辨认内部进程。
- 作者报告：正文将每个响应池的循环索引作为独立于 Wallbleed 内存泄漏的侧信道，辅助识别负载分配关系。
- 限制与下一步：主要漏洞是缓冲区越界读；纳入理由是另有明确的顺序侧信道，不将任意内存披露都称作侧信道。历史修补和系统归因限作者观察。
- 阅读层级：selected_full_text_sections；来源：official NDSS paper-page abstract; selected formal PDF text only where recorded。
- 已读章节：PDF p.10 V-B: ordered false-address pools and process inference
- [详细阅读记录](notes/ndss2025-static-power-quantum-and-scope-20261114.md)
- 代码/数据核查：not checked; official PDF link identified, no author code executed；引用追踪：pending。

## You Can Rand but You Can’t Hide: A Holistic Security Analysis of Google Fuchsia’s (and gVisor’s) Network Stack

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/you-can-rand-but-you-cant-hide-a-holistic-security-analysis-of-google-fuchsias-and-gvisors-network-stack/)；时间标记：NDSS 2025 within frozen rolling window; earliest online date not independently established。
- 作者：Inon Kaplan (Independent researcher), Ron even (Independent researcher), Amit Klein (The Hebrew University of Jerusalem, Israel)
- 对象：Fuchsia, gVisor, PRNG, device tracking；类型：attack。
- 核心想法：联合分析网络首部字段生成规则，推断 PRNG 种子和散列键以跟踪设备。
- 作者报告：作者在 Fuchsia 的浏览器模式和 IPv4/IPv6 网络条件下展示稳定设备标识，涉及与 gVisor 共用的网络栈。
- 限制与下一步：这是网络可见字段的算法泄漏，不是 CPU 功耗；版本与修补范围需全文，摘要中未来平台预测不作为当前事实。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official NDSS paper-page abstract; selected formal PDF text only where recorded。
- [详细阅读记录](notes/ndss2025-static-power-quantum-and-scope-20261114.md)
- 代码/数据核查：not checked; official PDF link identified, no author code executed；引用追踪：pending。

## Et tu, Brute? Side-Channel Assisted Chosen Ciphertext Attacks Using Valid Ciphertexts on HQC KEM

- 来源：[PQCrypto 2025](https://doi.org/10.1007/978-3-031-86602-9_11)；时间标记：within rolling five-year window。
- 作者：Thales B. Paiva; Prasanna Ravi; Dirmanto Jap; Shivam Bhasin; Sayan Das; Anupam Chattopadhyay
- 对象：HQC, Reed-Muller, chosen ciphertext；类型：attack。
- 核心想法：研究使用有效密文的侧信道辅助选择密文攻击，针对 HQC 译码的 ExpandAndSum 与 FindPeaks。
- 作者报告：摘要报告指定实验中的完整密钥恢复及对打乱的扩展，用以分析依赖无效密文检测的防护。
- 限制与下一步：100% 是作者所测条件的报告；平台、采集预算与准确版本待全文。不能泛化到所有 HQC 实现或最终标准；只核查摘要和参考列表。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://link.springer.com/chapter/10.1007/978-3-031-86602-9_11。
- [详细阅读记录](notes/mpcith-revisions-and-evidence-20261113.md)
- 代码/数据核查：not inspected; no author code executed；引用追踪：all 30 entries screened: 19 linked, 11 provisional background; original 11 discoveries resolved; recursive/forward closure incomplete。

## Single Trace Side-Channel Attack on the MPC-in-the-Head Framework

- 来源：[PQCrypto 2025](https://doi.org/10.1007/978-3-031-86602-9_10)；时间标记：within rolling five-year window。
- 作者：Julie Godard; Nicolas Aragon; Philippe Gaborit; Antoine Loiseau; Julien Maillard
- 对象：SDitH, TCitH, SASCA；类型：attack。
- 核心想法：利用有限域乘法泄漏和多项式求值约束构造针对阈值 MPCitH 的软分析攻击。
- 作者报告：作者报告 HW 模拟及 STM32F407 实测，并称各安全等级均可单迹线恢复目标私钥。
- 限制与下一步：对象是原始阈值 TCitH/SDitH 结构；单条攻击迹线不等于无需剖析。训练预算、完整参数和正文尚未核查；预印本到正式版本关系仅作原始来源推定。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://link.springer.com/chapter/10.1007/978-3-031-86602-9_10; https://eprint.iacr.org/2024/1882。
- [详细阅读记录](notes/mpcith-revisions-and-evidence-20261113.md)
- 代码/数据核查：not inspected; no author code executed；引用追踪：pending except explicitly linked references。

## SoK: On the Physical Security of UOV-Based Signature Schemes

- 来源：[PQCrypto 2025](https://doi.org/10.1007/978-3-031-86599-2_7)；时间标记：within frozen rolling window。
- 作者：Thomas Aulbach; Fabio Campos; Juliane Krämer
- 对象：UOV, MAYO, QR-UOV, SNOVA；类型：survey and countermeasure。
- 核心想法：按 UOV 规范及实现选择重新梳理侧信道与故障攻击，并讨论向相关签名方案的迁移。
- 作者报告：作者摘要报告 UOV/MAYO 的 Cortex-M4 一阶掩码与部分故障防护，并对所选子程序进行 TVLA。
- 限制与下一步：仅读正式及 ePrint 摘要；保护范围与密钥压缩、随机化选择相关。更小 t 值不等于全面无泄漏，不能把 UOV/MAYO 实测外推为 QR-UOV/SNOVA 同板实测。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://link.springer.com/chapter/10.1007/978-3-031-86599-2_7。
- [详细阅读记录](notes/muov-followups-and-masked-sampling-20261114.md)
- 代码/数据核查：no author code/data executed; artifact completeness not inspected；引用追踪：pending except explicit inventories。

## Single-trace Side-Channel Attacks on MAYO Exploiting Leaky Modular Multiplication

- 来源：[QRSEC 2025](https://doi.org/10.1145/3733820.3764682)；时间标记：within rolling five-year window by publication date。
- 作者：Sönke Jendral; Elena Dubrova
- 对象：MAYO, multivariate signatures；类型：attack。
- 核心想法：正式 QRSEC 版本研究模乘泄漏到 oil space 向量、再到秘密的代数恢复。
- 作者报告：机构保存的正式版本摘要报告 Cortex-M4 两种方法成功率 99.4% 与 93.1%。
- 限制与下一步：ePrint 当前摘要为 99.9% 与 91.6%；关联由 ePrint DOI 明确，但数值差异原因未核实。机构直接页面为挑战页，实际阅读搜索索引完整摘要；非全文预算确认。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://kth.diva-portal.org/smash/person.jsf?pid=authority-person%3A111623; https://api.crossref.org/works/10.1145/3733820.3764682; https://eprint.iacr.org/2024/1850。
- [详细阅读记录](notes/pqc-citation-followups-and-evidence-20261113.md)
- 代码/数据核查：no author code or data executed; artifact contents not inspected；引用追踪：pending except explicitly inventoried citations。

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

## A Hardware-Friendly Shuffling Countermeasure Against Side-Channel Attacks for Kyber

- 来源：[TCAS-II 2025](https://doi.org/10.1109/tcsii.2025.3528751)；时间标记：within frozen rolling window; publication and version dates retained。
- 作者：Dejun Xu; Kai Wang; Jing Tian
- 对象：Kyber, FPGA, shuffling, EM, CPA, TVLA；类型：hardware_countermeasure。
- 核心想法：修改 Fisher–Yates 并设计硬件地址打乱架构，评价 Kyber FPGA 保护与面积时间成本。
- 作者报告：arXiv v5 的图 4 报告保护版 100,000 条 EM CPA 与 10,000,000 条 EM TVLA；§IV 在 Artix-7 Kyber768 上评价。
- 限制与下一步：CPA 针对点乘，TVLA 针对解密；未逐项展示的约减/减法不能当作本项目核验。有限预算 TVLA 不证明全部已知或潜在泄漏点安全；故障保护列为未来工作。
- 阅读层级：selected_full_text_sections；来源：https://arxiv.org/abs/2407.02452v5。
- 已读章节：五页 arXiv v5 PDF 第 1 页摘要、第 4–5 页 §IV–VI、图 4、表 II 及九条选读参考；第 4 页已视觉核查。
- [详细阅读记录](notes/kyber-multiplication-and-shuffling-20261113.md)
- 代码/数据核查：not inspected；引用追踪：all 17 bibliography entries identity/scope screened; original seven discoveries resolved; recursive/forward tracing incomplete。

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

## ALERT: Machine Learning-Enhanced Risk Estimation for Databases Supporting Encrypted Queries

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/wang-longxiang)；时间标记：USENIX 2025 conference 2025-08-13 to 2025-08-15 within frozen window; earliest online date not established。
- 作者：Longxiang Wang, City University of Hong Kong; Lei Xu, Nanjing University of Science and Technology and City University of Hong Kong; Yufei Chen, City University of Hong Kong; Ying Zou, Nanjing University of Science and Technology; Cong Wang, City University of Hong Kong
- 对象：searchable symmetric encryption；类型：leakage risk estimation。
- 核心想法：用辅助特征与机器学习估计可搜索加密数据库的查询模式泄漏风险。
- 作者报告：作者报告在线风险估计及相对既有分析的加速。
- 限制与下一步：风险分数和运行加速不是安全证明或秘密恢复率；依赖查询及辅助信息模型。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX technical-session abstract。
- [详细阅读记录](notes/usenix2025-scope-blind-analysis-and-counter-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## BarraCUDA: Edge GPUs do Leak DNN Weights

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/horvath)；时间标记：USENIX 2025 conference 2025-08-13 to 2025-08-15 within frozen window; earliest online date not established。
- 作者：Peter Horvath, Radboud University; Lukasz Chmielewski, Masaryk University, Radboud University; Léo Weissbart and Lejla Batina, Radboud University; Yuval Yarom, Ruhr University Bochum
- 对象：DNN convolution；类型：physical EM attack。
- 核心想法：通过边缘 GPU 的电磁观察与卷积部分和关系推断 DNN 权重。
- 作者报告：作者在 NVIDIA Jetson 上报告权重恢复。
- 限制与下一步：假定物理观察及目标卷积实现；神经网络权重不是密码密钥，不能外推到所有 GPU。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX technical-session abstract。
- [详细阅读记录](notes/usenix2025-scope-blind-analysis-and-counter-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## Branch Privilege Injection: Compromising Spectre v2 Hardware Mitigations by Exploiting Branch Predictor Race Conditions

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/ruegge)；时间标记：USENIX 2025 conference 2025-08-13 to 2025-08-15 within frozen window; earliest online date not established。
- 作者：Sandro Rüegge, Johannes Wikner, and Kaveh Razavi, ETH Zurich Distinguished Paper Award Winner
- 对象：branch prediction, Spectre v2；类型：microarchitectural attack。
- 核心想法：利用分支预测器异步反馈的竞争条件跨越预测隔离边界。
- 作者报告：作者报告三类跨边界变体，并在六代 Intel CPU 上演示内核信息泄漏。
- 限制与下一步：需保留具体处理器与隔离配置；Raptor Cove 的 5.6 KiB/s 是所述场景性能。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX technical-session abstract。
- [详细阅读记录](notes/usenix2025-scope-blind-analysis-and-counter-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## Breaking the Blindfold: Deep Learning-based Blind Side-channel Analysis

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/rezaeezade)；时间标记：USENIX 2025 conference 2025-08-13 to 2025-08-15 within frozen window; earliest online date not established。
- 作者：Azade Rezaeezade, Delft University of Technology and Digital Security Group, Radboud University; Trevor Yap, Dirmanto Jap, and Shivam Bhasin, Temasek Laboratories and National integrated Centre For Evaluation, Nanyang Technological University; Stjepan Picek, Digital Security Group, Radboud University and University of Zagreb Faculty of Electrical Engineering and Computing
- 对象：AES, Ascon, Kyber；类型：blind side-channel analysis。
- 核心想法：用多点聚类和深度学习学习联合泄漏分布；Kyber 部分评价固定实现中单个 NTT 系数的候选排名。
- 作者报告：正文表 3 的 CNN+MC 为 GE=2.01、MLP+MC 为 9.2；Kyber 固定密钥数据 10 万条，8 万训练、2 万攻击池，每次抽 5000 条重复 100 次。
- 限制与下一步：选点使用真实 HW 与测量相关性；GE≤10 是平均排名指标，不保证每次位于前十，更不等于完整 Kyber 密钥恢复。实测掩码攻击仍开放；100 个候选网络及部分 top-10 选择的预算和真值使用需后续审计。
- 阅读层级：selected_full_text_sections；来源：official USENIX technical-session abstract; selected final proceedings PDF sections。
- 已读章节：PDF pp.6-7,9-11,14-16,19-20: threat/PoI assumptions, learning setup, Kyber target/results, limitations, artifact statement and appendices A/B; all 58 references on pp.16-19 initially screened; Table 3 p11 visually checked. Not a complete proof/artifact audit.
- [详细阅读记录](notes/usenix2025-scope-blind-analysis-and-counter-bounds-20261114.md)
- 代码/数据核查：PDF p16 links version DOI 10.5281/zenodo.15614359 and parent search 15612978; contents not inspected or executed；引用追踪：All 58 entries initially screened; now 19 linked, 26 pending discoveries, 13 provisional background. Ten original discoveries resolved this batch; recursive and forward closure incomplete.。

## DNS FLaRE: A Flush-Reload Attack on DNS Forwarders

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/moav)；时间标记：USENIX 2025 conference 2025-08-13 to 2025-08-15 within frozen window; earliest online date not established。
- 作者：Gilad Moav, Yehuda Afek, and Anat Bremler-Barr, Tel Aviv University; Amit Klein, Hebrew University of Jerusalem
- 对象：DNS caching；类型：cache timing attack。
- 核心想法：从网页利用 DNS 转发器缓存的时间差推断访问与家庭设备活动。
- 作者报告：作者提出 DNS FLaRE 缓存刷新与重载观察。
- 限制与下一步：依赖转发器、缓存及浏览器条件；不表示解密 DNS 内容。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX technical-session abstract。
- [详细阅读记录](notes/usenix2025-scope-blind-analysis-and-counter-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## DiskSpy: Exploring a Long-Range Covert-Channel Attack via mmWave Sensing of μm-level HDD Vibrations

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/xu-weiye)；时间标记：USENIX 2025 conference 2025-08-13 to 2025-08-15 within frozen window; earliest online date not established。
- 作者：Weiye Xu, Zhejiang University; China Mobile Research Institute; Danli Wen, Zhejiang University; Jianwei Liu, Zhejiang University; Hangzhou City University; Zixin Lin, Zhejiang University; Yuanqing Zheng, The Hong Kong Polytechnic University; Xian Xu and Jinsong Han, Zhejiang University
- 对象：HDD vibration；类型：physical covert channel。
- 核心想法：利用毫米波雷达读取 HDD 微小振动构造隐蔽信道。
- 作者报告：作者报告 22 米、20 bps 及低于 1.2% 的误码率场景。
- 限制与下一步：需要合作的编码发送端或恶意软件；隐蔽通信不等于被动恢复任意受害者秘密。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX technical-session abstract。
- [详细阅读记录](notes/usenix2025-scope-blind-analysis-and-counter-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## Double-Edged Shield: On the Fingerprintability of Customized Ad Blockers

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/el-hajj-chehade)；时间标记：USENIX 2025 conference 2025-08-13 to 2025-08-15 within frozen window; earliest online date not established。
- 作者：Saiid El Hajj Chehade, EPFL; Ben Stock, CISPA Helmholtz Center for Information Security; Carmela Troncoso, EPFL and Max-Planck Institute for Security and Privacy (MPI-SP)
- 对象：browser ad blocking；类型：configuration fingerprinting。
- 核心想法：通过无脚本规则探测识别定制广告拦截列表并形成用户指纹。
- 作者报告：作者报告过滤列表识别、熵及匿名集合大小评估。
- 限制与下一步：列表配置和用户总体决定区分力；中位匿名集合 48 不等于唯一识别全部用户。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX technical-session abstract。
- [详细阅读记录](notes/usenix2025-scope-blind-analysis-and-counter-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## EchoLLM: LLM-Augmented Acoustic Eavesdropping Attack on Bone Conduction Headphones with mmWave Radar

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/yao-xin)；时间标记：USENIX 2025 conference 2025-08-13 to 2025-08-15 within frozen window; earliest online date not established。
- 作者：Xin Yao and Kecheng Huang, Central South University; Yimin Chen, University of Massachusetts Lowell; Jiawei Guo, Jie Tang, and Ming Zhao, Central South University
- 对象：bone conduction, ASR；类型：physical acoustic inference。
- 核心想法：毫米波雷达感知骨传导耳机振动，结合使用者语音上下文辅助重建声音。
- 作者报告：作者报告 LLM 辅助的多模态 ASR，并给出最低 5.23% WER 场景。
- 限制与下一步：依赖物理位置、上下文与语言先验；最佳 WER 不是无条件逐字恢复保证。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX technical-session abstract。
- [详细阅读记录](notes/usenix2025-scope-blind-analysis-and-counter-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## Endangered Privacy: Large-Scale Monitoring of Video Streaming Services

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/bjorklund)；时间标记：USENIX 2025 conference 2025-08-13 to 2025-08-15 within frozen window; earliest online date not established。
- 作者：Martin Björklund and Romaric Duvignau, Chalmers University of Technology and University of Gothenburg
- 对象：DASH；类型：encrypted traffic analysis。
- 核心想法：通过加密 DASH 自适应码率流量的模式识别视频。
- 作者报告：作者在三个服务约 24 万视频及 VPN/WiFi 场景报告评估。
- 限制与下一步：依赖视频指纹库、先验和采集预算；高分类率不是 TLS 解密或任意视频覆盖。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX technical-session abstract。
- [详细阅读记录](notes/usenix2025-scope-blind-analysis-and-counter-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## Exploiting Inaccurate Branch History in Side-Channel Attacks

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/zhu-yuhui)；时间标记：USENIX 2025 conference 2025-08-13 to 2025-08-15 within frozen window; earliest online date not established。
- 作者：Yuhui Zhu, Scuola Superiore Sant'Anna and Scuola IMT Alti Studi Lucca; Alessandro Biondi, Scuola Superiore Sant'Anna
- 对象：branch history, Spectre；类型：microarchitectural attack。
- 核心想法：利用分支历史表示不准确及推测更新形成预测与控制流侧信道。
- 作者报告：作者提出 Spectre BSE/BHS、BiasScope 与 eBPF 内核演示 Chimera。
- 限制与下一步：24628 bit/s 是指定演示的比特率，不能改写成字节率或普遍处理器性能。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX technical-session abstract。
- [详细阅读记录](notes/usenix2025-scope-blind-analysis-and-counter-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## FLOP: Breaking the Apple M3 CPU via False Load Output Predictions

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/kim-jason)；时间标记：USENIX 2025 conference 2025-08-13 to 2025-08-15 within frozen window; earliest online date not established。
- 作者：Jason Kim, Jalen Chuang, and Daniel Genkin, Georgia Tech; Yuval Yarom, Ruhr University Bochum
- 对象：load value prediction；类型：transient execution attack。
- 核心想法：利用 Apple M/A 系列的装载值预测器构造瞬态读出。
- 作者报告：作者提出 FLOP 并在 Safari 和 Chrome 演示攻击。
- 限制与下一步：小值预测与构造出的 64 位读取应区分；依赖具体芯片、浏览器及实现条件。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX technical-session abstract。
- [详细阅读记录](notes/usenix2025-scope-blind-analysis-and-counter-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## Flexway O-Sort: Enclave-Friendly and Optimal Oblivious Sorting

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/gu-tianyao)；时间标记：USENIX 2025 conference 2025-08-13 to 2025-08-15 within frozen window; earliest online date not established。
- 作者：Tianyao Gu, Carnegie Mellon University and Oblivious Labs Inc.; Yilei Wang, Alibaba Cloud; Afonso Tinoco, Carnegie Mellon University and Oblivious Labs Inc.; Bingnan Chen and Ke Yi, HKUST; Elaine Shi, Carnegie Mellon University and Oblivious Labs Inc.
- 对象：oblivious sorting, SGX；类型：access-pattern defense。
- 核心想法：面向 enclave 内外存储设计高效 oblivious 排序。
- 作者报告：作者报告 Flexway O-Sort 在不同输入规模下的性能。
- 限制与下一步：保证针对声明的访问模式；不自动覆盖功耗、电磁和全部微架构观察。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX technical-session abstract。
- [详细阅读记录](notes/usenix2025-scope-blind-analysis-and-counter-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## Found in Translation: A Generative Language Modeling Approach to Memory Access Pattern Attacks

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/jia-grace)；时间标记：USENIX 2025 conference 2025-08-13 to 2025-08-15 within frozen window; earliest online date not established。
- 作者：Grace Jia, Alex Wong, and Anurag Khandelwal, Yale University
- 对象：page access patterns, sequence modeling；类型：controlled-channel inference。
- 核心想法：以生成式序列模型把操作系统可见页访问模式映射到对象访问。
- 作者报告：作者在 AI 推理与语义检索报告 71.7% 至 99.9% 的任务结果。
- 限制与下一步：需要 OS 观察/控制及相应剖析对象映射；不是任意密文到明文的通用翻译。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX technical-session abstract。
- [详细阅读记录](notes/usenix2025-scope-blind-analysis-and-counter-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## H2O2RAM: A High-Performance Hierarchical Doubly Oblivious RAM

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/zheng)；时间标记：USENIX 2025 conference 2025-08-13 to 2025-08-15 within frozen window; earliest online date not established。
- 作者：Leqian Zheng, City University of Hong Kong; Zheng Zhang, ByteDance Inc.; Wentao Dong, City University of Hong Kong; Yao Zhang and Ye Wu, ByteDance Inc.; Cong Wang, City University of Hong Kong
- 对象：O2RAM, TEE；类型：access-pattern defense。
- 核心想法：以分层结构构建同时隐藏 TEE 内外访问模式的 doubly oblivious RAM。
- 作者报告：作者报告 H2O2RAM 的时间与内存开销优势。
- 限制与下一步：最大约千倍加速及 5 至 44 倍节省依赖比较场景；双重 oblivious 不等于抵御所有物理观察。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX technical-session abstract。
- [详细阅读记录](notes/usenix2025-scope-blind-analysis-and-counter-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## HubBub: Contention-Based Side-Channel Attacks on USB Hubs

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/wan)；时间标记：USENIX 2025 conference 2025-08-13 to 2025-08-15 within frozen window; earliest online date not established。
- 作者：Junpeng Wan, Purdue University; Yanxiang Bi, The Chinese University of Hong Kong; Han Gao and Dave (Jing) Tian, Purdue University
- 对象：USB contention；类型：contention timing attack。
- 核心想法：通过 USB hub 的共享总线争用时间变化推断用户活动。
- 作者报告：作者在 VM、网页与 USB 外设场景评估浏览、相机活动及按键信息，报告 85% 至 99% 准确率。
- 限制与下一步：三种观察能力与场景不能混合；多数受测 hub 脆弱不代表全部 USB 设备。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX technical-session abstract。
- [详细阅读记录](notes/usenix2025-scope-blind-analysis-and-counter-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## I Know What You Said: Unveiling Hardware Cache Side-Channels in Local Large Language Model Inference

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/gao-zibo)；时间标记：USENIX 2025 conference 2025-08-13 to 2025-08-15 within frozen window; earliest online date not established。
- 作者：Zibo Gao, Junjie Hu, Feng Guo, Yixin Zhang, Yinglong Han, Siyuan Liu, Haiyang Li, and Zhiqiang Lv, Institute of Information Engineering, Chinese Academy of Sciences and School of Cyber Security, University of Chinese Academy of Sciences
- 对象：Llama, Falcon LLM, Gemma；类型：cache attack。
- 核心想法：利用本地 LLM 嵌入操作的缓存模式及自回归阶段时序推断 token 值和位置。
- 作者报告：作者报告输入/输出文本重建的编辑距离与余弦相似度指标。
- 限制与下一步：依赖本地共存、模型及推理实现；Falcon 在这里是语言模型，不是后量子签名。相似度不是逐字恢复率。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX technical-session abstract。
- [详细阅读记录](notes/usenix2025-scope-blind-analysis-and-counter-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## Mitigating Injection Attacks against E2EE Applications via View-Based Partitioning

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/fabrega-partitioning)；时间标记：USENIX 2025 conference 2025-08-13 to 2025-08-15 within frozen window; earliest online date not established。
- 作者：Andrés Fábrega, Samuel Breckenridge, and Armin Namavari, Cornell University; Thomas Ristenpart, Cornell Tech
- 对象：E2EE backups, compression；类型：leakage defense and formal model。
- 核心想法：对 E2EE 应用中的注入、压缩与加密备份可观察状态建立模型，以视图划分阻断机密推断。
- 作者报告：作者给出形式模型与安全证明，并评估 SQLite/XML 备份实现开销。
- 限制与下一步：证明限声明的注入及观察模型；压缩侧信道防护不等于消除所有 E2EE 实现泄漏。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX technical-session abstract。
- [详细阅读记录](notes/usenix2025-scope-blind-analysis-and-counter-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## Not so Refreshing: Attacking GPUs using RFM Rowhammer Mitigation

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/nazaraliyev)；时间标记：USENIX 2025 conference 2025-08-13 to 2025-08-15 within frozen window; earliest online date not established。
- 作者：Ravan Nazaraliyev and Yicheng Zhang, University of California, Riverside; Sankha Baran Dutta, Brookhaven National Laboratory; Andres Marquez and Kevin Barker, Pacific Northwest National Laboratory; Nael Abu-Ghazaleh, University of California, Riverside
- 对象：RFM, GDDR6, LPDDR5；类型：memory timing attack。
- 核心想法：利用 GPU 内存 Rowhammer 防护 RFM 触发的时间差构造隐蔽与侧信道。
- 作者报告：作者在 GDDR6/LPDDR5 平台演示指纹识别、每 bank 超过 50 KBps 的隐蔽信道及 DoS。
- 限制与下一步：这是防护引出的时间泄漏，不能因 Rowhammer 关键词归为纯故障；各平台、任务与最高 F1 需分开。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX technical-session abstract。
- [详细阅读记录](notes/usenix2025-scope-blind-analysis-and-counter-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## OBLIVIATOR: OBLIVIous Parallel Joins and other OperATORs in Shared Memory Environments

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/mavrogiannakis)；时间标记：USENIX 2025 conference 2025-08-13 to 2025-08-15 within frozen window; earliest online date not established。
- 作者：Apostolos Mavrogiannakis, University of California, Santa Cruz; Xian Wang, The Hong Kong University of Science and Technology; Ioannis Demertzis, University of California, Santa Cruz; Dimitrios Papadopoulos, The Hong Kong University of Science and Technology; Minos Garofalakis, ATHENA Research Center and Technical University of Crete
- 对象：oblivious database joins；类型：access-pattern defense。
- 核心想法：设计共享内存 TEE 场景下隐藏访问模式的并行 join 和数据库算子。
- 作者报告：作者报告对既有 oblivious join 的顺序及多线程性能改进。
- 限制与下一步：声明允许输入输出大小泄漏；并行倍数取决于线程数和比较基线，不是所有数据库操作。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX technical-session abstract。
- [详细阅读记录](notes/usenix2025-scope-blind-analysis-and-counter-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## OwlC: Compiling Security Protocols to Verified, Secure, High-Performance Libraries

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/singh)；时间标记：USENIX 2025 conference 2025-08-13 to 2025-08-15 within frozen window; earliest online date not established。
- 作者：Pratap Singh, Carnegie Mellon University; Joshua Gancher, Northeastern University; Bryan Parno, Carnegie Mellon University Distinguished Artifact Award Winner
- 对象：WireGuard, HPKE, Owl；类型：verified implementation and compilation。
- 核心想法：从已验证 Owl 协议生成正确且声明具备侧信道抵抗的 Rust 实现。
- 作者报告：作者以 WireGuard 与 HPKE 等协议评估互操作性及端到端性能。
- 限制与下一步：摘要未给完整侧信道模型；不能把高层证明外推到功耗、微架构或所有平台。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX technical-session abstract。
- [详细阅读记录](notes/usenix2025-scope-blind-analysis-and-counter-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## Phantom Trails: Practical Pre-Silicon Discovery of Transient Data Leaks

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/de-faveri-tron)；时间标记：USENIX 2025 conference 2025-08-13 to 2025-08-15 within frozen window; earliest online date not established。
- 作者：Alvise de Faveri Tron, Raphael Isemann, Hany Ragab, Cristiano Giuffrida, Klaus von Gleissenthall, and Herbert Bos, Vrije Universiteit Amsterdam
- 对象：BOOM, RISC-V, transient execution；类型：pre-silicon leak detection。
- 核心想法：以架构行为推断秘密位置，直接检测瞬态微架构数据泄漏的根因。
- 作者报告：作者在 BOOM RISC-V 设计 fuzzing 中报告发现已知问题和 Spectre-LoopPredictor。
- 限制与下一步：设计阶段检测独立于隐蔽传输通道；发现根因不等于已在真实芯片完成端到端泄漏。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX technical-session abstract。
- [详细阅读记录](notes/usenix2025-scope-blind-analysis-and-counter-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## Place Protections at the Right Place: Targeted Hardening for Cryptographic Code against Spectre v1

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/zhu-yiming)；时间标记：USENIX 2025 conference 2025-08-13 to 2025-08-15 within frozen window; earliest online date not established。
- 作者：Yiming Zhu, Wenchao Huang, and Yan Xiong, University of Science and Technology of China
- 对象：Spectre v1, OpenSSL, Libsodium, NaCL；类型：targeted hardening。
- 核心想法：LightSLH 以不动点分析跟踪逐步加固引起的程序行为变化，实施针对性 Spectre v1 防护。
- 作者报告：作者报告编译器插入栈装载风险、scatter-gather 的缓存行粒度泄漏和多种密码库性能。
- 限制与下一步：证明需保留对手和编译层边界；58.3% 测试例零开销不能泛化为所有实现。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX technical-session abstract。
- [详细阅读记录](notes/usenix2025-scope-blind-analysis-and-counter-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## PolySys: an Algebraic Leakage Attack Engine

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/espiritu)；时间标记：USENIX 2025 conference 2025-08-13 to 2025-08-15 within frozen window; earliest online date not established。
- 作者：Zachary Espiritu, MongoDB Research; Seny Kamara, Brown University and MongoDB Research; Tarik Moataz, MongoDB Research; Andrew Park, Carnegie Mellon University and MongoDB Research
- 对象：encrypted queries, polynomial constraints；类型：leakage inference framework。
- 核心想法：以可逆编码、结构等式和泄漏等式把加密查询的模式泄漏建模为多项式约束求解。
- 作者报告：作者报告 PolySys 在 point/range multi-map 的查询恢复和数据解析任务结果。
- 限制与下一步：这是加密查询泄漏引擎，不是 PQC 格求解器；最高 60 倍恢复率依赖相同假设的场景，规模仍受限。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX technical-session abstract。
- [详细阅读记录](notes/usenix2025-scope-blind-analysis-and-counter-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## Relocate-Vote: Using Sparsity Information to Exploit Ciphertext Side-Channels

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/yan-yuqin)；时间标记：USENIX 2025 conference 2025-08-13 to 2025-08-15 within frozen window; earliest online date not established。
- 作者：Yuqin Yan, University of Toronto; Wei Huang, University of Toronto and Seneca Polytechnic; Ilya Grishchenko and Gururaj Saileshwar, University of Toronto; Aastha Mehta, University of British Columbia; David Lie, University of Toronto
- 对象：AMD SEV-SNP, ciphertext equality；类型：ciphertext side-channel attack。
- 核心想法：利用机密计算内存搬移命令与相同 tweak 下的密文等值关系，推断空间值分布。
- 作者报告：作者演示去随机化 ASLR、OpenVDB 三维数据及稀疏 LLM token 信息。
- 限制与下一步：需要恶意 hypervisor 与特定管理接口；空间分布泄漏不等于任意加密内存明文读出。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX technical-session abstract。
- [详细阅读记录](notes/usenix2025-scope-blind-analysis-and-counter-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## SCASE: Automated Secret Recovery via Side-Channel-Assisted Symbolic Execution

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/weber)；时间标记：USENIX 2025 conference 2025-08-13 to 2025-08-15 within frozen window; earliest online date not established。
- 作者：Daniel Weber, Lukas Gerlach, and Leon Trampert, CISPA Helmholtz Center for Information Security; Youheng Lü, SCHUTZWERK GmbH; Jo Van Bulck, DistriNet, KU Leuven; Michael Schwarz, CISPA Helmholtz Center for Information Security
- 对象：SGX, RSA, RC4, AES, symbolic execution；类型：automated side-channel inference。
- 核心想法：用受控信道内存访问迹线剪枝符号执行，从不透明二进制自动推断秘密。
- 作者报告：作者的 Athena 在 SGX 上报告 RSA、RC4、AES 与其他输入恢复。
- 限制与下一步：依赖控制信道能力和被测二进制；RSA/RC4 的分钟级结果不是任意 enclave 自动恢复保证。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX technical-session abstract。
- [详细阅读记录](notes/usenix2025-scope-blind-analysis-and-counter-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## Secure Caches for Compartmentalized Software

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/arikan)；时间标记：USENIX 2025 conference 2025-08-13 to 2025-08-15 within frozen window; earliest online date not established。
- 作者：Kerem Arıkan, Huaxin Tang, Williams Zhang Cen, and Yu David Liu, Binghamton University; Nael Abu-Ghazaleh, University of California, Riverside; Dmitry Ponomarev, Binghamton University
- 对象：cache partitioning, compartments；类型：cache defense。
- 核心想法：为同地址空间 compartment 设计多级 cache 分区、按内存域分区与调用者专属共享库分区。
- 作者报告：作者给出 SCC 操作语义证明及 gem5 性能评估。
- 限制与下一步：性能来自模拟器；逻辑隔离、声明 cache 安全与全部物理共享资源隔离不可等同。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX technical-session abstract。
- [详细阅读记录](notes/usenix2025-scope-blind-analysis-and-counter-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## Shadows in Cipher Spaces: Exploiting Tweak Repetition in Hardware Memory Encryption

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/peng-wei)；时间标记：USENIX 2025 conference 2025-08-13 to 2025-08-15 within frozen window; earliest online date not established。
- 作者：Wei Peng, Yinshuai Li, and Yinqian Zhang, Southern University of Science and Technology
- 对象：Hygon CSV, memory encryption；类型：ciphertext side-channel attack。
- 核心想法：分析 Hygon CSV 内存加密的块内 tweak 重复，利用相等明文对应相等密文。
- 作者报告：作者提出 CipherShadow，报告 OpenSSH 认证绕过和机器学习训练数据重建。
- 限制与下一步：保留 Hygon CSV 及 64 B 内 16 B 子块条件；不把结论推广到所有 SGX/TDX/SEV。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX technical-session abstract。
- [详细阅读记录](notes/usenix2025-scope-blind-analysis-and-counter-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## SoK: So, You Think You Know All About Secure Randomized Caches?

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/bhatla)；时间标记：USENIX 2025 conference 2025-08-13 to 2025-08-15 within frozen window; earliest online date not established。
- 作者：Anubhav Bhatla, Hari Rohit Bhavsar, Sayandeep Saha, and Biswabandan Panda, Indian Institute of Technology Bombay Distinguished Artifact Award Winner
- 对象：randomized cache；类型：systematization。
- 核心想法：系统比较随机化 cache 的五类设计因素及其组合对冲突和占用攻击的作用。
- 作者报告：作者分析 skewing、无效 tag、高关联度、替换策略和 remapping。
- 限制与下一步：单一参数无全面保证是所述设计空间的结果；不能把任意组合都称为已证明安全。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX technical-session abstract。
- [详细阅读记录](notes/usenix2025-scope-blind-analysis-and-counter-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## Sound of Interference: Electromagnetic Eavesdropping Attack on Digital Microphones Using Pulse Density Modulation

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/onishi)；时间标记：USENIX 2025 conference 2025-08-13 to 2025-08-15 within frozen window; earliest online date not established。
- 作者：Arifu Onishi, The University of Electro-Communications; S. Hrushikesh Bhupathiraju, Rishikesh Bhatt, and Sara Rampazzi, University of Florida; Takeshi Sugawara, The University of Electro-Communications
- 对象：PDM microphones, EM emissions；类型：physical EM eavesdropping。
- 核心想法：利用数字 MEMS 麦克风 PDM 脉冲的电磁谐波读取声音。
- 作者报告：作者在设备上评估数字识别和语音转录，报告两米、25 cm 墙体场景及随机时钟防护。
- 限制与下一步：数字识别准确率与语音转录误差不同；摘要写 maximum 14% transcription error rate，具体统计待正文，不擅改为最佳 WER。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX technical-session abstract。
- [详细阅读记录](notes/usenix2025-scope-blind-analysis-and-counter-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## Systematic Evaluation of Randomized Cache Designs against Cache Occupancy

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/chakraborty)；时间标记：USENIX 2025 conference 2025-08-13 to 2025-08-15 within frozen window; earliest online date not established。
- 作者：Anirban Chakraborty, Max Planck Institute for Security and Privacy; Nimish Mishra, Indian Institute of Technology Kharagpur; Sayandeep Saha, Indian Institute of Technology Bombay; Sarani Bhattacharya and Debdeep Mukhopadhyay, Indian Institute of Technology Kharagpur
- 对象：CEASER, CEASER-S, MIRAGE, ScatterCache, SassCache, AES；类型：cache security evaluation。
- 核心想法：在统一性能基准与多种对手模型下比较五种随机化 cache 对占用侧信道的防护。
- 作者报告：作者评估隐蔽通信、进程指纹及 AES 密钥恢复。
- 限制与下一步：需保留 cache 配置、替换策略和仿真/实物来源；随机地址映射并不自动消除占用通道。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX technical-session abstract。
- [详细阅读记录](notes/usenix2025-scope-blind-analysis-and-counter-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## TDXploit: Novel Techniques for Single-Stepping and Cache Attacks on Intel TDX

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/rauscher)；时间标记：USENIX 2025 conference 2025-08-13 to 2025-08-15 within frozen window; earliest online date not established。
- 作者：Fabian Rauscher, Graz University of Technology; Luca Wilke, University of Lübeck; Hannes Weissteiner, Graz University of Technology; Thomas Eisenbarth, University of Lübeck; Daniel Gruss, Graz University of Technology
- 对象：Intel TDX, ECDSA, AES, TOTP；类型：single-stepping and cache attack。
- 核心想法：操纵 TDX 单步缓解内部状态，结合无需共享内存的 Flush+Flush 观察。
- 作者报告：作者报告 ECDSA、AES T-table 与单迹线 TOTP 演示及高单步准确率。
- 限制与下一步：单步准确率不等于秘密恢复率；需强主机权限及相应 TDX 模块版本，AES 的 8986 迹线与 TOTP 单迹线为不同任务。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX technical-session abstract。
- [详细阅读记录](notes/usenix2025-scope-blind-analysis-and-counter-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## TEEcorrelate: An Information-Preserving Defense against Performance-Counter Attacks on TEEs

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/weissteiner)；时间标记：USENIX 2025 conference 2025-08-13 to 2025-08-15 within frozen window; earliest online date not established。
- 作者：Hannes Weissteiner and Fabian Rauscher, Graz University of Technology; Robin Leander Schröder, Fraunhofer SIT and Fraunhofer Austria; Jonas Juffinger and Stefan Gast, Graz University of Technology; Jan Wichelmann and Thomas Eisenbarth, University Luebeck; Daniel Gruss, Graz University of Technology
- 对象：HQC, RSA, TOTP, AMD SEV-SNP；类型：performance-counter defense。
- 核心想法：通过时间聚合与模糊计数增量减弱 TEE 性能计数器泄漏，同时保留监控用途。
- 作者报告：表 4 对默认偏移窗口 2048 报告 HQC 约 27.0 天、RSA 824.6 天等估计；附录明确材料模拟防护行为，硬件开销也为估计。
- 限制与下一步：摘要/引言/表格的运行时间不同；HQC 的 800 ms 是每条 trace、6.13 min 为理想预言机基线。印刷公式存在负被开方项及 Tt 时间单位不相容，影响需独立核查；大计数差异与跨核计数器不在完整保护范围。
- 阅读层级：selected_full_text_sections；来源：official USENIX technical-session abstract; selected final proceedings PDF sections。
- 已读章节：PDF pp.3,9-15: design summary, overhead estimate, threat/statistical model, Table 3/4, HQC cost and limitations; six selected refs 20/24/46/53/74/76 from pp.17-19; artifact appendix pp.1-3 read. PDF pp.11-12 and 14 visually checked. Other references not fully screened.
- [详细阅读记录](notes/usenix2025-scope-blind-analysis-and-counter-bounds-20261114.md)
- 代码/数据核查：Main PDF cites 10.5281/zenodo.15592842; artifact appendix cites 10.5281/zenodo.15699920 and describes simulation/runtime calculation; version relation and contents not inspected or executed；引用追踪：Selected six of 82 references now linked; actual OT-PCA preprint and Aegis read. Remaining 76 references not completely screened; not citation closure.。

## TLBlur: Compiler-Assisted Automated Hardening against Controlled Channels on Off-the-Shelf Intel SGX Platforms

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/vanoverloop)；时间标记：USENIX 2025 conference 2025-08-13 to 2025-08-15 within frozen window; earliest online date not established。
- 作者：Daan Vanoverloop, DistriNet, KU Leuven; Andrés Sánchez, EPFL, Amazon; Flavio Toffalini, EPFL, RUB; Frank Piessens, DistriNet, KU Leuven; Mathias Payer, EPFL; Jo Van Bulck, DistriNet, KU Leuven
- 对象：SGX, AEX-Notify, TLB；类型：controlled-channel defense。
- 核心想法：借助 SGX AEX-Notify 与编译插桩，在中断后预取最近页面来模糊受控页信道。
- 作者报告：作者在 libjpeg、yescrypt、wolfSSL 和 OpenSSL 上评价 TLBlur。
- 限制与下一步：保护针对最近页面的匿名集合及特定硬件条件；限制页观察带宽不等于关闭全部 cache 或物理通道。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX technical-session abstract。
- [详细阅读记录](notes/usenix2025-scope-blind-analysis-and-counter-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## Treebeard: A Scalable and Fault Tolerant ORAM Datastore

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/setayesh)；时间标记：USENIX 2025 conference 2025-08-13 to 2025-08-15 within frozen window; earliest online date not established。
- 作者：Amin Setayesh, Cheran Mahalingam, Emily Chen, and Sujaya Maiyya, University of Waterloo
- 对象：ORAM, datastore；类型：access-pattern defense。
- 核心想法：通过多层架构、并发与复制构建可扩展容错 ORAM 存储。
- 作者报告：作者报告 16 台机器 160K ops/sec、故障恢复及与 QuORAM/Snoopy 比较。
- 限制与下一步：吞吐与容错结果依赖机器预算和配置；ORAM 模式保护不自动覆盖全部 TEE 物理观察。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX technical-session abstract。
- [详细阅读记录](notes/usenix2025-scope-blind-analysis-and-counter-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## V-ORAM: A Versatile and Adaptive ORAM Framework with Service Transformation for Dynamic Workloads

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/zhang-bo-voram)；时间标记：USENIX 2025 conference 2025-08-13 to 2025-08-15 within frozen window; earliest online date not established。
- 作者：Bo Zhang and Helei Cui, Northwestern Polytechnical University; Xingliang Yuan, The University of Melbourne; Zhiwen Yu, Northwestern Polytechnical University and Harbin Engineering University; Bin Guo, Northwestern Polytechnical University
- 对象：ORAM service transformation；类型：access-pattern defense。
- 核心想法：以中介 ORAM 同步状态，允许安全转换不同 ORAM 服务来适应工作负载。
- 作者报告：作者给出转换安全证明、规划器及三组医疗数据工作负载评估。
- 限制与下一步：转换相对重建的最大节省不是每次访问提升；具体 client/server 假设和金额成本需正文固定。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX technical-session abstract。
- [详细阅读记录](notes/usenix2025-scope-blind-analysis-and-counter-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## Vest: Verified, Secure, High-Performance Parsing and Serialization for Rust

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/cai-yi)；时间标记：USENIX 2025 conference 2025-08-13 to 2025-08-15 within frozen window; earliest online date not established。
- 作者：Yi Cai, University of Maryland, College Park; Pratap Singh and Zhengyao Lin, Carnegie Mellon University; Jay Bosamiya, Microsoft Research; Joshua Gancher, Northeastern University; Milijana Surbatovich, University of Maryland, College Park; Bryan Parno, Carnegie Mellon University
- 对象：Rust parsing, TLS 1.3, WebAssembly；类型：verified implementation。
- 核心想法：从 DSL 与验证组合子生成 Rust 解析/序列化代码，并声明抵抗基本数字侧信道。
- 作者报告：作者在 Bitcoin、TLS 1.3 和 WebAssembly 格式上比较执行和证明性能。
- 限制与下一步：basic digital side channels 的具体模型须全文确认；不将验证扩展为任意硬件或功耗安全。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX technical-session abstract。
- [详细阅读记录](notes/usenix2025-scope-blind-analysis-and-counter-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## When Good Kernel Defenses Go Bad: Reliable and Stable Kernel Exploits via Defense-Amplified TLB Side-Channel Leaks

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/maar-kernel)；时间标记：USENIX 2025 conference 2025-08-13 to 2025-08-15 within frozen window; earliest online date not established。
- 作者：Lukas Maar, Lukas Giner, Daniel Gruss, and Stefan Mangard, Graz University of Technology
- 对象：TLB, Linux kernel, ASLR；类型：defense-induced timing leak。
- 核心想法：利用内核防护放大的 TLB 争用模式泄露内核对象位置。
- 作者报告：作者分析 127 项防护，在三类配置及多种 Intel CPU/kernel 版本演示定位。
- 限制与下一步：需要相应配置与分配器操纵；位置披露可辅助利用但不等于通用任意内存读出。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX technical-session abstract。
- [详细阅读记录](notes/usenix2025-scope-blind-analysis-and-counter-bounds-20261114.md)
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

## Maskaglia: A New, Efficient Approach to Masked Discrete Gaussian Sampling

- 来源：[CRYPTO 2026](https://doi.org/10.1007/978-3-032-35415-0_6)；时间标记：within frozen rolling window。
- 作者：Calvin Abou Haidar; Thomas Espitau; Clément Hoffmann; Mehdi Tibouchi
- 对象：discrete Gaussian, HAWK, bitslicing, t-probing；类型：masking。
- 核心想法：从离散化的 Marsaglia 类拒绝采样构造新的、便于掩码的采样结构。
- 作者报告：正式摘要在 HAWK 用例报告 masked AND 数量优势，比较原有及经过优化的比较树采样器。
- 限制与下一步：摘要的分布范围为固定中心和固定标准差；AND 数量不是全签名墙钟时间或实测泄漏安全，不能直接推为 FALCON 可变中心采样的完整解法。仅读摘要和第 5 条参考。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://link.springer.com/chapter/10.1007/978-3-032-35415-0_6。
- [详细阅读记录](notes/muov-followups-and-masked-sampling-20261114.md)
- 代码/数据核查：no author code/data executed; artifact completeness not inspected；引用追踪：pending except explicit inventories。

## Side-Channel Attacks on VOLEitH Signature Schemes: Breaking Masked FAEST

- 来源：[IACR CiC 2026](https://doi.org/10.62056/aebngyl7s)；时间标记：within rolling five-year window。
- 作者：Sönke Jendral; Elena Dubrova
- 对象：FAEST, VOLEitH, deep learning；类型：attack。
- 核心想法：利用 witness 字节组合与 VOLE 标签转置的泄漏评估第一轮掩码 FAEST。
- 作者报告：作者在不同剖析和测试设备上报告单次签名恢复；无额外加噪条件下，两方法分别为 998/1000 与 1000/1000。
- 限制与下一步：每种方法使用 5000 条剖析迹线；数百万片段不等于独立采集。未知密钥自剖析只提出未实验，第二轮适用性仅讨论。训练与枚举成本必须计入；数据和预训练模型需向作者申请。
- 阅读层级：selected_full_text_sections；来源：https://cic.iacr.org/p/2/4/24/pdf; https://doi.org/10.62056/aebngyl7s; https://github.com/KTH-HWSEC/breaking-masked-faest/blob/main/README.md。
- 已读章节：Publisher PDF pages 2-3, 8-9, 12-13, 17-22 selected sections; Table 5 on page 20 visually checked; not all 27 pages or complete proofs. Artifact README read; no scripts inspected/executed.
- [详细阅读记录](notes/mpcith-revisions-and-evidence-20261113.md)
- 代码/数据核查：Author README read at Git blob 05f57fff7cbc43459587ef77b5fcc3601a11cf4a; scripts listed, datasets/pretrained models available upon request; no code inspected/executed；引用追踪：all 38 entries screened: 19 linked, 19 provisional background; original 12 discoveries resolved; recursive/forward closure incomplete。

## HYPERSHIELD: Protecting the Hypercube MPC-in-the-Head Framework Against Differential Probing Adversaries without Masking

- 来源：[IACR ePrint 2026](https://eprint.iacr.org/2026/081)；时间标记：within rolling five-year window。
- 作者：Linda Pirker; Quinten Norga; Suparna Kundu; Anindya Ganguly; Barry van Leeuwen; Angshuman Karmakar; Ingrid Verbauwhede
- 对象：SDitH, MPC-in-the-Head, Hypercube；类型：countermeasure_protocol。
- 核心想法：通过增加隐藏份额和调整 GGM 树揭示方式改变 Hypercube-MPCitH 协议，在差分探测模型下提供阶数保护。
- 作者报告：作者给出参数、计算量与签名长度权衡，并与传统掩码开销估计比较。
- 限制与下一步：这是协议修改而非透明替换实现；全掩码比较值含估算。摘要不证明所有 SPA 或物理观察安全，正文和各参数证明待核查。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://eprint.iacr.org/2026/081。
- [详细阅读记录](notes/mpcith-revisions-and-evidence-20261113.md)
- 代码/数据核查：not inspected; no author code executed；引用追踪：pending except explicitly linked references。

## AEX-NStep: Probabilistic Interrupt Counting Attacks on Intel SGX

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00035)；时间标记：formal SP 2026 metadata within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Nicolas Dutly; Friederike Groschupp; Ivan Puddu; Kari Kostiainen; Srdjan Čapkun
- 对象：SGX, AEX-Notify, ECDSA；类型：microarchitectural_side_channel。
- 核心想法：以概率性中断计数绕过 AEX-Notify 的执行进度隐藏目标。
- 作者报告：作者构造了启用 AEX-Notify 的 SGX ECDSA 密钥泄漏案例。
- 限制与下一步：不需要确定性单步不等于没有中断控制权限；具体密钥恢复预算待正文。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/11573587/。
- [详细阅读记录](notes/sp2026-scope-identity-and-frequency-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## Can I Get More? An Incremental Inference Attack on Encrypted SQL

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00133)；时间标记：formal SP 2026 metadata within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Xiaoqian Sun; Ruiqi He; Yang Zhang; Siyi Lv; Guiyun Qin; Fangzhou Yi; Zheli Liu; Xiaofeng Chen
- 对象：encrypted SQL, joint distributions；类型：system_metadata_side_channel。
- 核心想法：从列相等关系建立锚点，再逐步利用跨列联合分布恢复加密 SQL 数据映射。
- 作者报告：作者用最优传输处理部分域重叠，并区分值恢复和行恢复。
- 限制与下一步：依赖允许泄漏及辅助分布；最优条件下不同查询场景的数字不可合并为普遍恢复率。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/11573930/。
- [详细阅读记录](notes/sp2026-scope-identity-and-frequency-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## Chypnosis: Undervolting-based Static Side-channel Attacks

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00090)；时间标记：formal SP 2026 metadata within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Kyle Mitard; Saleh Khalaj Monfared; Fatemeh Khojasteh Dana; Robert Dumitru; Yuval Yarom; Shahin Tajik
- 对象：Chypnosis, OpenTitan, FPGA, static leakage, impedance, LLSI；类型：physical_side_channel。
- 核心想法：通过欠压停钟并阻止状态清理，再结合静态侧信道读取保留状态。
- 作者报告：作者报告多种 FPGA 传感器及 OpenTitan 模块案例，并提出时钟检测改进。
- 限制与下一步：包含主动供电操纵与 LLSI/阻抗读出，不能写成纯被动功耗；OpenTitan 模块实验不代表所有芯片版本。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/11573501/。
- [详细阅读记录](notes/sp2026-scope-identity-and-frequency-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## Credential Extraction Attacks Against Compromised Credential Checking Services of Password Managers

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00103)；时间标记：formal SP 2026 metadata within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Yihe Duan; Ding Wang; Yutong Li
- 对象：password managers, query patterns；类型：system_metadata_side_channel。
- 核心想法：利用密码管理器向凭据检查服务发出的确定性查询模式关联用户并提高猜测能力。
- 作者报告：攻击者为诚实但好奇的 C3 服务；作者评价 14 款管理器，其中 10 款受影响。
- 限制与下一步：用户识别率与一次猜测收益不同；服务端可见查询条件不可省略，非加密算法本身被破解。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/11573497/。
- [详细阅读记录](notes/sp2026-scope-identity-and-frequency-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## Crucible: Retrofitting Commodity CPUs with Vulnerabilities via Transparent Software Emulation

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00186)；时间标记：formal SP 2026 metadata within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Tristan Hornetz; Lukas Gerlach; Michael Schwarz
- 对象：Crucible, transient execution, emulation；类型：research_infrastructure。
- 核心想法：软件模拟 Meltdown 类瞬态漏洞以支持未修改的攻击与检测程序。
- 作者报告：作者在不受影响的 x86 硬件上模拟缓存读出、瞬态窗口和围栏行为，复现三项端到端案例。
- 限制与下一步：模拟得到的泄漏不证明宿主 CPU 原生存在漏洞；仿真保真度和适用漏洞族需区分。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/11573460/。
- [详细阅读记录](notes/sp2026-scope-identity-and-frequency-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## Defeating Transient Execution Attacks by Limiting Secret Reachability Through Register Hiding and ShadowCFI

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00015)；时间标记：formal SP 2026 metadata within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Daniël Trujillo; Jagadish Kotra; David Kaplan; Mengjia Yan
- 对象：Spectre v2, Register Hiding, ShadowCFI；类型：microarchitectural_countermeasure。
- 核心想法：以寄存器状态隐藏和控制流恢复约束削弱推测路径上的秘密可达性。
- 作者报告：作者实现 Linux 6.8.0 补丁并比较 AMD Zen 4 的防护开销。
- 限制与下一步：针对指定 Spectre v2 类攻击和恢复条件；不能扩展为全部瞬态、功耗或 EM 安全。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/11573418/。
- [详细阅读记录](notes/sp2026-scope-identity-and-frequency-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## Enter, Exit, Page Fault, Leak: Testing Isolation Boundaries for Microarchitectural Leaks

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00007)；时间标记：formal SP 2026 metadata within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Oleksii Oleksenko; Flavien Solt; Cedric Fournet; Jana Hofmann; Boris Kopf; Stavros Volos
- 对象：model-based relational testing, domain isolation；类型：side_channel_discovery。
- 核心想法：扩展关系测试以检查虚拟机、内核和进程之间的微架构隔离。
- 作者报告：作者在六款 x86-64 CPU 上报告四项新泄漏及已知案例。
- 限制与下一步：测试发现能力不等于穷尽证明；两次假阳性与所用模型、硬件集合一起保留。印刷目录缺此项，出版元数据仍存在。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/11573579/。
- [详细阅读记录](notes/sp2026-scope-identity-and-frequency-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## EyeSpy: Inferring Eye Gaze via Side-Channel Attacks Against Foveated Rendering

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00145)；时间标记：formal SP 2026 metadata within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Paul Maynard; Harris Amjad; Camila Molinares; Bo Ji; Brendan David-John
- 对象：VR, foveated rendering, GPU workload, gaze；类型：system_side_channel。
- 核心想法：通过注视点渲染引起的 GPU 工作量变化推断眼动位置。
- 作者报告：攻击在视野内移动高成本对象并观察帧率/帧时间，评价多个设备及渲染平台。
- 限制与下一步：需要控制渲染内容及性能观测；并非无需植入内容的被动读眼动。防御 F1 与角度误差属于不同任务。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/11573450/。
- [详细阅读记录](notes/sp2026-scope-identity-and-frequency-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## Fractal: An Operating System Designed for Microarchitecture Reverse Engineering

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00141)；时间标记：formal SP 2026 metadata within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Joseph Ravichandran; Mengjia Yan
- 对象：Fractal, microarchitecture, Apple M1；类型：research_infrastructure。
- 核心想法：专用 OS 通过低噪声跨特权级并发与可控调度支持微架构逆向。
- 作者报告：作者以 Apple M1 分支预测器为案例，报告有限 Phantom speculation 的证据。
- 限制与下一步：逆向证据不等于完整数据窃取；不把一个 M1 案例扩张为所有 Apple Silicon。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/11573600/。
- [详细阅读记录](notes/sp2026-scope-identity-and-frequency-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## From Perfect to Approximate Hints: Efficient LWE Secret Recovery Leveraging Low Hamming Weight

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00239)；时间标记：formal SP 2026 metadata within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Minki Hhan; Ga Hee Hong; Jiseung Kim; Changmin Lee; JeongHwan Lee
- 对象：LWE, FHE, sparse ternary secrets, hints；类型：pqc_side_information_solver。
- 核心想法：利用稀疏三元秘密结构减少 LWE 精确/近似提示的求解需求。
- 作者报告：摘要报告 GAA 条件分析与经验结果；n=2^15、h=32 时为 320 条提示，h=192 的 OpenFHE 场景仅验证精确提示。
- 限制与下一步：提示获取成本未由摘要建立；不是 ML-KEM 实测功耗恢复，O(h log h) 不能当作无条件保证。ePrint 正文访问 403，保留未读。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/11573630/。
- [详细阅读记录](notes/sp2026-scope-identity-and-frequency-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## Goldilocks and the Three P-States: Mitigating Hertzbleed with Formal Leakage Guarantees

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00167)；时间标记：formal SP 2026 metadata within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Inwhan Chun; Christine Guo; Riccardo Paccagnella
- 对象：Goldilocks, Hertzbleed, SIKE, Classic McEliece, ECDSA；类型：pqc_system_countermeasure。
- 核心想法：通过约束节流发生次数及持续时间限制 P-state 序列的泄漏。
- 作者报告：作者给出 O(N log t) 界；静态策略 N 有界，测量含 SIKE、Classic McEliece 与 ECDSA。
- 限制与下一步：限功耗到频率通道；冷态并非零泄漏，重访策略另计 N。τ 定义与实测计时起点待核对，SIKE 评估仅选 4/378 个比特。
- 阅读层级：selected_full_text_sections；来源：https://xplorestaging.ieee.org/document/11573361/。
- 已读章节：Publisher abstract; author PDF pp.3-10 and 13-17: model, design, implementation, evaluation setup/security scope, limitations, all 49 bibliography entries and appendices. Figures/table on pp.9 and 13 visually checked. Not complete proof or artifact audit.
- [详细阅读记录](notes/sp2026-scope-identity-and-frequency-bounds-20261114.md)
- 代码/数据核查：not retrieved or executed; timing-origin discrepancy requires implementation/author clarification；引用追踪：in_progress。

## HEAP LOCALIZATION: Cache Side-Channel Based Linux Kernel Heap Exploit Techniques

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00196)；时间标记：formal SP 2026 metadata within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Yoochan Lee; Sihyun Roh; Hyuk Kwon; Byoungyoung Lee; Thorsten Holz
- 对象：kernel heap, VIPT L1 cache；类型：microarchitectural_side_channel。
- 核心想法：通过 VIPT L1 缓存行为推断内核堆对象的页内位置。
- 作者报告：作者报告空闲与高负载条件下的定位成功率，并用于提高已存在漏洞的利用可靠性。
- 限制与下一步：定位原语、任意读取和端到端提权是不同能力；不能将无内存泄露前提扩张为无其他漏洞。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/11573609/。
- [详细阅读记录](notes/sp2026-scope-identity-and-frequency-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## Interplay of Efficient Model Checking and Secure Processor Design: A Case Study on Secure Speculation

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00203)；时间标记：formal SP 2026 metadata within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Tingzhen Dong; Kunpeng Wang; Yuheng Yang; Yu-Wei Fan; Qinhan Tan; Thomas Bourgeat; Sharad Malik; Mengjia Yan
- 对象：BOOM, secure speculation, noninterference；类型：formal_side_channel_verification。
- 核心想法：使用带历史的未解释函数抽象，保留信息流性质并弱化无关功能细节。
- 作者报告：作者把验证经验反馈到 BOOM 安全推测机制的设计，提出自动化框架。
- 限制与下一步：证明范围取决于抽象和观察性质；并非对任意真实物理波形的非干扰保证。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/11573397/。
- [详细阅读记录](notes/sp2026-scope-identity-and-frequency-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## Keytar: Practical Keystroke Timing Attacks and Input Reconstruction

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00106)；时间标记：formal SP 2026 metadata within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Mufan Qiu; Lihsuan Chuang; Dohhyun Kim; Huaizhi Qu; Tianlong Chen; Andrew Kwong
- 对象：keystroke timing, LLM, cache；类型：side_channel_reconstruction。
- 核心想法：将按键间隔到输入文本的恢复建模为机器翻译，并结合语言模型上下文。
- 作者报告：作者报告 top-5 候选中最佳结果的编辑距离阈值指标，并做原生及 Chrome 缓存观察案例。
- 限制与下一步：34.9% 使用最佳 top-5 且归一化编辑距离不超过 0.1，并非 top-1 完全正确。重放训练、噪声测量与真实输入需分开。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/11573555/。
- [详细阅读记录](notes/sp2026-scope-identity-and-frequency-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## LatORAM: ORAMs from Lateral Stashes and Delayed Shuffling

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00075)；时间标记：formal SP 2026 metadata within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Sarvar Patel; Giuseppe Persiano; Joon Young Seo; Kevin Yeo
- 对象：ORAM, access patterns；类型：access_pattern_countermeasure。
- 核心想法：利用横向暂存与延迟打乱组合 ORAM 查询和摊销成本优势。
- 作者报告：作者提出 LatORAM/LAT2ORAM，比较固定客户端存储下的通信及往返次数。
- 限制与下一步：协议访问模式隐藏不等于客户端实现的功耗/缓存安全；在线与摊销成本不能混算。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/11573492/。
- [详细阅读记录](notes/sp2026-scope-identity-and-frequency-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## Leafblower: a Leakage Attack Against Tee-Based Encrypted Databases

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00008)；时间标记：formal SP 2026 metadata within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Zachary Espiritu; Seny Kamara; Tarik Moataz; Valentin Ogier
- 对象：TEE, encrypted databases, B+ trees；类型：system_metadata_side_channel。
- 核心想法：利用加密 B+ 树索引的多快照结构泄漏推断插入顺序和明文。
- 作者报告：攻击只观察操作后的索引文件快照，结合辅助分布，无需注入或读取操作信息。
- 限制与下一步：96%/后段 100% 限小域和准确辅助信息的最优条件；不等于全部 TEE 数据库可完整恢复。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/11573629/。
- [详细阅读记录](notes/sp2026-scope-identity-and-frequency-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## Practical Covert Channel Across Isolated Browser Instances via GPU Command Queue Contention

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00254)；时间标记：formal SP 2026 metadata within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Jinhong Liu; Zifeng Kang; Song Li; Yinzhi Cao
- 对象：GPU command queues, browser, covert channel；类型：covert_channel。
- 核心想法：GPU 命令队列竞争支持跨隐私模式和跨浏览器的通信。
- 作者报告：作者在众包环境自适应协商速率，报告 1,434 次实验的完成率和已完成传输准确率。
- 限制与下一步：100% 是已完成传输的条件指标，整体完成率 92.81%；隐蔽通信不能直接当作被动受害者泄漏。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/11573605/。
- [详细阅读记录](notes/sp2026-scope-identity-and-frequency-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## PrintSpy: Pixel-Level Eavesdropping on Commodity Laser Printers via Electromagnetic Side Channels

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00119)；时间标记：formal SP 2026 metadata within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Wenhao Li; Jiarong Yang; Mingda Han; Xiuzhen Cheng; Pengfei Hu; Cong Wang
- 对象：laser printers, electromagnetic, diffusion models；类型：physical_side_channel。
- 核心想法：把打印机 EM 时间响应映射为像素矩阵，再以约束扩散模型修复结构。
- 作者报告：作者报告多款打印机的页面重建与字符错误率。
- 限制与下一步：生成式修复不能自动当作逐像素真值；距离、设备与文字先验条件待全文，非 PQC 秘密恢复。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/11573525/。
- [详细阅读记录](notes/sp2026-scope-identity-and-frequency-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## RISCy Cache Coherence: Timer-Free Architectural Cache Attacks via Instruction/Data Cache Incoherence

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00192)；时间标记：formal SP 2026 metadata within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Fabian Thomas; Michael Schwarz
- 对象：RISC-V, ARM, LoongArch, cache, AES；类型：microarchitectural_side_channel。
- 核心想法：借指令/数据缓存不一致把缓存状态转成架构可见结果，减少对计时器的依赖。
- 作者报告：作者测试 18 种微架构、12 种受影响，并给出 AES、Spectre 与 Android 事件案例。
- 限制与下一步：无计时器不等于无缓存访问或执行能力；跨架构结果需要分别保留实现条件。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/11573426/。
- [详细阅读记录](notes/sp2026-scope-identity-and-frequency-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## RadKey: An LLM-Guided RF Backscatter System for Through-Wall Keystroke Inference

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00160)；时间标记：formal SP 2026 metadata within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Qijun Wang; Chunqi Qian; Huacheng Zeng
- 对象：RF backscatter, keystrokes, LLM；类型：physical_side_channel。
- 核心想法：专用无电池标签把键盘振动和声学响应调制到背散射信号，再推断按键。
- 作者报告：作者构建标签与 RF 读出器，并用 LLM 伪标签在线适应。
- 限制与下一步：穿墙指 RF 读出链；仍需放置专用标签。伪标签不是独立真值，适应收益和新用户泛化待正文。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/11573589/。
- [详细阅读记录](notes/sp2026-scope-identity-and-frequency-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## Rain: Transiently Leaking Data from Public Clouds Using Old Vulnerabilities

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00063)；时间标记：formal SP 2026 metadata within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Mathé Hertogh; Dave Quakkelaar; Thijs Raymakers; Mahesh Hari Sarma; Marius Muench; Herbert Bos; Erik Van der Kouwe
- 对象：Rain, L1TF, cloud, TLS；类型：microarchitectural_side_channel。
- 核心想法：组合 L1TF 与推测越界载入，在商业云中跨虚拟机泄漏。
- 作者报告：作者报告噪声环境下 Nginx TLS 密钥案例，平均端到端时间 15 小时。
- 限制与下一步：特定云、老款 CPU 与缓解组合条件不代表所有云；密钥对象和计时边界待完整复核。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/11573429/。
- [详细阅读记录](notes/sp2026-scope-identity-and-frequency-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## SeqAss: Using SeqUential Associative Caches to Mitigate Conflict-Based Cache Attacks with Reduced Cache Misses and Performance Overhead

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00073)；时间标记：formal SP 2026 metadata within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Wei Song; Zhidong Wang; Jinchi Han; Da Xie; Hao Ma; Peng Liu
- 对象：SeqAss, randomized cache；类型：microarchitectural_countermeasure。
- 核心想法：以顺序相联方式防护冲突型缓存观察，同时保留组相联结构与 LRU。
- 作者报告：摘要报告与 Mirage/Chameleon 的防护、缺失率、面积和动态功耗比较。
- 限制与下一步：强度限所比较的冲突攻击模型；摘要面积/功耗百分数的基准措辞需查正文，暂不转述为绝对开销。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/11573472/。
- [详细阅读记录](notes/sp2026-scope-identity-and-frequency-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## State of Browser Process-Isolation: The Same-Site Weakness

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00096)；时间标记：formal SP 2026 metadata within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Fabian Kilger; Hannah Fischer; Adrian Staeves; Robin Marchart; Josef Schönberger; Fabian Franzen
- 对象：browser process isolation, Spectre v1；类型：microarchitectural_side_channel。
- 核心想法：分析同站子域共享进程的风险，并研究把域放入同进程后的观察攻击。
- 作者报告：作者在三类浏览器引擎展示案例，并评估隔离头和更严格进程策略。
- 限制与下一步：需相应子域控制/同进程条件；网站头采用率不能直接当作漏洞利用成功率。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/11573499/。
- [详细阅读记录](notes/sp2026-scope-identity-and-frequency-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## TDXRay: Microarchitectural Side-Channel Analysis of Intel TDX for Real-World Workloads

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00170)；时间标记：formal SP 2026 metadata within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Tristan Hornetz; Hosein Yavarzadeh; Albert Cheu; Adria Gascon; Lukas Gerlach; Daniel Moghimi; Phillipp Schoppmann; Michael Schwarz; Ruiyi Zhang
- 对象：Intel TDX, AES, LLM tokenization；类型：microarchitectural_side_channel。
- 核心想法：组合页级和缓存级主机观测，构建保密虚拟机访问轨迹。
- 作者报告：作者报告 AES T 表密钥与 LLM 分词阶段提示词推断案例。
- 限制与下一步：主机/恶意 hypervisor 能力不可省略；单条访存轨迹提示词恢复不代表任意模型、阶段或端到端响应解密。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/11573580/。
- [详细阅读记录](notes/sp2026-scope-identity-and-frequency-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## TEE.Fail: Breaking Trusted Execution Environments via DDR5 Memory Bus Interposition

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00101)；时间标记：formal SP 2026 metadata within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Jalen Chuang; Alex Seto; Nicolas Berrios; Stephan Van Schaik; Christina Garman; Daniel Genkin
- 对象：TEE.Fail, DDR5, memory encryption；类型：physical_ciphertext_side_channel。
- 核心想法：通过 DDR5 总线事务观察与确定性内存加密关系分析 TEE 秘密。
- 作者报告：作者报告服务器 TEE 的物理 interposer 案例，部分场景涉及证明密钥。
- 限制与下一步：需要物理总线接入，不能写成远程或纯软件攻击；不同 TEE 的观察/重放能力及恢复对象待正文区分。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/11573449/。
- [详细阅读记录](notes/sp2026-scope-identity-and-frequency-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## The Battle of Metasurfaces: Understanding Security in Smart Radio Environments

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00153)；时间标记：formal SP 2026 metadata within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Paul Staat; Christof Paar; Swarun Kumar
- 对象：metasurfaces, RIS, wireless sensing, obfuscation；类型：physical_observation_and_countermeasures。
- 核心想法：研究攻防双方都可改变无线传播环境时，信道混淆与感知防护的相互作用。
- 作者报告：作者以 Wi-Fi 干扰、感知欺骗和信道混淆进行理论及实测分析。
- 限制与下一步：纳入物理观察/防护背景；无线通信和感知的传播控制不等于密码芯片功耗或 EM 保护。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/11573514/。
- [详细阅读记录](notes/sp2026-scope-identity-and-frequency-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## Transient Architectural Execution: From Weird Gates to Weird Programs

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00066)；时间标记：formal SP 2026 metadata within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Ping-Lun Wang; Fraser Brown; Riccardo Paccagnella; Eyal Ronen; Riad S. Wahby; Yuval Yarom
- 对象：weird computation, transient execution, branch predictor；类型：side_channel_computation。
- 核心想法：瞬态地把微架构状态载入寄存器计算，再写回微架构状态。
- 作者报告：作者从布尔门推进到处理器式计算，并报告分支预测器上的宽变量及性能优势。
- 限制与下一步：隐式计算和放大原语不等于新的完整密钥恢复；比较对象为已有 weird gates，非普通程序速度。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/11573411/。
- [详细阅读记录](notes/sp2026-scope-identity-and-frequency-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## Trevex: A Black-Box Detection Framework for Data-Flow Transient Execution Vulnerabilities

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00135)；时间标记：formal SP 2026 metadata within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Daniel Weber; Fabian Thomas; Leon Trampert; Ruiyi Zhang; Michael Schwarz
- 对象：TREVEX, transient execution, FP-DSS；类型：side_channel_discovery。
- 核心想法：黑盒检测跨执行上下文的异常瞬态数据流。
- 作者报告：作者测试 20 种微架构，报告 AMD FP-DSS、新 FPVI 变体及兆芯案例。
- 限制与下一步：无 RTL/ISA 语义要求不代表无实验能力假设；检测覆盖不能作为不存在其他漏洞的证明。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/11573526/。
- [详细阅读记录](notes/sp2026-scope-identity-and-frequency-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## VMSCAPE: Exposing and Exploiting Incomplete Branch Predictor Isolation in Cloud Environments

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00046)；时间标记：formal SP 2026 metadata within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Jean-Claude Graf; Sandro Rüegge; Ali Hajiabadi; Kaveh Razavi
- 对象：VMSCAPE, Spectre-BTI, QEMU；类型：microarchitectural_side_channel。
- 核心想法：研究虚拟化边界上未完全隔离的分支预测状态。
- 作者报告：作者在 AMD Zen 5 的未修改 QEMU 上展示恶意 KVM 客户机泄漏主机用户态数据。
- 限制与下一步：多个 CPU 上的原语与完整利用平台要区分；154 B/s 是特定 PoC 读出速率，非任意云通用速率。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/11573554/。
- [详细阅读记录](notes/sp2026-scope-identity-and-frequency-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## When VR Meets BCI: (Un)Observable Brainwave-Aware Privacy Reconstruction in the Metaverse via Unrestricted Inbuilt Motion Sensors

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00117)；时间标记：formal SP 2026 metadata within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Tao Ni; Zehua Sun; Qingchuan Zhao; Wei-Bin Lee; Cong Wang
- 对象：VR, motion sensors, EEG-correlated representations；类型：sensor_side_channel。
- 核心想法：从 VR 内置运动传感器研究与视觉刺激相关的隐私推断。
- 作者报告：作者报告 EEG 相关表示、视觉内容类别、活动、身份和输入等不同任务。
- 限制与下一步：EEG 相关表示不等于直接测得脑电或任意思维；各任务准确率不可合并，生理机制及泛化仍待正文核验。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/11573488/。
- [详细阅读记录](notes/sp2026-scope-identity-and-frequency-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## Your Eyes Won't Lie: Snooping Online Voting Privacy from User Webcam

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00232)；时间标记：formal SP 2026 metadata within frozen 2021-11-12 to 2026-11-12 window。
- 作者：Zeyu Deng; Jingwei Zhang; Chen Wang
- 对象：webcam, eye motion, online voting；类型：physical_side_channel。
- 核心想法：利用投票时眼动与手部选择行为的配合推断屏幕选项。
- 作者报告：作者结合动作阶段、姿态校准和 transformer，评价网页表单及视频会议投票。
- 限制与下一步：摄像头、界面及训练条件不能省略；指定场景最高准确率不等于普遍选票恢复。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/11573577/。
- [详细阅读记录](notes/sp2026-scope-identity-and-frequency-bounds-20261114.md)
- 代码/数据核查：not checked；引用追踪：pending。

## Hardware Implementation and Security Analysis of Local-Masked NTT for CRYSTALS-Kyber

- 来源：[TC 2026](https://doi.org/10.1109/tc.2026.3729145)；时间标记：online 2026-09-17 within cutoff; assigned December 2026 issue is future at review date。
- 作者：Rafael Carrera Rodriguez; Emanuele Valea; Florent Bruguier; Pascal Benoit
- 对象：Kyber, NTT；类型：countermeasure_evaluation。
- 核心想法：实现并评估基于旋转因子随机化的局部掩码 NTT，比较不同配置的泄漏。
- 作者报告：IEEE 与同题 ePrint 摘要报告面积、性能和非特定 t 检验，指出配置之间泄漏倾向不同。
- 限制与下一步：不是完整 Kyber 密钥恢复结果；具体配置、测试规模与物理模型待全文。预印本正文 403，正式版与预印本全文等价未核实。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://xplorestaging.ieee.org/document/11695086/; https://eprint.iacr.org/2024/1194。
- [详细阅读记录](notes/kyber-shuffle-followups-and-evidence-20261113.md)
- 代码/数据核查：not inspected; no author code executed；引用追踪：selected backward/forward relation verified; complete tracing pending。

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

## Amortizing Randomness Cost: Efficient Masked Implementation of SDitH Signatures with Common Shares

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/liu-guowei)；时间标记：USENIX 2026 proceedings; conference 2026-08-12 to 2026-08-14 is within window; earliest online date not established。
- 作者：Guowei Liu, Weijia Wang, Lixuan Wu, Chaoran Wang, Yanhong Fan, Jinliang Wang, and Meiqin Wang, Shandong University
- 对象：SDitH, MPC-in-the-Head, Common Shares, Keccak；类型：masking_countermeasure。
- 核心想法：为 SDitH-Hypercube 的 last-party completion、BN 算术与秘密相关 Keccak 调用组织选择性掩码。
- 作者报告：Cortex-M4 上比较保护配置；Common Shares 的 16 B/签名只计算术掩码随机性。一阶 EM TVLA 针对指定热点与 RNI+opt+IND-Keccak 配置。
- 限制与下一步：选择性 Seed 边界不覆盖隐藏种子/种子树的完整单迹线恢复。IND 仅有一阶独立性，不能借用 DOM/SNI 的组合保证；不把局部 TVLA 未检出改写为完整签名无泄漏。 所引 FAEST 2025/1261 当前修订已撤回其掩码实现；此版本事实不自动否定 SDitH 本文自己的防护结果，详见 MPCitH 修订笔记。
- 阅读层级：selected_full_text_sections；来源：official final proceedings PDF and session abstract。
- 已读章节：PDF pp.5,9,12-16: Seed boundary, masking randomness, selected measurements/limits and references; figure 4 visually checked
- 代码/数据核查：author declares https://doi.org/10.5281/zenodo.20432040 in PDF p15; contents not inspected or run；引用追踪：all 27 bibliography entries screened; 21 linked and six provisional background entries; original five discoveries resolved; recursive/forward closure incomplete。

## Attacks on Approximate Caches in Text-to-Image Diffusion Models

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/sun-desen)；时间标记：USENIX 2026 proceedings; conference 2026-08-12 to 2026-08-14 is within window; earliest online date not established。
- 作者：Desen Sun, Shuncheng Jie, and Sihang Liu, University of Waterloo
- 对象：diffusion models, approximate cache, remote covert channel；类型：cache_side_channel。
- 核心想法：近似缓存复用形成跨用户隐蔽通信及提示词命中泄漏。
- 作者报告：作者还讨论缓存投毒，报告远程服务场景的验证。
- 限制与下一步：隐蔽通信、缓存提示词恢复与投毒是不同能力；具体缓存接口、辅助信息和部署条件待正文核查。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX 2026 session abstract; print TOC used only for bibliographic identity。
- 代码/数据核查：not checked；引用追踪：pending。

## Behind Bars: A Side-Channel Attack on NVIDIA MIG Cache Partitioning Using Memory Barriers

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/gu-cheng)；时间标记：USENIX 2026 proceedings; conference 2026-08-12 to 2026-08-14 is within window; earliest online date not established。
- 作者：Cheng Gu, University of Rochester; Reese Levine, UC Santa Cruz; Zhenkai Zhang, Clemson University; Tyler Sorensen, Microsoft and UC Santa Cruz; Yanan Guo, University of Rochester
- 对象：NVIDIA MIG, memory barriers, GPU, LLM；类型：microarchitectural_attack。
- 核心想法：GPU memory barrier 的跨 MIG 分区副作用使攻击者推断其他实例的内核启动模式。
- 作者报告：作者在 MIG 开启时观察跨 L2 分区时序干扰，并讨论 LLM 推理场景。
- 限制与下一步：内核模式泄漏不等于任意 GPU 内存读出；具体设备、权限和内容恢复范围待正文核查。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX 2026 session abstract; print TOC used only for bibliographic identity。
- 代码/数据核查：not checked；引用追踪：pending。

## Bridges to Self: Silent Web-to-App Tracking on Mobile via Localhost

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/vlummens)；时间标记：USENIX 2026 proceedings; conference 2026-08-12 to 2026-08-14 is within window; earliest online date not established。
- 作者：Tim Vlummens, COSIC, KU Leuven; Aniketh Girish and Nipuna Weerasekara, IMDEA Networks Institute; Frederik Zuiderveen Borgesius and Gunes Acar, Radboud University; Narseo Vallina-Rodriguez, IMDEA Networks Institute Distinguished Paper Award Winner
- 对象：Android, localhost, WebRTC, mDNS；类型：cross_context_tracking。
- 核心想法：分析网页与本地应用桥接身份，以及绕过隔离防护的额外网络侧通道。
- 作者报告：作者结合网页测量和 Android 分析讨论 localhost 跟踪与补丁绕过。
- 限制与下一步：核心 localhost 通信包含直接跨上下文连接；纳入的是隔离/侧通道部分，不能统一称为被动功耗或缓存攻击。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX 2026 session abstract; print TOC used only for bibliographic identity。
- 代码/数据核查：not checked；引用追踪：pending。

## Charting the Cache Side-Channel Frontier: A Systematic Study of Eviction Set Construction on Apple Silicon

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/wang-han)；时间标记：USENIX 2026 proceedings; conference 2026-08-12 to 2026-08-14 is within window; earliest online date not established。
- 作者：Han Wang, Yakun Wu, Yusi Feng, and Yinqian Zhang, Southern University of Science and Technology
- 对象：Apple Silicon, M4, eviction sets, SLC；类型：microarchitectural_measurement。
- 核心想法：逆向 M4 的 victim buffer、预取与分配行为，改进 L2/SLC eviction set 构造。
- 作者报告：摘要报告 L2 与 SLC 构造成功率，并形成跨 cluster 的细粒度原语。
- 限制与下一步：构造成功率不等于密钥恢复成功率；M4 结果不自动适用于所有 Apple 芯片。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX 2026 session abstract; print TOC used only for bibliographic identity。
- 代码/数据核查：not checked；引用追踪：pending。

## DDR-SSE: Duplicated Retrieval of Documents for System-wide Secure Searchable Symmetric Encryption

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/gui)；时间标记：USENIX 2026 proceedings; conference 2026-08-12 to 2026-08-14 is within window; earliest online date not established。
- 作者：Zichen Gui, University of Georgia; Simon-Philipp Merz and Kenneth G. Paterson, ETH Zürich; Sikhar Patranabis, IBM Research India
- 对象：SSE, access patterns, document retrieval；类型：metadata_countermeasure。
- 核心想法：DDR-SSE 用重复存储与随机取回抑制索引和文档取回的全系统泄漏。
- 作者报告：作者给出模拟式泄漏模型证明、查询重建评估与性能实验。
- 限制与下一步：需核查泄漏函数及辅助知识；协议模型不能覆盖全部端点物理通道。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX 2026 session abstract; print TOC used only for bibliographic identity。
- 代码/数据核查：not checked；引用追踪：pending。

## DuetORAM: Two-Server Distributed ORAM with Constant Rounds and O(log N) Communication

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/li-feng)；时间标记：USENIX 2026 proceedings; conference 2026-08-12 to 2026-08-14 is within window; earliest online date not established。
- 作者：Feng Li and Xiangfu Song, Nanyang Technological University; Yingying Li, Hangzhou Normal University; Lisha Yao and Guomin Yang, Singapore Management University; Tianwei Zhang, Nanyang Technological University; Robert H. Deng, Singapore Management University
- 对象：ORAM, DORAM, access patterns；类型：access_pattern_countermeasure。
- 核心想法：DuetORAM 在双服务器模型中以复制到份额编码及预处理打乱隐藏访问模式。
- 作者报告：作者报告常数轮访问与网络环境下的实现比较。
- 限制与下一步：服务器串谋和对手模型须从正文确认；访问模式隐私不等于密码实现功耗安全。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX 2026 session abstract; print TOC used only for bibliographic identity。
- 代码/数据核查：not checked；引用追踪：pending。

## Exploiting Hidden Resource Contention in Selective Speculation Defenses

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/cheng)；时间标记：USENIX 2026 proceedings; conference 2026-08-12 to 2026-08-14 is within window; earliest online date not established。
- 作者：Xiaoyu Cheng, Southeast University; Fei Tong, Southeast University; Purple Mountain Laboratories; Jiangsu Province Engineering Research Center of Security for Ubiquitous Network; Zhenyu Lei, Fang Jiang, Zhe Zhou, and Guang Cheng, Southeast University; Trevor E. Carlson, National University of Singapore (NUS)
- 对象：transient execution, reservation station, RISC-V, x86；类型：microarchitectural_attack。
- 核心想法：调度前的微操作展开、条件执行与依赖链造成选择性推测防护遗漏的 reservation-station 争用。
- 作者报告：防护绕过在 x86/RISC-V gem5 模型中构造；另在真实 CPU 验证争用信号和程序模式。
- 限制与下一步：模拟中的 STT/DOLMA 绕过与真实 CPU 争用验证必须分开，不能称为已攻破部署中的相同硬件防护。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX 2026 session abstract; print TOC used only for bibliographic identity。
- 代码/数据核查：not checked；引用追踪：pending。

## From Length to Content: Token-Length Side-Channel Attacks on LLM API Merged Outputs

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/li-sijia)；时间标记：USENIX 2026 proceedings; conference 2026-08-12 to 2026-08-14 is within window; earliest online date not established。
- 作者：Sijia Li, Tianyu Cui, Miao Chen, Xinjie Lin, and Zheyuan Gu, Zhongguancun Laboratory; Xinhao Deng, Tsinghua University; Ke Xu and Qi Li, Tsinghua University and Zhongguancun Laboratory
- 对象：LLM, encrypted traffic, token length；类型：traffic_side_channel。
- 核心想法：PromptEcho 从合并 token 的加密响应长度约束恢复部分语义。
- 作者报告：作者在商用 API 交互流量上评价主题识别及语义相似度。
- 限制与下一步：语义相似不等于逐字恢复；服务版本、训练先验和真实流量条件待正文核查。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX 2026 session abstract; print TOC used only for bibliographic identity。
- 代码/数据核查：not checked；引用追踪：pending。

## Fully Oblivious Differential Privacy for Frequency Estimation in the Augmented Shuffle Model with Trusted Processors

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/murakami)；时间标记：USENIX 2026 proceedings; conference 2026-08-12 to 2026-08-14 is within window; earliest online date not established。
- 作者：Takao Murakami, ISM/ROIS/AIST/RIKEN AIP; Yuichi Sei, UEC; Reo Eriguchi, AIST
- 对象：SGX, obliviousness, differential privacy；类型：access_pattern_countermeasure。
- 核心想法：FODP 为可信处理器中的 shuffle-DP 同时建模内外存访问和控制流。
- 作者报告：作者给出内存规模混淆框架、具体算法及 SGX 上的比较。
- 限制与下一步：DP 输出隐私与 TEE 内部观测保护分开；FODP 定义覆盖范围待正文证明核查。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX 2026 session abstract; print TOC used only for bibliographic identity。
- 代码/数据核查：not checked；引用追踪：pending。

## Injected and Leaked: Actively Inducing Side-Channel Leakage Using Electromagnetic Injection and Hardware Nonlinearity

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/yan-haoran)；时间标记：USENIX 2026 proceedings; conference 2026-08-12 to 2026-08-14 is within window; earliest online date not established。
- 作者：Haoran Yan, Ziyu Shao, and Shuhao Zhang, The Hong Kong University of Science and Technology (Guangzhou); Qinhong Jiang, The Hong Kong Polytechnic University; Yan Long, The Hong Kong University of Science and Technology (Guangzhou)
- 对象：electromagnetic injection, nonlinearity, analog signals；类型：active_physical_side_channel。
- 核心想法：利用非线性硬件把低频敏感信号调制到主动注入的 EM 载波上。
- 作者报告：作者在耳机音频、传感器和设备功耗场景报告注入诱发的泄漏。
- 限制与下一步：属于主动激励与非线性混合，不是无需发射的纯被动窃听，也未证明 PQC 密钥恢复。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX 2026 session abstract; print TOC used only for bibliographic identity。
- 代码/数据核查：not checked；引用追踪：pending。

## InstantOMR: Oblivious Message Retrieval with Low Latency and Optimal Parallelizability

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/liang)；时间标记：USENIX 2026 proceedings; conference 2026-08-12 to 2026-08-14 is within window; earliest online date not established。
- 作者：Haofei Liang, Shanghai Jiao Tong University; Zeyu Liu, Yale University; Eran Tromer, Boston University; Xiang Xie, Primus Labs; Yu Yu, Shanghai Jiao Tong University
- 对象：OMR, receiver metadata, FHE；类型：metadata_privacy_protocol。
- 核心想法：InstantOMR 联合 TFHE 与 RLWE 操作降低隐藏消息接收关联的检索延迟。
- 作者报告：作者给出实现与并行性能比较，部分评估使用另一库的估计。
- 限制与下一步：按通信元数据防护纳入；使用格技术不等于研究 PQC 实现侧信道，估计和实测性能应分列。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX 2026 session abstract; print TOC used only for bibliographic identity。
- 代码/数据核查：not checked；引用追踪：pending。

## LPG: Raise Your Location Privacy Game in Direct-to-Cell LEO Satellite Networks

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/shi-quan)；时间标记：USENIX 2026 proceedings; conference 2026-08-12 to 2026-08-14 is within window; earliest online date not established。
- 作者：Quan Shi, National University of Singapore; Liying Wang, Peking University; Prosanta Gope, University of Sheffield; Qi Liang and Haowen Wang, Beijing University of Posts and Telecommunications; Qirui Liu, Peking University; Chenren Xu, Peking University and Key Laboratory of High Confidence Software Technologies, Ministry of Education (PKU); Shangguang Wang and Qing Li, Beijing University of Posts and Telecommunications; Biplab Sikdar, National University of Singapore Distinguished Paper Award Winner
- 对象：LEO satellite, location metadata, identity privacy；类型：metadata_privacy_protocol。
- 核心想法：LPG 将卫星运营商所见位置与移动运营商管理的身份解耦。
- 作者报告：作者报告在轨卫星与手机验证，并允许配置位置披露粒度。
- 限制与下一步：这是协议层身份位置关联防护，不是功耗攻击；官方勘误仅改通讯作者脚注。 Erratum source: usenix-2026-errata-shi.
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX 2026 session abstract; print TOC used only for bibliographic identity。
- 代码/数据核查：not checked；引用追踪：pending。

## M-Step: A Single-Stepping Framework for Side-Channel Analysis on TrustZone-M

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/rodrigues)；时间标记：USENIX 2026 proceedings; conference 2026-08-12 to 2026-08-14 is within window; earliest online date not established。
- 作者：Cristiano Rodrigues, Centro ALGORITMI, Universidade do Minho; Marton Bognar, DistriNet, KU Leuven; Sandro Pinto, Centro ALGORITMI, Universidade do Minho; Jo Van Bulck, DistriNet, KU Leuven
- 对象：TrustZone-M, interrupt latency, RSA, Mbed TLS；类型：side_channel_framework。
- 核心想法：M-Step 利用中断延迟反馈在 TrustZone-M 上实现高分辨率单步观察。
- 作者报告：作者报告针对 Mbed TLS 的单迹线 RSA 密钥恢复。
- 限制与下一步：需要相应定时中断控制；单迹线不等于远程无权限，受影响版本和配置待正文核查。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX 2026 session abstract; print TOC used only for bibliographic identity。
- 代码/数据核查：not checked；引用追踪：pending。

## Network-Level Prompt and Trait Leakage in Local Research Agents

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/jeong)；时间标记：USENIX 2026 proceedings; conference 2026-08-12 to 2026-08-14 is within window; earliest online date not established。
- 作者：Hyejun Jeong, Mohammadreza Teymoorianfard, Abhinav Kumar, Amir Houmansadr, and Eugene Bagdasarian, University of Massachusetts Amherst
- 对象：research agents, IP metadata, timing；类型：traffic_side_channel。
- 核心想法：利用研究 Agent 访问域名/IP 及时间模式推断用户请求和跨会话特征。
- 作者报告：作者使用真实查询与合成人设评价功能语义恢复，并讨论部分观察。
- 限制与下一步：网络元数据推断不等于读取加密载荷；合成人设、真实请求及语义评分须分别理解。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX 2026 session abstract; print TOC used only for bibliographic identity。
- 代码/数据核查：not checked；引用追踪：pending。

## Oblivious Signaling

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/shuhan)；时间标记：USENIX 2026 proceedings; conference 2026-08-12 to 2026-08-14 is within window; earliest online date not established。
- 作者：Mirza Kamrul Bashar Shuhan, George Mason University; Foteini Baldimtsi, George Mason University & Mysten Labs; Giuseppe Ateniese, George Mason University
- 对象：receiver metadata, FHE, oblivious signaling；类型：metadata_privacy_protocol。
- 核心想法：用均匀同态更新隐藏消息目的地，把接收检索成本转移到发送。
- 作者报告：作者形式化不可信服务器下的接收者隐私，并比较原型成本。
- 限制与下一步：接收者隐私定义和串谋范围需正文核查；不声称消除全部通信时序泄漏。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX 2026 session abstract; print TOC used only for bibliographic identity。
- 代码/数据核查：not checked；引用追踪：pending。

## PROBE+DETECT+MITIGATE (PDM): Enabling Cloud Tenants to Self-Defend against Microarchitectural Attacks

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/daneshmand)；时间标记：USENIX 2026 proceedings; conference 2026-08-12 to 2026-08-14 is within window; earliest online date not established。
- 作者：Arash Daneshmand, University of British Columbia Okanagan and Concordia University; Hugo Kermabon-Bobinnec, Concordia University; Lingyu Wang, University of British Columbia Okanagan and Concordia University; Makan Pourzandi, Ericsson Security Research, Ericsson Canada; Suryadipta Majumdar, Concordia University; Yosr Jarraya, Ericsson Security Research, Ericsson Canada
- 对象：cloud, Prime+Probe, Spectre, attack detection；类型：countermeasure。
- 核心想法：PDM 让云租户以探测观察攻击活动，并按需启动混淆与内存加密。
- 作者报告：作者在测试床和 AWS Fargate 评价检测率、误报及开销。
- 限制与下一步：结果依赖被测试攻击与噪声；检测有效不等于所有隐蔽攻击都可发现。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX 2026 session abstract; print TOC used only for bibliographic identity。
- 代码/数据核查：not checked；引用追踪：pending。

## Plaintext Recovery Against Post-Filtering Access Control

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/espiritu)；时间标记：USENIX 2026 proceedings; conference 2026-08-12 to 2026-08-14 is within window; earliest online date not established。
- 作者：Zachary Espiritu, MongoDB Research; David Cash, University of Chicago
- 对象：PostgreSQL, Elasticsearch, timing, query reconstruction；类型：application_side_channel。
- 核心想法：后过滤访问控制中的存在性泄漏可与范围或前缀查询结合，放大成记录与文本恢复。
- 作者报告：作者分别利用 PostgreSQL RLS 时序与 Elasticsearch/OpenSearch DLS 评分/扩展行为。
- 限制与下一步：需要丰富查询接口及相应访问能力；不同系统通道不能统一称为单一时间攻击。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX 2026 session abstract; print TOC used only for bibliographic identity。
- 代码/数据核查：not checked；引用追踪：pending。

## Principled Design of Indexing Functions for Memory Coloring

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/duebler)；时间标记：USENIX 2026 proceedings; conference 2026-08-12 to 2026-08-14 is within window; earliest online date not established。
- 作者：Stephan Dübler and Jana Hofmann, Max Planck Institute for Security and Privacy (MPI-SP); Boris Köpf and Stavros Volos, Azure Research, Microsoft Distinguished Artifact Award Winner
- 对象：cache coloring, DRAM, index functions；类型：microarchitectural_countermeasure。
- 核心想法：以索引函数核空间交集为约束，合成支持多资源隔离的 memory coloring 函数。
- 作者报告：作者在服务器级 CPU 案例中同时划分 L3 cache 与 DRAM bank。
- 限制与下一步：设计空间和隔离资源有限；平均性能开销不证明全部共享资源通道关闭。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX 2026 session abstract; print TOC used only for bibliographic identity。
- 代码/数据核查：not checked；引用追踪：pending。

## Remise: Authorized Anonymous Communication Systems

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/ravi-rohan)；时间标记：USENIX 2026 proceedings; conference 2026-08-12 to 2026-08-14 is within window; earliest online date not established。
- 作者：Rohan Ravi, Paritosh Shukla, and Adithya Vadapalli, IIT Kanpur
- 对象：DORAM, anonymous communication, access patterns；类型：metadata_countermeasure。
- 核心想法：Remise 以双服务器 DORAM 保护访问索引、授权令牌及通信关系。
- 作者报告：作者在两种通信模式中给出协议和原型比较。
- 限制与下一步：两服务器不串谋与半诚实等假设需保留，不能改写为无信任匿名通信。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX 2026 session abstract; print TOC used only for bibliographic identity。
- 代码/数据核查：not checked；引用追踪：pending。

## SONIC: Concurrent Oblivious RAM & Data Structures for Low-Latency and High-Throughput

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/talur)；时间标记：USENIX 2026 proceedings; conference 2026-08-12 to 2026-08-14 is within window; earliest online date not established。
- 作者：Nihal Talur and Ioannis Demertzis, UC Santa Cruz
- 对象：ORAM, TEE, access patterns, concurrency；类型：access_pattern_countermeasure。
- 核心想法：SONIC 将 RingORAM 并发化，处理 enclave 中的访问、驱逐和 stash 协同。
- 作者报告：作者比较单服务器吞吐、延迟及多服务器扩展成本。
- 限制与下一步：必须区分不同数据量、服务器预算与比较实现；ORAM 不自动屏蔽全部物理通道。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX 2026 session abstract; print TOC used only for bibliographic identity。
- 代码/数据核查：not checked；引用追踪：pending。

## Side-Channel Attacks on Open vSwitch

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/kim-daewoo)；时间标记：USENIX 2026 proceedings; conference 2026-08-12 to 2026-08-14 is within window; earliest online date not established。
- 作者：Daewoo Kim and Sihang Liu, University of Waterloo
- 对象：Open vSwitch, software cache, remote timing；类型：network_side_channel。
- 核心想法：OVS 缓存层级形成远程隐蔽通道、报头字段恢复与流量率监测原语。
- 作者报告：作者比较不同缓存的攻击方式并讨论防护。
- 限制与下一步：报头、流量率和载荷内容是不同恢复目标；网络可达性及环境条件待正文核查。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX 2026 session abstract; print TOC used only for bibliographic identity。
- 代码/数据核查：not checked；引用追踪：pending。

## SoK: Deep Learning-based Physical Side-channel Analysis

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/karayalcin)；时间标记：USENIX 2026 proceedings; conference 2026-08-12 to 2026-08-14 is within window; earliest online date not established。
- 作者：Sengim Karayalcin, Leiden University; Marina Krček, Radboud University; Stjepan Picek, University of Zagreb Faculty of Electrical Engineering and Computing & Radboud University
- 对象：deep learning, physical side channels, reproducibility；类型：systematization。
- 核心想法：梳理深度学习物理侧信道分析的分类、趋势和复现问题。
- 作者报告：摘要强调攻击评价与完整复现依赖谨慎的实验设置。
- 限制与下一步：目前只读摘要；已取得全文但未将自动抽取片段算作完整阅读，综述引文仍待逐项追踪。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX 2026 session abstract; print TOC used only for bibliographic identity。
- 代码/数据核查：not checked；引用追踪：pending。

## SophOMR: Improved Oblivious Message Retrieval from SIMD-Aware Homomorphic Compression

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/lee-keewoo)；时间标记：USENIX 2026 proceedings; conference 2026-08-12 to 2026-08-14 is within window; earliest online date not established。
- 作者：Keewoo Lee, Ethereum Foundation; Yongdong Yeo, Seoul National University
- 对象：OMR, FHE, receiver metadata；类型：metadata_privacy_protocol。
- 核心想法：SophOMR 用 SIMD 友好的同态压缩降低隐私消息检索开销。
- 作者报告：作者比较给定消息数量及相关消息上界下的时间和摘要体积。
- 限制与下一步：协议接收者隐私与实现物理泄漏分开；未核查完整安全模型或代码。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX 2026 session abstract; print TOC used only for bibliographic identity。
- 代码/数据核查：not checked；引用追踪：pending。

## Spectre on RISC-V Silicon: Attacks and Defenses on Commercial Out-of-Order Processors

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/gerlach)；时间标记：USENIX 2026 proceedings; conference 2026-08-12 to 2026-08-14 is within window; earliest online date not established。
- 作者：Lukas Gerlach, CISPA Helmholtz Center for Information Security; Marton Bognar, DistriNet, KU Leuven; Daniel Weber and Michael Schwarz, CISPA Helmholtz Center for Information Security; Jo Van Bulck, DistriNet, KU Leuven
- 对象：RISC-V, Spectre, kernel memory；类型：transient_execution_attack。
- 核心想法：在商业乱序 RISC-V 硅片上评价 Spectre，并研究可抑制推测的指令。
- 作者报告：作者报告 P550、C910/C920 的攻击与软件防护比较。
- 限制与下一步：论文所列商业核心不等于所有未来 RISC-V；内核、编译器版本和补丁状态须固定。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX 2026 session abstract; print TOC used only for bibliographic identity。
- 代码/数据核查：not checked；引用追踪：pending。

## TIMESLICE-SANDWICH: A GPU Side-Channel Attack Exploiting Time-Sliced Scheduling

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/kim-hodong)；时间标记：USENIX 2026 proceedings; conference 2026-08-12 to 2026-08-14 is within window; earliest online date not established。
- 作者：Hodong Kim and Gyeongsup Lim, Korea University; Seunghee Shin, State University of New York at Binghamton; Youngjoo Shin and Junbeom Hur, Korea University
- 对象：GPU, time slicing, website fingerprinting；类型：scheduling_side_channel。
- 核心想法：TIMESLICE-SANDWICH 由 GPU 时间片长度变化推断并发任务执行模式。
- 作者报告：作者评价神经网络结构恢复和浏览器网站指纹。
- 限制与下一步：该通道不要求特定共享资源争用，但仍依赖 GPU 调度和共驻条件；不是任意内存读出。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX 2026 session abstract; print TOC used only for bibliographic identity。
- 代码/数据核查：not checked；引用追踪：pending。

## Towards Practical Few-shot Multi-tab Website Fingerprinting

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/liu-lin)；时间标记：USENIX 2026 proceedings; conference 2026-08-12 to 2026-08-14 is within window; earliest online date not established。
- 作者：Lin Liu and Ziling Wei, National University of Defense Technology; Zhuotao Liu and Xinhao Deng, Tsinghua University; Zixuan Dong and Shuhui Chen, National University of Defense Technology
- 对象：Tor, website fingerprinting, few-shot；类型：traffic_side_channel。
- 核心想法：MMF 将多标签混合流量分类改为支持集引导的网站存在性检测。
- 作者报告：作者使用公开及新采集的多标签页数据评价少样本识别。
- 限制与下一步：Novel Precision@k 改善不是任意开放世界去匿名成功率；训练、采集与标签划分待核查。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX 2026 session abstract; print TOC used only for bibliographic identity。
- 代码/数据核查：not checked；引用追踪：pending。

## TrojPix: Electromagnetic Covert Channels via Imperceptible Pixel Modulation

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/zhang-guoming)；时间标记：USENIX 2026 proceedings; conference 2026-08-12 to 2026-08-14 is within window; earliest online date not established。
- 作者：Guoming Zhang, Shandong University and Quan Cheng Laboratory; Huiting Zhang, Zhenwei Lu, Heqiang Fu, Xin Gao, Riccardo Spolaor, and Yetong Cao, Shandong University; Yanni Yang and Pengfei Hu, Shandong University and Quan Cheng Laboratory
- 对象：EM emissions, display cables, covert channel；类型：physical_covert_channel。
- 核心想法：TrojPix 用不可察觉的像素调制控制显示电缆电磁发射。
- 作者报告：作者在多种显示器与电缆上评价两种主动编码模式。
- 限制与下一步：需要发送端参与调制；最高吞吐与最大距离不可假定同配置同时达到，不是自然泄漏密钥的结果。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX 2026 session abstract; print TOC used only for bibliographic identity。
- 代码/数据核查：not checked；引用追踪：pending。

## Turn Your Face Into An Attack Surface: Screen Attack Using Facial Reflections in Video Conferencing

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/huang-yong)；时间标记：USENIX 2026 proceedings; conference 2026-08-12 to 2026-08-14 is within window; earliest online date not established。
- 作者：Yong Huang, Yanzhao Lu, Mingyang Chen, En Zhang, and Jiazi Li, Zhengzhou University; Wanqing Tu, Durham University
- 对象：optical reflections, video conferencing, application inference；类型：physical_side_channel。
- 核心想法：FaceTell 从视频会议中的面部屏幕反射推断应用活动。
- 作者报告：作者报告多设备、会议平台、参与者和室内环境实验。
- 限制与下一步：应用类别识别不等于屏幕文字或密码恢复；受控类别与开放环境泛化需区分。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX 2026 session abstract; print TOC used only for bibliographic identity。
- 代码/数据核查：not checked；引用追踪：pending。

## UncoreBleed: AEX-Free, High-Resolution, and Low-Noise Side-Channel Attacks on SGX Enclaved Execution

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/chen-decheng)；时间标记：USENIX 2026 proceedings; conference 2026-08-12 to 2026-08-14 is within window; earliest online date not established。
- 作者：Decheng Chen, South China University of Technology; Zhi Zhang, The University of Western Australia; Zhenkai Zhang, Clemson University; Xin Zhang, Shandong University; Yansong Gao, Southeast University; Yi Zou, South China University of Technology
- 对象：SGX, uncore PMC, RSA；类型：microarchitectural_attack。
- 核心想法：UncoreBleed 研究 enclave 执行时仍活动的 uncore 性能计数器及地址过滤。
- 作者报告：摘要报告 64 B 观察粒度、图像重建及单次 RSA 解密相关恢复。
- 限制与下一步：计数器配置权限、Xeon 型号和 TLBlur/AEX-Notify 配置待正文核查；不泛化为普通用户通道。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX 2026 session abstract; print TOC used only for bibliographic identity。
- 代码/数据核查：not checked；引用追踪：pending。

## Unlocking the True Potential of Decryption Failure Oracles: A Hybrid Adaptive-LDPC Attack on ML-KEM Using Imperfect Oracles

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/guo-qian)；时间标记：USENIX 2026 proceedings; conference 2026-08-12 to 2026-08-14 is within window; earliest online date not established。
- 作者：Qian Guo, Denis Nabokov, and Thomas Johansson, Lund University
- 对象：ML-KEM, decryption failure oracle, LDPC, GoFetch；类型：attack。
- 核心想法：将自适应查询与 LDPC 信念传播结合，利用有误差的解密失败预言机。
- 作者报告：正文在 M1 MacBook Air/macOS 13.5 讨论 GoFetch 实例。100 次 ML-KEM-512 尝试中，作者把距离真值不超过四个系数的 73 次归为成功；表 3 只汇总这部分。
- 限制与下一步：2,950 是抽象预言机查询数。实测表 3 的 6,047.84 平均迹线只计成功子集的恢复阶段，排除校准；约 25 分钟包含近半校准时间。不能把成功判据等同于逐系数零差错，也不能把 1024 的适用性讨论当实测。
- 阅读层级：selected_full_text_sections；来源：official final proceedings PDF and session abstract。
- 已读章节：PDF pp.12-16: GoFetch threat model, measurement setup, results and success definition, limitations, artifact statement, refs.1-4; Table 3 visually checked
- 代码/数据核查：author declares https://doi.org/10.5281/zenodo.17899501 in PDF p16; contents not inspected or run；引用追踪：pending。

## VROOM: Accelerating (Almost All) Number-Theoretic Cryptography Using Vectorization and the Residue Number System

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/langowski)；时间标记：USENIX 2026 proceedings; conference 2026-08-12 to 2026-08-14 is within window; earliest online date not established。
- 作者：Simon Langowski, Kaiwen He, and Srinivas Devadas, MIT
- 对象：RNS, vectorization, constant time, RSA, BLS；类型：constant_time_implementation。
- 核心想法：VROOM 用剩余数系统和向量运算设计通用模乘，摘要声明恒时算法。
- 作者报告：作者报告 RSA/BLS 和 GPU 模乘性能。
- 限制与下一步：算法和性能贡献含恒时实现，但恒时依据、指令数据依赖及全部物理通道未核查。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX 2026 session abstract; print TOC used only for bibliographic identity。
- 代码/数据核查：not checked；引用追踪：pending。

## VeCT: Secure and Efficient Constant-Time Code Rewriting with Vector Extensions

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/jiang-qisheng)；时间标记：USENIX 2026 proceedings; conference 2026-08-12 to 2026-08-14 is within window; earliest online date not established。
- 作者：Qisheng Jiang and Danfeng Zhang, Duke University
- 对象：constant time, AVX-512, LLVM；类型：constant_time_rewriting。
- 核心想法：VeCT 用向量扩展改善恒时代码转换，并为 AVX-512 建立经验安全使用规则。
- 作者报告：作者报告已有重写器中的漏洞及 AES/Blowfish 等程序性能比较。
- 限制与下一步：统计筛查指令不构成所有微架构的普遍保证；恒时时间模型不等于功耗安全。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX 2026 session abstract; print TOC used only for bibliographic identity。
- 代码/数据核查：not checked；引用追踪：pending。

## Your Keywords Know Each Other: Breaking SSE with <1% Leaked Documents

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/bian-mingyu)；时间标记：USENIX 2026 proceedings; conference 2026-08-12 to 2026-08-14 is within window; earliest online date not established。
- 作者：Mingyu Bian, Jiabei Wang, Dandan Xu, Guangyu Huang, and Yongbin Zhou, School of Cyber Science and Engineering, Nanjing University of Science and Technology
- 对象：SSE, query recovery, language models；类型：leakage_abuse_attack。
- 核心想法：Whisper 用语言模型生成语料及词向量补充关键词关系，增强 SSE 模式泄漏的查询恢复。
- 作者报告：作者在多个语料上评价少量文档泄漏及 padding/volume-hiding 防护。
- 限制与下一步：辅助语言知识与已知文档比例必须列明；官方摘要的 1727% 字串疑似格式丢失，不据此计算提升幅度。
- 阅读层级：abstract_and_bibliographic_metadata；来源：official USENIX 2026 session abstract; print TOC used only for bibliographic identity。
- 代码/数据核查：not checked；引用追踪：pending。

## microSCALE: Static Analysis for Microarchitectural Side-channel Leakage Evaluation

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/kumar-e)；时间标记：USENIX 2026 proceedings; conference 2026-08-12 to 2026-08-14 is within window; earliest online date not established。
- 作者：Akshay Kumar E, Pranav Krishna N, Annapurna Valiveti, Pallavi Borkar, Aditi Roy, and Chester Rebeiro, IIT Madras
- 对象：RTL, RISC-V, Rocket Core, GIFT, ASCON, AES；类型：leakage_analysis。
- 核心想法：microSCALE 静态追踪 CPU RTL 中份额重组并映射到软件指令交互。
- 作者报告：正文以 FPGA 上一轮 GIFT 的百万 EM 迹线作验证；90.3% 指 TVLA 超阈样点减少，而非攻击成功率减少。
- 限制与下一步：表 4 的静态转换泄漏和 TVLA 样点是不同指标。PDF p13 的 500 kS/s、2 µs、50 MHz、约十点每周期互不相容，已视读确认，采集参数待更正。
- 阅读层级：selected_full_text_sections；来源：official final proceedings PDF and session abstract。
- 已读章节：PDF pp.13-14: one-round GIFT FPGA validation and metric definitions; p13 visually checked, sampling-rate inconsistency retained
- 代码/数据核查：artifact PDF link available on official page; contents not inspected or run；引用追踪：pending。

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

## From Perfect to Approximate Hints: Efficient LWE Secret Recovery Leveraging Low Hamming Weight

- 来源：[ePrint 2026](https://eprint.iacr.org/2026/1081)；时间标记：ePrint received 2026-05-28 within frozen window。
- 作者：Minki Hhan; Ga Hee Hong; Jiseung Kim; Changmin Lee; JeongHwan Lee
- 对象：LWE, FHE, sparse ternary secrets, hints；类型：pqc_side_information_solver。
- 核心想法：利用稀疏三元秘密结构减少 LWE 精确/近似提示的求解需求。
- 作者报告：摘要报告 GAA 条件分析与经验结果；n=2^15、h=32 时为 320 条提示，h=192 的 OpenFHE 场景仅验证精确提示。
- 限制与下一步：提示获取成本未由摘要建立；不是 ML-KEM 实测功耗恢复，O(h log h) 不能当作无条件保证。ePrint 正文访问 403，保留未读。
- 阅读层级：abstract_and_bibliographic_metadata；来源：https://eprint.iacr.org/2026/1081。
- [详细阅读记录](notes/sp2026-scope-identity-and-frequency-bounds-20261114.md)
- 代码/数据核查：not checked; requested PDF returned HTTP 403 text/html challenge, not a readable paper；引用追踪：pending。
