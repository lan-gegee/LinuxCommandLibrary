# TAGLINE

按进程而非接口对带宽使用情况进行分组的网络监控工具

# TLDR

**启动** NetHogs（默认设备为 eth0）

```sudo nethogs```

监控**指定设备**上的带宽

```sudo nethogs [eth0]```

监控**多个设备**

```sudo nethogs [eth0] [wlan0]```

以秒为单位指定**刷新间隔**

```sudo nethogs -d [2]```

**跟踪模式**（输出到 stdout）

```sudo nethogs -t```

# SYNOPSIS

**nethogs** [**-d** _seconds_] [**-t**] [**-v**] [_device_...]

# PARAMETERS

**-d _seconds_**
> 刷新间隔（秒）；默认为 1

**-t**
> 跟踪模式；持续输出到 stdout

**-v**
> 视图模式；循环切换视图（0-2）

**-c _count_**
> 退出前的更新次数

**-p**
> 混杂模式（捕获所有数据包）

**-s**
> 按发送的数据量排序

**-a**
> 监控所有设备

# INTERACTIVE COMMANDS

**q**
> 退出

**s**
> 按发送字节数排序

**r**
> 按接收字节数排序

**m**
> 循环切换显示模式（KB/s、KB、B、MB）

# DESCRIPTION

**nethogs** 是一款网络监控工具，它按进程而非按接口或协议对带宽使用情况进行分组。它可以实时显示哪些进程正在消耗网络带宽。

与只显示各接口统计数据的传统网络监控工具不同，nethogs 能找出真正产生网络流量的程序，从而更容易发现占用带宽的应用。

# CAVEATS

需要 root 权限才能捕获网络数据包。在繁忙的系统上可能无法准确跟踪所有流量。仅监控 TCP 和 UDP 流量。某些短生命周期的连接可能被遗漏。

# HISTORY

**nethogs** 由 **Arnout Engelen** 开发，是一款按进程对带宽进行分组的 "net top" 工具。它填补了 iftop 和 nload 等传统工具只提供接口级统计数据的空白。

# INSTALL

```apt: sudo apt install nethogs```

```dnf: sudo dnf install nethogs```

```pacman: sudo pacman -S nethogs```

```apk: sudo apk add nethogs```

```zypper: sudo zypper install nethogs```

```brew: brew install nethogs```

```nix: nix profile install nixpkgs#nethogs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[iftop](/man/iftop)(8), [nload](/man/nload)(1), [bmon](/man/bmon)(1), [ss](/man/ss)(8)
