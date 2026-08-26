# TAGLINE

IP 子网与 CIDR 表示法计算器

# TLDR

**计算子网信息**

```ipcalc [192.168.1.0/24]```

**显示网络范围**

```sipcalc [10.0.0.0/8]```

**使用子网掩码计算**

```ipcalc [192.168.1.0] [255.255.255.0]```

**设计子网**

```ipcalc [192.168.1.0/24] [/27]```

# SYNOPSIS

**ipcalc** [_options_] _address_[/_prefix_] [_netmask_]
**sipcalc** [_options_] _address_[/_prefix_]

# DESCRIPTION

CIDR 计算器根据 IP 地址和子网掩码计算网络信息。常用工具包括 **ipcalc**、**sipcalc** 和 **whatmask**。它们可以计算网络地址、广播地址、可用主机范围、通配符掩码及其他子网参数。

这些工具对于网络规划、子网划分和故障排查必不可少。给定一个 IP 地址和前缀长度（或子网掩码），它们会列出所有相关的编址细节。部分工具还支持 IPv6、子网拆分和超网。

可通过软件包管理器在大多数 Linux 发行版上安装。若想直观地探索 CIDR 表示法，cidr.xyz 等在线工具提供交互式可视化。

# IPCALC OPTIONS

**-n**
> 不显示主机名

**-b**
> 不显示广播地址

**-s** _hosts_
> 按主机数拆分网络

**-r** _hosts_
> 计算所需的前缀长度

# SIPCALC OPTIONS

**-a**
> 显示全部信息

**-d**
> 解析主机名

**-4**
> 仅 IPv4

**-6**
> 仅 IPv6

# OUTPUT FIELDS

**Network**
> 子网中的第一个地址

**Broadcast**
> 子网中的最后一个地址

**HostMin/HostMax**
> 可用地址范围

**Hosts/Net**
> 可用地址数量

**Wildcard**
> Cisco 通配符掩码

# INSTALLATION

```
apt install ipcalc sipcalc
```

# CAVEATS

用于网络规划和故障排查。可在 cidr.xyz 使用在线工具进行可视化。

# INSTALL

```apt: sudo apt install cidr```

```brew: brew install cidr```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ip](/man/ip)(8), [ifconfig](/man/ifconfig)(8)
