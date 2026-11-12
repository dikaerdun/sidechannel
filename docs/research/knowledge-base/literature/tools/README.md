# 文献目录工具

依赖 Python 3、requests、lxml。工具只收集书目与生成阅读索引，不运行侧信道实验。

从仓库根目录运行，将完整页面/摘要缓存放在仓库之外：

```sh
python3 docs/research/knowledge-base/literature/tools/harvest_catalogs.py --cache <outside-repository-cache>
python3 docs/research/knowledge-base/literature/tools/build_indexes.py --cache <outside-repository-cache>
```

可用 `--venues TCHES CCS USENIX NDSS SP` 和 `--years 2021 2022 2023 2024 2025 2026` 选择收集任务。TCHES 为跨卷统一查询，单独按 DOI 卷年归档；其时间回看包含 2020 年，避免遗漏 2021 卷首期。

`harvest_catalogs.py` 保留全部目录条目与来源数量，并拒绝把零解析结果当作成功。CCS 2023/2025 使用官方网站页面脚本公开引用的 XML/JSON 数据；不会访问投稿系统或非公开资料。Crossref ISBN-only 查询只得到论文集容器，已明确不作为 CCS 论文目录。

`build_indexes.py` 只生成关键词优先级、覆盖表和候选队列。它读取已有的 `screening/decisions.jsonl`，不会自动作出纳入/排除判定。关键词不命中的记录仍为待筛查。原始摘要仅用于本地排队，不整批上传。

正式条目在 `papers.jsonl`；摘要卡片是人工构思并经来源阅读后写入的整理，不由关键词推导。引用队列中的 pending 不表示关系已经核实。当前没有对目录覆盖或实验结论作自动完成判定。

缓存命中时核对原始内容 SHA-256。网站布局变化、年份不一致、分页变化、重复记录及访问失败应留下缺口并人工处理。协议中的独立目录核对和全文阅读不会因脚本成功而自动完成。
