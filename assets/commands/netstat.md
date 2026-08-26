# TAGLINE

显示网络连接、路由表、接口统计信息、伪装连接

# TLDR

**显示所有连接**和监听端口

```netstat -a```

**仅显示监听端口**

```netstat -l```

以数字地址形式**显示 TCP 连接**

```netstat -tn```

**显示带进程 ID 的监听端口**

```sudo netstat -tulnp```

**显示路由表**

```netstat -r```

**显示网络接口统计信息**

```netstat -i```

**显示协议统计信息**

```netstat -s```

**持续刷新**连接状态

```netstat -c```

# SYNOPSIS

**netstat** [_options_]

**netstat** {--route|-r} [_options_]

**netstat** {--interfaces|-i} [_options_]

**netstat** {--statistics|-s} [_options_]

# PARAMETERS

**-a**, **--all**
> 同时显示监听和非监听状态的套接字

**-l**, **--listening**
> 仅显示处于监听状态的套接字

**-t**, **--tcp**
> 显示 TCP 连接

**-u**, **--udp**
> 显示 UDP 连接

**-n**, **--numeric**
> 显示数字地址而不解析名称

**-p**, **--program**
> 显示每个套接字的 PID 和程序名

**-r**, **--route**
> 显示内核路由表

**-i**, **--interfaces**
> 显示网络接口表

**-g**, **--groups**
> 显示多播组成员关系

**-s**, **--statistics**
> 显示协议统计信息（SNMP）

**-M**, **--masquerade**
> 显示被伪装的连接

**-c**, **--continuous**
> 每秒刷新一次显示

**-e**, **--extend**
> 显示扩展信息（使用两次可获得更多信息）

**-o**, **--timers**
> 包含网络计时器信息

**-v**, **--verbose**
> 详细输出

**-W**, **--wide**
> 不截断 IP 地址

**-4**
> 仅显示 IPv4

**-6**
> 仅显示 IPv6

**-A** _FAMILY_
> 地址族（inet、inet6、unix、ipx 等）

# DESCRIPTION

**netstat** 显示网络连接、路由表、接口统计信息、伪装连接和多播成员关系。它是一款传统的网络故障排查与监控工具。

不带选项时，netstat 显示打开的套接字。最常见的用法（**netstat -tulnp**）以数字地址形式显示带进程信息的 TCP 和 UDP 监听端口。路由表（**-r**）展示数据包如何被转发，而接口统计信息（**-i**）则显示各网络接口的流量和错误情况。

输出列包括：**Proto**（协议）、**Recv-Q/Send-Q**（排队的数据量）、**Local/Foreign Address**（两端地址）、**State**（连接状态，如 LISTEN、ESTABLISHED、TIME_WAIT），以及可选的 **PID/Program**（占用套接字的进程）。

# CAVEATS

netstat 在 Linux 上已被视为过时；推荐改用性能更好、功能更多的 **ss**。显示进程信息（**-p**）需要 root 权限。名称解析会显著拖慢输出速度；使用 **-n** 可获得更快的结果。部分选项在不同 Unix 实现之间可能有所差异。

# HISTORY

netstat 起源于 20 世纪 80 年代初的 **BSD Unix**，是最初 TCP/IP 实现的一部分。它成为所有类 Unix 系统和 Windows 上的标准网络工具。在 Linux 上，netstat 属于 **net-tools** 软件包，而该软件包如今已被弃用，由 **iproute2** 工具集取代。iproute2 中的 **ss** 命令于 **2001 年**前后推出，它直接从内核数据结构读取信息，以更好的性能提供类似功能。

# INSTALL

```apt: sudo apt install net-tools```

```dnf: sudo dnf install net-tools```

```pacman: sudo pacman -S net-tools```

```apk: sudo apk add net-tools```

```zypper: sudo zypper install net-tools```

```brew: brew install net-tools```

```nix: nix profile install nixpkgs#net-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ss](/man/ss)(8), [ip](/man/ip)(8), [lsof](/man/lsof)(8), [ifconfig](/man/ifconfig)(8)
