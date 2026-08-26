# TAGLINE

多线程系统基准测试工具

# TLDR

**CPU 基准测试**

```sysbench cpu run```

**多线程 CPU 基准测试**

```sysbench cpu --threads=[4] run```

**内存基准测试**

```sysbench memory run```

**文件 I/O 准备**

```sysbench fileio --file-total-size=[10G] prepare```

**文件 I/O 基准测试**

```sysbench fileio --file-total-size=[10G] --file-test-mode=[rndrw] run```

**MySQL 基准测试**

```sysbench oltp_read_write --mysql-host=[localhost] --mysql-user=[user] --mysql-password=[pass] --mysql-db=[test] run```

**清理测试文件**

```sysbench fileio --file-total-size=[10G] cleanup```

**自定义素数上限的 CPU 基准测试**

```sysbench cpu --cpu-max-prime=[20000] --threads=[4] run```

# SYNOPSIS

**sysbench** _test_ [_options_] [**prepare**|**run**|**cleanup**]

# PARAMETERS

**cpu**
> CPU 测试。

**memory**
> 内存测试。

**fileio**
> 文件 I/O 测试。

**oltp_read_write**
> 数据库 OLTP 测试。

**oltp_read_only**
> 只读数据库测试。

**threads**
> 线程调度器性能测试。

**mutex**
> 互斥锁争用性能测试。

**--threads** _N_
> 线程数（默认：1）。

**--time** _SECONDS_
> 测试时长（默认：10）。

**--events** _N_
> 事件数上限（默认：0，无限制）。

**--file-total-size** _SIZE_
> 文件总大小。

**--file-test-mode** _MODE_
> I/O 模式（seqwr、seqrd、rndrw 等）。

**--mysql-host** _HOST_
> MySQL 主机。

**--mysql-user** _USER_
> MySQL 用户。

**--mysql-password** _PASS_
> MySQL 密码。

**--mysql-db** _DB_
> MySQL 数据库名。

**--cpu-max-prime** _N_
> CPU 测试中素数计算的上限（默认：10000）。

**--memory-block-size** _SIZE_
> 内存测试的内存块大小（默认：1K）。

**--memory-total-size** _SIZE_
> 内存测试要传输的数据总量（默认：100G）。

**--memory-oper** _OP_
> 内存操作类型：read 或 write（默认：write）。

**--memory-access-mode** _MODE_
> 内存访问模式：seq 或 rnd（默认：seq）。

**--file-num** _N_
> 要创建的文件数（默认：128）。

**--file-extra-flags** _FLAGS_
> 打开文件的额外标志：sync、dsync、direct。

**--percentile** _N_
> 延迟统计中计算的百分位（默认：95）。

**--report-interval** _SECONDS_
> 定期报告中间统计信息（0 = 禁用）。

**prepare**
> 准备测试数据（fileio 和数据库测试必需）。

**run**
> 运行基准测试。

**cleanup**
> 清理 prepare 阶段创建的测试数据。

# DESCRIPTION

**sysbench** 是一个多线程基准测试工具，用于评估系统在 CPU、内存、文件 I/O 和数据库工作负载下的性能。它提供一致且可复现的测量结果，便于在不同硬件配置、内核版本或调优参数之间进行有意义的比较。

该工具内置了常见基准的测试类型。CPU 测试通过素数计算给处理器施加压力，以衡量计算吞吐量。内存测试测量顺序和随机访问模式下的带宽与延迟。文件 I/O 测试支持多种模式，包括顺序写、顺序读和随机读写混合；运行前需要准备步骤来创建测试文件，运行后需要清理步骤。

数据库基准测试针对 MySQL 或 PostgreSQL 模拟 OLTP（联机事务处理）工作负载，执行贴近真实的 select、insert、update 和 delete 查询组合。所有测试类型都支持多线程执行，以衡量性能随并行度扩展的情况，从而暴露瓶颈与争用点。除内置测试外，还可通过自定义 Lua 脚本定义更多工作负载。

# CAVEATS

结果取决于测试参数。合成基准无法反映所有工作负载。文件测试需要磁盘空间。数据库测试需要预先配置。

# HISTORY

**sysbench** 由 **Alexey Kopytov** 在 MySQL AB 于 **2004 年**前后创建。后来成为 MySQL 基准测试和通用系统性能测试的标准工具。

# INSTALL

```apt: sudo apt install sysbench```

```dnf: sudo dnf install sysbench```

```pacman: sudo pacman -S sysbench```

```apk: sudo apk add sysbench```

```zypper: sudo zypper install sysbench```

```brew: brew install sysbench```

```nix: nix profile install nixpkgs#sysbench```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fio](/man/fio)(1), [stress-ng](/man/stress-ng)(1), [pgbench](/man/pgbench)(1), [iperf](/man/iperf)(1)
