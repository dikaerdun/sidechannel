# 已阅读的相邻主题与方法背景

当前 340 条；保留在目录与引用图中，不计入侧信道纳入论文数量。后续全文证据可以修订范围判定。

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

## Status report on the third round of the NIST Post-Quantum Cryptography Standardization process

- 来源：[NIST IR 2022](https://doi.org/10.6028/nist.ir.8413)。
- 判定依据：NIST 第三轮标准化选择背景，不是独立侧信道实验；原报告已被勘误更新取代，引用的确切版次未指定。
- 阅读来源：https://csrc.nist.gov/pubs/ir/8413/final。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Status report on the third round of the NIST Post-Quantum Cryptography Standardization process

- 来源：[NIST IR 2022](https://doi.org/10.6028/nist.ir.8413-upd1)。
- 判定依据：NIST IR 8413 勘误版本：官方说明仅补两条历史引用并重排引用号，作为标准化和版本背景。
- 阅读来源：https://csrc.nist.gov/pubs/ir/8413/upd1/final。
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

## Error Detection Architectures for Hardware/Software Co-Design Approaches of Number-Theoretic Transform

- 来源：[TCAD 2023](https://doi.org/10.1109/tcad.2022.3218614)。
- 判定依据：NTT 错误检测与重算编码；摘要中的 stuck-at 覆盖来自模拟，FPGA 开销不等于侧信道安全评价。
- 阅读来源：https://xplorestaging.ieee.org/document/9933800/。
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

## Reconfigurable and High-Efficiency Polynomial Multiplication Accelerator for CRYSTALS-Kyber

- 来源：[TCAD 2023](https://doi.org/10.1109/tcad.2022.3230359)。
- 判定依据：Kyber 多项式乘法的 Barrett 约减、并行核与存储复用优化，摘要以性能和面积为主。
- 阅读来源：https://xplorestaging.ieee.org/document/9992019/。
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

## A Configurable ML-KEM/Kyber Key-Encapsulation Hardware Accelerator Architecture

- 来源：[TCAS-II 2024](https://doi.org/10.1109/tcsii.2024.3442228)。
- 判定依据：ML-KEM/Kyber 加速器资源与性能比较；摘要未给出物理泄漏评价，题名不能证明最终 FIPS 203 完整一致性。
- 阅读来源：https://xplorestaging.ieee.org/document/10634219/。
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

## Bitstream Fault Injection Attacks on CRYSTALS Kyber Implementations on FPGAs

- 来源：[DATE 2024](https://doi.org/10.23919/date58400.2024.10546550)。
- 判定依据：对 FPGA 比特流进行主动篡改的故障攻击及防护；本次摘要范围归入故障背景，不计为被动侧信道攻击。
- 阅读来源：https://xplorestaging.ieee.org/document/10546550/。
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

## Super-K: A Superscalar CRYSTALS-KYBER Processor Based on Efficient Arithmetic Array

- 来源：[TCAS-II 2024](https://doi.org/10.1109/tcsii.2024.3382772)。
- 判定依据：Kyber 处理器的性能、面积和功耗架构；摘要未给出侧信道攻击或防护评价，保留实现背景。
- 阅读来源：https://xplorestaging.ieee.org/document/10485193/。
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

## "That's my perspective from 30 years of doing this": An Interview Study on Practices, Experiences, and Challenges of Updating Cryptographic Code

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/krause)。
- 判定依据：开发者访谈及密码/PQC 迁移实践；摘要没有测量或实现侧信道机制。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## A Formal Analysis of Apple's iMessage PQ3 Protocol

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/linker)。
- 判定依据：iMessage PQ3 的 TAMARIN 协议证明；不是实现泄漏分析。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

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

## A Tale of Two Worlds, a Formal Story of WireGuard Hybridization

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/lafourcade)。
- 判定依据：混合 WireGuard 协议弱点与形式证明；不提供功耗或实现侧信道保证。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Accelerating NTT with RISC-V Vector Extension for Fully Homomorphic Encryption

- 来源：[TCHES 2025](https://doi.org/10.46586/tches.v2025.i4.711-736)。
- 判定依据：用 RISC-V 向量扩展优化 OpenFHE 的 NTT/INTT 与应用性能，摘要未涉及泄漏安全。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Achilles: A Formal Framework of Leaking Secrets from Signature Schemes via Rowhammer

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/liang-achilles)。
- 判定依据：Rowhammer 故障修改签名参数后利用输出泄露秘密，涵盖经典/PQC 签名；保留故障邻接方向，不归为被动侧信道。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Algebraic Linear Analysis for Number Theoretic Transform in Lattice-Based Cryptography

- 来源：[TCHES 2025](https://doi.org/10.46586/tches.v2025.i3.668-692)。
- 判定依据：摘要贡献是 CryptoLine/islpy 对 NTT 汇编范围与算术正确性的验证，未说明侧信道非干扰或泄漏评估；保留为 PQC 实现验证背景。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Approximation Enforced Execution of Untrusted Linux Kernel Extensions

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/sun-hao)。
- 判定依据：eBPF 内核扩展的空间内存安全与运行检查；摘要未建立侧信道非干扰。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Arbitrary-Threshold Fully Homomorphic Encryption with Lower Complexity

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/chang-yijia-encryption)。
- 判定依据：任意阈值 FHE/近似秘密分享协议构造；不是实现中的物理掩码泄漏。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## BlueGuard: Accelerated Host and Guest Introspection Using DPUs

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/orenbach)。
- 判定依据：DPU 提权观察下的主客机直接内省；非额外侧信道推断。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Breaking the Layer Barrier: Remodeling Private Transformer Inference with Hybrid CKKS and MPC

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/xu-tianshi)。
- 判定依据：CKKS/MPC 混合 Transformer 私有推理与性能；摘要未分析实现观察。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Bundled Authenticated Key Exchange: A Concrete Treatment of Signal's Handshake Protocol and Post-Quantum Security

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/hashimoto-key-exchange)。
- 判定依据：Signal 握手的 bundled authenticated key exchange 与后量子协议安全；非物理实现分析。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## CertTA: Certified Robustness Made Practical for Learning-Based Traffic Analysis

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/yan-jinzhu)。
- 判定依据：流量分类器对填充、时序和虚假包的鲁棒性认证；摘要未明确秘密推断目标，保留方法背景待正文细化。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## CoVault: Secure, Scalable Analytics of Personal Data

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/de-viti)。
- 判定依据：MPC/TEE 协同的隐私数据分析；摘要未给侧信道防护论证。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Comprehensive Deniability Analysis of Signal Handshake Protocols: X3DH, PQXDH to Fully Post-Quantum with Deniable Ring Signatures

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/katsumata)。
- 判定依据：Signal 握手否认性与后量子环签名协议；非实现侧信道。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Deanonymizing Ethereum Validators: The P2P Network Has a Privacy Issue

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/heimbach)。
- 判定依据：Ethereum P2P 验证者 IP 去匿名化；摘要未明确时序或共享资源观察机制，保留协议元数据邻接并待正文。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Detecting Compromise of Passkey Storage on the Cloud

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/islam)。
- 判定依据：已被窃取的云端 passkey 的滥用检测；密钥直接失窃不等于侧信道。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## DiffLoc: WiFi Hidden Camera Localization Based on Electromagnetic Diffraction

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/zhang-xiang)。
- 判定依据：利用主动金属板和 WiFi 衍射定位隐藏相机；观察正常无线发射，保留物理定位背景，不等同于计算的非预期电磁泄漏。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Dorami: Privilege Separating Security Monitor on RISC-V TEEs

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/kuhne)。
- 判定依据：RISC-V 安全监控器的固件权限分离；不是侧信道安全证明。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## ECC.fail: Mounting Rowhammer Attacks on DDR4 Servers with ECC Memory

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/kamadan)。
- 判定依据：DDR4 TRR/ECC 逆向及 RSA 公钥故障；主要是故障完整性攻击，不是 RSA 秘密的被动观察。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## EKC: A Portable and Extensible Kernel Compartment for De-Privileging Commodity OS

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/yan-jiaqin)。
- 判定依据：Rust 内核 compartment 与操作系统隔离；摘要未分析侧信道。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Enabling Low-Cost Secure Computing on Untrusted In-Memory Architectures

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/ghinani)。
- 判定依据：不可信存内计算架构上的安全计算协议；协议安全不等于物理观察安全。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Encarsia: Evaluating CPU Fuzzers via Automatic Bug Injection

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/bolcskei)。
- 判定依据：通过自动注入架构 bug 评估 CPU fuzzer；无侧信道检测结论。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Encrypted Access Logging for Online Accounts: Device Attributions without Device Tracking

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/ortega-perez)。
- 判定依据：加密设备归属日志及 FIDO2 协议隐私；无额外物理/时序观察。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Exploring How to Authenticate Application Messages in MLS: More Efficient, Post-Quantum, and Anonymous Blocklistable

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/hashimoto-blocklistable)。
- 判定依据：MLS 消息认证的带宽、后量子和匿名黑名单协议；非实现泄漏。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Exploring and Exploiting the Resource Isolation Attack Surface of WebAssembly Containers

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/yu-zhaofeng)。
- 判定依据：Wasm 容器的资源隔离与拒绝服务；摘要目标不是秘密推断。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

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

## For Human Ears Only: Preventing Automated Monitoring on Voice Data

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/shahid)。
- 判定依据：对直接录音作语音变换以限制 ASR；不是替代物理通道窃听。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Formally Verified Correctness Bounds for Lattice-Based Cryptography

- 来源：[CCS 2025](https://dl.acm.org/doi/10.1145/3719027.3765218)。
- 判定依据：形式化格 KEM 的解密正确性概率界；ML-KEM 部分针对文献使用的近似统计事件，FrodoKEM 展示非启发式界。摘要没有侧信道观察或实现泄漏保证，保留为 PQC 相邻理论。
- 阅读来源：https://kannwischer.eu/papers/2025_ec_lattice_bounds.pdf。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## GPUHammer: Rowhammer Attacks on GPU Memories are Practical

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/lin-shaopeng)。
- 判定依据：GDDR6 GPU Rowhammer 位翻转和 DNN 篡改；目标为故障完整性。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Game of Arrows: On the (In-)Security of Weight Obfuscation for On-Device TEE-Shielded LLM Partition Algorithms

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/wang-pengli)。
- 判定依据：对直接可访问的混淆权重作几何分析；不是缓存或功耗观察。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## GenHuzz: An Efficient Generative Hardware Fuzzer

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/wu-lichao)。
- 判定依据：生成式 RISC-V 硬件 fuzzing 发现架构漏洞；架构 bug 不自动属于侧信道。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Generation of Fast Finite Field Arithmetic forCortex-M4 with ECDH and SQIsign Applications

- 来源：[TCHES 2025](https://doi.org/10.46586/tches.v2025.i4.588-620)。
- 判定依据：m4-modarith 自动生成快速有限域算术并证明约减正确性；功能证明不能自动推得恒时保证。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## GlitchFHE: Attacking Fully Homomorphic Encryption Using Fault Injection

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/mankali)。
- 判定依据：CKKS/BFV FHE 加速器故障注入改变输出完整性；保留故障邻接，摘要不主张被动秘密泄漏。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

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

## Hobbit: Space-Efficient zkSNARK with Optimal Prover Time

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/pappas)。
- 判定依据：后量子 zkSNARK 的证明时间与空间；非实现侧信道。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## How to Compare Bandwidth Constrained Two-Party Secure Messaging Protocols: A Quest for A More Efficient and Secure Post-Quantum Protocol

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/auerbach)。
- 判定依据：后量子消息协议在带宽约束下的安全比较和优化；非实现泄漏。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## How to Recover a Cryptographic Secret From the Cloud

- 来源：[CCS 2025](https://doi.org/10.1145/3719027.3765127)。
- 判定依据：云端秘密备份与恢复协议，讨论凭据丢失及恶意云，不是通过功耗或侧信道恢复秘密。仅读明确对应题名与作者的 ePrint 摘要，正式版本差异待核。
- 阅读来源：https://eprint.iacr.org/2023/1308。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## HyTrack: Resurrectable and Persistent Tracking Across Android Apps and the Web

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/wessels)。
- 判定依据：Android 原生/web 共享浏览器状态与持久标识符跟踪；摘要是可直接使用的状态而非侧信道测量。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## I Can Tell Your Secrets: Inferring Privacy Attributes from Mini-app Interaction History in Super-apps

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/cai-yifeng)。
- 判定依据：super-app 内部部门利用可收集的交互日志推断属性；属直接数据用途与隐私推断。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

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

## LLMmap: Fingerprinting for Large Language Models

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/pasquini)。
- 判定依据：主动查询 LLM 并从正常文本输出识别模型版本；不是缓存、时间或功耗指纹。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Learning from Functionality Outputs: Private Join and Compute in the Real World

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/falzon)。
- 判定依据：PJC 协议功能输出本身导致隐私推断；保留功能泄漏边界背景。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Let us walk on the 3-isogeny graph: efficient, fast, and simple

- 来源：[TCHES 2025](https://doi.org/10.46586/tches.v2025.i4.644-666)。
- 判定依据：优化 3-isogeny 链、相关 KEM 与 CTIDH 密钥生成；虽应用于 CTIDH，摘要未单独给出新恒时证明或泄漏评估，先保留算术背景。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Lost in the Mists of Time: Expirations in DNS Footprints of Mobile Apps

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/so)。
- 判定依据：移动应用过期域名依赖与接管风险；DNS footprint 不是本文中的秘密侧信道。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## McSee: Evaluating Advanced Rowhammer Attacks and Defenses via Automated DRAM Traffic Analysis

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/jattke)。
- 判定依据：用示波器解码 DRAM 总线流量评估 Rowhammer 与防护；保留测量方法背景，摘要未作秘密推断。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## More is Less: Extra Features in Contactless Payments Break Security

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/pavlides)。
- 判定依据：EMV 附加功能的协议交互漏洞与未授权支付；非实现侧信道。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Multiplying Polynomials without Powerful Multiplication Instructions

- 来源：[TCHES 2025](https://doi.org/10.46586/tches.v2025.i1.160-202)。
- 判定依据：改进缺少强乘法指令平台的 Barrett/FFT 多项式乘法；shape-independent 指模数形状的效率/正确性，不是秘密独立性。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Narrowbeer: A Practical Replay Attack Against the Widevine DRM

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/roudot)。
- 判定依据：Widevine 时间与随机性处理的重放/许可证新鲜性漏洞；非侧信道测量。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## NeuroScope: Reverse Engineering Deep Neural Network on Edge Devices using Dynamic Analysis

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/wu-ruoyu)。
- 判定依据：对 DNN 二进制直接动态分析及逆向；摘要未限定非预期侧信道观察，保留方法背景。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

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

## PICACHV: Formally Verified Data Use Policy Enforcement for Secure Data Analytics

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/chen-haobin)。
- 判定依据：关系代数及 Coq 数据使用政策证明；TEE 运行信任不等于物理侧信道保证。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## PORTAL: Fast and Secure Device Access with Arm CCA for Modern Arm Mobile System-on-Chips (SoCs)

- 来源：[SP 2025](https://www.ieee-security.org/TC/SP2025/accepted-papers.html#collapse-48)。
- 判定依据：PORTAL 以 Arm CCA 访问隔离实现设备 I/O 的明文共享内存，摘要的保密与性能主张不能自动转为物理侧信道保护。
- 阅读来源：https://sang.fan/assets/papers/portal_sp25.pdf。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Phantom: Privacy-Preserving Deep Neural Network Model Obfuscation in Heterogeneous TEE and GPU System

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/bai-juyang)。
- 判定依据：TEE/GPU 异构系统中的 DNN 权重混淆与模型盗取防护；摘要没有侧信道观察模型。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Posthammer: Pervasive Browser-based Rowhammer Attacks with Postponed Refresh Commands

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/de-ridder)。
- 判定依据：浏览器通过推迟刷新实施 Rowhammer 位翻转；主要为故障攻击。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Practically Secure Honey Password Vaults: New Design and New Evaluation against Online Guessing

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/cheng-haibo)。
- 判定依据：honey password vault 的诱饵分布与在线猜测；不是实现侧信道。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Principled and Automated Approach for Investigating AR/VR Attacks

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/shoaib)。
- 判定依据：从 AR/VR 日志建立攻击来源图和因果关联；日志审计不是秘密侧信道观察。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Prompt Inference Attack on Distributed Large Language Model Inference Frameworks

- 来源：[CCS 2025](https://doi.org/10.1145/3719027.3744820)。
- 判定依据：从分布式 LLM 传输的中间输出重建提示，摘要未显示额外物理或微架构观察；保留为相邻隐私研究，与 MoEcho 硬件侧信道区分。
- 阅读来源：https://arxiv.org/abs/2503.09291。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Proving Faster Implementations Faster: Combining Deductive and Circuit-Based Reasoning in EasyCrypt

- 来源：[SP 2025](https://www.ieee-security.org/TC/SP2025/accepted-papers.html#collapse-166)。
- 判定依据：混合推演与电路等价检查用于 ML-KEM 优化代码的功能正确性。所读正文另介绍 Jasmin 对恒时/推测恒时属性的保持能力；功能等价证明本身不等于这些属性或模拟泄漏的证明。按功能验证与工具链背景保留。出版题名为 Faster Verification of Faster Implementations，录用目录的 Proving Faster Implementations Faster 是同一论文的题名别名。
- 阅读来源：https://xplorestaging.ieee.org/document/11023411/ ; https://cryptosith.org/papers/mapreduce-20250907.pdf。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Qelect: Lattice-based Single Secret Leader Election Made Practical

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/wang-yunhao)。
- 判定依据：基于格和阈值 FHE 的秘密领导者选举协议；PQC 构造及性能不等于实现侧信道。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

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

## RollingEvidence: Autoregressive Video Evidence via Rolling Shutter Effect

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/qian)。
- 判定依据：用滚动快门主动嵌入视频完整性验证探针；主要为取证编码，不是非预期秘密观察。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Rowhammer-Based Trojan Injection: One Bit Flip Is Sufficient for Backdooring DNNs

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/li-xiang)。
- 判定依据：用单比特 Rowhammer 故障为全精度 DNN 注入后门；属于完整性篡改。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Rudraksh: A compact and lightweight post-quantum key-encapsulation mechanism

- 来源：[TCHES 2025](https://doi.org/10.46586/tches.v2025.i2.647-680)。
- 判定依据：Rudraksh 联合选择 LWE 参数、ASCON 与 FPGA 实现以降低面积；摘要中的 CCA/Core-SVP 安全是密码学口径，不构成物理侧信道保护。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Save what must be saved: Secure context switching with Sailor

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/kalani)。
- 判定依据：从 Sail ISA 规范推导上下文切换必须保存的架构状态；摘要未明确旁路观察，保留隔离及架构泄漏背景。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Secure Information Embedding in Forensic 3D Fingerprinting

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/wang-canran)。
- 判定依据：在三维打印品中主动嵌入抗破坏标识；为取证水印，不是实现侧信道。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Security Attacks Abusing Pulse-level Quantum Circuits

- 来源：[SP 2025](https://www.ieee-security.org/TC/SP2025/accepted-papers.html#collapse-6)。
- 判定依据：研究量子 SDK 自定义门的脉冲语义与逻辑电路语义不一致导致的恶意执行，属于量子软件完整性；不是后量子密码实现或被动波形侧信道。
- 阅读来源：https://caslab.io/publications/xu2025security.pdf。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Seeing Through: Analyzing and Attacking Virtual Backgrounds in Video Calls

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/weissberg)。
- 判定依据：聚合视频背景分割失败后直接可见的环境像素；属功能输出隐私泄漏。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Serverless Functions Made Confidential and Efficient with Split Containers

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/shi-jiacheng)。
- 判定依据：机密 serverless 的 TCB、容器设计及性能；没有摘要级侧信道保证。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

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

## SoK: A Security Architect's View of Printed Circuit Board Attacks

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/harrison)。
- 判定依据：PCB 篡改威胁与防护架构综述；保留物理安全背景，摘要未给侧信道专项范围。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## SoK: Come Together – Unifying Security, Information Theory, and Cognition for a Mixed Reality Deception Attack Ontology & Analysis Framework

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/teymourian)。
- 判定依据：混合现实欺骗的信息论与认知框架；不是密码实现或硬件侧信道。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## SoK: Decoding the Enigma of Encrypted Network Traffic Classifiers

- 来源：[SP 2025](https://www.ieee-security.org/TC/SP2025/accepted-papers.html#collapse-219)。
- 判定依据：SoK 审查加密流量分类中的数据集、特征和评价假设，作为方法学背景；未据此推断所有网站指纹论文都使用同样有问题的数据。
- 阅读来源：https://arxiv.org/abs/2503.20093。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## SoK: Efficiency Robustness of Dynamic Deep Learning Systems

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/rathnasuriya)。
- 判定依据：动态深度学习的效率攻击与资源消耗；摘要针对可用性而非秘密推断。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Software Availability Protection in Cyber-Physical Systems

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/li-ao)。
- 判定依据：网络物理系统的软件攻击恢复和可用性；非秘密推断。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## System Register Hijacking: Compromising Kernel Integrity By Turning System Registers Against the System

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/miller)。
- 判定依据：通过系统寄存器劫持控制流和破坏内核完整性；非侧信道推断。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## TETD: Trusted Execution in Trust Domains

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/wang-zhanbo)。
- 判定依据：TDX 域内可信执行与权限分离；摘要未证明观察模式安全。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## THEMIS: Towards Practical Intellectual Property Protection for Post-Deployment On-Device Deep Learning Models

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/huang-yujin)。
- 判定依据：从部署 DNN 重建可写模型并加水印，保护知识产权；非侧信道。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## TimeTravel: Real-time Timing Drift Attack on System Time Using Acoustic Waves

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/liu-jianshuo)。
- 判定依据：利用声波操纵 RTC 石英振荡器造成时钟漂移；属于主动完整性/信号注入，而非被动读出。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Towards Practical, End-to-End Formally Verified X.509 Certificate Validators with Verdict

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/lin-zhengyao)。
- 判定依据：X.509 解析、构建及验证策略正确性；摘要未给侧信道保证。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Tracking You from a Thousand Miles Away! Turning a Bluetooth Device into an Apple AirTag Without Root Privileges

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/chen-junming)。
- 判定依据：利用 Find My 网络协议把蓝牙设备变为可跟踪标识；非 PQC，摘要没有实现泄漏机制。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## TrafficFormer: An Efficient Pre-trained Model for Traffic Data

- 来源：[SP 2025](https://www.ieee-security.org/TC/SP2025/accepted-papers.html#collapse-27)。
- 判定依据：TrafficFormer 的预训练、数据增强与协议理解是一般流量学习方法；摘要没有给出具体敏感目标与侧信道观察关系，保留为方法背景。
- 阅读来源：https://liuzhuotao.github.io/publications/trafficformer/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Transparent Attested DNS for Confidential Computing Services

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/delignat-lavaud)。
- 判定依据：通过 DNS 名称绑定 TEE 远程证明并作透明日志；协议认证不等于消除侧信道。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## VeloFHE: GPU Acceleration for FHEW and TFHE Bootstrapping

- 来源：[TCHES 2025](https://doi.org/10.46586/tches.v2025.i3.81-114)。
- 判定依据：VeloFHE 通过 GPU NTT、批处理与异步执行优化 FHEW/TFHE 自举，摘要未研究侧信道。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Wanilla: Sound Noninterference Analysis for WebAssembly

- 来源：[CCS 2025](https://doi.org/10.1145/3719027.3765156)。
- 判定依据：为 WebAssembly 提供静态非干扰与内存完整性分析；摘要没有明确的计时/物理泄漏模型，保留相邻层，不能由 noninterference 标题自动当作侧信道证明。
- 阅读来源：https://arxiv.org/abs/2509.08758。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Who Pays Whom? Anonymous EMV-Compliant Contactless Payments

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/olivier-anclin)。
- 判定依据：EMV 支付的匿名性与可链接性协议；SCA 在这里指 Strong Customer Authentication，不是 side-channel analysis。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## X.509DoS: Exploiting and Detecting Denial-of-Service Vulnerabilities in Cryptographic Libraries using Crafted X.509 Certificates

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/shi-bing)。
- 判定依据：X.509 证书触发密码库拒绝服务；不是秘密相关泄漏。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Your Shield is My Sword: A Persistent Denial-of-Service Attack via the Reuse of Unvalidated Caches in DNSSEC Validation

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/zhang-shuhan)。
- 判定依据：复用未验证 DNSSEC 缓存造成持久拒绝服务；不是缓存时间侧信道。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## eSIMplicity or eSIMplification? Privacy and Security Risks in the eSIM Ecosystem

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/motallebighomi)。
- 判定依据：eSIM 提供商、路由与配置生态隐私；非实现侧信道。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## "Tap" Without Tapping: A Tag Discovery Forgery Attack on Android NFC

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/li-yilin)。
- 判定依据：Android 标签派发伪造，无需物理 NFC 交互；摘要研究授权语义，非侧信道读出。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## 2FiA: Towards WiFi Sensing-Based Authentication with Unique Biometrics

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00087)。
- 判定依据：Wi-Fi 呼吸/心搏用于身份认证；摘要不研究非预期计算活动泄漏。RSA 在此指生理耦合，不是密码算法。
- 阅读来源：https://xplorestaging.ieee.org/document/11573398/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## A Formal Security Analysis of CAN XL

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/tang-zhaozhou)。
- 判定依据：CAN XL MAC 子层形式化与信号协议攻击；摘要未建立秘密侧信道推断。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## A Full Threshold NIST PQC-Compliant Framework for Distributed Trust in Federal Public Key Infrastructure

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00164)。
- 判定依据：SHIELD 为符合 ML-DSA 功能的分布式门限签名框架；标准兼容及抗节点失陷不等于实现侧信道安全。
- 阅读来源：https://xplorestaging.ieee.org/document/11573478/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## A High-Performance and Reconfigurable Hardware Architecture for FrodoKEM

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i3.171-197)。
- 判定依据：FrodoKEM 全硬件采用分块矩阵和共享 BRAM 优化吞吐率；摘要未给出共享残留或物理泄漏分析。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## A Leakage-Free Framework for Private Set Operations

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00171)。
- 判定依据：during-execution leakage 指集合操作协议中间信息；未建立功耗、时间或访存观察模型。
- 阅读来源：https://xplorestaging.ieee.org/document/11573505/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## A Maliciously-Secure Post-Quantum OPRF from Crypto Dark Matter

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00221)。
- 判定依据：后量子恶意安全 OPRF 和 VOLE 协议；相关随机性及模转换不自动等于掩码实现防护。
- 阅读来源：https://xplorestaging.ieee.org/document/11573481/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## A Unified RISC-V Vector Framework for Large-Scale NTT in FHE and ZKP

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i4.970-997)。
- 判定依据：RISC-V 向量框架适配 FHE/ZKP 大规模 NTT 并在 gem5 上评价性能，摘要未报告泄漏评估。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## AESpoly: Symmetric-Key Cryptographic Designs Using Instruction-Level Parallelism between AES and Polynomial Hash

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00138)。
- 判定依据：利用 AES/CLMUL 指令并行性设计对称方案并比较性能；未在摘要评估观察通道。
- 阅读来源：https://xplorestaging.ieee.org/document/11573476/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## ARM MTE Performance in Practice

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/noh)。
- 判定依据：MTE 性能与微架构开销测量；性能现象不自动构成秘密相关通道。
- 阅读来源：publisher-deposited Crossref abstract。
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

## Analyzing Cryptography in Context: A Cryptography-Native Approach to Threat Modeling

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/canetti)。
- 判定依据：密码协议的社会技术威胁建模；未评价实现泄漏。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Auditing Apple’s DifferentialPrivacy.framework: Implementation Bugs, Misconfigurations, and Practical Risks

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00225)。
- 判定依据：审计差分隐私浮点噪声及上传日志的协议输出风险；非本库实现侧信道纳入数，保留数值/隐私背景。
- 阅读来源：https://xplorestaging.ieee.org/document/11573572/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## BLE Theft Auto: Evaluating the Security of Aftermarket BLE-based Automotive Remote Control Systems

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/yu-jerry)。
- 判定依据：BLE 私有应用协议的控制与认证缺陷；摘要未建立侧信道。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## BOLT-FHE: An Efficient Unified Framework for GPU-based TFHE Bootstrapping via On-Chip Local Tiling Strategies

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i3.198-223)。
- 判定依据：BOLT-FHE 通过块内执行和融合内核优化 GPU 自举；固定执行模板不是自动成立的侧信道证明。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Banshee: Target Switch Attacks on Gimbal-Stabilized Visual Tracking Systems via Acoustic Injection

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00129)。
- 判定依据：声学注入改变云台与跟踪结果，是主动传感器完整性攻击而非秘密观察。
- 阅读来源：https://xplorestaging.ieee.org/document/11573942/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Battering RAM: Low-Cost Interposer Attacks on Confidential Computing via Dynamic Memory Aliasing

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00052)。
- 判定依据：动态内存地址篡改绕过 TEE 保护并取得明文读写；按物理完整性/故障相邻保留，区别于 TEE.Fail 的事务观察路径。
- 阅读来源：https://xplorestaging.ieee.org/document/11573462/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Beyond Indistinguishability: Measuring Extraction Risk in LLM APIs

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00165)。
- 判定依据：定义 LLM 输出提取与不可区分性的关系；是任务隐私理论，未建立密码实现的测量通道。
- 阅读来源：https://xplorestaging.ieee.org/document/11573553/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Blinding Post-Quantum Hash-and-Sign Signatures

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00032)。
- 判定依据：blinding 是盲签名协议，非侧信道盲化；UOV/Wave 构造未由摘要建立物理防护。
- 阅读来源：https://xplorestaging.ieee.org/document/11573475/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## BreakFAST: Confused Deputy Attack on Infinity Fabric to Break AMD SEV-SNP

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00259)。
- 判定依据：利用 PSP 与 MMIO 路由的 confused-deputy 逻辑缺陷；不是通过频率或功耗推断秘密。
- 阅读来源：https://xplorestaging.ieee.org/document/11573570/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

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

## Certified in Theory, Broken in Practice: Assumption Gaps in Cryptographic Model Certification

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/luck)。
- 判定依据：零知识模型审计的泛化假设缺口；非时序或物理实现泄漏。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Chorus: Secret Recovery with Ephemeral Client Committees

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00149)。
- 判定依据：以临时客户端委员会实现合法秘密恢复；secret recovery 不是侧信道攻击恢复。
- 阅读来源：https://xplorestaging.ieee.org/document/11573522/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## CompLeak: Deep Learning Model Compression Exacerbates Privacy Leakage

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/li-na)。
- 判定依据：利用模型置信输出的成员推断；本条为功能输出隐私，不是压缩计算耗时/硬件通道。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Completing the Chain: Verified Implementations of Hash-Based Signatures and Their Security

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i3.958-981)。
- 判定依据：摘要连接 XMSS/XMSSMT 功能实现、规范与密码学安全证明，未提出侧信道安全保证；保留为验证工具与哈希签名背景。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Concretely Efficient Blind Signatures Based on VOLE-in-the-Head Proofs and the MAYO Trapdoor

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/baum)。
- 判定依据：MAYO/VOLE-in-the-head 盲签名构造与性能，未给出实现泄漏分析。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Correction Fault Attack on CROSS under Unknown Bit Flips

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i2.192-217)。
- 判定依据：对 CROSS 公共校验矩阵的未知位置/值翻转进行纠正故障攻击，含电压注入和 ECC 条件分析；类 Rowhammer 的故障模型不代表已演示 Rowhammer。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Cryptanalysis of LDPC-Based Pseudorandom Error-Correcting Codes

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/wang-tianrui)。
- 判定依据：LDPC 伪随机码的数学攻击与水印分析，不是编码型 PQC 的功耗攻击。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Crypto Wars in Secure Messaging: Covert Channels in Signal Despite Leaked Keys

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/giustolisi)。
- 判定依据：Signal 密码文本中主动嵌入变形加密通信；非实现副作用产生的通道。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## DRR-NTT: Efficient NTT Accelerator in Lattice-Based Cryptography By Dimensionality Reduction in RRAM

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i2.808-833)。
- 判定依据：RRAM NTT 研究阵列干扰和量化误差的计算精度；使用实测电阻并不等于测量秘密相关泄漏。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## DRVFuzz: Data-Sensitive RISC-V CPU Fuzzing

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/yu-zehong)。
- 判定依据：数据敏感 CPU fuzzing 查逻辑错误；未报告泄漏观测模型。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Decor: Delegated Computation on Randomness for Secure Evaluation of Nonlinear Functions

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00256)。
- 判定依据：可信 dealer 预处理非线性函数的 MPC 框架；未建立实体机器观察下的掩码保证。
- 阅读来源：https://xplorestaging.ieee.org/document/11573504/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Demystifying and Exploiting ASLR on NVIDIA GPUs

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00078)。
- 判定依据：分析可获取地址之间的 ASLR 相关性及未随机化区域；摘要未建立额外时间/缓存读出通道，先作地址布局背景。
- 阅读来源：https://xplorestaging.ieee.org/document/11573432/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Descriptors of Exposure: Undermining Tor Anonymity through Exploiting Descriptor Flood

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00071)。
- 判定依据：以描述符洪泛、节点失效推动 DoS/去匿名；具体身份观察机制待正文，先保留主动网络攻击相邻项。
- 阅读来源：https://xplorestaging.ieee.org/document/11573569/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Design and Implementation of a Physical Implant Attack on the Boeing 737

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/crow)。
- 判定依据：物理总线植入与信号操纵；摘要主要是完整性攻击，非旁路观测恢复秘密。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Dory: Streaming PCG with Small Memory

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00079)。
- 判定依据：流式相关随机数生成与 LPN 参数攻击；low Hamming weight 不意味着实测侧信道提示。
- 阅读来源：https://xplorestaging.ieee.org/document/11573541/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Download More RAM: Dismantling Windows Operating System Defences with Mischievous Memory

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/collins)。
- 判定依据：内存别名导致直接任意读写；与基于侧信道的推断区分。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Efficient Polynomial Multiplication for HQC on ARM Cortex-M4

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i4.998-1021)。
- 判定依据：HQC 在 Cortex-M4 上以混合 FAFFT-CRT 和调度优化乘法，摘要未说明物理防护。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Efficient Threshold ML-DSA

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/celi)。
- 判定依据：兼容 ML-DSA 的阈值签名 MPC 协议；分布式秘密共享不自动等于实现掩码。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## FABRICKED: Misconfiguring Infinity Fabric to Break AMD SEV-SNP

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/schlueter-1)。
- 判定依据：修改互连路由导致直接读写与伪造证明；非隐含物理或时序推断。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## FLOSS: Fast Linear Online Secret-Shared Shuffling

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/chang-ian)。
- 判定依据：两方安全计算的秘密共享打乱；未声明本地实现的侧信道保护。
- 阅读来源：publisher-deposited Crossref abstract。
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

## Fuzzing Open-Source GPU Hardware with SIMT Program Generation

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/gao-zibo)。
- 判定依据：GPU RTL 与 ISA 差分 fuzzing 查正确性错误；未建立侧信道判据。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## GDDR: Greatly Disturbing DRAM Rows — Cross-Component Rowhammer Attacks from Modern GPUs

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00228)。
- 判定依据：GPU Rowhammer 位翻转引发跨 GPU/CPU 内存访问，为故障与完整性研究。
- 阅读来源：https://xplorestaging.ieee.org/document/11573509/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## GPUBreach: Privilege Escalation Attacks on GPUs using Rowhammer

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00177)。
- 判定依据：通过 GPU Rowhammer 提权后读取 cuPQC 密钥；PQC 案例属于内存失陷，不能记为 PQC 功耗恢复。
- 阅读来源：https://xplorestaging.ieee.org/document/11573424/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## GateBreaker: Gate-Guided Attacks on Mixture-of-Expert LLMs

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/wu-lichao)。
- 判定依据：定位并禁用 MoE 安全神经元的模型篡改；不是通过硬件路由时序推断。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## GeForge: Hammering GDDR Memory to Forge GPU Page Tables for Fun and Profit

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00230)。
- 判定依据：通过 GPU 页表位翻转获得访问和提权；不是正常执行下的秘密观测。
- 阅读来源：https://xplorestaging.ieee.org/document/11573423/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## GoSSamer: Lightweight and Linear-Communication Asynchronous (Dynamic Proactive) Secret Sharing and the Applications

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00185)。
- 判定依据：异步及主动秘密分享的通信与计算优化；PQC 协议性质不等于物理泄漏韧性。
- 阅读来源：https://xplorestaging.ieee.org/document/11573498/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## HAMLOCK: HArdware-Model LOgically Combined attacK

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/amgain)。
- 判定依据：硬件木马与模型后门配合改变输出；低功耗开销不是秘密侧信道实验。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Hardware Trojans from Invisible Inversions: On the Trojanizability of Standard Cell Libraries

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00219)。
- 判定依据：比较标准单元的背面 SEM 可辨性并植入后门；不是功耗/EM 木马检测或秘密观察评估。
- 阅读来源：https://xplorestaging.ieee.org/document/11573433/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

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

## HijackKV: New Threat in Position-Independent KV Cache Reuse

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/zhang-yichi)。
- 判定依据：KV 缓存复用造成上下文投毒与行为劫持；本篇摘要不报告缓存时序提取。
- 阅读来源：publisher-deposited Crossref abstract。
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

## INSIGHT: Automatic Generation of Explanations for Efficient Identification of Hardware Bugs and Underspecifications

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00201)。
- 判定依据：硬件与 ISA 参考模型的功能偏差解释和聚类；未由摘要建立侧信道非干扰。
- 阅读来源：https://xplorestaging.ieee.org/document/11573561/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Improving ML-KEM and ML-DSA on OpenTitan: Efficient Multiplication Vector Instructions for OTBN

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i2.495-519)。
- 判定依据：OTBN 的向量乘法扩展及软硬件分工优化时间面积积；不能继承 OpenTitan 名称所暗示的整体物理保护。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## InstrSem: Automatically and Generically Inferring Semantics of (Undocumented) CPU Instructions

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/hetterich-lorenz-instrsem)。
- 判定依据：从架构可见状态推断指令语义；属于相关逆向工具，非泄漏检测本身。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## It’s a Feature, Not a Bug: Secure and Auditable State Rollback for Confidential Cloud Applications

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00148)。
- 判定依据：允许受策略约束的状态回滚并审计完整性；未说明物理历史或时序泄漏。
- 阅读来源：https://xplorestaging.ieee.org/document/11573496/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Jailbreaking the AMD Secure Processor: Enabling Live Analysis of SEV-SNP's Undocumented Security Boundaries

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/shen)。
- 判定依据：内存别名与 TOCTOU 破解 ASP 并直接读取/伪造；非被动 SCA。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Lattice-based Threshold Blind Signatures

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00118)。
- 判定依据：格门限盲签名的协议构造与证明；盲性、节点门限和硬件掩码是不同保证。
- 阅读来源：https://xplorestaging.ieee.org/document/11573582/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Libra: Pattern-Scheduling Co-Optimization for Cross-Scheme FHE Code Generation over GPGPU

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/bian-song)。
- 判定依据：跨 FHE 方案的 GPU 编译与调度性能；未分析敏感执行副作用。
- 阅读来源：publisher-deposited Crossref abstract。
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

## Loongleak: Architectural Cross-Privilege-Boundary Data Leakage on LoongArch CPUs

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/hetterich-lorenz-loongleak)。
- 判定依据：作者明确为架构可见 stale bits 直接读出，不需要 timing 或 side channels。
- 阅读来源：publisher-deposited Crossref abstract。
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

## MULCOTAINT: Towards Efficient Multi-tag Dynamic Taint Analysis via Hardware/Software Co-design

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/qi-bing)。
- 判定依据：通用多标签动态污点分析加速；摘要没有秘密泄漏专项验证。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Memclave: Secure In-Memory Enclave for Untrusted Hosts

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/choudhari)。
- 判定依据：PIM 的隔离、完整性和保护数据路径；摘要提及 cache footprint，但未给出侧信道保证范围。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Motion in the Clear: Reconstructing VR User Behavior from Network Traffic

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/lee-jiho)。
- 判定依据：通过未加密 UDP 载荷字节恢复运动；不能归为加密流量侧信道。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## NeonCROSS: Vectorized Implementation of Post-Quantum Signature CROSS on Cortex-A72 and Apple M3

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i1.250-272)。
- 判定依据：NeonCROSS 优化模约减、矩阵和树哈希的向量执行，摘要未报告侧信道性质。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Non-Interactive Key Exchange from Lattices in the Standard Model

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/li-ying)。
- 判定依据：标准模型格 NIKE 构造与性能；未分析实现泄漏。官方勘误为通讯作者标记。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Nonlocalizable Jamming with Curving Beams

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00253)。
- 判定依据：曲线波束欺骗到达角并干扰无线系统；保留主动物理完整性背景。
- 阅读来源：https://xplorestaging.ieee.org/document/11573486/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Optimistic Asynchronous Dynamic-committee Proactive Secret Sharing

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00243)。
- 判定依据：动态委员会主动秘密分享的复杂度改进；不是连续物理泄漏实验。
- 阅读来源：https://xplorestaging.ieee.org/document/11573576/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

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

## Phoenix: Rowhammer Attacks on DDR5 with Self-Correcting Synchronization

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00083)。
- 判定依据：DDR5 刷新同步支持 Rowhammer 提权；以故障攻击背景保留。
- 阅读来源：https://xplorestaging.ieee.org/document/11573456/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Pipelining FALCON’s Gaussian sampler: Towards practical FALCON acceleration

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i4.447-470)。
- 判定依据：流水化 Falcon SamplerZ 并优化拒绝采样延迟及随机数消耗；摘要没有对采样泄漏或随机源质量给出安全评估，低随机量不自动等于安全。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Quorus: Efficient, Scalable Threshold ML-DSA Signatures from MPC

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/bienstock)。
- 判定依据：可扩展 ML-DSA 阈值 MPC 协议；协议份额安全不等于物理掩码安全。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## RIS-CLA: Reviving CSI-Based Continuous Location Authentication with Reconfigurable Intelligent Surfaces

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00031)。
- 判定依据：可重构表面增强位置认证，主要目标为抗 CSI 猜测；非密码运算泄漏分析。
- 阅读来源：https://xplorestaging.ieee.org/document/11573485/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## RainHash2.0: Hardware- and Arithmetization-friendly Hash Function

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i4.62-115)。
- 判定依据：RainHash2.0 面向二进制域 ZK 电路和硬件效率；证明电路友好性不等于物理泄漏保护。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Recovering and Rehosting Mobile Local LLM Conversations and Contexts via Memory Forensics

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00252)。
- 判定依据：直接读取进程内存/KV cache 进行取证与会话重建；不是计算活动侧信道。
- 阅读来源：https://xplorestaging.ieee.org/document/11573549/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Refined Approx-SVP Rank Reduction Conditions and Adaptive Lattice Reduction for MSIS Security Estimation

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i4.397-422)。
- 判定依据：APBKZ/HeadAPBKZ 研究 Approx-SVP 条件和 MSIS 具体安全估计，属于格求解成本背景。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Revisiting PQ WireGuard: A Comprehensive Security Analysis With a New Design Using Reinforced KEMs

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00057)。
- 判定依据：重新设计 PQ WireGuard 并证明 reinforced KEM 协议性质；无实现侧信道保证。
- 阅读来源：https://xplorestaging.ieee.org/document/11573471/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## SHARMONY: Composing SHA-2 and SHA-3 Hardware for Crypto-Agile PQC

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i4.945-969)。
- 判定依据：SHARMONY 为 SHA-2/SHA-3 共享寄存器与控制逻辑以提高资源效率；标准功能一致性不证明跨算法状态隔离。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## SING: Improving the Efficiency of MPC Protocol Assignment using Graph Neural Networks

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/blueml)。
- 判定依据：GNN 优化 MPC 协议选择；勘误披露 E2 训练集混入比较基准并重训，非侧信道工作。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## SQISign on ARM

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i4.471-495)。
- 判定依据：在 ARM NEON 上向量化 SQIsign 有限域与同源链，结合 Qlapoti 提升性能；摘要没有明确侧信道防护或评估贡献。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## STALEUS: Breaking AMD SEV-SNP via Memory Incoherence

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/schlueter-2)。
- 判定依据：破坏 PSP cache coherence 后获得直接读写；与泄漏推断区分。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## SatBleed: Security of Commoditized Communication Modules in Satellites

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00213)。
- 判定依据：卫星通信模块固件、协议和架构漏洞研究；名称 Bleed 不足以说明侧信道。
- 阅读来源：https://xplorestaging.ieee.org/document/11573399/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Scalable Registration-Based Encryption from Lattices

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00199)。
- 判定依据：格注册加密与密文压缩性能；不含摘要可确认的实现泄漏分析。
- 阅读来源：https://xplorestaging.ieee.org/document/11573539/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Secret State Leakage Attacks and their Impacts on EMV Contactless Payment Apps

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00125)。
- 判定依据：有本地/root 能力的应用秘密状态提取和协议分析；未确认利用时间、功耗或微架构观察。
- 阅读来源：https://xplorestaging.ieee.org/document/11573484/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Secure Lookup Tables: Faster, Leaner, and More General

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00209)。
- 判定依据：恶意安全 MPC 查找表协议；不是 CPU 缓存恒时 LUT 实现。
- 阅读来源：https://xplorestaging.ieee.org/document/11573422/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Shadowfax: Hybrid Security and Deniability for AKEMs

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/gajland)。
- 判定依据：混合 AKEM 的可否认性与实现性能；未分析实现侧信道。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Silicon Heist: (Ransom) Attacks for Cloud FPGAs via Privilege Escalation

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/klix)。
- 判定依据：FPGA ICAP/JTAG 权限提升及配置破坏；不把可重新启用其他攻击当成本文 SCA 结果。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Single-server Stateful PIR with Verifiability and Balanced Efficiency

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00019)。
- 判定依据：PIR 查询隐私及可验证性构造；未给出客户端或服务器执行观察模型。
- 阅读来源：https://xplorestaging.ieee.org/document/11573634/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Sirens' Whisper: Inaudible Near-Ultrasonic Jailbreaks of Speech-Driven LLMs

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/ling)。
- 判定依据：利用麦克风非线性注入近超声指令；主要为输入完整性攻击，非窃听秘密。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Site Isolation is Dead: How Site Isolation is Broken in Agentic Browsers and Extensions

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00241)。
- 判定依据：代理浏览器通过特权 IPC 被提示注入/直接外传；区别于同进程 Spectre 案例。
- 阅读来源：https://xplorestaging.ieee.org/document/11573584/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## SoK: All You Ever Wanted to Know About Bootloader Security But Were Afraid to Ask

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00163)。
- 判定依据：软件引导链漏洞的系统化综述；摘要不建立侧信道覆盖。
- 阅读来源：https://xplorestaging.ieee.org/document/11573574/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## SoK: Security of Cyber-physical Systems Under Intentional Electromagnetic Interference Attacks

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/jiang-qinhong)。
- 判定依据：IEMI 注入与信号操纵综述；相关物理机制保留，未把纯完整性攻击混入 SCA 主库。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## SoK: Systematizing a Decade of Architectural RowHammer Defenses Through the Lens of Streaming Algorithms

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00114)。
- 判定依据：从流式算法整理 Rowhammer 防护，是故障防御综述，不计为侧信道防御。
- 阅读来源：https://xplorestaging.ieee.org/document/11573421/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## StackWarp: Breaking AMD SEV-SNP Integrity via Deterministic Stack-Pointer Manipulation through the CPU's Stack Engine

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/zhang-ruiyi)。
- 判定依据：Stack engine 控制产生架构状态操纵；RSA-CRT 恢复基于完整性破坏，非侧信道读出。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Starfighters—On the General Applicability of X-Wing

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00143)。
- 判定依据：X-Wing/QSF/QSI 的 IND-CCA 与绑定性质；协议组合证明不自动覆盖共享电路泄漏。
- 阅读来源：https://xplorestaging.ieee.org/document/11573402/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

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

## The Person Behind the Sound: Demystifying Audio Private Attribute Profiling via Multimodal Large Language Models

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00150)。
- 判定依据：音频内容的私人属性推断与多模态模型；不计为密码/系统实现观察通道，保留泛隐私背景。
- 阅读来源：https://xplorestaging.ieee.org/document/11573542/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## The Pipes Model for Latency and Throughput Analysis

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00255)。
- 判定依据：分布式协议性能模型；latency/throughput 并非秘密相关时间泄漏分析。
- 阅读来源：https://xplorestaging.ieee.org/document/11573603/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## The Secrets Must Not Flow: Scaling Security Verification to Large Codebases

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00026)。
- 判定依据：Diodon 验证协议核心及应用 I/O 独立性；摘要未把功耗、执行时间或微架构观察纳入保证。
- 阅读来源：https://xplorestaging.ieee.org/document/11573428/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Tracegram: Framing Trace-Level Traffic Analysis with Temporally-Aware Multiple Instance Learning

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/qu)。
- 判定依据：一般跨流量攻击检测与归因，没有建立被加密秘密的旁路恢复。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Trust Nothing: RTOS Security without Run-Time Software TCB

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/ackermann)。
- 判定依据：能力架构隔离 RTOS 与外围设备；摘要未给出侧信道防护模型。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## TÄMU: Emulating Trusted Applications at the (GlobalPlatform)-API Layer

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00139)。
- 判定依据：在 GlobalPlatform API 层重宿主 TEE 应用并模糊测试；重宿主不意味着物理或微架构侧信道保真。
- 阅读来源：https://xplorestaging.ieee.org/document/11573358/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Vectorized Falcon-Sign Implementations using SSE2, AVX2, AVX-512F, NEON, and RVV

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i1.302-324)。
- 判定依据：跨指令集向量化 Falcon BaseSampler 与 FFT/iFFT，报告签名性能；摘要没有采样时序或物理泄漏防护结论。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## WAVED: Principled Identification of Off-Path Exploitable Weak Verifications within the TCP/IP Protocol Suite

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/zhao-yizhou)。
- 判定依据：TCP/IP 弱校验语义漏洞检测；摘要未描述旁路信息恢复。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## What You Decode Depends on Where You Stand: Distance-Based Optical QR Code

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/garg-pulkit)。
- 判定依据：多层 QR 设计与校验器规避，属于有意编码的视觉输入差异，非隐藏秘密泄漏。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## YATA: Yet Another TFHE Accelerator with Key Compression and Radix-8 NTT

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i1.325-352)。
- 判定依据：YATA 芯片压缩 TFHE 自举密钥并优化 NTT；硅片延迟/功耗效率不等于泄漏测试。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## mmCipher: Batching Post-Quantum Public Key Encryption Made Bandwidth-Optimal

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/wang-hongxiao)。
- 判定依据：基于 MLWE 的批量 PKE/KEM 构造；密码学提示不是测量泄漏的同义词。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。
