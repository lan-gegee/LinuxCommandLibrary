# TAGLINE

运行专用多人游戏服务器。

# TLDR

在前台**启动**专用服务器

```[path/to]/DedicatedServer```

在自定义端口上**运行**（需事先在 serversettings.xml 中配置）

```[path/to]/DedicatedServer -port [27015]```

通过 SteamCMD **安装或更新**服务器

```steamcmd +login anonymous +app_update [1026340] validate +quit```

# SYNOPSIS

**DedicatedServer** [_options_]

# DESCRIPTION

**DedicatedServer** 是 **Undertow Games** 为 **Barotrauma** 发行的无头游戏服务器；Barotrauma 是一款设定在木星卫星欧罗巴上的 2D 合作潜艇生存游戏。该二进制程序监听玩家连接、运行模拟，并充当回合状态的权威主机。

服务器行为几乎完全由游戏目录中的 **serversettings.xml** 驱动：玩家槽位数、密码、允许的模组、游戏模式（战役、沙盒、任务、PvP）以及 karma 设置。服务器下载的创意工坊内容位于 **WorkshopMods/** 下。还可以在运行时通过游戏内控制台（以 **/** 为前缀的命令）控制服务器。

# CONFIGURATION

**serversettings.xml**
> 主服务器配置文件。控制游戏设置、玩家槽位、密码、允许的模组以及大多数运行时参数。

**config_player.xml**
> 服务器端玩家配置（管理员列表、被封禁 IP 也保存在此）。

**servermessages.txt**
> 可选的每日轮播消息文件，向连接的玩家显示。

# CAVEATS

需要 Barotrauma 专用服务器文件（Steam 应用 ID **1026340**）。设置必须在启动前编写完成；目前服务器没有提供丰富的 CLI。面向互联网的部署需要对配置端口（默认 **27015**）进行 UDP 端口转发，客户端加入时可能还需要 Steam 认证。

# HISTORY

**Barotrauma** 于 **2019** 年开启抢先体验，并于 **2023** 年达到 **1.0** 版本。专用服务器二进制程序在整个游戏生命周期中都与游戏客户端一同发行，并可通过 Steam 自由再分发。

# SEE ALSO

[steamcmd](/man/steamcmd)(1)
