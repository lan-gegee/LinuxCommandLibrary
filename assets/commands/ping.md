# TAGLINE

使用 ICMP ECHO_REQUEST 数据包测试到主机的网络连通性

# TLDR

持续**ping 一台主机**

```ping [host]```

**ping 一台主机**指定的次数

```ping -c [5] [host]```

**以指定间隔 ping**（秒）

```ping -i [0.5] [host]```

**以指定数据包大小 ping**

```ping -s [1024] [host]```

**以指定 TTL ping**

```ping -t [64] [host]```

**ping 并只显示汇总**统计

```ping -q -c [10] [host]```

**使用 IPv6 ping**

```ping6 [host]```

收到响应时**发出声音提示**

```ping -a [host]```

# SYNOPSIS

**ping** [_options_] _destination_

**ping6** [_options_] _destination_

# PARAMETERS

**-c** _COUNT_
> 发送 COUNT 个数据包后停止

**-i** _INTERVAL_
> 数据包之间等待 INTERVAL 秒（默认：1）

**-s** _SIZE_
> 数据包数据大小，单位字节（默认：56，加上 ICMP 头共 64）

**-t** _TTL_
> 设置 IP 存活时间（TTL）

**-w** _DEADLINE_
> 无论是否收发完数据包，DEADLINE 秒后退出

**-W** _TIMEOUT_
> 每个响应最多等待 TIMEOUT 秒

**-q**
> 静默输出；只显示汇总

**-v**
> 详细输出

**-a**
> 带声音提示的 ping（收到回复时蜂鸣）

**-f**
> 泛洪 ping；尽可能快地发送数据包（仅 root）

**-n**
> 仅数字输出；不解析主机名

**-4**
> 仅使用 IPv4

**-6**
> 仅使用 IPv6

**-I** _INTERFACE_
> 使用指定的网络接口或地址

**-R**
> 记录路由（IPv4，可能被主机忽略）

**-D**
> 打印时间戳

**-Q** _TOS_
> 设置服务质量（QoS）位

**-p** _PATTERN_
> 用指定的模式字节填充数据包

# DESCRIPTION

**ping** 使用 ICMP ECHO_REQUEST 数据包测试到主机的网络连通性。它测量往返时间 (RTT) 和丢包率，是网络故障排查和监控的必备工具。

每个响应显示序号、TTL 和以毫秒计的时间。TTL 值反映了经过的路由跳数（从远程主机的初始 TTL 开始，通常为 64 或 255）。末尾的统计信息显示发送/接收的数据包数、丢包百分比以及 RTT 的 min/avg/max/mdev。

该命令需要网络访问权限，某些选项（如泛洪 ping）可能需要 root 权限。在许多系统上，IPv6 目标使用 **ping6** 或 **ping -6**。

# CAVEATS

某些主机和防火墙会拦截 ICMP 数据包，导致即使主机可达 ping 也失败。泛洪 ping (**-f**) 可能压垮网络，应谨慎使用。出于安全考虑，现代路由器通常会忽略 **-R** 记录路由选项。极小的间隔需要 root 权限。

# HISTORY

ping 命令由 **Mike Muuss** 于 **1983 年 12 月**在美国陆军弹道研究实验室编写。名称来自声呐的声音，体现了其测试远程主机是否"存在"的用途。Muuss 编写它是为了诊断网络问题，此后它成为使用最广泛的网络工具之一。最初的实现面向 BSD Unix，如今已被移植到几乎所有操作系统。

# INSTALL

```apt: sudo apt install iputils-ping```

```apk: sudo apk add iputils-ping```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[traceroute](/man/traceroute)(8), [mtr](/man/mtr)(8), [netstat](/man/netstat)(8), [ss](/man/ss)(8)
