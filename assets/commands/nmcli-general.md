# TAGLINE

管理 NetworkManager 的常规设置与状态

# TLDR

显示 NetworkManager 的**总体状态**

```nmcli general```

显示当前设备的**主机名**

```nmcli general hostname```

**修改当前设备的主机名**

```sudo nmcli general hostname [new_hostname]```

显示 NetworkManager 的**权限**

```nmcli general permissions```

显示**当前的日志级别**和域

```nmcli general logging```

**设置日志级别**和/或域

```sudo nmcli general logging level [INFO|OFF|ERR|WARN|DEBUG|TRACE] domain [domain_1,domain_2,...]```

# SYNOPSIS

**nmcli general** [_command_] [_arguments_]

# PARAMETERS

**status**
> 显示 NetworkManager 的整体状态（未指定子命令时的默认行为）

**hostname**
> 显示或设置系统主机名

**permissions**
> 显示当前用户的 NetworkManager 权限

**logging**
> 显示或设置日志详细程度和域

**reload**
> 重新加载 NetworkManager 配置

# DESCRIPTION

**nmcli general** 管理 NetworkManager 的常规设置，并提供网络管理子系统的状态信息。它会显示网络是否已启用、当前的连通性状态以及整个系统的网络状态。

**hostname** 子命令提供一种感知 NetworkManager 的方式来设置系统主机名，设置后会传播到其他主机名服务并在重启后保持。

**logging** 子命令控制 NetworkManager 的调试输出，有助于排查连接问题。域包括 WIFI、ETHERNET、VPN、DHCP 等。

# CAVEATS

设置主机名或日志级别需要 root 权限。日志更改会立即影响正在运行的守护进程，但除非在 NetworkManager.conf 中配置，否则不会在重启后保持。过高的调试级别会产生大量日志输出。

# INSTALL

```apt: sudo apt install network-manager```

```apk: sudo apk add networkmanager-cli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nmcli](/man/nmcli)(1), [nmcli-networking](/man/nmcli-networking)(1), [NetworkManager.conf](/man/NetworkManager.conf)(5), [hostnamectl](/man/hostnamectl)(1)
