# TAGLINE

为恐龙主题生存多人游戏托管专用游戏服务器。

# TLDR

以**指定地图**启动服务器

```[path/to]/ShooterGameServer [TheIsland]```

带**会话名称、密码**启动

```[path/to]/ShooterGameServer [TheIsland]?SessionName=[name]?ServerPassword=[pass]?ServerAdminPassword=[admin_pass]```

以**指定端口**和最大玩家数启动

```[path/to]/ShooterGameServer [TheIsland]?Port=[7777]?MaxPlayers=[1..70]```

启用 **PvE 模式**（禁用 PvP）

```[path/to]/ShooterGameServer [TheIsland]?ServerPVE=true```

设置**难度倍率**

```[path/to]/ShooterGameServer [TheIsland]?DifficultyOffset=[1.0]```

启用**指定活动**

```[path/to]/ShooterGameServer [TheIsland] -ActiveEvent=[Summer]```

启用 Steam 与 Epic Games 之间的**跨平台联机**

```[path/to]/ShooterGameServer [TheIsland] -crossplay -PublicIPForEpic=[ip_address]```

# SYNOPSIS

**ShooterGameServer** _map_ [_?options_] [_-flags_]

# DESCRIPTION

**ShooterGameServer** 为 ARK: Survival Evolved 运行无界面的专用服务器，这是一款恐龙主题的生存游戏。它支持托管多人服务器，可配置地图和玩法设定，并支持模组。

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

**Port=**_number_
> 服务器的网络端口

**MaxPlayers=**_count_
> 最大玩家数（1-70）

**-ActiveEvent=**_event_
> 启用指定的季节性活动

**-automanagedmods**
> 启用模组的自动下载与更新（仅 Steam）

**-crossplay**
> 启用 Steam 与 Epic Games 之间的跨平台联机

**-clusterid=**_id_, **-ClusterDirOverride=**_path_
> 使用给定的集群 ID 和共享数据目录加入服务器集群（共享玩家/恐龙转移）

**-NoBattlEye**
> 不带 BattlEye 反作弊运行服务器（客户端也必须禁用它）

# CONFIGURATION

**/ShooterGame/Saved/Config/LinuxServer/GameUserSettings.ini**
> 主服务器配置，包括会话名称、密码、端口、倍率和玩法开关。

**/ShooterGame/Saved/Config/LinuxServer/Game.ini**
> 高级玩法覆盖设置，包括印痕点数、战利品表和每级属性倍率。

# CAVEATS

需要大量系统资源（建议 8GB 以上内存）。服务器文件必须通过 SteamCMD 安装。模组需要 Steam 创意工坊集成。要持久化配置需编辑 GameUserSettings.ini 和 Game.ini 文件。

# SEE ALSO

[steamcmd](/man/steamcmd)(1), [ark-survival-ascended](/man/ark-survival-ascended)(1)
