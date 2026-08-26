# TAGLINE

管理 ARP 和 NDP 邻居表

# TLDR

显示**邻居/ARP 表**

```ip neighbor```

**清空**特定设备的条目

```sudo ip neighbor flush dev [eth0]```

**查找**一条邻居条目

```ip neighbor get [192.168.1.1] dev [eth0]```

**添加**一条静态 ARP 条目

```sudo ip neighbor add [192.168.1.100] lladdr [00:11:22:33:44:55] dev [eth0] nud reachable```

**删除**一条 ARP 条目

```sudo ip neighbor delete [192.168.1.100] dev [eth0]```

**替换**一条 ARP 条目

```sudo ip neighbor replace [192.168.1.100] lladdr [00:11:22:33:44:55] dev [eth0]```

# SYNOPSIS

**ip neighbor** [_command_] [_options_]

# PARAMETERS

**show** [**dev** _DEVICE_]
> 显示邻居表条目

**add** _IP_ **lladdr** _MAC_ **dev** _DEVICE_
> 添加一条邻居条目

**delete** _IP_ **dev** _DEVICE_
> 移除一条邻居条目

**change** _IP_ **lladdr** _MAC_ **dev** _DEVICE_
> 修改现有条目

**replace** _IP_ **lladdr** _MAC_ **dev** _DEVICE_
> 添加或修改条目

**flush** **dev** _DEVICE_
> 清空某个设备的条目

**get** _IP_ **dev** _DEVICE_
> 查找单条条目

**nud** _STATE_
> 邻居状态：permanent、noarp、reachable、stale、none、incomplete、delay、probe、failed。

**proxy** _ADDR_
> 管理代理 ARP/NDP 条目。

**to** _PREFIX_
> 按地址前缀过滤条目（与 show/flush 配合使用）。

# DESCRIPTION

**ip neighbor** 管理 ARP（IPv4）和 NDP（IPv6）邻居表。这些表将 IP 地址映射为直连网络上主机的链路层（MAC）地址。

邻居缓存通常通过 ARP/NDP 协议自动填充，但也可以为不响应 ARP 的主机或出于安全目的添加静态条目。

**neighbor** 是 **ip** 接受的美式拼写；**neighbour** 是对应的英式拼写，二者指同一对象。该关键字还可以缩写为 **neigh** 或 **n**。

# CAVEATS

修改条目需要 root 权限。如果实际 MAC 地址发生变化，静态条目可能会失效。IPv6 使用 NDP 而非 ARP，但通过同一接口进行管理。

# HISTORY

ip neighbor 是 iproute2 的一部分，取代了 net-tools 中较旧的 arp 命令。它提供统一的 IPv4 和 IPv6 邻居管理。

# SEE ALSO

[ip](/man/ip)(8), [ip-neighbour](/man/ip-neighbour)(8), [arp](/man/arp)(8), [arping](/man/arping)(8)

# RESOURCES

```[Source code](https://git.kernel.org/pub/scm/network/iproute2/iproute2.git)```

```[Documentation](https://www.man7.org/linux/man-pages/man8/ip-neighbour.8.html)```

<!-- verified: 2026-06-22 -->
