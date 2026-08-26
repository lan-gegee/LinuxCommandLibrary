# TAGLINE

BIRD 路由守护进程的控制客户端

# TLDR

**显示**协议

```birdc show protocols```

**显示**路由

```birdc show route```

**显示**协议详情

```birdc show protocols all [bgp1]```

**重载**配置

```birdc configure```

**禁用**协议

```birdc disable [bgp1]```

# SYNOPSIS

**birdc** [_options_] [_command_]

# DESCRIPTION

**birdc** 是 BIRD 路由守护进程的客户端。它通过控制套接字连接到 BIRD 守护进程，允许查询路由信息、管理协议以及重新配置守护进程。

该工具是监控和控制 BIRD 的主要界面。

# PARAMETERS

**-s** _socket_
> 控制套接字路径

**-r**
> 受限模式

# COMMON COMMANDS

**show protocols** [**all**] [_name_]
> 显示路由协议状态

**show route** [**all**]
> 显示路由表

**show interfaces**
> 显示网络接口

**show status**
> 显示守护进程状态

**configure** [_file_]
> 重载配置

**enable** _protocol_
> 启用协议

**disable** _protocol_
> 禁用协议

**restart** _protocol_
> 重启协议

**down**
> 关闭 BIRD 守护进程

# WORKFLOW

```bash
# Show all protocols
birdc show protocols

# Detailed protocol info
birdc show protocols all bgp1

# Show routing table
birdc show route

# Show specific route
birdc show route for 192.0.2.0/24

# Reload config
birdc configure

# Restart BGP session
birdc restart bgp1
```

# INTERACTIVE MODE

```bash
# Start interactive session
birdc

bird> show protocols
bird> show route all
bird> exit
```

# CONFIGURATION

**/etc/bird.conf**
> birdc 所控制的 BIRD 路由守护进程的主配置文件。Debian 等发行版使用 **/etc/bird/bird.conf**。默认控制套接字为 **/run/bird/bird.ctl**（较旧的构建使用 **/var/run/bird/bird.ctl**）。

# CAVEATS

需要 BIRD 守护进程正在运行。套接字权限可能限制访问。某些命令需要特权。配置错误可能扰乱路由。更改立即生效（无确认提示）。

# HISTORY

自 **1998 年**创建以来，**birdc** 一直是 BIRD 套件中路由守护进程的控制接口。BIRD 由 Ondrej Filip、Pavel Machek 和 Martin Mares 开发，现由 CZ.NIC Labs 维护。在 BIRD 1.x 及之前，需要单独的 **birdc6** 客户端来控制 IPv6 守护进程；BIRD 2.x 将 IPv4 和 IPv6 合并为单一守护进程，因此现在仅用 **birdc** 即可管理两者。

# INSTALL

```apt: sudo apt install bird2```

```dnf: sudo dnf install bird```

```pacman: sudo pacman -S bird```

```apk: sudo apk add bird```

```zypper: sudo zypper install bird```

```nix: nix profile install nixpkgs#bird2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bird](/man/bird)(8), [bgpctl](/man/bgpctl)(8), [vtysh](/man/vtysh)(1)

# RESOURCES

```[Source code](https://github.com/CZ-NIC/bird)```

```[Homepage](https://bird.network.cz/)```

```[Documentation](https://bird.network.cz/?get_doc&f=bird.html&v=30)```

<!-- verified: 2026-06-19 -->
