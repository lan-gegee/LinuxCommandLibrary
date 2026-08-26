# TAGLINE

显示来自 /proc/net/netstat 和 /proc/net/snmp 的网络统计信息

# TLDR

查看**自上次运行** nstat 以来的网络统计信息

```nstat```

查看**全部累计**的网络统计信息

```nstat -a```

显示统计信息但**不更新**历史记录

```nstat -s```

按**模式**过滤计数器

```nstat Tcp```

以 **JSON** 格式输出

```nstat -j```

# SYNOPSIS

**nstat** [_options_] [_PATTERN_...]

# PARAMETERS

**-a, --ignore**
> 显示绝对值（全部累计统计）而非增量

**-n, --nooutput**
> 不显示表头或输出（仅重置计数器）

**-r, --reset**
> 重置历史记录

**-s, --noupdate**
> 不更新历史记录（显示统计但不重置）

**-z, --zeros**
> 显示值为零的条目

**-j, --json**
> 以 JSON 格式输出

**-p, --pretty**
> 美化 JSON 输出（与 -j 配合使用）

**-d, --scan** _INTERVAL_
> 以守护进程模式运行，每隔 INTERVAL 秒收集一次统计信息

**-t, --interval** _INTERVAL_
> 用于平均速率的时间间隔（默认：60 秒）

**-h, --help**
> 显示帮助信息

# DESCRIPTION

**nstat** 显示来自 /proc/net/netstat 和 /proc/net/snmp 的网络统计信息，包括 IP、ICMP、TCP 和 UDP 计数器。默认情况下，它只显示自上次运行 nstat 以来的变化，因此非常适合持续监控网络活动。

该工具维护一个历史文件（~/.nstat.u）来跟踪之前的值。运行 nstat 会显示自上次运行以来的差值（增量），然后更新历史记录。使用 **-s** 可以在不更新的情况下查看统计。

统计内容包括数据包数量、错误数、重传次数以及各种协议特定的指标，对网络故障排查很有帮助。

# CAVEATS

增量模式依赖历史文件；首次运行会显示全零。**-a** 标志显示自启动以来的总量，忽略历史记录。属于 iproute2 软件包。

# INSTALL

```apt: sudo apt install iproute2```

```pacman: sudo pacman -S iproute2```

```apk: sudo apk add iproute2```

```zypper: sudo zypper install iproute2```

```brew: brew install iproute2```

```nix: nix profile install nixpkgs#iproute2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ss](/man/ss)(8), [ip](/man/ip)(8), [netstat](/man/netstat)(8), [sar](/man/sar)(1)
