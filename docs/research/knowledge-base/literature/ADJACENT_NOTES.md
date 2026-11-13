# 已阅读的相邻主题与方法背景

当前 697 条；保留在目录与引用图中，不计入侧信道纳入论文数量。后续全文证据可以修订范围判定。

## Power Analysis Attacks: Revealing the Secrets of Smart Cards

- 来源：[Springer book 2007](https://doi.org/10.1007/978-0-387-38162-6)。
- 判定依据：基础专著的出版商简介及第一版日期已核对，保留相邻参考入口，不将整本书或简介当作近五年研究论文/全文阅读。
- 阅读来源：https://link.springer.com/book/10.1007/978-0-387-38162-6。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## BEARZ Attack FALCON: Implementation Attacks with Countermeasures on the FALCON Signature Scheme

- 来源：[SECRYPT 2019](https://doi.org/10.5220/0007834800610071)。
- 判定依据：主要为 Falcon 故障分析：100% 恢复对应故障后处理模拟；另讨论故障与计时防护成本。未证明完整功耗/EM 实测恢复，保留相邻层。
- 阅读来源：https://eprint.iacr.org/2019/478。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

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

## 50 Shades of Support: A Device-Centric Analysis of Android Security Updates

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/50-shades-of-support-a-device-centric-analysis-of-android-security-updates/)。
- 判定依据：Android 安全更新生命周期与厂商支持差异；摘要未研究侧信道观察。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/50-shades-of-support-a-device-centric-analysis-of-android-security-updates/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## 5G-Spector: An O-RAN Compliant Layer-3 Cellular Attack Detection Service

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/5g-spector-an-o-ran-compliant-layer-3-cellular-attack-detection-service/)。
- 判定依据：O-RAN L3 网络遥测与入侵检测；未报告利用非预期泄漏推断秘密。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/5g-spector-an-o-ran-compliant-layer-3-cellular-attack-detection-service/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## A Configurable ML-KEM/Kyber Key-Encapsulation Hardware Accelerator Architecture

- 来源：[TCAS-II 2024](https://doi.org/10.1109/tcsii.2024.3442228)。
- 判定依据：ML-KEM/Kyber 加速器资源与性能比较；摘要未给出物理泄漏评价，题名不能证明最终 FIPS 203 完整一致性。
- 阅读来源：https://xplorestaging.ieee.org/document/10634219/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## A Duty to Forget, a Right to be Assured? Exposing Vulnerabilities in Machine Unlearning Services

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/a-duty-to-forget-a-right-to-be-assured-exposing-vulnerabilities-in-machine-unlearning-services/)。
- 判定依据：过度机器遗忘造成模型效用下降；不是侧信道观测或密钥恢复。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/a-duty-to-forget-a-right-to-be-assured-exposing-vulnerabilities-in-machine-unlearning-services/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## A Highly-efficient Lattice-based Post-Quantum Cryptography Processor for IoT Applications

- 来源：[TCHES 2024](https://doi.org/10.46586/tches.v2024.i2.130-153)。
- 判定依据：以 SIMD、双发射访存及资源复用改善 Kyber/Dilithium 处理器 PPAP；平均功耗改善不证明抗功耗分析。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## A Security and Usability Analysis of Local Attacks Against FIDO2

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/a-security-and-usability-analysis-of-local-attacks-against-fido2/)。
- 判定依据：FIDO2 扩展/XSS、物理令牌与协议/UX 缺陷；摘要研究消息访问、克隆检测和 cookie，而非实现侧信道。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/a-security-and-usability-analysis-of-local-attacks-against-fido2/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## A Systematic Study of Physical Sensor Attack Hardness

- 来源：[SP 2024](https://www.ieee-security.org/TC/SP2024/accepted-papers.html)。
- 判定依据：研究机器人传感器注入攻击的前提和成功难度，主要是主动完整性/安全性破坏；摘要未建立秘密经侧信道泄漏的关系。作为物理攻击前提分析方法保留。
- 阅读来源：https://xplorestaging.ieee.org/document/10646778/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## A Two-Layer Blockchain Sharding Protocol Leveraging Safety and Liveness for Enhanced Performance

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/a-two-layer-blockchain-sharding-protocol-leveraging-safety-and-liveness-for-enhanced-performance/)。
- 判定依据：区块链分片的安全性与活性；不属于测量泄漏研究。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/a-two-layer-blockchain-sharding-protocol-leveraging-safety-and-liveness-for-enhanced-performance/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## A Unified Symbolic Analysis of WireGuard

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/a-unified-symbolic-analysis-of-wireguard/)。
- 判定依据：WireGuard 协议匿名性与符号分析；摘要未建立物理泄漏模型。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/a-unified-symbolic-analysis-of-wireguard/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## AAKA: An Anti-Tracking Cellular Authentication Scheme Leveraging Anonymous Credentials

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/aaka-an-anti-tracking-cellular-authentication-scheme-leveraging-anonymous-credentials/)。
- 判定依据：匿名凭据与蜂窝认证的身份不可链接协议；摘要未分析额外时序/物理/流量侧信道，保留协议隐私背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/aaka-an-anti-tracking-cellular-authentication-scheme-leveraging-anonymous-credentials/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Abusing the Ethereum Smart Contract Verification Services for Fun and Profit

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/abusing-the-ethereum-smart-contract-verification-services-for-fun-and-profit/)。
- 判定依据：智能合约源码/字节码验证缺陷；直接验证逻辑问题不作为侧信道结果。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/abusing-the-ethereum-smart-contract-verification-services-for-fun-and-profit/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## ActiveDaemon: Unconscious DNN Dormancy and Waking Up via User-specific Invisible Token

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/activedaemon-unconscious-dnn-dormancy-and-waking-up-via-user-specific-invisible-token/)。
- 判定依据：DNN 访问令牌与后门式产权认证；不是被动测量泄漏。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/activedaemon-unconscious-dnn-dormancy-and-waking-up-via-user-specific-invisible-token/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## AnonPSI: An Anonymity Assessment Framework for PSI

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/anonpsi-an-anonymity-assessment-framework-for-psi/)。
- 判定依据：多次 PSI 及 PSI-SUM 的既定输出造成集合成员推断；属于输出隐私与组合背景，不据此认定实现泄漏。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/anonpsi-an-anonymity-assessment-framework-for-psi/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## AquaSonic: Acoustic Manipulation of Underwater Data Center Operations and Resource Management

- 来源：[SP 2024](https://www.ieee-security.org/TC/SP2024/accepted-papers.html)。
- 判定依据：水下声学注入使存储、分布式系统和调度降级，摘要核心是可用性与资源操纵；未证明通过观察间接信号恢复秘密，作为物理注入背景保留。
- 阅读来源：https://xplorestaging.ieee.org/document/10646672/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Architecting Trigger-Action Platforms for Security, Performance and Functionality

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/architecting-trigger-action-platforms-for-security-performance-and-functionality/)。
- 判定依据：TAPDance/Keystone enclave 架构与隔离；摘要未给出侧信道评估。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/architecting-trigger-action-platforms-for-security-performance-and-functionality/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Attributions for ML-based ICS Anomaly Detection: From Theory to Practice

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/attributions-for-ml-based-ics-anomaly-detection-from-theory-to-practice/)。
- 判定依据：工业控制故障/攻击归因诊断；不以秘密的侧信道推断为贡献。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/attributions-for-ml-based-ics-anomaly-detection-from-theory-to-practice/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Automatic Adversarial Adaption for Stealthy Poisoning Attacks in Federated Learning

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/automatic-adversarial-adaption-for-stealthy-poisoning-attacks-in-federated-learning/)。
- 判定依据：联邦学习中自适应投毒；约束的是恶意模型更新，不是物理泄漏。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/automatic-adversarial-adaption-for-stealthy-poisoning-attacks-in-federated-learning/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Automatic Policy Synthesis and Enforcement for Protecting Untrusted Deserialization

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/automatic-policy-synthesis-and-enforcement-for-protecting-untrusted-deserialization/)。
- 判定依据：反序列化策略自动合成；直接软件缺陷防护。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/automatic-policy-synthesis-and-enforcement-for-protecting-untrusted-deserialization/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## BGP-iSec: Improved Security of Internet Routing Against Post-ROV Attacks

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/bgp-isec-improved-security-of-internet-routing-against-post-rov-attacks/)。
- 判定依据：BGP-iSec 的路由泄漏指路由策略传播；与物理或微架构泄漏不同。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/bgp-isec-improved-security-of-internet-routing-against-post-rov-attacks/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Bernoulli Honeywords

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/bernoulli-honeywords/)。
- 判定依据：Bernoulli honeywords 通过诱饵检测账户泄露；不是硬件侧信道防护。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/bernoulli-honeywords/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Beyond the Surface: Uncovering the Unprotected Components of Android Against Overlay Attack

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/beyond-the-surface-uncovering-the-unprotected-components-of-android-against-overlay-attack/)。
- 判定依据：Android 叠层与点击劫持；不作为测量型侧信道攻击。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/beyond-the-surface-uncovering-the-unprotected-components-of-android-against-overlay-attack/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

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

## BreakSPF: How Shared Infrastructures Magnify SPF Vulnerabilities Across the Internet

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/breakspf-how-shared-infrastructures-magnify-spf-vulnerabilities-across-the-internet/)。
- 判定依据：共享 IP 下 SPF 身份认证绕过；直接认证逻辑问题。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/breakspf-how-shared-infrastructures-magnify-spf-vulnerabilities-across-the-internet/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## CAGE: Complementing Arm CCA with GPU Extensions

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/cage-complementing-arm-cca-with-gpu-extensions/)。
- 判定依据：Arm CCA 的 GPU 机密执行、内存隔离与工作流支持；摘要无具体侧信道机制或保护保证。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/cage-complementing-arm-cca-with-gpu-extensions/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## CASA: A Compact and Scalable Accelerator for Approximate Homomorphic Encryption

- 来源：[TCHES 2024](https://doi.org/10.46586/tches.v2024.i2.451-480)。
- 判定依据：CASA 优化 CKKS 算法、模块及 FPGA 架构；功耗延迟积与隐私协议保证不能代替泄漏证据。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## CamPro: Camera-based Anti-Facial Recognition

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/campro-camera-based-anti-facial-recognition/)。
- 判定依据：修改 ISP 参数保护摄像图像的人脸隐私，研究正常图像输出，不是 EM 或其他旁路观察。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/campro-camera-based-anti-facial-recognition/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Carry Your Fault: A Fault Propagation Attack on Side-Channel Protected LWE-based KEM

- 来源：[TCHES 2024](https://doi.org/10.46586/tches.v2024.i2.844-869)。
- 判定依据：攻击掩码为实现便利而引入的 A2B 进位传播，含 Kyber 模拟和 STM32 EM 故障验证；保留掩码与故障交互，任意阶原理不等于所有阶数已实测。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Certificate Transparency Revisited: The Public Inspections on Third-party Monitors

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/certificate-transparency-revisited-the-public-inspections-on-third-party-monitors/)。
- 判定依据：证书透明日志的监视器一致性检查；未建立秘密侧信道观察。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/certificate-transparency-revisited-the-public-inspections-on-third-party-monitors/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Compensating Removed Frequency Components: Thwarting Voice Spectrum Reduction Attacks

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/compensating-removed-frequency-components-thwarting-voice-spectrum-reduction-attacks/)。
- 判定依据：补偿对抗音频被删去的频率成分；spectral leakage 在这里是信号处理术语，不是密码信息侧漏。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/compensating-removed-frequency-components-thwarting-voice-spectrum-reduction-attacks/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Compromising Industrial Processes using Web-Based Programmable Logic Controller Malware

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/compromising-industrial-processes-using-web-based-programmable-logic-controller-malware/)。
- 判定依据：PLC Web 恶意软件直接调用接口控制工业过程；不等于被动波形泄漏。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/compromising-industrial-processes-using-web-based-programmable-logic-controller-malware/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Content Censorship in the InterPlanetary File System

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/content-censorship-in-the-interplanetary-file-system/)。
- 判定依据：IPFS 内容审查与 DHT 可用性；保留网络背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/content-censorship-in-the-interplanetary-file-system/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

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

## Crafter: Facial Feature Crafting against Inversion-based Identity Theft on Deep Models

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/crafter-facial-feature-crafting-against-inversion-based-identity-theft-on-deep-models/)。
- 判定依据：人脸特征反演与隐私防护；属于模型隐私相邻研究，未建立物理侧信道。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/crafter-facial-feature-crafting-against-inversion-based-identity-theft-on-deep-models/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## CrowdGuard: Federated Backdoor Detection in Federated Learning

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/crowdguard-federated-backdoor-detection-in-federated-learning/)。
- 判定依据：CrowdGuard 联邦后门检测采用 TEE；使用 TEE 本身不构成侧信道防护评估。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/crowdguard-federated-backdoor-detection-in-federated-learning/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## DEMASQ: Unmasking the ChatGPT Wordsmith

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/demasq-unmasking-the-chatgpt-wordsmith/)。
- 判定依据：DEMASQ 的 energy 与 Doppler 类比服务于文本检测；不是设备功耗测量。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/demasq-unmasking-the-chatgpt-wordsmith/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## DRAINCLoG: Detecting Rogue Accounts with Illegally-obtained NFTs using Classifiers Learned on Graphs

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/drainclog-detecting-rogue-accounts-with-illegally-obtained-nfts-using-classifiers-learned-on-graphs/)。
- 判定依据：NFT drainer 公共交易图分析；直接公开记录分析。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/drainclog-detecting-rogue-accounts-with-illegally-obtained-nfts-using-classifiers-learned-on-graphs/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## DeGPT: Optimizing Decompiler Output with LLM

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/degpt-optimizing-decompiler-output-with-llm/)。
- 判定依据：DeGPT 通过多个 LLM 角色改善反编译可读性；可作研究工具背景，非侧信道证据。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/degpt-optimizing-decompiler-output-with-llm/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Decentralized Information-Flow Control for ROS2

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/decentralized-information-flow-control-for-ros2/)。
- 判定依据：ROS2 数据消费权限与 ABE 信息流控制，摘要未给物理或微架构侧信道分析。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/decentralized-information-flow-control-for-ros2/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## DeepGo: Predictive Directed Greybox Fuzzing

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/deepgo-predictive-directed-greybox-fuzzing/)。
- 判定依据：DeepGo 强化学习引导模糊测试；方法背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/deepgo-predictive-directed-greybox-fuzzing/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Detecting Voice Cloning Attacks via Timbre Watermarking

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/detecting-voice-cloning-attacks-via-timbre-watermarking/)。
- 判定依据：语音水印用于主动产权标记；不是非预期泄漏。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/detecting-voice-cloning-attacks-via-timbre-watermarking/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Don’t Interrupt Me – A Large-Scale Study of On-Device Permission Prompt Quieting in Chrome

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/dont-interrupt-me-a-large-scale-study-of-on-device-permission-prompt-quieting-in-chrome/)。
- 判定依据：Chrome 权限提示界面与用户行为；非侧信道研究。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/dont-interrupt-me-a-large-scale-study-of-on-device-permission-prompt-quieting-in-chrome/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## DorPatch: Distributed and Occlusion-Robust Adversarial Patch to Evade Certifiable Defenses

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/dorpatch-distributed-and-occlusion-robust-adversarial-patch-to-evade-certifiable-defenses/)。
- 判定依据：对抗补丁鲁棒性；主动输入攻击与被动观测不同。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/dorpatch-distributed-and-occlusion-robust-adversarial-patch-to-evade-certifiable-defenses/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## DynPRE: Protocol Reverse Engineering via Dynamic Inference

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/dynpre-protocol-reverse-engineering-via-dynamic-inference/)。
- 判定依据：DynPRE 用交互式消息推断协议格式；显式协议内容分析，不是物理侧信道。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/dynpre-protocol-reverse-engineering-via-dynamic-inference/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

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

## Efficient Use-After-Free Prevention with Opportunistic Page-Level Sweeping

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/efficient-use-after-free-prevention-with-opportunistic-page-level-sweeping/)。
- 判定依据：内存分配器缓解 UAF；摘要未主张秘密推断或侧信道评估。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/efficient-use-after-free-prevention-with-opportunistic-page-level-sweeping/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Efficient and Timely Revocation of V2X Credentials

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/efficient-and-timely-revocation-of-v2x-credentials/)。
- 判定依据：V2X 凭据撤销与 Tamarin 协议验证；仿真网络时延不属于秘密时序泄漏分析。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/efficient-and-timely-revocation-of-v2x-credentials/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

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

## EnclaveFuzz: Finding Vulnerabilities in SGX Applications

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/enclavefuzz-finding-vulnerabilities-in-sgx-applications/)。
- 判定依据：EnclaveFuzz 面向 SGX 内存与 TOCTOU 缺陷；与侧信道机理分开。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/enclavefuzz-finding-vulnerabilities-in-sgx-applications/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Enhance Stealthiness and Transferability of Adversarial Attacks with Class Activation Mapping Ensemble Attack

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/enhance-stealthiness-and-transferability-of-adversarial-attacks-with-class-activation-mapping-ensemble-attack/)。
- 判定依据：基于类激活图的对抗样本检测；模型鲁棒性背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/enhance-stealthiness-and-transferability-of-adversarial-attacks-with-class-activation-mapping-ensemble-attack/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Experimental Analyses of the Physical Surveillance Risks in Client-Side Content Scanning

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/experimental-analyses-of-the-physical-surveillance-risks-in-client-side-content-scanning/)。
- 判定依据：通过投毒感知哈希数据库使客户端内容扫描监视特定场景；physical surveillance 是监视目标，不是物理侧信道。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/experimental-analyses-of-the-physical-surveillance-risks-in-client-side-content-scanning/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Facilitating Non-Intrusive In-Vivo Firmware Testing with Stateless Instrumentation

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/facilitating-non-intrusive-in-vivo-firmware-testing-with-stateless-instrumentation/)。
- 判定依据：非侵入式固件插桩与测试；不是对密码运行的被动测量攻击。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/facilitating-non-intrusive-in-vivo-firmware-testing-with-stateless-instrumentation/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

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

## Faster and Better: Detecting Vulnerabilities in Linux-based IoT Firmware with Optimized Reaching Definition Analysis

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/faster-and-better-detecting-vulnerabilities-in-linux-based-iot-firmware-with-optimized-reaching-definition-analysis/)。
- 判定依据：IoT 静态污点分析；代码分析方法背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/faster-and-better-detecting-vulnerabilities-in-linux-based-iot-firmware-with-optimized-reaching-definition-analysis/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Faults in Our Bus: Novel Bus Fault Attack to Break ARM TrustZone

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/faults-in-our-bus-novel-bus-fault-attack-to-break-arm-trustzone/)。
- 判定依据：主动总线 EM 故障导致可访问崩溃转储，读取 Dilithium 密钥或 Saber/Kyber 全部份额；另有 TrustZone 组合链。保留为 PQC 故障与系统边界背景，不标为被动功耗攻击。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/faults-in-our-bus-novel-bus-fault-attack-to-break-arm-trustzone/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## File Hijacking Vulnerability: The Elephant in the Room

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/file-hijacking-vulnerability-the-elephant-in-the-room/)。
- 判定依据：文件劫持漏洞；直接资源替换问题。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/file-hijacking-vulnerability-the-elephant-in-the-room/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## FreqFed: A Frequency Analysis-Based Approach for Mitigating Poisoning Attacks in Federated Learning

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/freqfed-a-frequency-analysis-based-approach-for-mitigating-poisoning-attacks-in-federated-learning/)。
- 判定依据：FreqFed 的频率分析对象是模型权重；不等于处理器频率泄漏。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/freqfed-a-frequency-analysis-based-approach-for-mitigating-poisoning-attacks-in-federated-learning/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## From Hardware Fingerprint to Access Token: Enhancing the Authentication on IoT Devices

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/from-hardware-fingerprint-to-access-token-enhancing-the-authentication-on-iot-devices/)。
- 判定依据：MCU 指纹作为主动认证令牌，并通过混入数据对抗模仿；摘要未显示窃取密码秘密的额外观察机制，保留硬件指纹/建模背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/from-hardware-fingerprint-to-access-token-enhancing-the-authentication-on-iot-devices/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## From Interaction to Independence: zkSNARKs for Transparent and Non-Interactive Remote Attestation

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/from-interaction-to-independence-zksnarks-for-transparent-and-non-interactive-remote-attestation/)。
- 判定依据：zkSNARK 远程证明的公开验证与零知识协议；没有据摘要建立物理泄漏安全。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/from-interaction-to-independence-zksnarks-for-transparent-and-non-interactive-remote-attestation/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Front-running Attack in Sharded Blockchains and Fair Cross-shard Consensus

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/front-running-attack-in-sharded-blockchains-and-fair-cross-shard-consensus/)。
- 判定依据：区块链抢跑与交易排序；协议层可见信息背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/front-running-attack-in-sharded-blockchains-and-fair-cross-shard-consensus/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## GNNIC: Finding Long-Lost Sibling Functions with Abstract Similarity

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/gnnic-finding-long-lost-sibling-functions-with-abstract-similarity/)。
- 判定依据：GNN 间接调用目标分析；可用于实现理解，非侧信道结果。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/gnnic-finding-long-lost-sibling-functions-with-abstract-similarity/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## GhostType: The Limits of Using Contactless Electromagnetic Interference to Inject Phantom Keys into Analog Circuits of Keyboards

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/ghosttype-the-limits-of-using-contactless-electromagnetic-interference-to-inject-phantom-keys-into-analog-circuits-of-keyboards/)。
- 判定依据：接触外 EMI 注入键盘 GPIO 造成幻键，属于输入完整性攻击，不是监听按键。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/ghosttype-the-limits-of-using-contactless-electromagnetic-interference-to-inject-phantom-keys-into-analog-circuits-of-keyboards/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Gradient Shaping: Enhancing Backdoor Attack Against Reverse Engineering

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/gradient-shaping-enhancing-backdoor-attack-against-reverse-engineering/)。
- 判定依据：GRASP 后门与梯度反演；模型隐私/攻击背景，不计为物理侧信道。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/gradient-shaping-enhancing-backdoor-attack-against-reverse-engineering/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## GraphGuard: Detecting and Counteracting Training Data Misuse in Graph Neural Networks

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/graphguard-detecting-and-counteracting-training-data-misuse-in-graph-neural-networks/)。
- 判定依据：GraphGuard 的数据成员检测与遗忘；模型隐私相邻主题。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/graphguard-detecting-and-counteracting-training-data-misuse-in-graph-neural-networks/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Group-based Robustness: A General Framework for Customized Robustness in the Real World

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/group-based-robustness-a-general-framework-for-customized-robustness-in-the-real-world/)。
- 判定依据：分组对抗鲁棒性指标；没有独立侧信道测量贡献。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/group-based-robustness-a-general-framework-for-customized-robustness-in-the-real-world/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Guessing on Dominant Paths: Understanding the Limitation of Wireless Authentication Using Channel State Information

- 来源：[SP 2024](https://www.ieee-security.org/TC/SP2024/accepted-papers.html)。
- 判定依据：CSI 猜测和预编码用于伪装合法无线身份，属于主动认证绕过；摘要未说明受保护计算经额外观察泄漏，作为物理层认证背景保留。
- 阅读来源：https://xplorestaging.ieee.org/document/10646746/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## HEIR: A Unified Representation for Cross-Scheme Compilation of Fully Homomorphic Computation

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/heir-a-unified-representation-for-cross-scheme-compilation-of-fully-homomorphic-computation/)。
- 判定依据：HEIR 跨 FHE 方案编译与性能优化；不以抽象同态隐私代替实现侧信道保护。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/heir-a-unified-representation-for-cross-scheme-compilation-of-fully-homomorphic-computation/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

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

## IDA: Hybrid Attestation with Support for Interrupts and TOCTOU

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/ida-hybrid-attestation-with-support-for-interrupts-and-toctou/)。
- 判定依据：可信硬件监测远程证明流程、处理中断和 TOCTOU；摘要是完整性保障。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/ida-hybrid-attestation-with-support-for-interrupts-and-toctou/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## INTFAIL: Using Spurious #VC Interrupts to Break AMD SEV-SNP

- 来源：[SP 2024](https://www.ieee-security.org/TC/SP2024/accepted-papers.html)。
- 判定依据：出版题名为 WeSee；恶意 hypervisor 注入 #VC 诱导寄存器/内存复制和任意行为，属于异常处理与完整性攻击。直接拷出 kTLS key 不自动构成侧信道推断；作为 TEE 威胁模型背景保留。
- 阅读来源：https://xplorestaging.ieee.org/document/10646722/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## IRRedicator: Pruning IRR with RPKI-Valid BGP Insights

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/irredicator-pruning-irr-with-rpki-valid-bgp-insights/)。
- 判定依据：RPKI/IRR 过期对象分类；网络配置背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/irredicator-pruning-irr-with-rpki-valid-bgp-insights/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Impeccable Keccak: Towards Fault Resilient SPHINCS+ Implementations

- 来源：[TCHES 2024](https://doi.org/10.46586/tches.v2024.i2.154-189)。
- 判定依据：为 SPHINCS+ 的 Keccak 提出 impeccable 电路与主动安全分析，给出指定位翻转模型的检测保证；这不是功耗掩码安全证明，也不是任意故障模型保证。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Improving the Robustness of Transformer-based Large Language Models with Dynamic Attention

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/improving-the-robustness-of-transformer-based-large-language-models-with-dynamic-attention/)。
- 判定依据：LLM 动态注意力与鲁棒性；非泄漏测量。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/improving-the-robustness-of-transformer-based-large-language-models-with-dynamic-attention/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Inaudible Adversarial Perturbation: Manipulating the Recognition of User Speech in Real Time

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/inaudible-adversarial-perturbation-manipulating-the-recognition-of-user-speech-in-real-time/)。
- 判定依据：超声波输入注入干扰 ASR；主动感知攻击，不等于语音窃听。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/inaudible-adversarial-perturbation-manipulating-the-recognition-of-user-speech-in-real-time/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Information Based Heavy Hitters for Real-Time DNS Data Exfiltration Detection

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/information-based-heavy-hitters-for-real-time-dns-data-exfiltration-detection/)。
- 判定依据：估计 DNS 域名传输信息量以检测外传；正常协议内容中的隧道检测，不是秘密状态旁路推断。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/information-based-heavy-hitters-for-real-time-dns-data-exfiltration-detection/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Invisible Reflections: Leveraging Infrared Laser Reflections to Target Traffic Sign Perception

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/invisible-reflections-leveraging-infrared-laser-reflections-to-target-traffic-sign-perception/)。
- 判定依据：红外激光反射欺骗交通标志感知；主动光学输入攻击。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/invisible-reflections-leveraging-infrared-laser-reflections-to-target-traffic-sign-perception/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## K-LEAK: Towards Automating the Generation of Multi-Step Infoleak Exploits against the Linux Kernel

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/k-leak-towards-automating-the-generation-of-multi-step-infoleak-exploits-against-the-linux-kernel/)。
- 判定依据：内核内存错误的多步直接信息泄露与数据流搜索，不是缓存或功耗旁路。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/k-leak-towards-automating-the-generation-of-multi-step-infoleak-exploits-against-the-linux-kernel/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## LDR: Secure and Efficient Linux Driver Runtime for Embedded TEE Systems

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/ldr-secure-and-efficient-linux-driver-runtime-for-embedded-tee-systems/)。
- 判定依据：TEE Linux 驱动运行时、隔离与控制流完整性；摘要没有侧信道评价。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/ldr-secure-and-efficient-linux-driver-runtime-for-embedded-tee-systems/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## LMSanitator: Defending Prompt-Tuning Against Task-Agnostic Backdoors

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/lmsanitator-defending-prompt-tuning-against-task-agnostic-backdoors/)。
- 判定依据：LMSanitator 模型后门防护；摘要未建立侧信道观测。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/lmsanitator-defending-prompt-tuning-against-task-agnostic-backdoors/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Large Language Model guided Protocol Fuzzing

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/large-language-model-guided-protocol-fuzzing/)。
- 判定依据：ChatAFL 使用 LLM 生成协议语法与测试输入；可作实验工具背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/large-language-model-guided-protocol-fuzzing/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Leaking the Privacy of Groups and More: Understanding Privacy Risks of Cross-App Content Sharing in Mobile Ecosystem

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/leaking-the-privacy-of-groups-and-more-understanding-privacy-risks-of-cross-app-content-sharing-in-mobile-ecosystem/)。
- 判定依据：跨应用共享标识和内容直接暴露身份与社会关系；保留隐私背景，未证明独立侧信道。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/leaking-the-privacy-of-groups-and-more-understanding-privacy-risks-of-cross-app-content-sharing-in-mobile-ecosystem/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## LiDAR Spoofing Meets the New-Gen: Capability Improvements, Broken Assumptions, and New Attack Strategies

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/lidar-spoofing-meets-the-new-gen-capability-improvements-broken-assumptions-and-new-attack-strategies/)。
- 判定依据：LiDAR 激光注入与目标检测完整性，属于物理欺骗。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/lidar-spoofing-meets-the-new-gen-capability-improvements-broken-assumptions-and-new-attack-strategies/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Like, Comment, Get Scammed: Characterizing Comment Scams on Media Platforms

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/like-comment-get-scammed-characterizing-comment-scams-on-media-platforms/)。
- 判定依据：YouTube 评论诈骗；内容生态研究。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/like-comment-get-scammed-characterizing-comment-scams-on-media-platforms/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## LoRDMA: A New Low-Rate DoS Attack in RDMA Networks

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/lordma-a-new-low-rate-dos-attack-in-rdma-networks/)。
- 判定依据：LoRDMA 用 RTT 反馈安排低速 DoS；有时序测量，但未建立秘密推断目标。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/lordma-a-new-low-rate-dos-attack-in-rdma-networks/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## MOCK: Optimizing Kernel Fuzzing Mutation with Context-aware Dependency

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/mock-optimizing-kernel-fuzzing-mutation-with-context-aware-dependency/)。
- 判定依据：MOCK 利用上下文改进内核模糊测试；方法背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/mock-optimizing-kernel-fuzzing-mutation-with-context-aware-dependency/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## MPCDiff: Testing and Repairing MPC-Hardened Deep Learning Models

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/mpcdiff-testing-and-repairing-mpc-hardened-deep-learning-models/)。
- 判定依据：MPC 模型与明文模型的差分正确性测试和修复，非侧信道。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/mpcdiff-testing-and-repairing-mpc-hardened-deep-learning-models/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## MadRadar: A Black-Box Physical Layer Attack Framework on mmWave Automotive FMCW Radars

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/madradar-a-black-box-physical-layer-attack-framework-on-mmwave-automotive-fmcw-radars/)。
- 判定依据：先估计雷达配置再进行信号注入，目标是点云完整性；保留测量与干预背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/madradar-a-black-box-physical-layer-attack-framework-on-mmwave-automotive-fmcw-radars/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Maginot Line: Assessing a New Cross-app Threat to PII-as-Factor Authentication in Chinese Mobile Apps

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/maginot-line-assessing-a-new-cross-app-threat-to-pii-as-factor-authentication-in-chinese-mobile-apps/)。
- 判定依据：PaFA 跨应用 PII 认证绕过；直接授权/数据访问缺陷。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/maginot-line-assessing-a-new-cross-app-threat-to-pii-as-factor-authentication-in-chinese-mobile-apps/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

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

## Modeling and Detecting Internet Censorship Events

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/modeling-and-detecting-internet-censorship-events/)。
- 判定依据：识别测量数据中的网络阻断事件，不是从额外观察推断密码秘密或私密行为。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/modeling-and-detecting-internet-censorship-events/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## More Haste, Less Speed: Cache Related Security Threats in Continuous Integration Services

- 来源：[SP 2024](https://www.ieee-security.org/TC/SP2024/accepted-papers.html)。
- 判定依据：CI cache 指依赖包缓存对象的隔离、投毒和直接敏感文件暴露；不是 CPU cache 时序侧信道。作为跨信任域缓存设计背景保留。
- 阅读来源：https://xplorestaging.ieee.org/document/10646699/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## NODLINK: An Online System for Fine-Grained APT Attack Detection and Investigation

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/nodlink-an-online-system-for-fine-grained-apt-attack-detection-and-investigation/)。
- 判定依据：NodLink 基于溯源图检测 APT；不是秘密侧信道恢复。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/nodlink-an-online-system-for-fine-grained-apt-attack-detection-and-investigation/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## New Security Proofs and Techniques for Hash-and-Sign with Retry Signature Schemes

- 来源：[IACR ePrint 2024](https://eprint.iacr.org/2024/609)。
- 判定依据：实际被引 ePrint 2024/609 研究 Hash-and-Sign with Retry 的经典安全界，应用于 MAYO/PROV/修改 UOV；是安全证明背景，没有物理观察验证，不能当作更紧量子安全界。
- 阅读来源：https://eprint.iacr.org/2024/609。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

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

## Not your Type! Detecting Storage Collision Vulnerabilities in Ethereum Smart Contracts

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/not-your-type-detecting-storage-collision-vulnerabilities-in-ethereum-smart-contracts/)。
- 判定依据：CRUSH 合约存储碰撞；程序语义/内存布局缺陷。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/not-your-type-detecting-storage-collision-vulnerabilities-in-ethereum-smart-contracts/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## ORL-AUDITOR: Dataset Auditing in Offline Deep Reinforcement Learning

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/orl-auditor-dataset-auditing-in-offline-deep-reinforcement-learning/)。
- 判定依据：利用 DRL 累积奖励进行训练数据审计，属于模型输出成员推断。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/orl-auditor-dataset-auditing-in-offline-deep-reinforcement-learning/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## One Vector to Rule Them All: Key Recovery from One Vector in UOV Schemes

- 来源：[PQCrypto 2024](https://doi.org/10.1007/978-3-031-62746-0_5)。
- 判定依据：给定 oil 子空间向量后的代数密钥恢复，保留为侧信息后处理的相邻理论；摘要没有证明从波形获取该向量。正式摘要为最多 13 秒，ePrint 页面写 15 秒，版本差异未消除，不能混用数值。
- 阅读来源：https://link.springer.com/chapter/10.1007/978-3-031-62746-0_5。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Optimized Hardware-Software Co-Design for Kyber and Dilithium on RISC-V SoC FPGA

- 来源：[TCHES 2024](https://doi.org/10.46586/tches.v2024.i3.99-135)。
- 判定依据：RISC-V SoC 上以多核、硬件乘法及汇编哈希加速 Kyber/Dilithium，摘要未评价泄漏。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Overconfidence is a Dangerous Thing: Mitigating Membership Inference Attacks by Enforcing Less Confident Prediction

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/overconfidence-is-a-dangerous-thing-mitigating-membership-inference-attacks-by-enforcing-less-confident-prediction/)。
- 判定依据：以置信度和训练正则减轻模型输出的成员推断，未给实现侧信道机制。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/overconfidence-is-a-dangerous-thing-mitigating-membership-inference-attacks-by-enforcing-less-confident-prediction/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Pandora: Principled Symbolic Validation of Intel SGX Enclave Runtimes

- 来源：[SP 2024](https://www.ieee-security.org/TC/SP2024/accepted-papers.html)。
- 判定依据：Pandora 对 SGX shielding runtime 的污点、符号内存及漏洞位置做验证；摘要未完整说明四类插件的侧信道性质，暂作实现验证背景，保留正文范围复核。
- 阅读来源：https://xplorestaging.ieee.org/document/10646841/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Parrot-Trained Adversarial Examples: Pushing the Practicality of Black-Box Audio Attacks against Speaker Recognition Models

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/parrot-trained-adversarial-examples-pushing-the-practicality-of-black-box-audio-attacks-against-speaker-recognition-models/)。
- 判定依据：鹦鹉语音式对抗输入；不是被动声音侧信道。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/parrot-trained-adversarial-examples-pushing-the-practicality-of-black-box-audio-attacks-against-speaker-recognition-models/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Pencil: Private and Extensible Collaborative Learning without the Non-Colluding Assumption

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/pencil-private-and-extensible-collaborative-learning-without-the-non-colluding-assumption/)。
- 判定依据：MPC 协作学习的模型/数据隐私与非串谋假设，未给物理观察分析。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/pencil-private-and-extensible-collaborative-learning-without-the-non-colluding-assumption/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Phoenix: Surviving Unpatched Vulnerabilities via Accurate and Efficient Filtering of Syscall Sequences

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/phoenix-surviving-unpatched-vulnerabilities-via-accurate-and-efficient-filtering-of-syscall-sequences/)。
- 判定依据：Phoenix 系统调用过滤；系统防护背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/phoenix-surviving-unpatched-vulnerabilities-via-accurate-and-efficient-filtering-of-syscall-sequences/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Pisces: Private and Compliable Cryptocurrency Exchange

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/pisces-private-and-compliable-cryptocurrency-exchange/)。
- 判定依据：Pisces 交易匿名性协议；未评估物理泄漏。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/pisces-private-and-compliable-cryptocurrency-exchange/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Powers of Tau in Asynchrony

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/powers-of-tau-in-asynchrony/)。
- 判定依据：Powers of Tau 多方参数生成；名称中的 power 与功耗无关。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/powers-of-tau-in-asynchrony/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Predictive Context-sensitive Fuzzing

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/predictive-context-sensitive-fuzzing/)。
- 判定依据：上下文敏感模糊测试；实验方法背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/predictive-context-sensitive-fuzzing/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## PriSrv: Privacy-Enhanced and Highly Usable Service Discovery in Wireless Communications

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/prisrv-privacy-enhanced-and-highly-usable-service-discovery-in-wireless-communications/)。
- 判定依据：匿名凭据与服务发现协议隐私；摘要没有独立旁路观察实验。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/prisrv-privacy-enhanced-and-highly-usable-service-discovery-in-wireless-communications/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Private Aggregate Queries to Untrusted Databases

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/private-aggregate-queries-to-untrusted-databases/)。
- 判定依据：私有聚合查询的 IT-PIR 功能与通信效率，保留查询隐私背景；未给实现侧信道分析。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/private-aggregate-queries-to-untrusted-databases/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Proof of Backhaul: Trustfree Measurement of Broadband Bandwidth

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/proof-of-backhaul-trustfree-measurement-of-broadband-bandwidth/)。
- 判定依据：Proof of Backhaul 验证网络带宽；度量性能不等于推断秘密。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/proof-of-backhaul-trustfree-measurement-of-broadband-bandwidth/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## QUACK: Hindering Deserialization Attacks via Static Duck Typing

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/quack-hindering-deserialization-attacks-via-static-duck-typing/)。
- 判定依据：QUACK 静态鸭子类型防止反序列化攻击；直接软件防护。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/quack-hindering-deserialization-attacks-via-static-duck-typing/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## REPLICAWATCHER: Training-less Anomaly Detection in Containerized Microservices

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/replicawatcher-training-less-anomaly-detection-in-containerized-microservices/)。
- 判定依据：ReplicaWatcher 比较副本行为检测异常；没有独立秘密推断模型。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/replicawatcher-training-less-anomaly-detection-in-containerized-microservices/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## ReqsMiner: Automated Discovery of CDN Forwarding Request Inconsistencies and DoS Attacks with Grammar-based Fuzzing

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/reqsminer-automated-discovery-of-cdn-forwarding-request-inconsistencies-and-dos-attacks-with-grammar-based-fuzzing/)。
- 判定依据：CDN 请求解释不一致引发 DoS；协议处理缺陷。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/reqsminer-automated-discovery-of-cdn-forwarding-request-inconsistencies-and-dos-attacks-with-grammar-based-fuzzing/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

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

## SLMIA-SR: Speaker-Level Membership Inference Attacks against Speaker Recognition Systems

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/slmia-sr-speaker-level-membership-inference-attacks-against-speaker-recognition-systems/)。
- 判定依据：通过说话人识别模型输出/白盒特征进行训练成员推断，不是声音电路的旁路泄漏。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/slmia-sr-speaker-level-membership-inference-attacks-against-speaker-recognition-systems/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## SSL-WM: A Black-Box Watermarking Approach for Encoders Pre-trained by Self-Supervised Learning

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/ssl-wm-a-black-box-watermarking-approach-for-encoders-pre-trained-by-self-supervised-learning/)。
- 判定依据：预训练编码器水印；主动标记与非预期泄漏分开。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/ssl-wm-a-black-box-watermarking-approach-for-encoders-pre-trained-by-self-supervised-learning/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Scrappy: SeCure Rate Assuring Protocol with PrivacY

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/scrappy-secure-rate-assuring-protocol-with-privacy/)。
- 判定依据：泄漏后仍保持特定限速性质的协议；正文明确秘密泄漏可破坏不可链接性，不能写成所有安全属性均抗侧信道。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/scrappy-secure-rate-assuring-protocol-with-privacy/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Secret-Shared Shuffle with Malicious Security

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/secret-shared-shuffle-with-malicious-security/)。
- 判定依据：秘密共享洗牌的恶意协议偏离、相关性检查与修补；不是物理掩码洗牌的侧信道防护。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/secret-shared-shuffle-with-malicious-security/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Secure Multiparty Computation of Threshold Signatures Made More Efficient

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/secure-multiparty-computation-of-threshold-signatures-made-more-efficient/)。
- 判定依据：阈值 ECDSA/BBS+ 协议成本、鲁棒性与公开验证；fault recovery 为协议参与者失败，不是测量故障/侧信道。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/secure-multiparty-computation-of-threshold-signatures-made-more-efficient/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Secure Ranging with IEEE 802.15.4z HRP UWB

- 来源：[SP 2024](https://www.ieee-security.org/TC/SP2024/accepted-papers.html)。
- 判定依据：对 IEEE 802.15.4z STS 接收器做安全测距证明和数值实验，主要保证主动距离操纵下的距离上界；不能等同秘密侧信道或实际芯片泄漏测量。
- 阅读来源：https://xplorestaging.ieee.org/document/10646848/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Security-Performance Tradeoff in DAG-based Proof-of-Work Blockchain Protocols

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/security-performance-tradeoff-in-dag-based-proof-of-work-blockchain-protocols/)。
- 判定依据：PoW DAG 拥塞与安全性；不属于功耗波形泄漏。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/security-performance-tradeoff-in-dag-based-proof-of-work-blockchain-protocols/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Separation is Good: A Faster Order-Fairness Byzantine Consensus

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/separation-is-good-a-faster-order-fairness-byzantine-consensus/)。
- 判定依据：BFT 排序公平性；协议安全背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/separation-is-good-a-faster-order-fairness-byzantine-consensus/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## ShapFuzz: Efficient Fuzzing via Shapley-Guided Byte Selection

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/shapfuzz-efficient-fuzzing-via-shapley-guided-byte-selection/)。
- 判定依据：ShapFuzz 用 Shapley 值选择输入字节；方法背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/shapfuzz-efficient-fuzzing-via-shapley-guided-byte-selection/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Sharing cyber threat intelligence: Does it really help?

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/sharing-cyber-threat-intelligence-does-it-really-help/)。
- 判定依据：威胁情报共享质量；非侧信道研究。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/sharing-cyber-threat-intelligence-does-it-really-help/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## SigmaDiff: Semantics-Aware Deep Graph Matching for Pseudocode Diffing

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/sigmadiff-semantics-aware-deep-graph-matching-for-pseudocode-diffing/)。
- 判定依据：SigmaDiff 以伪代码图比较二进制版本；实现差异分析方法背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/sigmadiff-semantics-aware-deep-graph-matching-for-pseudocode-diffing/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Singular points of UOV and VOX

- 来源：[IACR ePrint 2024](https://eprint.iacr.org/2024/219)。
- 判定依据：mUOV 实际引用的 ePrint 2024/219；研究 UOV-hat-plus/VOX 的奇异点代数分析，不是新物理测量论文。作者记录 VOX 恢复从指数改成多项式的修订，不能沿用旧版结论。
- 阅读来源：https://eprint.iacr.org/2024/219。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Sneaky Spikes: Uncovering Stealthy Backdoor Attacks in Spiking Neural Networks with Neuromorphic Data

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/sneaky-spikes-uncovering-stealthy-backdoor-attacks-in-spiking-neural-networks-with-neuromorphic-data/)。
- 判定依据：脉冲神经网络后门；spike 指模型计算事件，不是实测电流脉冲。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/sneaky-spikes-uncovering-stealthy-backdoor-attacks-in-spiking-neural-networks-with-neuromorphic-data/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

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

## Symphony: Path Validation at Scale

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/symphony-path-validation-at-scale/)。
- 判定依据：网络路径验证；协议安全背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/symphony-path-validation-at-scale/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## SyzBridge: Bridging the Gap in Exploitability Assessment of Linux Kernel Bugs in the Linux Ecosystem

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/syzbridge-bridging-the-gap-in-exploitability-assessment-of-linux-kernel-bugs-in-the-linux-ecosystem/)。
- 判定依据：SyzBridge 迁移内核漏洞可利用性判断；测试方法背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/syzbridge-bridging-the-gap-in-exploitability-assessment-of-linux-kernel-bugs-in-the-linux-ecosystem/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## TALISMAN: Tamper Analysis for Reference Monitors

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/talisman-tamper-analysis-for-reference-monitors/)。
- 判定依据：引用监视器的信息流完整性和授权查询防篡改，不是机密性侧信道证明。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/talisman-tamper-analysis-for-reference-monitors/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## TextGuard: Provable Defense against Backdoor Attacks on Text Classification

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/textguard-provable-defense-against-backdoor-attacks-on-text-classification/)。
- 判定依据：TextGuard 文本后门防护；模型鲁棒性研究。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/textguard-provable-defense-against-backdoor-attacks-on-text-classification/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## The CURE to Vulnerabilities in RPKI Validation

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/the-cure-to-vulnerabilities-in-rpki-validation/)。
- 判定依据：RPKI 模糊测试；网络实现分析背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/the-cure-to-vulnerabilities-in-rpki-validation/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## The Dark Side of E-Commerce: Dropshipping Abuse as a Business Model

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/the-dark-side-of-e-commerce-dropshipping-abuse-as-a-business-model/)。
- 判定依据：电商代发货滥用；平台生态研究。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/the-dark-side-of-e-commerce-dropshipping-abuse-as-a-business-model/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## The Dark Side of Scale: Insecurity of Direct-to-Cell Satellite Mega-Constellations

- 来源：[SP 2024](https://www.ieee-security.org/TC/SP2024/accepted-papers.html)。
- 判定依据：SatOver 利用信令和伪基站阻断 direct-to-cell 接入，主要是协议可用性与接入劫持；不可与卫星位置元数据侧信道合并。
- 阅读来源：https://xplorestaging.ieee.org/document/10646850/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Towards Automated Regulation Analysis for Effective Privacy Compliance

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/towards-automated-regulation-analysis-for-effective-privacy-compliance/)。
- 判定依据：法规文本分析；非侧信道研究。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/towards-automated-regulation-analysis-for-effective-privacy-compliance/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Towards Precise Reporting of Cryptographic Misuses

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/towards-precise-reporting-of-cryptographic-misuses/)。
- 判定依据：密码 API 误用分析与误报减少；实现审查背景，不等于物理泄漏结论。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/towards-precise-reporting-of-cryptographic-misuses/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Transpose Attack: Stealing Datasets with Bidirectional Training

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/transpose-attack-stealing-datasets-with-bidirectional-training/)。
- 判定依据：在恶意训练模型中编码训练数据并从反向模型取出，属于植入式数据外传。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/transpose-attack-stealing-datasets-with-bidirectional-training/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## TrustSketch: Trustworthy Sketch-based Telemetry on Cloud Hosts

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/trustsketch-trustworthy-sketch-based-telemetry-on-cloud-hosts/)。
- 判定依据：近似 sketch 遥测结果的完整性防护；未研究敏感状态的旁路观察。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/trustsketch-trustworthy-sketch-based-telemetry-on-cloud-hosts/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Understanding Route Origin Validation (ROV) Deployment in the Real World and Why MANRS Action 1 Is Not Followed

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/understanding-route-origin-validation-rov-deployment-in-the-real-world-and-why-manrs-action-1-is-not-followed/)。
- 判定依据：路由源验证部署测量；网络安全背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/understanding-route-origin-validation-rov-deployment-in-the-real-world-and-why-manrs-action-1-is-not-followed/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Understanding and Analyzing Appraisal Systems in the Underground Marketplaces

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/understanding-and-analyzing-appraisal-systems-in-the-underground-marketplaces/)。
- 判定依据：地下市场评价体系；非侧信道研究。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/understanding-and-analyzing-appraisal-systems-in-the-underground-marketplaces/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Understanding the Implementation and Security Implications of Protective DNS Services

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/understanding-the-implementation-and-security-implications-of-protective-dns-services/)。
- 判定依据：保护性 DNS 重写策略、规避和 DoS 的部署测量，摘要未给秘密侧信道。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/understanding-the-implementation-and-security-implications-of-protective-dns-services/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## UniID: Spoofing Face Authentication System by Universal Identity

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/uniid-spoofing-face-authentication-system-by-universal-identity/)。
- 判定依据：对抗注册攻击人脸认证；主动模型输入攻击。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/uniid-spoofing-face-authentication-system-by-universal-identity/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## UntrustIDE: Exploiting Weaknesses in VS Code Extensions

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/untrustide-exploiting-weaknesses-in-vs-code-extensions/)。
- 判定依据：IDE 扩展中的注入漏洞；直接软件攻击面。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/untrustide-exploiting-weaknesses-in-vs-code-extensions/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Unus pro omnibus: Multi-Client Searchable Encryption via Access Control

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/unus-pro-omnibus-multi-client-searchable-encryption-via-access-control/)。
- 判定依据：多客户端可搜索加密的委托、前向隐私和关键字猜测保护；保留搜索泄漏背景，摘要未显示新的实现侧信道分析。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/unus-pro-omnibus-multi-client-searchable-encryption-via-access-control/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## VETEOS: Statically Vetting EOSIO Contracts for the “Groundhog Day” Vulnerabilities

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/veteos-statically-vetting-eosio-contracts-for-the-groundhog-day-vulnerabilities/)。
- 判定依据：VETEOS 的回滚判断读取余额或显式暴露的全局状态；正文中的 timing 指执行中何时读状态，未建立耗时侧信道。摘要及 PDF pp.1,3–4 已读，保留为状态 oracle/因果背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/veteos-statically-vetting-eosio-contracts-for-the-groundhog-day-vulnerabilities/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## When Cryptography Needs a Hand: Practical Post-Quantum Authentication for V2V Communications

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/when-cryptography-needs-a-hand-practical-post-quantum-authentication-for-v2v-communications/)。
- 判定依据：后量子 V2V 认证、证书传输调度与混合协议性能；摘要未给侧信道贡献。93% 冗余与 0.39 ms 增量均为文中特定情景，不证明物理抗泄漏。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/when-cryptography-needs-a-hand-practical-post-quantum-authentication-for-v2v-communications/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## You Can Use But Cannot Recognize: Preserving Visual Privacy in Deep Neural Networks

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/you-can-use-but-cannot-recognize-preserving-visual-privacy-in-deep-neural-networks/)。
- 判定依据：对公开训练/推理图像做像素打乱以保护视觉内容，非实现侧信道。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/you-can-use-but-cannot-recognize-preserving-visual-privacy-in-deep-neural-networks/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## dRR: A Decentralized, Scalable, and Auditable Architecture for RPKI Repository

- 来源：[NDSS 2024](https://www.ndss-symposium.org/ndss-paper/drr-a-decentralized-scalable-and-auditable-architecture-for-rpki-repository/)。
- 判定依据：RPKI 仓库架构与运营；网络安全背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/drr-a-decentralized-scalable-and-auditable-architecture-for-rpki-repository/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## "That's my perspective from 30 years of doing this": An Interview Study on Practices, Experiences, and Challenges of Updating Cryptographic Code

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/krause)。
- 判定依据：开发者访谈及密码/PQC 迁移实践；摘要没有测量或实现侧信道机制。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## A Comprehensive Memory Safety Analysis of Bootloaders

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/a-comprehensive-memory-safety-analysis-of-bootloaders/)。
- 判定依据：启动加载器内存安全与模糊测试；摘要未建立测量型侧信道。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/a-comprehensive-memory-safety-analysis-of-bootloaders/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## A Formal Analysis of Apple's iMessage PQ3 Protocol

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/linker)。
- 判定依据：iMessage PQ3 的 TAMARIN 协议证明；不是实现泄漏分析。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## A Formal Approach to Multi-Layered Privileges for Enclaves

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/a-formal-approach-to-multi-layered-privileges-for-enclaves/)。
- 判定依据：Palantir 研究 enclave 权限层次和形式化隔离，摘要未给出侧信道观察或防护评估。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/a-formal-approach-to-multi-layered-privileges-for-enclaves/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## A High-performance NTT/MSM Accelerator for Zero-knowledge Proof Using Load-balanced Fully-pipelined Montgomery Multiplier

- 来源：[TCHES 2025](https://doi.org/10.46586/tches.v2025.i1.275-313)。
- 判定依据：通过统一 NTT/MSM 数据通路及流水模乘加速 ZKP；资源共享与性能不直接支持隔离或泄漏主张。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## A Key-Driven Framework for Identity-Preserving Face Anonymization

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/a-key-driven-framework-for-identity-preserving-face-anonymization/)。
- 判定依据：密钥控制的人脸匿名化与身份验证；处理图像表示，不是密码功耗或时序泄漏。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/a-key-driven-framework-for-identity-preserving-face-anonymization/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## A Large-Scale Measurement Study of the PROXY Protocol and its Security Implications

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/a-large-scale-measurement-study-of-the-proxy-protocol-and-its-security-implications/)。
- 判定依据：PROXY 协议误配置导致访问控制绕过与基础设施信息暴露，摘要不是侧信道测量。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/a-large-scale-measurement-study-of-the-proxy-protocol-and-its-security-implications/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## A Method to Facilitate Membership Inference Attacks in Deep Learning Models

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/a-method-to-facilitate-membership-inference-attacks-in-deep-learning-models/)。
- 判定依据：恶意训练代码放大黑盒成员推断并规避常见隐私审计；保留模型隐私背景，摘要没有物理或微架构观察。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/a-method-to-facilitate-membership-inference-attacks-in-deep-learning-models/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## A Multifaceted Study on the Use of TLS and Auto-detect in Email Ecosystems

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/a-multifaceted-study-on-the-use-of-tls-and-auto-detect-in-email-ecosystems/)。
- 判定依据：研究邮件 TLS 自动配置降级及明文凭据暴露，未报告时序或物理泄漏。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/a-multifaceted-study-on-the-use-of-tls-and-auto-detect-in-email-ecosystems/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## A New PPML Paradigm for Quantized Models

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/a-new-ppml-paradigm-for-quantized-models/)。
- 判定依据：隐私查表与量化模型的安全计算协议；摘要未讨论实际访问时序或物理泄漏。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/a-new-ppml-paradigm-for-quantized-models/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

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

## ASGARD: Protecting On-Device Deep Neural Networks with Virtualization-Based Trusted Execution Environments

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/asgard-protecting-on-device-deep-neural-networks-with-virtualization-based-trusted-execution-environments/)。
- 判定依据：以虚拟化 TEE 保护设备 DNN，主要是隔离和可信基压缩，未见侧信道评估。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/asgard-protecting-on-device-deep-neural-networks-with-virtualization-based-trusted-execution-environments/。
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

## Alba: The Dawn of Scalable Bridges for Blockchains

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/alba-the-dawn-of-scalable-bridges-for-blockchains/)。
- 判定依据：Alba 跨链桥与链下事件证明；协议扩展性背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/alba-the-dawn-of-scalable-bridges-for-blockchains/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Algebraic Linear Analysis for Number Theoretic Transform in Lattice-Based Cryptography

- 来源：[TCHES 2025](https://doi.org/10.46586/tches.v2025.i3.668-692)。
- 判定依据：摘要贡献是 CryptoLine/islpy 对 NTT 汇编范围与算术正确性的验证，未说明侧信道非干扰或泄漏评估；保留为 PQC 实现验证背景。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## All your (data)base are belong to us: Characterizing Database Ransom(ware) Attacks

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/all-your-database-are-belong-to-us-characterizing-database-ransomware-attacks/)。
- 判定依据：数据库弱认证导致勒索；直接访问缺陷，不是旁路观测。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/all-your-database-are-belong-to-us-characterizing-database-ransomware-attacks/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## AlphaDog: No-Box Camouflage Attacks via Alpha Channel Oversight

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/alphadog-no-box-camouflage-attacks-via-alpha-channel-oversight/)。
- 判定依据：AlphaDog 利用图像透明度处理差异进行主动视觉欺骗；Alpha channel 不是侧信道。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/alphadog-no-box-camouflage-attacks-via-alpha-channel-oversight/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## An Empirical Study on Fingerprint API Misuse with Lifecycle Analysis in Real-world Android Apps

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/an-empirical-study-on-fingerprint-api-misuse-with-lifecycle-analysis-in-real-world-android-apps/)。
- 判定依据：Android 指纹认证 API 生命周期误用；fingerprint 指生物认证，不是设备指纹测量。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/an-empirical-study-on-fingerprint-api-misuse-with-lifecycle-analysis-in-real-world-android-apps/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

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

## Attributing Open-Source Contributions is Critical but Difficult: A Systematic Analysis of GitHub Practices and Their Impact on Software Supply Chain Security

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/attributing-open-source-contributions-is-critical-but-difficult-a-systematic-analysis-of-github-practices-and-their-impact-on-software-supply-chain-security/)。
- 判定依据：GitHub 提交归属与签名真实性；供应链背景，未报告侧信道。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/attributing-open-source-contributions-is-critical-but-difficult-a-systematic-analysis-of-github-practices-and-their-impact-on-software-supply-chain-security/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Automated Expansion of Privacy Data Taxonomy for Compliant Data Breach Notification

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/automated-expansion-of-privacy-data-taxonomy-for-compliant-data-breach-notification/)。
- 判定依据：隐私数据分类法和法规通知；语义建模背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/automated-expansion-of-privacy-data-taxonomy-for-compliant-data-breach-notification/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Automated Mass Malware Factory: The Convergence of Piggybacking and Adversarial Example in Android Malicious Software Generation

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/automated-mass-malware-factory-the-convergence-of-piggybacking-and-adversarial-example-in-android-malicious-software-generation/)。
- 判定依据：恶意代码植入与对抗扰动规避检测；不是泄漏测量。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/automated-mass-malware-factory-the-convergence-of-piggybacking-and-adversarial-example-in-android-malicious-software-generation/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Automatic Insecurity: Exploring Email Auto-configuration in the Wild

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/automatic-insecurity-exploring-email-auto-configuration-in-the-wild/)。
- 判定依据：邮件自动配置引导错误服务器或不安全连接；直接凭据暴露与配置问题。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/automatic-insecurity-exploring-email-auto-configuration-in-the-wild/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Automatic Library Fuzzing through API Relation Evolvement

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/automatic-library-fuzzing-through-api-relation-evolvement/)。
- 判定依据：NEXZZER 学习 API 关系并生成模糊测试驱动；可复用测试方法背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/automatic-library-fuzzing-through-api-relation-evolvement/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## BARBIE: Robust Backdoor Detection Based on Latent Separability

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/barbie-robust-backdoor-detection-based-on-latent-separability/)。
- 判定依据：BARBIE 利用潜在表示可分性检测后门；非物理测量泄漏。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/barbie-robust-backdoor-detection-based-on-latent-separability/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## BULKHEAD: Secure, Scalable, and Efficient Kernel Compartmentalization with PKS

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/bulkhead-secure-scalable-and-efficient-kernel-compartmentalization-with-pks/)。
- 判定依据：PKS 内核分区、接口完整性与权限防护，不能据隔离主张推出侧信道安全。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/bulkhead-secure-scalable-and-efficient-kernel-compartmentalization-with-pks/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Balancing Privacy and Data Utilization: A Comparative Vignette Study on User Acceptance of Data Trustees in Germany and the US

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/balancing-privacy-and-data-utilization-a-comparative-vignette-study-on-user-acceptance-of-data-trustees-in-germany-and-the-us/)。
- 判定依据：数据托管人的用户接受度研究；非侧信道。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/balancing-privacy-and-data-utilization-a-comparative-vignette-study-on-user-acceptance-of-data-trustees-in-germany-and-the-us/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Be Careful of What You Embed: Demystifying OLE Vulnerabilities

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/be-careful-of-what-you-embed-demystifying-ole-vulnerabilities/)。
- 判定依据：Office OLE 信任边界和解析漏洞；直接软件攻击面。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/be-careful-of-what-you-embed-demystifying-ole-vulnerabilities/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Beyond Classification: Inferring Function Names in Stripped Binaries via Domain Adapted LLMs

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/beyond-classification-inferring-function-names-in-stripped-binaries-via-domain-adapted-llms/)。
- 判定依据：SymGen 用领域适配 LLM 恢复函数名；实现理解方法背景，不等于恢复秘密。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/beyond-classification-inferring-function-names-in-stripped-binaries-via-domain-adapted-llms/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## BinEnhance: An Enhancement Framework Based on External Environment Semantics for Binary Code Search

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/binenhance-an-enhancement-framework-based-on-external-environment-semantics-for-binary-code-search/)。
- 判定依据：BinEnhance 建模函数间环境语义进行代码搜索；关系图方法背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/binenhance-an-enhancement-framework-based-on-external-environment-semantics-for-binary-code-search/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## BitShield: Defending Against Bit-Flip Attacks on DNN Executables

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/bitshield-defending-against-bit-flip-attacks-on-dnn-executables/)。
- 判定依据：针对 DNN 可执行文件的位翻转与完整性检查，属于故障防护。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/bitshield-defending-against-bit-flip-attacks-on-dnn-executables/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Black-box Membership Inference Attacks against Fine-tuned Diffusion Models

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/black-box-membership-inference-attacks-against-fine-tuned-diffusion-models/)。
- 判定依据：微调扩散模型的输出分数成员推断；模型隐私相邻主题，未建立物理侧信道。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/black-box-membership-inference-attacks-against-fine-tuned-diffusion-models/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Blackbox Fuzzing of Distributed Systems with Multi-Dimensional Inputs and Symmetry-Based Feedback Pruning

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/blackbox-fuzzing-of-distributed-systems-with-multi-dimensional-inputs-and-symmetry-based-feedback-pruning/)。
- 判定依据：DistFuzz 操纵事件时序并用消息序列作反馈；时序是测试输入，不是秘密泄漏指标。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/blackbox-fuzzing-of-distributed-systems-with-multi-dimensional-inputs-and-symmetry-based-feedback-pruning/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Blindfold: Confidential Memory Management by Untrusted Operating System

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/blindfold-confidential-memory-management-by-untrusted-operating-system/)。
- 判定依据：Blindfold 研究不可信内核下的机密内存管理；摘要未建立访问模式或物理泄漏保证。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/blindfold-confidential-memory-management-by-untrusted-operating-system/。
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

## BumbleBee: Secure Two-party Inference Framework for Large Transformers

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/bumblebee-secure-two-party-inference-framework-for-large-transformers/)。
- 判定依据：两方安全 Transformer 推理协议及通信优化，摘要不涉及额外实现侧信道。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/bumblebee-secure-two-party-inference-framework-for-large-transformers/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Bundled Authenticated Key Exchange: A Concrete Treatment of Signal's Handshake Protocol and Post-Quantum Security

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/hashimoto-key-exchange)。
- 判定依据：Signal 握手的 bundled authenticated key exchange 与后量子协议安全；非物理实现分析。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## CASPR: Context-Aware Security Policy Recommendation

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/caspr-context-aware-security-policy-recommendation/)。
- 判定依据：CASPR 根据策略、日志和属性推荐 SELinux 权限；授权配置背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/caspr-context-aware-security-policy-recommendation/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## CCTAG: Configurable and Combinable Tagged Architecture

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/cctag-configurable-and-combinable-tagged-architecture/)。
- 判定依据：标签架构组合多种内存安全防护；这里的 mask 是策略设计，不是密码掩码。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/cctag-configurable-and-combinable-tagged-architecture/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## CENSOR: Defense Against Gradient Inversion via Orthogonal Subspace Bayesian Sampling

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/censor-defense-against-gradient-inversion-via-orthogonal-subspace-bayesian-sampling/)。
- 判定依据：CENSOR 对协议中上传的梯度进行防反演处理；高维正交子空间方法背景，不是波形证据。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/censor-defense-against-gradient-inversion-via-orthogonal-subspace-bayesian-sampling/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## CLIBE: Detecting Dynamic Backdoors in Transformer-based NLP Models

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/clibe-detecting-dynamic-backdoors-in-transformer-based-nlp-models/)。
- 判定依据：CLIBE 用权重扰动及其泛化检测动态后门；模型鲁棒性背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/clibe-detecting-dynamic-backdoors-in-transformer-based-nlp-models/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Careful About What App Promotion Ads Recommend! Detecting and Explaining Malware Promotion via App Promotion Graph

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/careful-about-what-app-promotion-ads-recommend-detecting-and-explaining-malware-promotion-via-app-promotion-graph/)。
- 判定依据：应用推广图与恶意软件传播检测；直接生态数据分析。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/careful-about-what-app-promotion-ads-recommend-detecting-and-explaining-malware-promotion-via-app-promotion-graph/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## CertTA: Certified Robustness Made Practical for Learning-Based Traffic Analysis

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/yan-jinzhu)。
- 判定依据：流量分类器对填充、时序和虚假包的鲁棒性认证；摘要未明确秘密推断目标，保留方法背景待正文细化。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Characterizing the Impact of Audio Deepfakes in the Presence of Cochlear Implant

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/characterizing-the-impact-of-audio-deepfakes-in-the-presence-of-cochlear-implant/)。
- 判定依据：人工耳蜗使用者对深度伪造语音的辨别；感知安全研究，不是被动窃听通道。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/characterizing-the-impact-of-audio-deepfakes-in-the-presence-of-cochlear-implant/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## CoVault: Secure, Scalable Analytics of Personal Data

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/de-viti)。
- 判定依据：MPC/TEE 协同的隐私数据分析；摘要未给侧信道防护论证。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Compiled Models, Built-In Exploits: Uncovering Pervasive Bit-Flip Attack Surfaces in DNN Executables

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/compiled-models-built-in-exploits-uncovering-pervasive-bit-flip-attack-surfaces-in-dnn-executables/)。
- 判定依据：通过 Rowhammer 类位翻转篡改 DNN 程序语义，主要是完整性攻击。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/compiled-models-built-in-exploits-uncovering-pervasive-bit-flip-attack-surfaces-in-dnn-executables/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Comprehensive Deniability Analysis of Signal Handshake Protocols: X3DH, PQXDH to Fully Post-Quantum with Deniable Ring Signatures

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/katsumata)。
- 判定依据：Signal 握手否认性与后量子环签名协议；非实现侧信道。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Cross-Origin Web Attacks via HTTP/2 Server Push and Signed HTTP Exchange

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/cross-origin-web-attacks-via-http-2-server-push-and-signed-http-exchange/)。
- 判定依据：HTTP/2 与 SXG 引起同源策略绕过，属于协议授权语义问题。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/cross-origin-web-attacks-via-http-2-server-push-and-signed-http-exchange/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Ctrl+Alt+Deceive: Quantifying User Exposure to Online Scams

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/ctrlaltdeceive-quantifying-user-exposure-to-online-scams/)。
- 判定依据：用户暴露于网络诈骗的统计研究；非侧信道。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/ctrlaltdeceive-quantifying-user-exposure-to-online-scams/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## DLBox: New Model Training Framework for Protecting Training Data

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/dlbox-new-model-training-framework-for-protecting-training-data/)。
- 判定依据：DLBox 限制不可信训练程序把数据写入模型；使用 SEV-SNP 不等于已评估其物理侧信道。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/dlbox-new-model-training-framework-for-protecting-training-data/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## DShield: Defending against Backdoor Attacks on Graph Neural Networks via Discrepancy Learning

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/dshield-defending-against-backdoor-attacks-on-graph-neural-networks-via-discrepancy-learning/)。
- 判定依据：DShield 通过语义和属性差异检测图后门；非测量泄漏。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/dshield-defending-against-backdoor-attacks-on-graph-neural-networks-via-discrepancy-learning/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## DUMPLING: Fine-grained Differential JavaScript Engine Fuzzing

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/dumpling-fine-grained-differential-javascript-engine-fuzzing/)。
- 判定依据：DUMPLING 比较解释与 JIT 执行状态发现编译缺陷；实现语义核查方法背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/dumpling-fine-grained-differential-javascript-engine-fuzzing/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Deanonymizing Ethereum Validators: The P2P Network Has a Privacy Issue

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/heimbach)。
- 判定依据：Ethereum P2P 验证者 IP 去匿名化；摘要未明确时序或共享资源观察机制，保留协议元数据邻接并待正文。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Defending Against Membership Inference Attacks on Iteratively Pruned Deep Neural Networks

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/defending-against-membership-inference-attacks-on-iteratively-pruned-deep-neural-networks/)。
- 判定依据：迭代剪枝中的记忆与成员隐私防护；模型输出泄漏背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/defending-against-membership-inference-attacks-on-iteratively-pruned-deep-neural-networks/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Delay-allowed Differentially Private Data Stream Release

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/delay-allowed-differentially-private-data-stream-release/)。
- 判定依据：允许延迟的数据流差分隐私发布；延迟为机制参数，不是观测秘密的耗时。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/delay-allowed-differentially-private-data-stream-release/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Density Boosts Everything: A One-stop Strategy for Improving Performance, Robustness, and Sustainability of Malware Detectors

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/density-boosts-everything-a-one-stop-strategy-for-improving-performance-robustness-and-sustainability-of-malware-detectors/)。
- 判定依据：通过密度增强改善恶意软件检测；学习方法背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/density-boosts-everything-a-one-stop-strategy-for-improving-performance-robustness-and-sustainability-of-malware-detectors/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Detecting Compromise of Passkey Storage on the Cloud

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/islam)。
- 判定依据：已被窃取的云端 passkey 的滥用检测；密钥直接失窃不等于侧信道。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Detecting IMSI-Catchers by Characterizing Identity Exposing Messages in Cellular Traffic

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/detecting-imsi-catchers-by-characterizing-identity-exposing-messages-in-cellular-traffic/)。
- 判定依据：通过蜂窝协议必须发送的身份消息检测 IMSI-Catcher；保护直接标识符披露，不归为物理侧信道。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/detecting-imsi-catchers-by-characterizing-identity-exposing-messages-in-cellular-traffic/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Detecting Ransomware Despite I/O Overhead: A Practical Multi-Staged Approach

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/detecting-ransomware-despite-i-o-overhead-a-practical-multi-staged-approach/)。
- 判定依据：按进程行为分阶段监控 I/O 检测勒索软件；没有秘密恢复目标。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/detecting-ransomware-despite-i-o-overhead-a-practical-multi-staged-approach/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## DiStefano: Decentralized Infrastructure for Sharing Trusted Encrypted Facts and Nothing More

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/distefano-decentralized-infrastructure-for-sharing-trusted-encrypted-facts-and-nothing-more/)。
- 判定依据：TLS 1.3 事实承诺与隐私协议，摘要不报告实现侧信道。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/distefano-decentralized-infrastructure-for-sharing-trusted-encrypted-facts-and-nothing-more/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## DiffLoc: WiFi Hidden Camera Localization Based on Electromagnetic Diffraction

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/zhang-xiang)。
- 判定依据：利用主动金属板和 WiFi 衍射定位隐藏相机；观察正常无线发射，保留物理定位背景，不等同于计算的非预期电磁泄漏。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Diffence: Fencing Membership Privacy With Diffusion Models

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/diffence-fencing-membership-privacy-with-diffusion-models/)。
- 判定依据：Diffence 用样本重生成降低成员推断；模型隐私背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/diffence-fencing-membership-privacy-with-diffusion-models/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Dissecting Payload-based Transaction Phishing on Ethereum

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/dissecting-payload-based-transaction-phishing-on-ethereum/)。
- 判定依据：Ethereum 恶意交易载荷钓鱼分析；直接交易语义攻击。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/dissecting-payload-based-transaction-phishing-on-ethereum/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Distributed Function Secret Sharing and Applications

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/distributed-function-secret-sharing-and-applications/)。
- 判定依据：分布式函数秘密共享和安全三角函数协议，未见侧信道贡献。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/distributed-function-secret-sharing-and-applications/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Do (Not) Follow the White Rabbit: Challenging the Myth of Harmless Open Redirection

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/do-not-follow-the-white-rabbit-challenging-the-myth-of-harmless-open-redirection/)。
- 判定依据：客户端开放重定向及其升级为 XSS/CSRF；直接 Web 漏洞。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/do-not-follow-the-white-rabbit-challenging-the-myth-of-harmless-open-redirection/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Do We Really Need to Design New Byzantine-robust Aggregation Rules?

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/do-we-really-need-to-design-new-byzantine-robust-aggregation-rules/)。
- 判定依据：FoundationFL 通过合成更新增强拜占庭鲁棒聚合；投毒防护背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/do-we-really-need-to-design-new-byzantine-robust-aggregation-rules/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Dorami: Privilege Separating Security Monitor on RISC-V TEEs

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/kuhne)。
- 判定依据：RISC-V 安全监控器的固件权限分离；不是侧信道安全证明。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Duumviri: Detecting Trackers and Mixed Trackers with a Breakage Detector

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/duumviri-detecting-trackers-and-mixed-trackers-with-a-breakage-detector/)。
- 判定依据：Duumviri 观察屏蔽请求造成的差异以检测跟踪器及破坏；保留隐私防护背景，摘要未核定具体侧信道推断。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/duumviri-detecting-trackers-and-mixed-trackers-with-a-breakage-detector/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## EAGLEYE: Exposing Hidden Web Interfaces in IoT Devices via Routing Analysis

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/eagleye-exposing-hidden-web-interfaces-in-iot-devices-via-routing-analysis/)。
- 判定依据：EAGLEYE 从路由参数推断隐藏 Web 接口并测试；显式接口发现，不是密码侧信道。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/eagleye-exposing-hidden-web-interfaces-in-iot-devices-via-routing-analysis/。
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

## ERW-Radar: An Adaptive Detection System against Evasive Ransomware by Contextual Behavior Detection and Fine-grained Content Analysis

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/erw-radar-an-adaptive-detection-system-against-evasive-ransomware-by-contextual-behavior-detection-and-fine-grained-content-analysis/)。
- 判定依据：ERW-Radar 用 I/O 重复性和文件字节分布检测勒索软件；直接行为与内容检测。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/erw-radar-an-adaptive-detection-system-against-evasive-ransomware-by-contextual-behavior-detection-and-fine-grained-content-analysis/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Eclipse Attacks on Monero’s Peer-to-Peer Network

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/eclipse-attacks-on-moneros-peer-to-peer-network/)。
- 判定依据：Monero eclipse 攻击利用连接管理与交易传播差异隔离节点；摘要的贡献不是秘密的测量推断。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/eclipse-attacks-on-moneros-peer-to-peer-network/。
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

## Enhancing Security in Third-Party Library Reuse – Comprehensive Detection of 1-day Vulnerability through Code Patch Analysis

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/enhancing-security-in-third-party-library-reuse-comprehensive-detection-of-1-day-vulnerability-through-code-patch-analysis/)。
- 判定依据：VULTURE 通过补丁和库依赖分析识别已知漏洞复用；供应链方法背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/enhancing-security-in-third-party-library-reuse-comprehensive-detection-of-1-day-vulnerability-through-code-patch-analysis/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## EvoCrawl: Exploring Web Application Code and State using Evolutionary Search

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/evocrawl-exploring-web-application-code-and-state-using-evolutionary-search/)。
- 判定依据：EvoCrawl 搜索有状态 Web 交互序列；测试方法背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/evocrawl-exploring-web-application-code-and-state-using-evolutionary-search/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Explanation as a Watermark: Towards Harmless and Multi-bit Model Ownership Verification via Watermarking Feature Attribution

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/explanation-as-a-watermark-towards-harmless-and-multi-bit-model-ownership-verification-via-watermarking-feature-attribution/)。
- 判定依据：EaaW 在特征归因解释中嵌入多位水印；主动产权标记，不作为非预期侧信道泄漏。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/explanation-as-a-watermark-towards-harmless-and-multi-bit-model-ownership-verification-via-watermarking-feature-attribution/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Exploring How to Authenticate Application Messages in MLS: More Efficient, Post-Quantum, and Anonymous Blocklistable

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/hashimoto-blocklistable)。
- 判定依据：MLS 消息认证的带宽、后量子和匿名黑名单协议；非实现泄漏。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Exploring User Perceptions of Security Auditing in the Web3 Ecosystem

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/exploring-user-perceptions-of-security-auditing-in-the-web3-ecosystem/)。
- 判定依据：Web3 用户对审计的理解与行为；非侧信道。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/exploring-user-perceptions-of-security-auditing-in-the-web3-ecosystem/。
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

## FUZZUER: Enabling Fuzzing of UEFI Interfaces on EDK-2

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/fuzzuer-enabling-fuzzing-of-uefi-interfaces-on-edk-2/)。
- 判定依据：FUZZUER 自动构造 UEFI 测试驱动；固件测试方法背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/fuzzuer-enabling-fuzzing-of-uefi-interfaces-on-edk-2/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

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

## From Large to Mammoth: A Comparative Evaluation of Large Language Models in Vulnerability Detection

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/from-large-to-mammoth-a-comparative-evaluation-of-large-language-models-in-vulnerability-detection/)。
- 判定依据：比较 LLM 漏洞检测能力；可供研究工具选用参考，不直接提供侧信道成果。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/from-large-to-mammoth-a-comparative-evaluation-of-large-language-models-in-vulnerability-detection/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## GAP-Diff: Protecting JPEG-Compressed Images from Diffusion-based Facial Customization

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/gap-diff-protecting-jpeg-compressed-images-from-diffusion-based-facial-customization/)。
- 判定依据：GAP-Diff 用抗 JPEG 扰动防止人脸定制；主动输入防护，不是测量噪声模型。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/gap-diff-protecting-jpeg-compressed-images-from-diffusion-based-facial-customization/。
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

## Generating API Parameter Security Rules with LLM for API Misuse Detection

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/generating-api-parameter-security-rules-with-llm-for-api-misuse-detection/)。
- 判定依据：GPTAid 结合 LLM、执行反馈和差分分析生成 API 规则；实验核验方法背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/generating-api-parameter-security-rules-with-llm-for-api-misuse-detection/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Generation of Fast Finite Field Arithmetic forCortex-M4 with ECDH and SQIsign Applications

- 来源：[TCHES 2025](https://doi.org/10.46586/tches.v2025.i4.588-620)。
- 判定依据：m4-modarith 自动生成快速有限域算术并证明约减正确性；功能证明不能自动推得恒时保证。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## GhostShot: Manipulating the Image of CCD Cameras with Electromagnetic Interference

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/ghostshot-manipulating-the-image-of-ccd-cameras-with-electromagnetic-interference/)。
- 判定依据：以电磁干扰向 CCD 图像注入内容，属于信号操纵而非泄漏观察。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/ghostshot-manipulating-the-image-of-ccd-cameras-with-electromagnetic-interference/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

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

## HADES Attack: Understanding and Evaluating Manipulation Risks of Email Blocklists

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/hades-attack-understanding-and-evaluating-manipulation-risks-of-email-blocklists/)。
- 判定依据：HADES 操纵邮件封禁列表使正常服务器被拒绝；与同名密码方案或功耗攻击区分。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/hades-attack-understanding-and-evaluating-manipulation-risks-of-email-blocklists/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Heimdall: Towards Risk-Aware Network Management Outsourcing

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/heimdall-towards-risk-aware-network-management-outsourcing/)。
- 判定依据：网络管理外包的风险与参考监控，非本库观察机制。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/heimdall-towards-risk-aware-network-management-outsourcing/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Hey, Your Secrets Leaked! Detecting and Characterizing Secret Leakage in the Wild

- 来源：[SP 2025](https://www.ieee-security.org/TC/SP2025/accepted-papers.html#collapse-169)。
- 判定依据：Keysentinel 检测代码与配置中的 API key、密码等直接暴露；此处 secret leakage 不是物理或共享资源侧信道。
- 阅读来源：https://xplorestaging.ieee.org/document/11023280/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Hidden and Lost Control: on Security Design Risks in IoT User-Facing Matter Controller

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/hidden-and-lost-control-on-security-design-risks-in-iot-user-facing-matter-controller/)。
- 判定依据：Matter 用户控制界面与权限设计缺陷；直接控制/授权问题。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/hidden-and-lost-control-on-security-design-risks-in-iot-user-facing-matter-controller/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Hitchhiking Vaccine: Enhancing Botnet Remediation With Remote Code Deployment Reuse

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/hitchhiking-vaccine-enhancing-botnet-remediation-with-remote-code-deployment-reuse/)。
- 判定依据：ECHO 复用恶意软件更新机制执行修复；直接代码部署路径，非侧信道。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/hitchhiking-vaccine-enhancing-botnet-remediation-with-remote-code-deployment-reuse/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Hobbit: Space-Efficient zkSNARK with Optimal Prover Time

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/pappas)。
- 判定依据：后量子 zkSNARK 的证明时间与空间；非实现侧信道。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Horcrux: Synthesize, Split, Shift and Stay Alive; Preventing Channel Depletion via Universal and Enhanced Multi-hop Payments

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/horcrux-synthesize-split-shift-and-stay-alive-preventing-channel-depletion-via-universal-and-enhanced-multi-hop-payments/)。
- 判定依据：Horcrux 缓解支付通道耗尽；channel 指支付关系，不是测量通道。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/horcrux-synthesize-split-shift-and-stay-alive-preventing-channel-depletion-via-universal-and-enhanced-multi-hop-payments/。
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

## I know what you MEME! Understanding and Detecting Harmful Memes with Multimodal Large Language Models

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/i-know-what-you-meme-understanding-and-detecting-harmful-memes-with-multimodal-large-language-models/)。
- 判定依据：多模态模型检测有害表情包；内容分析背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/i-know-what-you-meme-understanding-and-detecting-harmful-memes-with-multimodal-large-language-models/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## ICSQuartz: Scan Cycle-Aware and Vendor-Agnostic Fuzzing for Industrial Control Systems

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/icsquartz-scan-cycle-aware-and-vendor-agnostic-fuzzing-for-industrial-control-systems/)。
- 判定依据：ICSQuartz 利用 PLC 扫描周期语义作模糊测试；执行历史可作方法背景，未报告秘密泄漏。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/icsquartz-scan-cycle-aware-and-vendor-agnostic-fuzzing-for-industrial-control-systems/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Impact Tracing: Identifying the Culprit of Misinformation in Encrypted Messaging Systems

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/impact-tracing-identifying-the-culprit-of-misinformation-in-encrypted-messaging-systems/)。
- 判定依据：Impact Tracing 通过协议设计追踪消息传播者并保护其他用户；不是旁路观测。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/impact-tracing-identifying-the-culprit-of-misinformation-in-encrypted-messaging-systems/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Improving MPCitH with Preprocessing: Mask Is All You Need

- 来源：[TCHES 2025](https://doi.org/10.46586/tches.v2025.i2.1-22)。
- 判定依据：优化 MPCitH 预处理与 Picnic3 并行计算；mask 是证明协议中的随机掩蔽，摘要未给出物理掩码或侧信道安全评估。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Incorporating Gradients to Rules: Towards Lightweight, Adaptive Provenance-based Intrusion Detection

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/incorporating-gradients-to-rules-towards-lightweight-adaptive-provenance-based-intrusion-detection/)。
- 判定依据：CAPTAIN 用梯度优化溯源图入侵检测规则；图推断方法背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/incorporating-gradients-to-rules-towards-lightweight-adaptive-provenance-based-intrusion-detection/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Interventional Root Cause Analysis of Failures in Multi-Sensor Fusion Perception Systems

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/interventional-root-cause-analysis-of-failures-in-multi-sensor-fusion-perception-systems/)。
- 判定依据：多传感器融合故障的因果归因，可作研究方法背景，未研究秘密泄漏。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/interventional-root-cause-analysis-of-failures-in-multi-sensor-fusion-perception-systems/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Is MPC Secure? Leveraging Neural Network Classifiers to Detect Data Leakage Vulnerabilities in MPC Implementations

- 来源：[SP 2025](https://www.ieee-security.org/TC/SP2025/accepted-papers.html#collapse-235)。
- 判定依据：MPCGuard 用分类器比较 MPC 实现中参与者视图的隐私泄漏，作为实现隐私测试方法背景；摘要未把泄漏归因于功耗、时间或共享硬件观测。
- 阅读来源：https://xplorestaging.ieee.org/document/11023305/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## IsolateGPT: An Execution Isolation Architecture for LLM-Based Agentic Systems

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/isolategpt-an-execution-isolation-architecture-for-llm-based-agentic-systems/)。
- 判定依据：IsolateGPT 隔离 LLM 应用交互；自然语言系统安全架构，不代表硬件侧信道隔离。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/isolategpt-an-execution-isolation-architecture-for-llm-based-agentic-systems/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## JBomAudit: Assessing the Landscape, Compliance, and Security Implications of Java SBOMs

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/jbomaudit-assessing-the-landscape-compliance-and-security-implications-of-java-sboms/)。
- 判定依据：JBomAudit 审核 Java 软件物料清单完整性；供应链证据方法背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/jbomaudit-assessing-the-landscape-compliance-and-security-implications-of-java-sboms/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Kronos: A Secure and Generic Sharding Blockchain Consensus with Optimized Overhead

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/kronos-a-secure-and-generic-sharding-blockchain-consensus-with-optimized-overhead/)。
- 判定依据：Kronos 优化分片共识与跨片提交；时序假设讨论属于协议模型。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/kronos-a-secure-and-generic-sharding-blockchain-consensus-with-optimized-overhead/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## L-HAWK: A Controllable Physical Adversarial Patch Against a Long-Distance Target

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/l-hawk-a-controllable-physical-adversarial-patch-against-a-long-distance-target/)。
- 判定依据：L-HAWK 用激光触发物理对抗补丁；主动感知欺骗，不等于被动光学泄漏。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/l-hawk-a-controllable-physical-adversarial-patch-against-a-long-distance-target/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## LADDER: Multi-Objective Backdoor Attack via Evolutionary Algorithm

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/ladder-multi-objective-backdoor-attack-via-evolutionary-algorithm/)。
- 判定依据：LADDER 在图像/谱域优化后门触发器；谱域是输入表示，不是设备波形。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/ladder-multi-objective-backdoor-attack-via-evolutionary-algorithm/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## LESS is Even More: Optimizing Digital Signatures from Code Equivalence

- 来源：[TCHES 2025](https://doi.org/10.46586/tches.v2025.i4.386-408)。
- 判定依据：优化 LESS 规范形计算及参数选择的性能和签名长度，摘要未报告实现泄漏。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## LLMPirate: LLMs for Black-box Hardware IP Piracy

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/llmpirate-llms-for-black-box-hardware-ip-piracy/)。
- 判定依据：用 LLM 重写硬件设计逃避 IP 盗版检测，不是通过物理观察恢复电路。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/llmpirate-llms-for-black-box-hardware-ip-piracy/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

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

## LightAntenna: Characterizing the Limits of Fluorescent Lamp-Induced Electromagnetic Interference

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/lightantenna-characterizing-the-limits-of-fluorescent-lamp-induced-electromagnetic-interference/)。
- 判定依据：荧光灯诱发电磁干扰和传感器操纵，保留物理链路背景但不混入侧信道攻击数。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/lightantenna-characterizing-the-limits-of-fluorescent-lamp-induced-electromagnetic-interference/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Lost in the Mists of Time: Expirations in DNS Footprints of Mobile Apps

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/so)。
- 判定依据：移动应用过期域名依赖与接管风险；DNS footprint 不是本文中的秘密侧信道。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## MALintent: Coverage Guided Intent Fuzzing Framework for Android

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/malintent-coverage-guided-intent-fuzzing-framework-for-android/)。
- 判定依据：MALintent 对 Android Intent 处理器进行覆盖引导测试；直接接口与内存缺陷。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/malintent-coverage-guided-intent-fuzzing-framework-for-android/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## MOLE: Breaking GPU TEE with GPU-Embedded MCU

- 来源：[CCS 2025](https://doi.org/10.1145/3719027.3744823)。
- 判定依据：GPU 内嵌 MCU 的恶意固件绕过 TEE 隔离，直接提取或修改数据；摘要中的 AES 案例不是功耗/缓存推断证据，保留相邻硬件隔离研究。
- 阅读来源：https://hongyi.lu/papers/mole-ccs25.pdf。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## MTZK: Testing and Exploring Bugs in Zero-Knowledge (ZK) Compilers

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/mtzk-testing-and-exploring-bugs-in-zero-knowledge-zk-compilers/)。
- 判定依据：MTZK 用蜕变关系检查 ZK 编译正确性；密码实现核查背景，不等于零知识实现的物理安全。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/mtzk-testing-and-exploring-bugs-in-zero-knowledge-zk-compilers/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Magmaw: Modality-Agnostic Adversarial Attacks on Machine Learning-Based Wireless Communication Systems

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/magmaw-modality-agnostic-adversarial-attacks-on-machine-learning-based-wireless-communication-systems/)。
- 判定依据：Magmaw 向无线信号注入对抗扰动；即使测试加密通信，也不能直接称为被动泄漏恢复。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/magmaw-modality-agnostic-adversarial-attacks-on-machine-learning-based-wireless-communication-systems/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Manifoldchain: Maximizing Blockchain Throughput via Bandwidth-Clustered Sharding

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/manifoldchain-maximizing-blockchain-throughput-via-bandwidth-clustered-sharding/)。
- 判定依据：Manifoldchain 按带宽分组优化区块链吞吐；非功耗或时序侧信道。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/manifoldchain-maximizing-blockchain-throughput-via-bandwidth-clustered-sharding/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## McSee: Evaluating Advanced Rowhammer Attacks and Defenses via Automated DRAM Traffic Analysis

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/jattke)。
- 判定依据：用示波器解码 DRAM 总线流量评估 Rowhammer 与防护；保留测量方法背景，摘要未作秘密推断。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Mens Sana In Corpore Sano: Sound Firmware Corpora for Vulnerability Research

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/mens-sana-in-corpore-sano-sound-firmware-corpora-for-vulnerability-research/)。
- 判定依据：固件语料的代表性、去重和可重复性指南；可复用科研方法，不是侧信道攻击结论。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/mens-sana-in-corpore-sano-sound-firmware-corpora-for-vulnerability-research/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## MingledPie: A Cluster Mingling Approach for Mitigating Preference Profiling in CFL

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/mingledpie-a-cluster-mingling-approach-for-mitigating-preference-profiling-in-cfl/)。
- 判定依据：聚类联邦学习的客户端偏好推断防护，主要是算法可见输出隐私。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/mingledpie-a-cluster-mingling-approach-for-mitigating-preference-profiling-in-cfl/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Misdirection of Trust: Demystifying the Abuse of Dedicated URL Shortening Service

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/misdirection-of-trust-demystifying-the-abuse-of-dedicated-url-shortening-service/)。
- 判定依据：专用短链服务的信任误导与钓鱼；直接 URL 验证问题。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/misdirection-of-trust-demystifying-the-abuse-of-dedicated-url-shortening-service/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Moneta: Ex-Vivo GPU Driver Fuzzing by Recalling In-Vivo Execution States

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/moneta-ex-vivo-gpu-driver-fuzzing-by-recalling-in-vivo-execution-states/)。
- 判定依据：Moneta 回放 GPU 驱动状态以开展模糊测试；时间约束与快照不是侧信道观测。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/moneta-ex-vivo-gpu-driver-fuzzing-by-recalling-in-vivo-execution-states/。
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

## Mysticeti: Reaching the Latency Limits with Uncertified DAGs

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/mysticeti-reaching-the-latency-limits-with-uncertified-dags/)。
- 判定依据：DAG 拜占庭共识与快速提交；延迟是协议性能指标，未建立秘密侧信道。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/mysticeti-reaching-the-latency-limits-with-uncertified-dags/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

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

## NodeMedic-FINE: Automatic Detection and Exploit Synthesis for Node.js Vulnerabilities

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/nodemedic-fine-automatic-detection-and-exploit-synthesis-for-node-js-vulnerabilities/)。
- 判定依据：Node.js 的污点分析、类型感知测试与代码/命令注入验证；直接软件漏洞。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/nodemedic-fine-automatic-detection-and-exploit-synthesis-for-node-js-vulnerabilities/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## On the Realism of LiDAR Spoofing Attacks against Autonomous Driving Vehicle at High Speed and Long Distance

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/on-the-realism-of-lidar-spoofing-attacks-against-autonomous-driving-vehicle-at-high-speed-and-long-distance/)。
- 判定依据：激光欺骗 LiDAR 的距离和速度可行性，属于主动传感器注入。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/on-the-realism-of-lidar-spoofing-attacks-against-autonomous-driving-vehicle-at-high-speed-and-long-distance/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## On the Robustness of LDP Protocols for Numerical Attributes under Data Poisoning Attacks

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/on-the-robustness-of-ldp-protocols-for-numerical-attributes-under-data-poisoning-attacks/)。
- 判定依据：攻击者提交恶意数据污染 LDP 数值估计；属于统计隐私与鲁棒性背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/on-the-robustness-of-ldp-protocols-for-numerical-attributes-under-data-poisoning-attacks/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Onion Franking: Abuse Reports for Mix-Based Private Messaging

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/onion-franking-abuse-reports-for-mix-based-private-messaging/)。
- 判定依据：洋葱加密消息的可验证滥用举报与元数据保护；摘要贡献是协议机制，未评估具体测量型泄漏。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/onion-franking-abuse-reports-for-mix-based-private-messaging/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

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

## PBP: Post-training Backdoor Purification for Malware Classifiers

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/pbp-post-training-backdoor-purification-for-malware-classifiers/)。
- 判定依据：通过激活分布与批归一化清除恶意软件分类器后门；不是设备侧信道。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/pbp-post-training-backdoor-purification-for-malware-classifiers/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

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

## PQConnect: Automated Post-Quantum End-to-End Tunnels

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/pqconnect-automated-post-quantum-end-to-end-tunnels/)。
- 判定依据：PQC 隧道与 Tamarin 握手分析；附录承认 Python 时序和安全擦除问题，未提供相应侧信道防护证明，保留实现与引用背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/pqconnect-automated-post-quantum-end-to-end-tunnels/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Passive Inference Attacks on Split Learning via Adversarial Regularization

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/passive-inference-attacks-on-split-learning-via-adversarial-regularization/)。
- 判定依据：利用分割学习可见特征及辅助数据重建客户端输入，属于学习协议推断。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/passive-inference-attacks-on-split-learning-via-adversarial-regularization/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Phantom: Privacy-Preserving Deep Neural Network Model Obfuscation in Heterogeneous TEE and GPU System

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/bai-juyang)。
- 判定依据：TEE/GPU 异构系统中的 DNN 权重混淆与模型盗取防护；摘要没有侧信道观察模型。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## PhantomLiDAR: Cross-modality Signal Injection Attacks against LiDAR

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/phantomlidar-cross-modality-signal-injection-attacks-against-lidar/)。
- 判定依据：电磁注入干扰 LiDAR 内部模块及输出，非被动信息泄漏。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/phantomlidar-cross-modality-signal-injection-attacks-against-lidar/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## PolicyPulse: Precision Semantic Role Extraction for Enhanced Privacy Policy Comprehension

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/policypulse-precision-semantic-role-extraction-for-enhanced-privacy-policy-comprehension/)。
- 判定依据：用语义角色抽取改善隐私政策理解；文本分析背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/policypulse-precision-semantic-role-extraction-for-enhanced-privacy-policy-comprehension/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Posthammer: Pervasive Browser-based Rowhammer Attacks with Postponed Refresh Commands

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/de-ridder)。
- 判定依据：浏览器通过推迟刷新实施 Rowhammer 位翻转；主要为故障攻击。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## PowerRadio: Manipulate Sensor Measurement via Power GND Radiation

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/powerradio-manipulate-sensor-measurement-via-power-gnd-radiation/)。
- 判定依据：经共地线路耦合恶意信号改变传感器测量，保留 EMI 机制背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/powerradio-manipulate-sensor-measurement-via-power-gnd-radiation/。
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

## Privacy-Preserving Data Deduplication for Enhancing Federated Learning of Language Models

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/privacy-preserving-data-deduplication-for-enhancing-federated-learning-of-language-models/)。
- 判定依据：联邦学习的隐私去重与 PSI 协议，不以额外观察通道为贡献。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/privacy-preserving-data-deduplication-for-enhancing-federated-learning-of-language-models/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Probe-Me-Not: Protecting Pre-trained Encoders from Malicious Probing

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/probe-me-not-protecting-pre-trained-encoders-from-malicious-probing/)。
- 判定依据：限制预训练编码器在禁止领域的迁移用途；probing 指训练下游分类器，不是电路探测。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/probe-me-not-protecting-pre-trained-encoders-from-malicious-probing/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Prompt Inference Attack on Distributed Large Language Model Inference Frameworks

- 来源：[CCS 2025](https://doi.org/10.1145/3719027.3744820)。
- 判定依据：从分布式 LLM 传输的中间输出重建提示，摘要未显示额外物理或微架构观察；保留为相邻隐私研究，与 MoEcho 硬件侧信道区分。
- 阅读来源：https://arxiv.org/abs/2503.09291。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## PropertyGPT: LLM-driven Formal Verification of Smart Contracts through Retrieval-Augmented Property Generation

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/propertygpt-llm-driven-formal-verification-of-smart-contracts-through-retrieval-augmented-property-generation/)。
- 判定依据：LLM 检索生成智能合约性质并由证明器验证；研究工具方法背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/propertygpt-llm-driven-formal-verification-of-smart-contracts-through-retrieval-augmented-property-generation/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## ProvGuard: Detecting SDN Control Policy Manipulation via Contextual Semantics of Provenance Graphs

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/provguard-detecting-sdn-control-policy-manipulation-via-contextual-semantics-of-provenance-graphs/)。
- 判定依据：用控制器插桩和溯源图检测 SDN 策略操纵；显式活动日志与入侵检测背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/provguard-detecting-sdn-control-policy-manipulation-via-contextual-semantics-of-provenance-graphs/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Provably Unlearnable Data Examples

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/provably-unlearnable-data-examples/)。
- 判定依据：对抗扰动与参数平滑下的不可学习性认证；不是物理观测泄漏。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/provably-unlearnable-data-examples/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Proving Faster Implementations Faster: Combining Deductive and Circuit-Based Reasoning in EasyCrypt

- 来源：[SP 2025](https://www.ieee-security.org/TC/SP2025/accepted-papers.html#collapse-166)。
- 判定依据：混合推演与电路等价检查用于 ML-KEM 优化代码的功能正确性。所读正文另介绍 Jasmin 对恒时/推测恒时属性的保持能力；功能等价证明本身不等于这些属性或模拟泄漏的证明。按功能验证与工具链背景保留。出版题名为 Faster Verification of Faster Implementations，录用目录的 Proving Faster Implementations Faster 是同一论文的题名别名。
- 阅读来源：https://xplorestaging.ieee.org/document/11023411/ ; https://cryptosith.org/papers/mapreduce-20250907.pdf。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## QMSan: Efficiently Detecting Uninitialized Memory Errors During Fuzzing

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/qmsan-efficiently-detecting-uninitialized-memory-errors-during-fuzzing/)。
- 判定依据：QEMU 动态翻译支持未初始化内存错误检测；内存安全测试背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/qmsan-efficiently-detecting-uninitialized-memory-errors-during-fuzzing/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

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

## RACONTEUR: A Knowledgeable, Insightful, and Portable LLM-Powered Shell Command Explainer

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/raconteur-a-knowledgeable-insightful-and-portable-llm-powered-shell-command-explainer/)。
- 判定依据：结合专业知识和检索解释 shell 命令；安全分析工具背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/raconteur-a-knowledgeable-insightful-and-portable-llm-powered-shell-command-explainer/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## RAIFLE: Reconstruction Attacks on Interaction-based Federated Learning with Adversarial Data Manipulation

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/raifle-reconstruction-attacks-on-interaction-based-federated-learning-with-adversarial-data-manipulation/)。
- 判定依据：服务器操纵推荐项特征并从联邦学习交互重建用户信息；主动模型/更新反演相邻主题。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/raifle-reconstruction-attacks-on-interaction-based-federated-learning-with-adversarial-data-manipulation/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## RContainer: A Secure Container Architecture through Extending ARM CCA Hardware Primitives

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/rcontainer-a-secure-container-architecture-through-extending-arm-cca-hardware-primitives/)。
- 判定依据：扩展 ARM CCA 的容器隔离架构；摘要不支持物理或微架构侧信道安全断言。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/rcontainer-a-secure-container-architecture-through-extending-arm-cca-hardware-primitives/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## REED: Chiplet-based Accelerator for Fully Homomorphic Encryption

- 来源：[TCHES 2025](https://doi.org/10.46586/tches.v2025.i2.163-208)。
- 判定依据：REED 以 chiplet、通信和存储设计加速 FHE；其布局前功耗模拟是能效评估，不是秘密可辨识性验证。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## RISCover: Automatic Discovery of User-exploitable Architectural Security Vulnerabilities in Closed-Source RISC-V CPUs

- 来源：[CCS 2025](https://doi.org/10.1145/3719027.3765141)。
- 判定依据：在真实 RISC-V CPU 上进行架构差分模糊测试，发现直接物理内存写入及其他架构错误；摘要未展示侧信道推断，不能将 GhostWrite 的直接原语计作微架构测量攻击。
- 阅读来源：https://ghostwriteattack.com/riscover_ccs25.pdf。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## RMPocalypse: How a Catch-22 Breaks AMD SEV-SNP

- 来源：[CCS 2025](https://doi.org/10.1145/3719027.3765233)。
- 判定依据：通过 RMP 初始化的硬件访问控制缺口破坏 SEV-SNP，演示调试开启、证明欺骗、状态重放和代码注入；保留相邻机密计算隔离研究，与观察泄漏分开。
- 阅读来源：https://rmpocalypse.github.io/rmpocalypse-CCS2025.pdf。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## ReThink: Reveal the Threat of Electromagnetic Interference on Power Inverters

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/rethink-reveal-the-threat-of-electromagnetic-interference-on-power-inverters/)。
- 判定依据：电磁干扰欺骗逆变器电压电流传感器，主要是可用性和物理完整性攻击。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/rethink-reveal-the-threat-of-electromagnetic-interference-on-power-inverters/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Recurrent Private Set Intersection for Unbalanced Databases with Cuckoo Hashing and Leveled FHE

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/recurrent-private-set-intersection-for-unbalanced-databases-with-cuckoo-hashing-and-leveled-fhe/)。
- 判定依据：不平衡集合的可重复 PSI 与同态加密性能优化，非侧信道研究。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/recurrent-private-set-intersection-for-unbalanced-databases-with-cuckoo-hashing-and-leveled-fhe/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Rediscovering Method Confusion in Proposed Security Fixes for Bluetooth

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/rediscovering-method-confusion-in-proposed-security-fixes-for-bluetooth/)。
- 判定依据：蓝牙配对方法混淆、协议攻击和形式化修复；未建立功耗、时序或其他测量型泄漏。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/rediscovering-method-confusion-in-proposed-security-fixes-for-bluetooth/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Reinforcement Unlearning

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/reinforcement-unlearning/)。
- 判定依据：强化学习中的环境遗忘及环境推断评估；模型隐私背景，不是芯片记忆。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/reinforcement-unlearning/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Repurposing Neural Networks for Efficient Cryptographic Computation

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/repurposing-neural-networks-for-efficient-cryptographic-computation/)。
- 判定依据：将密码运算翻译成神经网络计算图以使用加速器；功能与算法安全表述不等于实现恒时或物理安全。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/repurposing-neural-networks-for-efficient-cryptographic-computation/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Resolution Without Dissent: In-Path Per-Query Sanitization to Defeat Surreptitious Communication Over DNS

- 来源：[SP 2025](https://www.ieee-security.org/TC/SP2025/accepted-papers.html#collapse-75)。
- 判定依据：TunTight 识别并阻断 DNS 域名中承载的隧道通信，属于显式数据外传及检测背景；不能仅凭 covert/exfiltration 用词纳入非预期实现泄漏。
- 阅读来源：https://xplorestaging.ieee.org/document/11023297/。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Rethinking Trust in Forge-Based Git Security

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/rethinking-trust-in-forge-based-git-security/)。
- 判定依据：gittuf 分散仓库政策、活动追踪与授权验证；供应链完整性背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/rethinking-trust-in-forge-based-git-security/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Retrofitting XoM for Stripped Binaries without Embedded Data Relocation

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/retrofitting-xom-for-stripped-binaries-without-embedded-data-relocation/)。
- 判定依据：以 MPK 加固执行只读内存并限制 JIT-ROP 的直接代码读取，未见侧信道保证。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/retrofitting-xom-for-stripped-binaries-without-embedded-data-relocation/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Revealing the Black Box of Device Search Engine: Scanning Assets, Strategies, and Ethical Consideration

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/revealing-the-black-box-of-device-search-engine-scanning-assets-strategies-and-ethical-consideration/)。
- 判定依据：通过蜜罐观察搜索引擎扫描行为并检查公开结果的隐私问题；直接网络行为和数据发布研究。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/revealing-the-black-box-of-device-search-engine-scanning-assets-strategies-and-ethical-consideration/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Revisiting Concept Drift in Windows Malware Detection: Adaptation to Real Drifted Malware with Minimal Samples

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/revisiting-concept-drift-in-windows-malware-detection-adaptation-to-real-drifted-malware-with-minimal-samples/)。
- 判定依据：用图网络与域适应改善漂移恶意软件检测；跨分布学习方法背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/revisiting-concept-drift-in-windows-malware-detection-adaptation-to-real-drifted-malware-with-minimal-samples/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Revisiting EM-based Estimation for Locally Differentially Private Protocols

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/revisiting-em-based-estimation-for-locally-differentially-private-protocols/)。
- 判定依据：LDP 中基于混合模型的 EM 估计；EM 是期望最大化算法，不是电磁泄漏。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/revisiting-em-based-estimation-for-locally-differentially-private-protocols/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Revisiting Physical-World Adversarial Attack on Traffic Sign Recognition: A Commercial Systems Perspective

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/revisiting-physical-world-adversarial-attack-on-traffic-sign-recognition-a-commercial-systems-perspective/)。
- 判定依据：交通标志对抗扰动与商业识别系统的空间记忆；主动感知欺骗，不是秘密旁路观测。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/revisiting-physical-world-adversarial-attack-on-traffic-sign-recognition-a-commercial-systems-perspective/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Ring of Gyges: Accountable Anonymous Broadcast via Secret-Shared Shuffle

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/ring-of-gyges-accountable-anonymous-broadcast-via-secret-shared-shuffle/)。
- 判定依据：四方秘密共享混洗与可追责匿名广播；协议匿名性背景，未报告物理份额泄漏。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/ring-of-gyges-accountable-anonymous-broadcast-via-secret-shared-shuffle/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## RollingEvidence: Autoregressive Video Evidence via Rolling Shutter Effect

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/qian)。
- 判定依据：用滚动快门主动嵌入视频完整性验证探针；主要为取证编码，不是非预期秘密观察。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Rondo: Scalable and Reconfiguration-Friendly Randomness Beacon

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/rondo-scalable-and-reconfiguration-friendly-randomness-beacon/)。
- 判定依据：分布式随机信标和可重配置共识，未研究随机源的物理泄漏。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/rondo-scalable-and-reconfiguration-friendly-randomness-beacon/。
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

## SCAMMAGNIFIER: Piercing the Veil of Fraudulent Shopping Website Campaigns

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/scammagnifier-piercing-the-veil-of-fraudulent-shopping-website-campaigns/)。
- 判定依据：购物域名、结账和商户标识分析以识别诈骗；直接交易生态测量。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/scammagnifier-piercing-the-veil-of-fraudulent-shopping-website-campaigns/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## SCRUTINIZER: Towards Secure Forensics on Compromised TrustZone

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/scrutinizer-towards-secure-forensics-on-compromised-trustzone/)。
- 判定依据：用 ARM CCA 执行可信取证和指令追踪，是授权观察能力设计，未见秘密推断侧信道。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/scrutinizer-towards-secure-forensics-on-compromised-trustzone/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## SHAFT: Secure, Handy, Accurate and Fast Transformer Inference

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/shaft-secure-handy-accurate-and-fast-transformer-inference/)。
- 判定依据：安全 softmax/GELU 协议和 Transformer 部署，未报告额外侧信道。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/shaft-secure-handy-accurate-and-fast-transformer-inference/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## SIGuard: Guarding Secure Inference with Post Data Privacy

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/siguard-guarding-secure-inference-with-post-data-privacy/)。
- 判定依据：安全推理的合法预测输出仍可用于成员推断；属于输出隐私而非硬件侧信道。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/siguard-guarding-secure-inference-with-post-data-privacy/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## SKILLPoV: Towards Accessible and Effective Privacy Notice for Amazon Alexa Skills

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/skillpov-towards-accessible-and-effective-privacy-notice-for-amazon-alexa-skills/)。
- 判定依据：Alexa 技能的语音隐私告知及代码插桩；声音是告知界面，不是窃听通道。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/skillpov-towards-accessible-and-effective-privacy-notice-for-amazon-alexa-skills/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## SafeSplit: A Novel Defense Against Client-Side Backdoor Attacks in Split Learning

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/safesplit-a-novel-defense-against-client-side-backdoor-attacks-in-split-learning/)。
- 判定依据：拆分学习后门防护；频域和旋转距离描述模型参数变化，不是采集波形。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/safesplit-a-novel-defense-against-client-side-backdoor-attacks-in-split-learning/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Safety Misalignment Against Large Language Models

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/safety-misalignment-against-large-language-models/)。
- 判定依据：LLM 提示、微调和编辑造成安全失配及其防护；模型行为安全背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/safety-misalignment-against-large-language-models/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Save what must be saved: Secure context switching with Sailor

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/kalani)。
- 判定依据：从 Sail ISA 规范推导上下文切换必须保存的架构状态；摘要未明确旁路观察，保留隔离及架构泄漏背景。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Scale-MIA: A Scalable Model Inversion Attack against Secure Federated Learning via Latent Space Reconstruction

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/scale-mia-a-scalable-model-inversion-attack-against-secure-federated-learning-via-latent-space-reconstruction/)。
- 判定依据：从聚合模型更新和精心构造的层进行数据反演；不是物理聚合功耗推断。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/scale-mia-a-scalable-model-inversion-attack-against-secure-federated-learning-via-latent-space-reconstruction/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## ScopeVerif: Analyzing the Security of Android’s Scoped Storage via Differential Analysis

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/scopeverif-analyzing-the-security-of-androids-scoped-storage-via-differential-analysis/)。
- 判定依据：差分检查 Android 分区存储操作是否违反访问策略；文件访问权限缺陷。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/scopeverif-analyzing-the-security-of-androids-scoped-storage-via-differential-analysis/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Secure Data Analytics in Apache Spark with Fine-grained Policy Enforcement and Isolated Execution

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/secure-data-analytics-in-apache-spark-with-fine-grained-policy-enforcement-and-isolated-execution/)。
- 判定依据：Spark 分析计划的访问策略及可信执行，不是数据无关或物理泄漏证明。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/secure-data-analytics-in-apache-spark-with-fine-grained-policy-enforcement-and-isolated-execution/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Secure IP Address Allocation at Cloud Scale

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/secure-ip-address-allocation-at-cloud-scale/)。
- 判定依据：云 IP 地址动态分配、扫描与误投递流量保护，摘要不提出时序或资源侧信道。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/secure-ip-address-allocation-at-cloud-scale/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Secure Information Embedding in Forensic 3D Fingerprinting

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/wang-canran)。
- 判定依据：在三维打印品中主动嵌入抗破坏标识；为取证水印，不是实现侧信道。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Secure Transformer Inference Made Non-interactive

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/secure-transformer-inference-made-non-interactive/)。
- 判定依据：非交互安全 Transformer 推理与同态计算，协议带宽优化不等于实现侧信道防护。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/secure-transformer-inference-made-non-interactive/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Securing BGP ASAP: ASPA and other Post-ROV Defenses

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/securing-bgp-asap-aspa-and-other-post-rov-defenses/)。
- 判定依据：BGP 路由劫持、路由泄漏及 ASPA 防护；route leakage 不指秘密侧信道。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/securing-bgp-asap-aspa-and-other-post-rov-defenses/。
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

## Sheep’s Clothing, Wolf’s Data: Detecting Server-Induced Client Vulnerabilities in Windows Remote IPC

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/sheeps-clothing-wolfs-data-detecting-server-induced-client-vulnerabilities-in-windows-remote-ipc/)。
- 判定依据：通过操纵 Windows IPC 返回值测试客户端漏洞；主动输入与内存安全问题。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/sheeps-clothing-wolfs-data-detecting-server-induced-client-vulnerabilities-in-windows-remote-ipc/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Sieving with Streaming Memory Access

- 来源：[TCHES 2025](https://doi.org/10.46586/tches.v2025.i2.362-384)。
- 判定依据：研究格筛的访存成本和 SVP 攻击资源估计，属于数学安全与后处理背景；不是观测受害实现的缓存攻击。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Silence False Alarms: Identifying Anti-Reentrancy Patterns on Ethereum to Refine Smart Contract Reentrancy Detection

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/silence-false-alarms-identifying-anti-reentrancy-patterns-on-ethereum-to-refine-smart-contract-reentrancy-detection/)。
- 判定依据：通过图表示和聚类识别智能合约防重入模式；静态分析方法背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/silence-false-alarms-identifying-anti-reentrancy-patterns-on-ethereum-to-refine-smart-contract-reentrancy-detection/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Singular Points of UOV and VOX

- 来源：[EUROCRYPT 2025](https://doi.org/10.1007/978-3-031-91095-1_11)。
- 判定依据：EUROCRYPT 2025 正式代数分析，建立与实际被引 ePrint 的显式关系；不是已完成侧信道采集或一般 UOV 失效的证据。
- 阅读来源：https://link.springer.com/chapter/10.1007/978-3-031-91095-1_11。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Siniel: Distributed Privacy-Preserving zkSNARK

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/siniel-distributed-privacy-preserving-zksnark/)。
- 判定依据：将 zkSNARK 证明生成委托给多个工作者并保护见证；协议隐私和效率，不是物理实现评估。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/siniel-distributed-privacy-preserving-zksnark/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

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

## SongBsAb: A Dual Prevention Approach against Singing Voice Conversion based Illegal Song Covers

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/songbsab-a-dual-prevention-approach-against-singing-voice-conversion-based-illegal-song-covers/)。
- 判定依据：对歌声添加扰动以阻止未授权声音转换；主动输入保护，不是被动声学泄漏。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/songbsab-a-dual-prevention-approach-against-singing-voice-conversion-based-illegal-song-covers/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Spatial-Domain Wireless Jamming with Reconfigurable Intelligent Surfaces

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/spatial-domain-wireless-jamming-with-reconfigurable-intelligent-surfaces/)。
- 判定依据：可重构智能表面对无线干扰进行空间定向，属于信号压制。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/spatial-domain-wireless-jamming-with-reconfigurable-intelligent-surfaces/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Starshields for iOS: Navigating the Security Cosmos in Satellite Communication

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/starshields-for-ios-navigating-the-security-cosmos-in-satellite-communication/)。
- 判定依据：iOS 卫星消息协议的完整性缺陷与限制绕过；摘要中的位置消息滥用是显式协议字段通道。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/starshields-for-ios-navigating-the-security-cosmos-in-satellite-communication/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Statically Discover Cross-Entry Use-After-Free Vulnerabilities in the Linux Kernel

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/statically-discover-cross-entry-use-after-free-vulnerabilities-in-the-linux-kernel/)。
- 判定依据：跨入口别名分析与偏序约束检测 Linux UAF；程序内存安全背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/statically-discover-cross-entry-use-after-free-vulnerabilities-in-the-linux-kernel/。
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

## THEMIS: Regulating Textual Inversion for Personalized Concept Censorship

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/themis-regulating-textual-inversion-for-personalized-concept-censorship/)。
- 判定依据：向文本反演嵌入加入触发机制以限制个性化图像概念；模型用途治理。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/themis-regulating-textual-inversion-for-personalized-concept-censorship/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## THEMIS: Towards Practical Intellectual Property Protection for Post-Deployment On-Device Deep Learning Models

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/huang-yujin)。
- 判定依据：从部署 DNN 重建可写模型并加水印，保护知识产权；非侧信道。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## TME-Box: Scalable In-Process Isolation through Intel TME-MK Memory Encryption

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/tme-box-scalable-in-process-isolation-through-intel-tme-mk-memory-encryption/)。
- 判定依据：利用 TME-MK 与编译器插桩进行进程内隔离；内存加密不能自动当作全侧信道防护。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/tme-box-scalable-in-process-isolation-through-intel-tme-mk-memory-encryption/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## TWINFUZZ: Differential Testing of Video Hardware Acceleration Stacks

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/twinfuzz-differential-testing-of-video-hardware-acceleration-stacks/)。
- 判定依据：正文的设备指纹来自特制视频的解码输出差异，另有跨标签页内容直接泄漏；保留功能差异与测试方法背景，不混同时间、共享资源或电磁侧信道。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/twinfuzz-differential-testing-of-video-hardware-acceleration-stacks/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## TZ-DATASHIELD: Automated Data Protection for Embedded Systems via Data-Flow-Based Compartmentalization

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/tz-datashield-automated-data-protection-for-embedded-systems-via-data-flow-based-compartmentalization/)。
- 判定依据：TrustZone 数据流分区和控制流完整性，未见物理或微架构泄漏评估。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/tz-datashield-automated-data-protection-for-embedded-systems-via-data-flow-based-compartmentalization/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## The (Un)usual Suspects – Studying Reasons for Lacking Updates in WordPress

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/the-unusual-suspects-studying-reasons-for-lacking-updates-in-wordpress/)。
- 判定依据：访谈研究 WordPress 网站缺乏更新的原因；用户与运营行为研究。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/the-unusual-suspects-studying-reasons-for-lacking-updates-in-wordpress/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## The Forking Way: When TEEs Meet Consensus

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/the-forking-way-when-tees-meet-consensus/)。
- 判定依据：TEE 与区块链组合中的分叉攻击，非物理或时序泄漏。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/the-forking-way-when-tees-meet-consensus/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## The Guardians of Name Street: Studying the Defensive Registration Practices of the Fortune 500

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/the-guardians-of-name-street-studying-the-defensive-registration-practices-of-the-fortune-500/)。
- 判定依据：防御性域名注册与 DNS 查询统计；域名滥用治理，不是秘密测量推断。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/the-guardians-of-name-street-studying-the-defensive-registration-practices-of-the-fortune-500/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## The Kids Are All Right: Investigating the Susceptibility of Teens and Adults to YouTube Giveaway Scams

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/the-kids-are-all-right-investigating-the-susceptibility-of-teens-and-adults-to-youtube-giveaway-scams/)。
- 判定依据：青少年和成人对 YouTube 赠品诈骗的辨别；社会工程与用户研究。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/the-kids-are-all-right-investigating-the-susceptibility-of-teens-and-adults-to-youtube-giveaway-scams/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## The Midas Touch: Triggering the Capability of LLMs for RM-API Misuse Detection

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/the-midas-touch-triggering-the-capability-of-llms-for-rm-api-misuse-detection/)。
- 判定依据：LLM 提取资源管理 API 约束并辅助 CodeQL 检错；研究工具方法背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/the-midas-touch-triggering-the-capability-of-llms-for-rm-api-misuse-detection/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## The Philosopher’s Stone: Trojaning Plugins of Large Language Models

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/the-philosophers-stone-trojaning-plugins-of-large-language-models/)。
- 判定依据：低秩适配器投毒使 LLM 输出或工具调用被操纵；后门攻击背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/the-philosophers-stone-trojaning-plugins-of-large-language-models/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## The Power of Words: A Comprehensive Analysis of Rationales and Their Effects on Users’ Permission Decisions

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/the-power-of-words-a-comprehensive-analysis-of-rationales-and-their-effects-on-users-permission-decisions/)。
- 判定依据：应用权限请求理由及其对用户决策的影响；可用安全研究。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/the-power-of-words-a-comprehensive-analysis-of-rationales-and-their-effects-on-users-permission-decisions/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## The Road to Trust: Building Enclaves within Confidential VMs

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/the-road-to-trust-building-enclaves-within-confidential-vms/)。
- 判定依据：SEV-SNP 中模拟 SGX enclave 的完整性与兼容性架构，摘要未建立侧信道保护。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/the-road-to-trust-building-enclaves-within-confidential-vms/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## The Skeleton Keys: A Large Scale Analysis of Credential Leakage in Mini-apps

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/the-skeleton-keys-a-large-scale-analysis-of-credential-leakage-in-mini-apps/)。
- 判定依据：小程序凭据机制中的直接密钥/令牌暴露与语义验证；不是密码能耗或时序恢复。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/the-skeleton-keys-a-large-scale-analysis-of-credential-leakage-in-mini-apps/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Time-varying Bottleneck Links in LEO Satellite Networks: Identification, Exploits, and Countermeasures

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/time-varying-bottleneck-links-in-leo-satellite-networks-identification-exploits-and-countermeasures/)。
- 判定依据：正文以公开轨道、流量信息和模拟识别瓶颈并分析链路洪泛；延迟推断仅为背景条件，当前贡献归为网络可用性相邻研究。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/time-varying-bottleneck-links-in-leo-satellite-networks-identification-exploits-and-countermeasures/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## TimeTravel: Real-time Timing Drift Attack on System Time Using Acoustic Waves

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/liu-jianshuo)。
- 判定依据：利用声波操纵 RTC 石英振荡器造成时钟漂移；属于主动完整性/信号注入，而非被动读出。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Too Subtle to Notice: Investigating Executable Stack Issues in Linux Systems

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/too-subtle-to-notice-investigating-executable-stack-issues-in-linux-systems/)。
- 判定依据：编译工具链、加载器与内核对可执行栈的共同影响；W xor X 配置与内存安全。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/too-subtle-to-notice-investigating-executable-stack-issues-in-linux-systems/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Towards Practical, End-to-End Formally Verified X.509 Certificate Validators with Verdict

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/lin-zhengyao)。
- 判定依据：X.509 解析、构建及验证策略正确性；摘要未给侧信道保证。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Towards Understanding Unsafe Video Generation

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/towards-understanding-unsafe-video-generation/)。
- 判定依据：视频生成的有害内容及采样阶段过滤；sampling 指扩散生成步骤，不是测量采样。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/towards-understanding-unsafe-video-generation/。
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

## TrajDeleter: Enabling Trajectory Forgetting in Offline Reinforcement Learning Agents

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/trajdeleter-enabling-trajectory-forgetting-in-offline-reinforcement-learning-agents/)。
- 判定依据：离线强化学习轨迹遗忘及审计；训练数据隐私背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/trajdeleter-enabling-trajectory-forgetting-in-offline-reinforcement-learning-agents/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Translating C To Rust: Lessons from a User Study

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/translating-c-to-rust-lessons-from-a-user-study/)。
- 判定依据：人工将 C 迁移为安全 Rust 的用户研究；内存安全与实现方法背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/translating-c-to-rust-lessons-from-a-user-study/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Transparency or Information Overload? Evaluating Users’ Comprehension and Perceptions of the iOS App Privacy Report

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/transparency-or-information-overload-evaluating-users-comprehension-and-perceptions-of-the-ios-app-privacy-report/)。
- 判定依据：用户对 iOS 隐私报告中传感器访问和域名活动的理解；可用隐私研究。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/transparency-or-information-overload-evaluating-users-comprehension-and-perceptions-of-the-ios-app-privacy-report/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Transparent Attested DNS for Confidential Computing Services

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/delignat-lavaud)。
- 判定依据：通过 DNS 名称绑定 TEE 远程证明并作透明日志；协议认证不等于消除侧信道。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Truman: Constructing Device Behavior Models from OS Drivers to Fuzz Virtual Devices

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/truman-constructing-device-behavior-models-from-os-drivers-to-fuzz-virtual-devices/)。
- 判定依据：从驱动推导设备行为模型并测试虚拟设备；依赖建模方法背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/truman-constructing-device-behavior-models-from-os-drivers-to-fuzz-virtual-devices/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Try to Poison My Deep Learning Data? Nowhere to Hide Your Trajectory Spectrum!

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/try-to-poison-my-deep-learning-data-nowhere-to-hide-your-trajectory-spectrum/)。
- 判定依据：在训练轨迹谱域识别投毒样本；谱特征来自模型训练，不是硬件响应。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/try-to-poison-my-deep-learning-data-nowhere-to-hide-your-trajectory-spectrum/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Tweezers: A Framework for Security Event Detection via Event Attribution-centric Tweet Embedding

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/tweezers-a-framework-for-security-event-detection-via-event-attribution-centric-tweet-embedding/)。
- 判定依据：从推文嵌入识别安全事件与威胁情报；文本与图分析背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/tweezers-a-framework-for-security-event-detection-via-event-attribution-centric-tweet-embedding/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## UI-CTX: Understanding UI Behaviors with Code Contexts for Mobile Applications

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/ui-ctx-understanding-ui-behaviors-with-code-contexts-for-mobile-applications/)。
- 判定依据：结合 UI 处理图和代码语义解释控件行为；显式程序分析背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/ui-ctx-understanding-ui-behaviors-with-code-contexts-for-mobile-applications/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## URVFL: Undetectable Data Reconstruction Attack on Vertical Federated Learning

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/urvfl-undetectable-data-reconstruction-attack-on-vertical-federated-learning/)。
- 判定依据：通过恶意梯度与标签信息重建纵向联邦学习数据；模型更新反演背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/urvfl-undetectable-data-reconstruction-attack-on-vertical-federated-learning/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Uncovering the iceberg from the tip: Generating API Specifications for Bug Detection via Specification Propagation Analysis

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/uncovering-the-iceberg-from-the-tip-generating-api-specifications-for-bug-detection-via-specification-propagation-analysis/)。
- 判定依据：沿调用关系传播 API 规格以发现误用；验证方法背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/uncovering-the-iceberg-from-the-tip-generating-api-specifications-for-bug-detection-via-specification-propagation-analysis/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Understanding Data Importance in Machine Learning Attacks: Does Valuable Data Pose Greater Harm?

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/understanding-data-importance-in-machine-learning-attacks-does-valuable-data-pose-greater-harm/)。
- 判定依据：分析数据价值与成员推断、模型窃取等攻击的关系；模型隐私背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/understanding-data-importance-in-machine-learning-attacks-does-valuable-data-pose-greater-harm/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Understanding Miniapp Malware: Identification, Dissection, and Characterization

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/understanding-miniapp-malware-identification-dissection-and-characterization/)。
- 判定依据：收集并分析恶意小程序的生命周期和隐私滥用；生态行为与直接数据访问。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/understanding-miniapp-malware-identification-dissection-and-characterization/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Unleashing the Power of Generative Model in Recovering Variable Names from Stripped Binary

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/unleashing-the-power-of-generative-model-in-recovering-variable-names-from-stripped-binary/)。
- 判定依据：利用生成模型恢复被剥离二进制的变量名；逆向理解工具，不等于秘密恢复。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/unleashing-the-power-of-generative-model-in-recovering-variable-names-from-stripped-binary/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## VeloFHE: GPU Acceleration for FHEW and TFHE Bootstrapping

- 来源：[TCHES 2025](https://doi.org/10.46586/tches.v2025.i3.81-114)。
- 判定依据：VeloFHE 通过 GPU NTT、批处理与异步执行优化 FHEW/TFHE 自举，摘要未研究侧信道。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## VeriBin: Adaptive Verification of Patches at the Binary Level

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/veribin-adaptive-verification-of-patches-at-the-binary-level/)。
- 判定依据：对二进制补丁作符号执行和功能等价验证；方法背景，功能等价不等于泄漏等价。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/veribin-adaptive-verification-of-patches-at-the-binary-level/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## VoiceRadar: Voice Deepfake Detection using Micro-Frequency and Compositional Analysis

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/voiceradar-voice-deepfake-detection-using-micro-frequency-and-compositional-analysis/)。
- 判定依据：用物理启发的频率模型识别音频深度伪造；输入是待鉴别音频本身，未建立设备旁路泄漏。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/voiceradar-voice-deepfake-detection-using-micro-frequency-and-compositional-analysis/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## VulShield: Protecting Vulnerable Code Before Deploying Patches

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/vulshield-protecting-vulnerable-code-before-deploying-patches/)。
- 判定依据：依据 sanitizer 报告生成内核执行策略以临时阻止漏洞触发；内存安全缓解。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/vulshield-protecting-vulnerable-code-before-deploying-patches/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Vulnerability, Where Art Thou? An Investigation of Vulnerability Management in Android Smartphone Chipsets

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/vulnerability-where-art-thou-an-investigation-of-vulnerability-management-in-android-smartphone-chipsets/)。
- 判定依据：Android 芯片漏洞披露、继承与修补生命周期研究；不凭芯片关键词认定侧信道。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/vulnerability-where-art-thou-an-investigation-of-vulnerability-management-in-android-smartphone-chipsets/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## WAVEN: WebAssembly Memory Virtualization for Enclaves

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/waven-webassembly-memory-virtualization-for-enclaves/)。
- 判定依据：Wasm enclave 的跨模块内存共享与细粒度访问控制，未涉及侧信道机制。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/waven-webassembly-memory-virtualization-for-enclaves/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Wanilla: Sound Noninterference Analysis for WebAssembly

- 来源：[CCS 2025](https://doi.org/10.1145/3719027.3765156)。
- 判定依据：为 WebAssembly 提供静态非干扰与内存完整性分析；摘要没有明确的计时/物理泄漏模型，保留相邻层，不能由 noninterference 标题自动当作侧信道证明。
- 阅读来源：https://arxiv.org/abs/2509.08758。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Was This You? Investigating the Design Considerations for Suspicious Login Notifications

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/was-this-you-investigating-the-design-considerations-for-suspicious-login-notifications/)。
- 判定依据：可疑登录邮件通知的设计与用户理解；认证可用性研究。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/was-this-you-investigating-the-design-considerations-for-suspicious-login-notifications/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Welcome to Jurassic Park: A Comprehensive Study of Security Risks in Deno and its Ecosystem

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/welcome-to-jurassic-park-a-comprehensive-study-of-security-risks-in-deno-and-its-ecosystem/)。
- 判定依据：Deno 权限、导入、符号链接和供应链问题；直接访问控制缺陷。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/welcome-to-jurassic-park-a-comprehensive-study-of-security-risks-in-deno-and-its-ecosystem/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## What’s Done Is Not What’s Claimed: Detecting and Interpreting Inconsistencies in App Behaviors

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/whats-done-is-not-whats-claimed-detecting-and-interpreting-inconsistencies-in-app-behaviors/)。
- 判定依据：比较用户预期和应用代码行为以发现未授权数据访问；直接隐私披露，不是波形推断。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/whats-done-is-not-whats-claimed-detecting-and-interpreting-inconsistencies-in-app-behaviors/。
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

## YuraScanner: Leveraging LLMs for Task-driven Web App Scanning

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/yurascanner-leveraging-llms-for-task-driven-web-app-scanning/)。
- 判定依据：LLM 驱动 Web 工作流扫描与 XSS 发现；主动软件测试方法。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/yurascanner-leveraging-llms-for-task-driven-web-app-scanning/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## eSIMplicity or eSIMplification? Privacy and Security Risks in the eSIM Ecosystem

- 来源：[USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/motallebighomi)。
- 判定依据：eSIM 提供商、路由与配置生态隐私；非实现侧信道。
- 阅读来源：https://www.usenix.org/conference/usenixsecurity25/technical-sessions。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## type++: Prohibiting Type Confusion with Inline Type Information

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/type-prohibiting-type-confusion-with-inline-type-information/)。
- 判定依据：通过内联类型信息防止 C++ 类型混淆；程序内存安全。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/type-prohibiting-type-confusion-with-inline-type-information/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## “Where Are We On Cyber?” – A Qualitative Study On Boards’ Cybersecurity Risk Decision Making

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/where-are-we-on-cyber-a-qualitative-study-on-boards-cybersecurity-risk-decision-making/)。
- 判定依据：董事会网络安全风险决策的访谈；组织治理研究。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/where-are-we-on-cyber-a-qualitative-study-on-boards-cybersecurity-risk-decision-making/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## ”Who is Trying to Access My Account?” Exploring User Perceptions and Reactions to Risk-based Authentication Notifications

- 来源：[NDSS 2025](https://www.ndss-symposium.org/ndss-paper/who-is-trying-to-access-my-account-exploring-user-perceptions-and-reactions-to-risk-based-authentication-notifications/)。
- 判定依据：用户对风险认证通知的认知和反应；可用认证研究。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/who-is-trying-to-access-my-account-exploring-user-perceptions-and-reactions-to-risk-based-authentication-notifications/。
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

## ANONYCALL: Enabling Native Private Calling in Mobile Networks

- 来源：[NDSS 2026](https://www.ndss-symposium.org/ndss-paper/anonycall-enabling-native-private-calling-in-mobile-networks/)。
- 判定依据：匿名呼叫发现与计费凭据的协议隐私设计，未报告流量或实现侧信道。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/anonycall-enabling-native-private-calling-in-mobile-networks/。
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

## Analysis of the Security Design, Engineering, and Implementation of the SecureDNA System

- 来源：[NDSS 2026](https://www.ndss-symposium.org/ndss-paper/analysis-of-the-security-design-engineering-and-implementation-of-the-securedna-system/)。
- 判定依据：SecureDNA 的协议认证、绑定与限速漏洞，摘要没有额外时序或物理侧信道机制。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/analysis-of-the-security-design-engineering-and-implementation-of-the-securedna-system/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Analyzing Cryptography in Context: A Cryptography-Native Approach to Threat Modeling

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/canetti)。
- 判定依据：密码协议的社会技术威胁建模；未评价实现泄漏。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Are your Sites Truly Isolated? Automatically Detecting Logic Bugs in Site Isolation Implementations

- 来源：[NDSS 2026](https://www.ndss-symposium.org/ndss-paper/are-your-sites-truly-isolated-automatically-detecting-logic-bugs-in-site-isolation-implementations/)。
- 判定依据：通过恶意 IPC 绕过站点隔离；提及 Spectre 是背景，实际新漏洞为直接跨站访问。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/are-your-sites-truly-isolated-automatically-detecting-logic-bugs-in-site-isolation-implementations/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Auditing Apple’s DifferentialPrivacy.framework: Implementation Bugs, Misconfigurations, and Practical Risks

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00225)。
- 判定依据：审计差分隐私浮点噪声及上传日志的协议输出风险；非本库实现侧信道纳入数，保留数值/隐私背景。
- 阅读来源：https://xplorestaging.ieee.org/document/11573572/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Automated Code Annotation with LLMs for Establishing TEE Boundaries

- 来源：[NDSS 2026](https://www.ndss-symposium.org/ndss-paper/automated-code-annotation-with-llms-for-establishing-tee-boundaries/)。
- 判定依据：用 LLM 识别应放入 TEE 的代码区域，分类准确率不能视为侧信道保护证明。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/automated-code-annotation-with-llms-for-establishing-tee-boundaries/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## BACnet or “BADnet”? On the (In)Security of Implicitly Reserved Fields in BACnet

- 来源：[NDSS 2026](https://www.ndss-symposium.org/ndss-paper/bacnet-or-badnet-on-the-insecurity-of-implicitly-reserved-fields-in-bacnet/)。
- 判定依据：保留字段和令牌占用导致的协议漏洞及 fuzzing，非秘密推断侧信道。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/bacnet-or-badnet-on-the-insecurity-of-implicitly-reserved-fields-in-bacnet/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## BKPIR: Keyword PIR for Private Boolean Retrieval

- 来源：[NDSS 2026](https://www.ndss-symposium.org/ndss-paper/bkpir-keyword-pir-for-private-boolean-retrieval/)。
- 判定依据：支持布尔查询的 PIR 协议设计，摘要未分析额外访问模式或物理泄漏。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/bkpir-keyword-pir-for-private-boolean-retrieval/。
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

## Better Safe than Sorry: Uncovering the Insecure Resource Management in App-in-App Cloud Services

- 来源：[NDSS 2026](https://www.ndss-symposium.org/ndss-paper/better-safe-than-sorry-uncovering-the-insecure-resource-management-in-app-in-app-cloud-services/)。
- 判定依据：小程序云资源的鉴权缺陷导致直接访问，非共享物理资源泄漏。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/better-safe-than-sorry-uncovering-the-insecure-resource-management-in-app-in-app-cloud-services/。
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

## Breaking Isolation: A New Perspective on Hypervisor Exploitation via Cross-Domain Attacks

- 来源：[NDSS 2026](https://www.ndss-symposium.org/ndss-paper/breaking-isolation-a-new-perspective-on-hypervisor-exploitation-via-cross-domain-attacks/)。
- 判定依据：客体内存重用辅助指针破坏与权限提升，属于直接内存利用。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/breaking-isolation-a-new-perspective-on-hypervisor-exploitation-via-cross-domain-attacks/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Breaking the Generative Steganography Trilemma: ANStega for Optimal Capacity, Efficiency, and Security

- 来源：[NDSS 2026](https://www.ndss-symposium.org/ndss-paper/breaking-the-generative-steganography-trilemma-anstega-for-optimal-capacity-efficiency-and-security/)。
- 判定依据：生成式隐写与编码容量研究，不是从目标计算的非预期物理或资源响应推断秘密。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/breaking-the-generative-steganography-trilemma-anstega-for-optimal-capacity-efficiency-and-security/。
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

## Cache Me, Catch You: Cache Related Security Threats in LLM Serving Frameworks

- 来源：[NDSS 2026](https://www.ndss-symposium.org/ndss-paper/cache-me-catch-you-cache-related-security-threats-in-llm-serving-frameworks/)。
- 判定依据：LLM 推理缓存碰撞与投毒造成内容欺骗和检查绕过；摘要没有时序推断。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/cache-me-catch-you-cache-related-security-threats-in-llm-serving-frameworks/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Cascading and Proxy Membership Inference Attacks

- 来源：[NDSS 2026](https://www.ndss-symposium.org/ndss-paper/cascading-and-proxy-membership-inference-attacks/)。
- 判定依据：基于模型行为和条件影子训练的成员推断，属于输出隐私方法背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/cascading-and-proxy-membership-inference-attacks/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

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

## Connecting the Dots: An Investigative Study on Linking Private User Data Across Messaging Apps

- 来源：[NDSS 2026](https://www.ndss-symposium.org/ndss-paper/connecting-the-dots-an-investigative-study-on-linking-private-user-data-across-messaging-apps/)。
- 判定依据：联系人发现、SSO 与邻近搜索 API 的跨应用身份关联；未建立额外物理或时序通道。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/connecting-the-dots-an-investigative-study-on-linking-private-user-data-across-messaging-apps/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Correction Fault Attack on CROSS under Unknown Bit Flips

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i2.192-217)。
- 判定依据：对 CROSS 公共校验矩阵的未知位置/值翻转进行纠正故障攻击，含电压注入和 ECC 条件分析；类 Rowhammer 的故障模型不代表已演示 Rowhammer。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Cross-Boundary Mobile Tracking: Exploring Java-to-JavaScript Information Diffusion in WebViews

- 来源：[NDSS 2026](https://www.ndss-symposium.org/ndss-paper/cross-boundary-mobile-tracking-exploring-java-to-javascript-information-diffusion-in-webviews/)。
- 判定依据：主要研究应用向 WebView 直接注入标识符及外传；另观察指纹代码，暂作跟踪背景，待正文明确独立推断贡献。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/cross-boundary-mobile-tracking-exploring-java-to-javascript-information-diffusion-in-webviews/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## CryptPEFT: Efficient and Private Neural Network Inference via Parameter-Efficient Fine-Tuning

- 来源：[NDSS 2026](https://www.ndss-symposium.org/ndss-paper/cryptpeft-efficient-and-private-neural-network-inference-via-parameter-efficient-fine-tuning/)。
- 判定依据：MPC 支持的 PEFT 私有推理架构优化，通信开销不等于侧信道风险。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/cryptpeft-efficient-and-private-neural-network-inference-via-parameter-efficient-fine-tuning/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

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

## Cryptobazaar: Private Sealed-bid Auctions at Scale

- 来源：[NDSS 2026](https://www.ndss-symposium.org/ndss-paper/cryptobazaar-private-sealed-bid-auctions-at-scale/)。
- 判定依据：密封竞价协议与零知识证明的隐私和可验证性，非实现泄漏分析。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/cryptobazaar-private-sealed-bid-auctions-at-scale/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

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

## Demystifying the Access Control Mechanism of ESXi VMKernel

- 来源：[NDSS 2026](https://www.ndss-symposium.org/ndss-paper/demystifying-the-access-control-mechanism-of-esxi-vmkernel/)。
- 判定依据：VMKernel 可写权限结构和系统调用导致直接权限提升，未见侧信道机制。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/demystifying-the-access-control-mechanism-of-esxi-vmkernel/。
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

## EXIA: Trusted Transitions for Enclaves via External-Input Attestation

- 来源：[NDSS 2026](https://www.ndss-symposium.org/ndss-paper/exia-trusted-transitions-for-enclaves-via-external-input-attestation/)。
- 判定依据：以外部输入写入证明保护 enclave 完整性；并不等同于观察无泄漏。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/exia-trusted-transitions-for-enclaves-via-external-input-attestation/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

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

## FLIPPYRAM: A Large-Scale Study of Rowhammer Prevalence

- 来源：[NDSS 2026](https://www.ndss-symposium.org/ndss-paper/flippyram-a-large-scale-study-of-rowhammer-prevalence/)。
- 判定依据：大规模 Rowhammer 故障发生率研究；地址逆向为辅助方法，摘要未研究秘密读取通道。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/flippyram-a-large-scale-study-of-rowhammer-prevalence/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

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

## GoldenFuzz: Generative Golden Reference Hardware Fuzzing

- 来源：[NDSS 2026](https://www.ndss-symposium.org/ndss-paper/goldenfuzz-generative-golden-reference-hardware-fuzzing/)。
- 判定依据：以 ISA 参考模型加速硬件 fuzzing，摘要未明确新漏洞为侧信道，保留方法背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/goldenfuzz-generative-golden-reference-hardware-fuzzing/。
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

## Hey there! You are using WhatsApp: Enumerating Three Billion Accounts for Security and Privacy

- 来源：[NDSS 2026](https://www.ndss-symposium.org/ndss-paper/hey-there-you-are-using-whatsapp-enumerating-three-billion-accounts-for-security-and-privacy/)。
- 判定依据：联系人枚举和 X25519 公钥重用的隐私调查，主要通过公开接口查询而非侧信道。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/hey-there-you-are-using-whatsapp-enumerating-three-billion-accounts-for-security-and-privacy/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

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

## HyperMirage: Direct State Manipulation in Hybrid Virtual CPU Fuzzing

- 来源：[NDSS 2026](https://www.ndss-symposium.org/ndss-paper/hypermirage-direct-state-manipulation-in-hybrid-virtual-cpu-fuzzing/)。
- 判定依据：虚拟 CPU 状态直接变异与 hypervisor fuzzing，摘要没有泄漏观测贡献。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/hypermirage-direct-state-manipulation-in-hybrid-virtual-cpu-fuzzing/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

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

## IsolatOS: Detecting Double Fetch Bugs in COTS RTOS by Re-enabling Kernel Isolation

- 来源：[NDSS 2026](https://www.ndss-symposium.org/ndss-paper/isolatos-detecting-double-fetch-bugs-in-cots-rtos-by-re-enabling-kernel-isolation/)。
- 判定依据：用页故障插桩捕获 double-fetch，是漏洞检测仪器化，不是受保护秘密的观察攻击。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/isolatos-detecting-double-fetch-bugs-in-cots-rtos-by-re-enabling-kernel-isolation/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

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

## Know Me by My Pulse: Toward Practical Continuous Authentication on Wearable Devices via Wrist-Worn PPG

- 来源：[NDSS 2026](https://www.ndss-symposium.org/ndss-paper/know-me-by-my-pulse-toward-practical-continuous-authentication-on-wearable-devices-via-wrist-worn-ppg/)。
- 判定依据：腕部 PPG 用作预期的生物认证输入，不属于密码计算的额外泄漏。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/know-me-by-my-pulse-toward-practical-continuous-authentication-on-wearable-devices-via-wrist-worn-ppg/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Lattice-based Threshold Blind Signatures

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00118)。
- 判定依据：格门限盲签名的协议构造与证明；盲性、节点门限和硬件掩码是不同保证。
- 阅读来源：https://xplorestaging.ieee.org/document/11573582/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## LatticeBox: A Hardware-Software Co-Designed Framework for Scalable and Low-Latency Compartmentalization

- 来源：[NDSS 2026](https://www.ndss-symposium.org/ndss-paper/latticebox-a-hardware-software-co-designed-framework-for-scalable-and-low-latency-compartmentalization/)。
- 判定依据：lattice 指权限偏序格而非格密码；主要是隔离与控制流架构。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/latticebox-a-hardware-software-co-designed-framework-for-scalable-and-low-latency-compartmentalization/。
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

## Looma: A Low-Latency PQTLS Authentication Architecture for Cloud Applications

- 来源：[NDSS 2026](https://www.ndss-symposium.org/ndss-paper/looma-a-low-latency-pqtls-authentication-architecture-for-cloud-applications/)。
- 判定依据：后量子 TLS 认证的在线离线拆分与预计算性能；摘要和所读性能章节未评估能耗或时序泄漏。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/looma-a-low-latency-pqtls-authentication-architecture-for-cloud-applications/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Loongleak: Architectural Cross-Privilege-Boundary Data Leakage on LoongArch CPUs

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/hetterich-lorenz-loongleak)。
- 判定依据：作者明确为架构可见 stale bits 直接读出，不需要 timing 或 side channels。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Losing the Beat: Understanding and Mitigating Desynchronization Risks in Container Isolation

- 来源：[NDSS 2026](https://www.ndss-symposium.org/ndss-paper/losing-the-beat-understanding-and-mitigating-desynchronization-risks-in-container-isolation/)。
- 判定依据：namespace 与 cgroup 规则失配导致容器隔离问题，非泄漏通道分析。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/losing-the-beat-understanding-and-mitigating-desynchronization-risks-in-container-isolation/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

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

## MVPNalyzer: An Investigative Framework for Auditing the Security & Privacy of Mobile VPNs

- 来源：[NDSS 2026](https://www.ndss-symposium.org/ndss-paper/mvpnalyzer-an-investigative-framework-for-auditing-the-security-privacy-of-mobile-vpns/)。
- 判定依据：VPN 配置、明文与隧道外直接泄漏的生态审计；流量混淆缺失是其中一项，暂保留相邻范围。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/mvpnalyzer-an-investigative-framework-for-auditing-the-security-privacy-of-mobile-vpns/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Memclave: Secure In-Memory Enclave for Untrusted Hosts

- 来源：[USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/choudhari)。
- 判定依据：PIM 的隔离、完整性和保护数据路径；摘要提及 cache footprint，但未给出侧信道保证范围。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Memory Band-Aid: A Principled Rowhammer Defense-in-Depth

- 来源：[NDSS 2026](https://www.ndss-symposium.org/ndss-paper/memory-band-aid-a-principled-rowhammer-defense-in-depth/)。
- 判定依据：通过 DRAM 限速阻止 Rowhammer 故障，非秘密推断通道；原型和预期硬件实现仍需区分。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/memory-band-aid-a-principled-rowhammer-defense-in-depth/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

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

## Pallas and Aegis: Rollback Resilience in TEE-Aided Blockchain Consensus

- 来源：[NDSS 2026](https://www.ndss-symposium.org/ndss-paper/pallas-and-aegis-rollback-resilience-in-tee-aided-blockchain-consensus/)。
- 判定依据：TEE 回滚与克隆下的 BFT 状态和活性保证；Aegis 同名不等于既有侧信道防护。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/pallas-and-aegis-rollback-resilience-in-tee-aided-blockchain-consensus/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## PhantomMap: GPU-Assisted Kernel Exploitation

- 来源：[NDSS 2026](https://www.ndss-symposium.org/ndss-paper/phantommap-gpu-assisted-kernel-exploitation/)。
- 判定依据：GPU 映射缺陷形成直接物理内存读写原语，未使用侧信道。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/phantommap-gpu-assisted-kernel-exploitation/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Phoenix: Rowhammer Attacks on DDR5 with Self-Correcting Synchronization

- 来源：[SP 2026](https://doi.org/10.1109/sp63933.2026.00083)。
- 判定依据：DDR5 刷新同步支持 Rowhammer 提权；以故障攻击背景保留。
- 阅读来源：https://xplorestaging.ieee.org/document/11573456/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## PhyFuzz: Detecting Sensor Vulnerabilities with Physical Signal Fuzzing

- 来源：[NDSS 2026](https://www.ndss-symposium.org/ndss-paper/phyfuzz-detecting-sensor-vulnerabilities-with-physical-signal-fuzzing/)。
- 判定依据：用声光电信号自动发现传感器注入漏洞，主要是测量完整性攻击。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/phyfuzz-detecting-sensor-vulnerabilities-with-physical-signal-fuzzing/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Pipelining FALCON’s Gaussian sampler: Towards practical FALCON acceleration

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i4.447-470)。
- 判定依据：流水化 Falcon SamplerZ 并优化拒绝采样延迟及随机数消耗；摘要没有对采样泄漏或随机源质量给出安全评估，低随机量不自动等于安全。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Pitfalls for Security Isolation in Multi-CPU Systems

- 来源：[NDSS 2026](https://www.ndss-symposium.org/ndss-paper/pitfalls-for-security-isolation-in-multi-cpu-systems/)。
- 判定依据：多 CPU 的 MPU、共享内存与外设访问控制失效，研究直接读写及代码执行。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/pitfalls-for-security-isolation-in-multi-cpu-systems/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## QNBAD: Quantum Noise-induced Backdoor Attacks against Zero Noise Extrapolation

- 来源：[NDSS 2026](https://www.ndss-symposium.org/ndss-paper/qnbad-quantum-noise-induced-backdoor-attacks-against-zero-noise-extrapolation/)。
- 判定依据：量子噪声条件下的模型后门和误差缓解攻击，不是经典 PQC 侧信道。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/qnbad-quantum-noise-induced-backdoor-attacks-against-zero-noise-extrapolation/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

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

## RTrace: Towards Better Visibility of Shared Library Execution

- 来源：[NDSS 2026](https://www.ndss-symposium.org/ndss-paper/rtrace-towards-better-visibility-of-shared-library-execution/)。
- 判定依据：共享库调用的授权运行时追踪工具，未报告侧信道秘密推断。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/rtrace-towards-better-visibility-of-shared-library-execution/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## RainHash2.0: Hardware- and Arithmetization-friendly Hash Function

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i4.62-115)。
- 判定依据：RainHash2.0 面向二进制域 ZK 电路和硬件效率；证明电路友好性不等于物理泄漏保护。
- 阅读来源：publisher-deposited Crossref abstract; tches-crossref-page1。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## ReFuzz: Reusing Tests for Processor Fuzzing with Contextual Bandits

- 来源：[NDSS 2026](https://www.ndss-symposium.org/ndss-paper/refuzz-reusing-tests-for-processor-fuzzing-with-contextual-bandits/)。
- 判定依据：上下文 bandit 重用处理器测试，摘要没有明确侧信道漏洞类型，保留测试方法背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/refuzz-reusing-tests-for-processor-fuzzing-with-contextual-bandits/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

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

## SECV: Securing Connected Vehicles with Hardware Trust Anchors

- 来源：[NDSS 2026](https://www.ndss-symposium.org/ndss-paper/secv-securing-connected-vehicles-with-hardware-trust-anchors/)。
- 判定依据：车载 TEE/HSM 消息认证和来源验证，未评估物理或微架构泄漏。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/secv-securing-connected-vehicles-with-hardware-trust-anchors/。
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

## Shadow in the Cache: Unveiling and Mitigating Privacy Risks of KV-cache in LLM Inference

- 来源：[NDSS 2026](https://www.ndss-symposium.org/ndss-paper/shadow-in-the-cache-unveiling-and-mitigating-privacy-risks-of-kv-cache-in-llm-inference/)。
- 判定依据：正文明确假设直接获得 KV-cache 和模型权重，属于中间状态反演；不能与仅观察缓存时序的攻击混同。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/shadow-in-the-cache-unveiling-and-mitigating-privacy-risks-of-kv-cache-in-llm-inference/。
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

## SoK: Analysis of Accelerator TEE Designs

- 来源：[NDSS 2026](https://www.ndss-symposium.org/ndss-paper/sok-analysis-of-accelerator-tee-designs/)。
- 判定依据：加速器 TEE 的访问控制、内存加密和证明综述；摘要未给出明确侧信道系统化，保留相关架构背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/sok-analysis-of-accelerator-tee-designs/。
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

## SoK: Understanding the Fundamentals and Implications of Sensor Out-of-band Vulnerabilities

- 来源：[NDSS 2026](https://www.ndss-symposium.org/ndss-paper/sok-understanding-the-fundamentals-and-implications-of-sensor-out-of-band-vulnerabilities/)。
- 判定依据：传感器带外响应的注入攻击系统化，主要是完整性和控制风险，保留测量物理背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/sok-understanding-the-fundamentals-and-implications-of-sensor-out-of-band-vulnerabilities/。
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

## Strategic Games and Zero Shot Attacks on Heavy-Hitter Network Flow Monitoring

- 来源：[NDSS 2026](https://www.ndss-symposium.org/ndss-paper/strategic-games-and-zero-shot-attacks-on-heavy-hitter-network-flow-monitoring/)。
- 判定依据：用联合学习研究流量重击检测与带宽规避，非秘密信息泄漏；可作动态对抗方法背景。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/strategic-games-and-zero-shot-attacks-on-heavy-hitter-network-flow-monitoring/。
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

## Targeted Physical Evasion Attacks in the Near-Infrared Domain

- 来源：[NDSS 2026](https://www.ndss-symposium.org/ndss-paper/targeted-physical-evasion-attacks-in-the-near-infrared-domain/)。
- 判定依据：近红外对抗扰动使识别系统误判，属于物理规避。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/targeted-physical-evasion-attacks-in-the-near-infrared-domain/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## The Heat is On: Understanding and Mitigating Vulnerabilities of Thermal Image Perception in Autonomous Systems

- 来源：[NDSS 2026](https://www.ndss-symposium.org/ndss-paper/the-heat-is-on-understanding-and-mitigating-vulnerabilities-of-thermal-image-perception-in-autonomous-systems/)。
- 判定依据：热成像均衡、校准和镜头导致的感知完整性问题，非热侧信道窃取。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/the-heat-is-on-understanding-and-mitigating-vulnerabilities-of-thermal-image-perception-in-autonomous-systems/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

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

## Towards Effective Prompt Stealing Attack against Text-to-Image Diffusion Models

- 来源：[NDSS 2026](https://www.ndss-symposium.org/ndss-paper/towards-effective-prompt-stealing-attack-against-text-to-image-diffusion-models/)。
- 判定依据：从公开生成图像反推提示词，使用模型输出而非实现侧信道。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/towards-effective-prompt-stealing-attack-against-text-to-image-diffusion-models/。
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

## UIEE: Secure and Efficient User-space Isolated Execution Environment for Embedded TEE Systems

- 来源：[NDSS 2026](https://www.ndss-symposium.org/ndss-paper/uiee-secure-and-efficient-user-space-isolated-execution-environment-for-embedded-tee-systems/)。
- 判定依据：嵌入式 TrustZone 用户态隔离与 LibOS 兼容性，摘要未给侧信道保护论证。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/uiee-secure-and-efficient-user-space-isolated-execution-environment-for-embedded-tee-systems/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

## Vectorized Falcon-Sign Implementations using SSE2, AVX2, AVX-512F, NEON, and RVV

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i1.302-324)。
- 判定依据：跨指令集向量化 Falcon BaseSampler 与 FFT/iFFT，报告签名性能；摘要没有采样时序或物理泄漏防护结论。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## VulSCA: A Community-Level SCA Approach for Accurate C/C++ Supply Chain Vulnerability Analysis

- 来源：[NDSS 2026](https://www.ndss-symposium.org/ndss-paper/vulsca-a-community-level-sca-approach-for-accurate-c-c-supply-chain-vulnerability-analysis/)。
- 判定依据：SCA 在此为 software composition analysis，不是 side-channel analysis。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/vulsca-a-community-level-sca-approach-for-accurate-c-c-supply-chain-vulnerability-analysis/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

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

## When Cache Poisoning Meets LLM Systems: Semantic Cache Poisoning and Its Countermeasures

- 来源：[NDSS 2026](https://www.ndss-symposium.org/ndss-paper/when-cache-poisoning-meets-llm-systems-semantic-cache-poisoning-and-its-countermeasures/)。
- 判定依据：语义缓存投毒控制返回内容，非基于缓存响应推断秘密。
- 阅读来源：https://www.ndss-symposium.org/ndss-paper/when-cache-poisoning-meets-llm-systems-semantic-cache-poisoning-and-its-countermeasures/。
- 核查日期：2026-11-14；没有独立第二审读或本地复现。

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
