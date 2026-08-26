# TAGLINE

基于硬件性能计数器的类 top 显示工具

# TLDR

**启动交互式监视器**

```tiptop```

每 2 秒刷新一次

```tiptop -d [2]```

只显示指定进程

```tiptop -p [firefox]```

只显示某个用户的任务

```tiptop -u [$USER]```

**以批处理模式运行** 5 次迭代（例如用于记录日志）

```tiptop -b -n [5]```

将内核活动计入计数器值（需要 root / **CAP_SYS_ADMIN**）

```sudo tiptop -K```

# SYNOPSIS

**tiptop** [_options_] [_command_]

# PARAMETERS

**-b**
> 批处理模式：输出到 stdout，无交互控制。

**-c**
> 显示完整命令行而不是进程名。

**-d** _SECONDS_
> 刷新间隔（允许小数值）。

**-H**
> 每个线程一行显示，而不是每个进程一行。

**-i**
> 包含空闲任务。

**-K**
> 统计内核态事件（需要 **perf_event_paranoid <= 1** 或 root）。

**-n** _COUNT_
> 刷新 _COUNT_ 次后退出（配合 **-b** 使用）。

**-p** _PID_or_NAME_
> 按 PID 或进程名限定显示范围。

**-u** _USER_
> 按用户限定显示范围。

**-w** _PID_
> 高亮并跟踪单个任务。

**-S** _COL_
> 按指定列排序。

**--sticky**
> 已结束的任务保留在表格中。

**--epoch**
> 批处理输出中使用 Unix epoch 时间戳。

# DESCRIPTION

**tiptop** 以类似 top 的视图显示运行中的任务，但各列的数据不是 CPU% 和 RSS，而是通过 Linux **perf_event** 接口读取的**硬件性能计数器**（每周期指令数、缓存未命中、分支预测失败等）。这使它适合发现标准 **top** 看不到的微架构瓶颈——糟糕的缓存行为、分支预测问题、FPU 压力等。

计数器的集合及其组合成列的方式按架构分别配置；用户还可以在 **~/.tiptoprc** 中自定义列，展示额外的计数器或派生指标。

# CAVEATS

需要硬件性能计数器支持和可访问的 **perf_event** 子系统；在加固内核上可能需要调低 **/proc/sys/kernel/perf_event_paranoid**。**-K**（统计内核事件）需要提升的权限。某些虚拟机不暴露 PMU 计数器，此时各列会显示为零。

# HISTORY

**tiptop** 由 **INRIA** 的 **Erven Rohou** 编写，目标是让硬件性能计数器像 **top** 一样易于使用。存在一个同名的独立 Python 工具，与本工具无关；本页面描述的是 Debian、Ubuntu、Fedora 和 Arch 中打包为 **tiptop** 的 Erven Rohou 正统实现。

# INSTALL

```apt: sudo apt install tiptop```

```dnf: sudo dnf install tiptop```

```zypper: sudo zypper install tiptop```

```nix: nix profile install nixpkgs#tiptop```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[top](/man/top)(1), [htop](/man/htop)(1), [perf](/man/perf)(1), [pidstat](/man/pidstat)(1)
