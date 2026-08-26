# TAGLINE

体素游戏引擎和沙盒游戏

# TLDR

**启动游戏**

```luanti```

**以指定游戏启动**

```luanti --game [minetest_game]```

**仅启动服务器**

```luanti --server```

**连接到服务器**

```luanti --address [server.example.com] --port [30000]```

**以指定世界启动**

```luanti --world [/path/to/world]```

**设置玩家名称**

```luanti --name [playername]```

**迁移地图数据库**

```luanti --migrate [sqlite3] --world [/path/to/world]```

**在终端中运行**（无图形界面）

```luanti --terminal --server```

# SYNOPSIS

**luanti** [_--server_] [_--address addr_] [_--world path_] [_--game name_] [_options_]

# PARAMETERS

**--server**
> 作为专用服务器运行。

**--address** _ADDR_
> 要连接或绑定的地址。

**--port** _PORT_
> 网络端口（默认 30000）。

**--world** _PATH_
> 世界目录的路径。

**--worldname** _NAME_
> worlds 目录中的世界名称。

**--game**, **--gameid** _ID_
> 要使用的游戏。

**--name** _NAME_
> 玩家名称。

**--password** _PASS_
> 服务器密码。

**--config** _FILE_
> 配置文件。

**--info**
> 打印更多信息。

**--verbose**
> 打印更多细节信息。

**--terminal**
> 以终端模式运行（服务器）。

**--migrate** _BACKEND_
> 将世界迁移到不同的后端。

**--version**
> 打印版本号。

**--help**
> 显示帮助。

# DESCRIPTION

**Luanti**（前身为 Minetest）是一个体素游戏引擎和沙盒游戏。玩家可以在由立方体方块构成的程序化生成世界中探索、建造和改造。

该引擎通过 Lua 脚本支持 mod 扩展。游戏（games）是定义玩法、方块、合成和生物的 mod 合集。默认的 Minetest Game 提供生存模式和创造模式。

多人服务器托管持久化世界，玩家可在其中协作或竞争。服务器可以运行具有自定义规则和内容的不同游戏。

世界数据默认存储在 SQLite 中，较大的服务器可选择 LevelDB 或 PostgreSQL。地图生成使用多种算法来生成地形、洞穴和建筑结构。

内容可通过内置的内容浏览器获取，包括来自社区的游戏、mod 和纹理包。

# CAVEATS

性能取决于硬件和世界的复杂程度。大型服务器需要调优。某些 mod 之间可能冲突。该引擎于 2024 年由 Minetest 更名为 Luanti。

# HISTORY

**Minetest** 由 **Perttu Ahola**（celeron55）于 **2010 年**创建，其灵感来自 Minecraft 和 InfiniMiner。它被设计为一个开源、可扩展的体素引擎。**2024 年**，该项目更名为 **Luanti**，以建立独立于 Minecraft 的自身身份。

# INSTALL

```pacman: sudo pacman -S luanti```

```apk: sudo apk add luanti```

```zypper: sudo zypper install luanti```

```nix: nix profile install nixpkgs#luanti```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[luantiserver](/man/luantiserver)(1), [minetestserver](/man/minetestserver)(1)
