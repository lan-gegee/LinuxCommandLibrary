# TAGLINE

用于构造 TCP/IP 数据包的网络工具

# TLDR

**TCP SYN ping**

```sudo hping3 -S -p [80] [target]```

**ICMP ping**

```sudo hping3 -1 [target]```

**UDP ping**

```sudo hping3 -2 -p [53] [target]```

**traceroute 模式**

```sudo hping3 --traceroute -p [80] -S [target]```

**洪水模式**

```sudo hping3 --flood -S -p [80] [target]```

**设置源端口**

```sudo hping3 -S -p [80] -s [12345] [target]```

**扫描一段端口范围**

```sudo hping3 -8 [1-1000] -S [target]```

# SYNOPSIS

**hping3** [_options_] _host_

# PARAMETERS

**-S**, **--syn**
> 设置 SYN 标志。

**-A**, **--ack**
> 设置 ACK 标志。

**-F**, **--fin**
> 设置 FIN 标志。

**-p** _port_
> 目标端口。

**-s** _port_
> 源端口。

**-1**, **--icmp**
> ICMP 模式。

**-2**, **--udp**
> UDP 模式。

**-8**, **--scan** _range_
> 端口扫描模式，例如 `-8 1-1000`。

**-V**, **--verbose**
> 详细输出。

**--flood**
> 洪水模式（尽可能快地发送）。

**--traceroute**
> traceroute 模式。

**-i** _interval_
> 数据包之间的间隔。

**-c** _count_
> 数据包数量。

**-a** _address_
> 伪造源地址。

**--data** _size_
> 数据大小。

# DESCRIPTION

**hping3** 是一个用于构造 TCP/IP 数据包的网络工具。它可用于防火墙测试、端口扫描、网络测试和安全审计。它比 ping 或 traceroute 提供更多控制能力。

hping3 可以发送带有指定标志、选项和载荷的自定义数据包，因此在渗透测试和故障排查中很有价值。未指定协议模式时，它默认使用 **TCP 模式**，向目标的 0 端口发送不设任何标志的报文头。

# CAVEATS

需要 root 权限。洪水模式可能造成 DoS。伪造数据包可能违法。仅限授权测试。某些功能可能触发 IDS。

# HISTORY

hping 由 **Salvatore Sanfilippo**（antirez，也是 Redis 的作者）创建。hping3 是最新版本，增加了脚本能力和改进的功能。

# INSTALL

```apt: sudo apt install hping3```

```dnf: sudo dnf install hping3```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hping](/man/hping)(8), [nmap](/man/nmap)(1), [ping](/man/ping)(8), [tcpdump](/man/tcpdump)(1), [scapy](/man/scapy)(1)

# RESOURCES

```[Source code](https://github.com/antirez/hping)```

<!-- verified: 2026-07-19 -->
