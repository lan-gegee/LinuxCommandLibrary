# TAGLINE

多人丧尸生存游戏专用服务器

# TLDR

**启动**服务器

```path/to/start-server.sh```

以**指定名称**启动服务器

```path/to/start-server.sh -servername server_name```

# SYNOPSIS

**start-server.sh** [_options_]

# PARAMETERS

**-servername** _name_
> 指定自定义服务器名称

# DESCRIPTION

**Project Zomboid** 专用服务器为这款开放世界生存恐怖游戏运行无界面的多人服务器。**start-server.sh** 脚本在不带图形界面的情况下启动服务器，使其适合在 Linux 主机或云实例上进行远程托管。

服务器管理多人会话，包括玩家连接、世界状态持久化、丧尸种群模拟和战利品刷新周期。服务器管理员可以通过服务器数据目录中的配置文件设置沙盒参数，控制难度、PvP 规则、玩家上限和模组加载。

**-servername** 选项允许在同一台机器上运行多个服务器实例，每个实例拥有独立的世界数据和设置。

# CONFIGURATION

**~/Zomboid/Server/<servername>.ini**
> 主服务器配置文件，控制游戏设置、玩家上限、PvP 规则、战利品刷新和网络选项。

**~/Zomboid/Server/<servername>_SandboxVars.lua**
> 沙盒设置，控制丧尸数量、风化速度、战利品稀有度、天气和难度参数。

# CAVEATS

服务器配置存储在单独的配置文件中。世界模拟和玩家连接需要足够的系统资源。

# HISTORY

**Project Zomboid** 是由 The Indie Stone 开发的生存恐怖电子游戏。专用服务器让玩家可以在自托管的基础设施上进行多人游戏。

# SEE ALSO

[screen](/man/screen)(1), [tmux](/man/tmux)(1)
