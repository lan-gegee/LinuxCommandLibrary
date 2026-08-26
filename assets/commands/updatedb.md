# TAGLINE

为 locate 搜索构建文件名数据库

# TLDR

**刷新**数据库

```sudo updatedb```

**详细输出**模式

```sudo updatedb -v```

# SYNOPSIS

**updatedb** [_OPTIONS_]

# PARAMETERS

**-v, --verbose**
> 在发现文件名时将其显示出来

**--prunepaths** _PATHS_
> 将指定路径排除在数据库之外

**--prunefs** _TYPES_
> 排除指定的文件系统类型

**-o, --output** _FILE_
> 写入到指定的数据库文件

**-U, --database-root** _PATH_
> 只保存以 PATH 为根的子树中的结果

**-e, --add-prunepaths** _PATHS_
> 向 PRUNEPATHS 添加条目

**-n, --add-prunenames** _NAMES_
> 向 PRUNENAMES 添加条目

**-l, --require-visibility** _FLAG_
> 控制可见性检查（0 或 1）

**--prune-bind-mounts** _FLAG_
> 覆盖 bind mount 的剪除设置（yes 或 no）

# DESCRIPTION

**updatedb** 创建或更新 locate 命令所使用的数据库。它扫描文件系统，为所有文件名建立索引，从而实现快速搜索。

该命令通常由 cron 每天运行一次，以保持数据库处于最新状态。若想在下次计划更新之前就为新创建的文件建立索引，则需要手动执行。

# CONFIGURATION

**/etc/updatedb.conf**
> 控制哪些路径、文件系统类型和文件模式会被纳入或排除出数据库。

# CAVEATS

完全访问文件系统需要 root 权限。在大型文件系统上，初次扫描可能耗时数分钟。网络文件系统默认通常会被排除。

# INSTALL

```apk: sudo apk add findutils-locate```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[locate](/man/locate)(1), [mlocate](/man/mlocate)(1), [plocate](/man/plocate)(1)
