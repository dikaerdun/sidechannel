# PQC 侧信道研究证据索引

信息截点：2026-09-11。配套阅读：[完整研究报告](nist-pqc-hardware-sidechannel-report.md)。本表用于查找原始证据，不用于按轨迹数给算法排名。

“全文”表示相关条件已经从论文正文核验；“摘要”表示未据其补写未知细节。所有数字均属于原文所测条件；空缺不是零成本。

| 原始研究 | 方案与对象 | 平台 / 证据 | 方法或结果粒度 | 关键限制 | 核验范围 |
|---|---|---|---|---|---|
| [Chosen Ciphertext k-Trace Attacks，2021](https://doi.org/10.46586/tches.v2021.i4.88-113) | 掩码 Kyber | 带噪泄漏模型 | 选择密文与 INTT 结构 | 少量轨迹结论依赖噪声假设 | 原始摘要/元数据 |
| [Curse of Re-encryption，2022 卷](https://doi.org/10.46586/tches.v2022.i1.296-322) | 多种 PQ KEM | PRF/PRG 的软件与硬件实例 | 重加密泄漏转化为预言机 | 不同 PRF 防护结果不同 | 原始摘要/元数据 |
| [Find the Bad Apples，2023 卷](https://eprint.iacr.org/2022/563) | Kyber-512 | Cortex-M4 EM 与模拟 | 不完美预言机的完整恢复框架 | 相对轨迹收益取决于原始准确率 | 摘要 |
| [Masked and Shuffled Kyber and Saber，2022](https://eprint.iacr.org/2022/1692) | 掩码与打乱实现 | 原文报告实现攻击 | 恢复排列相关信息及长期秘密 | 摘要的 4,608 条轨迹属于 Saber | 摘要 |
| [Correlation EM Analysis on FPGA Kyber，2023](https://eprint.iacr.org/2022/1361) | Kyber 多项式乘法 | FPGA EM | CPA；目标全部子密钥 | 166,620 条仅对应该实验 | 摘要/出版信息 |
| [Ji & Dubrova，2025](https://link.springer.com/article/10.1007/s13389-025-00375-7) | 一阶掩码 Kyber-512 解码 | 裁剪目标的 Artix-7 实测 | HD 标签；消息/会话密钥恢复 | 需剖析与重复解封装；跨设备下降 | 全文第 4–8 节 |
| [Hardware-Friendly Shuffling，2024 v1](https://arxiv.org/html/2407.02452v1) | Kyber 运算打乱 | Artix-7 | 有限 CPA 预算下的保护效果 | 未成功不是不可攻破证明 | v1 全文 |
| [KyberSlash，2025](https://doi.org/10.46586/tches.v2025.i2.209-234) | Kyber 软件实现 | Cortex-A7 / Cortex-M4 | 秘密相关除法时间 | 按指令、实现与修补版本判断 | 原始摘要/元数据 |
| [Profiling Dilithium，2022](https://eprint.iacr.org/2022/106) | 临时量与位操作 | Cortex-M4 | 剖析、求解与等价签名密钥 | 未核验完整轨迹预算 | 摘要 |
| [Breaking and Protecting the Crystal，2023](https://link.springer.com/chapter/10.1007/978-3-031-40003-2_25) | Dilithium NTT | 硬件实现 | 剖析与 CPA，系数/系数对 | 训练与攻击采集分开；非自动完整密钥 | 摘要 |
| [In-depth CPA on Dilithium Hardware，2024](https://link.springer.com/article/10.1186/s42400-024-00209-9) | Dilithium v3.1 | 并行 FPGA | 干扰建模和部分系数恢复 | 最低 70,000 条不是完整密钥成本 | 全文 |
| [DPA of XMSS and SPHINCS，2018](https://link.springer.com/chapter/10.1007/978-3-319-89641-0_10) | 旧 SPHINCS-256 / XMSS | BLAKE PRF 硬件等 | 秘密派生中的功耗信息 | 不是最终 SLH-DSA 直接攻击 | 摘要 |
| [SHIFT SNARE，2025](https://arxiv.org/abs/2504.00320) | Falcon 第三轮密钥生成 | Cortex-M4 | 单轨迹采样泄漏 | 不是通用 Falcon 签名硬件结论 | 摘要 |
| [t-Probing (In-)Security，2025/2026](https://eprint.iacr.org/2025/1202) | 固定重量多项式采样 | 十阶掩码构件分析与攻击 | 单轨迹、非均匀份额与噪声 | 不是完整最终 HQC 破解 | 摘要与正文前部 |
| [Carry Your Fault，2024](https://arxiv.org/abs/2401.14098) | 掩码 Kyber A2B | STM32 EMFI 与模拟 | 主动故障到长期密钥恢复 | 注入次数不能当被动轨迹数 | 原文模型与实验概述 |
| [Signature Correction，2022](https://arxiv.org/abs/2203.00637) | Dilithium 故障签名 | 软件与 Rowhammer 场景 | 部分秘密位恢复 | 剩余计算成本仍需计入 | 摘要 |
| [Sapphire，2019](https://arxiv.org/abs/1910.07557) | 历史格密码加速器 | 实际 40 nm 硅芯片 | 性能与特定时序/SPA 保护目标 | 不能替代最终标准完整掩码评价 | 摘要 |
| [Towards ML-KEM & ML-DSA on OpenTitan，2025](https://cryptojedi.org/papers/otpqc-20250514.pdf) | 统一 OTBN/KMAC 平台 | 架构与实现研究 | 性能、面积、受保护接口 | 部分完整掩码仍是后续工作 | 正文相关章节 |
| [Two Birds, One Mask，2026](https://doi.org/10.7717/peerj-cs.4003) | 统一 ML-KEM/ML-DSA 一阶掩码 | 摘要报告 FPGA 与 TVLA | 集成转换、采样、解码等 | 全文、预算、代码提交待核验 | 出版方提交的原始摘要/元数据 |

## 后续精读与复现应补齐的字段

1. 算法和参数版本，以及实现的固定提交。
2. 完整设备、裁剪模块或模拟模型的范围。
3. 剖析采集、目标采集、片段、重复查询和设备数量。
4. 标签来源与训练/验证/测试的独立性。
5. 位、系数、消息、会话密钥、长期密钥或等价签名能力的结果粒度。
6. 保护模块清单、阶数、份额分布、随机数生成与带宽。
7. 成功率和置信区间，以及失败条件和未覆盖的攻击。
8. 功能验证、面积、性能、能耗、随机数成本是否在相同配置下测得。

每次更新应保留旧结论对应的版本；新增证据可以改变结论，但不应静默替换历史实验条件。
