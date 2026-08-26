# TAGLINE

通过测量从主机列表中找出最快的网络服务器

# TLDR

选出**实测延迟最低**的主机

```sudo netselect [host1] [host2] [host3]```

返回**最快的 N 个**主机

```sudo netselect -s [N] [host1] [host2] [host3]```

增加详细程度，显示 **DNS 和探测统计信息**

```sudo netselect -vv [host1] [host2]```

限制探测包的 **TTL**

```sudo netselect -m [10] [host1] [host2]```

显示内置的**用法说明**（不带主机参数）

```netselect```

# SYNOPSIS

**netselect** [_options_] _hosts_...

# PARAMETERS

**-v**
> 详细模式；显示解析过程和统计信息（使用 -vv 获取更多细节）

**-m _ttl_**
> 探测包的最大 TTL（生存时间）

**-s _n_**
> 输出最快的 n 个服务器，而非仅最快的一个

**-t _n_**
> 向每台主机发送的数据包数量

**-I**
> 使用 ICMP echo 代替 UDP

# DESCRIPTION

**netselect** 通过测量数据包往返时间和路由跳数，从主机列表中确定最快的网络服务器。它发送探测包，并根据延迟和跳数的综合得分对主机排序。

输出得分按"延迟 ×（跳数）^3"计算，因此更偏向延迟低的邻近服务器。得分越低越好。

常用于挑选最快的 Debian 镜像或 DNS 服务器。配套工具 **netselect-apt** 可以自动为 Debian 系统选择镜像。

# CAVEATS

发送原始数据包需要 root 权限。结果可能因测试时的网络状况而异。某些防火墙会阻断 ICMP 数据包，从而影响结果。评分算法偏好跳数少的主机，但这并不总是最优选择。

# INSTALL

```apt: sudo apt install netselect```

```nix: nix profile install nixpkgs#netselect```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[netselect-apt](/man/netselect-apt)(1), [ping](/man/ping)(8), [traceroute](/man/traceroute)(8)
