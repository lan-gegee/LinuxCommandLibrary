# TAGLINE

IVPN 服务的命令行客户端

# TLDR

**连接到 VPN**

```ivpn connect```

**连接到指定服务器**

```ivpn connect -c [country_code]```

**断开连接**

```ivpn disconnect```

**显示状态**

```ivpn status```

**列出服务器**

```ivpn servers```

**启用防火墙**

```ivpn firewall -on```

**登录** IVPN 账号

```ivpn login [account_id]```

**连接到最快**的服务器

```ivpn connect -fastest```

# SYNOPSIS

**ivpn** _command_ [_options_]

# PARAMETERS

**connect**
> 连接到 VPN。

**disconnect**
> 断开 VPN 连接。

**status**
> 显示连接状态。

**servers**
> 列出可用服务器。

**firewall** _STATE_
> 控制 IVPN 防火墙（-on、-off）。

**-c** _COUNTRY_
> 服务器的国家代码。

**-fastest**
> 连接到最快的服务器。

**login** _ACCOUNT_ID_
> 使用 IVPN 账号进行身份验证。

**logout**
> 从 IVPN 账号登出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**ivpn** 是 IVPN 服务的命令行客户端。它以注重隐私为特色来管理 VPN 连接。

该工具支持 WireGuard 和 OpenVPN 协议。它内置防火墙以防止泄露。

# CAVEATS

需要 IVPN 订阅。守护进程必须正在运行。提供商以隐私为重点。

# HISTORY

ivpn CLI 是 **IVPN** 的官方客户端，IVPN 是一家总部位于直布罗陀、注重隐私的 VPN 服务商。

# INSTALL

```nix: nix profile install nixpkgs#ivpn```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wg](/man/wg)(1), [openvpn](/man/openvpn)(8)
