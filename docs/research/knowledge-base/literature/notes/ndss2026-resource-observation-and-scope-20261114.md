# NDSS 2026 资源观察与证据范围

阅读日期：2026-11-14。完成 265 条标题初筛及 80 篇官方完整摘要阅读，新增 34 张通用侧信道卡片、46 条相邻判定；185 篇摘要仍未读。本批没有新增 PQC 侧信道卡片，不表示该届没有相关研究。全部数字为作者报告，未本地复现。

## 目录与范围

[官方录用页](https://www.ndss-symposium.org/ndss2026/accepted-papers/)明确写 265 篇录用，与现有目录数量一致，但相邻的日程说明仍写 194 篇展示。这里保留差异，不能据此减少目录或称独立论文集成员已核对。标题初筛为 27 个候选、53 个不确定、185 个暂列标题范围外；三类都不是最终排除。

几项易混淆的范围判定如下。

- Looma 研究 PQTLS 认证的在线离线拆分与预计算性能。所读摘要和 PDF 第 12 页性能/供给开销不构成时序泄漏评估。历史 Dilithium-2 基线不能直接改称当前所有 ML-DSA 实现。
- LatticeBox 的 lattice 指权限偏序格；VulSCA 的 SCA 指软件成分分析。QNBAD 攻击量子计算中的误差缓解，并非经典 PQC 侧信道。
- Cache Me, Catch You 和 When Cache Poisoning Meets LLM Systems 的新攻击主要是缓存投毒与完整性破坏。
- Shadow in the Cache 在正式 PDF 第 3 页明确要求直接访问 KV-cache 和模型权重。它是中间状态反演，不能与仅有缓存命中时延的 PROMPTPEEK 混为一谈。[正式论文](https://www.ndss-symposium.org/wp-content/uploads/2026-f258-paper.pdf)
- Rowhammer、传感器注入、TEE 隔离和一般硬件 fuzzing 保留相邻记录；只有摘要或所读正文明确建立额外观察机制，才纳入对应侧信道范围。PhantomMotion 因使用无线流量确认注入结果而保留辅助观察卡片，主要影响仍是运动传感器完整性。

## PortRush 的发现阶段与证据层级

[PortRush 正式论文](https://www.ndss-symposium.org/wp-content/uploads/2026-f587-paper.pdf)，DOI 10.14722/ndss.2026.240587。选读 PDF 第 8–11 页、参考文献第 15–16 页；第 11 页表格已渲染核对。

方法把共享写端口、写入实体与仲裁优先关系组织为写请求图，再用 RTL 信号监测和指令序列搜索触发争用。这为“总活动相似但资源关系不同”的研究提供了直接先例，但本文不是功耗测量研究。

第 10 页明确全部实验使用软件仿真。静态分析在三个核中标记 13 个存储元素、177 个潜在争用；第 11 页报告动态触发来自 BOOM 和 NutShell 的 11 个存储元素、35 个实例。Rocket Core 的所列潜在争用没有动态触发，作者归因于顺序单发射结构。因此：

1. 三个核被分析不表示三个核都展示了可利用攻击。
2. 静态潜在关系、动态争用事件、带秘密依赖的时序路径，是不同阶段。
3. 35/109 的表 IV 覆盖分母只涉及 BOOM/NutShell，不能替换为全部静态 177。
4. 作者构造瞬态执行验证情形，不等于已在任意现有软件或硅片中完成同样攻击。

第 15–16 页全部 43 个参考位置已作初步身份与范围整理：八条对应现有目录、十五条待查、十九条暂列工具/硬件/通用方法背景、一条重复。参考 31 与 32 指向同一 CT-RSA 2006 AES 缓存研究；参考 14 同时写 USENIX Security 18 与 August 2019，年份冲突待查；参考 35 保留打印的 2024 网站版本；参考 36 的 MICRO 2018 CheckMate 不能与 CCS 2023 同名博弈研究连接。见[引用清单](../citations/portrush2026-reference-screen.jsonl)。这不是递归闭合。

## 内核与虚拟机观察的不同能力

OCCUPY+PROBE 的 RSA 案例使用同一逻辑核上的跨权限 BTB 观察。[正式 PDF](https://www.ndss-symposium.org/wp-content/uploads/2026-s925-paper.pdf)第 13 页将泄漏序列与真实 dp/dq 分支序列比较，准确率定义为归一化 Levenshtein 相似度。初次设置有 2M passes、十次请求及九段可见序列，另执行 150 次请求报告 98.6% 均值和作者标注的 4.7% standard error。它们不是 98.6% 的完整 RSA 密钥恢复成功率。第 14 页明确不能跨 SMT 线程或物理核推广；分支地址知识、调度与请求能力仍需随结果记录。该统计量的分布及 standard error 表述尚未进一步核验。

PCPLOST 则利用内核分配器的时序判断：PDF 第 4–6 页选读段落区分 PCP 列表与 zoned free_area 的页面来源，以及同阶/跨阶策略。其 cross-cache 指对象分配缓存之间的布局，不能自动归入 CPU 硬件缓存攻击。后续内存破坏与前置时序推断分开记录。[正式 PDF](https://www.ndss-symposium.org/wp-content/uploads/2026-f862-paper.pdf)

SNPeek 在 SEV-SNP 服务器上提供页表、缓存、计数器和密文等观察。[正式 PDF](https://www.ndss-symposium.org/wp-content/uploads/2026-f699-paper.pdf)第 3 页对不同平台的支持和缓解状态属于论文当时的陈述，不作为当前 KVM 或 Zen5 状态查询结果。

第 13 页的 497 kbit/s 来自主动编排的 Wasm UDF 隐蔽通道，并有恶意管理程序配合；评估传输 48 字节、重复 100 次，作者报告零错误。该吞吐量不是被动密码攻击的数据恢复速度。PIR、private heavy hitters 的统计区分实验属于另一些任务，不与吞吐量混用。

第 19 页材料附录要求支持 SEV-SNP 的 AMD EPYC 服务器、主机 root、定制内核及重启能力。已读取[作者仓库 README](https://github.com/google-parfait/cvm-side-channel-analysis)，其中明确为演示用途；未安装或执行代码。README 沿用旧题名并指向 [arXiv 2506.15924](https://arxiv.org/abs/2506.15924)，当前作者页题名和作者对应。由于作者页未明确列正式出版关系，版本边标为**原始来源推定**；2025-06-18 首稿与 2025-12-11 修订均未逐文比对正式版。

## 远距离与低采样率不等于无条件观察

ModelSpy 的六米结果针对 GPU 电磁信号中的 DNN 架构。PDF 第 3 页明确区别架构与权重，并指出知道 GPU 型号时可取得更好效果；后续对抗样本或成员推断还有各自前提。[正式 PDF](https://www.ndss-symposium.org/wp-content/uploads/2026-s141-paper.pdf)

OVRWatcher 的 1 Hz GPU 指标仍有执行入口条件。PDF 第 4 页说明实验通过开发者模式加载应用，并另讨论随应用打包 profiler 的路径。无 root、无需额外 SDK、无需并发独立应用，不等于没有安装和脚本执行前提；本文未独立核验商店审核或平台当前政策。[正式 PDF](https://www.ndss-symposium.org/wp-content/uploads/2026-s1302-paper.pdf)

TwiST 的“non-cooperative”不表示完整攻击被动。第 5 页明确允许发假包诱发 ACK；第 10 页实验用两块并置 ESP32，长距离使用外部偶极天线，单块实现是作者讨论。[正式 PDF](https://www.ndss-symposium.org/wp-content/uploads/2026-f926-paper.pdf)

第 9 页先从网络流量取得按键时刻，在没有逐键数据包的情形下则讨论用此前输入节律插值。CSI 位置估计、按键时间锚点、字典排序须分别评价。第 10 页的输入来自常见 10,000 英语词，并按 30/60/90 秒片段独立处理；第 13 页明确所有输入词都在之后搜索的字典中。

第 17 页表 VI 已渲染核对：30 米跨楼的 78.6% 是字典辅助 top-25，表中各条件均值为 64.23%；不能称为任意密码 top-1 或逐字符准确率。正文限制段说三位有 XR 经验的用户，表格列 User 1–4，人数口径待作者材料澄清，未擅自统一。稳定姿态、词典覆盖和按键节律也是其明确边界。

## 后续缺口

继续读取 NDSS 2026 的 185 篇摘要与 NDSS 2025 的 140 篇摘要，完成独立目录成员对应。优先解析 PortRush 十五条发现，补 SNPeek 的完整参考文献和版本差异、OCCUPY+PROBE 指标分布、TwiST 用户人数/无词典/时刻插值结果，以及 Adaptive Tamaraw 的切换证明范围。其余已纳入卡片大多仍是摘要级，不能视为全文审查完成。

本批来源、哈希和阅读层级见[来源记录](../provenance/ndss2026-candidates-20261114.json)。缓存中的完整摘要、PDF 和渲染图留在仓库之外；仓库只发布书目、简述、证据限制和引用关系。
