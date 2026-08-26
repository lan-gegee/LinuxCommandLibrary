# TAGLINE

实时监视网络状态变化并输出到 stdout

# TLDR

**监视**所有网络状态变化

```ip monitor```

监视**特定**事件类型

```ip monitor [link|address|route|neigh|rule|maddress]```

**回放**由 rtmon 生成的记录文件

```ip monitor file [path/to/file]```

# SYNOPSIS

**ip monitor** [_type_] [_options_]

# PARAMETERS

**link**
> 监视链路状态变化

**address**
> 监视地址变化

**route**
> 监视路由表变化

**neigh**
> 监视邻居/ARP 表变化

**rule**
> 监视策略路由规则变化

**maddress**
> 监视组播地址变化

**file** _FILE_
> 从文件回放事件（由 rtmon 生成）

# DESCRIPTION

**ip monitor** 实时监视网络状态变化并将其报告到 stdout。它使用 netlink 套接字接收内核关于网络配置变更的通知。

这可用于调试网络问题、监视动态变化，以及了解网络配置随时间的演变。可以同时监视多种事件类型。

# CAVEATS

监视需要适当的权限才能访问 netlink 套接字。在繁忙的系统上输出可能非常冗长。事件会实时报告，但可能被缓冲。

# HISTORY

ip monitor 是 iproute2 的一部分，由 Alexey Kuznetsov 开发。它所使用的 netlink 接口在 Linux 2.2 中引入，并在后续内核版本中不断增强。

# SEE ALSO

[ip](/man/ip)(8), [rtmon](/man/rtmon)(8), [ss](/man/ss)(8)
