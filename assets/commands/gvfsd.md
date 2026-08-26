# TAGLINE

处理虚拟文件系统操作的 GVFS 守护进程

# TLDR

**启动 GVFS 守护进程**

```gvfsd```

**替换现有守护进程**

```gvfsd --replace```

**调试模式**

```gvfsd --debug```

**禁用 FUSE 支持**

```gvfsd --no-fuse```

# SYNOPSIS

**gvfsd** [_options_]

# PARAMETERS

**--replace**
> 替换正在运行的守护进程。

**--no-fuse**
> 禁用 FUSE 支持。

**--debug**
> 启用调试输出。

**-h**, **--help**
> 显示帮助信息。

**--version**
> 显示版本号并退出。

# DESCRIPTION

**gvfsd** 是 GVFS 虚拟文件系统的主守护进程。它在会话总线上注册 `org.gtk.vfs.Daemon` 名称，如果尚未运行，会被 GIO 客户端自动启动。

gvfsd 的主要任务是充当挂载跟踪器/管理器。它按需派生新的后端，跟踪其生命周期，维护活动挂载点列表，并创建到它们的直接连接。GVFS 后端作为 gvfsd 进程的子进程运行。

# CAVEATS

通常由 D-Bus 自动启动。需要正确的 D-Bus 会话。GNOME 专属。

# HISTORY

gvfsd 作为 **GNOME** 桌面环境 **GVFS** 的一部分开发而成，用于提供虚拟文件系统支持。

# SEE ALSO

[gvfs-open](/man/gvfs-open)(1), [gvfsd-fuse](/man/gvfsd-fuse)(1), [gio](/man/gio)(1), [dbus-daemon](/man/dbus-daemon)(1)
