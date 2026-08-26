# TAGLINE

灵活的数据包生成与响应分析工具

# TLDR

**对端口进行 TCP ping**

```nping --tcp -p [80] [target]```

**UDP ping**

```nping --udp -p [53] [target]```

**ICMP echo ping**

```nping --icmp [target]```

**发送多个数据包**

```nping -c [5] [target]```

**设置发包速率**

```nping --rate [10] [target]```

**TCP SYN 数据包**

```nping --tcp --flags syn -p [22] [target]```

**ARP ping**（局域网）

```nping --arp [192.168.1.0/24]```

**路由追踪模式**

```nping --traceroute [target]```

# SYNOPSIS

**nping** [_--tcp_] [_--udp_] [_--icmp_] [_-p port_] [_-c count_] [_options_] _targets_

# PARAMETERS

**--tcp**
> TCP 模式。

**--udp**
> UDP 模式。

**--icmp**
> ICMP 模式。

**--arp**
> ARP 模式。

**-p** _PORT_
> 目标端口。

**-c** _COUNT_
> 数据包数量。

**--rate** _RATE_
> 每秒发送的数据包数。

**--flags** _FLAGS_
> TCP 标志（syn、ack、rst 等）。

**--ttl** _TTL_
> IP 生存时间。

**--data-length** _LEN_
> 追加随机数据。

**--data-string** _STR_
> 追加字符串数据。

**--traceroute**
> 路由追踪模式。

**-e** _IFACE_
> 网络接口。

**-S** _ADDR_
> 源地址。

**--echo-client** _PASS_
> 回显模式客户端。

**--echo-server** _PASS_
> 回显模式服务器。

# DESCRIPTION

**nping** 是一个灵活的数据包生成与响应分析工具，将 ping 的功能扩展到任意协议组合。

TCP 模式探测端口而不完成连接。SYN 数据包可用于测试防火墙规则和服务可用性。自定义标志组合可测试 TCP 协议栈的行为。

UDP 探测用于测试 UDP 服务。ICMP 除回显请求外还包含多种消息类型。ARP 查询用于解析局域网内的 MAC 地址。

回显模式让数据包经由服务器反弹，可用于测试防火墙和 NAT 穿越。客户端把数据包发给服务器，再由服务器返回。

路由追踪模式通过递增 TTL 值来发现网络路径，支持 TCP、UDP 或 ICMP 探测。

数据包定制包括载荷数据、时序和协议选项，从而支持协议研究和网络测试。

# CAVEATS

原始套接字需要 root 权限。某些模式可能触发入侵检测系统（IDS）告警。仅在获得授权的网络上使用。结果取决于防火墙配置。

# HISTORY

**nping** 由 **Gordon Lyon**（Fyodor）及贡献者作为 **Nmap** 项目的一部分开发，以主动探测能力补充 Nmap 的端口扫描功能。

# INSTALL

```apt: sudo apt install nmap```

```dnf: sudo dnf install nmap```

```pacman: sudo pacman -S nmap```

```apk: sudo apk add nmap-nping```

```brew: brew install nmap```

```nix: nix profile install nixpkgs#nmap```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nmap](/man/nmap)(1), [hping3](/man/hping3)(8), [ping](/man/ping)(1), [traceroute](/man/traceroute)(1)
