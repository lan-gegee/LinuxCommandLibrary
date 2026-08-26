# TAGLINE

初始化 Toolbx 容器内部环境

# TLDR

**初始化**一个正在运行的容器

```toolbox init-container --gid [gid] --home [home] --shell [shell] --uid [uid] --user [user]```

# SYNOPSIS

**toolbox init-container** [_OPTIONS_]

# PARAMETERS

**--gid** _GID_
> 用户的组 ID

**--home** _PATH_
> 主目录路径

**--home-link**
> 为 home 创建符号链接

**--media-link**
> 为 media 创建符号链接

**--mnt-link**
> 为 mnt 创建符号链接

**--monitor-host**
> 监视宿主机的配置变更

**--shell** _SHELL_
> 用户的登录 Shell

**--uid** _UID_
> 用户 ID

**--user** _NAME_
> 用户名

# DESCRIPTION

**toolbox init-container** 初始化一个正在运行的 Toolbx 容器。这是容器启动时自动执行的内部命令，不应由用户手动运行。

该命令将容器环境设置为与宿主机系统的用户配置一致，创建必要的符号链接并配置用户身份。

# CAVEATS

该命令不能在宿主系统上运行。它仅供 Toolbx 容器初始化进程内部使用。

# SEE ALSO

[toolbox](/man/toolbox)(1), [toolbox-create](/man/toolbox-create)(1)
