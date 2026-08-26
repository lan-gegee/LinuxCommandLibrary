# TAGLINE

在 Linux 上运行 Palworld 专用游戏服务器

# TLDR

以**默认**设置启动服务器

```[path/to]/PalServer.sh```

以指定的**端口**和**玩家数量**启动

```[path/to]/PalServer.sh -port=[8211] -players=[16]```

作为**公开**大厅启动

```[path/to]/PalServer.sh -publiclobby```

启用**多线程**优化启动

```[path/to]/PalServer.sh -useperfthreads -NoAsyncLoadingThread -UseMultithreadForDS```

使用公网 IP 启动**社区服务器**

```[path/to]/PalServer.sh -publicip=[ip_address] -publicport=[port]```

# SYNOPSIS

**PalServer.sh** [**-port=**_port_] [**-players=**_count_] [**-publiclobby**] [**-publicip=**_ip_] [**-publicport=**_port_]

# PARAMETERS

**-port=_port_**
> 服务器端口号（默认：8211）

**-players=_count_**
> 最大玩家数（1-32）

**-publiclobby**
> 让服务器显示在公共服务器列表中

**-publicip=_ip_**
> 社区服务器使用的公网 IP 地址

**-publicport=_port_**
> 社区服务器使用的公网端口

**-useperfthreads**
> 启用性能线程优化

**-NoAsyncLoadingThread**
> 禁用异步加载以提高稳定性

**-UseMultithreadForDS**
> 为专用服务器启用多线程

# DESCRIPTION

**PalServer.sh** 在 Linux 上运行 Palworld 专用游戏服务器。Palworld 是一款包含生物收集和基地建造玩法的多人生存游戏。专用服务器可以为多名玩家托管持久化世界。

该服务器需要 Steam 和 SteamCMD 进行安装。配置通过命令行参数和 PalWorldSettings.ini 文件完成。

# CAVEATS

需要大量系统资源（建议 8 GB 以上内存）。公共服务器需要端口转发。玩家连接需要 Steam 身份验证。建议定期备份世界数据。

# HISTORY

**Palworld** 由 **Pocketpair** 开发，于 2024 年 1 月以抢先体验形式发布。专用服务器支持让社区能够在 Linux 系统上托管游戏，将游戏的多人玩法扩展到点对点连接之外。

# SEE ALSO

[steamcmd](/man/steamcmd)(1), [screen](/man/screen)(1), [tmux](/man/tmux)(1)
