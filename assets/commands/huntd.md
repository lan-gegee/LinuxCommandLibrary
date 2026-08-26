# TAGLINE

hunt 游戏的服务器守护进程

# TLDR

**启动 hunt 服务器**

```huntd```

**指定端口**

```huntd -p [9999]```

**以服务器模式运行**（永久运行）

```huntd -s```

**fork 到后台运行**（通过 syslog 记录错误）

```huntd -b```

# SYNOPSIS

**huntd** [_options_]

# PARAMETERS

**-p** _port_
> 更改用于与玩家进程会合的 UDP 端口号。

**-s**
> 以服务器模式运行（永久运行）。无人游玩时会占用一个进程表条目。

**-b**
> fork 到后台。错误改由 syslog 记录，而不是输出到标准错误。

**-a** _addr_
> 只监听指定的接口地址（以 IP 地址给出）。

# DESCRIPTION

**huntd** 是 hunt 游戏的服务器守护进程。它负责管理游戏世界并协调多名玩家。

服务器创建迷宫，并处理玩家连接、射击和计分。多名玩家通过 hunt 客户端连接。

# CAVEATS

属于 BSD games 的一部分。可以用 -s 独立运行，也可以在 inetd 下运行。不带 -s 时，所有玩家断开连接后守护进程就会退出。

# HISTORY

huntd 是 **hunt** 的服务端组件。hunt 是上世纪 80 年代的经典 BSD 网络游戏。

# SEE ALSO

[hunt](/man/hunt)(6), [bsdgames](/man/bsdgames)(6)
