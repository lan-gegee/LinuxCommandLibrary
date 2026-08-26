# TAGLINE

网络连接查看与监控工具

# TLDR

显示网络连接

```trawl```

显示所有连接

```trawl -a```

按进程过滤

```trawl -p [pid]```

仅显示监听中的连接

```trawl -l```

监控模式

```trawl -w```

# SYNOPSIS

**trawl** [_-a_] [_-l_] [_-p pid_] [_-w_] [_options_]

# PARAMETERS

**-a**
> 所有连接。

**-l**
> 仅监听中的连接。

**-p** _PID_
> 按进程过滤。

**-w**
> 监控模式。

**-n**
> 数字化输出。

**--help**
> 显示帮助。

# DESCRIPTION

**trawl** 是一个网络连接查看器，用于显示系统上活动的 TCP 连接信息。它展示的详细信息包括本地和远程地址、连接状态，以及与每个连接关联的进程。

监控模式提供持续更新，定期刷新连接列表以实现实时监控。可以按进程 ID 过滤连接，从而聚焦特定应用的网络活动；仅监听模式则显示等待传入连接的套接字。

输出设计得简洁易读，并提供数字化显示选项以避免 DNS 解析延迟。

# CAVEATS

可能需要 root 权限。与平台相关。属于网络工具。

# HISTORY

**trawl** 是一个网络连接查看器，提供活动 TCP 连接的相关信息。

# SEE ALSO

[ss](/man/ss)(1), [netstat](/man/netstat)(1), [lsof](/man/lsof)(1)
