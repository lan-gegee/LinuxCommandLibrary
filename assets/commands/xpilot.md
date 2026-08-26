# TAGLINE

多人太空对战游戏

# TLDR

**启动游戏**并连接到服务器

```xpilot```

**连接到指定服务器**

```xpilot -join [server_address]```

**为本次会话设置玩家名称**

```xpilot -name "[player_name]"```

**选择队伍后连接**

```xpilot -join [server] -team [team_number]```

**使用特定的飞船外形**

```xpilot -shipShape "[shape_string]"```

**列出网络上可用的服务器**

```xpilot -list```

**以指定显示器启动**

```xpilot -display [hostname:0]```

# SYNOPSIS

**xpilot** [_-display host:n_] [_-join server_] [_-name name_] [_-team n_] [_-list_] [_-port n_] [_-shipShape shape_] [_options_]

# PARAMETERS

**-display** _host:n_
> 连接到指定显示器上的 X server。

**-join** _server_
> 直接连接到指定游戏服务器。

**-name** _name_
> 设置玩家名称（默认：登录名）。

**-team** _n_
> 加入指定队伍编号。

**-list**
> 查询并列出网络上可用的服务器。

**-port** _n_
> 使用指定端口号连接服务器。

**-shipShape** _shape_
> 使用外形字符串定义自定义飞船外观。

**-geometry** _WxH+X+Y_
> 设置窗口几何尺寸。

**-fps** _n_
> 目标帧率。

**-keyTurnLeft** _key_
> 绑定左转按键。

**-keyTurnRight** _key_
> 绑定右转按键。

**-keyThrust** _key_
> 绑定推进按键。

**-keyFire** _key_
> 绑定开火按键。

**-help**
> 显示帮助与可用选项。

# DESCRIPTION

**XPilot** 是一款面向 X Window System 的多人战术太空对战游戏。玩家在 2D 场地中驾驶航天器，与其他人竞争多种游戏模式，包括团队战斗、夺旗和生存赛。

游戏采用包含动量与重力的牛顿物理，要求玩家熟练掌握推进与旋转操作来机动。飞船可以收集道具，获得导弹、激光和地雷等武器。玩法强调导航技巧和战斗时机的把握。

玩家连接到托管游戏地图并管理比赛的服务器。多个客户端可以连接到同一台服务器进行对抗。游戏同时支持互联网对战和局域网会话。可以使用飞船外形规范语言创建自定义飞船设计。

XPilot 拥有活跃的社区以及多个分支和增强版本。可以通过命令行选项或用户主目录中的 **.xpilotrc** 配置文件自定义配置。

# CAVEATS

需要 X11 显示。网络延迟会显著影响互联网服务器上的游戏体验。某些服务器可能运行着规则或物理特性不同的修改版。原版 XPilot 已被 XPilot-AI 和 XPilot NG 等功能更强的分支取代。

# HISTORY

**XPilot** 由 Bjorn Stabell 和 Ken Ronny Schouten 创建，于 **1991 年**首次公开发布。它是 Unix 系统上最早流行的联网多人游戏之一。整个 20 世纪 90 年代，世界各地都有服务器运行该游戏，积累了忠实的玩家群体。后来出现了多个分支，其中 XPilot NG（Next Generation）现代化了代码库并添加了新功能。

# INSTALL

```aur: yay -S xpilot```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xpilot-ng](/man/xpilot-ng)(1), [xscreensaver](/man/xscreensaver)(1)
