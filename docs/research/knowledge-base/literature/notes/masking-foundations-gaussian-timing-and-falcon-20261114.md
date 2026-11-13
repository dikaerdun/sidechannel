# 掩码基础 高斯采样时序与 Falcon 引用证据

更新日期：2026-11-14。沿 mUOV 与 Falcon floor 的实际书目，本批解析 20 条待查引用，新增 18 张阅读卡片和三条相邻判定；另通过一条实际引用补入 2022 年高斯采样论文。共新增 21 条目录、21 条引用和 11 条版本关系，其中八条有显式发表说明、三条仍为推定。

18 张卡片中，EUROCRYPT 2023 的 Falcon 攻击与 Cybersecurity 2022 的采样论文在冻结五年窗口内；其余 16 张为引用追踪所需的早期基础研究。读过摘要不等于审完证明或复现实验。

## 实际引用的身份

| 引用组 | 本批处理 | 当前状态 |
|---|---|---|
| mUOV 52 个作者稿书目位置 | 解析九条，包含八条纳入、一条相邻理论 | 27 条目录对应，一条待查，24 条暂列背景 |
| Falcon floor 31 个正式书目位置 | 解析十一条，包含九条纳入、两条相邻 | 21 条目录对应，零条待查身份，十条暂列背景 |
| 2022 Gaussian 论文 | 核对其参考 22 确实引用 PQCrypto 2020 sampler | 仅此位置选读，其余 44 个位置未筛查 |

完整清单见 [mUOV](../citations/muov2025-reference-screen.jsonl)、[floor](../citations/falcon-floor-reference-screen.jsonl)与 [2022 Gaussian 选读](../citations/gaussian2022-selected-reference-screen.jsonl)。floor 的“零条待查身份”只涉及这次已列入待查队列的条目；十条暂列背景、目标论文正文、版本和递归引用均未闭合。

TCHES 的两篇转换/低延迟论文出版页使用历史 `10.13154` DOI，当前 Crossref 注册记录为 `10.46586`。题名、作者、年份和页码对应，旧 DOI 保存在目录字段；floor 的 B2A 引用确实印出旧 DOI，mUOV 的低延迟引用则未印 DOI，二者不混同。未将这个身份对应算成新版本边。B2A 旧 DOI 的 Crossref 请求返回 404，不代表论文不存在。

CARDIS 2014 的 *Lazy Engineering* 章节在 2015 年出版，会议年和出版日期分别保留。CRYPTO 2021 *Secure Wire Shuffling* 也在 2021-11-12 起点之前，不计为窗口内研究。

[Power Analysis Attacks](https://link.springer.com/book/10.1007/978-0-387-38162-6) 的出版页列第一版版权 2007、硬皮 2007-03-12、电子版 2008-01-03、平装 2010-10-29。floor 的 MOP08 引用可对应该书，但没有明确物理载体；本批只读出版商简介与版本元数据，放在相邻基础入口。

mUOV 参考 12 实际引用的是 [ePrint 2024/609](https://eprint.iacr.org/2024/609)，因此目录保留该身份。这是 Hash-and-Sign with Retry 的经典安全证明改进，不能写成功耗测量或量子模型中的同等紧界。

## 掩码转换与物理模型的分界

| 论文 | 原始来源中的研究对象 | 本库保留的条件 |
|---|---|---|
| [CHES 2014 双向转换](https://link.springer.com/chapter/10.1007/978-3-662-44709-3_11) | 任意阶 A2B/B2A，摘要复杂度 O(n²k)，32 位 AVR HMAC-SHA-1 周期 | n 为保护阶数，k 为位宽；ISW 证明与周期不等于物理测量保证 |
| [FSE 2015 A2B](https://link.springer.com/chapter/10.1007/978-3-662-48116-5_7) | Kogge-Stone 加法结构，位宽对数复杂度 | 摘要明确证明一阶；不能因它被高阶方案引用就改成任意阶保证 |
| [CHES 2017 B2A](https://link.springer.com/chapter/10.1007/978-3-319-66787-4_5) | 位宽无关的高阶转换及旧构造攻击 | 针对 Hutter-Tunstall 的攻击不能改写成对所有转换算法的否定 |
| [TCHES 2018 改进 B2A](https://doi.org/10.46586/tches.v2018.i2.22-45) | 减少刷新、保持指定探针模型证明 | 约 25% 是作者对转换算法的性能报告，不是完整 PQC 签名提速 |
| [Lazy Engineering](https://link.springer.com/chapter/10.1007/978-3-319-16763-3_5) | 中间值模型到转换泄漏模型的保证损失，两个微控制器评估 | 摘要中的阶数折半有模型与实现前提，不是无条件物理定律 |
| [maskVerif](https://link.springer.com/chapter/10.1007/978-3-030-29959-0_15) | 含毛刺或转换的自动掩码验证 | “包含物理效应”仍指工具编码的观察模型 |
| [robust probing](https://doi.org/10.46586/tches.v2018.i3.89-120) | 鲁棒性与组合性的共同形式化 | 部件实现细节是证明条件，不能只引用模型名称 |
| [PINI](https://doi.org/10.1109/TIFS.2020.2971153) | 按份额位置的组合规则及 MIMO-SNI | 作者稿第一页也明确探针证明只是实际实现分析的一步 |
| [Secure Wire Shuffling](https://link.springer.com/chapter/10.1007/978-3-030-84252-9_8) | 最坏情形探针下的统计安全与线性 t 开销 | 与完美安全掩码的保证不同；摘要 AES 性能优势条件为 t≥6000 |

以上除 PINI 第一页引言外，本批主要读完整原始摘要，未完整审读定理。PINI 的正文阅读范围也仅限作者稿第一页，不能写成完成全篇组合证明核验。

## DOM 与低延迟方案的数字不能拼接

mUOV 引用的是 TIS 2016 的 DOM 会议摘要。作者机构页明确分类为会议摘要并给出 ACM DOI；Crossref 为页码 3–3。机构页另有不一致的页数栏，因此本库保留原始页码，不依赖该栏推断篇幅。[作者机构记录](https://tugraz.elsevierpure.com/en/publications/domain-oriented-masking-compact-masked-hardware-implementations-w/)

该摘要报告约 6 kGE、每 S-box 18 个随机位、综合至第 15 保护阶，以及至第二保护阶的 t-test 评估；[ePrint 2016/486](https://eprint.iacr.org/2016/486) 摘要则给出 7.1 kGE。两者不得合成一个“最佳配置”，综合阶数也不等于同阶物理评估。预印本仍标为 preprint，版本关联只记为推定。

[Generic Low-Latency Masking](https://doi.org/10.46586/tches.v2018.i2.1-21) 的摘要讨论跳过份额压缩的极端变体，以及不同面积/延迟折衷。不能把某变体不需要在线随机性的性质，与另一个压缩输出变体的面积、接口和周期混为一谈。Ascon 的至三阶形式验证与 AES 的其他评估分别保留。

## Gaussian 采样的 isochrony 保护什么

[Howe 等的 PQCrypto 2020 论文](https://link.springer.com/chapter/10.1007/978-3-030-44223-1_4)用 isochrony 表示运行时间与指定敏感变量的独立性或统计接近，而非每次调用运行完全相同的时间。作者托管 25 页稿的第 4 页 Definition 4、第 9 页 Theorem 8/Corollary 9 已选读；第 9 页已目视核对。[作者稿](https://tprest.github.io/pdf/pub/isochronous-gaussian-sampling.pdf)

Theorem 8 包含基本整数和浮点运算 isochronous 的前提，并约束标准差与误差参数。摘要中任意中心/标准差的框架能力，不免除具体实现中的参数范围、原语和预计算条件。SAGA 是采样分布的统计检查入口，不能代替功耗或 EM 防护验证。

沿后续引用补入 [Sun 等 Cybersecurity 2022](https://link.springer.com/article/10.1186/s42400-022-00113-0)。正式 PDF 第 3 页表 1、贡献段和第 5 页定义/原语假设已读并目视核对，发现以下比较边界：

- Type I 针对 σ、c、z；Type II 针对 c、z；Type III 仅针对 z。比较采样吞吐时必须同时报告类型。
- 表 1 脚注 d 提醒 COSAC 的拒绝率仍似乎依赖 c，作者的 Algorithm 8 也可能有同样问题；这不是对 Algorithm 4 Type I 变体的同一项判定。
- FALCON 的 13–14% 签名提速以 LDL 树已经建立为条件；PALISADE 的 44.12% 是在线 G-lattice 采样阶段，不能当作完整生命周期加速。
- 整数四则、部分浮点、取整和位运算的 isochrony 是前提，浮点除法等涉及预计算。这里没有提供一般功耗/EM 安全结论。

该文参考 22 核实了它对 Howe 2020 的引用。其 ePrint 2021/199 与 2022 正式论文的题名作者对应，但 ePrint 仍写 preprint，故版本关系记为推定；正式 2022 日期在窗口内，不把 2021 预印本日期替换成正式发表日期。

## BLISS 与 Falcon 的恢复预算

| 论文 | 摘要报告的观察与结果 | 不能省略的区别 |
|---|---|---|
| [Flush Gauss and Reload 2016](https://link.springer.com/chapter/10.1007/978-3-662-53140-2_16) | 理想侧信道约 450 签名；真实 Flush+Reload 概念验证不足 3500 签名 | 0.96 成功率和小预算属于理想情况，不能替代缓存实验条件 |
| [BLISS 分支与 EMA 2017](https://eprint.iacr.org/2017/505) | 相对范数、分支跟踪、稀疏乘法 EMA 三条路线 | 相对范数路线有因子分解条件；单次分支跟踪与单条 AVR EMA 是不同能力 |
| [BLISS-B 2017](https://eprint.iacr.org/2017/490) | strongSwan 生产实现异步缓存观测，约 6000 次签名生成 | 不与前作理想侧信道预算混合，仍需核查具体版本和总后处理成本 |
| [Improved Falcon 2023](https://link.springer.com/chapter/10.1007/978-3-031-30634-1_19) | 三组预算：220000 traces 且约 25% 成功；170000 traces 符号路线；45000 signature measurements 双泄漏组合 | 三组条件不得合并为普遍的 45000 条功耗波形恢复保证 |

Falcon 2023 的正式与 ePrint 摘要明确报告 Cortex-M4 上发现符号泄漏，但完整恢复流程的测量、模拟、分类和后处理条件仍需论文正文。直接 ePrint PDF 返回 403；Springer 的 PDF URL 返回 200，却重定向为 HTML 章节页。已在 provenance 中显式记录，不能把 HTTP 200 写成 PDF 已获取。

IACR 托管的[作者报告幻灯](https://iacr.org/submit/files/slides/2023/eurocrypt/eurocrypt2023/102/slides.pdf)可读取。文件含 55 个物理页，逻辑页码为 31 页并有叠加动画；本批选读逻辑页 20、22–26。第 22 页明确使用半空间学习来组织符号泄漏，后续讨论方向估计与筛选。这也是[判定边界几何提案](../../brainstorms/2026-11-14-population-noise-response-boundaries.md)需要比较的已有研究先例，不能把从泄漏学习方向本身称为新颖性。

幻灯不能补足论文中的所有实验条件，故 Falcon 卡片仍保持摘要阅读级别，另记补充材料阅读。提取器对一个图形对象有解码警告，且动画隐藏层会进入文本；数值结论采用正式摘要，未从未核对的曲线估算额外成功率。

[BEARZ](https://eprint.iacr.org/2019/478) 的摘要明确把 100% 恢复标为故障后处理模拟，另讨论故障与计时防护成本。此项进入相邻层，正式引用边指向 SCITEPRESS 论文，预印本关系独立保存，不写成功耗实测攻击。

## 接续与证据层级

新增卡片的三条正文选读是 PINI 作者稿第一页、Howe sampler 作者稿指定两页、Sun sampler 正式稿指定页面；另外十五条保持摘要层级。完整原始摘要、PDF 和 HTML 留在仓库外缓存，只公开原创整理、元数据、来源哈希和关系。

下一步先取得 UOV 2018 完整原始摘要及 Falcon 2023 论文正文，补 Sun 2022 剩余 44 条引用。随后继续 mUOV 最终 ACM 书目、floor/Maskaglia 的完整保护边界，以及核心年度未读目录。没有运行实验、训练、仿真或作者代码；本批不代表近五年覆盖完成。
