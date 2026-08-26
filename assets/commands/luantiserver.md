# TAGLINE

运行 Luanti 专用游戏服务器

# TLDR

**启动 Luanti 服务器**

```luantiserver```

**以指定世界**和游戏启动

```luantiserver --world [/path/to/world] --gameid [minetest_game]```

**在指定端口启动**

```luantiserver --port [30000]```

**以交互式终端**和详细日志启动

```luantiserver --terminal --verbose```

**以自定义配置文件**和日志文件启动

```luantiserver --config [/path/to/minetest.conf] --logfile [/path/to/server.log]```

# SYNOPSIS

**luantiserver** [_options_]

# PARAMETERS

**--world** _path_
> 世界目录路径。

**--worldname** _name_
> 按名称设置世界路径。

**--port** _port_
> 设置网络端口（UDP）。默认为 30000。

**--gameid** _id_ | **list**
> 设置要使用的游戏 ID，或列出可用的游戏。

**--config** _file_
> 从指定文件加载配置。

**--logfile** _file_
> 设置日志文件路径（'' 表示不记录日志）。

**--terminal**
> 运行期间基于 ncurses 显示交互式终端。

**--info**
> 向控制台打印更多信息。

**--verbose**
> 向控制台打印更多细节信息。

**--trace**
> 向控制台打印海量信息。

**--quiet**
> 只向控制台打印错误。

**--migrate** _backend_
> 将当前的地图后端迁移为其他后端（sqlite3、leveldb、postgresql、redis）。

**--migrate-players** _backend_
> 将当前的玩家数据后端迁移为其他后端（sqlite3、leveldb、postgresql、files）。

**--migrate-auth** _backend_
> 将当前的身份验证后端迁移为其他后端（sqlite3、leveldb、files）。

**--go**
> 直接运行服务器而不启动客户端。

**--help**
> 打印可用选项并退出。

**--version**
> 打印版本信息并退出。

# DESCRIPTION

**luantiserver** 运行 Luanti 的专用游戏服务器。Luanti（前身为 Minetest）是一个开源的体素游戏创作平台。该服务器托管支持完整 mod 功能的多人世界，默认使用 UDP 端口 30000。

# CAVEATS

Luanti 仅使用 UDP 协议；防火墙可以安全地丢弃所有其他流量。--terminal 选项需要在编译时启用 ncurses 支持。

# HISTORY

Luanti 原名 **Minetest**，于 **2024 年**更名。它是一个开源的体素游戏引擎和平台，拥有活跃的 mod 社区。

# INSTALL

```zypper: sudo zypper install luantiserver```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[luanti](/man/luanti)(1), [minetestserver](/man/minetestserver)(1), [minetest](/man/minetest)(1)
