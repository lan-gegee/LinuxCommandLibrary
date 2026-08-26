# TAGLINE

向 IPv6 主机发送 ICMPv6 回显请求

# TLDR

**ping IPv6 地址**

```ping6 [2001:db8::1]```

**ping 主机名**

```ping6 [ipv6.example.com]```

**限制数据包数量**

```ping6 -c [5] [host]```

**设置间隔**

```ping6 -i [2] [host]```

**设置数据包大小**

```ping6 -s [1000] [host]```

**泛洪 ping**

```ping6 -f [host]```

**静默输出**

```ping6 -q -c [10] [host]```

**指定接口**

```ping6 -I [eth0] [fe80::1]```

# SYNOPSIS

**ping6** [_-c count_] [_-i interval_] [_-s size_] [_-I interface_] [_options_] _destination_

# PARAMETERS

**-c** _COUNT_
> 发送 count 个数据包后停止。

**-i** _INTERVAL_
> 数据包之间的间隔秒数。

**-s** _SIZE_
> 数据包数据大小。

**-I** _INTERFACE_
> 源接口。

**-q**
> 静默输出。

**-f**
> 泛洪模式。

**-t** _TTL_
> 存活时间（TTL）。

**-w** _DEADLINE_
> 超时时间，单位秒。

# DESCRIPTION

**ping6** 向 IPv6 主机发送 ICMPv6 回显请求。它测试网络连通性并测量延迟。

链路本地地址需要指定接口。-I 选项绑定到特定的网络接口。

统计信息显示丢包率和往返时间。报告最小、平均和最大延迟。

泛洪模式测试负载下的网络状况。需要 root 权限。

许多系统现在用 ping 同时处理 IPv4 和 IPv6。独立的 ping6 命令仅为兼容性保留。

# CAVEATS

防火墙可能拦截 ICMPv6。链路本地地址需要指定接口。泛洪 ping 需要 root 权限。

# HISTORY

**ping6** 随 **20 世纪 90 年代**的 IPv6 实现而出现。在许多现代系统上，**ping** 命令同时处理两种协议，ping6 只是兼容性别名。

# INSTALL

```apt: sudo apt install iputils-ping```

```apk: sudo apk add iputils-ping```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ping](/man/ping)(1), [traceroute6](/man/traceroute6)(1), [ip](/man/ip)(8)
