# TAGLINE

将文件和目录移入回收站的 GNOME 虚拟文件系统命令

# TLDR

**将文件移入回收站**

```gvfs-trash [path/to/file]```

**将多个文件移入回收站**

```gvfs-trash [file1] [file2] [file3]```

**清空回收站**

```gvfs-trash --empty```

**将文件移入回收站**并忽略不存在的文件导致的错误

```gvfs-trash -f [path/to/file]```

**从标准输入读取要移入回收站的文件**（每行一个）

```echo "[path/to/file]" | gvfs-trash```

# SYNOPSIS

**gvfs-trash** [_options_] [_file_...]

**gvfs-trash** --empty

# PARAMETERS

**-f**, **--force**
> 忽略不存在的和不可删除的文件

**--empty**
> 清空回收站

**-h**, **--help**
> 打印帮助文本并退出

**--version**
> 显示版本信息并退出

# DESCRIPTION

**gvfs-trash** 是一个 GNOME 虚拟文件系统命令，它将文件和目录移动到用户的回收站中，而不是永久删除它们。相比 **rm**，这是一种更安全的方式，允许恢复误删的文件。

回收站的位置取决于文件所在的文件系统。对于用户主目录中的文件，回收站位于 **$XDG_DATA_HOME/Trash**（通常是 **~/.local/share/Trash**）。可移动磁盘上的文件可能拥有各自独立的回收站文件夹。

不带 **--empty** 选项调用时，gvfs-trash 期望以文件路径作为参数。如果未指定任何文件，它会从标准输入读取路径，每行一个。在清空回收站之前，将文件移入回收站并不会释放磁盘空间。

# CAVEATS

并非所有文件系统都支持回收站概念；此类系统上的文件可能会被立即删除。该命令已被弃用，建议改用提供相同功能的 **gio trash**。如需永久删除请使用 **gvfs-rm**，查看回收站内容可用 **gvfs-ls trash://**。

# HISTORY

gvfs-trash 是 **GVFS**（GNOME 虚拟文件系统）的一部分，于 **2008 年**随 **GNOME 2.22** 引入，用于取代更旧的 gnome-vfs 库。GVFS 为 GNOME 中的各种文件系统和存储后端提供统一接口。gvfs 命令行工具后来被弃用，改用将所有 GVFS 操作整合到单一工具中的 **gio** 命令。

# SEE ALSO

[gio](/man/gio)(1), [trash-cli](/man/trash-cli)(1), [rm](/man/rm)(1), [gvfs-rm](/man/gvfs-rm)(1)

# RESOURCES

```[Source code](https://gitlab.gnome.org/GNOME/gvfs)```

```[Homepage](https://wiki.gnome.org/Projects/gvfs)```

<!-- verified: 2026-07-17 -->
