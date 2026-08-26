# TAGLINE

为 GVFS 挂载点提供 FUSE 访问

# TLDR

**启动 FUSE 桥接**

```gvfsd-fuse [/run/user/UID/gvfs]```

**以调试模式启动**

```gvfsd-fuse -d [mountpoint]```

**前台模式**

```gvfsd-fuse -f [mountpoint]```

# SYNOPSIS

**gvfsd-fuse** [_options_] _mountpoint_

# PARAMETERS

_MOUNTPOINT_
> FUSE 挂载位置。

**-d**
> 启用 FUSE 调试输出（隐含 **-f**）。

**-f**
> 在前台运行。

**-s**
> 以单线程方式运行。

**-o** _OPTION_
> 传递 FUSE 专用的挂载选项（可用设置参见 FUSE 文档）。

# DESCRIPTION

**gvfsd-fuse** 维护一个 FUSE 挂载，将 GVFS 后端（SMB、SFTP、FTP、MTP 等）暴露给对 GVFS 一无所知的普通 POSIX 应用程序。挂载点以 _PATH_ 形式给出，在现代系统上通常是 **$XDG_RUNTIME_DIR/gvfs**（或旧式的 **$HOME/.gvfs**）。

与已弃用的 gvfs-bin 命令行工具（gvfs-ls、gvfs-mount 等，均已被 **gio** 取代）不同，gvfsd-fuse 仍是当前 GVFS 架构中的活跃组成部分：正是它让不感知 GNOME 的程序能够像访问本地文件一样打开 GVFS 挂载下的文件。

该守护进程通常在首次有内容被挂载时由 **gvfsd** 自动启动，无需手动运行。

# CAVEATS

通常由 gvfsd 自动启动；很少需要手动调用。需要内核支持 FUSE。性能取决于底层 GVFS 后端。

# HISTORY

**gvfsd-fuse** 自 GNOME 2.22（2008 年）起就是 **GVFS** 的一部分，为不直接使用 GIO/GVFS API 的应用程序提供基于 FUSE 的文件系统访问，以访问 GVFS 挂载点。

# SEE ALSO

[gvfsd](/man/gvfsd)(1), [fusermount](/man/fusermount)(1), [gio](/man/gio)(1)

# RESOURCES

```[Source code](https://gitlab.gnome.org/GNOME/gvfs)```

```[Homepage](https://wiki.gnome.org/Projects/gvfs)```

<!-- verified: 2026-07-17 -->
