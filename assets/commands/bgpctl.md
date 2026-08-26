# TAGLINE

控制和查询 OpenBGPD 路由守护进程

# TLDR

**显示 BGP 摘要**（邻居状态）

```bgpctl show summary```

**显示所有 BGP 邻居**

```bgpctl show neighbor```

**显示 RIB**（路由信息库）

```bgpctl show rib```

**显示来自指定邻居的路由**

```bgpctl show rib neighbor [192.168.1.1]```

**显示指定前缀的路由**

```bgpctl show rib [10.0.0.0/8]```

**软重置邻居**会话

```bgpctl neighbor [192.168.1.1] refresh```

**清除邻居**会话

```bgpctl neighbor [192.168.1.1] clear```

**显示 BGP network 声明**

```bgpctl show network```

# SYNOPSIS

**bgpctl** [**-n**] [**-s** _socket_] _command_ [_arguments_]

# DESCRIPTION

**bgpctl** 是 OpenBGPD（边界网关协议版本 4 的一个实现）的控制程序。它与运行中的 bgpd 守护进程通信，以显示路由信息并控制 BGP 会话。

该命令可查看 BGP 路由信息库（RIB）、邻居会话状态，并允许执行管理操作，如重置会话或注入路由。它通过 Unix 套接字连接到 bgpd。

bgpctl 是 OpenBGPD 项目的一部分，该项目起源于 OpenBSD，已被移植到其他操作系统。

# PARAMETERS

**show summary**
> 显示邻居状态概览。

**show neighbor** [_peer_]
> 显示详细的邻居信息。

**show rib** [_options_]
> 显示路由信息库。

**show network**
> 显示已配置的 network 声明。

**show fib** [_options_]
> 显示转发信息库。

**neighbor** _peer_ **up**
> 启动邻居会话。

**neighbor** _peer_ **down**
> 关闭邻居会话。

**neighbor** _peer_ **clear**
> 清除并重置会话。

**neighbor** _peer_ **refresh**
> 请求路由刷新。

**network add** _prefix_
> 添加要通告的网络。

**network delete** _prefix_
> 移除网络通告。

**-n**
> 显示 IP 地址而不是名称。

**-s** _socket_
> 连接到备用的控制套接字。

# CAVEATS

需要适当的权限才能访问 bgpd 控制套接字。某些命令可能中断 BGP 会话并导致路由变化。clear 命令会拆除 TCP 会话，而 refresh 执行的是软重置。路由变化可能需要时间才能在整个网络中传播。

# HISTORY

**bgpctl** 是 **OpenBGPD** 的一部分，后者由 Henning Brauer 和 Claudio Jeker 自 **2003 年**起为 **OpenBSD** 开发。在对其他 BGP 实现的安全性产生担忧之后，它被设计为一个干净、安全的 BGP 实现。面向 Linux 和其他系统的可移植版本自 **2016 年**起可用。OpenBGPD 以简洁和对安全的专注而闻名。

# INSTALL

```apt: sudo apt install openbgpd```

```dnf: sudo dnf install openbgpd```

```apk: sudo apk add openbgpd```

```nix: nix profile install nixpkgs#openbgpd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bgpd](/man/bgpd)(8), [vtysh](/man/vtysh)(1)
