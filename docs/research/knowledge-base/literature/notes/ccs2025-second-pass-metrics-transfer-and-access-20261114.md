# CCS 2025 第二轮阅读中的指标 迁移与观察条件

阅读日期：2026-11-14。目录截点仍为 2026-11-12。本批完成 13 篇 CCS 2025 原始摘要判定，纳入十篇、相邻三篇；沿引用补入一篇 CCS 2018 基础论文，共新增 11 张卡片。作者报告未独立复现，没有运行实验、仿真、训练或作者代码。

本轮覆盖 WiFi、光学、网络流量、加密搜索和访问隐藏等通用侧信道方向。新增条目均不是 PQC 专项；已有 PQC 阅读与引用队列继续保留。逐条层级见[阅读卡片](../PAPER_NOTES.md)，来源 URL、时间和 SHA-256 见[来源记录](../provenance/ccs2025-second-pass-20261114.json)。

## 三种不能扩大解释的成绩

**BFId。** 论文从 WiFi 波束成形反馈推断身份。收集涉及 197 人，但第 8 页给出的可用 CSI/BFI 分别为 170/161 人；181 人同意向研究者按请求共享，不等于整套数据无条件公开。第 11 页以视角 1 训练、其他视角测试时，准确率均低于 5%；相近视角之间有所改善。因此“在多个视角中取得高准确率”不等于“模型能跨任意视角迁移”。第 12 页明确 softmax 设置不能评估未见身份泛化。选读 PDF 第 1、8、11–12 页，其余附录未完整核查。[作者机构 PDF](https://publikationen.bibliothek.kit.edu/1000185756/168100988)

**HW-Spy。** 可见的是笔尾，目标是推断不可见笔尖对应的手写内容。第 8 页定义：字符级为字符正确比例；词级是在拼写校正后计算字符正确比例；句级是在拼写及语法校正后计算字符正确比例。后两者不是整词或整句全部正确的概率。第 12 页的未见书写者评估采用留一人设置，训练和测试会话也有区别；不能把个性化结果当作此设置。选读 PDF 第 1、8、12 页。[作者 PDF](https://rtcl.eecs.umich.edu/rtclweb/assets/publications/2025/ccs25-huang.pdf)

**Swallow。** 摘要的每网站五条标签样本用于微调；第 13 页另列 10,000/95,000 条预训练流量。全部受测网站指纹防护均从未防护轨迹模拟生成，真实部署留作未来工作；当前任务为一次访问一个网站主页，多标签页及站内网页另列开放问题。同页写 BYOL 训练开销更高，却给出每轮 79.51 秒、SimCLR 228.46 秒，文字方向与数字不一致；本库记录待查，不擅自更正文意。选读 PDF 第 1、13–14 页。[作者 PDF](https://raw.githubusercontent.com/wujinhe0814/Swallow/main/paper/Swallow.pdf)

[Swallow 作者 README](https://github.com/wujinhe0814/Swallow/blob/main/README.md)链接 [Zenodo 16607834](https://zenodo.org/records/16607834)，说明提供选定的闭集/开放世界场景，以及 D1–D5 的部分原始轨迹。这里只核对 README 声明，没有下载该存档或验收全部材料，不能据仓库存在便称完整复现条件齐备。

## 访问隐藏保证与实际恢复目标

[Differentially Private Access in Encrypted Search](https://www.research-collection.ethz.ch/server/api/core/bitstreams/f6e317c8-6025-4b80-859d-200a8ee12d9d/content)分析 DO-Range 和 epsilon-OPE-Range。ETH 文件有一页封面，本文所称 PDF 第 2、5–6、12 页分别对应摘要、定义/方案区别与恢复讨论。相邻数据库、只读 Find 和自适应性要求决定保证的对象，不能概括为 DP 定理失效。第 12 页的恢复受分区边界限制，作者明确区分分区级分布与分区内部个体精确值。两个实例的插入与 Find 隐私预算讨论也不能自动推广为所有 DP 系统。

[MegaBlocks](https://eprint.iacr.org/2025/1592)研究逻辑字小于物理块的非对称模型；其 O(log N / log log N) I/O 结论必须携带这一条件。摘要的加速比较依赖块大小与本地内存，作者也说明被比较方案原本未针对大块设计。ePrint 明示 CCS 2025 major revision 和正式 DOI；本批只读摘要与版本记录，不把它当作同一经典模型中推翻对数下界。

[Peekaboo](https://arxiv.org/abs/2509.03806)以间歇泄漏观察、辅助知识及其他泄漏推断 DSSE 查询。搜索模式聚类的 ARI 与查询正确率分别记录；“被动”不等于没有观察能力，而是与主动文件注入区分。[作者全文](https://arxiv.org/pdf/2509.03806)首页明确对应 CCS 2025 DOI。本批只读摘要及首页说明，观察预算、基线与其余正文待补。

## 各通道需要的观察条件

| 论文 | 本批核定的观察关系 | 不能省略的条件 |
|---|---|---|
| [PMTUD 与共享公网 IP](https://arxiv.org/abs/2509.11833) | 跨连接共享路径 MTU 状态用于 TCP 推断 | 与同公网 IP 下的恶意设备协作；不是任意远程无附加条件能力 |
| [3D 打印光学通道](https://arxiv.org/abs/2506.21897) | 喷头视频轨迹映射到打印指令 | 90.87% 对应作者的打印等价评价，非原始 G-code 逐字节恢复率 |
| [Styled to Steal](https://d-we.me/papers/stylemail_ccs25.pdf) | CSS 渲染条件把已解密字符映射到网络请求 | 恶意内容注入、打开渲染和网络行为；无 JavaScript 不等于无攻击输入 |
| [Time Tells All](https://arxiv.org/abs/2508.21440) | 账本确认时间与 RPC 轮询 TCP 时间相关 | 能观察网络边界/交换点的强被动对手；零交易费不等于零总成本 |

以上四篇仅读完整摘要及元数据，不能将论文时点的具体系统结论写成当前所有部署均受影响。光学论文页面给出扩展版说明及正式 DOI，建立显式版本边；PMTUD 和 Time Tells All 尚未取得明确正式版本声明，其题名与作者匹配不自动升级为已核实版本关系。

MOLE、RISCover 和 RMPocalypse 本批列入[相邻条目](../ADJACENT_NOTES.md)：摘要分别展示恶意 GPU 固件突破隔离、CPU 架构错误原语、RMP 初始化访问控制缺口。直接读取/修改受保护数据与从额外观察推断秘密是不同证据，不因出现 AES、GPU 或机密计算就自动纳入侧信道计数。

## Swallow 引用初筛及版本保留

[完整引用清单](../citations/swallow2025-reference-screen.jsonl)保留作者 PDF 第 14 页全部 37 个参考位置：十条目录对应、十五条待查、十一条暂列背景、一个重复位置。第 18、19 条作者、题名、年份和页码完全相同，只增加一条引用边。

该重复项促成补读 [Measuring Information Leakage in Website Fingerprinting Attacks and Defenses](https://experts.umn.edu/en/publications/measuring-information-leakage-in-website-fingerprinting-attacks-a/)，核定 CCS 2018 DOI 10.1145/3243734.3243832。本批只读机构完整摘要与正式元数据；作为五年窗口外度量基础保留，不声称复核了其估计器或实验。

第 3 条 Var-CNN 实际引用 arXiv 2018 版，第 13 条 RegulaTor 引用 arXiv 2020 版，第 26 条 Tik-Tok 引用 arXiv 2019 版。追踪时应先核定这些被引版本，再寻找正式版本关系，不能直接替换成后来出版版本。另待查包括早期 WF 防护、TrafficSliver、Triplet Fingerprinting、TIFS 应用识别与 PAM 数据增强。目录已有对应也不代表目标摘要已读完。

## 尚未解决的入口与接续

Co-Prime 和 GAPDiS 已补 Crossref 正式元数据，但出版页返回 HTTP 403；GAPDiS 的实现 README 不构成完整摘要，两篇均保持摘要未读。MOLE、RISCover、RMPocalypse 的 Crossref 小型大写标签引入了空格，保留作者/录用表拼写并记录原始字段，不记成实质改题名。

CCS 2025 现有 34 篇摘要判定，27 篇纳入、七篇相邻，仍有 282 篇摘要待复核。优先补 Co-Prime/GAPDiS 原始摘要、PMTUD/Time Tells All 正式版本说明，Swallow 指标文字差异及新登记引用；其余核心年份、扩展会议系统目录和 PQC 全文/前后向引用继续推进。本轮没有新增独立会议目录对应，也没有完成递归引用闭合。
