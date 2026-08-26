# TAGLINE

使用 GVFS 显示文件信息

# TLDR

**显示文件信息**

```gvfs-info [file]```

**显示远程文件信息**

```gvfs-info smb://server/share/file```

**显示指定属性**

```gvfs-info -a [standard::size] [file]```

**显示文件系统信息**

```gvfs-info -f [file]```

# SYNOPSIS

**gvfs-info** [_options_] _location_

# PARAMETERS

_LOCATION_
> 文件路径或 URI。

**-a**, **--attributes** _ATTR_
> 显示指定的属性。

**-f**, **--filesystem**
> 显示文件系统信息。

**-n**, **--nofollow-symlinks**
> 不跟随符号链接。

**-w**, **--query-writable**
> 显示可写属性。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gvfs-info** 使用 GVFS 显示文件信息。它会显示本地和远程文件的大小、类型、权限及自定义元数据等属性。

该工具通过 GVFS 后端访问文件，在 SMB、FTP 和本地文件系统等不同协议间提供统一的信息。

# CAVEATS

自 GNOME 3.22 起被弃用，建议改用 **gio info**。需要 GVFS 守护进程正在运行。仅在带有 GNOME/GLib 技术栈的系统上可用。

# SEE ALSO

[gio](/man/gio)(1), [stat](/man/stat)(1), [file](/man/file)(1)
