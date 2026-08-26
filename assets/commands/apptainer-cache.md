# TAGLINE

管理本地 Apptainer 容器缓存

# TLDR

**列出所有缓存的镜像**

```apptainer cache list```

**列出缓存镜像及其详情**

```apptainer cache list -v```

**仅列出 OCI 缓存镜像**

```apptainer cache list -T oci```

**清理所有缓存的镜像**

```apptainer cache clean```

**不经确认直接清理缓存**

```apptainer cache clean -f```

**清理 30 天前的缓存条目**

```apptainer cache clean -D 30```

**试运行以查看将被清理的内容**

```apptainer cache clean -n```

# SYNOPSIS

**apptainer cache** [_subcommand_] [_options_]

# DESCRIPTION

**apptainer cache** 管理本地 Apptainer 容器镜像缓存。拉取或构建容器时，Apptainer 会在本地存储中间镜像和层，以加快后续操作。此命令可用于列出缓存内容并清理磁盘空间。

缓存默认存储在 **$HOME/.apptainer/cache**，或存储在 **APPTAINER_CACHEDIR** 环境变量指定的路径中。

# SUBCOMMANDS

**list**
> 显示本地缓存的内容，包括缓存镜像的大小和类型

**clean**
> 从本地缓存移除条目以回收磁盘空间

# PARAMETERS

**-T, --type** _strings_
> 将操作限制为特定缓存类型：**library**、**oci**、**shub**、**blob**、**net**、**oras**、**all**（默认：all）

**-v, --verbose**
> 显示缓存镜像的详细信息（仅限 list）

**-D, --days** _int_
> 移除早于指定天数的缓存条目（仅限 clean）

**-n, --dry-run**
> 显示将要删除的内容，但实际不删除任何东西（仅限 clean）

**-f, --force**
> 跳过确认提示，立即清理（仅限 clean）

# CAVEATS

大型构建和频繁拉取可能使缓存目录占用大量磁盘空间。缓存是按用户隔离的，不会影响系统上的其他用户。清理缓存后，下次使用时会强制重新下载镜像。

# INSTALL

```dnf: sudo dnf install apptainer```

```pacman: sudo pacman -S apptainer```

```apk: sudo apk add apptainer```

```zypper: sudo zypper install apptainer```

```brew: brew install apptainer```

```nix: nix profile install nixpkgs#apptainer```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[apptainer](/man/apptainer)(1), [apptainer-build](/man/apptainer-build)(1), [apptainer-pull](/man/apptainer-pull)(1)
