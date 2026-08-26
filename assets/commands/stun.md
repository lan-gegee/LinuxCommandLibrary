# TAGLINE

测试 NAT 穿透与外部地址

# TLDR

**测试 NAT 类型**

```stun [stun.example.com]```

**使用指定端口**

```stun -p [3478] [stun.example.com]```

**详细输出**

```stun -v [stun.example.com]```

**绑定本地端口**

```stun -L [54321] [stun.example.com]```

# SYNOPSIS

**stun** [_-p port_] [_-L localport_] [_-v_] _server_

# PARAMETERS

**-p** _PORT_
> 服务器端口。

**-L** _PORT_
> 本地端口。

**-v**
> 详细模式。

**-t**
> TCP 模式。

**-h**
> 显示帮助。

# DESCRIPTION

**stun** 是一个 STUN（Session Traversal Utilities for NAT）客户端，它查询 STUN 服务器来确定 NAT 类型并发现外部地址信息。它向 STUN 服务器发送绑定请求，并分析响应以对客户端所在网络的 NAT 行为进行分类。

该工具可以识别多种 NAT 类型，包括完全锥形、受限锥形、端口受限锥形和对称型 NAT。它还会报告 STUN 服务器所看到的外部 IP 地址和端口映射，这是建立点对点连接的关键信息。

它可用于排查 VoIP 和 SIP 连接问题、诊断 WebRTC 连接失败以及了解网络拓扑。NAT 类型直接影响能否建立点对点连接，其中对称型 NAT 的限制最为严格。

# CAVEATS

需要 STUN 服务器。依赖网络状况。默认使用 UDP。

# HISTORY

**stun** 是一个 STUN（Session Traversal Utilities for NAT）客户端，用于测试 NAT 行为并发现外部地址。

# INSTALL

```apt: sudo apt install stun-client```

```dnf: sudo dnf install stun```

```nix: nix profile install nixpkgs#stun```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pystun3](/man/pystun3)(1), [nmap](/man/nmap)(1), [netcat](/man/netcat)(1)
