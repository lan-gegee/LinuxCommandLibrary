# TAGLINE

下一代多人太空对战游戏

# TLDR

**启动游戏客户端**

```xpilot-ng-x11```

**启动 SDL/OpenGL 客户端**

```xpilot-ng-sdl```

**连接到指定服务器**

```xpilot-ng-x11 -join [server.example.com]```

**启动本地服务器**

```xpilot-ng-server```

**使用地图启动服务器**

```xpilot-ng-server -map [/path/to/map.xp2]```

**列出公共服务器**

```xpilot-ng-x11 -list```

# SYNOPSIS

**xpilot-ng-x11** [_options_]

**xpilot-ng-server** [_options_]

# CLIENT PARAMETERS

**-join** _server_
> 连接到指定服务器。

**-name** _name_
> 玩家名称。

**-team** _num_
> 加入指定队伍。

**-list**
> 列出可用服务器。

**-port** _num_
> 服务器端口（默认：15345）。

# SERVER PARAMETERS

**-map** _file_
> 加载指定的地图文件。

**-port** _num_
> 监听端口（默认：15345）。

**-contactPort** _num_
> 元服务器联系端口。

**-password** _pass_
> 服务器密码。

# DESCRIPTION

**xpilot-ng**（XPilot Next Generation）是一款多人太空对战游戏，玩家驾驶飞船、收集道具，并在多种游戏模式中竞技，包括死亡竞赛、夺旗和竞速。

NG 版本采用多边形地图、通过 SDL 客户端实现 OpenGL 图形，性能较原版 XPilot 有所提升。玩家连接到托管对局的服务器；中央元服务器会列出可用的公共服务器。

/etc/xpilot-ng/defaults.txt 中的服务器配置可控制大量玩法选项，包括重力、武器、计分和物理规则。客户端设置保存在 ~/.xpilotrc 中。

# CAVEATS

多人游戏需要网络连接。公共服务器的可用性各不相同。X11 客户端需要 X server；SDL 客户端需要 OpenGL 支持。

# HISTORY

**XPilot** 由 Bjørn Stabell 和 Ken Schouten 于 1991 年在特罗姆瑟大学创建。XPilot NG 于 2000 年分支出独立版本，加入了多边形地图和 OpenGL 渲染。它是最古老的持续运营在线多人游戏之一。

# INSTALL

```dnf: sudo dnf install xpilot-ng```

```nix: nix profile install nixpkgs#xpilot-ng```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xpilot](/man/xpilot)(6)
