# TAGLINE

管理网络接口上的 IP 地址

# TLDR

**列出**所有地址

```ip address show```

只显示**活跃的**接口

```ip address show up```

显示**指定**接口的地址

```ip address show dev [eth0]```

只显示 **IPv4** 地址

```ip -4 address show```

**添加** IP 地址到接口

```sudo ip address add [192.168.1.100/24] dev [eth0]```

**删除**接口上的 IP 地址

```sudo ip address delete [192.168.1.100/24] dev [eth0]```

**清空**接口上的所有地址

```sudo ip address flush dev [eth0]```

# SYNOPSIS

**ip** [_OPTIONS_] **address** {_command_|**help**}

# DESCRIPTION

**ip address** 管理网络接口上的 IP 地址。它可以显示、添加、删除和清空 IPv4 与 IPv6 协议的地址。

# PARAMETERS

**show** [**dev** _device_]
> 显示 IP 地址（默认动作）。

**add** _address/prefix_ **dev** _device_
> 向接口添加 IP 地址。

**change** _address/prefix_ **dev** _device_
> 更改已有地址的属性。

**replace** _address/prefix_ **dev** _device_
> 在接口上添加或更新地址。

**delete** _address/prefix_ **dev** _device_
> 从接口删除 IP 地址。

**flush** [**dev** _device_]
> 删除所有匹配条件的地址。

**save**
> 将地址配置保存到 stdout。

**restore**
> 从 stdin 恢复地址配置。

**dev** _device_
> 要操作的接口名称。

**scope** _global|link|host_
> 过滤或设置地址作用域。

**label** _label_
> 设置地址标签（必须以设备名开头）。

**broadcast** _address_
> 设置广播地址。

**metric** _number_
> 设置该地址前缀路由的优先级。

**valid_lft** _lft_
> 地址的有效生存期（默认：永久）。

**preferred_lft** _lft_
> 地址的首选生存期（默认：永久）。

**up**
> 过滤，只显示活跃（UP）接口。

**permanent**
> 过滤，只显示永久（静态）地址。

**dynamic**
> 过滤，只显示动态分配的地址。

**to** _prefix_
> 过滤匹配某前缀的地址。

# CAVEATS

添加的地址重启后不会保留。要持久化请使用网络配置文件或 NetworkManager。一个接口可以有多个 IP 地址。

# HISTORY

**ip address** 是 **iproute2** 的一部分，取代了已弃用的 ifconfig 命令。

# SEE ALSO

[ip](/man/ip)(8), [ip-link](/man/ip-link)(8), [ip-route](/man/ip-route)(8), [ip-neighbour](/man/ip-neighbour)(8)
