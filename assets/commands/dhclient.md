# TAGLINE

用于动态网络配置的 ISC DHCP 客户端

# TLDR

**为接口获取 IP 地址**

```dhclient [eth0]```

**释放当前租约**

```dhclient -r [eth0]```

**释放并获取**新租约

```dhclient -r [eth0] && dhclient [eth0]```

**以前台方式运行**并输出详细信息

```dhclient -d -v [eth0]```

**使用指定的配置文件**

```dhclient -cf [/etc/dhcp/dhclient.conf] [eth0]```

**联系指定的 DHCP 服务器**

```dhclient -s [192.168.1.1] [eth0]```

# SYNOPSIS

**dhclient** [_options_] [_interface_...]

# PARAMETERS

_INTERFACE_
> 要配置的网络接口。

**-r**
> 释放当前租约。

**-d**
> 以前台方式运行（调试模式）。

**-v**
> 详细输出。

**-cf** _FILE_
> 使用指定的配置文件。

**-lf** _FILE_
> 使用指定的租约文件。

**-s** _ADDRESS_
> 指定要联系的 DHCP 服务器地址。

**-4**
> 仅使用 DHCPv4。

**-6**
> 仅使用 DHCPv6。

**--help**
> 显示帮助信息。

# CONFIGURATION

**/etc/dhcp/dhclient.conf**
> DHCP 客户端配置文件。控制请求行为、超时时间和自定义 DHCP 选项。

**/var/lib/dhcp/dhclient.leases**
> 存储网络接口的活跃与历史租约信息。

# DESCRIPTION

**dhclient** 是 Internet Systems Consortium 的 DHCP 客户端。它通过从 DHCP 服务器获取 IP 地址、子网掩码、网关和 DNS 服务器来动态配置网络接口。

该客户端实现了 DHCP 协议，处理租约的协商、续约和释放。dhclient.conf 中的配置选项允许自定义请求，包括请求特定的选项或地址。

dhclient 将租约信息保存在租约文件中，使其在重连时可以请求相同的地址。它能同时管理多个接口，并同时支持 DHCPv4 和 DHCPv6。

# CAVEATS

需要 root 权限。可能与 NetworkManager 等网络管理器冲突。租约文件会随时间不断累积。某些选项需要服务器支持。

# HISTORY

dhclient 是 **ISC DHCP** 软件包的一部分，最初由 Internet Systems Consortium 的 **Ted Lemon** 开发。ISC DHCP 自 20 世纪 90 年代末以来一直是 DHCP 的参考实现，不过随着更新的实现出现，它已进入维护模式。

# INSTALL

```apt: sudo apt install isc-dhcp-client```

```pacman: sudo pacman -S dhclient```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dhcpcd](/man/dhcpcd)(8), [ip](/man/ip)(8), [ifconfig](/man/ifconfig)(8), [networkctl](/man/networkctl)(1)
