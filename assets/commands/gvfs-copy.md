# TAGLINE

使用 GVFS 虚拟文件系统复制文件（已弃用）

# TLDR

**复制本地文件**

```gvfs-copy [source] [destination]```

**从远程 SMB 共享复制文件**

```gvfs-copy smb://server/share/file.txt [local-file]```

**从 FTP 服务器复制文件**

```gvfs-copy ftp://server/path/file.txt [local-file]```

**复制并显示进度指示器**

```gvfs-copy -p [source] [destination]```

**覆盖已存在文件前先提示**

```gvfs-copy -i [source] [destination]```

**复制并保留文件属性**

```gvfs-copy --preserve [source] [destination]```

# SYNOPSIS

**gvfs-copy** [_options_] _source_ _destination_

# PARAMETERS

_SOURCE_
> 源文件路径或 URI。

_DESTINATION_
> 目标文件路径或 URI。

**-p**, **--progress**
> 在复制操作期间显示进度指示器。

**-i**, **--interactive**
> 覆盖已存在的目标文件前先提示。

**--preserve**
> 保留时间戳和权限等文件属性。

**-b**, **--backup**
> 如果目标文件已存在，为其创建备份。

**--no-dereference**
> 不跟随符号链接；复制链接本身。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gvfs-copy** 使用 GVFS（GNOME 虚拟文件系统）复制文件。它支持本地文件和远程 URI，包括 SMB、FTP、SFTP、DAV 以及其他由 GVFS 后端支持的协议。

该工具透明地处理网络协议，可在不同后端之间复制文件。它与 GNOME 的文件系统抽象层集成。

此命令已被弃用，由提供相同功能的 **gio copy** 取代。

# CAVEATS

已被弃用，建议改用 **gio copy**。需要 GNOME/GVFS 库和正在运行的 GVFS 守护进程。

# HISTORY

gvfs-copy 是 GNOME 的 **GVFS** 的一部分开发而成，如今已在很大程度上被 GLib 2.36 中引入的 **gio** 命令取代。

# SEE ALSO

[gio](/man/gio)(1), [cp](/man/cp)(1), [gvfs-move](/man/gvfs-move)(1), [gvfs-ls](/man/gvfs-ls)(1), [rsync](/man/rsync)(1)
