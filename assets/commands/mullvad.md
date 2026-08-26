# TAGLINE

Mullvad VPN（注重隐私的 VPN 服务）的命令行界面

# TLDR

**连接 VPN**

```mullvad connect```

**断开 VPN**

```mullvad disconnect```

**检查连接状态**

```mullvad status```

**设置 VPN 服务器位置**

```mullvad relay set location [us] [nyc]```

**列出可用位置**

```mullvad relay list```

**启用开机自动连接**

```mullvad auto-connect set on```

**启用 kill switch**

```mullvad lockdown-mode set on```

**检查账户状态**

```mullvad account get```

# SYNOPSIS

**mullvad** _command_ [_subcommand_] [_options_]

# PARAMETERS

**connect**
> 建立 VPN 连接。

**disconnect**
> 关闭 VPN 连接。

**reconnect**
> 重新连接 VPN。

**status**
> 显示当前连接状态。

**account** _subcommand_
> 管理账户（login、logout、get、set）。

**relay** _subcommand_
> 配置中继/服务器选择。

**tunnel** _subcommand_
> 配置隧道协议选项。

**dns** _subcommand_
> 配置 DNS 设置。

**lockdown-mode** _subcommand_
> 配置 kill switch（阻止非 VPN 流量）。

**auto-connect** _subcommand_
> 配置启动时自动连接。

**lan** _subcommand_
> 允许/阻止本地网络访问。

**obfuscation** _subcommand_
> 配置流量混淆。

**split-tunnel** _subcommand_
> 将应用程序排除在 VPN 隧道之外。

**bridge** _subcommand_
> 为受审查网络配置桥接模式。

**version**
> 显示版本信息。

# DESCRIPTION

**mullvad** 是 Mullvad VPN 的命令行界面，后者是一家总部位于瑞典、注重隐私的 VPN 服务商。它通过控制 Mullvad 守护进程来管理 VPN 连接和配置。

该客户端支持 WireGuard 和 OpenVPN 协议。WireGuard 是默认选项，且因性能更佳而受到推荐。服务器选择可以是自动的，也可以按国家、城市或特定服务器手动设置。中继列表显示所有可用的端点。

封锁模式（kill switch）会在 VPN 断开时阻断所有互联网流量，防止泄露。可以允许 LAN 访问以使用本地网络资源。拆分隧道可将特定应用程序排除在 VPN 隧道之外。

DNS 选项包括使用 Mullvad 的 DNS、自定义服务器，或通过其 DNS 屏蔽广告/跟踪器/恶意软件。流量混淆有助于绕过受审查网络中的 VPN 封锁。

账户系统使用编号令牌而非电子邮件/密码。匿名支付方式包括现金和加密货币。

# CAVEATS

需要 Mullvad 订阅。守护进程必须正在运行（mullvad-daemon 服务）。部分功能需要 root 权限。拆分隧道支持因平台而异。WireGuard 在 Linux 上需要内核模块。Kill switch 可能干扰本地服务。请妥善保管账户令牌。

# HISTORY

**Mullvad** 由 Amagicom AB 于 **2009 年**在瑞典创立，从一开始就专注于隐私。CLI 工具与其桌面客户端同步演进。Mullvad 因率先支持 WireGuard VPN 和匿名账户系统而备受关注。**2022 年**，瑞典警方曾试图查扣其服务器，但由于其无日志政策而未发现任何用户数据。该服务已接受过多次独立审计。

# INSTALL

```nix: nix profile install nixpkgs#mullvad```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wg](/man/wg)(1), [openvpn](/man/openvpn)(1), [nordvpn](/man/nordvpn)(1)
