# TAGLINE

使用 ARP 发现网络中的主机

# TLDR

**扫描本地网络**

```netdiscover```

**扫描指定范围**

```netdiscover -r [192.168.1.0/24]```

**被动模式**

```netdiscover -p```

**使用指定接口**

```netdiscover -i [eth0]```

**快速扫描**

```netdiscover -f```

**从文件读取扫描范围**

```netdiscover -l [ranges.txt]```

# SYNOPSIS

**netdiscover** [_options_]

# PARAMETERS

**-r** _RANGE_
> 要扫描的 IP 范围。

**-p**
> 被动模式（仅监听）。

**-i** _IFACE_
> 网络接口。

**-f**
> 快速模式。

**-l** _FILE_
> 从文件读取 IP 范围。

**--help**
> 显示帮助信息。

# DESCRIPTION

**netdiscover** 使用 ARP 发现网络中的主机。它可以找到本地网络中的活动主机。

该工具发送 ARP 请求，并显示 MAC 地址和设备厂商。

# CAVEATS

需要 root 权限。仅限本地网络。可能触发 IDS 告警。

# HISTORY

netdiscover 是为**网络侦察**和发现本地网络主机而创建的。

# INSTALL

```apt: sudo apt install netdiscover```

```zypper: sudo zypper install netdiscover```

```nix: nix profile install nixpkgs#netdiscover```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[arp-scan](/man/arp-scan)(1), [nmap](/man/nmap)(1), [arping](/man/arping)(1)
