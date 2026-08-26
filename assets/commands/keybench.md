# TAGLINE

面向排序键值存储的可脚本化基准测试工具

# TLDR

对默认的内存引擎**运行工作负载**

```keybench [path/to/workload.lua]```

一次运行中**测试多个引擎**（持久化引擎需要数据目录）

```keybench --backend [skiplist,rocksdb,tidesdb] --data-dir [path/to/data] [path/to/workload.lua]```

**扫描一组线程数**以测试扩展性

```keybench --threads [1,2,4,8] [path/to/workload.lua]```

按固定时长运行，而非固定操作次数

```keybench --secs [30] [path/to/workload.lua]```

**重复每次测量**并报告中位数

```keybench --repeat [5] [path/to/workload.lua]```

**将结果写入**控制台和 TSV 文件

```keybench --report [console,tsv:results.tsv] [path/to/workload.lua]```

# SYNOPSIS

**keybench** [_options_] _workload_file_ [_workload_file ..._]

# DESCRIPTION

**keybench** 是一个基准测试框架，用于测量多个**排序键值存储引擎**的吞吐量和延迟。工作负载只需用 **Lua** 编写一次，即可不加修改地在所有后端上运行，从而在相同访问模式下公平地比较各引擎。

每个工作负载是一个 Lua 表，必须包含 **run** 函数（被测量的工作单元），可选包含 **load** 函数，用于在计时开始前填充存储。工作负载还可以声明一个 **sweep**，在一系列参数取值上重复执行 run。该框架会报告两项吞吐量指标——每秒工作负载单元数（**wu/s**）和每秒原始操作数（**ops/s**），以及每种操作类型的 p50、p99、p99.9 和最大延迟。

keybench 使用 **make** 编译；生成的二进制文件默认内嵌内存版 skiplist 引擎。持久化引擎需在构建时启用，例如 **make ROCKSDB=1 TIDESDB=1**。

# OPTIONS

**--ops** _N_
> 所有线程总共要运行的工作负载单元数（默认 200000）。

**--secs** _S_
> 运行 _S_ 秒，而非固定的操作次数。

**--users** _N_
> 传递给工作负载上下文的用户规模。

**--items** _N_
> 传递给工作负载上下文的目录或键空间大小。

**--seed** _N_
> 基础随机数种子；线程 _t_ 使用 seed + _t_。

**--backend** _LIST_
> 要测试的引擎列表，逗号分隔（例如 skiplist,rocksdb,tidesdb）。

**--threads** _LIST_
> 用于扩展性测试扫描的线程数列表，逗号分隔。

**--seed-once**
> 每个引擎只填充一次数据集，并在整个线程扫描过程中复用。

**--repeat** _N_
> 每个网格点运行 _N_ 次并报告中位数。

**--data-dir** _DIR_
> rocksdb、tidesdb 等持久化引擎的数据目录（这些引擎必需）。

**--report** _LIST_
> 输出目标：console、tsv:file 或 timeline:file。

**--report-dir** _DIR_
> 创建带时间戳的目录，并将所有运行产物归档其中。

**--auto-plot**
> 在运行结束后生成图表。

**--config** _FILE_
> 从 INI 文件加载运行参数。

**--save-config** _FILE_
> 将生效的运行参数写为可复现的配置文件。

# STORAGE ENGINES

**skiplist**
> 带读写锁的内存概率跳表。参考实现引擎；不支持持久化。

**rocksdb**
> 持久化的 LSM-tree 存储，通过 INI 配置中的 [rocksdb] 区段进行设置。

**tidesdb**
> 支持事务的持久化 LSM-tree 存储，通过 [tidesdb] 区段进行设置。

# CAVEAT

持久化引擎（rocksdb、tidesdb）仅在编译时启用后才可用（**make ROCKSDB=1 TIDESDB=1**），并且需要 **--data-dir**。结果高度依赖硬件、内存分配器和构建选项，因此只应在同一台机器和相同构建下比较运行结果。

# HISTORY

**keybench** 是一款开源基准测试工具，主要由开发者 **guycipher** 以 **C** 编写（配合 Lua 工作负载和 Python 辅助脚本），采用 **GPL-2.0** 许可证发布。

# SEE ALSO

[redis-benchmark](/man/redis-benchmark)(1), [memtier_benchmark](/man/memtier_benchmark)(1), [sysbench](/man/sysbench)(1), [fio](/man/fio)(1), [hyperfine](/man/hyperfine)(1)
