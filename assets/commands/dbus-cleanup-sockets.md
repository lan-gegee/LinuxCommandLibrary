# TAGLINE

清理残留 D-Bus Unix 域套接字的工具

# TLDR

**清理残留的** D-Bus 套接字

```dbus-cleanup-sockets```

**在指定目录清理**套接字

```dbus-cleanup-sockets [/run/user/1000/bus]```

# SYNOPSIS

**dbus-cleanup-sockets** [_directory_]

# PARAMETERS

_DIRECTORY_
> 存放待清理 D-Bus 套接字的目录。默认使用标准 D-Bus 套接字位置。

# DESCRIPTION

**dbus-cleanup-sockets** 移除由 D-Bus 创建但已不再使用的残留 Unix 域套接字。当 D-Bus 会话异常终止而未正确清理时，这些孤立套接字会不断累积。

该工具扫描指定目录（或默认的 D-Bus 套接字位置），移除没有活动监听者的套接字文件。这有助于防止套接字命名空间污染和潜在的连接问题。

此命令通常由系统初始化脚本自动执行，或作为周期性维护任务的一部分。

# CAVEATS

对活跃套接字执行可能中断 D-Bus 连接。移除套接字文件需要相应权限。不应在 D-Bus 会话正在初始化时运行。

# HISTORY

dbus-cleanup-sockets 是 **D-Bus** 消息总线系统的一部分，后者由 **Red Hat** 和 freedesktop.org 项目自 **2003 年**起开发。这个清理工具帮助长期运行的系统保持整洁。

# INSTALL

```apt: sudo apt install dbus-bin```

```dnf: sudo dnf install dbus```

```pacman: sudo pacman -S dbus```

```apk: sudo apk add dbus```

```brew: brew install dbus```

```nix: nix profile install nixpkgs#dbus```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dbus-daemon](/man/dbus-daemon)(1), [dbus-launch](/man/dbus-launch)(1), [dbus-send](/man/dbus-send)(1), [dbus-monitor](/man/dbus-monitor)(1)
