# TAGLINE

执行路由查找并显示内核将使用的确切路由

# TLDR

输出**到目的地的路由**

```ip route get [1.1.1.1]```

从**特定源**输出路由

```ip route get [destination] from [source]```

输出从**特定接口**到达的数据包的路由

```ip route get [destination] iif [eth0]```

输出强制经**特定接口**发出的路由

```ip route get [destination] oif [eth0]```

输出带**服务类型**的路由

```ip route get [destination] tos [0x10]```

使用 **VRF** 实例输出路由

```ip route get [destination] vrf [myvrf]```

# SYNOPSIS

**ip route get** _destination_ [_options_]

# PARAMETERS

**from** _SOURCE_
> 用于路由查找的源地址

**iif** _DEVICE_
> 入站接口（针对转发的数据包）

**oif** _DEVICE_
> 强制指定出站接口

**tos** _TOS_
> 服务类型值

**vrf** _NAME_
> VRF 实例名称

**mark** _MARK_
> 防火墙标记值

# DESCRIPTION

**ip route get** 执行一次路由查找，显示内核对给定目标实际会使用的路由。它会显示完整的路由条目，包括网关、接口、源地址以及其他属性。

与显示已存储路由的 ip route list 不同，ip route get 会查询内核针对特定数据包的路由决策，并将策略路由规则和路由选择算法考虑在内。

# CAVEATS

输出反映当前路由状态，可能会动态变化。VRF 查找要求 VRF 已配置。基于 mark 的查找需要有匹配的策略规则。

# HISTORY

ip route get 是 iproute2 的一部分，可用于了解内核的实际路由决策；由于策略规则和路由 metric 的存在，这一决策可能与存储的路由表不同。

# SEE ALSO

[ip](/man/ip)(8), [ip-route](/man/ip-route)(8), [ip-route-list](/man/ip-route-list)(8), [ip-rule](/man/ip-rule)(8)
