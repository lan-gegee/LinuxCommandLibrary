# TAGLINE

导出远程主机的 NTLM 身份验证信息

# TLDR

通过 SMB 从目标主机**导出 NTLM 信息**

```impacket-dumpntlminfo [192.168.1.100]```

使用指定端口**导出 NTLM 信息**

```impacket-dumpntlminfo -port [139] [192.168.1.100]```

使用 RPC 协议代替 SMB **导出 NTLM 信息**

```impacket-dumpntlminfo -protocol RPC [192.168.1.100]```

以指定的目标 IP **导出 NTLM 信息**

```impacket-dumpntlminfo -target-ip [192.168.1.100] [hostname]```

**启用调试输出**以便排查问题

```impacket-dumpntlminfo -debug [192.168.1.100]```

# SYNOPSIS

**impacket-dumpntlminfo** [_-debug_] [_-ts_] [_-target-ip IP_] [_-port PORT_] [_-protocol {SMB,RPC}_] _target_

# PARAMETERS

**-debug**
> 开启 DEBUG 输出。

**-ts**
> 为每条日志输出添加时间戳。

**-target-ip** _IP_
> 目标机器的 IP 地址。当目标是无法解析的 NetBIOS 名称时很有用。

**-port** _PORT_
> 连接 SMB/RPC 服务器的目标端口。默认为 445。

**-protocol** {**SMB**, **RPC**}
> 要使用的协议。默认为 SMB。端口 135 通常使用 RPC。

# DESCRIPTION

**impacket-dumpntlminfo** 对远程主机执行 NTLM 身份验证，并从 NTLM 质询响应中提取信息，且**无需任何凭据**。通过发起 SMB 或 RPC 连接，该工具会触发一次 NTLM 身份验证握手，并解析服务器的响应，从而揭示主机名、域名、DNS 信息、操作系统版本和时间戳等细节。

这在渗透测试侦察阶段非常有用，因为它可以在不进行身份验证的情况下获取网络和主机信息。

# CAVEATS

仅对暴露了 SMB 或 RPC 服务的主机有效。防火墙或安全策略可能会阻止未经身份验证的 NTLM 协商。返回信息的数量取决于目标的 SMB/RPC 配置和 Windows 版本。

# HISTORY

属于 **Impacket** 库，最初由 **SecureAuth**（现为 **Fortra**）开发。Impacket 是一组用于处理网络协议的 Python 类，广泛用于渗透测试和安全研究。该工具利用 NTLM 身份验证握手在无需凭据的情况下提取服务器元数据。

# INSTALL

```pacman: sudo pacman -S impacket```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[impacket-psexec](/man/impacket-psexec)(1), [impacket-smbclient](/man/impacket-smbclient)(1), [impacket-rpcdump](/man/impacket-rpcdump)(1)
