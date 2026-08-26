# TAGLINE

多人 FPS 专用服务器

# TLDR

运行**休闲模式游戏服务器**

```[path/to]/cs2 -dedicated +game_type 0 +game_mode 0 +map [de_dust2]```

运行**竞技模式游戏服务器**

```[path/to]/cs2 -dedicated +game_type 0 +game_mode 1 +map [de_dust2]```

以指定的 **IP、端口和最大玩家数**运行

```[path/to]/cs2 -dedicated +map [de_dust2] -ip [1.2.3.4] -port [27015] -maxplayers [10]```

使用 **Steam 身份验证令牌**运行

```[path/to]/cs2 -dedicated +map [de_dust2] +sv_setsteamaccount [token]```

# SYNOPSIS

**cs2** [_options_] [+_commands_]

# DESCRIPTION

**Counter-Strike 2** 专用服务器为多人对局托管无界面的游戏服务器。它在没有图形界面的情况下运行，可通过控制台命令或 RCON（远程控制台）进行远程管理。

服务器可以通过命令行参数、控制台命令和配置文件进行配置。它支持自定义游戏模式、地图、插件和管理控制。专用服务器是举办竞技比赛、社区服务器以及具有特定规则设置的私人对局的关键。

服务器性能取决于玩家数量、tick 频率和可用系统资源。专用服务器通过 SteamCMD 分发，运行需要 Steam 身份验证。

# PARAMETERS

**-dedicated**
> 以专用服务器方式运行（无界面，无 GUI）

**+map** _mapname_
> 指定要加载的地图（如 de_dust2、de_mirage）

**+game_type** _type_
> 游戏类型（0 = 经典，1 = 军备竞赛/爆破/死亡竞赛）

**+game_mode** _mode_
> 游戏模式（随 game_type 变化，如 0 = 休闲，1 = 竞技）

**+mapgroup** _group_
> 要使用的地图组（如 mg_active、mg_allclassic）

**-maxplayers** _count_
> 最大玩家数量

**-ip** _address_
> 要绑定的服务器 IP 地址

**-port** _port_
> 服务器端口（默认：27015）

**-insecure**
> 禁用 VAC 反作弊

**-usercon**
> 启用 RCON 远程控制台管理

**+hostname** _name_
> 设置服务器的显示名称

**+sv_lan** _0|1_
> 切换仅限局域网模式（1 = 局域网，0 = 互联网）

**+sv_password** _password_
> 要求输入密码才能加入服务器

**+rcon_password** _password_
> 设置 RCON 管理密码

**+sv_setsteamaccount** _token_
> 用于 Steam 身份验证的游戏服务器登录令牌

# CONSOLE COMMANDS

**quit**
> 关闭服务器

**changelevel** _map_
> 切换到其他地图

**status**
> 显示服务器状态

# CONFIGURATION

**game/csgo/cfg/server.cfg**
> 服务器配置，包括主机名、密码、游戏规则和管理设置。

# CAVEATS

需要 Steam 和有效的游戏文件。服务器硬件需求取决于玩家数量。公开服务器还需要网络配置（端口转发、防火墙）。

# SEE ALSO

[steamcmd](/man/steamcmd)(1)
