# TAGLINE

面向 Linux 的新一代 OpenVPN 客户端，提供基于 D-Bus 的架构

# TLDR

**启动**新的 VPN 会话

```openvpn3 session-start -c [path/to/config.conf]```

**列出**已建立的会话

```openvpn3 sessions-list```

**断开**当前已建立的会话

```openvpn3 session-manage -c [path/to/config.conf] -D```

**导入** VPN 配置

```openvpn3 config-import -c [path/to/config.conf]```

**列出**已导入的配置

```openvpn3 configs-list```

# SYNOPSIS

**openvpn3** _command_ [_options_]

# PARAMETERS

**session-start** **-c** _config_
> 使用指定的配置启动新的 VPN 会话

**session-manage** **-c** _config_ **-D**
> 管理活动会话（断开连接）

**sessions-list**
> 列出所有活动的 VPN 会话

**config-import** **-c** _config_
> 将 VPN 配置文件导入配置管理器

**configs-list**
> 列出所有已导入的配置

**config-manage** **-c** _config_
> 管理已导入的配置（重命名、移除）

**config-show** **-c** _config_
> 显示配置详情

**log** **-c** _config_
> 显示会话日志输出

**-c**, **--config** _path_
> OpenVPN 配置文件的路径

**-D**, **--disconnect**
> 断开会话

**-R**, **--restart**
> 重启会话

**-P**, **--pause**
> 暂停会话

**--resume**
> 恢复已暂停的会话

# DESCRIPTION

**openvpn3** 是面向 Linux 的新一代 OpenVPN 客户端，提供基于 D-Bus 的架构，允许非 root 用户管理 VPN 连接。它将 VPN 配置管理与会话管理分离，从而更好地与桌面环境和系统服务集成。

该客户端支持持久化地导入和存储配置，可同时管理多个 VPN 会话，并通过 D-Bus 策略提供细粒度的访问控制。其设计目标是与 NetworkManager 及其他 Linux 桌面组件集成。

# CAVEATS

需要 openvpn3-linux 软件包及相关的 D-Bus 服务。并非所有 OpenVPN 2.x 配置指令都受支持。导入配置时凭据会存入配置管理器；敏感环境请审查访问策略。

# HISTORY

由 **OpenVPN Inc.** 开发，是基于 OpenVPN 3 Core 库的现代化 Linux 客户端。发布目的在于解决传统 OpenVPN 2.x 客户端的局限，尤其是权限分离和桌面集成方面的问题。引入 D-Bus 架构正是为了让非特权用户也能管理 VPN。

# INSTALL

```apt: sudo apt install openvpn3-client```

```nix: nix profile install nixpkgs#openvpn3```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[openvpn](/man/openvpn)(8), [nmcli](/man/nmcli)(1), [networkctl](/man/networkctl)(1)
