# TAGLINE

ARK 生存游戏专用服务器

# TLDR

以**指定地图**启动服务器

```[path/to]/ArkAscendedServer [TheIsland_WP]```

带**会话名称、密码**启动

```[path/to]/ArkAscendedServer [TheIsland_WP]?SessionName=[name]?ServerPassword=[pass]?ServerAdminPassword=[admin_pass]```

以**指定端口**和最大玩家数启动

```[path/to]/ArkAscendedServer [TheIsland_WP] -port=[7777] -WinLiveMaxPlayers=[1..70]```

启用 **PvE 模式**（禁用 PvP）

```[path/to]/ArkAscendedServer [TheIsland_WP]?ServerPVE=true```

设置**难度倍率**

```[path/to]/ArkAscendedServer [TheIsland_WP]?DifficultyOffset=[1.0]```

按 ID 启用**指定模组**

```[path/to]/ArkAscendedServer [TheIsland_WP] -mods=[mod_id1,mod_id2,...]```

允许来自**特定平台**的连接

```[path/to]/ArkAscendedServer [TheIsland_WP] -ServerPlatform=[PC+XSX+PS5]```

# SYNOPSIS

**ArkAscendedServer** _map_ [_?options_] [_-flags_]

# DESCRIPTION

**ArkAscendedServer** 为 ARK: Survival Ascended 运行无界面的专用服务器，这是原版生存游戏基于虚幻引擎 5 的重制版。它支持托管多人游戏会话，可配置地图、模组和玩法设定。

服务器选项有两种传递方式：玩法设置使用 URL 风格的查询参数（以 **?** 连接），技术配置使用命令行标志（以 **-** 开头）。

# PARAMETERS

**SessionName=**_name_
> 设置服务器在服务器浏览器中的显示名称

**ServerPassword=**_password_
> 要求输入密码才能加入服务器

**ServerAdminPassword=**_password_
> 设置 RCON 和游戏内管理员命令的管理员密码

**ServerPVE=true**
> 启用 PvE 模式，禁用玩家对战

**DifficultyOffset=**_value_
> 缩放难度（影响野生生物等级）

**-port=**_number_
> 服务器的网络端口

**-WinLiveMaxPlayers=**_count_
> 最大玩家数（1-70）

**-mods=**_ids_
> 要启用的模组 ID 列表（逗号分隔）

**-ServerPlatform=**_platforms_
> 允许跨平台连接（PC、XSX、PS5）

**-clusterid=**_id_, **-ClusterDirOverride=**_path_
> 使用给定的集群 ID 和共享数据目录加入服务器集群（共享玩家/恐龙转移）

**-NoBattlEye**
> 不带 BattlEye 反作弊运行服务器（客户端也必须禁用它）

# CONFIGURATION

**ShooterGame/Saved/Config/WindowsServer/GameUserSettings.ini**
> 主服务器配置，包括会话设置、管理员密码、玩家上限和玩法选项。

**ShooterGame/Saved/Config/WindowsServer/Game.ini**
> 高级玩法覆盖设置，涉及印痕技能、战利品表、生物生成和制作配方。

# CAVEATS

需要大量系统资源（建议 16GB 以上内存）。服务器文件必须通过 SteamCMD 安装。要持久化配置需编辑 GameUserSettings.ini 和 Game.ini 文件。

# SEE ALSO

[steamcmd](/man/steamcmd)(1), [ark-survival-evolved](/man/ark-survival-evolved)(1)
