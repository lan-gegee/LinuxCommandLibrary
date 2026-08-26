# TAGLINE

显示内核路由表中的条目

# TLDR

显示 **main** 路由表

```ip route list```

显示 **local** 路由表

```ip route list table local```

显示**所有**路由表

```ip route list table all```

列出**特定设备**的路由

```ip route list dev [eth0]```

列出**特定作用范围**内的路由

```ip route list scope link```

显示**路由缓存**

```ip route list cache```

仅显示 **IPv6** 路由

```ip -6 route```

仅显示 **IPv4** 路由

```ip -4 route```

# SYNOPSIS

**ip route list** [_selector_]

# PARAMETERS

**table** _TABLE_
> 路由表：main（254）、local（255）、all（0），或自定义名称/编号

**dev** _DEVICE_
> 仅显示特定设备的路由

**scope** _SCOPE_
> 按作用范围过滤：global、link、host

**cache**
> 显示路由缓存条目

**type** _TYPE_
> 路由类型：unicast、local、broadcast、multicast 等

**proto** _PROTOCOL_
> 按路由协议过滤

# DESCRIPTION

**ip route list** 显示内核路由表中的条目。main 表包含用户配置的路由，而 local 表包含由内核自动维护的本地地址路由。

路由条目显示目标网络、网关或接口，以及各种属性，如 metric、源地址偏好和添加该路由的协议。

# CAVEATS

路由缓存在 Linux 3.6 中已被移除。非常大的路由表可能产生大量输出。策略路由设置中会存在多个路由表。

# HISTORY

ip route list 是 iproute2 的一部分，取代了较旧的 route 命令。它全面支持 Linux 的高级路由功能，包括多路由表和策略路由。

# SEE ALSO

[ip](/man/ip)(8), [ip-route](/man/ip-route)(8), [ip-route-add](/man/ip-route-add)(8), [ip-rule](/man/ip-rule)(8)
