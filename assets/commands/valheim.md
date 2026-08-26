# TAGLINE

Valheim 专用游戏服务器

# TLDR

**启动**服务器

```[path/to]/start_server.sh```

优雅地**停止**服务器

```<Ctrl c>```

通过 **Docker** 脚本启动

```[path/to/docker_start_server.sh] [path/to/start_server.sh]```

# SYNOPSIS

**start_server.sh** [_OPTIONS_]

# DESCRIPTION

**Valheim** 专用服务器用于创建和运行无头（headless）的 Valheim 游戏服务器。玩家可以连接到服务器进行多人生存游戏。

服务器配置通过编辑 start_server.sh 脚本的副本完成，可以在其中设置服务器名称、世界名称、密码和端口。

# CAVEATS

需要有效的 Steam 账户和 Valheim 专用服务器文件。服务器配置需要编辑启动脚本。托管多名玩家需要足够的系统资源。

# HISTORY

**Valheim** 是由 **Iron Gate AB** 开发的生存探索游戏，于 **2021 年**以抢先体验形式发布。专用服务器允许托管持久化的世界。

# SEE ALSO

[screen](/man/screen)(1), [tmux](/man/tmux)(1)
