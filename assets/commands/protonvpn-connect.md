# TAGLINE

建立 Proton VPN 连接

# TLDR

**连接到可用的最快服务器**

```protonvpn connect --fastest```

**连接到指定国家最快的服务器**

```protonvpn connect --cc [US]```

**连接到特定服务器**

```protonvpn connect [server_name]```

**连接到最快的 P2P 服务器**

```protonvpn connect --p2p```

**连接到最快的 Secure Core 服务器**

```protonvpn connect --sc```

**使用 TCP 协议连接**

```protonvpn connect --fastest -p tcp```

# SYNOPSIS

**protonvpn connect** [_options_] [_server_]

# PARAMETERS

**--fastest**
> 连接到可用的最快服务器。

**--random**
> 连接到随机服务器。

**--cc** _CODE_
> 连接到指定国家最快的服务器。

**--p2p**
> 连接到最快的 P2P 服务器。

**--sc**
> 连接到最快的 Secure Core 服务器。

**-p** _PROTOCOL_
> 指定传输协议（udp 或 tcp）。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**protonvpn connect** 建立到 Proton VPN 服务的连接。它可以自动选择可用的最快服务器，或连接到特定的服务器、国家或城市。

该命令是 Linux 版 Proton VPN CLI 工具的一部分，通过 Proton 网络提供安全的 VPN 连接。

# CAVEATS

需要有效的 Proton VPN 订阅，并已事先通过 `protonvpn login` 完成身份验证。网络配置可能需要 root 权限。

# HISTORY

属于 **Proton VPN** 的 Linux CLI 客户端，由 Proton AG 开发，用于通过其 VPN 基础设施安全地访问互联网。

# SEE ALSO

[protonvpn](/man/protonvpn)(1), [openvpn](/man/openvpn)(8)
