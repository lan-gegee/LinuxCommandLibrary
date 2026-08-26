# TAGLINE

IPv4 和 IPv6 子网计算器

# TLDR

**计算子网**

```sipcalc [192.168.1.0/24]```

把网络**拆分为 /26 子网**

```sipcalc -s [26] [192.168.1.0/24]```

IPv6 地址

```sipcalc [2001:db8::1/64]```

显示全部信息

```sipcalc -a [192.168.1.100/24]```

接口地址

```sipcalc [eth0]```

CIDR 位图输出

```sipcalc -b [192.168.1.0/24]```

有类别地址信息

```sipcalc -c [10.0.0.0]```

把 Cisco 通配符掩码转换为网络掩码

```sipcalc -w [0.0.0.255]```

IPv6 反向 DNS

```sipcalc -r [2001:db8::1/48]```

# SYNOPSIS

**sipcalc** [_-s size_] [_-a_] [_-b_] [_options_] _address_

# PARAMETERS

**-a**
> 给出地址或接口的所有可能信息。

**-b**
> 显示基于 CIDR 的位图（IPv4）。

**-c**
> 显示有类别地址信息（IPv4）。

**-d**
> 启用名称解析。

**-e**
> 显示 v4inv6 地址信息（IPv6）。

**-i**
> 显示 CIDR 地址信息（默认 IPv4）。

**-n** _NUM_
> 从当前子网开始显示 NUM 个额外子网。

**-r**
> 显示 IPv6 反向 DNS 信息。

**-s** _MASK_
> 将 IPv4 网络拆分为 MASK 大小的子网。

**-S** _MASK_
> 将 IPv6 网络拆分为 MASK 大小的子网。

**-t**
> 显示标准 IPv6 地址信息（默认 IPv6）。

**-u**
> 网络拆分的详细模式。

**-w**
> 将 Cisco 通配符（反向掩码）转换为常规网络掩码。

**-4** _ADDR_
> 显式添加一个 IPv4 地址。

**-6** _ADDR_
> 显式添加一个 IPv6 地址。

# DESCRIPTION

**sipcalc** 是一个高级 IP 子网计算器，同时支持 IPv4 和 IPv6 地址。给定带前缀长度或网络掩码的地址，它会以 CIDR 和传统网络掩码两种记法显示网络地址、广播地址、主机范围及其他细节。

子网拆分选项（**-s**）按指定前缀长度将网络划分为更小的子网，并显示所有结果范围。接口模式接受网络接口名而非地址，读取系统配置的地址进行分析。**-b** 选项增加二进制表示，帮助在位级别理解子网边界。

# CAVEATS

复杂的子网划分可能需要验证。IPv6 输出较为冗长。接口模式需要相应权限。

# HISTORY

**sipcalc** 由 **Simon Ekstrand** 编写，用于 IP 地址计算。它以一致的输出格式支持两种协议版本。

# INSTALL

```apt: sudo apt install sipcalc```

```dnf: sudo dnf install sipcalc```

```apk: sudo apk add sipcalc```

```zypper: sudo zypper install sipcalc```

```brew: brew install sipcalc```

```nix: nix profile install nixpkgs#sipcalc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ipcalc](/man/ipcalc)(1), [ip](/man/ip)(8), [ifconfig](/man/ifconfig)(8)
