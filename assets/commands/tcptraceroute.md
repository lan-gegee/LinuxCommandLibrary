# TAGLINE

使用 TCP 数据包的 traceroute

# TLDR

对主机进行**路由跟踪**

```tcptraceroute host```

跟踪到指定**目标端口**

```tcptraceroute host 80```

指定**源端口**和地址

```tcptraceroute host -p 12345 -s 192.168.1.10```

设置**初始和最大 TTL**

```tcptraceroute host -f 1 -m 30```

设置**等待时间**和每跳查询次数

```tcptraceroute host -w 3 -q 3```

指定**网络接口**

```tcptraceroute host -i eth0```

仅使用**数字**输出

```tcptraceroute -n host```

# SYNOPSIS

**tcptraceroute** [_options_] _host_ [_destination_port_] [_packet_length_]

# DESCRIPTION

**tcptraceroute** 是一种使用 TCP 数据包的 traceroute 实现。它通过向指定端口发送 TCP SYN 包，可以穿透封锁传统 ICMP 或 UDP traceroute 数据包的防火墙完成路由跟踪。

# PARAMETERS

**-p PORT**
> 设置本地源端口

**-s ADDRESS**
> 设置源 IP 地址

**-i INTERFACE**
> 指定使用的网络接口

**-f TTL**
> 设置初始（第一个）TTL 值

**-m TTL**
> 设置最大 TTL 值（默认为 30）

**-w SECONDS**
> 设置每个探测的超时时间（默认为 3）

**-q QUERIES**
> 设置每跳的查询次数（默认为 3）

**-n**
> 仅打印数字地址（不做 DNS 解析）

**-N**
> 启用主机名查询

**-S**
> 在发出的数据包上设置 SYN 标志

**-A**
> 在发出的数据包上设置 ACK 标志

**-E**
> 在发出的数据包上设置 ECN 标志

# CAVEATS

发送原始数据包需要 root 权限或相应的能力。目标端口默认为 80（HTTP）。某些防火墙仍可能根据自身配置阻止 TCP 探测。

# HISTORY

**tcptraceroute** 作为传统 traceroute 的替代方案而创建，通过使用 TCP SYN 包绕过封锁 ICMP 和 UDP 数据包的防火墙。

# INSTALL

```apk: sudo apk add tcptraceroute```

```brew: brew install tcptraceroute```

```nix: nix profile install nixpkgs#tcptraceroute```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[traceroute](/man/traceroute)(8), [mtr](/man/mtr)(8), [tracepath](/man/tracepath)(8)
