# TAGLINE

内存带宽基准测试工具

# TLDR

用 512 MiB 数组运行**全部测试 3 次**

```mbw -n 3 512```

用 512 MiB 运行测试并采用**安静模式**抑制平均值输出

```mbw -n 3 -q -a 512```

用 512 MiB 运行 **memcpy 测试** 3 次，只显示统计结果

```mbw -n 3 -q -t0 512```

用 8192 MiB 数组和 **1024 字节块**运行 **mcblock 测试** 10 次

```mbw -n 10 -q -t2 -b 1024 8192```

用 2048 MiB 运行 dumb 测试并**无限循环运行**

```mbw -n 0 -t1 -q 2048```

# SYNOPSIS

**mbw** [_options_] _size_in_MiB_

# PARAMETERS

**-n _count_**
> 测试迭代次数（0 表示无限）

**-q**
> 安静模式；只显示统计结果，不显示每次迭代的输出

**-a**
> 不打印平均值

**-t _type_**
> 测试类型：0=memcpy，1=dumb（逐字节复制），2=mcblock（块复制）

**-b _bytes_**
> mcblock 测试（-t2）的块大小（字节）

**-h**
> 显示简要帮助

# DESCRIPTION

**mbw**（Memory Bandwidth）是一个基准测试工具，通过分配两块内存区域并测量数据在它们之间复制的速度来衡量内存复制性能。

提供三种测试方法：**memcpy** 使用 C 库优化过的 memcpy 函数；**dumb** 逐字节复制以测量原始内存访问速度；**mcblock** 按用户指定的块大小复制以分析缓存行为。

结果以 MB/s 报告，有助于评估内存子系统性能、比较不同系统或发现内存配置问题。

# CAVEATS

结果可能因系统负载、CPU 频率调节和内存访问模式而有显著差异。要获得一致的基准数据，请确保系统空闲，并考虑禁用 CPU 频率调节。dumb 测试故意很慢，适合测量最坏情况下的内存延迟。

# HISTORY

mbw 由 Andras Horvath 编写，是一个简单的内存带宽测试工具，特别适用于比较不同系统或配置下的 RAM 性能。

# INSTALL

```apt: sudo apt install mbw```

```brew: brew install mbw```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[memtester](/man/memtester)(1), [stress-ng](/man/stress-ng)(1), [sysbench](/man/sysbench)(1)
