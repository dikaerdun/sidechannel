# 跨层八方向审计脚本（EXP-20261111-10）

输入只读，路径由 `PQC_ROOT` 指定（默认本机绝对路径）。全部脚本 `from common import ...`，需在本目录执行：

```
PQC_ROOT=/path/to/pqc-20261107-local python3 period_adjudicate.py
PQC_ROOT=... python3 b01_code.py
...
```

- `period_adjudicate.py` 周期裁决：包络模板 + 副本间互相关测间距，不预设格点。
- `b01_code.py` 三位码：码字分布、熵、分半波形译码 BER、命中格大小。
- `b04_path.py` 乘积高字与修正乘子的增量 R²（4 个读数、置换 null）。
- `b06_params.py` 对齐位移与幅度增益的增量 R²。
- `b07_position.py` 副本位置效应：开发选点、留出评估、交互检验。
- `b08_ident.py` 尺度对称群、中心化子、HW 别名类与锚点破除。

结果 JSON 见 `results/crosslayer-2026-11-11/`。
