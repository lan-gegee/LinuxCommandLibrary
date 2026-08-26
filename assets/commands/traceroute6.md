# TAGLINE

追踪到主机的 IPv6 数据包路由

# TLDR

**追踪到 IPv6 主机的路由**

```traceroute6 [host]```

以纯数字输出**追踪**（不做 DNS 解析）

```traceroute6 -n [host]```

**设置最大跳数限制**

```traceroute6 -m [60] [host]```

**从指定跳开始**

```traceroute6 -f [5] [host]```

**使用 ICMP ECHO 代替 UDP**

```traceroute6 -I [host]```

**设置每跳的探测次数**

```traceroute6 -q [5] [host]```

**指定源地址**

```traceroute6 -s [source_address] [host]```

# SYNOPSIS

**traceroute6** [_-dIlnNrvU_] [_-f firsthop_] [_-g gateway_] [_-m hoplimit_] [_-p port_] [_-q probes_] [_-s src_] [_-w waittime_] _target_ [_datalen_]

# PARAMETERS

**-n**
> 不将地址解析为主机名

**-m** _hoplimit_
> 最大跳数限制（默认：30，上限：255）

**-f** _firsthop_
> 从指定跳开始探测（跳过更早的跳）

**-I**
> 使用 ICMPv6 ECHO 代替 UDP 数据报

**-N**
> 使用不带上层报头的数据包

**-p** _port_
> 设置目的 UDP 端口

**-q** _probes_
> 每跳的探测次数（默认：3）

**-s** _src_
> 使用指定的源地址

**-w** _waittime_
> 等待响应的时间（秒）

**-g** _gateway_
> 指定中间网关（使用路由报头）

# DESCRIPTION

**traceroute6** 追踪 IPv6 数据包到达目标主机所经过的路由。它利用 IPv6 的跳数字段，发送跳数限制递增的探测包，诱使路径上的每台路由器返回 ICMPv6 TIME_EXCEEDED 响应。

输出的每一行显示跳数、网关地址（除非使用了 **-n**，否则还包括主机名）以及每次探测的往返时间。追踪会持续进行，直到目标响应或达到最大跳数限制为止。

该命令等同于 **traceroute -6**，默认发送 UDP 数据报。如需改用 ICMPv6 ECHO 探测，请使用 **-I**。

# CAVEATS

在 Linux 上需要 CAP_NET_RAW 能力或 root 权限。某些路由器可能不响应探测，在输出中显示为 * * *。防火墙可能拦截 traceroute 探测。各次探测之间的响应时间可能差异很大。

# HISTORY

traceroute 最初由 **Van Jacobson** 于 **1988 年**编写。IPv6 版本于 **1996 年**从 NRL 的 IPv6 发行版移植而来，后由 Pedro Roque 移植到 Linux。

# SEE ALSO

[traceroute](/man/traceroute)(1), [ping6](/man/ping6)(8), [mtr](/man/mtr)(8), [tracepath](/man/tracepath)(8)
