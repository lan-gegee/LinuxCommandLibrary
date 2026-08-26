# TAGLINE

使用 GVFS 移动文件

# TLDR

**移动本地文件**

```gvfs-move [source] [destination]```

**移动到远程**

```gvfs-move [local-file] smb://server/share/```

**移动并显示进度**

```gvfs-move -p [source] [destination]```

**交互模式**

```gvfs-move -i [source] [destination]```

# SYNOPSIS

**gvfs-move** [_options_] _source_ _destination_

# PARAMETERS

_SOURCE_
> 源文件或 URI。

_DESTINATION_
> 目标文件或 URI。

**-p**, **--progress**
> 显示进度。

**-i**, **--interactive**
> 覆盖文件前先提示。

**-b**, **--backup**
> 为已存在的目标文件创建备份。

**-T**, **--no-target-directory**
> 即使目标是目录也不要移入其中。

**-h**, **--help**
> 打印简短帮助文本并退出。

# DESCRIPTION

**gvfs-move** 使用 GVFS 移动文件。它支持本地文件和远程 URI，透明地处理跨不同后端的移动操作。

该工具在同一文件系统内提供原子性移动，对跨文件系统的移动则采用先复制后删除的方式。它与 GNOME 的 VFS 集成。

# CAVEATS

属于 gvfs-bin 命令行工具集，在 gvfs 1.31（2016 年）中被弃用，并在 gvfs 1.38（2018 年）中被完全移除，由统一的 **gio** 命令（`gio move`）取代。现代发行版不再附带 gvfs-move。跨文件系统移动会退化为先复制后删除，因此目标处需要有足够的可用空间。

# HISTORY

**gvfs-move** 是 GVFS 原始 gvfs-bin 实用工具的一部分，于 **2008 年**（GNOME 2.22）随 GVFS 一同为 GNOME 引入。此后被 **gio move** 取代。

# SEE ALSO

[gio](/man/gio)(1), [mv](/man/mv)(1), [gvfs-copy](/man/gvfs-copy)(1)

# RESOURCES

```[Source code](https://gitlab.gnome.org/GNOME/gvfs)```

```[Homepage](https://wiki.gnome.org/Projects/gvfs)```

<!-- verified: 2026-07-17 -->
