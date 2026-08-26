# TAGLINE

关闭系统并断电

# TLDR

**关闭**系统电源

```systemctl poweroff```

**强制**立即关机

```systemctl poweroff -f```

关机时不发送 **wall** 消息

```systemctl poweroff -f --no-wall```

# SYNOPSIS

**systemctl poweroff** [_OPTIONS_]

# PARAMETERS

**-f, --force**
> 跳过服务的优雅关闭

**--force --force** (-ff)
> 立即断电，不做清理（危险）

**--no-wall**
> 不向已登录用户发送 wall 消息

**--when** _TIME_
> 在指定时间安排关机

# DESCRIPTION

**systemctl poweroff** 关闭系统并切断机器电源。它会优雅地停止所有服务、卸载文件系统，然后向硬件发出断电信号。

使用 `--force` 时，服务不会被优雅地停止。使用双重 `--force` 时，文件系统也不会被卸载，有数据丢失风险。

# CAVEATS

需要相应的权限。如果文件系统未正确同步，强制模式可能导致数据丢失。某些硬件可能不支持软件断电，此时会改为停机。

# HISTORY

**poweroff** 子命令提供 systemd 原生的关机方式，与计划关机机制和 wall 通知系统集成。

# SEE ALSO

[systemctl-halt](/man/systemctl-halt)(1), [systemctl-reboot](/man/systemctl-reboot)(1), [poweroff](/man/poweroff)(8)
