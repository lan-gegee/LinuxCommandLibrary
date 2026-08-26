# TAGLINE

将内核跟踪记录到文件

# TLDR

使用指定**插件**记录

```sudo trace-cmd record -p [plugin]```

记录指定的**可执行文件**

```sudo trace-cmd record -F [executable]```

记录指定的**函数**

```sudo trace-cmd record -g [function]```

**排除**某个函数

```sudo trace-cmd record -n [function]```

限制**调用图深度**

```sudo trace-cmd record --max-graph-depth [depth]```

按**进程** ID 记录

```sudo trace-cmd record -P [pid]```

# SYNOPSIS

**trace-cmd record** [_OPTIONS_]

# PARAMETERS

**-p** _PLUGIN_
> 使用指定的跟踪器插件

**-F** _EXECUTABLE_
> 只跟踪指定的可执行文件

**-g** _FUNCTION_
> 跟踪指定的函数

**-n** _FUNCTION_
> 在跟踪中排除该函数

**--max-graph-depth** _DEPTH_
> 限制函数调用图深度

**-P** _PID_
> 跟踪指定的进程 ID

# DESCRIPTION

**trace-cmd record** 将内核跟踪事件捕获到文件（默认为 trace.dat）。它会配置 Ftrace 框架、启动跟踪并保存结果，供之后用 trace-cmd report 进行分析。

各种选项支持按函数、进程或可执行文件过滤，并可限制跟踪深度以减少数据量。

# CAVEATS

需要 root 权限。大型跟踪会占用大量磁盘空间。高频跟踪会影响系统性能。输出文件可能快速增长。

# INSTALL

```apt: sudo apt install trace-cmd```

```dnf: sudo dnf install trace-cmd```

```pacman: sudo pacman -S trace-cmd```

```zypper: sudo zypper install trace-cmd```

```nix: nix profile install nixpkgs#trace-cmd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[trace-cmd](/man/trace-cmd)(1), [trace-cmd-list](/man/trace-cmd-list)(1), [trace-cmd-report](/man/trace-cmd-report)(1)
