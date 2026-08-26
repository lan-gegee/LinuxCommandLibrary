# TAGLINE

Mozilla 的 VPN 客户端

# TLDR

**连接 VPN**

```mozillavpn activate```

**断开 VPN**

```mozillavpn deactivate```

**查看连接状态**

```mozillavpn status```

**选择服务器位置**

```mozillavpn select [us-ny]```

**列出可用服务器**

```mozillavpn servers```

**登录账户**

```mozillavpn login```

# SYNOPSIS

**mozillavpn** [_command_] [_options_]

# PARAMETERS

_COMMAND_
> 要执行的操作。

**activate**
> 连接 VPN。

**deactivate**
> 断开 VPN。

**status**
> 显示连接状态。

**select** _SERVER_
> 选择服务器位置。

**servers**
> 列出可用服务器。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mozillavpn** 是 Mozilla 的 VPN 客户端。它通过 WireGuard 协议提供安全的网络连接。

该工具会加密互联网流量，提供全球多个服务器位置可选。

# CAVEATS

需要订阅。依赖 WireGuard 内核模块。最多支持 5 台设备。

# HISTORY

mozillavpn 由 **Mozilla** 于 2020 年推出，是一项使用 WireGuard 技术的隐私优先 VPN 服务。

# INSTALL

```nix: nix profile install nixpkgs#mozillavpn```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wg](/man/wg)(1), [openvpn](/man/openvpn)(1)
