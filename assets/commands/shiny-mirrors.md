# TAGLINE

管理 Manjaro Linux 镜像列表

# TLDR

获取当前镜像的**状态**

```shiny-mirrors status```

使用默认配置**生成**镜像列表

```sudo shiny-mirrors refresh```

显示当前**配置**

```shiny-mirrors config show```

以交互方式切换到其他**分支**

```sudo shiny-mirrors config --branch```

为**特定国家/地区**刷新镜像

```sudo shiny-mirrors refresh --country [country_code]```

# SYNOPSIS

**shiny-mirrors** _command_ [_OPTIONS_]

# PARAMETERS

**status**
> 显示当前镜像的状态和健康情况

**refresh**
> 根据配置的条件生成并更新镜像列表

**config show**
> 显示当前的配置文件

**config --branch**
> 交互式切换到不同的 Manjaro 分支（stable、testing、unstable）

**--country** _code_
> 按国家/地区代码筛选镜像

**--protocol** _protocol_
> 按协议筛选（https、http）

**--help**
> 显示用法信息

# DESCRIPTION

**shiny-mirrors** 为 Manjaro Linux 生成并管理 pacman 镜像列表。它会测试可用镜像的速度和可靠性，然后创建优化的镜像列表用于软件包下载。

该工具基于地理位置、响应时间和同步状态选择镜像。运行 shiny-mirrors 之后，必须使用 **sudo pacman -Syyu** 同步数据库并更新系统，才能应用新的镜像配置。

# CAVEATS

修改系统文件的刷新操作需要 root 权限。镜像选择可能因测试时的网络状况而异。刷新镜像后务必运行 **pacman -Syyu**，避免发生部分升级。切换分支会影响可用的软件包版本。

# HISTORY

**shiny-mirrors** 是一款 Manjaro 专用工具，作为 **pacman-mirrors** 的现代替代品开发。它旨在为 Manjaro Linux 用户提供更快、更可靠的镜像管理。该工具作为 Manjaro 生态的一部分得到积极维护。

# INSTALL

```aur: yay -S shiny-mirrors```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pacman](/man/pacman)(8), [pacman-mirrors](/man/pacman-mirrors)(1), [reflector](/man/reflector)(1)
