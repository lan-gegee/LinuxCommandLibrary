# TAGLINE

类似 top 的 Austin Python 帧栈采样器 TUI 界面

# TLDR

**分析一个 Python 脚本**

```austin-tui python3 [path/to/script.py]```

按 PID **附加到正在运行的 Python 进程**

```sudo austin-tui -p [pid]```

**附加到进程及其子进程**

```sudo austin-tui -Cp [pid]```

**分析内存使用**而非 CPU 时间

```austin-tui -m python3 [path/to/script.py]```

以自定义采样间隔（微秒）进行分析

```austin-tui -i [200] python3 [path/to/script.py]```

**限时采样**（单位为秒）

```austin-tui -x [10] python3 [path/to/script.py]```

# SYNOPSIS

**austin-tui** [_options_] [_command_ [_args..._]]

**austin-tui** [_options_] **-p** _pid_

# PARAMETERS

**-p** _pid_, **--pid** _pid_
> 通过进程 ID 附加到已存在的 Python 进程。

**-C**, **--children**
> 同时采样子 Python 进程。可用方向键在它们之间切换。

**-m**, **--memory**
> 分析内存使用而非实际耗时。

**-c**, **--cpu**
> 仅采样 CPU 上运行的调用栈，忽略空闲时间。

**-i** _microseconds_, **--interval** _microseconds_
> 设置以微秒为单位的采样间隔（默认值为 100）。

**-x** _seconds_, **--exposure** _seconds_
> 仅采样指定的秒数，然后停止。

**-t** _milliseconds_, **--timeout** _milliseconds_
> 近似的启动等待时间；在较慢的机器上可增大该值（默认值为 100 ms）。

# DESCRIPTION

**austin-tui** 是 CPython 帧栈采样器 **Austin** 的一个类 top 文本界面。它以实时终端视图展示 Python 应用把时间花在哪里或在何处分配内存，同时显示 CPU 和内存使用图表以及逐帧统计信息。

Austin 的工作原理是读取 CPython 解释器的虚拟内存来采样帧栈，无需任何插桩，对目标应用的开销也极小。austin-tui 将这些采样数据封装在一个受 Unix **top** 命令启发的基于 curses 的界面中。

默认视图显示当前进程和线程最近一次出现的调用栈，大约每秒刷新一次。按下 **F** 切换到完整模式，以层级树形式显示所有收集到的帧统计信息。按下 **G** 启动实时火焰图可视化。使用左右方向键在线程间导航，当前 PID 和 TID 显示在标题栏中。

其他交互按键包括：**P** 暂停显示（后台采样继续进行）、**S** 将收集到的性能数据保存到带时间戳的文件、以及 **+**/**-** 调整所显示帧的最小百分比阈值。

在 VS Code 终端中运行时，输出中的源文件路径支持 Ctrl+Click（macOS 上为 Cmd+Click）跳转。保存的数据可在 Austin VS Code 扩展中加载，进行进一步的火焰图分析。

# CONFIGURATION

austin-tui 不使用配置文件。所有选项都通过命令行参数传递。底层的 Austin 二进制文件必须单独安装，并能在系统 PATH 中找到。

在 Linux 上，若想避免用 **sudo** 运行，可以为 Austin 二进制文件授予 ptrace 能力：

```sudo setcap cap_sys_ptrace+ep `which austin```

# CAVEATS

需要已安装 **Austin 3** 二进制文件并在 PATH 中可用。在 macOS 上，系统完整性保护（SIP）会阻止对 /usr/bin/python3 这一系统 Python 进行采样；请改用虚拟环境或通过 Homebrew 安装的解释器。在 Windows 上，标准的 Python curses 模块已损坏，必须手动安装替代 wheel 包。

# HISTORY

**austin-tui** 由 **Gabriele N. Tornetta**（P403n1x87）创建，首个候选版本（v1.1.0rc1）发布于 **2019 年 11 月**。火焰图模式于 **v1.2.0**（2021 年 4 月）加入，MOJO 二进制格式支持则出现在 **v1.4.0**（2024 年 11 月）。项目采用 GPL-3.0 许可证。

# SEE ALSO

[top](/man/top)(1), [htop](/man/htop)(1), [py-spy](/man/py-spy)(1), [perf](/man/perf)(1)
