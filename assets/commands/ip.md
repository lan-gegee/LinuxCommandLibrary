# TAGLINE

现代 Linux 网络命令，用于查看和操作路由

# TLDR

列出接口及**详细信息**

```ip address```

以**简要格式**列出接口的网络层信息

```ip -br address```

以简要格式列出接口的**链路层**信息

```ip -br link```

显示**路由表**

```ip route```

显示**邻居**（ARP 表）

```ip neighbour```

将接口**启用/禁用**

```sudo ip link set [ethX] up```
```sudo ip link set [ethX] down```

为接口**添加/删除** IP 地址

```sudo ip address add [ip_address]/[mask] dev [ethX]```
```sudo ip address delete [ip_address]/[mask] dev [ethX]```

添加**默认路由**

```sudo ip route add default via [ip_address] dev [ethX]```

# SYNOPSIS

**ip** [_-br_] [_-c_] [_-4_|_-6_] _object_ [_command_]

# DESCRIPTION

**ip** 是现代 Linux 网络命令，用于查看和操作路由、设备、策略路由和隧道。它取代了较旧的 **ifconfig**、**route** 和 **arp** 命令。

# PARAMETERS

**address, a**
> 显示和管理 IP 地址

**link, l**
> 显示和管理网络接口

**route, r**
> 显示和管理路由表

**neighbour, n**
> 显示和管理 ARP/邻居缓存

**tunnel**
> 显示和管理 IP 隧道

**maddr**
> 显示和管理组播地址

**rule**
> 显示和管理路由策略数据库

**-br, -brief**
> 以简要格式输出

**-c, -color**
> 使用彩色输出

**-4**
> 仅 IPv4

**-6**
> 仅 IPv6

**-s, -stats**
> 输出更多统计信息

**-o, -oneline**
> 每条记录输出为单行

# CAVEATS

通过 **ip** 所做的更改在重启后不会保留。要使更改持久化，请使用网络配置文件或 NetworkManager。

# HISTORY

属于 **iproute2** 软件包，在 **Linux 2.2** 中引入，用于取代旧的 net-tools 软件包（ifconfig、route、arp）。

# INSTALL

```apt: sudo apt install iproute2```

```pacman: sudo pacman -S iproute2```

```apk: sudo apk add iproute2-minimal```

```zypper: sudo zypper install iproute2```

```brew: brew install iproute2```

```nix: nix profile install nixpkgs#iproute2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ifconfig](/man/ifconfig)(8), [route](/man/route)(8), [arp](/man/arp)(8), [ss](/man/ss)(8), [ip-address](/man/ip-address)(8), [ip-route](/man/ip-route)(8)
