# 引用发现解析与 S&P 2025 论文集目录核对

日期：2026-11-13。本批推进统一文献库，不运行攻击、采集、训练或仿真。

## 已完成的增量

- 解析 Scheduled Disclosure 的 Red Alert、The Finger in the Power、Controlled Preemption 三条引用，以及 OpenTitan 的 Share-slicing 引用。四篇进入同一阅读库；Red Alert 标为 2021 窗口前边界，Share-slicing 标为 2019 发表的基础文献。
- 补读 S&P 2025 八篇候选：Peek-a-Walk、SLAP、Breaking the Barrier、Ceviche、CipherSteal、Slice+Slice Baby、TikTag、Training Solo。Peek-a-Walk 的标题没有 PQC 名称，正文却包含参考 Dilithium-2 的恢复案例。
- 新增 12 张卡片，其中 3 张为指定全文章节阅读、9 张为摘要及元数据阅读。新增 6 条核实引用边；13 条已登记发现均完成身份与范围解析，但引用队列仍未闭合。
- 核查两个作者仓库的 README。Peek-a-Walk 说明仍有材料移植/TODO，Share-slicing 明确区分补充设置与论文设置；Finger in the Power 的链接仓库 API 返回 404，代码和数据可取得性未确认。
- SLAP、CipherSteal 升级为经 Crossref 核实的 DOI 身份，保留原官方目录 ID。

## S&P 2025 的独立目录核对

另从 Curran 取得 IEEE 论文集的印刷目录表示，核查封面、版权页及全部目录条目：IEEE 编号 CFP25020-POD，印刷 ISBN 979-8-3315-2237-7，在线 ISBN 979-8-3315-2236-0。它是独立于录用网页取得的出版目录副本，不是另一次同行评审。

255 条目录记录双向一一对应：254 条规范化题名一致；原录用题名 `Attitudes towards Client-Side Scanning in the USA and from the view-point of IT security experts` 在印刷目录中改为 `“Not the Right Question?” A Study on Attitudes Toward Client-Side Scanning with Security and Privacy Researchers and a U.S. Population Sample`，四位作者和主题一致，分别保留两个题名。

`(Blind) Users Really Do Heed Aural Telephone Scam Warnings` 的页码标为 N/A。它确实出现在目录，但最终出版状态还需查证；不据此推断撤稿或删除条目。对应证据见[逐条清单](../literature/toc-crosschecks/sp-2025.jsonl)及[来源与方法](../literature/provenance/sp2025-print-toc-crosscheck-20261113.json)。

目录抽取遇到两条题名和页码处于同一 PDF 文本段的情况，已修正解析并重新进行双向集合检查。此次核对仅证明所取得两份目录的条目对应，不能证明摘要筛查或论文阅读完成。

## 当前规模与后续工作

统一目录 6647 条，包含 6629 条核心会议年记录和 18 条引用扩展/基础记录。它们覆盖全部主题，不是 6647 篇侧信道论文。标题初筛仍为 854 条；摘要及以上判定 165 条，其中纳入 130 篇、相邻主题 35 条。纳入记录有 101 篇 PQC 相关、29 篇通用侧信道；作者报告与本地复现分开。

S&P 2025 已读 11/255 条，剩余 244 条尚无摘要判定；其他年份/会议仍需逐题筛查。TCHES 冻结 PQC 候选列表尚余 86 条待判定。其余 29 个核心会议年单元仍待独立目录核对，扩展会议系统目录、全文专题和代码/数据核查也未完成。

下一步优先处理 S&P 2025 剩余候选与不确定项，推进 TCHES 剩余摘要，补查上述 N/A 记录及不可访问的数据仓库，并继续引用追踪。GoFetch 还有 58 条基础引用待处理，Scheduled Disclosure 另有 16 条；本批没有把“已登记发现为零”写成没有遗漏。

验证包括 JSON/身份/计数一致性、255 条目录双向对应、阅读来源、引用关系与相对链接。脚本通过仅证明产物一致性，不构成文献普查完成、独立科学核验或实验复现。
