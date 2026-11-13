# 下一步

更新日期：2026-11-11（批次 EXP-20261111-10 后）。当前阶段：找到可用的离散通道，但**只能读 3 个符号位，读不出幅度**；无硬件，H005 仍停在条件缺失。

## 2026-11-14 扩大构思交接

[参数规模、随机性实现与物理密码原语](brainstorms/2026-11-14-parameter-scaling-randomness-realization-physical-primitives.md)要求验证者先交资源边界与同预算协议、匹配输出联合分布的实现对、物理状态方程及模拟命题或反例。第三项保留理论诊断机会；由用户安排他人验证，未派发或执行任务，不增加种子计数，见[本轮交接](records/2026-11-14-parameter-randomness-physical-primitive-handoff.md)。

此前把已有方向推进为三个待验证目标：约束物理关系的证明、可迁移的物理状态、从允许泄漏反向设计实现；详见[基础引用与交接](records/2026-11-14-kyber-foundations-saber.md)。当前全库 575 张卡片、326 条引用、80 条版本关系、136 条待解析发现；SABER 八条基础引用已解析，44 个参考位置为 22 条对应、0 条身份待查、22 条暂列背景。没有新增实验或派发任务。下文批次数字保留为历史快照，实时计数以[覆盖文件](literature/COVERAGE.md)为准。

[安全容差、保密物理核验与诱饵执行](brainstorms/2026-11-14-robustness-private-audit-and-decoy-execution.md)展开三项研究目标。验证者分别先交可测扰动到预算相关安全界、有限作弊族下的核验与隐私构造或反例、包含公开验证和结果选择的诱饵通道比较。第二项保留小规模理论诊断机会；后三个开放问题暂留种子池。由用户安排他人验证，未派发或执行任务，不改变旧实验结论，见[交接记录](records/2026-11-14-robustness-audit-decoy-handoff.md)。

## 2026-11-14 文献库建设接续

最新批次补读 NDSS 2025 的 70 篇摘要，累计 141/211，另 70 篇未读；211 个独立印刷目录成员已对应，日程活动和印刷重复项分别记录。新增 MineShark 的流量推断卡片及三条引用发现，见[本批交接](records/2026-11-14-literature-ndss2025-second-toc.md)。下一步从原目录位置 106（Mysticeti）接续，不能把已下载的剩余 70 篇算作已读。全库 1,203 条判定，八个年度完整目录对应、一个部分对应、21 个待核对。PQC 正文与引用缺口继续保留。

此前批次完成 NDSS 2024 全部 140 篇摘要及 140 条独立印刷目录对应，新增 MASTERKEY 的计时卡片；SABER 八条基础引用的修订、恒时保护变量与评估者条件分开记录，见[本批交接](records/2026-11-14-literature-ndss2024-completion-saber.md)。目录 6,790 条，判定 1,133 条，七个年度完整成员对应、一部分对应、22 个待核对。下一步补 NDSS 2025 剩余 140 篇摘要和独立目录，再继续 NDSS 2026 的 185 篇；PQC 线补 2016 Ring-LWE 正文、转换修订和 Gaussian 引用。以下为各批历史快照，已解决项以上方与实时覆盖为准。

[统一文献入口](literature/README.md)包含核心 30 单元的 6,628 条目录和 150 条扩展/基础记录；已初筛 3,444 条标题、作出 1,039 条摘要及以上判定，纳入 561 条出版/版本记录。已核对 299 条引用、74 条版本关系（64 条核实、十条推定）；100 条发现已解析、137 条待核查。六个核心单元完成独立目录成员对应，S&P 2026 部分对应（252/254），其余 23 个待核对。

此前接续 NDSS 2024 第二批：52 篇新增摘要判定与两张 PQC 掩码防护卡片；该年累计 58/140 篇摘要，继续剩余 82 篇、独立目录和全文。EM Eye 全部 42 条引用初筛有十三条待查；总线故障五条选读补入 SABER 与 Kyber。继续核查 SABER 正式版差异与完整参考列表，保留缩小参数 TVLA、Kyber 双平台及逐函数测试条件，见[第二批记录](records/2026-11-14-literature-ndss2024-second.md)。

随后完成 Kyber 作者修订稿的 25 个参考位置初筛：十一条对应、四条待查、十条暂列背景，新增两条明确版本关系。先解析 Keccak 防护、LATINCRYPT 2019 NTT、ePrint 2020/549 与 CHES 2015 泄漏评估；再补原始修订差异与 NDGJ21 全文的剖析/输入预算，见[Kyber 引用接续](records/2026-11-14-kyber-masked-bibliography.md)。当前 1,122 项任务中 71 进行中、1,051 待处理。用户安排的构思验证继续保留，本轮没有实验或派发任务。

此前 NDSS 2026 批次读完 265 条标题与 80 篇摘要，新增 34 张通用卡片、46 条相邻判定；继续余下 185 篇摘要及独立目录对应。PortRush 全部 43 个参考位置初筛新增八条引用、十五条待查；SNPeek 新增一条推定版本关系。优先补 PortRush 引用身份、RSA 编辑距离指标、TwiST 人数/词典/时刻条件与 SNPeek 全文版本，见[批次记录](records/2026-11-14-literature-ndss2026.md)和[证据笔记](literature/notes/ndss2026-resource-observation-and-scope-20261114.md)。1,080 项引用任务中 69 进行中、1,011 待处理。

此前 NDSS 2025 批次读完 211 条标题及 71 篇官方摘要，新增 27 张通用卡片与 44 条相邻判定，见[批次记录](records/2026-11-14-literature-ndss2025.md)和[证据笔记](literature/notes/ndss2025-static-power-quantum-and-scope-20261114.md)。继续该年余下 140 篇摘要、其他 NDSS 年度及独立目录对应；补 Borrowed Time 清理与检测条件、Android 过滤/权限、NISQ 门检测到分类的误差传递，以及五条新引用。十二条指定引用只新增七条核对边与一条明确版本关系，不代表完整书目。1,012 项引用任务中 68 进行中、944 待处理。

此前批次解析 mUOV 九条、floor 十一条发现，新增 18 张卡片、三条相邻判定、21 条引用和 11 条版本关系，见[批次记录](records/2026-11-14-literature-masking-foundations.md)与[证据笔记](literature/notes/masking-foundations-gaussian-timing-and-falcon-20261114.md)。优先取得 UOV 2018 完整摘要及 Falcon 2023 正文，补 Sun 2022 剩余 44 条引用；不能把 isochrony 各变体、DOM 综合与检测阶数或 Falcon 三组预算混合。958 项引用任务仍有 67 进行中、891 待处理。

此前批次完成 CCS 2025 第二轮 13 篇摘要判定，新增十篇本届卡片及一篇基础文献，补十条引用与三条版本关系。四篇正文选读区分 BFId 视角迁移、HW-Spy 字符指标、DP 访问分区粒度和 Swallow 模拟防护范围。Swallow 的 37 个参考位置新增十五条待查，重复项不重复计边，见[批次记录](records/2026-11-14-literature-ccs2025-second-pass.md)和[证据笔记](literature/notes/ccs2025-second-pass-metrics-transfer-and-access-20261114.md)。Co-Prime/GAPDiS 原始摘要、PMTUD/Time Tells All 显式版本关系及 Swallow 引用队列继续保留。

此前批次解析 mUOV 七条发现，新增六张卡片、18 条引用与五条版本关系；补 floor 正式版 31 条参考及 Maskaglia 的引用，见[批次记录](records/2026-11-14-literature-muov-followups.md)和[证据笔记](literature/notes/muov-followups-and-masked-sampling-20261114.md)。SoK 完整检测条件、GE 正式/作者稿差异、floor 拒绝流程、Maskaglia 分布限制及 ICCD 浮点转换摘要仍待补；引用身份最新状态以上述掩码基础批次为准。

此前批次完成 CCS 2025 的 316 条标题初筛及 21 篇摘要判定，新增 19 条卡片、11 条引用边和七条显式版本关系。mUOV 作者稿的 52 条参考位置初筛产生 17 条待查；正式 ACM 参考列表与独立出版目录仍待对照。见[批次记录](records/2026-11-14-literature-ccs2025-first-pass.md)和[证据笔记](literature/notes/ccs2025-masking-contracts-and-observation-boundaries-20261114.md)。

继续 CCS 2025 其余 282 篇摘要，优先未读候选/不确定项，以及已建卡的 UOV SoK、Gaussian elimination、Falcon floor 的剩余全文。补 mUOV 正式版差异、标准参数实测范围、ML-Cube 缓存缓解的具体证据和 SecSep 硬件契约；不要把一阶缩小参数 TVLA 或寄存器内运算写成全面安全证明。

此前批次新增十五条论文/版本卡片，解析十二条 USENIX 2025 引用发现；新增十五条引用边和四条版本关系（三条核实、一条推定）。MORE 的 27 条引用初筛产生十九条新线索。见[批次记录](records/2026-11-14-literature-usenix2025-citation-followup.md)和[版本与防护证据](literature/notes/usenix2025-citation-followup-versions-and-defense-20261114.md)。

此前批次完成 USENIX 2025 的 438 条标题与 103 篇选定摘要判定，新增 36 条卡片、升级已有 DL-BSCA，并补读 TEEcorrelate 正文及材料附录。58 条完整引用初筛与六条选读新增 13 条引用边、38 条发现。见[批次记录](records/2026-11-14-literature-usenix2025.md)和[证据笔记](literature/notes/usenix2025-scope-blind-analysis-and-counter-bounds-20261114.md)。

ICCAD Kyber、CSUR、OT-PCA 与 Aegis 身份已对应；继续补 Kyber 分类器预算、HQC 调用与测量成本、Aegis 完整序列隐私和噪声实现映射。碰撞论文两版数字与显式关系、CSUR 最早上线日期仍待核。DL-BSCA 余下 26 条及 MORE 新增 19 条发现继续追踪。TEEcorrelate 的标准差表达式、HQC 成本单位和材料 DOI 关系，DL-BSCA 的选点/模型选择预算，以及主席 407+32 与目录 438 的差异仍待查。该届其余 335 篇摘要和 TEEcorrelate 其余 76 条引用继续保留，不能把标题暂判视为排除。

此前批次完成 S&P 2026 的 254 条标题与 74 篇摘要判定，新增 32 条卡片；含一个明确关联的 ePrint 小修订版本。Goldilocks 全部 49 条引用初筛新增 11 条引用边、18 条待查发现。见[批次记录](records/2026-11-14-literature-sp2026.md)和[证据笔记](literature/notes/sp2026-scope-identity-and-frequency-bounds-20261114.md)。

优先核对 Goldilocks 的 τ 是否包含检测延迟、稀疏 LWE 正文与版本差别，以及印刷目录两篇缺项和 251 条页码差异。计时文字差异不是已证实漏洞，目录缺项不表示撤回。S&P 2026 的其余 180 篇摘要与其他年度继续筛查；Goldilocks 新增 18 条频率/定量泄漏线索与原 Falcon/HQC 的 21 条发现一并保留。

此前 PQC 批次解析原 23 条发现，补 MAYO 正式版和 Saber 期刊扩展，共 25 条卡片。继续补读 MAYO 两版数字差异、HQC 对固定 RM 译码边界的批评、Saber 扩展的指令分析。MAYO、HOST、五阶 Kyber 正式摘要的直接页面仍有访问限制；Falcon 的 -O0 条件与置信水平不可省略，FAEST PDF Disclaimer/历史页仍需核对。完整引用列表初筛不等于递归闭合。

此前 USENIX 2026 已完成 362 条标题和 76 篇摘要判定，目录改正与原始范围见[记录](records/2026-11-13-literature-usenix2026.md)。已取得的 DLSCA SoK 正文可用于补充引用，但尚未正式通读。

继续核查 SDitH 的 Seed 例外及不同 Keccak 配置、ML-KEM 查询与测量预算及版本差异、microSCALE 第 13 页采样单位矛盾。材料链接仅核到作者声明，没有运行代码。此前[硬件打乱引用批次](records/2026-11-13-literature-kyber-shuffle-followups.md)的 17 条对应保留；NIST 错误 DOI 已纠正，零值过滤运行时间、裁减硬件与恢复对象边界仍适用。

继续核查新卡片全文和显式版本关系：FPT 正式页码 1–1、TECS 同题早期摘要与正式 200K TVLA 表述、复制/随机时钟的作者正文、局部掩码 NTT 的实际配置。JCEN 参考 23 实际引用 ePrint 2021/1189，尚未建立到正式 TECS 的核实版本边，其余参考文献继续筛查。局部掩码在线于 2026-09-17、分配 12 月卷期，两个日期不能互换。ACNS 正文访问失败，具体剖析条件仍待核查；其仓库仅读 README。

继续其他核心会议的逐题筛查和目录核对。USENIX 2026 还有 286 篇摘要未读；S&P 2022 有 98 条，2023 有 148 条，2024、2025 各有 219 条。扩展会议系统目录、TCHES 非关键词候选、HADES/HAETAE 防护章节、McEliece FPGA 勘误及 PQC 全文专题继续保留。GoFetch 还有 58 条基础引用、Scheduled Disclosure 还有 16 条待处理。922 项前后向任务中 65 项进行中、857 项待处理，没有全面完成的任务。

书目与材料缺口：S&P 2022 MSR Templating 的出版页码字段；2023 三个 N/A、两组重复 DOI 与五条作者字段差异；2024 九条作者差异；2025 一条 N/A 的最终出版状态。继续查 Finger in the Power 仓库 404、Peek-a-Walk 材料完整性，以及 Episode V 不同版本与最终 FIPS 203 的对应。Raccoon 的测试用随机数及两份额 TVLA、Jasmin 的同地址空间边界不能省略。此前[功耗权限与 PQC 恢复范围](literature/notes/power-observation-and-pqc-boundaries-20261113.md)继续适用；接续先读[覆盖缺口](literature/COVERAGE.md)，不能把队列补读完或脚本通过当作普查完成。

## 2026-11-12 新方向交接（与既有实验接续并列）

2026-11-14 增补[自我观察、密钥选择与动态防护](brainstorms/2026-11-14-self-observation-key-selection-adaptive-defense.md)。先分别提交内部与外部观察的覆盖条件或盲区、器件条件下的密钥重加权及密码学后果、包含配置痕迹与物理历史的动态策略模型。第一项保留一次理论诊断。三项深化已有种子，待用户安排他人验证；未执行或派发任务，见[本轮交接](records/2026-11-14-self-observation-selection-strategy-handoff.md)。定位性阅读未增加正式文献卡片。

2026-11-14 增补[硬件适应、公开可模拟波形与稀有泄漏路径](brainstorms/2026-11-14-adaptive-hardware-simulation-rare-paths.md)。验证者先交真实反馈与策略更新规则、明确观察范围内的模拟命题、无需测试秘密标签的事件定义与首次进入预测。第二项保留理论诊断机会；三项深化现有种子，验证由用户安排，见[交接记录](records/2026-11-14-adaptation-simulation-rare-paths-handoff.md)。未运行实验、仿真、训练或派发任务。

2026-11-14 增补[器件条件、噪声响应与判定边界几何](brainstorms/2026-11-14-population-noise-response-boundaries.md)。验证者先交固定设备参数与合法校准、共享参数的噪声与响应模型、真实离散分区及留出输入方向预测。第二项保留长期物理诊断机会；第一项区分混合通道与平均单机风险，第三项需比较已有判定预言机研究。三项深化既有方向，不增加种子计数，验证由用户安排，见[交接记录](records/2026-11-14-population-response-boundary-handoff.md)。未运行实验或派发任务。

2026-11-14 增补[瞬态响应、顺序放大与防护相容性](brainstorms/2026-11-14-transients-switching-compatibility.md)。验证者先交有物理坐标的响应模型与留出脉冲预测、两种正确编排及状态转移、有限实现库的满足解或相容约束冲突。相容性方向保留理论诊断；A、B 同属动力学路线。用户安排他人验证，本轮未派发或执行实验任务，不增加种子计数；见[交接记录](records/2026-11-14-transient-switching-compatibility-handoff.md)。

2026-11-14 增补[跨密钥关系、光子事件与后量子求解成本](brainstorms/2026-11-14-key-populations-photon-events-quantum-costs.md)。验证者先交有无合法锚点的小型关系图及资源转换、合法电路与同次光子事件预算、有限 PQC 约束实例及完整求解资源表。光子方向保留远期诊断。用户安排验证，本轮未派发或执行任务，不增加种子计数，见[交接记录](records/2026-11-14-key-photon-quantum-handoff.md)。

2026-11-14 增补[计算冗余、拒绝轨迹与随机计算图](brainstorms/2026-11-14-computation-codes-rejected-transcripts-random-graphs.md)。验证者先交两种正确实现及整体可辨识预测、完整拒绝流程与观察契约、少量图族及已知/未知路线的精确比较。第三项保留小规模理论诊断机会。三项深化旧方向，未增加种子计数、执行实验或派发任务，由用户安排他人验证；见[交接记录](records/2026-11-14-computation-rejection-graph-handoff.md)。

2026-11-14 增补[物理遗忘、时空隔离与可逆计算](brainstorms/2026-11-14-physical-forgetting-spacetime-reversible-computation.md)。验证者先交同数字边界的准备历史与未来观察预算、真实传播图及路径干预预测、可逆小映射与完整能量记账。第三项保留一次远期理论诊断。三项深化旧方向，未增加编号或执行任务；由用户安排验证，见[交接记录](records/2026-11-14-forgetting-spacetime-reversible-handoff.md)。

2026-11-14 增补[回路关系、正确性裕量与信息迁移](brainstorms/2026-11-14-cycle-relations-correctness-margins-leakage-migration.md)。验证者先交实际关联图与合法断开对照、真实路径及正常工作条件的分叉预测、固定总预算的完整观察与秘密任务。回路方向保留理论诊断机会，另外三个开放问题暂不展开。三项深化已有种子，未增加编号或执行任务；验证由用户安排，见[交接记录](records/2026-11-14-cycle-margin-migration-handoff.md)。

2026-11-14 增补[算法噪声、高维匿名性与跨尺度模型](brainstorms/2026-11-14-noise-labels-anonymity-and-scale.md)。验证者先交误差生命周期及侧信息通道、小图的排列与秘密等价类、两种模型对留出尺度的分叉预测。第三项保留理论诊断机会。三项深化已有种子，未增加编号、派发任务或执行实验；验证由用户安排，见[交接记录](records/2026-11-14-noise-anonymity-scale-handoff.md)。

2026-11-14 增补[秘密算子、物理操作语法与面向观察者的实现设计](brainstorms/2026-11-14-secret-operators-physical-grammar-observation-design.md)。分别先交实际读出与合法碰撞类、两套操作语义的留出组合预测、多端口约束下的正确构造或不可行证书。第三项保留小规模理论诊断机会。三项深化旧方向，不增加 BOLD 编号，待用户安排其他研究者验证；未派发或执行任务，见[本批交接](records/2026-11-14-operator-grammar-observation-handoff.md)。

2026-11-13 增补[轨迹编码、任务安全与物理可辨识性](brainstorms/2026-11-13-trajectory-codes-task-security-identifiability.md)。先由掩码/RTL 研究者界定真实观察族，由密码学/推断研究者明确任务与公开信息基线，由系统辨识/测量研究者提交等价范围和分叉干预。六个开放问题中详细展开这三项，保留可辨识性的理论诊断机会。均待用户安排他人验证，未派发、未执行，不增加 BOLD 种子数；见[交接记录](records/2026-11-13-trajectory-task-identifiability-handoff.md)。

2026-11-13 增补[时间方向、模约减商与混合算法的物理组合](brainstorms/2026-11-13-time-arrow-quotients-hybrid-composition.md)。分别交给随机过程/电路、编译器/格侧信息、组合密码学/实现研究者：先核对同谱反向链并找真实状态；导出固定内核的整数语义；写出含分支披露与共享状态的观察游戏。保留时间方向的小规模理论诊断。三项均待验证，未派发、未执行，不增加 BOLD 种子数；见[交接记录](records/2026-11-13-time-quotient-hybrid-handoff.md)。

2026-11-13 增补[安全资源下界、难问题泄漏与跨实现预测](brainstorms/2026-11-13-resource-bounds-lwe-leakage-counterfactuals.md)。第一项先交有限计算图中的完整资源规则及证明或反例；第二项先交允许接口、安全游戏及全执行模拟器或反例，保留小规模理论诊断；第三项先交四份功能等价实现及对留出实现的分叉预测。三项深化既有方向，不增加种子计数，由用户安排他人验证；详见[交接记录](records/2026-11-13-resource-lwe-counterfactual-handoff.md)。本轮未运行实验、仿真、训练或派发任务。

2026-11-13 增补[随机源反馈及两项研究深化](brainstorms/2026-11-13-randomness-feedback-hardness-state-discovery.md)：新种子 BOLD-40 先交实际耦合闭环、调理器与可见性；BOLD-14 的深化先交两套约束及完整求解成本；BOLD-22 与原型 M 的深化先交两个竞争状态模型及分叉干预。后两项不重复计为新机制。用户安排他人验证，随机源方向保留小规模探索机会；详见[交接记录](records/2026-11-13-randomness-hardness-state-handoff.md)。未运行实验、仿真、训练或派发任务，原有文献与实验接续保持不变。

2026-11-13 增补[第十一批 BOLD-20261113-37 至 39](brainstorms/2026-11-13-self-calibration-hidden-encoding-observer.md)：37 先交联合标定的可辨识性与锚点；38 先交实际编码矩阵、份额布局和节点关系；39 先交只改读出与改变状态演化的竞争预测。验证由用户另行安排，39 保留小规模探索机会，详见[交接记录](records/2026-11-13-calibration-encoding-observer-handoff.md)。未运行实验、仿真、训练或派发任务，文献普查及历史实验接续保持不变。

2026-11-13 增补[三个研究原型 E、R、M](brainstorms/2026-11-13-echo-representations-mechanism-discovery.md)：E 先交可实现的响应反向操作对及间隔扫描预测；R 先交小内核的正确表示图、转换成本与不变量；M 先交两个竞争机制和使预测分叉的合法干预。它们细化 RP-A、RP-C，不增加 BOLD 编号；E 保留小规模探索机会。用户安排其他人验证，详见[交接记录](records/2026-11-13-echo-representation-discovery-handoff.md)。没有执行实验或派发任务，文献普查接续保持不变。

2026-11-13 增补[第十批 BOLD-20261113-34 至 36](brainstorms/2026-11-13-key-device-seeds-scaling.md)：34 先交合法密钥与器件的交互预测；35 先交秘密来源图及两种存储政策；36 先交可实现阶数、资源预算和共享节点隔离预测。均由用户安排其他人验证，36 保留长期探索机会。详见[交接记录](records/2026-11-13-key-seed-scaling-handoff.md)；未运行实验或派发任务，文献普查和既有实验状态继续保留。

2026-11-13 增补[三条研究主线 RP-A 至 C](brainstorms/2026-11-13-three-research-programs.md)：A 先提交模型等价对及跨操作预测；B 先提交真实物理节点、关系函数及切断交互的预测；C 先提交有限观察模型、正确实现和受限模拟器。它们组织既有 33 条种子，不另增机制计数；用户安排其他人验证。详见[主线交接](records/2026-11-13-research-programs-handoff.md)，未运行实验或派发任务。

2026-11-13 增补[第九批 BOLD-20261113-31 至 33](brainstorms/2026-11-13-schedulers-invariants-selection.md)：31 先提交真实支路时序和共同控制规则；32 先核对变换族、功能正确性、不变量与读出资格；33 先提交触发丢弃的依赖图及目标独立的审计采样方案。均由用户安排其他人验证；详见[交接记录](records/2026-11-13-scheduler-invariant-selection-handoff.md)。未运行实验或派发任务，不改变已有实验判定和文献普查队列。

2026-11-13 增补[第八批 BOLD-20261113-28 至 30](brainstorms/2026-11-13-closed-loops-delayed-disclosure-leakage-contracts.md)：28 先核对闭合积分及真实恢复状态；29 先提交随机量与公开信息时间图，区分事后检验和自适应交互；30 先给出非平凡状态关系与逐历史组合前提。均由用户安排其他人验证；详见[交接记录](records/2026-11-13-closed-loop-disclosure-contract-handoff.md)。未启动实验或派发任务，也未更新既有实验判定。

2026-11-13 增补[第七批 BOLD-20261113-25 至 27](brainstorms/2026-11-13-spatial-modes-port-response-noise-geometry.md)：25 先提交空间与回流映射及留出位置预测；26 先提交允许激励、端口响应模型及主动/被动条件；27 先提交同实际成本的噪声配置与联合观察预算。三项均待验证，由用户安排其他人推进；详见[交接记录](records/2026-11-13-spatial-port-noise-handoff.md)。本轮未启动实验或派发任务。

2026-11-13 增补[第六批 BOLD-20261113-22 至 24](brainstorms/2026-11-13-predictive-states-criticality-security-order.md)：22 先提交旧模型等价的准备历史及跨操作预测；23 先核对增益、噪声、恢复时间与真实模态；24 先核对小通道反例，再定义成对防护的敏感任务及辅助信息。均待验证，由用户安排其他人推进；未启动实验或派发任务。详见[交接记录](records/2026-11-13-predictive-criticality-order-handoff.md)。

2026-11-13 增补[第五批 BOLD-20261113-19 至 21](brainstorms/2026-11-13-interventions-memory-device-diversity.md)，继续由用户安排其他人验证：19 提交竞争机制及能区分它们的保护干预；20 提交跨调用观测预算与物理状态模型；21 提交器件校准、共同状态和互补性资格诊断。三项均待验证，未启动实验或派发任务。详见[交接记录](records/2026-11-13-interventions-memory-diversity-handoff.md)。

[第四批 BOLD-20261112-16 至 18](brainstorms/2026-11-12-observation-as-computation.md) 按用户要求继续扩大构思，验证由其他人负责：16 先交付真实清理生命周期及全轨迹模型；17 先交付合法顺序、资源映射与可辨识关系；18 保留一次聚合响应映射和秘密等价类的诊断机会。三项全部待验证，没有启动实验或派发任务。已明确与旧方向及文献先例的区别，详见[交接记录](records/2026-11-12-observation-handoff.md)。

继续扩大的[第三批提案 BOLD-20261112-13 至 15](brainstorms/2026-11-12-model-breaking-directions.md) 已整理，仍由用户安排其他人验证：13 先找模型等价的合法执行对；14 先核对真实波形到结构化约束的映射与总求解成本；15 先独立检查同步例子并寻找真实振荡/自定时载体。已有先例与尚缺增量已分开标注，详见[交接记录](records/2026-11-12-model-breaking-handoff.md)。未运行新实验，未派发外部任务。

用户进一步要求扩大脑洞，验证仍由其他人负责。[第二批六项提案 BOLD-20261112-07 至 12](brainstorms/2026-11-12-beyond-values.md) 已形成；本批优先交接三个问题：07 的状态驻留与噪声时间尺度是否相容；08 的份额关系在哪里与测量链混合；09 的真实控制环及补偿量是否可观察。先提交实现映射、数学核对或明确反例，再决定实验预算。10–12 保留在种子池，旧方向仍保留。详见[交接记录](records/2026-11-12-beyond-values-handoff.md)。没有启动采集、仿真、训练或独立复算。

用户要求扩大构思并由其他人验证。[六项提案](brainstorms/2026-11-12-bolder-directions.md) 已记录机制、预测、反例、来源和未知项。本轮未启动新实验。建议第一批只做三项资格检查：

1. **BOLD-20261112-01：**从固定代码/RTL 提取真实随机依赖，证明候选抵消关系留下非公开量，并检查观测预算；不存在则提交反例。
2. **BOLD-20261112-02：**识别随机位请求与补给时序，检查给定公开上下文后是否仍可能依赖秘密；先区分供应元数据与随机值质量。
3. **BOLD-20261112-03：**核查秘密相关的活动分布与存储驻留，明确如何区分短时恢复、静态存储留痕与动态运算的长期影响。

当前 Reference-PPM 包不具备这三类机制的直接验证条件。04–06 留在提案池；不得以运行报错否定机制，也不得把讨论升级为实测支持。近五年论文库的覆盖核对与引用追踪仍需继续，本次定位性检索不算完成普查。

## 度量基础已更正（后续必读）

旧批反复引用的“单点 |t| 12–17 上限”是 **b1 目标失配**，不是信噪比。`r10`/`r00` 是 Montgomery 的近似随机重标记（`corr=0.07`、`sign` 一致率 51%）。换成结果值符号后同库单样本 AUC 0.994–1.000。**以后选点一律同时报线性 b1 与结果值符号两套目标。**

## 跨层八方向审计（EXP-20261111-10）后的增补

外部 brainstorm 的 B01–B08 已逐条判定，见记录 EXP-20261111-10。三条对下一步有直接影响：

1. **B07 位置绑定已被实测确认**（7/12 副本强且极性跨文件恒定，4 个在机会水平）。下一次选点必须报副本编号，不能只报"通道点"；单点结论要附同副本对照。
2. **B08 说明候选压缩已顶到 HW 别名天花板**（类均值 49.6、最大 138，与三位码 65 同量级）。继续换分类器收益有限，**要降候选只能加锚点或加精确值**，不是换模型。
3. **B04 的整数轨迹只有 0.1% R² 量级增量**，且 a 恒定时证明不了独立自由度。要证它，先做改 a 的构建。

## 本批结论

- PQC-H013 三通道（`sign(b1)` 30688 / `sign(r10)` 14360 / `sign(r00)` 33145，copy 26/12/28）**有限支持**：AUC 0.994–1.000、互检 0.37–0.65、`|b1|` 分层内 ≥0.993。缺陷：`same_copy_near` 判据恒真（退化成中心点 AUC），A599 的 r00 峰跨 copy 漂移 745 样本。
- PQC-H014 单 trace 候选集**不成立**：符号 1.000，但 HW 读数只精确命中 23%，候选集 7–14、命中 0.19–0.26。错配点集合更小（2–6）却更差（0.00–0.01）——**集合大小不能单独当指标**。
- PQC-H015 基线差分**不成立**：比值 0.26–0.38。

## 周期基线（更正）

基周期 **67.83**（整数化 68），1153 = 17 个周期。核验方 5 倍处反号是相位错位（5780 偏 14.4 样本 → −0.264；5765 偏 0.6 样本 → +0.575）。**长程对齐勿用 1156。**

## 下一条可执行动作（按价值）

1. **补第二个独立幅度读数**，让候选集真正收紧。方向：在 r10 通道的**多个 copy**上同时取同相位样本（同一 HW 的重复观测），而不是单点。这是 H014 失败唯一直接指向的增量路径。
2. **修正 H013 判据**：`same_copy_near` 换成“对该目标用全局 argmax 独立定位 + 峰区 Jaccard”，并把 A599 的 r00 漂移作为已知反例长期跟踪。
3. **验证 3 个符号位是否真的条件独立**：三通道互检 AUC 0.37–0.65 只是“不冗余”，不等于“给定 b1 后独立”。需要分层到固定 b1 值再互检（本数据 b1 近似单射，跨文件可按值配，但每值只有 1 条）。
4. 有板时：用 3 位通道做同 ELF 同址重复，检验位点是否随代码搬移。
5. 跨数据集复现：换新公开包，别再用这 12 个文件当确认。

## 恢复时必须记录

当前假设与版本、冻结协议 SHA、数据/代码版本、进程、已运行命令、产物位置、最近核验、未决分歧、下一动作、剩余预算、远端同步状态。

## 可复算入口

`scripts/signref/channels.py`（`--design` 仅 A99 选址 / `--fit` 拟合读数 / `--eval <tag>` 执行），`scripts/signref/sites.json`、`h014_fit.json` 与脚本同目录；数值见 `results/signref-2026-11-11/aggregate.json`；记录 `records/2026-11-11-signal-channels-batch.md`。
