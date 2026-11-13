# 侧信道科研知识库

更新日期：2026-11-13（保留既有实验批次，追加五批大胆方向与供他人验证的交接）。用途：让研究问题、证据、失败条件和下一步工作可检索、可复算、可接续。

2026-11-11 追加批次 EXP-20261111-07/08/09（离散通道）：**更正旧批的度量基础**——`r10`/`r00` 是 Montgomery 的近似随机重标记（`corr(r10,b1)=0.07`、`sign` 一致率 51%），所以拿 `b1` 做相关目标测的是被打散的代理，旧批 12–17 的“单点上限”是模型失配。换成结果值符号位后，三位点上单样本 AUC 0.994–1.000、互检 AUC 0.37–0.65（分处 copy 12/26/28）、`|b1|` 分层内最小 0.993 → PQC-H013 **有限支持**。H014（单 trace 候选集 ≤4）与 H015（基线差分）**不成立**，原因分别是幅度读数只精确命中 HW 23%、增益 CV 仅 0.10。核验方独立实现判定一致，核心数值 <1e−6；并指出主实现 `same_copy_near` 恒真、A599 有 1 处峰区漂移 745 样本。**仍未恢复任何 b1 完整值。**

2026-11-11 追加批次 EXP-20261111-01/02/03：在 SRC-001 上做公开实测再分析，确认集 A699/A799 一次性打开。PQC-H006（位点身份分裂）与 PQC-H007（`sign` 漂移排除）为**有限支持**；PQC-H008（归约后位点对中间量不可见）**当前实验不支持**。同时更正上一批的前提：`r10`/`r00` 是两个 Montgomery 结果（400/400 全等），**标签里没有物理前态**，本数据只有 `b1` 一个自变量。独立 GPT 核验对 H006/H007 逐位一致（1e−13），H008 由核验方先发现判据语义分歧、判定不通过。**无硬件、无模拟功耗、无密钥恢复。**

2026-11-11 追加批次 EXP-20261111-04/05/06（新攻击范式取向）：三条候选全部**不成立**，但产出可复用结构事实——原批次的“1153=17×68”等式存在算术错误；后续局部周期估计见[新增批次](records/2026-11-11-crosslayer-audit.md)，其结论边界见[静态审读](brainstorms/2026-11-11-two-hour/16-concurrent-evidence-boundary-review.md)；`trace 内有 N 个副本 ⇏ N 倍样本`（单点比相位折叠强 3.6–13.6 倍）；序号轴≈固定能量包络（随机偏移 null r=0.947）。M2 形状 AUC 0.80–0.85 但支持集不稳；M3 冗余项 R² 高 575 倍但符号跨文件翻转。核验方独立判同。

2026-11-07 追加批次 EXP-20261107-01/02/03 基于作者公开的 Reference-PPM 实测波形（CC BY 4.0）完成了：一次固定实现下的表示预测实验（四个留出文件，PQC-H001 → 有限支持）、一个 q=7 精确枚举算例（PQC-H002 → 仅逻辑有限支持）、一次前史交互资料资格核对（PQC-H004 → 条件缺失）。**不声称任何密钥恢复或物理机制归因**。独立 GPT 核验阶段 A/B/C 已全部完成并封存（独立实现封存于 2026-11-07T19:43:15+08:00，首次揭盲 19:43:42；阶段 C 比对 19:47:40）：H001 逐项一致（最大差 ≤3.98e−13，十二门 12/12），H002 由核验方发现主实现对公开 B 的边际化错误、修正后逐格一致（NLL 差 0），H004 一致。

## 从这里开始

- [保护干预、跨调用时间组合与器件互补；BOLD-19 至 21 待验证](brainstorms/2026-11-13-interventions-memory-device-diversity.md)
- [第五批交接：竞争机制、物理记忆与共同观测盲区](records/2026-11-13-interventions-memory-diversity-handoff.md)
- [改变观察对象：清理轨迹、编排测量与秘密整体结构；BOLD-16 至 18 待验证](brainstorms/2026-11-12-observation-as-computation.md)
- [第四批交接：三项最小资格诊断与已知反例](records/2026-11-12-observation-handoff.md)
- [再扩大研究对象：自动模型反例、测量与格求解联合设计、物理同步；BOLD-13 至 15 待验证](brainstorms/2026-11-12-model-breaking-directions.md)
- [第三批构思修订与验证交接](records/2026-11-12-model-breaking-handoff.md)
- [近五年文献库（建设中）：599 条 TCHES 标题初筛、105 篇阅读卡片、引用扩展与版本追踪](literature/README.md)
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
