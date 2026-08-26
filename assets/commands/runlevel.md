# TAGLINE

显示当前和上一个 SysV 运行级别

# TLDR

**显示**上一个和当前的 SysV 运行级别

```runlevel```

**显示**帮助信息

```runlevel --help```

# SYNOPSIS

**runlevel** [_options_]

# PARAMETERS

**--help**
> 显示帮助信息

# ENVIRONMENT

**$RUNLEVEL**
> 覆盖该命令报告的当前运行级别。

**$PREVLEVEL**
> 覆盖该命令报告的上一个运行级别。

# DESCRIPTION

**runlevel** 从 utmp 文件（**/run/utmp**）中打印上一个和当前的 SysV 运行级别。运行级别是 Unix System V 风格 init 系统中的一种运行模式，定义了哪些服务正在运行。

输出包含两个值：上一个运行级别（如果不可用则为 **N**）和当前运行级别。如果两者都无法确定，则打印 **unknown**。

# CAVEATS

主要与旧式 SysV init 系统相关。在基于 systemd 的系统上，运行级别的概念已被 target 取代，不过为了兼容性 runlevel 仍然可用。systemd 中的等价操作是使用 **systemctl get-default**。

# HISTORY

**runlevel** 源自 **System V init**。在 systemd 系统上，它会读取 utmp 以保持向后兼容。对应的 systemd 命令是 **systemctl get-default**。

# INSTALL

```apt: sudo apt install runit-init```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[init](/man/init)(8), [systemctl](/man/systemctl)(1)
