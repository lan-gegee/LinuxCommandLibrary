# TAGLINE

显示由 lldpd 守护进程收集的链路层发现协议信息

# TLDR

显示**邻居数据**

```sudo lldpctl```

显示**帮助**

```lldpctl --help```

# SYNOPSIS

**lldpctl** [_options_] [_interfaces_]

# DESCRIPTION

**lldpctl** 显示由 lldpd 守护进程收集的链路层发现协议（LLDP）信息。网络设备使用 LLDP 在本地网络上通告自己的身份、能力和邻居信息。

# PARAMETERS

**-f FORMAT**
> 输出格式：plain、xml、json、keyvalue

**-a**
> 显示所有接口，包括隐藏接口

**-C PATTERN**
> 配置特定设置

**-L LOCATION**
> 设置位置信息

**-h, --help**
> 显示帮助信息

# CAVEATS

需要 lldpd 守护进程正在运行。完整功能需要 root 权限。

# HISTORY

LLDP 于 **2005 年**被标准化为 IEEE 802.1AB，作为一种厂商中立的发现协议，取代了 Cisco CDP 等专有协议。

# INSTALL

```apt: sudo apt install lldpd```

```dnf: sudo dnf install lldpd```

```pacman: sudo pacman -S lldpd```

```apk: sudo apk add lldpd```

```zypper: sudo zypper install lldpd```

```brew: brew install lldpd```

```nix: nix profile install nixpkgs#lldpd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tcpdump](/man/tcpdump)(8)
