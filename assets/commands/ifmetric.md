# TAGLINE

操作网络接口的 IPv4 路由度量值

# TLDR

设置网络接口的**优先级**（数值越大 = 优先级越低）

```sudo ifmetric [interface] [value]```

将接口的优先级**重置**为默认值

```sudo ifmetric [interface] 0```

给无线接口设置更高的度量值，使**有线**连接优先于无线

```sudo ifmetric wlan0 100```

# SYNOPSIS

**ifmetric** _interface_ _metric_

# PARAMETERS

_interface_
> 网络接口名称（如 eth0、wlan0）

_metric_
> 路由度量值（数值越大表示优先级越低，0 表示重置为默认）

# DESCRIPTION

**ifmetric** 操作网络接口的 IPv4 路由度量值。当存在多条到达同一目的地的路由时，路由度量值决定优先使用哪个接口——度量值越小优先级越高。

对于拥有多个网络连接（如有线和无线）的系统，它可用于控制出站流量优先使用哪个连接。

# CAVEATS

需要 root 权限。只影响 IPv4 路由。除非编写脚本，更改在重启后不会保留。不适用于 IPv6 路由。

# HISTORY

ifmetric 由 Lennart Poettering（后来创建了 PulseAudio 和 systemd）开发，提供了一种无需复杂 ip route 命令即可操作路由度量的简单方式。

# INSTALL

```apt: sudo apt install ifmetric```

```nix: nix profile install nixpkgs#ifmetric```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ip](/man/ip)(8), [route](/man/route)(8), [ifconfig](/man/ifconfig)(8), [ifup](/man/ifup)(8)
