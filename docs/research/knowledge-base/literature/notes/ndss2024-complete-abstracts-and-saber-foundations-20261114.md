# NDSS 2024 摘要补齐与 SABER 基础引用

核查日期：2026-11-14。冻结文献窗口仍为 2021-11-12 至 2026-11-12。八篇早期基础文献通过 SABER 引用纳入，不伪装为窗口内新成果。本批只有文献阅读、目录核对和记录整理；没有实验、仿真、训练或作者代码执行，也没有独立第二科学审读。

## 摘要筛查发现的遗漏

补读 NDSS 2024 剩余 82 篇完整官方摘要，新增一张通用卡片和 81 条相邻/背景判定。该年度现有 140/140 篇摘要判定：20 条纳入、120 条相邻主题。后者表示在已读范围下未归为本库的直接侧信道成果，不表示全部正文已读或永久排除。[逐篇阅读凭据](../screening/batches/ndss2024-remaining-20261114.jsonl)保存来源及摘要哈希，不复制摘要全文。

新增的 [MASTERKEY](https://www.ndss-symposium.org/wp-content/uploads/2024-188-paper.pdf)标题以大模型越狱为主，但正文包含响应时间推断防护流程，因此纳入计时侧信道。已读摘要及 PDF 第 1、4–6 页，并渲染核对第 6 页。表 III 用五个问题、四种请求长度和四个历史服务检验长度与时间关系；四个 Pearson 系数为 0.567、0.838、0.762、0.465，不能全部改写成同等强度的相关。图 3 区分猜测组件与已知组件，时序吻合不是服务内部结构的直接确认。整体越狱成功率与这部分计时证据分开，历史结果不外推当前服务。

[VETEOS](https://www.ndss-symposium.org/wp-content/uploads/2024-972-paper.pdf)保留为相邻主题。摘要及第 1、3–4 页表明，回滚判断使用显式余额或全局状态读取；这里的 timing 主要是执行中何时检查状态，并未建立耗时测量通道。它可作状态 oracle 与因果干预背景，但本批不把它写成计时侧信道成果。

同样，DEMASQ 的 energy/Doppler 类比、FreqFed 的权重频率、脉冲网络的 spike、Powers of Tau 的 power 均按实际变量判断；没有因词面相似就视为功耗研究。LoRDMA 虽使用 RTT 反馈，但已读摘要的目标是 DoS，不是秘密恢复。DeGPT、ChatAFL、SigmaDiff、密码 API 误用分析作为方法背景保留。

## 官方目录的独立对应

另取的 [官方日程](https://www.ndss-symposium.org/ndss-program/symposium-2024/)包含 140 个不同论文链接，与原目录一致。再从[论文集前置页](https://www.ndss-symposium.org/wp-content/uploads/2024/09/NDSS2024_Proceedings_Front_Matter.pdf)第 4–20 页独立提取题名，完成双向 140 条成员对应；138 条规范化题名相同，两条差异经渲染核对：

- `A Unified Symbolic Analysis of WireGuard` 在印刷目录中没有开头的 `A`；作者顺序也不同，按来源分别保留。
- `50 Shades of Support ... Security Updates` 在印刷目录中为单数 `Update`。

目录第 4 页有一个独立的 `Censorship` 残留标签；第 19 页把 Certificate Transparency 的题名排成斜体并与首位作者连写。后者经页面核对分离，前者不计为论文。这里没有论文起始页码，清单统一记 N/A，而非捏造页码。[逐项清单](../toc-crosschecks/ndss-2024.jsonl)与[来源、异常及哈希](../provenance/ndss2024-completion-saber-20261114.json)可复查。

## 八篇基础文献与修订关系

| SABER 引用 | 核实身份 | 本批阅读范围及关键限制 |
|---|---|---|
| Gou01 | [Goubin，CHES 2001](https://doi.org/10.1007/3-540-44709-1_2) | 完整原始摘要；B2A/A2B 转换的一阶防护语境，不代表所有实现的物理安全 |
| CT03 | [Coron–Tchulkine，CHES 2003](https://doi.org/10.1007/978-3-540-45238-6_8) | 完整原始摘要；后续正确性问题不能省略 |
| NP04 | [Neiße–Pulkus，CHES 2004](https://doi.org/10.1007/978-3-540-28632-5_17) | 完整原始摘要；表空间与 IDEA 模 2^k+1 乘法背景，不是 PQC 实测 |
| Deb12 | [Debraize，CHES 2012](https://doi.org/10.1007/978-3-642-33027-8_7) | 摘要及 PDF 第 1–2、10、14–15 页；没有独立复算证明与算法 |
| HT19 | [Hutter–Tunstall，JCEN](https://doi.org/10.1007/s13389-018-0191-z) | 出版商和 ePrint 完整摘要；固定阶数下恒时，复杂度随阶数增长 |
| KRR+18 | [Constant-Time Discrete Gaussian Sampling](https://doi.org/10.1109/tc.2018.2814587) | 机构接受稿封面、摘要及第 16–18 页；测试执行时间，不是功耗/EM |
| RRVV15 | [A Masked Ring-LWE Implementation](https://doi.org/10.1007/978-3-662-48324-4_34) | 摘要及第 13–16 页，第 16 页渲染核对；低噪声与强评估者假设 |
| RdCR+16 | [Additively Homomorphic Ring-LWE Masking](https://doi.org/10.1007/978-3-319-29360-8_15) | 完整原始摘要；PDF 请求返回订阅预览 HTML，正文仍未取得 |

**正确性修正与泄漏修正必须分开。** Debraize 2012 引言明确指出 Coron–Tchulkine 算法的正确性问题并提出修正；[TCHES 2021 后续分析](https://eprint.iacr.org/2021/067)又报告 Debraize 新方法中某中间变量的掩码不均匀，产生可检测 DPA 泄漏。后一来源本批重读完整摘要，尚未重新核算证明与实测。不能沿引用链逐次继承标题中的安全保证。

**恒时结论必须绑定保护变量。** [Gaussian 接受稿](https://pure-oai.bham.ac.uk/ws/files/74518268/Constant_time_Discrete.pdf)采用固定/随机输入种子分组、RDTSC、t 检验和 KS 检验，作者报告在指定配置下至六百万次位切片采样未检出依赖。文中也限定具体架构、编译器和平台。有限测试未拒绝零假设不能推出所有分布相同，更不能转换为功耗安全结论。

**Ring-LWE 评估包含特意有利于评估者的条件。** 2015 正文假设知道流水线等实现细节，猜测子密钥时知道其余密钥；关闭 PRNG 对照、已知掩码相关性与正常开启 PRNG 的分析分开。二阶分析成功与一阶指定分析未检出是不同层级的证据，不能借二阶结果证明已穷尽所有一阶攻击。2016 方案用随机消息加密生成掩码、允许常规译码器，是不同设计；正文缺失时不推断它适用于任意 KEM 或任意噪声条件。

## 版本、日期和接续

[Ring-LWE ePrint 2015/724](https://eprint.iacr.org/2015/724)明确标为 CHES 2015 的小修订，建立一条明确版本关系；出版页 First Online 为 2015-01-01，Crossref 则为 2015-09-01，冲突保留。Gaussian 机构接受稿封面明确列 DOI 和正式出处，建立作者稿关系；[机构页](https://research.birmingham.ac.uk/en/publications/constant-time-discrete-gaussian-sampling/)给出早期在线 2018-03-12，卷期为 2018 年 11 月，两者分别记录。

[B2A ePrint 2016/1023](https://eprint.iacr.org/2016/1023)与 JCEN 同题同作者，但页面没有明确指定期刊，关联仍标为推定。期刊在线 2018-05-23、卷期 2019；当前 ePrint 提到 t-NI 到 t-SNI 的修订，不能自动归于所有旧版。版本身份核实不表示全文完全相同。

SABER 44 个参考位置现为 22 条对应、0 条待查身份、22 条暂列背景。八个发现已解析；背景原文、各版本差异和递归/前向追踪仍开放。全库现有 574 张卡片、325 条引用、80 条版本关系（68 明确、12 推定）；133 条发现尚待解析。

下一步补 NDSS 2025 剩余 140 篇摘要与独立目录，再继续 NDSS 2026 的 185 篇；PQC 线继续取得 2016 Ring-LWE 正文、补掩码转换的证明/修订差异及 Gaussian 2022 剩余引用。本批为已有大胆提案补充证据条件，没有新增实验支持，也没有派发他人验证任务。
