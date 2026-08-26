# TAGLINE

显示接口的网络配置参数

# TLDR

显示**所有**网络配置

```ip netconf```

显示**特定接口**的配置

```ip netconf show dev eth0```

仅显示 **IPv4** 配置

```ip -4 netconf```

仅显示 **IPv6** 配置

```ip -6 netconf```

# SYNOPSIS

**ip** [_OPTIONS_] **netconf** { **show** [ **dev** _NAME_ ] | **help** }

# DESCRIPTION

**ip netconf** 监视并显示来自 /proc/sys/net/ipv[4|6]/conf/ 的 IPv4 和 IPv6 网络配置参数。它显示转发状态、RPF（反向路径过滤）模式、组播转发以及代理 ARP/NDP 状态等设置。若未指定接口，则显示 **all** 条目。

# PARAMETERS

**show**
> 显示网络配置（省略时为默认操作）

**dev NAME**
> 显示特定接口的配置

**help**
> 显示帮助信息

# OUTPUT FIELDS

**forwarding**
> IP 转发是否已启用

**rp_filter**
> 反向路径过滤模式（0=关闭，1=严格，2=宽松）

**mc_forwarding**
> 组播转发是否已启用

**proxy_neigh**
> 代理邻居（ARP/NDP）是否已启用

**ignore_routes_with_linkdown**
> 链路断开时忽略路由

# CAVEATS

使用 -4 或 -6 可按地址族过滤。配置只能通过 sysctl 或接口专用工具修改，无法直接通过 ip netconf 更改。

# SEE ALSO

[ip](/man/ip)(8), [ip-link](/man/ip-link)(8), [ip-address](/man/ip-address)(8), [sysctl](/man/sysctl)(8)
