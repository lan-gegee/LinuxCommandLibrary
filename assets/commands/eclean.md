# TAGLINE

Gentoo 软件仓库清理工具

# TLDR

清理**源码文件**目录

```sudo eclean distfiles```

清理**二进制包**目录

```sudo eclean packages```

**深度清理**已卸载软件包的 distfiles

```sudo eclean -d -n distfiles```

**深度清理**二进制包

```sudo eclean -d -n packages```

# SYNOPSIS

**eclean** [_options_] _target_

# DESCRIPTION

**eclean** 清理 Gentoo 软件仓库中的源码文件和二进制包。它移除旧的或不再使用的 distfiles 和软件包以释放磁盘空间。

该工具作用于两个主要目标：distfiles（/usr/portage/distfiles 中的源码压缩包）和 packages（/usr/portage/packages 中的二进制包）。这些目录会随时间积累旧版本和已卸载软件包的文件，占用大量磁盘空间。

eclean 提供保守和激进两种清理模式。普通模式保留已安装软件包和当前 portage 树条目对应的文件，而深度模式只保留当前已安装软件包所需的文件。这对存储空间有限或刚完成系统升级的系统尤其有用。

# PARAMETERS

**distfiles**
> 清理源码下载目录（DISTDIR，默认 `/var/cache/distfiles`）。

**packages**
> 清理二进制包目录（PKGDIR，默认 `/var/cache/binpkgs`）。

**-d, --deep**
> 只保留当前已安装软件包所需的文件（激进清理）。

**-n**, **--package-names**
> 按软件包名而非精确版本/slot 保护文件。

**-p, --pretend**
> 试运行：列出将要移除的内容而不实际删除。

**-C, --color** _mode_
> 输出着色：_yes_、_no_ 或 _auto_。

**-t, --time-limit** _time_
> 保护晚于 _time_ 的文件（例如 `7d`、`1m`）。

**-s, --size-limit** _size_
> 保护大于 _size_ 的文件（例如 `50M`、`1G`）。

**-e, --exclude-file** _file_
> 从 _file_ 读取额外的排除模式。

**-i, --interactive**
> 移除每个文件前请求确认。

**-q, --quiet**
> 抑制提示性输出。

**-h, --help**
> 显示帮助信息。

# CAVEATS

仅限 Gentoo。删除前请先用 -p 预览。深度清理可能删除重装软件包所需的文件。

# SEE ALSO

[emerge](/man/emerge)(1), [eclean-kernel](/man/eclean-kernel)(1)
