# TAGLINE

基于 Impacket 库、使用原始套接字的 ICMPv6 ping 实现

# TLDR

向目标**发送 ICMPv6 回显请求**

```impacket-ping6 [2001:db8::1]```

**以指定源地址 ping IPv6 地址**

```impacket-ping6 -src [2001:db8::50] [2001:db8::1]```

# SYNOPSIS

**impacket-ping6** [_-h_] [_-src IP_] _target_

# PARAMETERS

**-src** _IP_
> 用于 ping 数据包的源 IPv6 地址

# DESCRIPTION

**impacket-ping6** 是一个 ICMPv6 ping 实现，通过 Impacket 库使用原始套接字。它向指定的 IPv6 目标发送 ICMPv6 回显请求包，并报告响应。

该工具利用 Impacket 的原始套接字能力提供 IPv6 ping 功能，适用于安全测试场景中的 IPv6 连通性测试。

# CAVEATS

创建原始套接字需要 root/管理员权限。目标必须是 IPv6 地址。可能被过滤 ICMPv6 流量的防火墙拦截。对大多数场景而言，标准的 **ping6** 或 **ping -6** 命令功能更完善。

# HISTORY

属于 SecureAuth 的 **Impacket** 库，为使用 IPv6 网络的环境提供 impacket-ping 的 IPv6 对应版本。

# INSTALL

```pacman: sudo pacman -S impacket```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ping](/man/ping)(1), [impacket-ping](/man/impacket-ping)(1), [ping6](/man/ping6)(1)
