# 已阅读的相邻主题与方法背景

当前 179 条；保留在目录与引用图中，不计入侧信道纳入论文数量。后续全文证据可以修订范围判定。

## A Compact Hardware Implementation of CCA-Secure Key Exchange Mechanism CRYSTALS-KYBER on FPGA

- 来源：[TCHES 2021](https://doi.org/10.46586/tches.v2021.i2.328-356)。
- 判定依据：给出 CCA 安全 Kyber 的完整 FPGA 架构与资源调度；协议层 CCA 保证不能直接说明物理实现安全。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Fault Attacks on CCA-secure Lattice KEMs

- 来源：[TCHES 2021](https://doi.org/10.46586/tches.v2021.i2.37-60)。
- 判定依据：研究指令跳过后有效/无效故障所形成的不等式，含 Kyber/NewHope 模拟及 Cortex-M4 时钟毛刺；保留为故障预言机与求解背景，不把故障解封装次数当成功耗迹线数。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Learning Parity with Physical Noise: Imperfections, Reductions and FPGA Prototype

- 来源：[TCHES 2021](https://doi.org/10.46586/tches.v2021.i3.390-417)。
- 判定依据：LPPN 的输出相关物理误差、到 LPN 的难度归约与 FPGA 原型；摘要侧重误差分布和问题安全，没有具体侧信道读取或防护评估，保留物理学习背景。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## NTT Multiplication for NTT-unfriendly Rings: New Speed Records for Saber and NTRU on Cortex-M4 and AVX2

- 来源：[TCHES 2021](https://doi.org/10.46586/tches.v2021.i2.159-188)。
- 判定依据：研究面向不适合直接 NTT 的 Saber/NTRU 环的变换与乘法加速，摘要的速度比较不能证明侧信道保护。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Polynomial Multiplication in NTRU Prime: Comparison of Optimization Strategies on Cortex-M4

- 来源：[TCHES 2021](https://doi.org/10.46586/tches.v2021.i1.217-238)。
- 判定依据：研究 NTRU Prime 的 NTT/混合基数乘法在 Cortex-M4 上的速度与内存折衷，摘要未提出泄漏评估。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Rapidly Verifiable XMSS Signatures

- 来源：[TCHES 2021](https://doi.org/10.46586/tches.v2021.i1.137-168)。
- 判定依据：修改 XMSS 签名搜索以加快公开验证，并分析经典/量子安全与多目标攻击；摘要没有侧信道贡献，签名搜索时间与验证性能不等同于秘密时序泄漏。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Scabbard: a suite of efficient learning with rounding key-encapsulation mechanisms

- 来源：[TCHES 2021](https://doi.org/10.46586/tches.v2021.i4.474-509)。
- 判定依据：提出 Scabbard 中的 LWR KEM 设计和实现比较；摘要未报告侧信道贡献。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## A Compact and High-Performance Hardware Architecture for CRYSTALS-Dilithium

- 来源：[TCHES 2022](https://doi.org/10.46586/tches.v2022.i1.270-295)。
- 判定依据：研究 Dilithium 紧凑 FPGA 架构及吞吐率/资源折衷，摘要未声称泄漏防护。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## A Logic and an Interactive Prover for the Computational Post-Quantum Security of Protocols

- 来源：[SP 2022](https://doi.org/10.1109/sp46214.2022.9833800)。
- 判定依据：证明协议面对量子攻击者的计算安全；摘要未涉及实现侧信道。
- 阅读来源：https://xplorestaging.ieee.org/document/9833800/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Annotating, Tracking, and Protecting Cryptographic Secrets with CryptoMPK

- 来源：[SP 2022](https://doi.org/10.1109/sp46214.2022.9833650)。
- 判定依据：CryptoMPK 保护敏感内存免受任意读取；摘要未给时间、微架构或物理非干扰保证。
- 阅读来源：https://xplorestaging.ieee.org/document/9833650/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Anti-Tamper Radio: System-Level Tamper Detection for Computing Systems

- 来源：[SP 2022](https://doi.org/10.1109/sp46214.2022.9833631)。
- 判定依据：ATR 通过无线传播变化检测物理插入；侧信道是防护动机，摘要未评价具体秘密泄漏，保留物理防拆背景。
- 阅读来源：https://xplorestaging.ieee.org/document/9833631/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## BAT: Small and Fast KEM over NTRU Lattices

- 来源：[TCHES 2022](https://doi.org/10.46586/tches.v2022.i2.240-265)。
- 判定依据：新的 NTRU 型 BAT KEM、解码与整数实现；文中 masking parameter p 是方案结构参数，不据此认定为抗侧信道掩码。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Blacksmith: Compromising Target Row Refresh by Rowhammering in the Frequency Domain

- 来源：[SP 2022](https://doi.org/10.1109/sp46214.2022.9833772)。
- 判定依据：Blacksmith 生成 Rowhammer 位翻转，当前摘要为故障向量与 TRR 绕过，没有附加观察秘密的侧信道关系。
- 阅读来源：https://xplorestaging.ieee.org/document/9833772/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## CFNTT: Scalable Radix-2/4 NTT Multiplication Architecture with an Efficient Conflict-free Memory Mapping Scheme

- 来源：[TCHES 2022](https://doi.org/10.46586/tches.v2022.i1.94-126)。
- 判定依据：通过冲突无关的存储映射优化 NTT；避免访存冲突不等于秘密无关或侧信道隔离。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## CirC: Compiler infrastructure for proof systems, software verification, and more

- 来源：[SP 2022](https://doi.org/10.1109/sp46214.2022.9833782)。
- 判定依据：CirC 是约束编译基础设施，用于证明、验证及 MPC；本摘要未给实现侧信道性质。
- 阅读来源：https://xplorestaging.ieee.org/document/9833782/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## HAMRAZ: Resilient Partitioning and Replication

- 来源：[SP 2022](https://doi.org/10.1109/sp46214.2022.9833661)。
- 判定依据：HAMRAZ 是分布式分区、复制及 Byzantine 情形的信息流保证，未说明时间或物理观察模型。
- 阅读来源：https://xplorestaging.ieee.org/document/9833661/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Hardening Circuit-Design IP Against Reverse-Engineering Attacks

- 来源：[SP 2022](https://doi.org/10.1109/sp46214.2022.9833634)。
- 判定依据：电路 IP 隐藏与逆向恢复的密码学模型，非功耗/EM 观察分析。
- 阅读来源：https://xplorestaging.ieee.org/document/9833634/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Highly Vectorized SIKE for AVX-512

- 来源：[TCHES 2022](https://doi.org/10.46586/tches.v2022.i2.41-68)。
- 判定依据：SIKE 的 AVX-512IFMA 并行算术与性能比较；摘要未明确提出恒时或泄漏评估贡献。保留历史实现背景，不作为当前部署推荐。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## How Not to Protect Your IP - An Industry-Wide Break of IEEE 1735 Implementations

- 来源：[SP 2022](https://doi.org/10.1109/sp46214.2022.9833605)。
- 判定依据：IEEE 1735 私钥提取与白盒 RSA 破解；摘要显示直接软件/白盒分析，不是侧信道测量。
- 阅读来源：https://xplorestaging.ieee.org/document/9833605/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Improved Plantard Arithmetic for Lattice-based Cryptography

- 来源：[TCHES 2022](https://doi.org/10.46586/tches.v2022.i4.614-636)。
- 判定依据：改进 Plantard 算术范围与约减效率；数值正确性和性能不等于泄漏安全。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Invisible Finger: Practical Electromagnetic Interference Attack on Touchscreen-based Electronic Devices

- 来源：[SP 2022](https://doi.org/10.1109/sp46214.2022.9833718)。
- 判定依据：Invisible Finger 主要为 EM 触摸注入；反馈与定位用于辅助注入，未见敏感值侧信道推断。
- 阅读来源：https://xplorestaging.ieee.org/document/9833718/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Low-Bandwidth Threshold ECDSA via Pseudorandom Correlation Generators

- 来源：[SP 2022](https://doi.org/10.1109/sp46214.2022.9833559)。
- 判定依据：门限 ECDSA 协议及通信复杂度，不能把秘密分享协议自动视为物理掩码。
- 阅读来源：https://xplorestaging.ieee.org/document/9833559/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## MatRiCT+: More Efficient Post-Quantum Private Blockchain Payments

- 来源：[SP 2022](https://doi.org/10.1109/sp46214.2022.9833655)。
- 判定依据：MatRiCT+ 为后量子隐私支付与证明系统，非实现泄漏研究。
- 阅读来源：https://xplorestaging.ieee.org/document/9833655/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Multi-Parameter Support with NTTs for NTRU and NTRU Prime on Cortex-M4

- 来源：[TCHES 2022](https://doi.org/10.46586/tches.v2022.i4.349-371)。
- 判定依据：在 Cortex-M4 上支持多个 NTRU/NTRU Prime 参数集，摘要侧重算法与实现效率。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Neon NTT: Faster Dilithium, Kyber, and Saber on Cortex-A72 and Apple M1

- 来源：[TCHES 2022](https://doi.org/10.46586/tches.v2022.i1.221-244)。
- 判定依据：以 Neon 和模乘优化加速 A72/M1 上的 NTT；摘要未验证时序或物理泄漏。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## PROTRR: Principled yet Optimal In-DRAM Target Row Refresh

- 来源：[SP 2022](https://doi.org/10.1109/sp46214.2022.9833664)。
- 判定依据：ProTRR 为 Rowhammer 刷新缓解及形式界，当前属故障防护背景。
- 阅读来源：https://xplorestaging.ieee.org/document/9833664/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Polynomial multiplication on embedded vector architectures

- 来源：[TCHES 2022](https://doi.org/10.46586/tches.v2022.i1.482-505)。
- 判定依据：优化嵌入式向量平台多项式乘法的性能与能耗；能量效率不是秘密相关功耗泄漏度量。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Privacy-from-Birth: Protecting Sensed Data from Malicious Sensors with VERSA

- 来源：[SP 2022](https://doi.org/10.1109/sp46214.2022.9833737)。
- 判定依据：VERSA 约束恶意软件直接访问 GPIO/传感值，未说明非预期侧信道的观察边界。
- 阅读来源：https://xplorestaging.ieee.org/document/9833737/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## RT-TEE: Real-time System Availability for Cyber-physical Systems using ARM TrustZone

- 来源：[SP 2022](https://doi.org/10.1109/sp46214.2022.9833604)。
- 判定依据：RT-TEE 主要保证实时可用性、外设访问与调度隔离，摘要未研究侧信道。
- 阅读来源：https://xplorestaging.ieee.org/document/9833604/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Roulette: A Diverse Family of Feasible Fault Attacks on Masked Kyber

- 来源：[TCHES 2022](https://doi.org/10.46586/tches.v2022.i4.637-660)。
- 判定依据：Roulette 利用掩码/盲化随机性促进故障命中，报告掩码 Kyber 的 Cortex-M4 时钟毛刺恢复。是防护交互的重要相邻研究，实际攻击仍依赖主动注入，不能宣称被动掩码安全被直接推翻。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## SMILE: Secure Memory Introspection for Live Enclave

- 来源：[SP 2022](https://doi.org/10.1109/sp46214.2022.9833714)。
- 判定依据：SMILE 为授权的 enclave 内存读取/诊断服务，不是通过间接观察推断秘密。
- 阅读来源：https://xplorestaging.ieee.org/document/9833714/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## SecFloat: Accurate Floating-Point meets Secure 2-Party Computation

- 来源：[SP 2022](https://doi.org/10.1109/sp46214.2022.9833697)。
- 判定依据：SecFloat 为精确浮点两方安全计算；不等于分析真实浮点硬件计时/功耗泄漏。
- 阅读来源：https://xplorestaging.ieee.org/document/9833697/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Security Analysis of the MLS Key Derivation

- 来源：[SP 2022](https://doi.org/10.1109/sp46214.2022.9833678)。
- 判定依据：MLS 密钥派生的协议计算安全与恢复性质，非物理实现泄漏。
- 阅读来源：https://xplorestaging.ieee.org/document/9833678/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Security Foundations for Application-Based Covert Communication Channels

- 来源：[SP 2022](https://doi.org/10.1109/sp46214.2022.9833752)。
- 判定依据：ABCC 形式化应用协议承载的隐蔽通信与抗被动检测，非非预期实现泄漏；保留通信理论背景。
- 阅读来源：https://xplorestaging.ieee.org/document/9833752/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Verified NTT Multiplications for NISTPQC KEM Lattice Finalists: Kyber, SABER, and NTRU

- 来源：[TCHES 2022](https://doi.org/10.46586/tches.v2022.i4.718-750)。
- 判定依据：CryptoLine 验证六种 NTT 乘法的代数正确性与数值范围；摘要及正文首页未给出恒时/非干扰结论，保留为验证背景。
- 阅读来源：https://tches.iacr.org/index.php/TCHES/article/download/9838/9341。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## WIGHT: Wired Ghost Touch Attack on Capacitive Touchscreens

- 来源：[SP 2022](https://doi.org/10.1109/sp46214.2022.9833740)。
- 判定依据：WIGHT 经充电线注入触摸事件，为主动信号注入而非敏感信息侧信道读取。
- 阅读来源：https://xplorestaging.ieee.org/document/9833740/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## When Bad News Become Good News: Towards Usable Instances of Learning with Physical Errors

- 来源：[TCHES 2022](https://doi.org/10.46586/tches.v2022.i4.1-24)。
- 判定依据：将非精确计算产生错误从 LPPN 推广为 LWPE，分析数据相关误差与 FPGA 设计修正；保留物理采样和数学安全背景，不把输出误差依赖自动称为测量侧信道。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## vSGX: Virtualizing SGX Enclaves on AMD SEV

- 来源：[SP 2022](https://doi.org/10.1109/sp46214.2022.9833694)。
- 判定依据：vSGX 研究跨硬件虚拟化与证明链；摘要的 comparable security 未具体包括侧信道。
- 阅读来源：https://xplorestaging.ieee.org/document/9833694/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## BASALISC: Programmable Hardware Accelerator for BGV Fully Homomorphic Encryption

- 来源：[TCHES 2023](https://doi.org/10.46586/tches.v2023.i4.32-57)。
- 判定依据：BASALISC 的 BGV 架构、仿真及功能单元验证聚焦性能和可实现性；面积/功耗指标不是泄漏安全验证。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Blue's Clues: Practical Discovery of Non-Discoverable Bluetooth Devices

- 来源：[SP 2023](https://www.ieee-security.org/TC/SP2023/program-papers.html)。
- 判定依据：摘要直接发现非可发现蓝牙设备并取得 MAC/标识符；观察是否依赖额外侧信道仍待正文核对，先保留协议隐私背景。
- 阅读来源：https://xplorestaging.ieee.org/document/10179358/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## CSI:Rowhammer - Cryptographic Security and Integrity against Rowhammer

- 来源：[SP 2023](https://www.ieee-security.org/TC/SP2023/program-papers.html)。
- 判定依据：摘要为 Rowhammer 错误检测/纠正，在 gem5 评估；不等于实测侧信道防护。
- 阅读来源：https://xplorestaging.ieee.org/document/10179390/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Control Flow and Pointer Integrity Enforcement in a Secure Tagged Architecture

- 来源：[SP 2023](https://www.ieee-security.org/TC/SP2023/program-papers.html)。
- 判定依据：摘要保护控制流与指针完整性，未说明时间或物理观察非干扰。
- 阅读来源：https://xplorestaging.ieee.org/document/10179416/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## EC: Embedded Systems Compartmentalization via Intra-Kernel Isolation

- 来源：[SP 2023](https://www.ieee-security.org/TC/SP2023/program-papers.html)。
- 判定依据：摘要为嵌入式权限与内存隔离；未给出观察通道保证。
- 阅读来源：https://xplorestaging.ieee.org/document/10179285/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Efficient Algorithms for Large Prime Characteristic Fields and Their Application to Bilinear Pairings

- 来源：[TCHES 2023](https://doi.org/10.46586/tches.v2023.i3.445-472)。
- 判定依据：优化大素数域的乘积和及双线性对计算，包含同源协议应用背景；摘要未报告侧信道贡献。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Enabling FrodoKEM on Embedded Devices

- 来源：[TCHES 2023](https://doi.org/10.46586/tches.v2023.i3.74-96)。
- 判定依据：降低 FrodoKEM 的栈消耗并分析时间与内存折衷，部分结果需微调规范；摘要未报告侧信道保护，低内存不等于泄漏安全。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## FIDO2, CTAP 2.1, and WebAuthn 2: Provable Security and Post-Quantum Instantiation

- 来源：[SP 2023](https://www.ieee-security.org/TC/SP2023/program-papers.html)。
- 判定依据：摘要证明 FIDO2 协议及条件性后量子实例化，未研究其实现泄漏。
- 阅读来源：https://xplorestaging.ieee.org/document/10179454/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Fast Practical Lattice Reduction Through Iterated Compression

- 来源：[CRYPTO 2023](https://doi.org/10.1007/978-3-031-38548-3_1)。
- 判定依据：精度管理与递归格基约简方法，提供 LLL 类保证及实现基准；是 GoFetch 的求解背景，不是独立侧信道攻击。ePrint 为 CRYPTO 2023 major revision，不能假定全文完全相同。
- 阅读来源：https://eprint.iacr.org/2023/237。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Fiddling the Twiddle Constants - Fault Injection Analysis of the Number Theoretic Transform

- 来源：[TCHES 2023](https://doi.org/10.46586/tches.v2023.i2.447-481)。
- 判定依据：通过 NTT twiddle 相关故障降低输出熵，覆盖 Kyber/Dilithium 多种恢复或伪造目标并报告 EM 注入；属于主动故障分析，不合并为功耗或电磁被动测量攻击。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Formally verifying Kyber: Episode IV: Implementation correctness

- 来源：[TCHES 2023](https://doi.org/10.46586/tches.v2023.i3.164-193)。
- 判定依据：正文 PDF pp.4、26 明确将恒时/Spectre 防护指向另一工作及后续结合；本篇的功能正确性结论不能升级成该实现已有端到端侧信道证明。
- 阅读来源：https://tches.iacr.org/index.php/TCHES/article/download/10960/10267。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## From MLWE to RLWE: A Differential Fault Attack on Randomized & Deterministic Dilithium

- 来源：[TCHES 2023](https://doi.org/10.46586/tches.v2023.i4.262-286)。
- 判定依据：指令跳过使 Dilithium 的 MLWE 结构退化，使用同一故障签名给出的 hints 与格约简恢复并提出防护；保留故障与后处理背景，不将 hints 获取记为功耗测量。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## How IoT Re-using Threatens Your Sensitive Data: Exploring the User-Data Disposal in Used IoT Devices

- 来源：[SP 2023](https://www.ieee-security.org/TC/SP2023/program-papers.html)。
- 判定依据：摘要研究数据删除、存储残留与直接读取，非此处的非侵入计算活动观察；保留生命周期背景。
- 阅读来源：https://xplorestaging.ieee.org/document/10179294/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## IPvSeeYou: Exploiting Leaked Identifiers in IPv6 for Street-Level Geolocation

- 来源：[SP 2023](https://www.ieee-security.org/TC/SP2023/program-papers.html)。
- 判定依据：摘要从 IPv6 中直接暴露的 MAC 与地理数据库关联定位；先作标识符隐私背景，未确认实现侧信道。
- 阅读来源：https://xplorestaging.ieee.org/document/10179376/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Jolt: Recovering TLS Signing Keys via Rowhammer Faults

- 来源：[SP 2023](https://www.ieee-security.org/TC/SP2023/program-papers.html)。
- 判定依据：Jolt 的核心为故障签名与 Rowhammer 注入；侧信道只是动机背景，当前按纯故障相邻研究保留。
- 阅读来源：https://xplorestaging.ieee.org/document/10179450/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Leaking Arbitrarily Many Secrets: Any-out-of-Many Proofs and Applications to RingCT Protocols

- 来源：[SP 2023](https://www.ieee-security.org/TC/SP2023/program-papers.html)。
- 判定依据：摘要是零知识证明与隐藏秘密数量的协议设计，不是物理或实现通道的密钥泄漏。
- 阅读来源：https://xplorestaging.ieee.org/document/10179292/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Loop Aborts Strike Back: Defeating Fault Countermeasures in Lattice Signatures with ILP

- 来源：[TCHES 2023](https://doi.org/10.46586/tches.v2023.i4.367-392)。
- 判定依据：用 ILP 处理 loop-abort 造成的噪声线性系统，突破打乱等防护并在 Cortex-M4 验证；恢复对象含等价签名密钥，所报少量签名是故障签名而非被动迹线。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Low-Cost Privilege Separation with Compile Time Compartmentalization for Embedded Systems

- 来源：[SP 2023](https://www.ieee-security.org/TC/SP2023/program-papers.html)。
- 判定依据：摘要以编译期约束实现权限分隔，未给出侧信道安全性质。
- 阅读来源：https://xplorestaging.ieee.org/document/10179388/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## OWL: Compositional Verification of Security Protocols via an Information-Flow Type System

- 来源：[SP 2023](https://www.ieee-security.org/TC/SP2023/program-papers.html)。
- 判定依据：摘要为协议组合证明和信息流类型，未把执行时间/微架构观察纳入已说明模型。
- 阅读来源：https://xplorestaging.ieee.org/document/10179477/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Oil and Vinegar: Modern Parameters and Implementations

- 来源：[TCHES 2023](https://doi.org/10.46586/tches.v2023.i3.321-365)。
- 判定依据：重新选择 Oil and Vinegar 参数并实现 AVX2、Cortex-M4、FPGA 与 Neon；摘要的安全讨论是数学密码分析及参数，未给出泄漏或恒时贡献。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## On Protecting SPHINCS+ Against Fault Attacks

- 来源：[TCHES 2023](https://doi.org/10.46586/tches.v2023.i2.80-114)。
- 判定依据：分析 SPHINCS+ 的随机签名、错误签名组合与缓存防护，建议冗余检查；保留故障安全背景，未由摘要推定被动泄漏。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Private Collaborative Data Cleaning via Non-Equi PSI

- 来源：[SP 2023](https://www.ieee-security.org/TC/SP2023/program-papers.html)。
- 判定依据：摘要允许差分隐私的集合交大小泄漏以换取性能；这是协议泄漏模型，不是实现通道评估。
- 阅读来源：https://xplorestaging.ieee.org/document/10179337/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## REGA: Scalable Rowhammer Mitigation with Refresh-Generating Activations

- 来源：[SP 2023](https://www.ieee-security.org/TC/SP2023/program-papers.html)。
- 判定依据：摘要针对 Rowhammer 刷新缓解及开销，不是侧信道观察防护。
- 阅读来源：https://xplorestaging.ieee.org/document/10179327/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Red Team vs. Blue Team: A Real-World Hardware Trojan Detection Case Study Across Four Modern CMOS Technology Generations

- 来源：[SP 2023](https://www.ieee-security.org/TC/SP2023/program-papers.html)。
- 判定依据：摘要通过 GDSII 与 SEM 图像比对检测布局改动，非功耗/EM 木马侧信道评估。
- 阅读来源：https://xplorestaging.ieee.org/document/10179341/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## SPHINCS+C: Compressing SPHINCS+ With (Almost) No Cost

- 来源：[SP 2023](https://www.ieee-security.org/TC/SP2023/program-papers.html)。
- 判定依据：摘要优化 SPHINCS+ 签名大小与速度；可变搜索次数不自动证明秘密泄漏，需另查实现模型。
- 阅读来源：https://xplorestaging.ieee.org/document/10179381/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## SecureCells: A Secure Compartmentalized Architecture

- 来源：[SP 2023](https://www.ieee-security.org/TC/SP2023/program-papers.html)。
- 判定依据：摘要为 VMA 权限、上下文隔离和低成本跨域调用，未给出侧信道覆盖。
- 阅读来源：https://xplorestaging.ieee.org/document/10179472/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## ShadowNet: A Secure and Efficient On-device Model Inference System for Convolutional Neural Networks

- 来源：[SP 2023](https://www.ieee-security.org/TC/SP2023/program-papers.html)。
- 判定依据：摘要通过 TEE 和权重变换保护外包模型，未核查时间、功耗或访问模式边界。
- 阅读来源：https://xplorestaging.ieee.org/document/10179382/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## SoK: Cryptographic Neural-Network Computation

- 来源：[SP 2023](https://www.ieee-security.org/TC/SP2023/program-papers.html)。
- 判定依据：摘要综述基于密码学的神经网络计算，属于方法背景而非实现侧信道研究。
- 阅读来源：https://xplorestaging.ieee.org/document/10179483/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Sound Verification of Security Protocols: From Design to Interoperable Implementations

- 来源：[SP 2023](https://www.ieee-security.org/TC/SP2023/program-papers.html)。
- 判定依据：摘要保证代码继承 Tamarin 的协议 trace 性质；这里的 trace 不等于测量波形或时间泄漏。
- 阅读来源：https://xplorestaging.ieee.org/document/10179325/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Vectorized and Parallel Computation of Large Smooth-Degree Isogenies using Precedence-Constrained Scheduling

- 来源：[TCHES 2023](https://doi.org/10.46586/tches.v2023.i3.246-269)。
- 判定依据：大光滑度同源计算的先后约束调度、多核同步和 AVX-512 性能；同步在此是并行计算手段，摘要没有同步侧信道主张。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Volttack: Control IoT Devices by Manipulating Power Supply Voltage

- 来源：[SP 2023](https://www.ieee-security.org/TC/SP2023/program-papers.html)。
- 判定依据：摘要操纵供电信号造成传感/执行错误，为主动注入背景而非秘密观察攻击。
- 阅读来源：https://xplorestaging.ieee.org/document/10179340/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## WaVe: A Verifiably Secure WebAssembly Sandboxing Runtime

- 来源：[SP 2023](https://www.ieee-security.org/TC/SP2023/program-papers.html)。
- 判定依据：摘要证明 Wasm 内存安全及 OS 资源访问隔离，未承诺时序/微架构非干扰。
- 阅读来源：https://xplorestaging.ieee.org/document/10179357/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## WebSpec: Towards Machine-Checked Analysis of Browser Security Mechanisms

- 来源：[SP 2023](https://www.ieee-security.org/TC/SP2023/program-papers.html)。
- 判定依据：摘要为浏览器逻辑安全机制的模型检查，不等于侧信道自动发现或功耗模型。
- 阅读来源：https://xplorestaging.ieee.org/document/10179465/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## cuZK: Accelerating Zero-Knowledge Proof with A Faster Parallel Multi-Scalar Multiplication Algorithm on GPUs

- 来源：[TCHES 2023](https://doi.org/10.46586/tches.v2023.i3.194-220)。
- 判定依据：cuZK 加速 GPU 上 zkSNARK 的矩阵乘法、NTT、MSM 与传输；零知识协议性质不自动覆盖证明过程的实现泄漏。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## uSWITCH: Fast Kernel Context Isolation with Implicit Context Switches

- 来源：[SP 2023](https://www.ieee-security.org/TC/SP2023/program-papers.html)。
- 判定依据：摘要为内核资源和内存隔离性能，不等于防住共享微架构观察。
- 阅读来源：https://xplorestaging.ieee.org/document/10179284/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## A Highly-efficient Lattice-based Post-Quantum Cryptography Processor for IoT Applications

- 来源：[TCHES 2024](https://doi.org/10.46586/tches.v2024.i2.130-153)。
- 判定依据：以 SIMD、双发射访存及资源复用改善 Kyber/Dilithium 处理器 PPAP；平均功耗改善不证明抗功耗分析。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## A Systematic Study of Physical Sensor Attack Hardness

- 来源：[SP 2024](https://www.ieee-security.org/TC/SP2024/accepted-papers.html)。
- 判定依据：研究机器人传感器注入攻击的前提和成功难度，主要是主动完整性/安全性破坏；摘要未建立秘密经侧信道泄漏的关系。作为物理攻击前提分析方法保留。
- 阅读来源：https://xplorestaging.ieee.org/document/10646778/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## AquaSonic: Acoustic Manipulation of Underwater Data Center Operations and Resource Management

- 来源：[SP 2024](https://www.ieee-security.org/TC/SP2024/accepted-papers.html)。
- 判定依据：水下声学注入使存储、分布式系统和调度降级，摘要核心是可用性与资源操纵；未证明通过观察间接信号恢复秘密，作为物理注入背景保留。
- 阅读来源：https://xplorestaging.ieee.org/document/10646672/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Breach Extraction Attacks: Exposing and Addressing the Leakage in Second Generation Compromised Credential Checking Services

- 来源：[SP 2024](https://www.ieee-security.org/TC/SP2024/accepted-papers.html)。
- 判定依据：MIGP 的密码协议与部署允许客户端取得额外凭据信息；摘要未把新增泄漏绑定到时间、长度或共享资源侧信道。保留协议泄漏背景，待全文澄清实现部分。
- 阅读来源：https://xplorestaging.ieee.org/document/10646859/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## CASA: A Compact and Scalable Accelerator for Approximate Homomorphic Encryption

- 来源：[TCHES 2024](https://doi.org/10.46586/tches.v2024.i2.451-480)。
- 判定依据：CASA 优化 CKKS 算法、模块及 FPGA 架构；功耗延迟积与隐私协议保证不能代替泄漏证据。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Carry Your Fault: A Fault Propagation Attack on Side-Channel Protected LWE-based KEM

- 来源：[TCHES 2024](https://doi.org/10.46586/tches.v2024.i2.844-869)。
- 判定依据：攻击掩码为实现便利而引入的 A2B 进位传播，含 Kyber 模拟和 STM32 EM 故障验证；保留掩码与故障交互，任意阶原理不等于所有阶数已实测。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## ConvKyber: Unleashing the Power of AI Accelerators for Faster Kyber with Novel Iteration-based Approaches

- 来源：[TCHES 2024](https://doi.org/10.46586/tches.v2024.i2.25-63)。
- 判定依据：ConvKyber 重排 NTT 矩阵计算并利用 Tensor Core 资源以提升吞吐率；摘要未作泄漏评估。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Correction Fault Attacks on Randomized CRYSTALS-Dilithium

- 来源：[TCHES 2024](https://doi.org/10.46586/tches.v2024.i3.174-199)。
- 判定依据：通过纠正随机/hedged Dilithium 的故障签名提取约束，包括公共矩阵被故障的场景，并报告模拟及 MCU 时钟毛刺；物理故障敏感性不能由被动泄漏敏感性替代。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Efficient ASIC Architecture for Low Latency Classic McEliece Decoding

- 来源：[TCHES 2024](https://doi.org/10.46586/tches.v2024.i2.403-425)。
- 判定依据：Classic McEliece 译码 ASIC 的逆元消除和阵列设计降低面积/延迟；制造芯片和性能测量本身不构成侧信道评估。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Efficient Actively Secure DPF and RAM-based 2PC with One-Bit Leakage

- 来源：[SP 2024](https://www.ieee-security.org/TC/SP2024/accepted-papers.html)。
- 判定依据：one-bit leakage 是主动安全 2PC 协议的形式化放宽，不是论文已验证一个物理比特侧信道。作为密码协议泄漏模型背景保留。
- 阅读来源：https://xplorestaging.ieee.org/document/10646747/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Elastic MSM: A Fast, Elastic and Modular Preprocessing Technique for Multi-Scalar Multiplication Algorithm on GPUs

- 来源：[TCHES 2024](https://doi.org/10.46586/tches.v2024.i4.258-284)。
- 判定依据：Elastic MSM 研究 GPU 预处理的时间与存储折衷，摘要没有实现侧信道贡献。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Enabling PERK and other MPC-in-the-Head Signatures on Resource-Constrained Devices

- 来源：[TCHES 2024](https://doi.org/10.46586/tches.v2024.i4.84-109)。
- 判定依据：通过重组数据结构减少 PERK/MPCitH 内存占用并实现 Cortex-M4 版本；省内存不等于抗泄漏。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Fast and Clean: Auditable high-performance assembly via constraint solving

- 来源：[TCHES 2024](https://doi.org/10.46586/tches.v2024.i1.87-132)。
- 判定依据：摘要聚焦汇编调度、寄存器分配与性能优化；未说明具体泄漏评估或侧信道安全保证。保留为 PQC 实现工具背景。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-12；没有独立第二审读或本地复现。

## Faster Bootstrapping via Modulus Raising and Composite NTT

- 来源：[TCHES 2024](https://doi.org/10.46586/tches.v2024.i1.563-591)。
- 判定依据：通过复合 NTT、模数提升及 CRT 打包提高 FHEW 自举效率；误差增长与计算噪声不是测量泄漏。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Faster NTRU-based Bootstrapping in less than 4 ms

- 来源：[TCHES 2024](https://doi.org/10.46586/tches.v2024.i3.418-451)。
- 判定依据：以近似分解、密钥展开及窗口策略加速 NTRU 自举，摘要聚焦 CPU/FPGA 性能。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Guessing on Dominant Paths: Understanding the Limitation of Wireless Authentication Using Channel State Information

- 来源：[SP 2024](https://www.ieee-security.org/TC/SP2024/accepted-papers.html)。
- 判定依据：CSI 猜测和预编码用于伪装合法无线身份，属于主动认证绕过；摘要未说明受保护计算经额外观察泄漏，作为物理层认证背景保留。
- 阅读来源：https://xplorestaging.ieee.org/document/10646746/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## High-Performance Hardware Implementation of MPCitH and Picnic3

- 来源：[TCHES 2024](https://doi.org/10.46586/tches.v2024.i2.190-214)。
- 判定依据：MPCitH/Picnic3 硬件流水线和多方执行优化；MPCitH 中的参与方数量不等于物理掩码安全阶数。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Holepunch: Fast, Secure File Deletion with Crash Consistency

- 来源：[SP 2024](https://www.ieee-security.org/TC/SP2024/accepted-papers.html)。
- 判定依据：Holepunch 用可穿孔 PRF 和 TPM 实现密码擦除与崩溃一致性；摘要没有审查清理期间功耗或其他侧信道。最终存储不可恢复与清理轨迹安全须区分。
- 阅读来源：https://xplorestaging.ieee.org/document/10646784/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## INTFAIL: Using Spurious #VC Interrupts to Break AMD SEV-SNP

- 来源：[SP 2024](https://www.ieee-security.org/TC/SP2024/accepted-papers.html)。
- 判定依据：出版题名为 WeSee；恶意 hypervisor 注入 #VC 诱导寄存器/内存复制和任意行为，属于异常处理与完整性攻击。直接拷出 kTLS key 不自动构成侧信道推断；作为 TEE 威胁模型背景保留。
- 阅读来源：https://xplorestaging.ieee.org/document/10646722/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Impeccable Keccak: Towards Fault Resilient SPHINCS+ Implementations

- 来源：[TCHES 2024](https://doi.org/10.46586/tches.v2024.i2.154-189)。
- 判定依据：为 SPHINCS+ 的 Keccak 提出 impeccable 电路与主动安全分析，给出指定位翻转模型的检测保证；这不是功耗掩码安全证明，也不是任意故障模型保证。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## MetaFly: Wireless Backhaul Interception via Aerial Wavefront Manipulation

- 来源：[SP 2024](https://www.ieee-security.org/TC/SP2024/accepted-papers.html)。
- 判定依据：MetaFly 改变定向无线链路的波前以截获其通信信号；摘要是主通信信道窃听与物理操纵，不是密码实现的非预期泄漏。作为测量/传播背景保留。
- 阅读来源：https://xplorestaging.ieee.org/document/10646843/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## ModHE: Modular Homomorphic Encryption Using Module Lattices: Potentials and Limitations

- 来源：[TCHES 2024](https://doi.org/10.46586/tches.v2024.i1.527-562)。
- 判定依据：将 CKKS 类方案迁移到 Module-LWE 以改善硬件结构和参数灵活性；摘要讨论的是计算复杂度折衷。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## More Haste, Less Speed: Cache Related Security Threats in Continuous Integration Services

- 来源：[SP 2024](https://www.ieee-security.org/TC/SP2024/accepted-papers.html)。
- 判定依据：CI cache 指依赖包缓存对象的隔离、投毒和直接敏感文件暴露；不是 CPU cache 时序侧信道。作为跨信任域缓存设计背景保留。
- 阅读来源：https://xplorestaging.ieee.org/document/10646699/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Nibbling MAYO: Optimized Implementations for AVX2 and Cortex-M4

- 来源：[TCHES 2024](https://doi.org/10.46586/tches.v2024.i2.252-275)。
- 判定依据：MAYO 由位切片转为 nibble 切片并优化 M4R/向量乘法；摘要未说明秘密相关查表或恒时边界，需正文再筛。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## No Privacy Left Outside: On the (In-)Security of TEE-Shielded DNN Partition for On-Device ML

- 来源：[SP 2024](https://www.ieee-security.org/TC/SP2024/accepted-papers.html)。
- 判定依据：TSDP 的模型窃取和成员推断利用分区后可见的权重/接口；摘要未将攻击归因于时序、功耗或缓存观察，作为 TEE 与 ML 隐私背景保留。
- 阅读来源：https://xplorestaging.ieee.org/document/10646815/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Optimized Hardware-Software Co-Design for Kyber and Dilithium on RISC-V SoC FPGA

- 来源：[TCHES 2024](https://doi.org/10.46586/tches.v2024.i3.99-135)。
- 判定依据：RISC-V SoC 上以多核、硬件乘法及汇编哈希加速 Kyber/Dilithium，摘要未评价泄漏。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Pandora: Principled Symbolic Validation of Intel SGX Enclave Runtimes

- 来源：[SP 2024](https://www.ieee-security.org/TC/SP2024/accepted-papers.html)。
- 判定依据：Pandora 对 SGX shielding runtime 的污点、符号内存及漏洞位置做验证；摘要未完整说明四类插件的侧信道性质，暂作实现验证背景，保留正文范围复核。
- 阅读来源：https://xplorestaging.ieee.org/document/10646841/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Revisiting Keccak and Dilithium Implementations on ARMv7-M

- 来源：[TCHES 2024](https://doi.org/10.46586/tches.v2024.i2.1-24)。
- 判定依据：优化 ARMv7-M 上 Keccak 旋转、访存流水及 Dilithium 小多项式乘法；摘要聚焦性能，不把哈希占比下降解释为泄漏降低。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## SDitH in Hardware

- 来源：[TCHES 2024](https://doi.org/10.46586/tches.v2024.i2.215-251)。
- 判定依据：SDitH 硬件中的 secret-share splitting 是协议实现内容；摘要未把它验证为物理侧信道掩码。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Secure Ranging with IEEE 802.15.4z HRP UWB

- 来源：[SP 2024](https://www.ieee-security.org/TC/SP2024/accepted-papers.html)。
- 判定依据：对 IEEE 802.15.4z STS 接收器做安全测距证明和数值实验，主要保证主动距离操纵下的距离上界；不能等同秘密侧信道或实际芯片泄漏测量。
- 阅读来源：https://xplorestaging.ieee.org/document/10646848/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## SoK: Efficient Design and Implementation of Polynomial Hash Functions over Prime Fields

- 来源：[SP 2024](https://www.ieee-security.org/TC/SP2024/accepted-papers.html)。
- 判定依据：素域多项式哈希设计的安全/性能综述与实现基准；摘要没有提出明确的实现侧信道目标，作为算术设计背景保留，正文恒时相关部分待核。
- 阅读来源：https://xplorestaging.ieee.org/document/10646805/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Surveilling the Masses with Wi-Fi-Based Positioning Systems

- 来源：[SP 2024](https://www.ieee-security.org/TC/SP2024/accepted-papers.html)。
- 判定依据：通过 WPS 服务直接枚举 BSSID 地理位置并做纵向关联，属于位置数据库/API 隐私暴露；摘要没有额外物理或共享资源侧信道，作为位置隐私背景保留。
- 阅读来源：https://xplorestaging.ieee.org/document/10646810/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## The Dark Side of Scale: Insecurity of Direct-to-Cell Satellite Mega-Constellations

- 来源：[SP 2024](https://www.ieee-security.org/TC/SP2024/accepted-papers.html)。
- 判定依据：SatOver 利用信令和伪基站阻断 direct-to-cell 接入，主要是协议可用性与接入劫持；不可与卫星位置元数据侧信道合并。
- 阅读来源：https://xplorestaging.ieee.org/document/10646850/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## A High-performance NTT/MSM Accelerator for Zero-knowledge Proof Using Load-balanced Fully-pipelined Montgomery Multiplier

- 来源：[TCHES 2025](https://doi.org/10.46586/tches.v2025.i1.275-313)。
- 判定依据：通过统一 NTT/MSM 数据通路及流水模乘加速 ZKP；资源共享与性能不直接支持隔离或泄漏主张。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## A New Trick for Polynomial Multiplication: A verified CRT polymul utilizing a monomial factor

- 来源：[TCHES 2025](https://doi.org/10.46586/tches.v2025.i4.795-816)。
- 判定依据：CryptoLine 验证 CRT 多项式乘法的范围和编译结果等价性；这些是正确性属性，不是泄漏非干扰证明。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Accelerating NTT with RISC-V Vector Extension for Fully Homomorphic Encryption

- 来源：[TCHES 2025](https://doi.org/10.46586/tches.v2025.i4.711-736)。
- 判定依据：用 RISC-V 向量扩展优化 OpenFHE 的 NTT/INTT 与应用性能，摘要未涉及泄漏安全。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Algebraic Linear Analysis for Number Theoretic Transform in Lattice-Based Cryptography

- 来源：[TCHES 2025](https://doi.org/10.46586/tches.v2025.i3.668-692)。
- 判定依据：摘要贡献是 CryptoLine/islpy 对 NTT 汇编范围与算术正确性的验证，未说明侧信道非干扰或泄漏评估；保留为 PQC 实现验证背景。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## FINAL bootstrap acceleration on FPGA using DSP-free constant-multiplier NTTs

- 来源：[TCHES 2025](https://doi.org/10.46586/tches.v2025.i3.293-316)。
- 判定依据：FINAL 自举的 DSP-free constant multiplier 指常数乘法硬件；不能仅凭 constant 一词判为恒时防护。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## FalconSign: An Efficient and High-Throughput Hardware Architecture for Falcon Signature Generation

- 来源：[TCHES 2025](https://doi.org/10.46586/tches.v2025.i1.203-226)。
- 判定依据：FalconSign 优化 Fast-Fourier Sampling、随机数和浮点硬件调度，摘要未说明掩码或泄漏验证。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Faster amortized bootstrapping using the incomplete NTT for free

- 来源：[TCHES 2025](https://doi.org/10.46586/tches.v2025.i4.520-543)。
- 判定依据：以不完全 NTT 改善摊销自举时间和解密失败率，DFR 指密码计算误差而非测量噪声。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Generation of Fast Finite Field Arithmetic forCortex-M4 with ECDH and SQIsign Applications

- 来源：[TCHES 2025](https://doi.org/10.46586/tches.v2025.i4.588-620)。
- 判定依据：m4-modarith 自动生成快速有限域算术并证明约减正确性；功能证明不能自动推得恒时保证。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## GuardAIn: Protecting Emerging Generative AI Workloads on Heterogeneous NPU

- 来源：[SP 2025](https://www.ieee-security.org/TC/SP2025/accepted-papers.html#collapse-114)。
- 判定依据：GuardAIn 讨论 NPU 的认证加密、隔离与任务证明；摘要未建立功耗、时间或微架构侧信道性质，作为机密计算背景保留。
- 阅读来源：https://clement-thorens.ch/pdfs/guardain.pdf。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Hey, Your Secrets Leaked! Detecting and Characterizing Secret Leakage in the Wild

- 来源：[SP 2025](https://www.ieee-security.org/TC/SP2025/accepted-papers.html#collapse-169)。
- 判定依据：Keysentinel 检测代码与配置中的 API key、密码等直接暴露；此处 secret leakage 不是物理或共享资源侧信道。
- 阅读来源：https://xplorestaging.ieee.org/document/11023280/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Improving MPCitH with Preprocessing: Mask Is All You Need

- 来源：[TCHES 2025](https://doi.org/10.46586/tches.v2025.i2.1-22)。
- 判定依据：优化 MPCitH 预处理与 Picnic3 并行计算；mask 是证明协议中的随机掩蔽，摘要未给出物理掩码或侧信道安全评估。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Is MPC Secure? Leveraging Neural Network Classifiers to Detect Data Leakage Vulnerabilities in MPC Implementations

- 来源：[SP 2025](https://www.ieee-security.org/TC/SP2025/accepted-papers.html#collapse-235)。
- 判定依据：MPCGuard 用分类器比较 MPC 实现中参与者视图的隐私泄漏，作为实现隐私测试方法背景；摘要未把泄漏归因于功耗、时间或共享硬件观测。
- 阅读来源：https://xplorestaging.ieee.org/document/11023305/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## LESS is Even More: Optimizing Digital Signatures from Code Equivalence

- 来源：[TCHES 2025](https://doi.org/10.46586/tches.v2025.i4.386-408)。
- 判定依据：优化 LESS 规范形计算及参数选择的性能和签名长度，摘要未报告实现泄漏。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Let us walk on the 3-isogeny graph: efficient, fast, and simple

- 来源：[TCHES 2025](https://doi.org/10.46586/tches.v2025.i4.644-666)。
- 判定依据：优化 3-isogeny 链、相关 KEM 与 CTIDH 密钥生成；虽应用于 CTIDH，摘要未单独给出新恒时证明或泄漏评估，先保留算术背景。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Multiplying Polynomials without Powerful Multiplication Instructions

- 来源：[TCHES 2025](https://doi.org/10.46586/tches.v2025.i1.160-202)。
- 判定依据：改进缺少强乘法指令平台的 Barrett/FFT 多项式乘法；shape-independent 指模数形状的效率/正确性，不是秘密独立性。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## New Quantum Cryptanalysis of Binary Elliptic Curves

- 来源：[TCHES 2025](https://doi.org/10.46586/tches.v2025.i2.781-804)。
- 判定依据：估算 Shor 二进制椭圆曲线攻击的量子电路资源；此处电路深度不是物理侧信道观测。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Optimized One-Dimensional SQIsign Verification on Intel and Cortex-M4

- 来源：[TCHES 2025](https://doi.org/10.46586/tches.v2025.i1.497-522)。
- 判定依据：优化一维 SQIsign 的验签与并行实现，摘要未报告秘密泄漏分析。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Optimized Software Implementation of Keccak, Kyber, and Dilithium on RV{32,64}IM{B}{V}

- 来源：[TCHES 2025](https://doi.org/10.46586/tches.v2025.i1.632-655)。
- 判定依据：在 RISC-V 多种 ISA 上优化 Keccak/NTT 与双发射调度，摘要没有非干扰或物理泄漏结论。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## PORTAL: Fast and Secure Device Access with Arm CCA for Modern Arm Mobile System-on-Chips (SoCs)

- 来源：[SP 2025](https://www.ieee-security.org/TC/SP2025/accepted-papers.html#collapse-48)。
- 判定依据：PORTAL 以 Arm CCA 访问隔离实现设备 I/O 的明文共享内存，摘要的保密与性能主张不能自动转为物理侧信道保护。
- 阅读来源：https://sang.fan/assets/papers/portal_sp25.pdf。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Proving Faster Implementations Faster: Combining Deductive and Circuit-Based Reasoning in EasyCrypt

- 来源：[SP 2025](https://www.ieee-security.org/TC/SP2025/accepted-papers.html#collapse-166)。
- 判定依据：混合推演与电路等价检查用于 ML-KEM 优化代码的功能正确性。所读正文另介绍 Jasmin 对恒时/推测恒时属性的保持能力；功能等价证明本身不等于这些属性或模拟泄漏的证明。按功能验证与工具链背景保留。出版题名为 Faster Verification of Faster Implementations，录用目录的 Proving Faster Implementations Faster 是同一论文的题名别名。
- 阅读来源：https://xplorestaging.ieee.org/document/11023411/ ; https://cryptosith.org/papers/mapreduce-20250907.pdf。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Quantum security analysis of Module-LWE PQC based on practical cost estimates

- 来源：[TCHES 2025](https://doi.org/10.46586/tches.v2025.i4.437-462)。
- 判定依据：以量子筛电路和纠错成本估计 Module-LWE 安全强度，属于计算攻击成本背景。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## REED: Chiplet-based Accelerator for Fully Homomorphic Encryption

- 来源：[TCHES 2025](https://doi.org/10.46586/tches.v2025.i2.163-208)。
- 判定依据：REED 以 chiplet、通信和存储设计加速 FHE；其布局前功耗模拟是能效评估，不是秘密可辨识性验证。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Resolution Without Dissent: In-Path Per-Query Sanitization to Defeat Surreptitious Communication Over DNS

- 来源：[SP 2025](https://www.ieee-security.org/TC/SP2025/accepted-papers.html#collapse-75)。
- 判定依据：TunTight 识别并阻断 DNS 域名中承载的隧道通信，属于显式数据外传及检测背景；不能仅凭 covert/exfiltration 用词纳入非预期实现泄漏。
- 阅读来源：https://xplorestaging.ieee.org/document/11023297/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Rudraksh: A compact and lightweight post-quantum key-encapsulation mechanism

- 来源：[TCHES 2025](https://doi.org/10.46586/tches.v2025.i2.647-680)。
- 判定依据：Rudraksh 联合选择 LWE 参数、ASCON 与 FPGA 实现以降低面积；摘要中的 CCA/Core-SVP 安全是密码学口径，不构成物理侧信道保护。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Security Attacks Abusing Pulse-level Quantum Circuits

- 来源：[SP 2025](https://www.ieee-security.org/TC/SP2025/accepted-papers.html#collapse-6)。
- 判定依据：研究量子 SDK 自定义门的脉冲语义与逻辑电路语义不一致导致的恶意执行，属于量子软件完整性；不是后量子密码实现或被动波形侧信道。
- 阅读来源：https://caslab.io/publications/xu2025security.pdf。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Sharing the Mask: TFHE Bootstrapping on Packed Messages

- 来源：[TCHES 2025](https://doi.org/10.46586/tches.v2025.i4.925-971)。
- 判定依据：Sharing the Mask 的 mask 是多个 FHE 密文共享的随机掩码部分；不能与抗功耗的秘密分享掩码混为一谈。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Sieving with Streaming Memory Access

- 来源：[TCHES 2025](https://doi.org/10.46586/tches.v2025.i2.362-384)。
- 判定依据：研究格筛的访存成本和 SVP 攻击资源估计，属于数学安全与后处理背景；不是观测受害实现的缓存攻击。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## SoK: Decoding the Enigma of Encrypted Network Traffic Classifiers

- 来源：[SP 2025](https://www.ieee-security.org/TC/SP2025/accepted-papers.html#collapse-219)。
- 判定依据：SoK 审查加密流量分类中的数据集、特征和评价假设，作为方法学背景；未据此推断所有网站指纹论文都使用同样有问题的数据。
- 阅读来源：https://arxiv.org/abs/2503.20093。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## TrafficFormer: An Efficient Pre-trained Model for Traffic Data

- 来源：[SP 2025](https://www.ieee-security.org/TC/SP2025/accepted-papers.html#collapse-27)。
- 判定依据：TrafficFormer 的预训练、数据增强与协议理解是一般流量学习方法；摘要没有给出具体敏感目标与侧信道观察关系，保留为方法背景。
- 阅读来源：https://liuzhuotao.github.io/publications/trafficformer/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## VeloFHE: GPU Acceleration for FHEW and TFHE Bootstrapping

- 来源：[TCHES 2025](https://doi.org/10.46586/tches.v2025.i3.81-114)。
- 判定依据：VeloFHE 通过 GPU NTT、批处理与异步执行优化 FHEW/TFHE 自举，摘要未研究侧信道。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## A High-Performance and Reconfigurable Hardware Architecture for FrodoKEM

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i3.171-197)。
- 判定依据：FrodoKEM 全硬件采用分块矩阵和共享 BRAM 优化吞吐率；摘要未给出共享残留或物理泄漏分析。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## A Unified RISC-V Vector Framework for Large-Scale NTT in FHE and ZKP

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i4.970-997)。
- 判定依据：RISC-V 向量框架适配 FHE/ZKP 大规模 NTT 并在 gem5 上评价性能，摘要未报告泄漏评估。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## AVX2 Implementation of QR-UOV for Modern x86 Processors

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i2.325-346)。
- 判定依据：QR-UOV 在小奇素数扩域上使用乘法器和 SIMD 提速，摘要未给出时序或功耗安全分析。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Accelerating FrodoKEM in Hardware

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i3.881-907)。
- 判定依据：FrodoKEM 的可配置 FPGA/ASIC 实现比较吞吐率和面积能效，摘要未论证物理安全。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Accelerating HQC with Additive FFT

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i2.520-544)。
- 判定依据：HQC 通过 additive FFT 及缓存密钥变换减少冗余计算；缓存是实现策略，摘要未建立缓存侧信道。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Additive FFTs for HQC on ARM Cortex-M4, Revisited

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i3.377-401)。
- 判定依据：HQC 结合 FAFFT/CRT 及 EEA 译码提高性能；规则数据流不自动推出全部操作恒时。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## An Efficient Variant of F4 Algorithm for Solving MQ Problem

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i3.1284-1309)。
- 判定依据：改进 F4 的 S-polynomial 选择与 MQ 求解性能，属于代数密码分析背景。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## BOLT-FHE: An Efficient Unified Framework for GPU-based TFHE Bootstrapping via On-Chip Local Tiling Strategies

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i3.198-223)。
- 判定依据：BOLT-FHE 通过块内执行和融合内核优化 GPU 自举；固定执行模板不是自动成立的侧信道证明。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Breaking the Myth of MPCitH Inefficiency: Optimizing MQOM for Embedded Platforms

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i3.279-305)。
- 判定依据：MQOM 在微控制器上优化树、流式处理及时间空间折衷，摘要未报告物理掩码或泄漏评估。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## CAPSS: A Framework for SNARK-Friendly Post-Quantum Signatures

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i4.731-758)。
- 判定依据：CAPSS 构造 SNARK 友好的后量子签名，比较证明约束及签名长度；摘要未研究实现侧信道。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Completing the Chain: Verified Implementations of Hash-Based Signatures and Their Security

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i3.958-981)。
- 判定依据：摘要连接 XMSS/XMSSMT 功能实现、规范与密码学安全证明，未提出侧信道安全保证；保留为验证工具与哈希签名背景。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Correction Fault Attack on CROSS under Unknown Bit Flips

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i2.192-217)。
- 判定依据：对 CROSS 公共校验矩阵的未知位置/值翻转进行纠正故障攻击，含电压注入和 ECC 条件分析；类 Rowhammer 的故障模型不代表已演示 Rowhammer。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## DRR-NTT: Efficient NTT Accelerator in Lattice-Based Cryptography By Dimensionality Reduction in RRAM

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i2.808-833)。
- 判定依据：RRAM NTT 研究阵列干扰和量化误差的计算精度；使用实测电阻并不等于测量秘密相关泄漏。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Efficient Polynomial Multiplication for HQC on ARM Cortex-M4

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i4.998-1021)。
- 判定依据：HQC 在 Cortex-M4 上以混合 FAFFT-CRT 和调度优化乘法，摘要未说明物理防护。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Fault Attack Countermeasures for SPHINCS+: WOTS+ with Checksum Segmentation and Subtree Root Children Caching

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i3.1-23)。
- 判定依据：分析 WOTS+ 复用的安全退化分布，提出校验和分段及子树缓存，并做 ChipWhisperer 故障评估；方案结构改动与最终 SLH-DSA 兼容性须另查。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Fault Attacks on VOLEitH Signature Schemes

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i1.225-249)。
- 判定依据：对第二轮 FAEST/SDitH 的 VOLEitH 特有组件进行 Cortex-M4 故障攻击与防护分析；单签名恢复是故障签名，不能称为单被动迹线。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Faultless Key Recovery: Iteration-Skip and Loop-Abort Fault Attacks on LESS

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i3.71-97)。
- 判定依据：LESS 的 GGM 签名压缩扩大 iteration-skip/loop-abort 故障面，作者报告数学模型与毛刺验证；Faultless 是题名表达，攻击实际仍需要故障。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Finding Bugs and Features Using Cryptographically-Informed Functional Testing

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i1.425-447)。
- 判定依据：摘要聚焦功能、内存及密码逻辑错误的黑盒测试；未报告侧信道贡献，保留为实现安全背景。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-12；没有独立第二审读或本地复现。

## HawkPU: An Efficient and Low-Latency Hardware Architecture for HAWK Signature Generation and Verification

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i3.719-743)。
- 判定依据：HawkPU 以整数、FFT/NTT 和采样相关模块实现低延迟 HAWK；不用浮点不等于无侧信道。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## High-Performance FPGA Accelerator for the Post-quantum Signature Scheme CROSS

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i3.98-121)。
- 判定依据：CROSS FPGA 并行拒绝采样与调度降低运行时间；隐藏调度开销不等于隐藏秘密信息。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## High-Throughput GPU Design and Implementation of MAYO with Matrix Computation Reordering

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i4.496-521)。
- 判定依据：MAYO 的 GPU 数据复用、矩阵重排和流并发提高吞吐率；摘要未分析共享硬件的观测泄漏。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Homomorphic Field Trace Revisited : Breaking the Cubic Noise Barrier

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i1.105-134)。
- 判定依据：Homomorphic Field Trace 中 trace 是域迹运算，noise 是密文误差；不是测量波形或物理噪声分析。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Hybrid Parallel SHA-3 and its Applications to Fiat-Shamir with Aborts Signatures

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i4.679-704)。
- 判定依据：并行 SHA-3 与跨拒绝轮次预计算用于 ML-DSA/HAETAE 提速；新随机数消费与状态历史是否泄漏仍待核查。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Improving ML-KEM and ML-DSA on OpenTitan: Efficient Multiplication Vector Instructions for OTBN

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i2.495-519)。
- 判定依据：OTBN 的向量乘法扩展及软硬件分工优化时间面积积；不能继承 OpenTitan 名称所暗示的整体物理保护。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Lightening CROSS: Memory Optimized Implementations of CROSS

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i2.630-658)。
- 判定依据：CROSS 通过树结构、即时哈希和 DSP 降低内存/运行成本，摘要未报告泄漏分析。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Lightweight PQ KEM and Hybrid MQTT Protocol for 8-bit AVR Sensor Nodes

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i2.372-408)。
- 判定依据：CTRU-Light、AVR 算术和混合 KEM–MQTT 的资源/握手优化，摘要未提供侧信道证据。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Low-Stack HAETAE for Memory-Constrained Microcontrollers

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i4.293-315)。
- 判定依据：Low-Stack HAETAE 通过分阶段执行、提前拒绝及熵编码省内存；摘要没有论证这些变化的恒时边界，需正文再筛。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## MPSpeed: Implementing and Optimizing MPC-in-the-Head Digital Signatures in Hardware: Accelerating Mirath on FPGA

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i3.982-1006)。
- 判定依据：MPSpeed 优化 Mirath 的 GGM 树和 MPC 算术硬件；MPC 协议视图不能自动视为抗泄漏掩码。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## NeonCROSS: Vectorized Implementation of Post-Quantum Signature CROSS on Cortex-A72 and Apple M3

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i1.250-272)。
- 判定依据：NeonCROSS 优化模约减、矩阵和树哈希的向量执行，摘要未报告侧信道性质。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Optimized Implementations of Keccak, Kyber, and Dilithium on the MSP430 Microcontroller

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i2.409-440)。
- 判定依据：MSP430 上调整 Keccak 和 NTT 的算术及内存访问以提速，摘要未声称秘密无关性或泄漏验证。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Optimizing and Implementing Threshold MAYO

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i3.489-517)。
- 判定依据：摘要中的 threshold 指多方分布式签名和主动对手安全，不能据此当成对功耗泄漏的掩码保护；保留为相邻主题。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-12；没有独立第二审读或本地复现。

## Optimizing the Post Quantum Signature Scheme CROSS for Resource Constrained Devices

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i3.224-246)。
- 判定依据：CROSS 在 Cortex-M4 上降低栈空间并以 DSP 提速，摘要未分析泄漏。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## PHOENIX: Crypto-Agile Hardware Sharing for ML-KEM and HQC

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i3.1228-1255)。
- 判定依据：PHOENIX 在 ML-KEM/HQC 间复用变换硬件以支持算法切换；共享资源是否泄漏是待研究问题，不是本文摘要已证实结果。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Pipelining FALCON’s Gaussian sampler: Towards practical FALCON acceleration

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i4.447-470)。
- 判定依据：流水化 Falcon SamplerZ 并优化拒绝采样延迟及随机数消耗；摘要没有对采样泄漏或随机源质量给出安全评估，低随机量不自动等于安全。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## RainHash2.0: Hardware- and Arithmetization-friendly Hash Function

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i4.62-115)。
- 判定依据：RainHash2.0 面向二进制域 ZK 电路和硬件效率；证明电路友好性不等于物理泄漏保护。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Refined Approx-SVP Rank Reduction Conditions and Adaptive Lattice Reduction for MSIS Security Estimation

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i4.397-422)。
- 判定依据：APBKZ/HeadAPBKZ 研究 Approx-SVP 条件和 MSIS 具体安全估计，属于格求解成本背景。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## SHARMONY: Composing SHA-2 and SHA-3 Hardware for Crypto-Agile PQC

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i4.945-969)。
- 判定依据：SHARMONY 为 SHA-2/SHA-3 共享寄存器与控制逻辑以提高资源效率；标准功能一致性不证明跨算法状态隔离。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## SQISign on ARM

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i4.471-495)。
- 判定依据：在 ARM NEON 上向量化 SQIsign 有限域与同源链，结合 Qlapoti 提升性能；摘要没有明确侧信道防护或评估贡献。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Structured Module Lattice-based Cryptography: Fine-Grained Parameter Selection without Compromising Performance

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i3.1032-1055)。
- 判定依据：为 Module-LWE/LWR 增加结构以细化参数和提速，摘要聚焦数学安全与性能取舍。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## TP-NTT: Batch NTT Hardware with Application to Relinearization

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i4.705-730)。
- 判定依据：TP-NTT 面向 FHE 批量变换和重线性化的面积吞吐优化，摘要未报告泄漏属性。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## TWFalcon: Triple-Word Arithmetic for Falcon: Giving Falcon the Precision to Fly Securely

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i2.347-371)。
- 判定依据：摘要聚焦 Falcon 数值精度、Gaussian sampler 误差界与性能，未给出具体侧信道防护评估；数值安全不能等同物理泄漏安全。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Vectorized Falcon-Sign Implementations using SSE2, AVX2, AVX-512F, NEON, and RVV

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i1.302-324)。
- 判定依据：跨指令集向量化 Falcon BaseSampler 与 FFT/iFFT，报告签名性能；摘要没有采样时序或物理泄漏防护结论。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## YATA: Yet Another TFHE Accelerator with Key Compression and Radix-8 NTT

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i1.325-352)。
- 判定依据：YATA 芯片压缩 TFHE 自举密钥并优化 NTT；硅片延迟/功耗效率不等于泄漏测试。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。
