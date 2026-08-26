# TAGLINE

处理 IPv4 链路本地地址事件

# TLDR

将获取到的 IPv4LL 地址**添加**到网络接口（BIND 事件）

```/etc/avahi/avahi-autoipd.action BIND [interface] [ip_address]```

因检测到地址冲突而**移除**地址（CONFLICT 事件）

```/etc/avahi/avahi-autoipd.action CONFLICT [interface] [ip_address]```

在有可路由地址可用时**移除**地址（UNBIND 事件）

```/etc/avahi/avahi-autoipd.action UNBIND [interface] [ip_address]```

守护进程关闭时**移除**地址（STOP 事件）

```/etc/avahi/avahi-autoipd.action STOP [interface] [ip_address]```

# SYNOPSIS

**/etc/avahi/avahi-autoipd.action** _event_ _interface_ _address_

# PARAMETERS

**_event_**
> 事件类型：**BIND**、**CONFLICT**、**UNBIND** 或 **STOP**

**_interface_**
> 网络接口名称（如 eth0、wlan0）

**_address_**
> 位于 169.254.0.0/16 范围内的 IPv4LL 地址

# DESCRIPTION

**avahi-autoipd.action** 是由 **avahi-autoipd** 自动调用的动作脚本，每当获取到 IPv4 链路本地地址或检测到 IP 地址冲突时触发。该脚本负责在网络接口上添加或移除指定地址。

脚本接收三个参数：事件字符串、网络接口名称和 IPv4LL 地址。根据事件类型，它会执行相应的网络配置：

> **BIND** - 已成功获取 IP 地址；脚本将其添加到网络接口

> **CONFLICT** - avahi-autoipd 检测到该 IP 地址已被本地网络中的其他主机使用；脚本移除已配置的地址

> **UNBIND** - 其他程序已为接口配置了可路由地址；脚本移除 IPv4LL 地址以避免冲突

> **STOP** - avahi-autoipd 正在关闭；脚本从接口上移除该 IP 地址

默认脚本通常使用 **ip** 或 **ifconfig** 命令操作接口地址。用户可以自定义此脚本，以便与特定的网络管理系统集成，或添加额外的配置步骤。

# CAVEATS

该脚本以提升的权限运行，并由 **avahi-autoipd** 自动执行。修改此脚本前应仔细测试，因为错误可能导致 IPv4LL 地址无法正确配置。自定义前务必保留备份。

# SEE ALSO

[avahi-autoipd](/man/avahi-autoipd)(8), [ip](/man/ip)(8), [ifconfig](/man/ifconfig)(8)
