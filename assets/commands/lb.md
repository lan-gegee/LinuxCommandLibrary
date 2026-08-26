# TAGLINE

创建 Debian live 系统镜像

# TLDR

**初始化 live 构建**

```lb config```

**构建 live 镜像**

```lb build```

**清理构建目录**

```lb clean```

**使用选项进行配置**

```lb config --distribution [bookworm] --archive-areas "main contrib"```

**构建特定类型的镜像**

```lb config --binary-images [iso-hybrid]```

**清理时包含缓存**

```lb clean --cache```

# SYNOPSIS

**lb** _command_ [_options_]

# PARAMETERS

**config**
> 初始化配置。

**build**
> 构建 live 镜像。

**clean**
> 清理构建产物。

**--distribution** _NAME_
> 目标发行版。

**--archive-areas** _AREAS_
> 软件仓库区域（如 "main contrib non-free"）。

**--binary-images** _TYPE_
> 镜像类型：iso、iso-hybrid、netboot、tar、hdd。

**--architecture** _ARCH_
> 目标架构（默认为主机架构）。

**--bootappend-live** _PARAMS_
> live 系统的启动参数。

**--cache**
> 清理缓存目录（默认不清理）。

**--force**
> 强制执行辅助操作，即使 stage 文件已存在。

**--quiet**
> 抑制输出消息。

**--verbose**
> 显示详细输出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**lb**（live-build）用于创建 Debian live 系统镜像。它可以构建可引导的 ISO、netboot 和 HDD 镜像。

该工具支持自定义软件包、配置和钩子。它是制作 Debian live 镜像的标准工具。默认情况下，`lb clean` 会移除 chroot、binary 和 source 各阶段的产物，但保留缓存。

# CAVEATS

Debian/Ubuntu 专属工具。需要 root 权限。需要足够的磁盘空间。

# HISTORY

live-build 由 **Debian Live** 项目创建，用于构建可定制的 live 系统镜像。

# SEE ALSO

[debootstrap](/man/debootstrap)(1), [mksquashfs](/man/mksquashfs)(1)
