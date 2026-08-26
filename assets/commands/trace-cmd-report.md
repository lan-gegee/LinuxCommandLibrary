# TAGLINE

显示已记录的内核跟踪数据

# TLDR

显示**已记录的**跟踪

```sudo trace-cmd report```

显示特定 **CPU** 的跟踪

```sudo trace-cmd report --cpu [cpu_number]```

# SYNOPSIS

**trace-cmd report** [_OPTIONS_] [_FILE_]

# PARAMETERS

**--cpu** _NUMBER_
> 只显示特定 CPU 的跟踪

**-i** _FILE_
> 从指定文件读取跟踪数据

# DESCRIPTION

**trace-cmd report** 显示来自 trace.dat 文件（或指定文件）的已记录跟踪事件。它解析二进制跟踪数据并以人类可读的格式呈现。

输出按时间顺序显示时间戳、CPU 编号、进程信息和跟踪事件。过滤选项可用于聚焦特定的 CPU 或事件类型。

# CAVEATS

需要内核版本匹配才能正确解析符号。处理大型跟踪文件可能耗时。某些事件需要调试信息才能完整解读。

# INSTALL

```apt: sudo apt install trace-cmd```

```dnf: sudo dnf install trace-cmd```

```pacman: sudo pacman -S trace-cmd```

```zypper: sudo zypper install trace-cmd```

```nix: nix profile install nixpkgs#trace-cmd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[trace-cmd](/man/trace-cmd)(1), [trace-cmd-list](/man/trace-cmd-list)(1), [trace-cmd-record](/man/trace-cmd-record)(1)
