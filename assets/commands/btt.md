# TAGLINE

分析块层 I/O 跟踪数据

# TLDR

**分析块层跟踪**数据

```btt -i [sda.blktrace.0]```

**以指定输出前缀进行分析**

```btt -i [device.blktrace.0] -o [analysis]```

**生成 Q2C 延迟数据**

```btt -i [trace.blktrace.0] -q [q2c_output]```

**生成 D2C 延迟数据**

```btt -i [trace.blktrace.0] -d [d2c_output]```

**分析合并后的跟踪文件**

```blkparse -i [sda] -d [merged.bin] && btt -i [merged.bin]```

**详细输出**的分析

```btt -i [trace.blktrace.0] -v```

# SYNOPSIS

**btt** [_options_] **-i** _trace_file_

# DESCRIPTION

**btt**（Block Trace Timeline）分析由 blktrace 生成的块层跟踪数据。它生成统计报告，展示整个块 I/O 栈中的 I/O 延迟分布、吞吐量和时序分解。

该分析将请求处理分解为多个阶段：Q（入队）、G（获取请求）、I（插入）、M（合并）、D（派发）、C（完成）。btt 报告这些阶段之间的延迟，以定位瓶颈。

输出包括总体统计、按设备的细分，以及可选的各阶段转换的详细计时文件。这些数据对于理解存储性能特征和诊断延迟问题非常有价值。

# PARAMETERS

**-i** _file_
> 输入的跟踪文件（来自 blkparse -d）。

**-o** _prefix_
> 输出文件前缀。

**-q** _file_
> 写入 Q2C 延迟数据。

**-d** _file_
> 写入 D2C 延迟数据。

**-l** _file_
> 写入每个 I/O 的延迟数据。

**-m** _file_
> 写入 D2D 寻道距离数据。

**-B** _file_
> 写入块号数据。

**-v**
> 详细输出。

**-V**
> 版本信息。

**-a**
> 包含全部统计项。

**-M**
> 仅显示设备映射信息。

# CAVEATS

需要来自 blkparse -d 的二进制跟踪数据，而非原始 blktrace 文件。大型跟踪会产生庞大的分析输出。时间戳必须同步，分析结果才有意义。输出文件可用 gnuplot 绘图以进行可视化。

# HISTORY

**btt** 由 **Alan D. Brunelle** 与 **blktrace** 一同开发，是 Linux 块层跟踪基础设施的一部分，自 Linux 内核 **2.6.17**（**2006 年**）引入 blktrace 软件包以来一直包含其中。它作为 blktrace 数据采集能力的配套分析工具，支持对块 I/O 子系统的深入性能分析。

# INSTALL

```apt: sudo apt install blktrace```

```dnf: sudo dnf install blktrace```

```zypper: sudo zypper install blktrace```

```nix: nix profile install nixpkgs#blktrace```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[blktrace](/man/blktrace)(8), [blkparse](/man/blkparse)(1), [iostat](/man/iostat)(1)
