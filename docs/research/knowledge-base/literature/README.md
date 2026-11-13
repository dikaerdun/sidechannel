# 侧信道与后量子密码文献库

目录截点：2026-11-12；阅读与引用更新：2026-11-14。状态：**建设中，尚未完成目录覆盖、逐篇筛查与引用追踪。**

这里统一整理 TCHES/CHES、安全顶会及引用扩展中的侧信道研究。重点是后量子密码，也保留通用泄漏模型、攻击方法、防护、验证与测量研究。收集完整 2021–2026 年度目录，并单独标记滚动五年窗口及窗口外基础文献。

## 阅读入口

- [NDSS 2024 初筛与观察模型范围](notes/ndss2024-initial-observation-models-20261114.md)：140 条标题、六篇摘要、五张通用卡片；其余 134 篇摘要与正文/引用待处理。
- [NDSS 2026 资源观察与证据范围](notes/ndss2026-resource-observation-and-scope-20261114.md)：265 条标题、80 篇摘要、34 张通用卡片与 PortRush 全部 43 个参考位置初筛。
- [NDSS 2025 静态功耗、量子硬件与范围核查](notes/ndss2025-static-power-quantum-and-scope-20261114.md)：211 条标题、71 篇摘要、27 张通用卡片、十二条引用选读及物理证据边界。
- [掩码基础、Gaussian 时序与 Falcon 引用证据](notes/masking-foundations-gaussian-timing-and-falcon-20261114.md)：20 条发现解析、18 张新卡片、采样保护变量与版本差异。
- [CCS 2025 第二轮指标、迁移与访问条件](notes/ccs2025-second-pass-metrics-transfer-and-access-20261114.md)：13 篇摘要判定、四篇正文选读、Swallow 全部引用初筛和一篇基础文献补录。
- [mUOV 引用接续与掩码采样](notes/muov-followups-and-masked-sampling-20261114.md)：七条引用解析、floor 正式版书目与 Maskaglia 前向追踪。
- [CCS 2025 掩码、契约与观察范围](notes/ccs2025-masking-contracts-and-observation-boundaries-20261114.md)：316 条标题、21 篇摘要，mUOV 的模型/检测边界、ML-Cube 安全主张及 52 条作者稿引用初筛。
- [USENIX 2025 范围、盲分析与计数器防护](notes/usenix2025-scope-blind-analysis-and-counter-bounds-20261114.md)：438 条标题、103 篇摘要、单系数 GE、成本估计及印刷公式待查项。
- [USENIX 2025 目录对应](toc-crosschecks/usenix-2025.jsonl)：438 条成员对应；主席致辞合计 439 的差异另行保留。
- [S&P 2026 身份、范围与频率界限](notes/sp2026-scope-identity-and-frequency-bounds-20261114.md)：254 条标题、74 篇摘要、印刷目录两篇缺项、稀疏 LWE 条件和 Goldilocks 指定正文。
- [S&P 2026 印刷目录部分对应](toc-crosschecks/sp-2026.jsonl)：252/254 条对应，251 条起始页与 Crossref 不同；两套来源分别保留。
- [HQC、MAYO、Falcon 与受保护格实现的引用证据](notes/pqc-citation-followups-and-evidence-20261113.md)：23 条发现解析、25 条卡片、八条版本关系及两份完整引用初筛。
- [MPCitH 修订与 FAEST/HQC 证据](notes/mpcith-revisions-and-evidence-20261113.md)：FAEST 掩码撤回、单迹线剖析条件、模拟/实测区别及三份完整引用初筛。
- [USENIX 2026 范围与后量子证据](notes/usenix2026-scope-and-pqc-evidence-20261113.md)：362 条目录对应、SDitH 保护边界、ML-KEM 成功判据及 microSCALE 单位疑点。
- [USENIX 2026 论文集对应](toc-crosschecks/usenix-2026.jsonl)：移出 2016 回顾讨论，保留 19 条非论文活动；361 条规范化题名相同、一条数学记号差异。
- [打乱引用与后续证据](notes/kyber-shuffle-followups-and-evidence-20261113.md)：全部 17 条参考文献、NIST 错链、硬件裁减、运行时间与迹线预算、在线与卷期日期。
- [S&P 2022 范围与身份](notes/sp2022-scope-and-identity-20261113.md)及 [Kyber 乘法与打乱证据](notes/kyber-multiplication-and-shuffling-20261113.md)：故障到泄漏组合、局部恢复、模拟/实测与版本条件。
- [S&P 2022 印刷目录对应](toc-crosschecks/sp-2022.jsonl)：147 条双向对应，含七处改题名；146 个可用出版起始页匹配，一处页码字段缺失。
- [范围与筛查协议](PROTOCOL.md)：纳入标准、时间边界、证据层级和完成条件。
- [545 条阅读卡片](PAPER_NOTES.md)：按主要对象分为 193 条 PQC、352 条通用研究；473 条以摘要为主，72 条补读正文部分章节，均未本地复现。会议/期刊版本分别保留，不能把记录数当作独立研究数量。
- [440 条相邻主题与方法背景](ADJACENT_NOTES.md)：保留纯故障、防护交互、格约简、数值安全和实现背景，不混入侧信道纳入数。
- [掩码版本演变与 Kyber 硬件证据](notes/masking-lineage-and-kyber-hardware-evidence-20261113.md)：Leveling/Protecting 的实质修正、Mitaka 恒时限制、硬件恢复对象，以及模拟与测量的边界。
- [S&P 2023 掩码、推测与观察条件](notes/sp2023-masking-speculation-observation-20261113.md)：Raccoon 的随机数/测试条件与 Jasmin 的应用边界，含九条引用选读。
- [Episode V 恒时保证与证明边界](notes/kyber-verification-episode-v-20261113.md)：区分规范证明、恒时实现、经典模型、版本差异和两篇窗口外基础文献。
- [S&P 2024 物理通道与保证范围](notes/sp2024-physical-and-proof-boundaries-20261113.md)：共享存储资源、软件模拟的 LAM/UAI、推测恒时模型、SRAM 老化及视频功耗观察的具体条件。
- [S&P 2025 观察能力与证明范围](notes/sp2025-observation-and-proof-scopes-20261113.md)：Half-Spectre、BadRAM、SCAD、IncognitOS、Sparta 与 ML-KEM 验证论文的范围核查。
- [实现证据范围](notes/tches-implementation-evidence-boundaries-20261113.md)：掩码优化、恒时边界、形式验证缺口与性能背景。
- [功耗权限、掩码假设与 PQC 恢复对象](notes/power-observation-and-pqc-boundaries-20261113.md)：Peek-a-Walk 的 Dilithium 案例、Share-slicing 的观测成本及材料可得性。
- [S&P 2025 保护范围与观测通道](notes/sp2025-protection-and-observation-boundaries-20261113.md)：OpenTitan 的掩码边界、Scheduled Disclosure 的 SIKE 实验及作者代码入口。
- [比较条件专题](notes/pqc-comparison-boundaries-20261113.md)：区分 trace/query/hint、模型与测量、实际求解与难度估计。
- [算法/对象索引](TOPIC_INDEX.md)与[年度索引](YEAR_INDEX.md)：浏览已纳入研究，区分历史实现与最终标准。
- [标题初筛](TITLE_SCREENING.md)：TCHES 599 条、S&P 2022 的 147 条、2023 的 196 条、2024 的 261 条、2025 的 255 条、2026 的 254 条，加 USENIX 2025 的 438 条和 2026 的 362 条，以及 CCS 2025 的 316 条、NDSS 2024 的 140 条、2025 的 211 条与 2026 的 265 条，共 3,444 条已读；暂判不等于最终纳入/排除。
- [覆盖与缺口](COVERAGE.md)：逐会议、逐年的实际状态。
- [引用与版本进度](CITATION_PROGRESS.md)：282 条核对引用、71 条版本关系（61 条核实、10 条推定）；100 条发现完成身份与范围判定、120 条仍待解析，整体引用追踪尚未完成。
- [扩展来源](EXTENDED_SOURCES.md)：通过引用、检索和版本关联取得的 148 条记录，包含扩展会议、预印本及窗口外基础论文；尚非完整年度目录。
- [S&P 2023 印刷目录对应](toc-crosschecks/sp-2023.jsonl)：196 条对应、两处改题名和三个 N/A；两组重复 DOI 继续保留待查。
- [S&P 2024 印刷目录逐项对应](toc-crosschecks/sp-2024.jsonl)：261 条双向对应，含两处改题名；四条由渲染页读取，另 257 条从文字层提取。
- [S&P 2025 印刷目录逐项对应](toc-crosschecks/sp-2025.jsonl)：255 条双向对应，含一处改题名及一条页码 N/A 的记录，后者最终出版状态待查。
- [后量子候选阅读队列](PQC_QUEUE.md)：用于安排阅读，尚未核查的条目不会冒充正式纳入。
- [已有来源索引](../SOURCE_INDEX.md)：保留历史 SRC 编号、数据集说明和阅读范围。
- [原有研究证据矩阵](../../evidence-matrix.md)：保留其原始信息截点。

## 目录约定

| 路径 | 内容 | 能证明什么 |
|---|---|---|
| catalogs/ | 官方目录或出版商元数据中的全部书目条目 | 该来源包含哪些记录；不证明它们都与侧信道有关 |
| provenance/ | 来源 URL、时间、哈希、分页和数量核对 | 收集过程及尚未解决的覆盖问题 |
| toc-crosschecks/ | 独立取得的论文集目录与当前条目的对应 | 目录成员核对；不证明全文已读或全部条目均已正式发表 |
| screening/ | 候选优先级与逐条阅读判定 | 当前筛查进度；自动候选不等于纳入结论 |
| papers.jsonl | 经阅读后正式纳入的论文及摘要性卡片 | 指定阅读层级下的整理结果 |
| citations/ | 引用、版本关系与待追踪队列 | 已核查的关系和未处理工作 |
| tools/ | 可重复的元数据收集与索引生成脚本 | 所采用的方法；脚本成功不等于普查完成 |

自动候选本身不构成范围判定；只有实际阅读后才更新 include/adjacent 等状态。未命中关键词的论文也必须经过目录筛查，不能直接排除。逐篇条目区分作者报告与本地复现；本次文献整理不运行攻击实验。

当前已解析 30 个核心会议年单元的 6,628 条目录记录，另有 148 条扩展/基础记录，总计 6,776 条；这些覆盖所有主题，不是 6,776 篇侧信道论文。另有 73 条前言、索引、主题演讲、Enigma/圆桌、历史回顾、会议活动与占位记录单列到 catalog-exclusions/，保留排除依据。

已完成 3,444 条标题初筛和 985 条摘要及以上阅读判定，其中纳入 545 条、相邻主题 440 条。1090 项前后向任务中，69 项进行中、1021 项待处理，没有任务被标为全面追踪完成。GoFetch 的 98 条参考文献初筛保持原状：30 条身份对应、58 条基础文献待处理、10 条背景/实现记录。Scheduled Disclosure 的 79 条引用中有 15 条身份对应、16 条基础文献待处理、48 条背景/实现记录。OpenTitan、Peek-a-Walk、EasyCrypt 以及 Episode V 的指定选读继续保留。S&P 2023 的九条选读均已对应；追加 GLP、Protecting、3D-Shield 的九条选读已全部对应；硬件打乱论文全部 17 条引用已作身份与范围判定，七条发现已解析；另连入后续论文三条关系，其中一条证据来自出版商提交的 DOI。其余指定选读仍不代表完整参考文献筛查，17 条对应也不代表递归追踪完成。

最新 NDSS 2026 批次新增 34 张卡片、46 条相邻判定、八条引用及一条推定版本关系，另有 185 篇摘要未读。PortRush 的 43 个参考位置中十五条待查，见[本批笔记](notes/ndss2026-resource-observation-and-scope-20261114.md)和[批次记录](../records/2026-11-14-literature-ndss2026.md)。软件仿真、序列准确率、隐蔽通道和字典辅助结果分别保留边界。

此前批次解析 mUOV/floor 的 20 条发现，新增 18 张卡片、三条相邻判定、21 条引用和 11 条版本关系（八条核实、三条推定）。mUOV 尚余 UOV 2018 完整摘要；floor 已列队身份解析完毕，但背景与递归追踪仍未完成。采样类型、转换阶数、DOM 数字及 Falcon 预算区别见[本批笔记](notes/masking-foundations-gaussian-timing-and-falcon-20261114.md)与[批次记录](../records/2026-11-14-literature-masking-foundations.md)。

此前批次补读 CCS 2025 的 13 篇摘要，另补一篇窗口外基础文献，共新增 11 张卡片、十条引用和三条版本关系。Swallow 的 37 个参考位置初筛为十条对应、十五条待查、十一条背景及一个重复位置；其材料与指标范围见[第二轮笔记](notes/ccs2025-second-pass-metrics-transfer-and-access-20261114.md)及[批次记录](../records/2026-11-14-literature-ccs2025-second-pass.md)。

此前批次解析 mUOV 七条待查，新增六张卡片、18 条引用边与五条显式版本关系；floor 正式版 31 条参考初筛又产生 11 条待查。该批次结束时引用边 236、版本关系 55（49 核实、六条推定），发现 80 条已解析、105 条待查。见[批次记录](../records/2026-11-14-literature-muov-followups.md)和[证据笔记](notes/muov-followups-and-masked-sampling-20261114.md)。

此前批次完成 CCS 2025 的 316 条标题初筛和 21 篇选定摘要判定，新增 19 条卡片（包括一个作者版本及引用促成的 PoMMES）、11 条引用边、七条显式版本关系。mUOV 的 52 条作者稿引用初筛另产生 17 条待查。官方录用表与日程对应不等于独立出版目录核对。见[本批记录](../records/2026-11-14-literature-ccs2025-first-pass.md)与[证据笔记](notes/ccs2025-masking-contracts-and-observation-boundaries-20261114.md)。

此前批次解析十二条 USENIX 2025 引用发现，新增十五条论文/版本卡片、十五条引用边及四条版本关系（三条核实、一条推定）。MORE 的 27 条引用完整初筛新增十九条待查，Aegis 指定正文区分实际任务、离线成本与理论保证边界。见[本批记录](../records/2026-11-14-literature-usenix2025-citation-followup.md)与[证据笔记](notes/usenix2025-citation-followup-versions-and-defense-20261114.md)。

此前批次完成 USENIX 2025 的 438 条标题与 103 篇选定摘要判定，新增 36 条卡片并升级已有 DL-BSCA 正文阅读。58 条完整引用初筛与六条选读新增 13 条引用边、38 条待查发现。438 条印刷目录成员对应完成，但主席统计合计 439 仍未解释；恢复对象、估计条件及公式问题见[本批记录](../records/2026-11-14-literature-usenix2025.md)。

此前批次完成 S&P 2026 全部 254 条标题与 74 篇摘要判定，新增 31 条核心卡片及一条明确关联的 ePrint 版本卡片。Goldilocks 49 条引用初筛新增 11 条引用边、18 条待查发现；另新增一条核实版本边。目录只部分对应（252/254），不能计作完整；页码差异与 τ 计时起点问题见[本批记录](../records/2026-11-14-literature-sp2026.md)。

此前批次解析原 23 条发现，新增 25 条论文/版本卡片、34 条引用边及八条版本关系（五条核实、三条推定）。完整初筛 Falcon Down 的 28 个引用位置和 HQC RM/RS 的 17 条引用，另选读 Saber 期刊版第 41 条；Falcon 有一个重复位置不重复计边，新登记 21 条待查。版本差异、消息/共享密钥与长期私钥、剖析和故障条件分别保留，见[批次记录](../records/2026-11-13-literature-pqc-citation-followups.md)。

此前批次解析五条 SDitH 发现，新增 16 条卡片；完整初筛 SDitH、CiC FAEST 攻击和 HQC 有效密文攻击的 95 条参考文献，新增 31 条引用边及六条版本关系，登记 23 条新待查发现。FAEST 当前撤回的掩码实现、剖析预算和版本推定状态均已标注，见[批次记录](../records/2026-11-13-literature-mpcith-followup.md)。

此前批次完成 USENIX 2026 全部 362 条标题与 76 篇摘要判定，新增 34 条卡片、41 条相邻判定，并升级已有 ML-KEM 预言机卡片。七条引用对应与五条待查发现已登记；该年仍有 286 篇摘要未读。详见[批次记录](../records/2026-11-13-literature-usenix2026.md)。

此前批次新增九条卡片、七条相邻判定，并升级已有 JCEN 硬件攻击的正文阅读；新增 18 条引用边、两条版本关系，解析七条待查发现。当时发现清单暂时清空不等于遗漏已排除，见[该批记录](../records/2026-11-13-literature-kyber-shuffle-followups.md)。

此前批次完成 S&P 2022 的 147 条标题与 49 条摘要判定，新增 29 条通用卡片；又解析四条 Kyber 发现，新增四条 PQC 卡片。本批共新增 33 条卡片、6 条引用边、3 条版本关系，登记七条继续追踪的发现。详见[接续记录](../records/2026-11-13-literature-sp2022-kyber-four.md)。其余 98 条 S&P 2022 摘要未读，目录对应不等于全文或引用关闭。

此前批次解析八条待查发现，并通过版本/硬件检索扩展新增 16 条卡片，升级 Protecting 的正文阅读。新增 13 条引用边与 7 条书目版本关系，另登记四条待查发现。详见[本批记录](../records/2026-11-13-literature-masking-lineage-hardware.md)。正式 Protecting 修正旧 SPA 分类，3D-Shield 和统计风险模型的模拟结论与物理测量分开记录。

此前批次读完 S&P 2023 全部 196 条标题并补读 47 篇原始摘要，新增 24 篇卡片、23 条相邻判定；两篇 PQC 研究补读指定正文。独立印刷目录 196 条对应已完成，193 条标题身份升级为 DOI。详见[该批记录](../records/2026-11-13-literature-sp2023-candidates.md)。该年已有 48/196 条摘要判定，另 148 条待复核。

此前批次读完 S&P 2024 的 42 个候选/不确定项摘要，新增 27 篇卡片、15 条相邻判定，并补查四篇指定正文；又核对 Episode V 及两篇基础文献，合计新增 30 篇卡片。S&P 2024 的 261 条目录已完成独立印刷目录对应和 DOI 身份迁移，九条作者字段差异继续保留待查。详见[该批记录](../records/2026-11-13-literature-sp2024-candidates-kyber-v.md)。加上 S&P 2022、2023、2025 和 USENIX 2025、2026，目前共六个完整成员对应；S&P 2026 为部分对应，另有 23 个单元待核对。

此前补读 S&P 2025 剩余 25 个候选/不确定项，新增 16 篇卡片、9 条相邻判定，并补查六篇指定正文；该年现有 36/255 条摘要判定。S&P 2024 现有 42/261 条摘要判定；两年各有 219 条仍待摘要复核。此前全年标题筛查过程见[该批记录](../records/2026-11-13-literature-sp2025-remaining-sp2024-titles.md)。

此前批次新增 12 篇卡片、6 条引用边，解析四条发现，并完成 S&P 2025 录用目录与印刷目录的双向对应，详见[该批记录](../records/2026-11-13-literature-power-sp2025-followup.md)。新查到的 EasyCrypt 题名变化发生在录用/印刷目录与 IEEE 出版页之间，已按同一 DOI 保留别名。

此前读完剩余 86 条 TCHES 冻结候选摘要，新增 9 篇卡片与 77 条相邻判定，并对四篇做指定正文范围核查，详见[该批记录](../records/2026-11-13-literature-tches-remaining.md)。冻结的 168 条补读队列已全部有判定；这不等于全部 TCHES 全文已筛完，相邻主题也不是全文排除。

此前的[范围复核与全年标题初筛](../records/2026-11-13-literature-scope-and-sp2025.md)及[49 篇阅读与引用解析](../records/2026-11-13-literature-pqc-followup.md)保留；PREFETCHX 的版本差异、Flatter 的背景定位及 Crossref 摘要缺失边界继续有效。

引用追踪修正了一个真实遗漏：S&P 2023 主官方列表漏列 DVFS Frequently Leaks Secrets，已用另一官方日程与 DOI 补入。TCHES 同时补全副标题、分离一条卷首前言，因此核心总数恰好不变，不能只看数量判断有没有漏收。详见[覆盖表](COVERAGE.md)与[引用进度](CITATION_PROGRESS.md)。

元数据获取与索引重建方法见[工具说明](tools/README.md)。旧报告、SRC 编号和既有实验的证据状态保持可追溯；这份新目录不自动更新它们的历史判断。
