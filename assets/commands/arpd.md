# TAGLINE

带持久化存储的用户态 ARP 缓存守护进程。

# TLDR

在某个接口上**启动** ARP 守护进程，并使用数据库文件

```sudo arpd -b [/var/lib/arpd/arpd.db] [eth0]```

同时**主动解析**地址（最多发送 N 次广播查询）

```sudo arpd -a [3] -b [/var/lib/arpd/arpd.db] [eth0]```

将 ARP 数据库**转储**到标准输出并退出

```arpd -l -b [/var/lib/arpd/arpd.db]```

**抑制**内核的广播查询（让 arpd 负责询问）

```sudo arpd -k [eth0]```

# SYNOPSIS

**arpd** [_-lkh?_] [_-a N_] [_-b dbase_] [_-B number_] [_-f file_] [_-p interval_] [_-n time_] [_-R rate_] [_interface ..._]

# DESCRIPTION

**arpd** 是一个用户态 ARP 守护进程，它收集 ARP 信息并存储到数据库中。它可以直接从缓存回答内核的 ARP 请求，从而减少大型网络上的 ARP 流量。

该守护进程维护一个可在重启后保留的持久化 ARP 数据库，有助于提升网络性能并减少广播流量。

# PARAMETERS

**-l**
> 将 arpd 数据库（接口索引、IP 地址、MAC 地址）转储到标准输出并退出

**-a** _N_
> 主动发送广播 ARP 查询，在把主机标记为失效前最多尝试 _N_ 次（否则 arpd 只被动监听）

**-b** _file_
> 数据库文件的位置（默认：**/var/lib/arpd/arpd.db**）

**-f** _file_
> 从 **-l** 输出格式的文本文件读取并预加载数据库

**-k**
> 抑制内核发送的广播 ARP 查询，由 arpd 自行完成协商

**-n** _time_
> 负缓存的超时时间，单位秒（默认：60）

**-p** _interval_
> 轮询内核 ARP 表的时间间隔，单位秒（默认：30）

**-R** _rate_
> arpd 发送广播的最大稳态速率，单位为每秒数据包数（默认：1）

**-B** _number_
> arpd 可连续背靠背发送的广播数量（默认：3）

**interface**
> 要监视的网络接口

# CAVEATS

在现代网络中很少需要。ARP 缓存过期时可能引发问题。通常只在超大规模的二层网络中才有用。要使用 arpd，必须配置内核通过 **/proc/sys/net/ipv4/neigh/**_iface_**/** 中的 **app_solicit** 将未解析的地址推送给它。

# HISTORY

**arpd** 是 **iproute2** 软件包的一部分，为特定网络场景提供用户态的 ARP 表管理。

# INSTALL

```apt: sudo apt install iproute2```

```pacman: sudo pacman -S iproute2```

```zypper: sudo zypper install iproute2```

```brew: brew install iproute2```

```nix: nix profile install nixpkgs#iproute2```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[arp](/man/arp)(8), [ip-neighbour](/man/ip-neighbour)(8)

# RESOURCES

```[Source code](https://git.kernel.org/pub/scm/network/iproute2/iproute2.git)```

<!-- verified: 2026-06-15 -->
