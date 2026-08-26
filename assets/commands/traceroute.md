# TAGLINE

追踪到网络主机的数据包路由

# TLDR

**追踪到主机的路由**

```traceroute [host]```

使用 **ICMP 回显**代替 UDP

```traceroute -I [host]```

使用 **TCP SYN** 进行探测

```sudo traceroute -T [host]```

**设置最大跳数**

```traceroute -m [20] [host]```

**设置每跳的探测次数**

```traceroute -q [1] [host]```

**使用指定端口**

```traceroute -p [80] [host]```

**强制使用 IPv4 或 IPv6**

```traceroute -4 [host]```

**不解析主机名**

```traceroute -n [host]```

# SYNOPSIS

**traceroute** [_options_] _host_ [_packet_size_]

# PARAMETERS

**-4**, **-6**
> 强制使用 IPv4 或 IPv6

**-I**
> 使用 ICMP ECHO 进行探测

**-T**
> 使用 TCP SYN 进行探测（需要 root）

**-U**
> 使用 UDP 数据报（默认）

**-m** _MAX_
> 最大跳数（默认：30）

**-q** _NQUERIES_
> 每跳的探测次数（默认：3）

**-w** _WAIT_
> 等待响应的时间（秒）（默认：5.0）

**-p** _PORT_
> 目的端口（UDP 基础端口或 TCP 目的端口）

**-n**
> 不将 IP 地址解析为主机名

**-N** _NUM_
> 同时进行的探测数（默认：16）

**-f** _FIRST_
> 从指定的 TTL 开始（默认：1）

**-F**
> 设置 "Don't Fragment"（不分片）位

**-i** _INTERFACE_
> 指定网络接口

**-s** _SOURCE_
> 使用指定的源地址

**-z** _PAUSE_
> 探测之间的停顿（秒；大于 10 时按毫秒计）

**-A**
> 执行 AS 路径查询

**--mtu**
> 沿路径发现 MTU

**-V**
> 显示版本

# DESCRIPTION

**traceroute** 显示数据包到达网络主机所经过的路由。它发送 TTL（生存时间）值递增的探测包，使路径上的每台路由器返回 ICMP "time exceeded"（超时）消息，从而暴露其地址。

每一行显示跳数、路由器主机名/IP 以及每次探测的往返时间（默认：3 次）。星号（*）表示在超时时间内没有响应——原因可能是防火墙、速率限制或丢包。

不同的探测方法在不同网络中效果不同：ICMP（**-I**）可能被防火墙拦截，TCP（**-T**）可以到达封锁其他探测方式的主机，而 UDP（默认）可供无特权用户使用但可能被过滤。

# CAVEATS

许多网络会过滤 ICMP 或 UDP traceroute 数据包。非对称路由意味着返回路径可能与所显示的正向路径不同。响应时间包含每一跳的处理延迟，而不仅仅是传输时间。某些路由器不递减 TTL 或不响应探测。TCP 模式需要 root 权限。

# HISTORY

traceroute 由 **Van Jacobson** 于 **1987 年**在劳伦斯伯克利实验室编写。它已成为必不可少的网络诊断工具，几乎所有类 Unix 系统都有收录。这一思路利用了 TTL 字段防止路由循环的原始用途。变体包括 **tracepath**（无需 root）、**mtr**（结合了 ping 和 traceroute）以及 Windows 的 **tracert**。

# INSTALL

```dnf: sudo dnf install traceroute```

```pacman: sudo pacman -S traceroute```

```apk: sudo apk add traceroute```

```zypper: sudo zypper install traceroute```

```nix: nix profile install nixpkgs#traceroute```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ping](/man/ping)(8), [mtr](/man/mtr)(8), [tracepath](/man/tracepath)(8), [netstat](/man/netstat)(8)
