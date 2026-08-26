# TAGLINE

报告正在运行的进程状态

# TLDR

**列出所有进程**

```ps aux```

**列出当前用户的进程**

```ps -u [username]```

**显示进程树**

```ps -ef --forest```

**显示特定进程**

```ps -p [pid]```

**自定义输出格式**

```ps -eo pid,ppid,cmd,%mem,%cpu```

**列出线程**

```ps -eLf```

**按内存占用排序**（降序）

```ps aux --sort=-%mem```

**按命令名选择进程**

```ps -C [nginx]```

# SYNOPSIS

**ps** [_options_]

# PARAMETERS

**a**
> 所有用户。

**u**
> 面向用户的格式。

**x**
> 包含无 tty 的进程。

**-e**
> 所有进程。

**-f**
> 完整格式。

**-p** _PID_
> 按 PID 选择。

**-u** _USER_
> 按用户选择。

**--forest**
> 进程树。

**-o** _FORMAT_
> 自定义输出。

**-L**
> 显示线程及 LWP 和 NLWP 列。

**-C** _CMD_
> 按命令名选择。

**--sort** _KEY_
> 对输出排序（如 --sort=-%mem）。

# DESCRIPTION

**ps** 报告系统当前运行进程的快照。它显示每个进程的进程 ID、用户、CPU 和内存占用、命令名、运行时长等信息，提供系统活动在某一时刻的视图。

该命令接受两种风格的选项：BSD 语法（不带连字符，如 **aux**）和 POSIX 语法（带连字符，如 **-ef**）。两者产生的输出类似，但在默认列和过滤行为上有所不同。**-o** 选项允许完全自定义输出格式，选择 pid、ppid、command 和资源占用等特定字段。

常见用法包括：用 **ps aux** 列出所有进程及详细信息，用 **ps -ef --forest** 以树状显示进程层级，用 **ps -p** 按 PID 检查特定进程。

# CAVEATS

BSD 与 POSIX 选项有所差异。常用 aux 或 -ef。

# HISTORY

ps 是一款**经典的 Unix** 进程监控工具。

# INSTALL

```apt: sudo apt install procps```

```dnf: sudo dnf install procps-ng```

```pacman: sudo pacman -S procps-ng```

```apk: sudo apk add procps-ng```

```zypper: sudo zypper install procps```

```brew: brew install procps```

```nix: nix profile install nixpkgs#procps```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[top](/man/top)(1), [htop](/man/htop)(1), [pgrep](/man/pgrep)(1), [kill](/man/kill)(1)
