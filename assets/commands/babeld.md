# TAGLINE

避免环路的距离向量路由协议守护进程。

# TLDR

**启动**Babel 路由守护进程

```babeld [eth0]```

使用**配置文件**启动

```babeld -c [/etc/babeld.conf] [eth0]```

以**前台**方式运行

```babeld -d [1] [eth0]```

**多个接口**

```babeld [eth0] [eth1] [wlan0]```

# SYNOPSIS

**babeld** [_options_] _interface_...

# DESCRIPTION

**babeld** 是一个避免环路的距离向量路由协议守护进程。Babel 面向 IPv6 和 IPv4 网络设计，特别适合无线网状网络，收敛速度快且开销低。

该守护进程实现了 Babel 路由协议（RFC 8966），适用于中小型网络。

# PARAMETERS

**-c** _file_
> 配置文件（可重复指定）。

**-C** _statement_
> 通过命令行提供配置语句。

**-d** _level_
> 调试级别（0-3）。

**-D**
> 启动时转为守护进程运行。

**-L** _file_
> 日志文件位置。

**-I** _file_
> PID 文件位置。

**-S** _file_
> 状态文件，用于在多次运行之间保留长期信息。

**-h** _seconds_
> 无线接口的 Hello 包发送间隔（默认：4s）。

**-H** _seconds_
> 有线接口的 Hello 包发送间隔（默认：4s）。

**-m** _address_
> 链路本地多播地址（默认：ff02:0:0:0:0:0:1:6）。

**-p** _port_
> UDP 端口号（默认：6696）。

**-k** _priority_
> 内核路由安装优先级（默认：0）。

**-g** _port|path_
> 启用只读配置服务器。

**-G** _port|path_
> 启用读写配置服务器。

**-t** _table_
> 用于插入路由的内核路由表。

**-w**
> 默认将所有接口视为无线接口。

**-s**
> 在有线接口上禁用水平分割（split-horizon）。

**-r**
> 使用随机 router-id，而不是从 MAC 地址推导。

**-l**
> 使用 IFF_RUNNING 来检测接口可用性。

# FEATURES

- 无环路由
- 快速收敛
- 支持 IPv4 和 IPv6
- 链路质量感知
- 多种路由度量
- 可通过配置进行扩展

# CONFIGURATION

**/etc/babeld.conf**
> 主配置文件，用于接口设置、过滤器和路由重分发规则。

# CAVEATS

需要正确的网络配置。所有节点必须运行兼容的 Babel 实现。无线网络需要启用链路质量扩展。不适合大规模网络（请使用 BGP/OSPF）。配置错误可能导致路由环路。

# HISTORY

**Babel** 由 Juliusz Chroboczek 于 **2008** 年前后设计，是为网状网络打造的一种改进型距离向量协议，后来标准化为 RFC 6126，随后更新为 RFC 8966。

# INSTALL

```apt: sudo apt install babeld```

```dnf: sudo dnf install babeld```

```pacman: sudo pacman -S babeld```

```apk: sudo apk add babeld```

```brew: brew install babeld```

```nix: nix profile install nixpkgs#babeld```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[bird](/man/bird)(1), [route](/man/route)(8), [ip](/man/ip)(8), [traceroute](/man/traceroute)(1)
