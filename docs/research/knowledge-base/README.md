# 侧信道科研知识库

更新日期：2026-11-14（追加硬件适应、公开模拟与稀有路径构思，保留文献接续及既有实验状态）。用途：让研究问题、证据、失败条件和下一步工作可检索、可复算、可接续。

2026-11-11 追加批次 EXP-20261111-07/08/09（离散通道）：**更正旧批的度量基础**——`r10`/`r00` 是 Montgomery 的近似随机重标记（`corr(r10,b1)=0.07`、`sign` 一致率 51%），所以拿 `b1` 做相关目标测的是被打散的代理，旧批 12–17 的“单点上限”是模型失配。换成结果值符号位后，三位点上单样本 AUC 0.994–1.000、互检 AUC 0.37–0.65（分处 copy 12/26/28）、`|b1|` 分层内最小 0.993 → PQC-H013 **有限支持**。H014（单 trace 候选集 ≤4）与 H015（基线差分）**不成立**，原因分别是幅度读数只精确命中 HW 23%、增益 CV 仅 0.10。核验方独立实现判定一致，核心数值 <1e−6；并指出主实现 `same_copy_near` 恒真、A599 有 1 处峰区漂移 745 样本。**仍未恢复任何 b1 完整值。**

2026-11-11 追加批次 EXP-20261111-01/02/03：在 SRC-001 上做公开实测再分析，确认集 A699/A799 一次性打开。PQC-H006（位点身份分裂）与 PQC-H007（`sign` 漂移排除）为**有限支持**；PQC-H008（归约后位点对中间量不可见）**当前实验不支持**。同时更正上一批的前提：`r10`/`r00` 是两个 Montgomery 结果（400/400 全等），**标签里没有物理前态**，本数据只有 `b1` 一个自变量。独立 GPT 核验对 H006/H007 逐位一致（1e−13），H008 由核验方先发现判据语义分歧、判定不通过。**无硬件、无模拟功耗、无密钥恢复。**

2026-11-11 追加批次 EXP-20261111-04/05/06（新攻击范式取向）：三条候选全部**不成立**，但产出可复用结构事实——原批次的“1153=17×68”等式存在算术错误；后续局部周期估计见[新增批次](records/2026-11-11-crosslayer-audit.md)，其结论边界见[静态审读](brainstorms/2026-11-11-two-hour/16-concurrent-evidence-boundary-review.md)；`trace 内有 N 个副本 ⇏ N 倍样本`（单点比相位折叠强 3.6–13.6 倍）；序号轴≈固定能量包络（随机偏移 null r=0.947）。M2 形状 AUC 0.80–0.85 但支持集不稳；M3 冗余项 R² 高 575 倍但符号跨文件翻转。核验方独立判同。

2026-11-07 追加批次 EXP-20261107-01/02/03 基于作者公开的 Reference-PPM 实测波形（CC BY 4.0）完成了：一次固定实现下的表示预测实验（四个留出文件，PQC-H001 → 有限支持）、一个 q=7 精确枚举算例（PQC-H002 → 仅逻辑有限支持）、一次前史交互资料资格核对（PQC-H004 → 条件缺失）。**不声称任何密钥恢复或物理机制归因**。独立 GPT 核验阶段 A/B/C 已全部完成并封存（独立实现封存于 2026-11-07T19:43:15+08:00，首次揭盲 19:43:42；阶段 C 比对 19:47:40）：H001 逐项一致（最大差 ≤3.98e−13，十二门 12/12），H002 由核验方发现主实现对公开 B 的边际化错误、修正后逐格一致（NLL 差 0），H004 一致。

## 从这里开始

- [硬件适应、公开可模拟波形与稀有泄漏路径：三个待他人验证的问题](brainstorms/2026-11-14-adaptive-hardware-simulation-rare-paths.md)
- [本轮交接：实际反馈、模拟命题与首次进入预测](records/2026-11-14-adaptation-simulation-rare-paths-handoff.md)
- [mUOV 与 Falcon 引用接续：20 条发现解析、18 张新卡片及采样时序边界](records/2026-11-14-literature-masking-foundations.md)
- [器件条件、噪声响应与判定边界几何：三个待他人验证的问题](brainstorms/2026-11-14-population-noise-response-boundaries.md)
- [本轮交接：合法校准、物理关系与留出方向预测](records/2026-11-14-population-response-boundary-handoff.md)
- [CCS 2025 第二轮文献：11 张新卡片、指标与迁移边界、Swallow 引用接续](records/2026-11-14-literature-ccs2025-second-pass.md)
- [瞬态响应、运算顺序与防护条件的整体相容性：待他人验证](brainstorms/2026-11-14-transients-switching-compatibility.md)
- [本轮交接：物理度量、合法编排与约束冲突](records/2026-11-14-transient-switching-compatibility-handoff.md)
- [UOV 引用接续：六张新卡片、floor 正式书目与 Maskaglia](records/2026-11-14-literature-muov-followups.md)
- [CCS 2025 文献接续：316 条标题、19 条新卡片与 UOV 引用追踪](records/2026-11-14-literature-ccs2025-first-pass.md)
- [跨密钥物理关系、光子事件与后量子求解成本：三个待他人验证的问题](brainstorms/2026-11-14-key-populations-photon-events-quantum-costs.md)
- [本轮交接：独立秘密的关系图、同次事件观察与完整资源账本](records/2026-11-14-key-photon-quantum-handoff.md)
- [USENIX 2025 引文接续：15 条新卡片、版本核实及 Aegis 防护边界](records/2026-11-14-literature-usenix2025-citation-followup.md)
- [计算冗余、拒绝轨迹与随机计算图：三个待他人验证的方向](brainstorms/2026-11-14-computation-codes-rejected-transcripts-random-graphs.md)
- [本轮交接：跨实现预测、完整转录与路线的联合推断](records/2026-11-14-computation-rejection-graph-handoff.md)
- [USENIX 2025 文献接续：36 条新卡片、438 条目录对应及盲分析/计数器证据边界](records/2026-11-14-literature-usenix2025.md)
- [物理遗忘、份额的时空隔离与可逆计算：三个待验证方向](brainstorms/2026-11-14-physical-forgetting-spacetime-reversible-computation.md)
- [本轮交接：未来观察、传播图与完整能量记账](records/2026-11-14-forgetting-spacetime-reversible-handoff.md)
- [回路关系、正确性裕量与防护后的信息迁移：三项详细提案，待他人验证](brainstorms/2026-11-14-cycle-relations-correctness-margins-leakage-migration.md)
- [本轮交接：真实关联、留出工作点与完整观察预算](records/2026-11-14-cycle-margin-migration-handoff.md)
- [S&P 2026 文献接续：32 条新卡片、目录缺项及 Goldilocks 证据边界](records/2026-11-14-literature-sp2026.md)
- [算法噪声的侧信息、高维去匿名化与跨尺度模型：三个大胆方向，待他人验证](brainstorms/2026-11-14-noise-labels-anonymity-and-scale.md)
- [本轮交接：误差生命周期、图的等价类与尺度转换](records/2026-11-14-noise-anonymity-scale-handoff.md)
- [秘密算子、物理操作语法与面向观察者的实现设计：三个长期目标，待他人验证](brainstorms/2026-11-14-secret-operators-physical-grammar-observation-design.md)
- [本轮交接：合法等价类、组合预测与可实现的共同盲区](records/2026-11-14-operator-grammar-observation-handoff.md)
- [PQC 文献接续：25 条论文/版本卡片、恢复目标与引用初筛](records/2026-11-13-literature-pqc-citation-followups.md)
- [计算轨迹的防护编码、任务安全与物理可辨识性：六个开放问题，三项详细提案](brainstorms/2026-11-13-trajectory-codes-task-security-identifiability.md)
- [本轮交接：观察族、任务定义、等价模型与独立锚点](records/2026-11-13-trajectory-task-identifiability-handoff.md)
- [时间方向、模约减商与混合算法的物理组合：三项深化，待他人验证](brainstorms/2026-11-13-time-arrow-quotients-hybrid-composition.md)
- [本轮交接：同谱见证、整数语义与组合观察游戏](records/2026-11-13-time-quotient-hybrid-handoff.md)
- [MPCitH 与 FAEST/HQC 文献接续：16 条卡片、版本撤回和 95 条引用初筛](records/2026-11-13-literature-mpcith-followup.md)
- [安全资源下界、难问题泄漏与跨实现预测：三项研究深化，待他人验证](brainstorms/2026-11-13-resource-bounds-lwe-leakage-counterfactuals.md)
- [本轮交接：资源反例、全执行模拟与留出实现预测](records/2026-11-13-resource-lwe-counterfactual-handoff.md)
- [USENIX 2026 文献接续：362 条目录对应、34 条新卡片与 PQC 证据边界](records/2026-11-13-literature-usenix2026.md)
- [随机源反馈、求解难度与物理状态发现：一个新种子及两项深化，待他人验证](brainstorms/2026-11-13-randomness-feedback-hardness-state-discovery.md)
- [本轮交接：耦合闭环、约束成本与分叉干预](records/2026-11-13-randomness-hardness-state-handoff.md)
- [Kyber 打乱引用后续：九条新卡片、已有硬件攻击的正文升级及错链纠正](records/2026-11-13-literature-kyber-shuffle-followups.md)
- [算法约束自校准、隐藏编码与可感知测量；BOLD-37 至 39 待验证](brainstorms/2026-11-13-self-calibration-hidden-encoding-observer.md)
- [第十一批交接：可辨识性、编码节点和观察者反作用](records/2026-11-13-calibration-encoding-observer-handoff.md)
- [三个更大胆的原型：泄漏回波、动态表示与机制发现；待验证](brainstorms/2026-11-13-echo-representations-mechanism-discovery.md)
- [原型交接：操作对、表示图与事前干预预测](records/2026-11-13-echo-representation-discovery-handoff.md)
- [S&P 2022 与 Kyber 引用接续：33 条新卡片、147 条目录对应和恢复范围](records/2026-11-13-literature-sp2022-kyber-four.md)
- [密钥与器件的交互、种子展开与防护规模；BOLD-34 至 36 待验证](brainstorms/2026-11-13-key-device-seeds-scaling.md)
- [第十批交接：合法密钥总体、秘密生命周期与资源边界](records/2026-11-13-key-seed-scaling-handoff.md)
- [三条研究主线：物理状态发现、关系计算与实现逆向设计；待验证](brainstorms/2026-11-13-three-research-programs.md)
- [研究主线交接：从 33 条种子到三个可持续推进的问题](records/2026-11-13-research-programs-handoff.md)
- [调度器的关系计算、防护的不变量与采集选择；BOLD-31 至 33 待验证](brainstorms/2026-11-13-schedulers-invariants-selection.md)
- [第九批交接：控制节点、变换轨道和未保存的执行](records/2026-11-13-scheduler-invariant-selection-handoff.md)
- [闭合路径、后续公开信息与组合契约；BOLD-28 至 30 待验证](brainstorms/2026-11-13-closed-loops-delayed-disclosure-leakage-contracts.md)
- [第八批交接：积分模型、信息时间图与逐历史保证](records/2026-11-13-closed-loop-disclosure-contract-handoff.md)
- [空间电流、端口响应与防护噪声方向；BOLD-25 至 27 待验证](brainstorms/2026-11-13-spatial-modes-port-response-noise-geometry.md)
- [第七批交接：空间预测、响应边界与同成本噪声配置](records/2026-11-13-spatial-port-noise-handoff.md)
- [预测状态、临界响应与防护信息偏序；BOLD-22 至 24 待验证](brainstorms/2026-11-13-predictive-states-criticality-security-order.md)
- [第六批交接：抽象修补、放大收益与防护排序反例](records/2026-11-13-predictive-criticality-order-handoff.md)
- [保护干预、跨调用时间组合与器件互补；BOLD-19 至 21 待验证](brainstorms/2026-11-13-interventions-memory-device-diversity.md)
- [第五批交接：竞争机制、物理记忆与共同观测盲区](records/2026-11-13-interventions-memory-diversity-handoff.md)
- [改变观察对象：清理轨迹、编排测量与秘密整体结构；BOLD-16 至 18 待验证](brainstorms/2026-11-12-observation-as-computation.md)
- [第四批交接：三项最小资格诊断与已知反例](records/2026-11-12-observation-handoff.md)
- [再扩大研究对象：自动模型反例、测量与格求解联合设计、物理同步；BOLD-13 至 15 待验证](brainstorms/2026-11-12-model-breaking-directions.md)
- [第三批构思修订与验证交接](records/2026-11-12-model-breaking-handoff.md)
- [近五年文献库（建设中）：2,828 条标题初筛、479 条阅读卡片、引用扩展与版本追踪](literature/README.md)
- [掩码与硬件补读：16 条新增记录、八条发现解析及版本/模拟边界](records/2026-11-13-literature-masking-lineage-hardware.md)
- [S&P 2023 全标题、47 篇摘要补读及掩码/恒时引用](records/2026-11-13-literature-sp2023-candidates.md)
- [S&P 2024 摘要补读、261 条目录核对与 Episode V 引用补漏](records/2026-11-13-literature-sp2024-candidates-kyber-v.md)
- [S&P 接续：25 篇摘要、16 篇新增卡片、2024 年 261 条标题与题名归并](records/2026-11-13-literature-sp2025-remaining-sp2024-titles.md)
- [TCHES 候选补读：86 篇摘要、9 篇新增卡片及实现证据范围](records/2026-11-13-literature-tches-remaining.md)
- [文献接续：四条引用解析、12 篇新增卡片及 S&P 2025 印刷目录逐项核对](records/2026-11-13-literature-power-sp2025-followup.md)
- [TCHES 范围复核与 S&P 2025 接续：255 条标题、13 篇新增卡片及 12 条引用边](records/2026-11-13-literature-scope-and-sp2025.md)
- [2026-11-13 文献接续：新增 49 篇卡片，解析 9 条引用发现并整理比较条件](records/2026-11-13-literature-pqc-followup.md)
- [文献筛查与引用补漏批次：S&P 官方目录遗漏、扩展来源和阅读边界](records/2026-11-12-literature-screening-citation-batch.md)
- [继续扩大构思（2026-11-12）：噪声动力学、模拟混合、控制器补偿等六项；全部待验证](brainstorms/2026-11-12-beyond-values.md)
- [本次构思修订与三个交接问题](records/2026-11-12-beyond-values-handoff.md)
- [六个更大胆的方向（2026-11-12）：随机依赖关系、随机位供给、长期器件变化等；全部待验证](brainstorms/2026-11-12-bolder-directions.md)
- [本轮构思与交接记录（未运行新实验）](records/2026-11-12-bold-research-handoff.md)
- [两小时深入发散记录（2026-11-11，已完成；13 篇专题与验证交接）](brainstorms/2026-11-11-two-hour/README.md)
- [三个优先验证方向：内部锚点、同步参考、SLH-DSA 跨角色记忆](brainstorms/2026-11-11-two-hour/14-priority-validation-handoff.md)
- [理论命题、否定性知识与证据状态](brainstorms/2026-11-11-two-hour/15-claims-evidence-and-negative-knowledge.md)
- [并行新增批次的证据边界审读（仅静态检查，未复算）](brainstorms/2026-11-11-two-hour/16-concurrent-evidence-boundary-review.md)
- [发散假设池：八个跨层方向（2026-11-11，供他人验证，未运行实验）](brainstorms/2026-11-11-cross-layer-directions.md)
- [自主研究提示词：Codex + 独立 GPT Agent](prompts/autonomous-gpt-research.md)
- [工作流程与知识入库规则](WORKFLOW.md)
- [模型索引与三张候选卡](MODEL_INDEX.md)
- [来源索引与实际阅读范围](SOURCE_INDEX.md)
- [模板：实验记录](templates/experiment-record.md)
- [实验记录：Reference-PPM 批次 EXP-20261107-01/02/03](records/2026-11-07-reference-ppm-batch.md)
- [实验记录：位点分裂批次 EXP-20261111-01/02/03](records/2026-11-11-site-split-batch.md)
- [实验记录：新范式批次 EXP-20261111-04/05/06（全负）](records/2026-11-11-paradigm-batch.md)
- [实验记录：离散符号通道批次 EXP-20261111-07/08/09](records/2026-11-11-signal-channels-batch.md)
- [实验记录：位点分裂批次 EXP-20261111-01/02/03](records/2026-11-11-site-split-batch.md)（本批含一处负结果与前提更正）
- [复算脚本](scripts/h001_representation.py)、[精确算例](scripts/h002_exact.py)、[小型结果](results/reference-ppm-2026-11-07/summary.json)

### 复算 H001 的最小步骤

1. 从 DOI [10.5281/zenodo.15352482](https://doi.org/10.5281/zenodo.15352482)（CC BY 4.0）取发布包，按 [members-manifest.json](results/reference-ppm-2026-11-07/members-manifest.json) 逐成员验收长度、CRC32 与 SHA-256（12 个成员；本仓库不含任何波形样本）。
2. 由**独立**核对方从留出标签的第二个 LE signed16 字导出 `b1_A*.csv`（100 行、原始行序、无标题），并保存 SHA-256 清单；主拟合不得打开留出 `noncesA*.mat`。
3. `.venv/bin/python scripts/h001_representation.py --mode freeze-dev --root <repo-root>` 冻结开发选点与系数；再 `--mode holdout --root <repo-root>` 读一次留出并出判定。
4. 精确算例无需数据：`.venv/bin/python scripts/h002_exact.py`（`H002_OUTDIR` 指定输出目录）。
- [下一步与当前缺口](NEXT_ACTION.md)
- [本次知识库初始化记录](records/2026-11-07-initialization.md)

## 与已有材料的关系

- [完整研究报告](../nist-pqc-hardware-sidechannel-report.md)：原有综述，其原始信息截点继续保留。
- [原始研究证据索引](../evidence-matrix.md)：既有文献证据入口；本知识库的来源索引是补充。
- [研究思考](../../14-research-thinking.md)：研究方法背景。
- [教程](../../../TUTORIAL.zh-CN.md)、[ML-KEM 课件](../../../courses/ml-kem/README.md)、[教学实验说明](../../../labs/README.md)：学习入口。教学与合成结果不自动升级为真实测量证据。

## 一条知识的最小单位

使用稳定 ID 关联问题、来源、实验与结论。例如 PQC-H001（假设）、SRC-001（来源）、EXP-日期-序号（实验），而不是以聊天标题作为证据。

每条记录至少写明：主张、类型、适用条件、来源及阅读范围、反证或限制、证据位置、实际核验方式、更新日期、下一步。模型卡和实验记录使用下列状态：

| 状态 | 含义 |
|---|---|
| 待验证 | 提案，尚无对应实验 |
| 有限支持 | 仅在列明实现、数据与预算下得到支持 |
| 当前实验不支持 | 该版本的预定预测未获支持；写明检验能力 |
| 证据不足 | 不能在竞争解释之间作出判断 |
| 条件缺失 | 缺数据、实现、仪器或其他必要条件 |
| 被新版本替代 | 保留旧记录并链接后继版本 |

“文献报告”“本地复现”“模拟验证”“实测验证”单独标注，不能只用一个“已验证”标签。主 Agent 负责汇总；子代理原始意见及未解决分歧必须可追溯。
