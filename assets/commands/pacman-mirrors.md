# TAGLINE

为 Manjaro Linux 生成和管理 pacman 镜像列表

# TLDR

生成**最快的**镜像列表

```sudo pacman-mirrors --fasttrack```

检查镜像**状态**

```pacman-mirrors --status```

显示当前**分支**

```pacman-mirrors --get-branch```

**切换**分支

```sudo pacman-mirrors --api --set-branch stable```

使用 **geoip** 镜像

```sudo pacman-mirrors --geoip```

# SYNOPSIS

**pacman-mirrors** [_OPTIONS_]

# DESCRIPTION

**pacman-mirrors** 为 Manjaro Linux 生成和管理 pacman 镜像列表。它测试镜像速度、选择最快的镜像，还可以在 stable、testing 和 unstable 分支之间切换。

# PARAMETERS

**-f, --fasttrack** [_number_]
> 用最快的镜像生成镜像列表

**--status**
> 显示当前镜像的状态

**-g, --geoip**
> 使用地理定位从你所在的国家选择镜像

**--get-branch**
> 显示当前分支

**--api**
> 使用 API 进行分支切换

**--set-branch** _branch_
> 设置分支（stable、testing、unstable）

**-c, --country** _country_
> 将镜像限制在特定国家

**-l, --list**
> 列出可用的国家

# CAVEATS

生成新的镜像列表后，请使用 **sudo pacman -Syyu** 同步并升级。切换分支（stable → testing → unstable）可能引入不稳定因素。unstable 分支更紧密地跟踪 Arch Linux 仓库。这是 Manjaro 专属工具；Arch Linux 上不可用（请改用 **reflector**）。

# HISTORY

**pacman-mirrors** 是 **Manjaro Linux** 专属的，提供了上游 Arch Linux 所没有的镜像管理功能。

# SEE ALSO

[pacman](/man/pacman)(8), [pacman-sync](/man/pacman-sync)(8)
