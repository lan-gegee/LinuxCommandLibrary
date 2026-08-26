# TAGLINE

列出由套接字激活的单元

# TLDR

列出**活动的**套接字单元

```systemctl list-sockets```

显示**套接字类型**

```systemctl list-sockets --show-types```

列出**全部**单元（包括未激活的）

```systemctl list-sockets -a```

按**状态**过滤

```systemctl list-sockets --state [active|inactive|failed]```

按**模式**过滤

```systemctl list-sockets [pattern]```

# SYNOPSIS

**systemctl list-sockets** [_OPTIONS_] [_PATTERN_...]

# PARAMETERS

**-a, --all**
> 包括未激活和失败的套接字单元

**--state=** _STATE_
> 按状态过滤

**--show-types**
> 显示套接字类型（Stream、Datagram 等）

**--no-legend**
> 不显示表头和页脚

**--no-pager**
> 禁用分页器

# DESCRIPTION

**systemctl list-sockets** 显示当前内存中处于活动状态的套接字单元，按监听地址排序。套接字单元实现了套接字激活：当连接到达时才按需启动服务。

输出内容包括监听地址（IP:端口、路径等）、套接字单元名称及其激活的单元。

# CAVEATS

只显示 systemd 管理的套接字，而非系统上所有监听中的套接字。要查看完整列表请使用 `ss` 或 `netstat`。套接字激活可能在首次连接时造成启动延迟。

# HISTORY

**list-sockets** 子命令展示了 systemd 套接字激活基础设施的情况，该机制只在需要时启动服务，从而降低内存占用。

# SEE ALSO

[systemctl](/man/systemctl)(1), [systemctl-list-units](/man/systemctl-list-units)(1), [ss](/man/ss)(8), [netstat](/man/netstat)(8)
