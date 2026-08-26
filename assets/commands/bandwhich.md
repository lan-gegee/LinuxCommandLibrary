# TAGLINE

按进程显示网络带宽占用

# TLDR

**监控**网络使用情况（需要 root）

```sudo bandwhich```

监控**指定接口**

```sudo bandwhich --interface [eth0]```

**不解析**主机名

```sudo bandwhich --no-resolve```

只显示**进程**表

```sudo bandwhich --processes```

显示**累计**总利用率

```sudo bandwhich --total-utilization```

输出**机器可读的**文本而不是 UI

```sudo bandwhich --raw```

# SYNOPSIS

**bandwhich** [_options_]

# DESCRIPTION

**bandwhich** 是一款按进程、连接和远程 IP/主机名显示当前网络利用率的 CLI 工具。它提供终端 UI，实时展示哪些程序正在占用带宽。

该工具特别适合找出高带宽应用并监控网络活动。

# PARAMETERS

**-i**, **--interface** _name_
> 监控指定的网络接口（可重复使用）。

**-r**, **--raw**
> 输出机器友好的文本，而不是交互式终端 UI。

**-n**, **--no-resolve**
> 不将 IP 地址解析为主机名。

**-s**, **--show-dns**
> 在输出中显示 DNS 查询。

**-d**, **--dns-server** _ip_
> 使用自定义 DNS 服务器进行反向查询。

**-p**, **--processes**
> 只显示进程表。

**-c**, **--connections**
> 只显示连接表。

**-a**, **--addresses**
> 只显示远程地址表。

**-t**, **--total-utilization**
> 显示累计用量统计而不是每秒速率。

**-u**, **--unit-family** _family_
> 单位格式：bin-bytes、bin-bits、si-bytes 或 si-bits。

# FEATURES

- 实时带宽监控
- 按进程统计
- 连接详情
- 远程主机识别
- 交互式终端 UI
- DNS 查询日志

# INTERFACE

显示区域：
- **Processes** - 各进程占用的带宽
- **Connections** - 活动连接
- **Remote addresses** - 按目的地统计的流量
- **Total** - 汇总统计

# CAVEATS

抓包需要 root/sudo 权限。可能无法捕获所有类型的流量。主机名解析会拖慢显示。终端必须支持所需特性。部分 VPN 流量可能无法正确归属到进程。

# HISTORY

**bandwhich** 由 Aram Drevekenin 于 **2019** 年前后创建，是 iftop 和 nethogs 等工具的现代易用替代品。它使用 Rust 编写，目前处于低强度维护状态。

# INSTALL

```pacman: sudo pacman -S bandwhich```

```apk: sudo apk add bandwhich```

```brew: brew install bandwhich```

```nix: nix profile install nixpkgs#bandwhich```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[iftop](/man/iftop)(8), [nethogs](/man/nethogs)(8), [nload](/man/nload)(1), [netstat](/man/netstat)(8)

# RESOURCES

```[Source code](https://github.com/imsnif/bandwhich)```

<!-- verified: 2026-06-19 -->
