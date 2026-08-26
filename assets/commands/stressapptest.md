# TAGLINE

Google 内存与硬件压力测试工具

# TLDR

**运行内存压力测试**

```stressapptest -s [60]```

**指定内存大小**

```stressapptest -M [1024] -s [60]```

**文件测试**

```stressapptest -f [/tmp/testfile] -s [60]```

**详细输出**

```stressapptest -v [2] -s [60]```

**多个内存复制线程**

```stressapptest -m [4] -s [60]```

**带 CPU 压力线程**

```stressapptest -C [4] -s [60]```

在块设备上进行**直接磁盘测试**

```stressapptest -d [/dev/sda] -s [60]```

# SYNOPSIS

**stressapptest** [_-s seconds_] [_-M mbytes_] [_-m threads_] [_options_]

# PARAMETERS

**-s** _SEC_
> 持续时间（秒）。

**-M** _MB_
> 内存量（MB）。

**-m** _N_
> 内存复制线程数。

**-C** _N_
> CPU 压力线程数。

**-i** _N_
> 内存取反（invert）线程数。

**-f** _FILE_
> 使用临时文件添加一个磁盘线程。

**-d** _DEV_
> 使用块设备（或文件）添加一个直接写盘线程。

**-n** _IP_
> 添加一个连接到指定 IP 地址的网络线程。

**-v** _LEVEL_
> 详细程度级别。

**-l** _FILE_
> 日志文件。

**-W**
> 使用热复制（带缓存预热的内存拷贝）。

**-A**
> 在不兼容的系统上以降级模式运行。

# DESCRIPTION

**stressapptest**（Stressful Application Test）是 Google 开发的内存和硬件验证工具，用于发现内存子系统、磁盘 I/O 和其他硬件组件中的错误。它生成真实的高负载模式，对内存总线、缓存层次结构和存储通路进行考验，以暴露间歇性的硬件故障。

该工具分配可配置数量的内存，并持续写入数据模式、读回并校验正确性。这种方法能有效检测 ECC 内存错误、故障 DIMM 内存条、内存控制器问题和热节流问题。还可以加入文件 I/O 测试，同时对磁盘和存储控制器硬件施压。

Stressapptest 特别适合用于验收新硬件、服务器投产前的烤机测试，以及诊断在负载下出现间歇性崩溃或数据损坏的系统。

# CAVEATS

会产生热量。可能触发故障。在生产环境使用时务必小心。

# HISTORY

**stressapptest** 由 **Google** 开发，用于对内存子系统进行压力测试并发现硬件错误。

# INSTALL

```apt: sudo apt install stressapptest```

```dnf: sudo dnf install stressapptest```

```zypper: sudo zypper install stressapptest```

```nix: nix profile install nixpkgs#stressapptest```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[stress](/man/stress)(1), [memtester](/man/memtester)(1), [mprime](/man/mprime)(1)
