# TAGLINE

内核环形缓冲区消息查看工具

# TLDR

显示**内核消息**

```sudo dmesg```

显示内核**错误消息**

```sudo dmesg -l err```

实时**跟踪**内核消息

```sudo dmesg -w```

以**人类可读时间戳**显示消息

```sudo dmesg -T```

以**易读格式**显示消息

```sudo dmesg -H```

输出**着色**

```sudo dmesg -L```

按 **facility** 过滤消息

```sudo dmesg -f kern```

# SYNOPSIS

**dmesg** [_-l level_] [_-f facility_] [_-T_] [_-H_] [_-w_] [_-L_]

# DESCRIPTION

**dmesg** 打印并控制内核环形缓冲区，其中包含来自内核的消息，如硬件检测、驱动加载和系统事件。它是调试硬件与驱动问题的重要工具。

# PARAMETERS

**-l, --level level**
> 只显示指定的日志级别（emerg、alert、crit、err、warn、notice、info、debug）

**-f, --facility facility**
> 只显示指定的 facility（kern、user、mail、daemon 等）

**-T, --ctime**
> 打印人类可读的时间戳

**-H, --human**
> 启用带颜色和时间戳的易读输出

**-w, --follow**
> 等待新消息（类似 tail -f）

**-L, --color**
> 输出着色

**-c, --read-clear**
> 打印后清空环形缓冲区

**-C, --clear**
> 清空环形缓冲区但不打印

**-n, --console-level level**
> 设置打印到控制台的消息级别

**-k, --kernel**
> 仅打印内核消息

**-u, --userspace**
> 仅打印用户空间消息

**--time-format** _format_
> 时间戳格式：ctime、reltime、delta、iso、raw

**--since** _time_
> 显示指定时间之后的记录

**--until** _time_
> 显示指定时间之前的记录

**-J, --json**
> 以 JSON 格式输出

**-t, --notime**
> 不打印内核时间戳

**-r, --raw**
> 打印带日志级别前缀的原始消息缓冲区

**-x, --decode**
> 将 facility 和级别解码为可读前缀

# CAVEATS

在大多数系统上需要 root 权限。**-w**（follow）选项要求内核 3.5.0 及以上版本（用于 /dev/kmsg）。**-T** 和 **-H** 是 util-linux 的用户空间特性，不依赖特定内核版本。

# HISTORY

属于 **util-linux** 软件包。内核环形缓冲区自 Linux 早期版本就存在，提供重要的诊断信息。

# INSTALL

```apt: sudo apt install util-linux```

```dnf: sudo dnf install util-linux```

```pacman: sudo pacman -S util-linux```

```apk: sudo apk add dmesg```

```zypper: sudo zypper install util-linux```

```brew: brew install util-linux```

```nix: nix profile install nixpkgs#util-linux```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[journalctl](/man/journalctl)(1), [tail](/man/tail)(1)
