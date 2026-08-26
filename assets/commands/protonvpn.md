# TAGLINE

Proton VPN 官方命令行客户端

# TLDR

**登录** Proton VPN

```protonvpn signin [username]```

**登出**

```protonvpn signout```

**连接**到最快的服务器

```protonvpn connect```

连接到**特定国家**

```protonvpn connect --country [US]```

连接到**指定名称的服务器**

```protonvpn connect [US-NY-01]```

**断开连接**

```protonvpn disconnect```

**启用 kill switch**

```protonvpn config set kill-switch on```

**列出可配置的选项**

```protonvpn config list```

# SYNOPSIS

**protonvpn** [**signin**|**signout**|**connect**|**disconnect**|**info**|**status**]

# COMMANDS

**signin** [_username_]
> 使用 Proton VPN 凭据进行身份验证。

**signout**
> 移除存储的凭据。

**connect** [_server_]
> 建立 VPN 连接。不带参数时连接到可用的最快服务器。可接受服务器名称，或配合 **--country** / **--city** 使用。

**disconnect**
> 终止当前活动的 VPN 连接。

**status**
> 显示当前连接状态。

**info**
> 显示账户信息。

**config list**
> 列出可配置的选项。

**config set** _option_ _value_
> 更改配置选项（例如 **kill-switch on**、**netshield f1**、**vpn-accelerator on**）。

# PARAMETERS

**--country** _CODE_
> 将 **connect** 限制为特定国家的服务器。

**--city** _CITY_
> 将 **connect** 限制为特定城市的服务器。

**--protocol** _PROTOCOL_
> 覆盖连接协议（例如 _wireguard_、_openvpn-tcp_、_openvpn-udp_）。

**-h, --help**
> 显示帮助信息。

# DESCRIPTION

**protonvpn** 是 Proton VPN 服务的官方命令行客户端。它提供安全加密的 VPN 连接，支持 kill switch、拆分隧道和服务器选择等功能。

该 CLI 支持以脚本方式管理 VPN 连接，并为无界面服务器或终端用户提供图形客户端的全部功能。

# CAVEATS

需要 Proton VPN 订阅。某些功能需要付费套餐。NetworkManager 集成情况因发行版而异。某些操作可能需要 root 权限。

# HISTORY

**protonvpn** CLI 由 **Proton AG** 开发，是其图形 VPN 客户端的补充。Proton VPN 强调隐私，总部位于隐私法律严格的瑞士。

# SEE ALSO

[openvpn](/man/openvpn)(8), [wg-quick](/man/wg-quick)(8), [nmcli](/man/nmcli)(1)
