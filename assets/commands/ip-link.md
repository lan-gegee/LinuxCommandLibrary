# TAGLINE

网络设备配置：启用/禁用接口、设置 MAC、MTU，创建虚拟链路

# TLDR

显示**所有**接口

```ip link```

显示**特定**接口

```ip link show eth0```

显示**详细**统计信息

```ip -s link show eth0```

将接口**启用/禁用**

```sudo ip link set eth0 up```

设置**别名**名称

```sudo ip link set eth0 alias "LAN Interface"```

更改 **MAC** 地址（接口必须处于 down 状态）

```sudo ip link set dev eth0 address ff:ee:dd:cc:bb:aa```

设置 **MTU** 大小

```sudo ip link set eth0 mtu 9000```

设置**混杂模式**

```sudo ip link set eth0 promisc on```

创建一个 **VLAN** 子接口

```sudo ip link add link eth0 name eth0.10 type vlan id 10```

# SYNOPSIS

**ip** [_OPTIONS_] **link** _COMMAND_ [_arguments_]

# DESCRIPTION

**ip link** 用于管理网络设备。它可以列出接口、更改接口的状态和参数（MAC 地址、MTU、别名、混杂模式），并创建或删除虚拟链路，例如桥接（bridge）、绑定（bond）、VLAN、VXLAN、dummy、veth 对以及 tun/tap 设备。

它是 **iproute2** 工具集的一部分，用于取代较旧的 **ifconfig** 工具。

# PARAMETERS

**show** [_device_]
> 显示接口信息。不指定 _device_ 时显示所有接口。可与 **-s** 组合查看统计信息，与 **-d** 组合查看详细的驱动信息。

**set** _device_
> 修改现有接口的属性。

**add** [_link DEV_] **name** _NAME_ **type** _TYPE_
> 创建指定类型的虚拟接口（bridge、vlan、veth、dummy、bond、vxlan 等）。

**delete** _device_
> 删除虚拟接口。

**up** | **down**
> 将接口管理性启用或禁用。

**address** _LLADDR_
> 设置链路层（MAC）地址。通常需要先将接口置于 down 状态。

**mtu** _BYTES_
> 设置最大传输单元（MTU）。

**alias** _NAME_
> 设置人类可读的接口描述。

**promisc** **on** | **off**
> 启用或禁用混杂模式。

**multicast** **on** | **off**
> 启用或禁用组播接收。

**arp** **on** | **off**
> 在接口上启用或禁用 ARP。

**master** _DEVICE_
> 将接口挂到主设备（桥接或绑定）之下。

**nomaster**
> 将接口与其主设备解绑。

**txqueuelen** _N_
> 设置发送队列长度。

**netns** _PID_ | _NAME_
> 将接口移入指定的网络命名空间。

# CAVEATS

更改 MAC 地址通常需要先禁用接口。通过 **ip link add** 创建的虚拟接口在重启后不会保留，除非将其写入发行版特定的网络配置中（NetworkManager、systemd-networkd、/etc/network/interfaces 等）。某些操作需要 **CAP_NET_ADMIN** 权限（通常是 root）。

# HISTORY

**ip link** 是 **iproute2** 的一部分，最初由 **Alexey Kuznetsov** 编写，目前由 **Stephen Hemminger** 维护。它取代了 net-tools 中已弃用的 **ifconfig** 命令。

# INSTALL

```apt: sudo apt install iproute2```

```pacman: sudo pacman -S iproute2```

```apk: sudo apk add iproute2-minimal```

```zypper: sudo zypper install iproute2```

```brew: brew install iproute2```

```nix: nix profile install nixpkgs#iproute2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ip](/man/ip)(8), [ip-address](/man/ip-address)(8), [ip-route](/man/ip-route)(8), [ip-tuntap](/man/ip-tuntap)(8), [ip-monitor](/man/ip-monitor)(8), [bridge](/man/bridge)(8), [ethtool](/man/ethtool)(8)
