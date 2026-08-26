# TAGLINE

Linux 流量控制与整形

# TLDR

添加固定**延迟**

```sudo tc qdisc add dev eth0 root netem delay 100ms```

添加**可变**延迟

```sudo tc qdisc add dev eth0 root netem delay 100ms 20ms```

添加数据包**丢失**

```sudo tc qdisc add dev eth0 root netem loss 5%```

**限制**带宽

```sudo tc qdisc add dev eth0 root tbf rate 10mbit burst 32kbit latency 400ms```

**显示**生效的策略

```tc qdisc show dev eth0```

**删除**所有规则

```sudo tc qdisc delete dev eth0```

**修改**规则

```sudo tc qdisc change dev eth0 root netem delay 50ms```

# SYNOPSIS

**tc** [_OPTIONS_] _OBJECT_ _COMMAND_

# DESCRIPTION

**tc**（traffic control，流量控制）用于配置内核的数据包调度、整形和过滤。它可以模拟延迟、丢包、带宽限制等网络状况，用于测试或服务质量（QoS）管理。

# PARAMETERS

**qdisc**
> 排队规则——管理数据包排队

**add**
> 添加新的流量控制策略

**delete**
> 移除流量控制策略

**change**
> 修改现有策略

**show**
> 显示当前策略

**netem**
> 网络模拟（延迟、丢包、损坏）

**tbf**
> 令牌桶过滤器（带宽限制）

**delay** _ms_
> 为数据包增加延迟

**loss** _percent_
> 按百分比丢弃数据包

**rate** _bandwidth_
> 最大带宽速率

# CAVEATS

只影响出站流量。若要双向控制，需在两端分别配置。更改立即生效，可能中断网络连接。重启后不会保留。

# HISTORY

**tc** 是 Linux 网络工具集 **iproute2** 的组成部分，提供高级的流量整形与网络模拟能力。

# INSTALL

```apt: sudo apt install iproute2```

```pacman: sudo pacman -S iproute2```

```apk: sudo apk add iproute2-tc```

```zypper: sudo zypper install iproute2```

```brew: brew install iproute2```

```nix: nix profile install nixpkgs#iproute2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ip](/man/ip)(8), [ethtool](/man/ethtool)(8)
