# TAGLINE

通过 GVFS 挂载虚拟文件系统

# TLDR

**挂载远程位置**

```gvfs-mount [smb://server/share]```

**挂载 SSH 位置**

```gvfs-mount [sftp://user@host]```

**列出已挂载的位置**

```gvfs-mount -l```

**卸载位置**

```gvfs-mount -u [smb://server/share]```

**弹出介质**

```gvfs-mount -e [/dev/sr0]```

# SYNOPSIS

**gvfs-mount** [_options_] [_location_...]

**gvfs-mount** **--list** [_options_]

**gvfs-mount** **--unmount-scheme**=_SCHEME_

# PARAMETERS

_LOCATION_
> 要挂载的文件或目录路径或 URI。

**-m**, **--mountable**
> 将指定位置作为可挂载对象挂载，而非执行默认的挂载操作。

**-d**, **--device** _DEVICE_
> 挂载具有给定设备文件的卷。

**-u**, **--unmount**
> 卸载给定的位置。

**-e**, **--eject**
> 弹出给定的位置。

**-s**, **--unmount-scheme** _SCHEME_
> 卸载所有使用给定协议（scheme）的挂载点（如 smb、sftp）。

**-l**, **--list**
> 列出所有已知的挂载点。

**-o**, **--monitor**
> 监视挂载和卸载事件。

**-i**, **--detail**
> 为 **--list** 和 **--monitor** 显示额外信息。

**-h**, **--help**
> 打印简短帮助文本并退出。

# DESCRIPTION

**gvfs-mount** 通过 GVFS（GNOME 虚拟文件系统）挂载虚拟文件系统。它支持多种协议，包括 SMB/CIFS、SFTP、FTP、WebDAV 和 MTP。

GVFS 提供用户空间文件系统层，让文件管理器和应用程序能够透明地访问远程资源。

# SUPPORTED SCHEMES

```
smb://    SMB/CIFS network shares
sftp://   SSH file transfer
ftp://    FTP servers
dav://    WebDAV servers
mtp://    MTP devices (phones)
gphoto2:// PTP cameras
```

# CAVEATS

属于 gvfs-bin 命令行工具集，在 gvfs 1.31（2016 年）中被弃用，并在 gvfs 1.38（2018 年）中被完全移除，由统一的 **gio** 命令（`gio mount`）取代。现代发行版不再附带 gvfs-mount。需要正在运行的 GVFS 守护进程；挂载点位于 /run/user/$UID/gvfs/ 下。

# HISTORY

**gvfs-mount** 是 GVFS 原始 gvfs-bin 实用工具的一部分，于 **2008 年**（GNOME 2.22）随 GVFS 一同为 GNOME 引入。此后被 **gio mount** 取代。

# SEE ALSO

[gio](/man/gio)(1), [mount](/man/mount)(8), [smbclient](/man/smbclient)(1), [fusermount](/man/fusermount)(1)

# RESOURCES

```[Source code](https://gitlab.gnome.org/GNOME/gvfs)```

```[Homepage](https://wiki.gnome.org/Projects/gvfs)```

<!-- verified: 2026-07-17 -->
