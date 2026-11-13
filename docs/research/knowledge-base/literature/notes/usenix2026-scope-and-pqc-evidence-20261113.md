# USENIX 2026 目录范围与后量子证据

日期：2026-11-13。完成 362 篇研究论文的标题初筛与 76 篇摘要判定，新增 34 条卡片、41 条相邻判定，已有 ML-KEM 预言机卡片升级为指定正文阅读。以下为作者报告与来源核查，没有运行作者代码或实验。

## 议程与论文集数量

[官方议程](https://www.usenix.org/conference/usenixsecurity26/technical-sessions)有 381 个 paper 类节点，但该网页结构同时装载演讲和历史回顾。旧解析器要求链接含 `/presentation/`，漏记了三条采用其他路径的演讲；另把有作者文本栏的历史回顾误判为新论文。

[回顾页面](https://www.usenix.org/conference/usenixsecurity26/presentation/tot-discussion)明确说明 Stealing Machine Learning Models via Prediction APIs 原于 2016 年报告。修正后为 362 篇研究论文与 19 条其他议程活动；原有非论文记录保留，增加四条排除理由，没有删除研究论文。

单独下载的[正式目录](https://www.usenix.org/sites/default/files/sec26_contents.pdf)共 27 页，解析出 362 条，与议程研究条目双向对应。[主席报告](https://www.usenix.org/sites/default/files/sec26_message.pdf)第 4 页的两轮录用数为 166、196，总计 362。361 条标题规范化后相同，一条 L∞ 与 L_infinity 为同一数学记号，已视读目录第 13 页；Lighthouse 的 O(1) 混合字体也保留。目录对应只证明成员关系，不证明摘要、全文或引文已经读完。

修订解析器后以 2021–2026 缓存检查节点记账：前五年目录数量不变，仅 2026 移出历史回顾。实现见[解析器](../tools/harvest_catalogs.py)、[目录对应脚本](../tools/reconcile_usenix2026_toc.py)与[逐条清单](../toc-crosschecks/usenix-2026.jsonl)。官方 PDF 与议程来自同一组织，是分别取得的出版资料，不是独立研究者的主题复审。

## SDitH 的保护配置与随机性预算

[Amortizing Randomness Cost](https://www.usenix.org/conference/usenixsecurity26/presentation/liu-guowei) 的[正式 PDF](https://www.usenix.org/system/files/usenixsecurity26-liu-guowei.pdf)选读页为 5、9、12–16，覆盖 Seed 边界、资源预算、实验与局限及引用。

- **16 B/签名只计 Common Shares 的算术掩码随机性。** 可复用矩阵按签名刷新，不能跨签名复用。DOM/SNI Keccak 仍占主要随机性开销，不能把局部预算写成完整签名的全部随机性。
- **选择性 Seed 边界不是公开值边界。** 每次签名的新种子可在限定阶段不掩码；完整隐藏种子或种子树的单迹线恢复不在其保护声明内。种子展开为协议份额，或吸收秘密相关 aux 后，需要转为受保护状态。
- **实验配置需要明确。** 第 12–14 页的一阶 EM TVLA 包含指定热点与 RNI+opt+IND-Keccak 的部分签名段；IND 的一阶独立性不能继承 DOM/SNI 的组合保证。未检出不排除高阶、水平分析或其他测量条件。

原文声明的 [Zenodo 材料](https://doi.org/10.5281/zenodo.20432040)尚未检查内容。已连入 Picnic、Threshold-Computation-in-the-Head、无新鲜随机性的组合、NullFresh 与 Common Shares 五条引用；FAEST、两篇 PQCrypto、HYPERSHIELD 与窗口前 SNI-in-the-head 进入待解析发现。选读清单不是全部 27 条参考文献的范围审查。

## ML-KEM 查询效率与实际测量

[Hybrid Adaptive-LDPC](https://www.usenix.org/conference/usenixsecurity26/presentation/guo-qian) 的[正式 PDF](https://www.usenix.org/system/files/usenixsecurity26-guo-qian.pdf)选读第 12–16 页，并视读表 3。

摘要中的 2,950 次对应指定准确率的 ML-KEM-768 预言机查询。GoFetch 实例采用同机无特权进程、独立地址空间、高分辨率计时和校准，不能改写为网络远程或浏览器攻击。作者的具体测量平台为 M1 MacBook Air、macOS 13.5。

正文的 ML-KEM-512 实验有 100 次尝试，作者将与真实秘密相差不超过四个系数的 73 次归为成功。表 3 仅对这个子集汇总，平均 6,047.84 条迹线只计恢复阶段；约 25 分钟的总时间则包含接近一半的校准。这里必须区分成功判据、逐系数零误差、查询数、重复测量数和校准成本。

第 15 页对 ML-KEM-1024 是方法适用性及预期成本讨论，不是该节的 1024 硬件实测。此处只核实正文所见实验，不能凭摘要的广泛措辞补出其他参数组的测量。作者明确表示关闭相关 DMP 路径仍可阻断这一具体通道。

已补上对 KyberSlash 和 GoFetch 的引用边；作者声明的 [Zenodo 材料](https://doi.org/10.5281/zenodo.17899501)未运行，最终稿与预发布稿也尚未逐段比较。

## microSCALE 的指标与单位疑点

[microSCALE](https://www.usenix.org/conference/usenixsecurity26/presentation/kumar-e) 的[正式 PDF](https://www.usenix.org/system/files/usenixsecurity26-kumar-e.pdf)第 13–14 页将静态分析与 FPGA 上一轮 GIFT 的 EM TVLA 对照。表 4 的转换泄漏计数与图 6 的超阈时间样点不是同一指标；90.3% 对应后者的减少，不能写成密钥恢复能力或攻击成功率减少。

第 13 页同时写 500 kS/s、每 2 µs 一个样点、50 MHz 时钟和约十个样点/周期。前三个数推出每周期 0.01 个样点，无法与第四项兼容。该处已经检查渲染页，不是仅靠文本抽取发现的异常。保留为未解决的采集参数问题，不自行将 kS/s 改成 MS/s，也不据此否定其余全部结果。

## 摘要范围判定与勘误

LoongLeak 明确报告无需时序或侧信道的架构读出；StackWarp、FABRICKED、STALEUS 等主要是完整性破坏或直接读写，保存在相邻层。Motion in the Clear 使用未加密 UDP 载荷，不能作为加密流量旁路恢复的案例。相反，数据库后过滤时序、OVS 缓存、合并 token 长度、MIG barrier 与 GPU 时间片均有明确的额外观察关系，进入一般侧信道层。

阈值 ML-DSA、Quorus 与混合 AKEM 属于协议构造；协议份额不能当成本地硬件掩码。OMR、DORAM、SSE 与位置关联保护则按各自元数据/访问模式模型标记，不能因使用格技术就归为 PQC 实现侧信道。

本轮读取三份官方勘误的说明文字：[LPG](https://www.usenix.org/sites/default/files/sec26-errata_shi-quan.pdf)与[格 NIKE](https://www.usenix.org/system/files/sec26-errata_li-ying.pdf)只修订通讯作者脚注；[SING](https://www.usenix.org/sites/default/files/sec26-errata_blueml.pdf)修订 E2 训练中混入比较基准后的结果。后者重新排除相应电路并训练，后续比较应查修订表图；本轮未转录这些图表的具体数字。

## 保留的缺口

该年尚有 286 篇摘要未读。已读条目的全文、版本、材料与前后向引用也没有整体关闭。深度学习物理侧信道 SoK 已下载正文，但本批卡片仍仅按摘要阅读，不能把自动抽取片段冒充全文审读。五条新增 PQC 引用发现、其他会议年度目录和全部扩展来源仍需继续。

[本批来源与哈希](../provenance/usenix2026-candidates-20261113.json) · [目录核对来源](../provenance/usenix2026-print-toc-crosscheck-20261113.json) · [引用选读](../citations/usenix2026-pqc-selected-reference-screen.jsonl) · [总体覆盖](../COVERAGE.md)
