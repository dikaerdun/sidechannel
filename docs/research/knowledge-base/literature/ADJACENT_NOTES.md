# 已阅读的相邻主题与方法背景

当前 35 条；保留在目录与引用图中，不计入侧信道纳入论文数量。后续全文证据可以修订范围判定。

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

## Rapidly Verifiable XMSS Signatures

- 来源：[TCHES 2021](https://doi.org/10.46586/tches.v2021.i1.137-168)。
- 判定依据：修改 XMSS 签名搜索以加快公开验证，并分析经典/量子安全与多目标攻击；摘要没有侧信道贡献，签名搜索时间与验证性能不等同于秘密时序泄漏。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## BAT: Small and Fast KEM over NTRU Lattices

- 来源：[TCHES 2022](https://doi.org/10.46586/tches.v2022.i2.240-265)。
- 判定依据：新的 NTRU 型 BAT KEM、解码与整数实现；文中 masking parameter p 是方案结构参数，不据此认定为抗侧信道掩码。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Highly Vectorized SIKE for AVX-512

- 来源：[TCHES 2022](https://doi.org/10.46586/tches.v2022.i2.41-68)。
- 判定依据：SIKE 的 AVX-512IFMA 并行算术与性能比较；摘要未明确提出恒时或泄漏评估贡献。保留历史实现背景，不作为当前部署推荐。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Roulette: A Diverse Family of Feasible Fault Attacks on Masked Kyber

- 来源：[TCHES 2022](https://doi.org/10.46586/tches.v2022.i4.637-660)。
- 判定依据：Roulette 利用掩码/盲化随机性促进故障命中，报告掩码 Kyber 的 Cortex-M4 时钟毛刺恢复。是防护交互的重要相邻研究，实际攻击仍依赖主动注入，不能宣称被动掩码安全被直接推翻。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## When Bad News Become Good News: Towards Usable Instances of Learning with Physical Errors

- 来源：[TCHES 2022](https://doi.org/10.46586/tches.v2022.i4.1-24)。
- 判定依据：将非精确计算产生错误从 LPPN 推广为 LWPE，分析数据相关误差与 FPGA 设计修正；保留物理采样和数学安全背景，不把输出误差依赖自动称为测量侧信道。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Enabling FrodoKEM on Embedded Devices

- 来源：[TCHES 2023](https://doi.org/10.46586/tches.v2023.i3.74-96)。
- 判定依据：降低 FrodoKEM 的栈消耗并分析时间与内存折衷，部分结果需微调规范；摘要未报告侧信道保护，低内存不等于泄漏安全。
- 阅读来源：publisher-deposited Crossref abstract。
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

## From MLWE to RLWE: A Differential Fault Attack on Randomized & Deterministic Dilithium

- 来源：[TCHES 2023](https://doi.org/10.46586/tches.v2023.i4.262-286)。
- 判定依据：指令跳过使 Dilithium 的 MLWE 结构退化，使用同一故障签名给出的 hints 与格约简恢复并提出防护；保留故障与后处理背景，不将 hints 获取记为功耗测量。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Loop Aborts Strike Back: Defeating Fault Countermeasures in Lattice Signatures with ILP

- 来源：[TCHES 2023](https://doi.org/10.46586/tches.v2023.i4.367-392)。
- 判定依据：用 ILP 处理 loop-abort 造成的噪声线性系统，突破打乱等防护并在 Cortex-M4 验证；恢复对象含等价签名密钥，所报少量签名是故障签名而非被动迹线。
- 阅读来源：publisher-deposited Crossref abstract。
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

## Vectorized and Parallel Computation of Large Smooth-Degree Isogenies using Precedence-Constrained Scheduling

- 来源：[TCHES 2023](https://doi.org/10.46586/tches.v2023.i3.246-269)。
- 判定依据：大光滑度同源计算的先后约束调度、多核同步和 AVX-512 性能；同步在此是并行计算手段，摘要没有同步侧信道主张。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Carry Your Fault: A Fault Propagation Attack on Side-Channel Protected LWE-based KEM

- 来源：[TCHES 2024](https://doi.org/10.46586/tches.v2024.i2.844-869)。
- 判定依据：攻击掩码为实现便利而引入的 A2B 进位传播，含 Kyber 模拟和 STM32 EM 故障验证；保留掩码与故障交互，任意阶原理不等于所有阶数已实测。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Correction Fault Attacks on Randomized CRYSTALS-Dilithium

- 来源：[TCHES 2024](https://doi.org/10.46586/tches.v2024.i3.174-199)。
- 判定依据：通过纠正随机/hedged Dilithium 的故障签名提取约束，包括公共矩阵被故障的场景，并报告模拟及 MCU 时钟毛刺；物理故障敏感性不能由被动泄漏敏感性替代。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Fast and Clean: Auditable high-performance assembly via constraint solving

- 来源：[TCHES 2024](https://doi.org/10.46586/tches.v2024.i1.87-132)。
- 判定依据：摘要聚焦汇编调度、寄存器分配与性能优化；未说明具体泄漏评估或侧信道安全保证。保留为 PQC 实现工具背景。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-12；没有独立第二审读或本地复现。

## Impeccable Keccak: Towards Fault Resilient SPHINCS+ Implementations

- 来源：[TCHES 2024](https://doi.org/10.46586/tches.v2024.i2.154-189)。
- 判定依据：为 SPHINCS+ 的 Keccak 提出 impeccable 电路与主动安全分析，给出指定位翻转模型的检测保证；这不是功耗掩码安全证明，也不是任意故障模型保证。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Revisiting Keccak and Dilithium Implementations on ARMv7-M

- 来源：[TCHES 2024](https://doi.org/10.46586/tches.v2024.i2.1-24)。
- 判定依据：优化 ARMv7-M 上 Keccak 旋转、访存流水及 Dilithium 小多项式乘法；摘要聚焦性能，不把哈希占比下降解释为泄漏降低。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Algebraic Linear Analysis for Number Theoretic Transform in Lattice-Based Cryptography

- 来源：[TCHES 2025](https://doi.org/10.46586/tches.v2025.i3.668-692)。
- 判定依据：摘要贡献是 CryptoLine/islpy 对 NTT 汇编范围与算术正确性的验证，未说明侧信道非干扰或泄漏评估；保留为 PQC 实现验证背景。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Improving MPCitH with Preprocessing: Mask Is All You Need

- 来源：[TCHES 2025](https://doi.org/10.46586/tches.v2025.i2.1-22)。
- 判定依据：优化 MPCitH 预处理与 Picnic3 并行计算；mask 是证明协议中的随机掩蔽，摘要未给出物理掩码或侧信道安全评估。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Let us walk on the 3-isogeny graph: efficient, fast, and simple

- 来源：[TCHES 2025](https://doi.org/10.46586/tches.v2025.i4.644-666)。
- 判定依据：优化 3-isogeny 链、相关 KEM 与 CTIDH 密钥生成；虽应用于 CTIDH，摘要未单独给出新恒时证明或泄漏评估，先保留算术背景。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## Rudraksh: A compact and lightweight post-quantum key-encapsulation mechanism

- 来源：[TCHES 2025](https://doi.org/10.46586/tches.v2025.i2.647-680)。
- 判定依据：Rudraksh 联合选择 LWE 参数、ASCON 与 FPGA 实现以降低面积；摘要中的 CCA/Core-SVP 安全是密码学口径，不构成物理侧信道保护。
- 阅读来源：publisher-deposited Crossref abstract。
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

## Optimizing and Implementing Threshold MAYO

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i3.489-517)。
- 判定依据：摘要中的 threshold 指多方分布式签名和主动对手安全，不能据此当成对功耗泄漏的掩码保护；保留为相邻主题。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-12；没有独立第二审读或本地复现。

## Pipelining FALCON’s Gaussian sampler: Towards practical FALCON acceleration

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i4.447-470)。
- 判定依据：流水化 Falcon SamplerZ 并优化拒绝采样延迟及随机数消耗；摘要没有对采样泄漏或随机源质量给出安全评估，低随机量不自动等于安全。
- 阅读来源：publisher-deposited Crossref abstract。
- 核查日期：2026-11-13；没有独立第二审读或本地复现。

## SQISign on ARM

- 来源：[TCHES 2026](https://doi.org/10.46586/tches.v2026.i4.471-495)。
- 判定依据：在 ARM NEON 上向量化 SQIsign 有限域与同源链，结合 Qlapoti 提升性能；摘要没有明确侧信道防护或评估贡献。
- 阅读来源：publisher-deposited Crossref abstract。
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
