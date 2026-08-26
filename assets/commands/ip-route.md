# TAGLINE

管理内核路由表

# TLDR

显示**路由**表

```ip route```

添加**默认**网关

```sudo ip route add default via gateway_ip```

经**接口**添加默认路由

```sudo ip route add default dev eth0```

添加**静态**路由

```sudo ip route add destination_ip via gateway_ip dev eth0```

**删除**路由

```sudo ip route delete destination_ip dev eth0```

**修改**路由

```sudo ip route change destination_ip via gateway_ip dev eth0```

**获取**到目的地的路由

```ip route get destination_ip```

显示特定**表**

```ip route list table 100```

# SYNOPSIS

**ip route** [_command_] [_OPTIONS_]

# DESCRIPTION

**ip route** 管理内核路由表。它可以添加、删除和修改路由，还可以查询内核对特定目标将使用的路由。

# PARAMETERS

**list**（或不带子命令）
> 显示路由表

**add**
> 添加新路由

**delete**
> 移除一条路由

**change**
> 修改现有路由

**replace**
> 修改路由，不存在则添加

**get** _address_
> 显示到特定目标的路由

**default**
> 默认网关路由

**via** _gateway_
> 指定下一跳网关

**dev** _interface_
> 指定出站接口

**table** _id_
> 操作特定路由表

# CAVEATS

添加的路由不会持久保留；要使其持久化需使用网络配置文件。多个路由表可与策略路由配合使用。默认表为 "main"。

# HISTORY

**ip route** 是 **iproute2** 的一部分，取代了已弃用的 route 命令。

# SEE ALSO

[ip](/man/ip)(8), [ip-address](/man/ip-address)(8), [routel](/man/routel)(8)
