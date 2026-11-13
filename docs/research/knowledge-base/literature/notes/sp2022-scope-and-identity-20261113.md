# S&P 2022 的范围判定与书目对应

阅读日期：2026-11-13。147 条录用目录标题全部初筛；49 个候选/不确定项读过原始摘要，29 条纳入通用侧信道研究，20 条保留为相邻背景。另 98 条没有摘要判定，标题层判断可以修订。两项后量子协议论文没有因标题含 PQC 自动纳入侧信道卡片。

## 目录对应与元数据差异

[录用目录](https://www.ieee-security.org/TC/SP2022/program-papers.html)与独立取得的 [IEEE 印刷论文集目录](https://www.proceedings.com/content/064/064986webtoc.pdf)均对应 147 条：140 条规范化题名相同，7 条改题名经作者列表与页码对应。没有 N/A。146 条可用 Crossref 起始页与印刷目录相同；MSR Templating 的 Crossref 页码字段缺失，印刷目录仅确认起始页 1474，未补造结束页。

七处题名差异涉及 Mobile Gambling Scams、Wireless Coexistence 的长副标题、Production Federated Learning、Blacksmith、PCR-Auth、Private Approximate Nearest Neighbor Search、Sexual Abuse。录用题名继续保留，正式题名作为别名及印刷题名字段。147 条稳定标题身份升级为 DOI，旧 ID 与已有引用中的对应关系保留。

Crossref 广义容器查询返回 1000 条结果中的精确 DOI 前缀子集：154 条，其中 147 篇论文与 7 条前言/索引。此查询本身不证明完整性；目录成员的证据来自逐项印刷目录对应。前言/索引单独留档。

六组作者差异经指定印刷页复核：Xiaojing Liaoy、Jun Zengy、Yinqian Zhangyz 的尾部字符据印刷目录更正，同时保存未调和的出版商名字；FSAFlow 的八作者版本与 Transfer Attacks 的十作者版本采用出版元数据并保留录用列表；Wöhler/Woehler 及 Alex Liu/Alex X. Liu 的名字形式差异保留。印刷页不是完整论文作者修订历史，不能据此解释变动原因。

提取方法仅适用于冻结 PDF 的 OpenSans 字形映射。已视觉校准的页面与哈希见[目录来源](../provenance/sp2022-print-toc-crosscheck-20261113.json)，可用[提取审计脚本](../tools/audit_sp2022_print_toc.py)复核。它检验冻结文本提取，不能替代第二位读者或主题完整性审查。

## 不能仅按关键词分类的例子

| 条目 | 本批处理 | 理由与边界 |
|---|---|---|
| DeepSteal、SpecHammer | 纳入 | 明确把 Rowhammer 故障与信息泄漏结合；不是只有位翻转破坏 |
| Blacksmith、ProTRR | 相邻 | 当前摘要主要为 Rowhammer 攻击/缓解，没有额外秘密观察关系 |
| Wireless Coexistence | 纳入并补读正文 | 共存协议暴露按键事件时序；另有直接内存读写/权限升级，分开记录 |
| CryptoMPK、vSGX、SMILE | 相邻 | 内存权限、虚拟化或授权诊断不自动构成侧信道保证 |
| Noise、TDI、Secret-Free | 纳入 | 摘要明确涉及侧信道或推测读取保护；保证仍限各自模型 |
| DeepCoFFEA、Surakav | 纳入 | 明确研究加密流量元数据与用户关联/访问网站之间的泄漏 |
| ABCC | 相邻 | 应用协议中的有意隐蔽通信形式化，不是非预期实现泄漏 |
| Noise-SDR | 纳入 | 普通软件对设备 EM 发射的调制原语，单列为有意物理通道 |
| ATR、Invisible Finger、WIGHT | 相邻 | 防拆检测或主动信号注入；未从当前摘要确认秘密值推断 |

## Wireless Coexistence 的实际阅读边界

[作者稿](https://arxiv.org/pdf/2112.05719)第 4 页 §III.B 描述共存协议中的时序、优先级与活动元数据；第 9 页 §V.D.5 描述控制 Wi-Fi 核后观察 Bluetooth 键盘包时序与类型。实验将协议记录与主机上的真值对齐，用于核对事件时间。

纳入依据是跨芯片的元数据观察。所读段落展示的是按键活动/时间，不是完成键值或密码恢复；主机真值也不能算攻击者自然拥有的信息。文章另外讨论的直接内存读写不与这条侧信道混称。未全面审查其余攻击、补丁现状或完整参考文献。

BLE 跟踪论文的 IEEE staging 页面重复返回 502，改读 [UCSD 作者 PDF](https://wcsng.ucsd.edu/files/sp22_paper.pdf)第 1 页摘要及引言开头；芯片、温度、功率和接收设备造成的可靠性限制保留。未据作者项目页的示意比例推成所有设备可唯一跟踪。

## 接续缺口

其余 98 条摘要仍需复核。IronMask、Noise、Cats vs. Spectre 与相关防护需要核对完整观察模型及证明条件；Augury 不能继承后来 GoFetch 的恢复能力。新的 29 条卡片均未独立复现，前后向引用仍待系统追踪。来源、身份与阅读范围见[本批来源](../provenance/sp2022-candidates-20261113.json)。
