# TAGLINE

查看和操作 ARP 缓存

# TLDR

**以 BSD 风格显示 ARP 表**

```arp -a```

**以数字格式显示 ARP 表**，不做 DNS 解析

```arp -an```

**以默认 Linux 格式显示 ARP 表**

```arp -e```

**添加一条静态 ARP 条目**

```sudo arp -s [192.168.1.1] [00:11:22:33:44:55]```

**删除一条 ARP 条目**

```sudo arp -d [192.168.1.1]```

**显示指定接口的条目**

```arp -i [eth0] -a```

**从文件加载条目**

```sudo arp -f [/etc/ethers]```

# SYNOPSIS

**arp** [**-a**] [**-d** _address_] [**-s** _address_ _hw_addr_] [**-i** _interface_] [_options_]

# DESCRIPTION

**arp** 用于操作系统的 ARP（地址解析协议）缓存。ARP 在本地网段内将 IPv4 地址映射为 MAC（硬件）地址。

ARP 表随着系统的通信动态建立，但也可以手动添加、删除或查看条目，用于网络故障排查。

# PARAMETERS

**-a**
> 以 BSD 风格的输出格式显示所有条目。

**-e**
> 以默认 Linux 风格、固定列宽显示条目。

**-n**, **--numeric**
> 显示数字地址，而不解析主机名。

**-d** _address_
> 删除指定地址对应的条目。需要 root 权限。

**-s** _address_ _hw_addr_
> 添加一条静态 ARP 条目。加上 **temp** 可使其成为非永久条目。

**-i** _If_, **--device** _If_
> 将显示限制在指定的网络接口。

**-D**, **--use-device**
> 使用指定接口的硬件地址而非 hw_addr。

**-f** _filename_, **--file** _filename_
> 从文件加载地址条目（默认：/etc/ethers）。

**-v**, **--verbose**
> 详细输出。

**-H** _type_, **--hw-type** _type_
> 硬件类型（ether、arcnet、pronet、ax25、netrom）。

# CAVEATS

在现代 Linux 上，arp 命令已被 **ip neigh** 取代。静态条目默认在重启后不会保留。ARP 仅用于 IPv4；IPv6 使用邻居发现协议（NDP）。

# HISTORY

**arp** 自 **1980** 年代 TCP/IP 早期就一直是 Unix 网络工具的一部分。在 Linux 上它属于 **net-tools** 软件包，而该软件包正被 **iproute2** 取代。

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

[ip-neighbour](/man/ip-neighbour)(8), [arping](/man/arping)(8), [arp-scan](/man/arp-scan)(1), [ifconfig](/man/ifconfig)(8), [ip](/man/ip)(8)
