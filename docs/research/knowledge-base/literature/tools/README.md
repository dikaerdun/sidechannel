# 文献目录工具

依赖 Python 3、requests、lxml。工具只收集书目与生成阅读索引，不运行侧信道实验。

从仓库根目录运行，将完整页面/摘要缓存放在仓库之外：

```sh
python3 docs/research/knowledge-base/literature/tools/harvest_catalogs.py --cache <outside-repository-cache>
python3 docs/research/knowledge-base/literature/tools/build_indexes.py --cache <outside-repository-cache>
```

可用 `--venues TCHES CCS USENIX NDSS SP` 和 `--years 2021 2022 2023 2024 2025 2026` 选择收集任务。TCHES 为跨卷统一查询，单独按 DOI 卷年归档；其时间回看包含 2020 年，避免遗漏 2021 卷首期。

`harvest_catalogs.py` 保留全部目录条目与来源数量，并拒绝把零解析结果当作成功。CCS 2023/2025 使用官方网站页面脚本公开引用的 XML/JSON 数据；不会访问投稿系统或非公开资料。Crossref ISBN-only 查询只得到论文集容器，已明确不作为 CCS 论文目录。

`build_indexes.py` 生成关键词优先级、覆盖表、候选队列、阅读卡片、相邻主题记录、标题筛查表与引用进度表。它读取已有的 `screening/decisions.jsonl`、`screening/title-decisions.jsonl`、`papers.jsonl` 和 `citations/`，不会自动作出纳入/排除判定。关键词不命中的记录仍为待筛查。原始摘要仅用于本地排队，不整批上传；`Not Available` 等占位文字不计作摘要。

2026-11-13 更新：发现记录区分待处理与已解析，已解析记录继续保留；引用表显示实际被引预印本及相邻主题阅读状态。覆盖表同时保留目录截点与实际阅读更新日期。校验器检查解析状态、目录身份、范围判定和引用边一致，仍不判断引用闭包是否完整。

2026-11-13 接续：标题记录已覆盖 TCHES 六卷与 S&P 2025；校验器按实际登记的会议年单元核对整批身份，不再假定标题记录全部属于 TCHES。多个引用初筛文件以“起点论文 + 引用号”关联发现与引用边，避免不同论文的相同编号相互混淆。GoFetch 98 条和 Scheduled Disclosure 79 条是完整条目初筛；OpenTitan 目前仅选读一条，Peek-a-Walk 仅选读两条。

S&P 2025 印刷目录另有只读复查工具，需要额外安装 PyMuPDF。先从 [provenance](../provenance/sp2025-print-toc-crosscheck-20261113.json) 所列 URL 将 PDF 保存到仓库外，然后运行：

```sh
python3 docs/research/knowledge-base/literature/tools/audit_sp2025_print_toc.py --pdf <outside-repository-pdf>
```

它先核对来源 SHA-256，再按该 PDF 的字形布局提取题名及页码，逐行比较 255 条已保存目录；不接受已变化的来源。`validate_library.py` 再核对目录到当前身份的双向对应、改题名及 N/A 例外。只证明目录成员对应，不证明那条 N/A 记录最终正式发表，也不代替摘要筛查。生成器把核心会议的窗口外卷年（如 TCHES 2020 基础论文）列入引用扩展，避免漏计或混入核心 30 单元。

正式条目在 `papers.jsonl`；摘要卡片是人工构思并经来源阅读后写入的整理，不由关键词推导。引用队列中的 pending 不表示关系已经核实。当前没有对目录覆盖或实验结论作自动完成判定。

缓存命中时核对原始内容 SHA-256。网站布局变化、年份不一致、分页变化、重复记录及访问失败应留下缺口并人工处理。协议中的独立目录核对和全文阅读不会因脚本成功而自动完成。

2026-11-12 修正：保留 Crossref 主标题与副标题，合并为可读标题；TCHES 卷首前言单列排除。S&P 2023 以另一官方日程补入主列表遗漏的 DVFS 论文，两个页面的差异留在 provenance。引用扩展条目放在 `catalogs/citation-expansion.jsonl`，不是完整会议目录；扩展来源与核心 30 单元分开计数。

重建后运行 `python3 docs/research/knowledge-base/literature/tools/validate_library.py`，检查身份、阅读状态、覆盖数量、引用编号、来源和链接。此检查仅验证产物一致性，不确认论文结论、独立复现、新颖性或文献无遗漏。
