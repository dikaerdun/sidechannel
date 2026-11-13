# S&P 2025 中的保护范围与功耗转时间通道

更新：2026-11-13。这是两篇论文的局部正文阅读记录，以及第三篇作者报告的摘要定位。只记录指定证据范围，不含本地实验。

## OpenTitan 的掩码 KMAC 与完整方案掩码

[Towards ML-KEM & ML-DSA on OpenTitan](https://doi.org/10.1109/SP61157.2025.00220) 的作者版本中，§2.4.2 采用一阶掩码 KMAC 的性能设置；§4 讨论接口扩展及既有保护；§5.2.5 则讨论如何支持未来的掩码方案，§8 再次将完整 ML-KEM/ML-DSA 掩码及扩展适当性重评估列为后续工作。因此，保留掩码哈希模块和 OTBN 原有保护，不能写成已完成完整方案的高阶保护。[作者 PDF](https://cryptojedi.org/papers/otpqc-20250514.pdf)

正文建议把不同值的份额放入向量寄存器，并引用 Share-slicing: Friend or foe?。这是一条需要继续追踪的实现假设，不能只因算法变量不同，就跳过实际资源、历史转换与模拟耦合的核查。该基础引用已登记；本次尚未读取被引论文。

作者的[代码仓库 README](https://github.com/PQC-OpenTitan/towards-ml-kem-and-ml-dsa-on-opentitan)列出四个子模块、ISA/模拟器修改、性能数据库与测试入口。README 明确区分 Python/Verilator、FPGA 和 ASIC 综合，并说明较大设计的 CW340 与构建限制。这里核实了说明文件中的这些入口，没有下载数据库或验证子模块完整性，也没有构建。README 中的正式书目用于补全 DOI，原官方目录身份保留为 alias。

实际阅读范围：作者 PDF 第 1 页摘要；第 2、4、6、8、11、14–15 页与保护、实现范围和后续工作相关的段落；第 17 页选定引用。没有将整篇标为已精读。此文在本库作为带具体保护设计讨论的实现研究纳入；一般只谈性能的 PQC 论文继续留在相邻层。

## Scheduled Disclosure 的观测通道和比较条件

[Scheduled Disclosure](https://www.hertzbleed.com/scheduled-disclosure-sp2025.pdf) 研究功耗如何经 Thread Director 提示和 Windows 调度行为转为时间差，说明固定频率本身未必切断全部功耗转时间路径。§6.1 的密码测试对象为 SIKE-751，不能记作 Kyber 或 ML-KEM；§6.2 的另一对象是浏览器跨源像素。

§6.1 的条件包括固定密钥、选择密文、同网远程计时与并发请求负载。正文比较默认设置和受限 P-state 设置，分别报告约 7 小时与约 38 小时的完整恢复；摘要所称约五倍收益使用了旧平台 Hertzbleed 结果作参照。这是跨平台个案比较，不能作为通用攻击效率排名。计时观测也不是一条独立物理功耗迹线。论文把已弃用的 SIKE 用作通道比较对象，结论是实现与系统通道，不能外推为现行 PQC 标准被恢复。

[作者仓库 README](https://github.com/cmu-msrg/scheduled-disclosure)说明其源码针对 Intel Core Ultra 7 155H 与 Windows 11 24H2 调整，其他平台需改配置。README 也说明两个攻击演示沿用了并修改既有项目；不能据“有仓库”认定全部演示一键复现。本轮只读 README，未检查每个文件或执行代码。

实际阅读范围：PDF 第 1 页、§6 所在第 14–15 页及第 17–18 页完整参考文献条目。79 条引用中，12 条已对应现有目录；3 条新发现待确认身份和范围，16 条基础文献待处理，48 条暂列背景或实现材料。以上只是第一轮条目判定，尚无前后向引用闭包。

## EUCLEAK 的版本与物理访问边界

S&P 2025 官方目录使用简称 EUCLEAK。本轮读取的是 Thomas Roche 的[2024-10-22 作者技术报告](https://ninjalab.io/wp-content/uploads/2024/10/20241022_eucleak.pdf)封面、修订表和摘要。它报告非恒时模逆相关的 ECDSA 电磁泄漏；需要物理访问与相应仪器。作者报告的器件、固件和时间范围不能升级为当前所有产品均受影响，亦不把少量正式采集与全部逆向、剖析成本合并。2024 报告与 2025 会议版的全文差异未核对。

## 可继续补读的具体问题

- OpenTitan：阅读 Share-slicing 原文，核对寄存器打包建议的证明或实验前提；审查完整方案掩码为何仍为后续工作。
- Scheduled Disclosure：补读功率约束、系统配置和统计稳定性，核对新发现的 ASIACCS、DIMVA、ASPLOS 论文，并继续前向搜索。
- EUCLEAK：取得正式会议版，核查报告版本变化、采集/剖析预算与真实产品覆盖。

全文快照与来源哈希记录在[本批 provenance](../provenance/sp2025-scope-followup-20261113.json)。公开仓库只收原创笔记和书目关系，PDF 与完整摘要留在本地缓存。
