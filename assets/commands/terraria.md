# TAGLINE

Terraria 专用游戏服务器

# TLDR

启动**交互式**服务器设置

```[path/to]/TerrariaServer```

以指定**世界**启动服务器

```[path/to]/TerrariaServer -world [path/to/world.wld]```

# SYNOPSIS

**TerrariaServer** [_OPTIONS_]

# PARAMETERS

**-world** _PATH_
> 要加载的世界文件

**-port** _PORT_
> 服务器端口（默认：7777）

**-maxplayers** _N_
> 允许的最大玩家数

**-password** _PASS_
> 服务器密码

**-config** _FILE_
> 配置文件路径

**-autocreate** _SIZE_
> 自动创建世界（1=小、2=中、3=大）

**-worldname** _NAME_
> 自动创建世界的名称

# DESCRIPTION

**TerrariaServer** 创建并运行无界面的 Terraria 游戏服务器。它可以交互式启动以进行设置，也可以使用命令行参数实现自动化部署。

该服务器承载 Terraria 多人游戏会话，允许玩家连接并一起游玩。

# CAVEATS

需要有效的 Terraria 服务器安装。世界文件是平台相关的。对于大世界和大量玩家，服务器消耗的资源相当可观。

# HISTORY

**Terraria** 是由 **Re-Logic** 开发的 2D 沙盒游戏，于 **2011** 年首次发布。专用服务器让你无需运行完整游戏客户端即可托管多人游戏。

# SEE ALSO

[screen](/man/screen)(1), [tmux](/man/tmux)(1)
