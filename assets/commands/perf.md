# TAGLINE

官方 Linux 内核性能分析工具

# TLDR

显示命令的**性能统计数据**

```perf stat [command]```

显示**实时的**全系统性能概况

```sudo perf top```

**记录**性能概况到 perf.data

```sudo perf record [command]```

记录**现有进程**的性能概况

```sudo perf record -p [pid]```

**显示**已记录的性能概况

```sudo perf report```

**记录**调用关系图

```sudo perf record -g [command]```

列出可用的**事件**

```perf list```

# SYNOPSIS

**perf** [**stat**|**record**|**report**|**top**|**list**] [_options_] [_command_]

# COMMANDS

**stat**
> 运行命令并收集性能计数器统计信息

**record**
> 运行命令并把性能概况记录到 perf.data

**report**
> 读取 perf.data 并显示性能概况

**top**
> 全系统实时性能剖析

**list**
> 列出可用的性能事件

**annotate**
> 读取 perf.data 并显示带注解的代码

**script**
> 读取 perf.data 并以脚本能读取的格式输出跟踪数据

**bench**
> 运行针对调度器、内存等的内置微基准测试

**trace**
> 跟踪系统调用（类似 strace）

**sched**
> 分析调度器延迟和行为

**diff**
> 比较两个 perf.data 文件

# PARAMETERS

**-p, --pid _pid_**
> 按 PID 分析现有进程

**-e, --event _event_**
> 选择要测量的特定事件

**-g**, **--call-graph**
> 启用调用图（栈链/回溯）记录

**-a**, **--all-cpus**
> 从所有 CPU 进行全系统采集

**-F _freq_**, **--freq _freq_**
> 以指定频率采样（每秒采样次数）

**-o _file_**, **--output _file_**
> 输出文件名

**-c _count_**, **--count _count_**
> 每发生 _count_ 个事件采集一个样本

# DESCRIPTION

**perf** 是官方的 Linux 内核性能分析工具。它提供对硬件性能计数器、跟踪点和软件性能事件的访问能力。对于定位应用程序和内核中的性能瓶颈来说必不可少。

该工具可以测量 CPU 周期、缓存未命中、分支预测失败等众多底层事件。它既支持基于采样的性能分析，也支持事件计数。

# CAVEATS

许多操作需要 root 权限或调整 kernel.perf_event_paranoid 内核参数。硬件计数器的可用性因 CPU 而异。性能数据可能很大。某些功能需要特定的内核配置。

# HISTORY

**perf** 作为 Linux 内核的一部分开发而成，主要贡献者是 **Ingo Molnar** 和 **Thomas Gleixner**。它取代了较旧的 OProfile 工具，并直接集成进内核源码树，成为 Linux 标准的性能分析接口。

# INSTALL

```apt: sudo apt install linux-perf```

```dnf: sudo dnf install perf```

```pacman: sudo pacman -S perf```

```apk: sudo apk add perf```

```zypper: sudo zypper install perf```

```nix: nix profile install nixpkgs#perf```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[strace](/man/strace)(1), [ltrace](/man/ltrace)(1), [valgrind](/man/valgrind)(1), [gprof](/man/gprof)(1)
