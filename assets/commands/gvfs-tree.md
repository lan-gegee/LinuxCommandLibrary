# TAGLINE

使用 GVFS 以树状格式显示目录内容

# TLDR

**显示目录树**

```gvfs-tree [directory]```

**显示远程目录树**

```gvfs-tree smb://server/share/```

**显示隐藏文件**

```gvfs-tree -h [directory]```

**跟随符号链接**

```gvfs-tree -l [directory]```

# SYNOPSIS

**gvfs-tree** [_options_] _location_

# PARAMETERS

_LOCATION_
> 目录路径或 URI。

**-h**, **--hidden**
> 显示隐藏文件。

**-l**, **--follow-symlinks**
> 跟随符号链接、挂载点和快捷方式。

**-?**, **--help**
> 打印简短帮助文本并退出。

# DESCRIPTION

**gvfs-tree** 使用 GVFS 以树状格式显示目录内容。它可以显示本地和远程目录的层次结构。

该工具可在 GVFS 各后端之间可视化目录树，为本地和网络文件系统提供统一的视图。

# CAVEATS

属于 gvfs-bin 命令行工具集，在 gvfs 1.31（2016 年）中被弃用，并在 gvfs 1.38（2018 年）中被完全移除，由统一的 **gio** 命令（`gio tree`）取代。现代发行版不再附带 gvfs-tree。大型或嵌套很深的远程目录树枚举起来可能很慢。

# HISTORY

**gvfs-tree** 是 GVFS 原始 gvfs-bin 实用工具的一部分，于 **2008 年**（GNOME 2.22）随 GVFS 一同为 GNOME 引入。此后被 **gio tree** 取代。

# SEE ALSO

[gio](/man/gio)(1), [tree](/man/tree)(1), [gvfs-ls](/man/gvfs-ls)(1)

# RESOURCES

```[Source code](https://gitlab.gnome.org/GNOME/gvfs)```

```[Homepage](https://wiki.gnome.org/Projects/gvfs)```

<!-- verified: 2026-07-17 -->
