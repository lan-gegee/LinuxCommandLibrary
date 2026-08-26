# TAGLINE

高级系统压力测试框架

# TLDR

**对 CPU 施压**

```stress-ng --cpu [4] --timeout [60s]```

**对内存施压**

```stress-ng --vm [2] --vm-bytes [1G] --timeout [60s]```

**对磁盘 I/O 施压**

```stress-ng --io [4] --timeout [60s]```

**组合压力测试**

```stress-ng --cpu [2] --vm [2] --io [2] --timeout [60s]```

**矩阵运算**（CPU 密集型）

```stress-ng --matrix [4] --timeout [60s]```

**显示可用的压力源**

```stress-ng --stressors```

**输出指标**

```stress-ng --cpu [4] --metrics --timeout [60s]```

**限制 CPU 占用**

```stress-ng --cpu [4] --cpu-load [50] --timeout [60s]```

# SYNOPSIS

**stress-ng** [_--cpu n_] [_--vm n_] [_--io n_] [_--timeout t_] [_options_]

# PARAMETERS

**--cpu** _N_
> CPU 压力工作进程数。

**--cpu-load** _PERCENT_
> 目标 CPU 负载。

**--vm** _N_
> 内存压力工作进程数。

**--vm-bytes** _SIZE_
> 每个工作进程的内存量。

**--io** _N_
> I/O 压力工作进程数。

**--hdd** _N_
> 磁盘写入工作进程数。

**--matrix** _N_
> 矩阵计算压力。

**--timeout** _TIME_
> 测试时长。

**--metrics**
> 显示统计信息。

**--verbose**
> 详细输出。

**--stressors**
> 列出所有压力源。

**--class** _CLASS_
> 运行指定类别的压力源。

**--sequential** _N_
> 顺序运行压力源。

**--all** _N_
> 运行全部压力源。

# DESCRIPTION

**stress-ng** 用于测试系统在各种负载下的稳定性。它对 CPU、内存、I/O 和其他子系统施加压力，以发现硬件或软件问题。

CPU 压力源包括整数运算、浮点运算、矩阵操作和加密算法。不同的压力源锻炼 CPU 的不同部件。

内存测试会分配、写入并校验 RAM。它们可以暴露内存故障、散热问题和内存控制器缺陷。

I/O 压力源会考验文件系统和块设备操作。它们能揭示磁盘、控制器和驱动器的问题。

指标显示每秒操作次数和系统统计信息。这有助于量化性能并定位瓶颈。

组合负载模拟真实的多组件压力。散热和供电问题往往只在混合负载下出现。

# CAVEATS

可能损坏不稳定的硬件。可能产生高温。可能触发 OOM killer。使用时请配合温度监控。

# HISTORY

**stress-ng** 由 **Canonical** 的 **Colin Ian King** 编写，是 stress 的增强版本。它提供多得多的压力源类型，被用于内核和硬件测试。

# INSTALL

```apt: sudo apt install stress-ng```

```dnf: sudo dnf install stress-ng```

```pacman: sudo pacman -S stress-ng```

```apk: sudo apk add stress-ng```

```zypper: sudo zypper install stress-ng```

```brew: brew install stress-ng```

```nix: nix profile install nixpkgs#stress-ng```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[stress](/man/stress)(1), [sysbench](/man/sysbench)(1), [memtester](/man/memtester)(8), [fio](/man/fio)(1)
