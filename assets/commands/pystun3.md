# TAGLINE

使用 STUN 协议探测 NAT 类型

# TLDR

**检查 NAT 类型**

```pystun3```

**使用指定 STUN 服务器**

```pystun3 -H [stun.example.com]```

**指定源端口**

```pystun3 -p [54320]```

**使用指定网络接口**

```pystun3 -i [192.168.1.100]```

**启用调试日志**

```pystun3 -d```

**指定 STUN 服务器端口**

```pystun3 -H [stun.example.com] -P [3478]```

# SYNOPSIS

**pystun3** [_-H server_] [_-p port_] [_-i ip_] [_options_]

# PARAMETERS

**-H** _STUN_HOST_, **--host** _STUN_HOST_
> STUN 服务器主机名。

**-P** _STUN_PORT_, **--host-port** _STUN_PORT_
> STUN 服务器端口（默认：3478）。

**-p** _SOURCE_PORT_, **--port** _SOURCE_PORT_
> 要监听的源端口（默认：54320）。

**-i** _SOURCE_IP_, **--interface** _SOURCE_IP_
> 客户端使用的网络接口（默认：0.0.0.0）。

**-d**, **--debug**
> 启用调试日志。

**--version**
> 显示程序版本。

# DESCRIPTION

**pystun3** 是一个 STUN（Session Traversal Utilities for NAT）客户端，用于发现主机与互联网之间的 NAT 类型。它与 STUN 服务器通信以判定 NAT 分类（完全锥形、受限锥形、端口受限或对称型），并报告外部 IP 地址和映射端口。

了解 NAT 类型对配置 VoIP、视频会议以及需要主机间直连的对等应用至关重要。该工具可指定 STUN 服务器并绑定到特定网络接口。

# CAVEATS

需要网络访问。STUN 服务器必须可达。NAT 类型各有差异。

# HISTORY

**pystun3** 是 pystun 的 Python 3 移植版，实现 STUN（Session Traversal Utilities for NAT）客户端功能。

# SEE ALSO

[stun](/man/stun)(1), [nmap](/man/nmap)(1), [netcat](/man/netcat)(1)
