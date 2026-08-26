# TAGLINE

按连接细分显示网络接口上的带宽使用情况

# TLDR

显示默认接口的**带宽使用情况**

```sudo iftop```

显示**指定接口**的带宽使用情况

```sudo iftop -i [interface]```

带**端口号**显示带宽使用情况

```sudo iftop -P```

跳过 **DNS 和服务名查询**（启动更快）

```sudo iftop -nNP```

以**字节**而非比特显示流量并隐藏条形图

```sudo iftop -Bb```

只显示流经**特定网络**的流量

```sudo iftop -F [192.168.1.0/24]```

使用 **pcap 语法**过滤（如仅 TCP 端口 80）

```sudo iftop -f "tcp port 80"```

以**文本模式**运行（无 ncurses）以便记录日志

```sudo iftop -t -s [10]```

# SYNOPSIS

**iftop** [**-hnNpPlbBt**] [**-i** _interface_] [**-f** _filter_] [**-F** _net/mask_] [**-G** _net6/mask6_] [**-m** _limit_] [**-c** _config_] [**-s** _seconds_]

# PARAMETERS

**-i** _INTERFACE_
> 监听指定的接口。

**-P**
> 在主机名之外同时显示 TCP/UDP 端口号。

**-p**
> 以混杂模式运行（统计并非发往本主机的流量）。

**-n**
> 不解析主机名（更快，在繁忙网络上更精确）。

**-N**
> 不把端口号转换为服务名。

**-l**
> 显示并统计链路本地 IPv6 地址。

**-b**
> 不显示流量条形图。

**-B**
> 以字节/秒而非比特/秒显示带宽。

**-f** _FILTER_
> 应用 pcap 过滤器（如 `"tcp port 443"`、`"not host 10.0.0.1"`）。

**-F** _NET/MASK_
> 只显示流入/流出给定 IPv4 网络的流量（如 `10.0.0.0/8`）。

**-G** _NET6/MASK6_
> **-F** 的 IPv6 等价选项。

**-m** _LIMIT_
> 设置带宽刻度的上限（如 `10M`、`100K`）。

**-c** _FILE_
> 使用备用配置文件而非 `~/.iftoprc`。

**-t**
> 文本输出模式；不使用 ncurses，直接打印到 stdout（与 **-s** 组合可定时采集）。

**-s** _SECONDS_
> 文本模式下，运行 _SECONDS_ 秒后退出。

**-h**
> 打印简短的用法摘要。

# DESCRIPTION

**iftop** 按主机对（host-pair）连接细分显示网络接口上的带宽使用情况，就像 **top** 对进程所做的那样。它使用 libpcap 进行监听，识别源/目的端点，并渲染一个大约每秒更新两次的实时 ncurses 表格。

三列速率分别显示最近 **2、10 和 40 秒**的指数加权平均值。速率默认以比特/秒为单位（使用 **-B** 改为字节）。底部显示累计总量、峰值速率以及聚合的发送/接收数据。

## Interactive commands

运行时按 **?** 获取帮助。常用按键：**s**/**d** 按源/目的聚合，**S**/**D** 切换源/目的端口，**p** 切换端口显示，**t** 循环切换显示模式，**1**/**2**/**3** 按速率列排序，**</>** 按源/目的名称排序，**n** 切换 DNS 解析，**N** 切换端口名称，**P** 暂停，**o** 冻结排序顺序，**j**/**k** 滚动，**l** 添加主机过滤器，**f** 编辑 pcap 过滤器，**q** 退出。

# CAVEATS

抓包需要 **root** 权限或 `CAP_NET_RAW` + `CAP_NET_ADMIN`。在繁忙的接口上 DNS 查询可能拖慢显示——请使用 **-n**。默认情况下 **iftop** 不以混杂模式运行；添加 **-p** 可看到并非发往本机的流量（例如在镜像交换机端口上）。**iftop** 统计的是第三层带宽，因此其总量会与包含帧开销的接口计数器略有差异。

# HISTORY

**iftop** 由牛津大学的 **Paul Warren** 编写，首次发布于 **2002 年**，明确以 **top** 为蓝本。此后它被大多数 Linux 发行版收录为标准诊断工具，也常安装在网络设备和路由器上。

# INSTALL

```apt: sudo apt install iftop```

```dnf: sudo dnf install iftop```

```pacman: sudo pacman -S iftop```

```apk: sudo apk add iftop```

```zypper: sudo zypper install iftop```

```brew: brew install iftop```

```nix: nix profile install nixpkgs#iftop```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nethogs](/man/nethogs)(8), [tcpdump](/man/tcpdump)(8), [ifstat](/man/ifstat)(1), [bmon](/man/bmon)(1), [vnstat](/man/vnstat)(1), [ss](/man/ss)(8)
