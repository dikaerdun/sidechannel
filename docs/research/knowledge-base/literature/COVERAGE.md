# 目录覆盖与未完成工作

更新：2026-11-12。目录记录数不是相关论文数，也不是版本去重后的论文数。
“已提取”只说明已从指定来源解析记录；独立目录核对、逐条主题筛查、全文阅读和引用追踪另行判定。

| 会议/卷 | 年份 | 已提取记录 | 交叉核对 | 标题初筛 | 摘要及以上判定 | 来源与数量证据 |
|---|---:|---:|---|---|---|---|
| TCHES | 2021 | 78 | 待核对 | 78/78 | 3/78 | [记录](provenance/tches.json) |
| TCHES | 2022 | 83 | 待核对 | 83/83 | 8/83 | [记录](provenance/tches.json) |
| TCHES | 2023 | 78 | 待核对 | 78/78 | 4/78 | [记录](provenance/tches.json) |
| TCHES | 2024 | 101 | 待核对 | 101/101 | 8/101 | [记录](provenance/tches.json) |
| TCHES | 2025 | 111 | 待核对 | 111/111 | 6/111 | [记录](provenance/tches.json) |
| TCHES | 2026 | 148 | 待核对 | 148/148 | 20/148 | [记录](provenance/tches.json) |
| SP | 2021 | 115 | 待核对 | 0/115 | 0/115 | [记录](provenance/sp-2021.json) |
| SP | 2022 | 147 | 待核对 | 0/147 | 0/147 | [记录](provenance/sp-2022.json) |
| SP | 2023 | 196 | 待核对 | 0/196 | 1/196 | [记录](provenance/sp-2023.json) |
| SP | 2024 | 261 | 待核对 | 0/261 | 0/261 | [记录](provenance/sp-2024.json) |
| SP | 2025 | 255 | 待核对 | 0/255 | 0/255 | [记录](provenance/sp-2025.json) |
| SP | 2026 | 254 | 待核对 | 0/254 | 0/254 | [记录](provenance/sp-2026.json) |
| USENIX | 2021 | 246 | 待核对 | 0/246 | 0/246 | [记录](provenance/usenix-2021.json) |
| USENIX | 2022 | 256 | 待核对 | 0/256 | 1/256 | [记录](provenance/usenix-2022.json) |
| USENIX | 2023 | 422 | 待核对 | 0/422 | 0/422 | [记录](provenance/usenix-2023.json) |
| USENIX | 2024 | 417 | 待核对 | 0/417 | 1/417 | [记录](provenance/usenix-2024.json) |
| USENIX | 2025 | 438 | 待核对 | 0/438 | 1/438 | [记录](provenance/usenix-2025.json) |
| USENIX | 2026 | 363 | 待核对 | 0/363 | 1/363 | [记录](provenance/usenix-2026.json) |
| CCS | 2021 | 196 | 待核对 | 0/196 | 0/196 | [记录](provenance/ccs-2021.json) |
| CCS | 2022 | 218 | 待核对 | 0/218 | 0/218 | [记录](provenance/ccs-2022.json) |
| CCS | 2023 | 234 | 待核对 | 0/234 | 0/234 | [记录](provenance/ccs-2023.json) |
| CCS | 2024 | 328 | 待核对 | 0/328 | 0/328 | [记录](provenance/ccs-2024.json) |
| CCS | 2025 | 316 | 待核对 | 0/316 | 0/316 | [记录](provenance/ccs-2025.json) |
| CCS | 2026 | 483 | 待核对 | 0/483 | 0/483 | [记录](provenance/ccs-2026.json) |
| NDSS | 2021 | 90 | 待核对 | 0/90 | 0/90 | [记录](provenance/ndss-2021.json) |
| NDSS | 2022 | 85 | 待核对 | 0/85 | 0/85 | [记录](provenance/ndss-2022.json) |
| NDSS | 2023 | 94 | 待核对 | 0/94 | 0/94 | [记录](provenance/ndss-2023.json) |
| NDSS | 2024 | 140 | 待核对 | 0/140 | 0/140 | [记录](provenance/ndss-2024.json) |
| NDSS | 2025 | 211 | 待核对 | 0/211 | 0/211 | [记录](provenance/ndss-2025.json) |
| NDSS | 2026 | 265 | 待核对 | 0/265 | 0/265 | [记录](provenance/ndss-2026.json) |

## 当前已知缺口

- 全部核心目录仍需与独立出版目录/正式论文集核对；同一个来源的 JSON 与 HTML 不算独立证据。
- IEEE S&P 2026 页面标题与目录年度为 2026，但有一个 cycle 小标题写 2025，保留为需复核的页面不一致。
- IEEE S&P 2023 主列表漏列 DVFS Frequently Leaks Secrets；GoFetch 引用与另一官方日程促成补录。两份官方页面的对照不替代独立论文集全量审计。
- CCS 2026 为截至截点的官方录用目录；会议尚未举行，不能统一标为已正式发表。
- Crossref 的 ISBN 查询只返回 CCS 论文集容器，不能用于证明其中没有论文；已改用官方网站目录。
- TCHES 按卷年与出版日期分别处理，回看 2020 年元数据以补齐 2021 卷首期。Crossref 未提交引用列表不等于没有引用。
- TCHES 已逐题初筛完整标题及可用副标题；标题暂判不是最终纳入/排除。卷首前言另存于 catalog-exclusions/tches.jsonl。
- 摘要占位文本 Not Available 不计为可读摘要；标题层的相邻/范围外条目仍可被后续摘要或引用证据修订。
- CRYPTO/EUROCRYPT/ASIACRYPT、PQCrypto、COSADE、HOST 等扩展来源仍待系统补齐；引用扩展取得少量条目不等于补齐会议年度目录。
- 标题/摘要筛查、正式条目、版本归并与前后向引用追踪尚未完成。
- 当前统计只针对已收集目录；未取得的目录、没有摘要的条目和日期不明记录均不视为完成。
