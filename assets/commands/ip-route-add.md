# TAGLINE

向内核路由表添加新路由

# TLDR

添加经由网关的**默认路由**

```sudo ip route add default via [gateway_ip]```

添加经由接口的**默认路由**

```sudo ip route add default dev [eth0]```

添加**静态路由**

```sudo ip route add [192.168.1.0/24] via [gateway_ip] dev [eth0]```

添加带指定 **metric**（优先级）的路由

```sudo ip route add [192.168.2.0/24] via [gateway_ip] metric [100]```

向**特定路由表**添加路由

```sudo ip route add [10.0.0.0/8] dev [eth0] table [100]```

添加指定首选**源地址**的路由

```sudo ip route add [192.168.1.0/24] dev [eth0] src [192.168.1.5]```

# SYNOPSIS

**ip route add** _destination_ [_options_]

# PARAMETERS

**default**
> 默认路由（0.0.0.0/0 或 ::/0）

**via** _GATEWAY_
> 下一跳网关地址

**dev** _DEVICE_
> 出站设备名称

**table** _TABLE_
> 路由表（编号或名称）

**metric** _NUM_
> 路由优先级（数值越小越优先）

**src** _ADDRESS_
> 首选源地址

**proto** _PROTOCOL_
> 路由协议标识符（static、boot、dhcp 等）

**scope** _SCOPE_
> 路由的作用范围（global、link、host）

**mtu** _NUM_
> 该路由的最大传输单元

**nexthop** _NEXTHOP_
> 定义具有多个下一跳的多路径路由

# DESCRIPTION

**ip route add** 向内核路由表添加新路由。路由根据目标地址决定数据包如何转发到目的地。

一条路由要么指定转发数据包的网关（下一跳路由器），要么指定直连网络的出站接口。多个路由表可用于策略路由。

# CAVEATS

需要 root 权限。若无额外配置，路由在重启后不会保留。添加相互冲突的路由可能失败或产生意外行为。

# HISTORY

ip route 命令是 iproute2 的一部分，后者取代了 net-tools 中较旧的 route 命令。iproute2 提供对所有 Linux 网络功能的统一管理。

# SEE ALSO

[ip](/man/ip)(8), [ip-route](/man/ip-route)(8), [ip-route-list](/man/ip-route-list)(8), [ip-rule](/man/ip-rule)(8), [ip-address](/man/ip-address)(8), [route](/man/route)(8)
