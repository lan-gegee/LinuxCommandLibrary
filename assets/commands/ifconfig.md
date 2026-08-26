# TAGLINE

配置网络接口

# TLDR

**显示所有接口**

```ifconfig```

**显示指定接口**

```ifconfig [eth0]```

**设置 IP 地址**

```sudo ifconfig [eth0] [192.168.1.100]```

**启用接口**

```sudo ifconfig [eth0] up```

**禁用接口**

```sudo ifconfig [eth0] down```

**设置子网掩码**

```sudo ifconfig [eth0] netmask [255.255.255.0]```

# SYNOPSIS

**ifconfig** [_interface_] [_options_]

# PARAMETERS

_INTERFACE_
> 网络接口名称。

**up**
> 激活接口。

**down**
> 停用接口。

**netmask** _MASK_
> 设置子网掩码。

**broadcast** _ADDR_
> 设置广播地址。

**mtu** _SIZE_
> 设置 MTU 大小。

**-a**
> 显示所有接口，包括已停用的。

**hw** _class_ _address_
> 设置硬件（MAC）地址（如 `hw ether AA:BB:...`）。

**promisc** / **-promisc**
> 启用或禁用混杂模式。

**arp** / **-arp**
> 在接口上启用或禁用 ARP 协议。

**multicast** / **-multicast**
> 启用或禁用多播标志。

**add** _ADDR_/_PREFIX_
> 向接口添加 IPv6 地址。

**del** _ADDR_/_PREFIX_
> 从接口移除 IPv6 地址。

**--help**
> 显示帮助信息。

# DESCRIPTION

**ifconfig** 用于配置网络接口。它可以显示和修改 IP 地址、子网掩码和接口状态。不带参数时显示所有活动的接口。使用 **-a** 时显示所有接口，包括已停用的。

该工具属于 **net-tools**，正在被 iproute2 的 **ip** 命令取代，但在许多系统上仍被广泛使用。

# CAVEATS

已被 ip 命令弃用。属于 net-tools。修改配置需要 root 权限。

# HISTORY

**ifconfig** 自 **4.2BSD**（1983 年）起就是 Unix 网络功能的一部分。在 Linux 上它属于 **net-tools** 软件包，如今已在很大程度上被 **iproute2** 取代。

# INSTALL

```apt: sudo apt install net-tools```

```dnf: sudo dnf install net-tools```

```pacman: sudo pacman -S net-tools```

```apk: sudo apk add net-tools```

```zypper: sudo zypper install net-tools```

```brew: brew install net-tools```

```nix: nix profile install nixpkgs#net-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ip](/man/ip)(8), [route](/man/route)(8), [netstat](/man/netstat)(8)
