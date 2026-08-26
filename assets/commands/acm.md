# TAGLINE

联网空战飞行模拟器

# TLDR

**启动**空战游戏

```acm```

连接**服务器**进行多人游戏

```acm -server [hostname]```

作为服务器主持**多人游戏**

```acm -host```

为多人游戏设置**呼号**

```acm -name [callsign]```

# SYNOPSIS

**acm** [_-server host_] [_-host_] [_-name callsign_] [_options_]

# DESCRIPTION

**acm**（Aerial Combat Multiplayer）是一款飞行战斗模拟器，允许玩家之间进行网络空战缠斗。游戏模拟多种机型的空战，具有逼真的飞行动力学和武器系统。

游戏可以单人对战 AI 对手，也可以通过网络进行多人对战。玩家驾驶喷气式战机，使用机炮和导弹进行空对空作战。

# PARAMETERS

**-server** _host_
> 连接到指定的多人游戏服务器

**-host**
> 以多人游戏服务器身份运行

**-name** _callsign_
> 设置你的飞行员呼号

**-plane** _type_
> 选择机型

**-team** _n_
> 加入指定的队伍编号

**-geometry** _WxH_
> 设置窗口几何尺寸

# CAVEATS

显示需要 X Window System。网络对战需要对 UDP 流量正确配置防火墙。性能取决于图形硬件；多人游戏的体验还受网络延迟影响。

# HISTORY

**acm** 开发于 **20 世纪 90 年代**初，是最早面向 Unix/X11 系统的联网多人战斗飞行模拟器之一。在网络游戏主要还局限于专用游戏平台的时代，它展示了 Unix 工作站上联网游戏的潜力。

# SEE ALSO

[xpilot](/man/xpilot)(1)
