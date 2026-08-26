# TAGLINE

使用 GVFS 删除文件

# TLDR

**删除文件**

```gvfs-rm [file]```

**删除远程文件**

```gvfs-rm smb://server/share/file.txt```

**强制删除**

```gvfs-rm -f [file]```

# SYNOPSIS

**gvfs-rm** [_options_] _location_

# PARAMETERS

_LOCATION_
> 要删除的文件路径或 URI。

**-f**, **--force**
> 忽略不存在的和不可删除的文件。

**-?**, **--help**
> 打印简短帮助文本并退出。

# DESCRIPTION

**gvfs-rm** 使用 GVFS 删除文件。它可以删除本地文件以及通过 GVFS 后端访问的远程服务器上的文件。

该工具透明地处理不同协议下的删除操作。它适用于 SMB、FTP、SSH 以及其他 GVFS 支持的系统。

# CAVEATS

属于 gvfs-bin 命令行工具集，在 gvfs 1.31（2016 年）中被弃用，并在 gvfs 1.38（2018 年）中被完全移除，由统一的 **gio** 命令（`gio remove`）取代。现代发行版不再附带 gvfs-rm。删除是永久性的而非移入回收站；不支持递归删除目录。如需可恢复的删除请使用 **gvfs-trash**。

# HISTORY

**gvfs-rm** 是 GVFS 原始 gvfs-bin 实用工具的一部分，于 **2008 年**（GNOME 2.22）随 GVFS 一同为 GNOME 引入。此后被 **gio remove** 取代。

# SEE ALSO

[gio](/man/gio)(1), [rm](/man/rm)(1), [gvfs-trash](/man/gvfs-trash)(1)

# RESOURCES

```[Source code](https://gitlab.gnome.org/GNOME/gvfs)```

```[Homepage](https://wiki.gnome.org/Projects/gvfs)```

<!-- verified: 2026-07-17 -->
