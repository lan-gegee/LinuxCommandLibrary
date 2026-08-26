# TAGLINE

显示系统运行时间和平均负载

# TLDR

**显示系统运行时间**和平均负载

```uptime```

**以美观格式显示运行时间**

```uptime -p```

**显示系统的启动时间**

```uptime -s```

# SYNOPSIS

**uptime** [_options_]

# PARAMETERS

**-p**, **--pretty**
> 以人类可读的格式显示运行时间

**-s**, **--since**
> 显示系统启动的日期和时间（yyyy-mm-dd HH:MM:SS）

**-h**, **--help**
> 显示帮助信息

**-V**, **--version**
> 显示版本信息

# OUTPUT FORMAT

默认输出包括：
- 当前时间
- 系统运行时间（天、小时、分钟）
- 已登录用户数
- 1、5 和 15 分钟的平均负载

示例：`14:30:05 up 7 days, 3:42, 2 users, load average: 0.15, 0.20, 0.18`

# DESCRIPTION

**uptime** 显示系统已运行了多长时间、当前登录的用户数量，以及过去 1、5、15 分钟的系统平均负载。

平均负载代表等待 CPU 时间的进程数量的均值。在单 CPU 系统上，负载 1.0 表示 CPU 已被完全占用；在 4 CPU 系统上，负载 4.0 表示满载。如果数值超过 CPU 数量，则表明有进程在排队等待 CPU 时间。

该命令从 **/proc/uptime** 读取系统运行时间，从 **/var/run/utmp** 读取用户信息。它属于 procps-ng 软件包。

# CAVEATS

平均负载包含等待 I/O 的进程，而不仅仅是 CPU 密集型进程，这使得解读起来不那么直观。用户数统计的是登录会话，同一用户的多个终端会被重复计入。系统运行时间在重启后会清零；如需历史在线时长追踪，请使用外部监控工具。

# HISTORY

uptime 命令源自早期 Unix 系统，是快速检查系统健康状况的手段之一。它后来成为标准 Unix 工具集的一员，被所有类 Unix 系统收录。负载平均值的概念由 BSD Unix 引入。在 Linux 上，uptime 属于 **procps**（后更名为 **procps-ng**）软件包，该软件包提供了一组用于检查 **/proc** 文件系统的实用工具。

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

[w](/man/w)(1), [top](/man/top)(1), [who](/man/who)(1), [last](/man/last)(1)
