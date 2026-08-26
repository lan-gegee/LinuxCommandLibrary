# TAGLINE

测量命令执行时间的命令行基准测试工具

# TLDR

**对一条命令进行基准测试**

```hyperfine '[sleep 0.3]'```

**比较多条命令**

```hyperfine '[command1]' '[command2]' '[command3]'```

在计时前**运行预热迭代**

```hyperfine --warmup [3] '[command]'```

**设置最小运行次数**

```hyperfine --min-runs [20] '[command]'```

每次基准测试前**运行准备命令**

```hyperfine --prepare '[make clean]' '[make]'```

将结果**导出为 JSON**

```hyperfine '[command]' --export-json [results.json]```

以参数范围进行基准测试

```hyperfine -P threads 1 8 '[./program --threads {threads}]'```

忽略命令失败

```hyperfine --ignore-failure '[command]'```

# SYNOPSIS

**hyperfine** [_options_] _command_ [_command ..._]

# PARAMETERS

**-w**, **--warmup** _n_
> 计时前运行 n 次预热迭代。

**-m**, **--min-runs** _n_
> 最小运行次数（默认：10）。

**-M**, **--max-runs** _n_
> 最大运行次数。

**-r**, **--runs** _n_
> 精确的运行次数。

**-p**, **--prepare** _cmd_
> 每次计时运行前执行的命令。

**-c**, **--cleanup** _cmd_
> 每次计时运行后执行的命令。

**-s**, **--setup** _cmd_
> 所有基准测试开始前执行一次的命令。

**-P**, **--parameter-scan** _var start end_
> 对参数范围运行基准测试。

**-L**, **--parameter-list** _var_ _vals_
> 对逗号分隔的值运行基准测试。

**-S**, **--shell** _shell_
> 要使用的 shell（默认：系统默认 shell）。

**-N**
> 不经过 shell，直接运行命令。

**--ignore-failure**
> 遇到非零退出码时继续执行。

**--export-json** _file_
> 导出为 JSON。

**--export-csv** _file_
> 导出为 CSV。

**--export-markdown** _file_
> 导出为 Markdown。

**--show-output**
> 显示命令输出。

**--style** _type_
> 输出样式：auto、full、basic、nocolor、color、none。

# DESCRIPTION

**hyperfine** 是一款命令行基准测试工具，通过统计分析来测量命令执行时间。它多次运行命令并计算平均值、标准差、最小值、最大值和相对比较，从而提供准确的测量结果。

该工具会根据方差自动确定最优运行次数，确保结果具有统计意义。预热运行有助于消除缓存效应和解释型语言 JIT 编译的影响。

比较多条命令时，hyperfine 会显示相对加速/减速比。彩色输出会高亮最快的命令。这让优化的 A/B 测试变得简单直接。

参数扫描可以在一个数值范围内进行基准测试，而无需编写包装脚本。例如，用一条命令即可测试 1-16 的线程数。结果可导出为 JSON、CSV 或 Markdown，以便进一步分析或写入文档。

prepare 选项可实现干净状态的基准测试（例如清除缓存或重新构建）。shell 选项允许测试特定 shell 的特性，或使用 -N 以最小的 shell 开销直接运行。

# CAVEATS

系统负载会影响结果——请关闭其他应用以获得准确的测量。对于 JIT 编译或涉及缓存的操作，预热非常重要。极快的命令（< 5ms）可能存在明显的测量开销。统计离群值会影响平均值；请检查最小/最大值。

# HISTORY

**hyperfine** 由 David Peter（sharkdp）创建，于 **2018 年**前后发布。它用 Rust 编写，设计初衷是提供比基于 **time** 的 shell 基准测试更易用且统计上更严谨的替代方案。它是现代 CLI 工具集（包括 fd、bat 等）中的一员，这些工具是对传统 Unix 工具的改进。

# INSTALL

```apt: sudo apt install hyperfine```

```dnf: sudo dnf install hyperfine```

```pacman: sudo pacman -S hyperfine```

```apk: sudo apk add hyperfine```

```zypper: sudo zypper install hyperfine```

```brew: brew install hyperfine```

```nix: nix profile install nixpkgs#hyperfine```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[time](/man/time)(1), [perf](/man/perf)(1), [pv](/man/pv)(1)
