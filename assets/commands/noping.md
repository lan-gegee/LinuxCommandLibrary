# TAGLINE

基于 Ncurses 的多主机可视化 ping 工具

# TLDR

以可视化方式**同时 ping 多个主机**

```noping [host1] [host2] [host3]```

**以特定间隔 ping**（单位为秒，支持小数）

```noping -i [seconds] [host]```

**发送指定数量的 ping 后**退出

```noping -c [count] [host]```

**强制使用 IPv4 或 IPv6**

```noping -4 [host]```

**从文件读取主机列表**

```noping -f [hosts.txt]```

**将测量结果写入 CSV 文件**

```noping -O [output.csv] [host1] [host2]```

**选择图形类型**（none、prettyping、boxplot、histogram）

```noping -g [prettyping] [host]```

# SYNOPSIS

**noping** [_-4_ | _-6_] [_-c count_] [_-i interval_] _host_ [_host_...]
**noping** [_-4_ | _-6_] [_-c count_] [_-i interval_] **-f** _filename_

# PARAMETERS

**-4**
> 强制使用 IPv4。

**-6**
> 强制使用 IPv6。

**-c** _COUNT_
> 发送并接收 COUNT 个 ICMP 包，然后停止并退出。

**-i** _INTERVAL_
> 每隔 INTERVAL 秒向每个主机发送一个 ICMP 包。支持浮点数以实现亚秒级精度。

**-w** _TIMEOUT_
> 等待 ECHO REPLY 的超时时间（秒）。默认为 1.0。

**-t** _TTL_
> 设置 IP 生存时间 TTL（1-255）。默认为 64。

**-I** _ADDRESS_
> 设置源地址（IP 或主机名）。

**-D** _DEVICE_
> 设置发出数据包的网络设备。

**-f** _FILENAME_
> 从 FILENAME 读取主机名而非命令行参数。用 - 表示 stdin。

**-O** _FILENAME_
> 将测量结果以 CSV 格式写入 FILENAME。

**-g** _TYPE_
> 选择图形类型：none、prettyping、boxplot 或 histogram。

**-Q** _QOS_
> 为发出的数据包指定服务质量（QoS）。

**-b**
> 声音提示；收到数据包时输出 ASCII BEL 字符。

**-P** _PERCENT_
> 配置要报告的延迟百分位（0-100，不含端点）。

**-Z** _PERCENT_
> 如果任一主机的丢包率超过此百分比，则以非零状态退出。

**-u**
> 强制 UTF-8 输出。

**-U**
> 禁用 UTF-8 输出。

# DESCRIPTION

**noping** 是 liboping 的 ncurses 前端，可使用 IPv4 和/或 IPv6 并行 ping 多个主机，并在终端中实时显示统计信息。往返时间（RTT）以颜色标记：绿色表示正常，黄色表示轻度异常，红色表示明显偏离正常值。

支持多种图形类型，可用 **g** 键切换。随时可用 **a** 键添加新主机。显示模式包括基于时间的图形和展示 RTT 分布的箱线图。

# CAVEATS

访问 ICMP 可能需要 root 权限或 CAP_NET_RAW 能力。

# HISTORY

**noping** 是 **Florian Forster**（octo）的 **liboping** 项目的一部分，使用 **C** 编写。

# INSTALL

```apt: sudo apt install oping```

```dnf: sudo dnf install liboping```

```apk: sudo apk add liboping```

```zypper: sudo zypper install oping```

```brew: brew install liboping```

```nix: nix profile install nixpkgs#liboping```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ping](/man/ping)(8), [mtr](/man/mtr)(8), [fping](/man/fping)(8), [traceroute](/man/traceroute)(8)
