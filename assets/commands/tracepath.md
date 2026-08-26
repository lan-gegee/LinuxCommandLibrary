# TAGLINE

追踪网络路径并发现 MTU

# TLDR

**追踪**到主机的路径并发现 MTU

```tracepath -p 33434 [host]```

使用指定目的端口**追踪**

```tracepath -p [port] [host]```

同时**输出**主机名和 IP 地址

```tracepath -b [host]```

**指定**最大 TTL（跳数）

```tracepath -m [max_hops] [host]```

**指定**初始数据包长度

```tracepath -l [packet_length] [host]```

只**使用** IPv6 地址

```tracepath -6 [host]```

# SYNOPSIS

**tracepath** [_options_] _host_

# PARAMETERS

**-p _port_**
> 设置初始目的端口

**-b**
> 同时输出主机名和数字 IP 地址

**-m _max_hops_**
> 设置最大跳数（TTL）

**-l _length_**
> 设置初始数据包长度

**-4**
> 只使用 IPv4

**-6**
> 只使用 IPv6

**-n**
> 只输出数字地址

# DESCRIPTION

**tracepath** 追踪到网络主机的路径，并沿路径发现 MTU（最大传输单元）。与 traceroute 不同，它不需要超级用户权限，并且能够检测路径 MTU。

输出会显示每一跳及其 RTT 和 MTU 信息。

# CAVEATS

在封锁 UDP 数据包的防火墙后可能无法工作。结果可能因网络状况和防火墙规则而异。是 iputils 软件包的组成部分。

# INSTALL

```apt: sudo apt install iputils-tracepath```

```apk: sudo apk add iputils-tracepath```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[traceroute](/man/traceroute)(8), [ping](/man/ping)(8), [mtr](/man/mtr)(8)
