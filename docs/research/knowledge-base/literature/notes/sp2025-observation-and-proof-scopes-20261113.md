# S&P 2025 的观察能力 攻击链与验证范围

更新：2026-11-13。本批补读 25 篇原始摘要，纳入 16 篇通用侧信道研究，保留 9 篇相邻主题；其中五篇纳入条目与一篇相邻条目补查指定正文位置。没有运行作者代码或复现攻击。[逐篇阅读清单](../screening/batches/sp2025-remaining-20261113.jsonl)与[来源、身份迁移及获取失败记录](../provenance/sp2025-remaining-20261113.json)保留实际范围。

## 观察原语与后续攻击分开记录

**Half-Spectre 不能仅按 Rowhammer 标题归为纯故障攻击。** [作者 PDF](https://download.vusec.net/papers/halfspectre_sp25.pdf)第 3 页的威胁模型要求本地无特权进程、可经系统调用到达的内核 gadget，以及物理内存 direct map。其 PRELOAD+TIME 观察原语为后续故障利用提供条件；侧信道与故障阶段的能力、成本和可靠性需要分别评价。“不能直接读取某个载入值”不等于片段没有可利用的活动信息。

**BadRAM 的平台结论不同。** [作者 PDF](https://vanbulck.net/files/oakland25-badram.pdf)摘要区分 SEV-SNP 的完整性/证明攻击、classic SGX 的写入模式通道，以及所研究 scalable SGX/TDX 的别名检测。第 4 页攻击者模型以一次 SPD 操作为起点，也提到未写保护模块的软件修改可能性。不能写成全部 TEE 都可由同一种纯软件方法突破，也不能把后续年份的网站更新并入这篇 2025 论文。

**观测链中的激励条件需要明确。** [BTC 出版页](https://xplorestaging.ieee.org/document/11023318/)摘要描述串口阻抗回散，入射载波的产生与访问条件仍待正文核查，不能直接写成纯被动辐射窃听；其短线缆结果还需区分实际测量与全波模拟。[视频会议论文出版页](https://xplorestaging.ieee.org/document/11023324/)明确讨论参与者利用双向音频主动感知，摄像头关闭并不等于麦克风静音，地点分类也不是精确坐标定位。两篇本批只读摘要，不扩张其威胁模型。

## 检测范围与防护范围分开记录

**SCAD 的自动化仍依赖分析者定义观察对象。** 已读[作者 PDF](https://www.cs.ucr.edu/~zhiyunq/pub/oakland25_SCAD.pdf)第 3 页 §3.1–3.2、第 8 页 §5.2–5.4，以及第 13–14 页 §9。其离路径攻击模型允许源 IP 伪造；人工输入包括秘密变量、响应可观察点与分析范围。过窄范围会遗漏路径，欠约束状态和具体化可能产生不可达状态误报。因此，符号模型中的非干扰违例不是未经进一步核验的实际利用证明，更不是穷尽检测保证。

**IncognitOS 的 full-system 不表示覆盖一切攻击。** [作者 PDF](https://kha-dinh.github.io/assets/pdf/incognitos.pdf)第 3–4 页 §2.4 把 CPU、整个 CVM 与自身组件纳入 TCB，明确不考虑瞬态执行攻击。第 4 页概述以同步 ticks 估计 VMExit 速率并调节重随机化。需要继续核对攻击频率假设、覆盖窗口与性能配置；这不是与所有保护方案可直接比较的单一“安全百分比”。

**Sparta 的性能与用户假设必须一起读。** [作者 PDF](https://idemertzis.com/Papers/sp2025_sparta.pdf)第 4 页指出用户不能按实际收到的流量决定取回；该页还区分处理时间、用户等待和服务端等待，并说明性能比较使用了不同数据库大小。摘要中的低处理延迟不能直接解释为端到端消息延迟。其通信状态模型还依赖定长消息和重加密等条件。

## ML-KEM 论文改题名与功能验证的边界

录用目录及印刷目录使用 **Proving Faster Implementations Faster**，IEEE 出版页使用 **Faster Verification of Faster Implementations**。已核对十位作者、起始页 3820 和 DOI [10.1109/SP61157.2025.00214](https://doi.org/10.1109/SP61157.2025.00214)。作者顺序在录用表与出版元数据间有差异。目录保留原始题名，另列出版题名和别名；采用一个 DOI 身份，不增加论文数。

[ePrint 2025/1607](https://eprint.iacr.org/2025/1607)明确链接同一 DOI 并标为 minor revision，记录 2025-09-07 收稿、09-11 批准。它是书目已核实的作者修订关系；尚未核对修订稿与正式版的完整差异。

已读[作者 PDF](https://cryptosith.org/papers/mapreduce-20250907.pdf)第 2 页贡献、第 3 页脚注、第 6 页 Jasmin 说明、第 17 页结论及第 18 页两条参考文献。论文的新方法聚焦功能正确性，将推演证明与电路等价检查结合以验证优化的 ML-KEM 拒绝采样、压缩和 Keccak。正文另说明 Jasmin 工具链对恒时与推测恒时属性的保持能力，但**功能等价、工具具备检查能力、具体程序通过检查和物理泄漏安全是不同层次**。当前按功能验证与工具链背景保留，不将摘要或通用工具能力扩张为本地审计过的新实现侧信道保证。

参考文献 [11] 已与 TCHES 2023 的 Episode IV 对应；[12] 的 CRYPTO 2024 Episode V 已登记待核对身份与范围。[两条选读引用](../citations/easycrypt-selected-reference-screen.jsonl)不是全参考文献清单。前一篇的[实现证据范围记录](tches-implementation-evidence-boundaries-20261113.md)继续适用。

## 其他容易混淆的范围

- CountMamba 是具体网站指纹问题；TrafficFormer 是一般流量学习方法，SoK 的分类器审查作为方法背景保留。一般分类准确率不能自动证明敏感信息泄漏。
- Mixnets 的采样结果给出攻击优势下界；不能当作安全上界或无限部署条件下的最优性证明。
- BPSniff 的运动传感器推断与医疗有效性评价不同；Eyes 的词句识别与密码恢复也不同。
- GuardAIn、PORTAL 的访问隔离或认证加密主张不自动覆盖时间、功耗和微架构通道。
- Keysentinel 的直接凭据暴露、TunTight 的 DNS 隧道检测、MPCGuard 的协议参与者视图测试、量子脉冲的恶意执行，分别保留为相邻研究，避免仅按 leakage 或 security 一词纳入。

本轮仅收紧所读范围下的分类。相邻状态可由后续全文证据修订；没有把尚未读到的章节判为“不含相关内容”。
