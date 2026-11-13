# CCS 2025 掩码 观察模型与防护边界

日期：2026-11-14。完成官方录用目录的 316 条标题初筛，以及 21 篇选定论文的摘要及以上判定：17 篇纳入，4 篇相邻。另加入 mUOV 的明确关联作者版本，并沿引用补读 TCHES 2024 PoMMES，共新增 19 条卡片。版本记录不等于独立研究数量。

## 目录身份与覆盖

官方录用 JSON 和另取的官方日程 JSON 各有 316 条唯一论文 DOI，集合完全一致。两者属于同一会议网站，可能共享上游数据，因此仅登记官方列表一致性，独立出版目录仍待取得。标题暂判为 27 个候选、63 个不确定、226 个标题层范围外；全部仍可被摘要证据修订，不能把未读的 295 篇摘要当作最终排除。

20 篇补入 Crossref 出版元数据：会议举办于 2025-10-13 至 17，所读记录的 print 为 2025-11-19，online 为 2025-11-22。三个日期分别保留。Correctness Bounds 的单篇 Crossref 请求返回 429，保留官方录用身份与作者论文来源，没有据此猜测出版页码。

SecSep 录用题名包含 “and a Hardware Extension”，出版元数据与作者 CCS 格式 PDF 的题名不含该短语；DOI 相同，保留录用别名。Heracles 的 Crossref 格式化文本插入空格，显示名按作者项目页规范化，原字段保留。这两项分别属于改题名和格式差异。

来源、失败状态与哈希见[本批溯源](../provenance/ccs2025-first-pass-20261114.json)。IOValve 的常规 HTTP 抓取遇到 TLS 错误，完整作者机构摘要改由网页工具读取；缓存明确标为工具提取文本，不冒充原始 HTTP 字节。

## mUOV 必须分开的四类证据

[mUOV 正式身份](https://doi.org/10.1145/3719027.3765188)由官方目录和出版商元数据确定；[作者 ePrint](https://eprint.iacr.org/2024/1875)明确声明 CCS 2025 minor revision，首次上传 2024-11-16，最后修订 2025-08-06。另选读 [NIST 托管的作者稿](https://csrc.nist.gov/csrc/media/events/2025/sixth-pqc-standardization-conference/muov%20masking%20the%20unbalanced%20oil%20and%20vinegar.pdf)。正式 ACM 页面返回 403，未确认两份全文或参考列表逐字一致。

| 证据 | 本轮读到的范围 | 不应写成 |
|---|---|---|
| 探针模型论证 | 任意阶算法和指定探针、组合假设下的论证 | 任意真实微架构、物理观察都安全 |
| 机械验证 | 部分组合的一阶、二阶 maskVerif 检查；第 15 页说明 NIo 工具限制阻止完整签名组合的机械验证 | 完整任意阶签名已由工具全部证明 |
| 物理检测 | Cortex-M4、缩小参数 m=4 与 n=10、一阶 TVLA；三个部件各 1M 条迹线，Gaussian elimination 为 100K | 标准参数完整签名的所有高阶泄漏已排除 |
| 性能 | UOV-Ip 与 UOV-III 的一至三阶软件周期比较，在 i7-6600 平台记录 | 与 Cortex-M4 泄漏测试是同一组硬件证据 |

作者用汇编清理处理份额依次占用资源时的重组合，并结合优化及禁用指令调度选项。这个实现条件不能从后续性能比较中删去。未跨阈值仅是该设置下的阴性检测结果；本文没有独立复算检测、证明或执行代码。

实际阅读：第 1 页，第 15–18 页，第 19–22 页讨论与完整参考列表，第 23 页 Appendix A；第 17 页的表和图另经渲染核查。其余证明和附录没有通读。

## ML Cube 的安全主张需要正文资格核查

[作者公开摘要](https://bianyiby.github.io/publications/)明确说 ML-Cube 面向 FIPS 203 ML-KEM 与 FIPS 204 ML-DSA，通过 Tensor Core 内部分析和寄存器内计算减少外部内存依赖，并声称缓解内存披露与缓存侧信道。

因此，本库将它纳入 PQC 实现及防护主张层，而不因题名主要谈加速就略过。但当前仅核对摘要和出版身份，尚未读到攻击实验、防护证明或完整威胁模型。memory-less 不能被改写为恒时、功耗安全或整个 GPU 上不存在其他观察。

## 非干扰与契约的观察范围

| 论文与原始来源 | 本轮可以记录 | 仍需保留的条件 |
|---|---|---|
| [SecSep 作者 PDF](https://people.csail.mit.edu/mengjia/data/2025.CCS.SecSep.pdf) | 汇编类型推断与秘密/公开栈分离；第 3 页给出软硬件两侧契约 | 假定恒时软件，并依赖满足相应非干扰条件的硬件；引用 ProSpeCT 的硬件机制，不是只重写软件就保护任意现有处理器 |
| [LeaSyn 作者 PDF](https://mguarnieri.github.io/publication/ccs2025/ccs2025.pdf) | 在模板内合成契约，以经验测试指导精确性、形式验证支持健全性 | 第 3 页的精确性相对于模板和已探索测试对；观察示例是指令退休周期，不是模拟功耗、电磁的全面保证 |
| [MileSan 作者论文](https://comsec-files.ethz.ch/papers/milesan_ccs25.pdf) | 比较架构与 RTL 污点流，并用 RandOS 搜索可观察的额外信息流 | 给定程序的判断、随机搜索的覆盖、整个处理器无漏洞是不同命题；本轮只读摘要及作者项目说明 |
| [BLACKOUT 作者版本](https://arxiv.org/abs/2504.14654) | CHERI blinded capabilities 与数据无关计算约束 | 具体异常行为和观察模型待正文；摘要不覆盖所有物理通道 |
| [BOLT 作者版本](https://arxiv.org/abs/2509.01742) | 隔离 HBM 的不可观察区域支持 OMAP 设计 | HBM 隔离和不可观察性是模型条件，不能由封装结构直接推广到功耗或电磁安全 |
| [IOValve 作者机构摘要](https://www.microsoft.com/en-us/research/publication/iovalve-leakage-free-i-o-sandbox-for-large-scale-untrusted-data-processing/) | 在独立网络设备上拦截并规整全部网络 I/O | “Leakage-Free” 需要连同指定 I/O 边界和隔离前提阅读 |

SecSep 与 LeaSyn 只选读第 1、3 页，其余证明和实验尚未完整审查。四篇相邻论文也分别保留理由：Correctness Bounds 的概率正确性、云秘密恢复、分布式 LLM 中间输出反演、Wanilla 静态非干扰，均不能单凭题名升级为侧信道保证或攻击。

## 观察权限与恢复对象

[ExfilState](https://fabianthomas.de/publications/2025/thomas2025exfilstate/)和 [GhostCache](https://www.thu-haslab.org/publication/2025-ghostcache/)说明限制计时器不等于消除缓存观察；它们利用不同的架构可见结果。缓存通道带宽、网站分类准确率与密码恢复预算仍需分开核对。

[Heracles](https://heracles-attack.github.io/)涉及恶意管理程序的页移动与确定性重加密观察；[WireTap](https://wiretap.fail/files/wiretap.pdf)则需要物理 DRAM 总线接触。WireTap 的摘要明确指出物理攻击不在 Intel 声明的 SGX 保护边界内，不能把结果描述成只靠远程软件就能完成。

[MoEcho](https://arxiv.org/abs/2508.15036)观察 MoE 路由留下的 CPU/GPU 硬件痕迹，纳入非密码目标侧信道。[Pixnapping 作者论文](https://www.pixnapping.com/pixnapping.pdf)涉及进入 Android 渲染流程的像素，显示的 2FA 码与从未显示的存储密钥不是同一恢复对象。[TEMPEST-LoRa](https://arxiv.org/abs/2506.21069)是主动调制的电磁隐蔽通信，发送控制条件不能从摘要摘除；最大距离与最大速率也不是同一工作点。

[DP 计时研究](https://zacharyratliff.org/files/dp-timing-attacks.pdf)将输出、执行时间与预处理一起审计；数据库大小是否公开、数据邻接定义及测量噪声影响结论。经验隐私损失下界不能代替安全上界。[补丁研究作者摘要](https://researchportal.hkust.edu.hk/en/publications/an-empirical-study-measuring-in-the-wild-cryptographic-microarchi/)则提示修复一个泄漏模型后可能留下另一个模型的泄漏，具体补丁及版本仍待正文。

## mUOV 引用初筛与接续

[52 条参考位置](../citations/muov2025-reference-screen.jsonl)均从 NIST 托管作者稿第 19–22 页读取，按出现顺序编号并保留原字母标签。11 条与现有目录对应、17 条进入发现队列、24 条暂列背景。正式 ACM 参考列表尚未对照；背景暂判不是最终排除，整份列表初筛也不是递归闭合。

引用促成补读 [PoMMES](https://doi.org/10.46586/tches.v2024.i3.342-376)：其作者摘要直接讨论微架构感知寄存器分配和 Cortex-M0+ 功耗评估。它此前在完整 TCHES 目录中，但还没有阅读卡片，现加入通用侧信道层。

优先解析 UOV 物理安全 SoK、任意阶 Gaussian elimination、Falcon floor masking、One Vector、maskVerif 和早期 UOV 侧信道研究；必须匹配实际被引版本。GLP 引用对应 2018 会议版，不能替成后来的期刊扩展。High-order Polynomial Comparison 的 2022 在线年与 2023 卷年、CARDIS 检测论文的会议年与上线年继续分别保留。

下一批继续 CCS 2025 其余候选与不确定项、独立出版目录，以及上述 17 条发现。其他年份与扩展会议的覆盖缺口仍在[覆盖表](../COVERAGE.md)，本轮没有完成“无遗漏”审计。
