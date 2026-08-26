# TAGLINE

控制由 NetworkManager 管理的整体网络状态

# TLDR

显示 NetworkManager 的**网络状态**

```nmcli networking```

**启用或禁用**网络及 NetworkManager 管理的所有接口

```nmcli networking [on|off]```

显示**最近一次已知的连通性**状态

```nmcli networking connectivity```

显示**当前连通性**状态（执行一次检查）

```nmcli networking connectivity check```

# SYNOPSIS

**nmcli networking** [_command_]

# PARAMETERS

**on**
> 启用网络及所有由 NetworkManager 管理的接口

**off**
> 禁用网络并停用所有连接

**connectivity**
> 不执行检查，直接显示连通性状态

**connectivity check**
> 执行连通性检查并显示结果

# DESCRIPTION

**nmcli networking** 控制由 NetworkManager 管理的整体网络状态。它提供一个总开关，可以一次性启用或禁用所有网络接口。

连通性状态包括：
- **full**：已连接，可完整访问互联网
- **limited**：已接入网络但无法访问互联网（强制门户、防火墙）
- **portal**：处于需要登录的强制门户之后
- **none**：没有网络连接

**connectivity check** 会通过访问一个已知 URL 来主动探测连通性，而不带 "check" 时只是报告上次探测得到的缓存状态。

# CAVEATS

禁用网络会影响所有由 NetworkManager 管理的连接，但不影响由其他工具管理的接口。连通性检查依赖对连通性检查服务器的网络可达性（可在 NetworkManager.conf 中配置）。某些网络会阻止这些探测。

# INSTALL

```apt: sudo apt install network-manager```

```apk: sudo apk add networkmanager-cli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nmcli](/man/nmcli)(1), [nmcli-general](/man/nmcli-general)(1), [nmcli-radio](/man/nmcli-radio)(1), [NetworkManager](/man/NetworkManager)(8)
