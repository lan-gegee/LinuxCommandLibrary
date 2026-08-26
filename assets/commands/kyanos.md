# TAGLINE

基于 eBPF 的网络分析与追踪工具

# TLDR

**查看 HTTP 流量**

```kyanos watch http```

**查看特定端口上的流量**

```kyanos watch --port [port]```

**按进程 ID 过滤查看流量**

```kyanos watch --pids [1234]```

**按容器 ID 过滤查看流量**

```kyanos watch --container-id [abc123]```

**按键过滤查看 Redis 流量**

```kyanos watch redis --keys [my-key1,my-key2]```

**显示网络统计信息**

```kyanos stat```

**显示外部依赖概览**

```kyanos overview```

# SYNOPSIS

**kyanos** _command_ [_options_]

# DESCRIPTION

**kyanos** 是一款基于 eBPF 的网络分析工具，可以将数据包在内核中耗费的时间可视化，捕获 HTTP、Redis、MySQL 等协议的请求与响应，从而提升故障排查效率。

它提供三个子命令：**watch** 用于捕获网络流量，并可按 IP、端口、进程、容器或协议层细节进行过滤；**stat** 用于聚合请求/响应数据并给出统计信息；**overview** 用于展示本机所依赖的外部资源。它还能自动解密 SSL 流量。

该工具提供内核级追踪点，呈现数据包从网卡到达直到进入内核套接字缓冲区的完整路径，并以可视化形式展示，帮助精确定位造成延迟的阶段。

# CAVEATS

要求 Linux 内核版本为 3.10（自 3.10.0-957 起）或 4.14 及以上。eBPF 操作需要 root 权限。仅支持 amd64 和 arm64 架构。

# HISTORY

**kyanos** 由 **hengyoush** 创建，主体使用 **Go** 编写，eBPF 程序部分使用 **C**。它的设计目标是成为轻量且几乎零依赖的网络分析工具——只需一个二进制文件即可运行。

# SEE ALSO

[tcpdump](/man/tcpdump)(8), [wireshark](/man/wireshark)(1), [bpftrace](/man/bpftrace)(8)
