# TAGLINE

第四层路由追踪（Layer Four Traceroute）

# TLDR

**对主机进行路由追踪**

```lft [hostname]```

**使用指定端口**

```lft -d [80] [hostname]```

**TCP 模式**

```lft -T [hostname]```

**UDP 模式**

```lft -U [hostname]```

**显示 ASN 信息**

```lft -A [hostname]```

**设置最大 TTL**

```lft -m [30] [hostname]```

# SYNOPSIS

**lft** [_options_] _host_

# PARAMETERS

_HOST_
> 目标主机名或 IP 地址。

**-d** _PORT_
> 目标端口。

**-T**
> TCP 模式。

**-U**
> UDP 模式。

**-A**
> 显示 AS 号。

**-m** _TTL_
> 最大 TTL。

**-n**
> 不做 DNS 解析。

**--help**
> 显示帮助信息。

# DESCRIPTION

**lft** 即第四层路由追踪（Layer Four Traceroute）。它在第 4 层使用 TCP、UDP 或 ICMP 进行路由追踪。

该工具能够绕过许多屏蔽 ICMP 的防火墙。它还可以显示 AS 号，方便进行网络分析。

# CAVEATS

可能需要 root 权限。对防火墙友好。属于网络诊断工具。

# HISTORY

LFT 由 **Victor Oppleman** 创建，作为传统 traceroute 的防火墙友好替代方案。

# INSTALL

```apt: sudo apt install lft```

```brew: brew install lft```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[traceroute](/man/traceroute)(1), [mtr](/man/mtr)(1), [tcptraceroute](/man/tcptraceroute)(1)
