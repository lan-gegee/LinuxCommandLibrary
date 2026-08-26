# TAGLINE

计算 IP 网络信息

# TLDR

**计算网络信息**

```ipcalc [192.168.1.0/24]```

**以子网掩码方式显示**

```ipcalc [192.168.1.0] [255.255.255.0]```

**将网络拆分为子网**

```ipcalc [192.168.0.0/16] -s [256] [256] [256]```

**检查 IP 是否属于某网络**

```ipcalc -c [192.168.1.100] [192.168.1.0/24]```

**显示二进制表示**

```ipcalc -b [192.168.1.0/24]```

# SYNOPSIS

**ipcalc** [_options_] _address_ [_netmask_]

# PARAMETERS

_address_
> 带可选 CIDR 的 IP 地址。

_netmask_
> 子网掩码（当不使用 CIDR 时）。

**-b**, **--broadcast**
> 显示广播地址。

**-n**, **--network**
> 显示网络地址。

**-h**, **--hostname**
> 显示主机名。

**-s** _size_...
> 按大小拆分为子网。

**-c**, **--check**
> 校验地址。

**--class**
> 显示地址类别（A、B、C、D 或 E）。

**--minaddr**
> 显示最小主机地址。

**--maxaddr**
> 显示最大主机地址。

**-4**, **-6**
> 强制使用 IPv4/IPv6。

**-r**, **--random-private**
> 为给定前缀长度生成一个随机私有地址。

**--no-decorate**
> 输出不带修饰（适合脚本处理）。

# DESCRIPTION

**ipcalc** 计算 IP 网络信息。根据 IP 地址和子网掩码或 CIDR 表示法，它显示网络地址、广播地址、主机范围及其他细节。

该工具是网络规划、子网划分以及排查 IP 配置问题的必备工具。

# CAVEATS

存在两种不同的实现：Red Hat 版本（initscripts 中的 ipcalc）和 Nikos Mavrogiannopoulos 编写的较新 ipcalc。二者的选项和功能不同。`-s` 子网拆分与 `-c` 校验选项仅在部分版本中可用。IPv6 支持仅存在于较新的实现中。

# HISTORY

**ipcalc** 有多个实现。最初的版本是 Red Hat **initscripts** 软件包的一部分。较新且功能更多的版本由 **Nikos Mavrogiannopoulos** 编写，支持 IPv6 并提供额外的计算功能。

# INSTALL

```dnf: sudo dnf install ipcalc```

```pacman: sudo pacman -S ipcalc```

```apk: sudo apk add ipcalc```

```zypper: sudo zypper install ipcalc```

```brew: brew install ipcalc```

```nix: nix profile install nixpkgs#ipcalc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sipcalc](/man/sipcalc)(1), [ip](/man/ip)(8), [ifconfig](/man/ifconfig)(8)
