# TAGLINE

获取或设置单个服务的日志目的地

# TLDR

显示服务的**日志目标**

```systemctl service-log-target [service]```

设置为 **console**

```systemctl service-log-target [service] console```

设置为 **journal**

```systemctl service-log-target [service] journal```

设置为 **syslog**

```systemctl service-log-target [service] syslog```

设置为 **auto**

```systemctl service-log-target [service] auto```

**禁用**日志

```systemctl service-log-target [service] null```

# SYNOPSIS

**systemctl service-log-target** _SERVICE_ [_TARGET_]

# LOG TARGETS

**console** - 将日志发送到 stderr

**journal** - 将日志发送到 systemd-journald

**syslog** - 将日志发送到 /dev/log

**auto** - 由 systemd 自行选择

**null** - 禁用所有日志输出

# DESCRIPTION

**systemctl service-log-target** 通过 D-Bus 获取或设置服务发送日志消息的目的地。这可以在不重启的情况下在运行时重定向服务日志。

服务必须支持标准的 D-Bus 日志接口。

# CAVEATS

只对集成了 D-Bus 的服务有效。更改是临时的，服务重启后会恢复原状。并非所有服务都支持此功能。

# HISTORY

**service-log-target** 子命令提供按服务粒度的日志路由控制，便于调试和排查特定服务。

# SEE ALSO

[systemctl-service-log-level](/man/systemctl-service-log-level)(1), [systemctl-log-target](/man/systemctl-log-target)(1), [journalctl](/man/journalctl)(1)
