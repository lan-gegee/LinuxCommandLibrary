# TAGLINE

NordVPN 服务的命令行界面，提供安全的 VPN 连接

# TLDR

**交互式登录** NordVPN 账户

```nordvpn login```

显示**连接状态**

```nordvpn status```

连接到**最近的 NordVPN 服务器**

```nordvpn connect```

列出所有**可用国家**

```nordvpn countries```

连接到**特定国家**的服务器

```nordvpn connect [Germany]```

连接到**特定国家和城市**的服务器

```nordvpn connect [Germany] [Berlin]```

设置**自动连接选项**

```nordvpn set autoconnect on```

# SYNOPSIS

**nordvpn** _command_ [_options_]

# PARAMETERS

**login**
> 使用 NordVPN 账户进行身份验证

**logout**
> 登出当前账户

**connect, c**
> 连接到 VPN 服务器

**disconnect, d**
> 断开 VPN 连接

**status**
> 显示当前连接状态

**countries**
> 列出可用的服务器所在国家

**cities _country_**
> 列出某个国家可用的城市

**set, s**
> 配置 NordVPN 设置

**settings**
> 显示当前设置

**whitelist**
> 管理白名单端口和子网

# DESCRIPTION

**nordvpn** 是 NordVPN 服务的命令行界面，提供连接全球服务器的安全 VPN。它管理身份验证、服务器连接和客户端设置。

该客户端支持多种连接协议（NordLynx/WireGuard、OpenVPN），以及终止开关、自动连接、拆分隧道等功能。服务器选择可以是自动的（最近/最快）或手动的，按国家、城市或具体服务器选择。

CLI 的运行依赖 NordVPN 守护进程；它通常作为 systemd 服务进行管理。

# CAVEATS

需要有效的 NordVPN 订阅。必须运行 nordvpnd 守护进程（通常通过 systemd 启动）。首次登录会打开浏览器进行身份验证。启用终止开关后，若 VPN 断开将阻止互联网访问。

# INSTALL

```nix: nix profile install nixpkgs#nordvpn```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[openvpn](/man/openvpn)(8), [wg](/man/wg)(8), [nmcli](/man/nmcli)(1)
