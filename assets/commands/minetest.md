# TAGLINE

类似 Minecraft 的开源体素游戏引擎和沙盒游戏

# TLDR

**启动 Minetest 客户端**

```minetest```

**连接到服务器**

```minetest --address [server.example.com] --port [30000]```

**以指定游戏启动**

```minetest --gameid [minetest_game]```

**以终端模式运行**

```minetest --terminal```

# SYNOPSIS

**minetest** [_options_]

# PARAMETERS

**--address** _host_
> 要连接的服务器地址。

**--port** _port_
> 服务器端口（默认 30000）。

**--name** _name_
> 玩家名称。

**--password** _pass_
> 玩家密码。

**--gameid** _id_
> 要使用的游戏 ID。

**--world** _path_
> 世界目录。

**--config** _file_
> 配置文件。

**--terminal**
> 以终端模式运行。

**--go**
> 禁用主菜单，直接连接到指定的服务器。

**--server**
> 作为专用服务器（无界面）运行。

**--map-dir** _path_
> 作为服务器运行时的世界地图目录。

**--logfile** _file_
> 记录日志到文件（除控制台外）。

**--run-unittests**
> 运行内置单元测试后退出。

**--videomodes**
> 显示可用的视频模式。

**--speedtests**
> 运行速度测试后退出。

**--info**
> 打印信息后退出。

# DESCRIPTION

**minetest** 是一个类似 Minecraft 的开源体素游戏引擎和沙盒游戏。它支持客户端和专用服务器两种模式、多人游戏、模组和自定义内容。该引擎通过 Lua 脚本和内容包具有高度可扩展性。

游戏、模组和材质包通过内置的内容浏览器管理，或放置在 **~/.minetest/**（Linux）、**~/Library/Application Support/minetest/**（macOS）中。默认游戏是 **Minetest Game**，但还有许多社区游戏。

配置存储在用户数据目录的 **minetest.conf** 中。

# CAVEATS

**--go** 参数需要同时设置 **--address**。使用 **--server** 作为服务器运行时需要世界目录（默认为找到的第一个世界）。客户端需要 OpenGL 支持。

# INSTALL

```dnf: sudo dnf install minetest```

```pacman: sudo pacman -S luanti```

```apk: sudo apk add luanti```

```zypper: sudo zypper install luanti```

```nix: nix profile install nixpkgs#luanti```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[minetestserver](/man/minetestserver)(1)
