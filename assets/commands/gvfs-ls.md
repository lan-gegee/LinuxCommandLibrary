# TAGLINE

使用 GVFS 列出文件和目录内容

# TLDR

**列出目录**

```gvfs-ls [directory]```

**列出远程目录**

```gvfs-ls smb://server/share/```

**显示隐藏文件**

```gvfs-ls -h [directory]```

**长列表格式**

```gvfs-ls -l [directory]```

**显示指定属性**

```gvfs-ls -a [standard::name,standard::size] [directory]```

# SYNOPSIS

**gvfs-ls** [_options_] [_location_...]

# PARAMETERS

_LOCATION_
> 文件或目录的路径或 URI（默认为当前目录）。

**-h**, **--hidden**
> 显示隐藏文件。

**-l**, **--long**
> 长列表格式。

**-a**, **--attributes** _ATTR_
> 显示指定属性，可以是 gvfs 属性名、命名空间，或用 `*` 表示全部。

**-n**, **--nofollow-symlinks**
> 不跟随符号链接。

**--version**
> 显示版本信息。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gvfs-ls** 列出给定位置的信息，类似于传统的 **ls** 工具，但使用的是 GVFS 位置而非本地文件，因此可以直接列出 smb://server/share/file.txt 之类的路径。

通过 **-a** 请求的属性可以是 gvfs 属性名（如 standard::icon）、命名空间（如 unix）或通配符（*），多个值以逗号分隔。

# CAVEATS

属于 gvfs-bin 命令行工具集，在 gvfs 1.31（2016 年）中被弃用，并在 gvfs 1.38（2018 年）中被完全移除，由统一的 **gio** 命令（`gio list`）取代。现代发行版不再附带 gvfs-ls。访问非本地后端需要正在运行的 GVFS 守护进程。

# HISTORY

**gvfs-ls** 是 GVFS 原始 gvfs-bin 实用工具的一部分，于 **2008 年**（GNOME 2.22）随 GVFS 一同为 GNOME 引入，用于取代更旧的 gnome-vfs 库中的工具。此后被 **gio list** 取代。

# SEE ALSO

[gio](/man/gio)(1), [ls](/man/ls)(1), [gvfs-info](/man/gvfs-info)(1)

# RESOURCES

```[Source code](https://gitlab.gnome.org/GNOME/gvfs)```

```[Homepage](https://wiki.gnome.org/Projects/gvfs)```

<!-- verified: 2026-07-17 -->
