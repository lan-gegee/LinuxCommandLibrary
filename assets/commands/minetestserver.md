# TAGLINE

运行专用的 Minetest 游戏服务器

# TLDR

**启动 Minetest 服务器**

```minetestserver```

**以指定世界启动**

```minetestserver --world [/path/to/world]```

**在指定端口启动**

```minetestserver --port [30000]```

**以指定游戏 ID 启动**

```minetestserver --gameid [minetest_game] --world [/path/to/world]```

# SYNOPSIS

**minetestserver** [_options_]

# PARAMETERS

**--world** _path_
> 世界目录路径。

**--port** _port_
> 服务器端口（默认 30000）。

**--gameid** _id_
> 要使用的游戏 ID。

**--config** _file_
> 配置文件。

**--logfile** _file_
> 日志输出文件。

**--terminal**
> 以终端模式运行。

**--migrate** _backend_
> 将地图数据迁移到指定后端。

# DESCRIPTION

**minetestserver** 运行专用的 Minetest 游戏服务器。无需图形客户端即可托管多人世界。支持模组、自定义游戏和玩家管理。

# INSTALL

```pacman: sudo pacman -S luanti-server```

```apk: sudo apk add luanti-server```

```nix: nix profile install nixpkgs#luanti-server```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[minetest](/man/minetest)(1)
