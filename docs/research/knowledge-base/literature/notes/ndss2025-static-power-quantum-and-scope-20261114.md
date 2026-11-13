# NDSS 2025 静态功耗 量子硬件与范围核查

阅读日期：2026-11-14。本批逐题读取官方录用目录的 211 个标题，读取 71 篇完整官方摘要，新增 27 张通用研究卡片与 44 条相邻判定。余下 140 篇摘要仍待阅读；没有据标题最终排除。官方录用页的 211 条尚未与独立出版目录完成成员核对。

标题初筛为 20 条 candidate、51 条 uncertain、140 条 outside_title_scope。摘要阅读后，七条标题不确定项也进入正式卡片，包括 CHAOS、IoT 设备识别评估、Iris、LAMP、LeakLess、ReDAN 和 Wallbleed。这说明关键词或显式的 side-channel 标题不能替代逐条阅读。

## 静态防护需要区分实测与推测

[On Borrowed Time](https://www.ndss-symposium.org/ndss-paper/on-borrowed-time-preventing-static-side-channel-analysis/)限制敏感中间态的驻留时间。本文阅读正式 PDF 第 6、9、14 页，以及第 15–16 页的八条指定引用；第 9 页图示与方案比较表已渲染核对。

- 第 6 页的目标是攻击者拥有物理访问、了解实现，并利用自然门控或外部控制使时钟停止。**根密钥存储假设安全**；被清理的是暂存敏感中间态，不能解读为直接密钥存储读出的通用防护。
- 第 9 页的异步方案检测停钟后选择随机输入，再提供清理时钟边沿。表 I 将 PLL 方案列为不兼容门控，异步方案兼容门控但设计成本更高。不能将两种配置的优点合成一套实现。
- 第 14 页报告已测试的静态功耗 CPA 在一百万迹线下未恢复子密钥。该结果不证明任意测量预算下安全。
- 同页明确说**没有进行 LLSI 或阻抗分析的防护实测**。对两者有效属于作者预期，正常运行周期内的扫描能力仍待调查。
- 误触发会中止正在进行的计算；功率门控 ASIC、数据保持模式及侵入式电路编辑仍有范围限制。

这篇论文与知识库的清理轨迹、驻留时间和物理遗忘方向直接相关，但不能用它确认我们尚未验证的机制。

## Android 传感器论文展示的是部分候选排名降低

[Power-Related Side-Channel Attacks using the Android Sensor Framework](https://www.ndss-symposium.org/ndss-paper/power-related-side-channel-attacks-using-the-android-sensor-framework/)将传感器寄生响应作为功耗代理。正文第 12–13 页已读，第 13 页表格与排名曲线已渲染核对。

AES 案例是 Pixel 6a 上的本地应用，需在前台或作为前台服务采集传感器，并能触发已知明文的加密。传感器每个采集窗口内重复加密相同明文；因此一个测量样本不等于一次 AES 调用。

作者先采集约 35.6M 样本、历时 44 小时，再使用过滤后的 17.8M 样本分析；排名图横轴仅展示至 300K 样本。正文指出若干字节有下降趋势，另一些没有有意义的趋势。**这些预算和排名结果不能合写成“30 万次加密恢复完整 AES 密钥”。** 本地 AES、浏览器像素推断及不同浏览器传感器权限需要分开。

本轮未审完过滤规则、全部姿态校准和浏览器权限细节，未根据曲线新增精确读数，也未复现。

## 量子硬件串扰不是后量子算法密钥攻击

[Crosstalk-induced Side Channel Threats in Multi-Tenant NISQ Computers](https://www.ndss-symposium.org/ndss-paper/crosstalk-induced-side-channel-threats-in-multi-tenant-nisq-computers/)纳入 general_sca，标签为量子计算、串扰及电路分类，不能因出现 quantum 就纳入 PQC 密钥恢复。

第 6–7 页描述 IBM 量子硬件上的门检测：研究邻近 CNOT 活动怎样影响观察比特的零计数，且敏感程度随比特和连接变化。第 11–12 页另以 336 个基准电路及 16 种编译变体构建图分类数据；第 12 页明确先假定门检测无误，再人为加入门计数不确定性。

因此，硬件证明了候选物理通道；分类部分不能直接称为 336 类量子程序的端到端实机攻击。摘要最高 85.7% 与正文基准 85.6% 分开保存；其评估设置、分辨率描述和完整误差传递尚待核查。第 12 页已渲染，未把图中其他曲线数值扩展为新结论。

书目核对还发现官方录用列表把首位作者写成 Ruixuan Li (Choudhury)，正式 PDF 首页为 **Navnil Choudhury**。已按正式稿修正作者字段，并保留原录用字段；没有因为来源是官网就沿用错误。

## PQConnect 保留为实现背景并继续追引用

[PQConnect](https://www.ndss-symposium.org/ndss-paper/pqconnect-automated-post-quantum-end-to-end-tunnels/)的贡献是自动建立后量子隧道和握手分析，本批列为 adjacent。正式 PDF 第 16 页附录 A 说明 Python 主体调用 libmceliece、libntruprime、lib25519 与 libsodium，并承认高层语言的时序与安全擦除困难。**握手的 Tamarin 分析不等于这些实现问题已经解决。**

PDF 首页标注稿件日期 2024-12-04，单独保留，未当作上线或会议日期。

本批选读参考 13、20、42、63。第 13 条实际引用 ePrint 2024/1049；当前 [KyberSlash 作者页](https://eprint.iacr.org/2024/1049)明确标注为 TCHES 2025 的小修订版。引用边保留实际 2024 预印本标识，并新增一条明确版本关系；没有声称当前作者稿与被引的 2024 文件逐字相同。

其余三个线索分别是 SecDev 2017 的 FaCT、RWC 2024 高保证实现演示材料和 EuroS&P 2018 的编译器副作用论文，进入待查队列。RWC 材料保留为演示类型，不先当作独立会议研究论文。

## 摘要中的其他容易混淆之处

| 工作 | 已确认的范围 | 不能由当前阅读推出 |
|---|---|---|
| 缓存通道系统评估 | 九项性质、四种既有及三种新通道；含 AES、按键、KASLR 与功耗放大案例 | 通道容量等于密钥恢复速率，或各 CPU 的缓存条件相同 |
| CounterSEVeillance | 恶意管理程序通过中断与页故障单步获取指令级计数器 | 普通无权限应用同样能做到；论文当时的补丁状态等于当前状态 |
| GadgetMeter | 正式 PDF 摘要说既有工具报告的 471 个 gadget 被判为不可利用 | 官方网页缺词后的句子原意正确；或该判定对全部处理器成立 |
| Oreo | Linux 与 gem5 中的 ASLR 防护实现和评估 | 已在生产芯片上实测，或覆盖模拟电路泄漏 |
| VRecKey | 红外观察下字符与词的 top-3 成绩 | 相同数字的 top-1 恢复率 |
| CHAOS | 合作发送者利用信标顺序及 TSF 构造隐蔽通信 | 520 bit/s 是从不合作受害者恢复秘密的速率 |
| Wallbleed | 主漏洞是直接越界读取；第 10 页另给出循环地址顺序的进程辨认侧信道 | 所有直接内存披露都属于侧信道 |

Iris 和 LAMP 按查询路径、流量观察的明确隐私关系纳入；普通安全计算协议、纯故障、EMI 注入、成员推断及隔离架构按相邻主题保留，并逐项解释。功能正确、内存加密、可信执行和密码协议安全均不自动推出物理侧信道安全。

八份 PDF 首页的作者与 DOI 另已核对。Wallbleed 首页附 NDSS 程序委员会的研究伦理声明，明确接受论文不代表认可其所用方法；卡片保留此出版说明，本库没有独立裁定相关伦理或法律问题。

## 引用清单与后续缺口

[Borrowed Time 八条选读](../citations/borrowedtime2025-selected-reference-screen.jsonl)连入六条已有目录，新增时钟/电压检测器与小 Mersenne 素数掩码两条线索；没有筛完其余参考文献。[PQConnect 四条选读](../citations/pqconnect2025-selected-reference-screen.jsonl)连入 KyberSlash，另有三条待查。合计新增七条引用、一条明确版本关系、五条待查发现。

继续 NDSS 2025 的 140 篇未读摘要与独立目录成员核对；补 Borrowed Time 的清理实现、全部评估和剩余引用；补 Android 过滤及权限条件、NISQ 数据产生到实测门检测的衔接、GadgetMeter 主文判据，以及新引用的实际版本。其他年度和旧的 UOV/Falcon 缺口继续保留。

本批新增四张正文选读卡片；PQConnect 的相邻判定也附有正文阅读范围。其他卡片仍以摘要为主。来源 URL、抓取时间与 SHA256 见[本批 provenance](../provenance/ndss2025-candidates-20261114.json)，完整网页、摘要集合、PDF 和渲染图留在仓库外缓存。没有运行实验、作者代码、仿真或独立核验代理。
