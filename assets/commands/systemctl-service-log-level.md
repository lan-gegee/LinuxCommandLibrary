# TAGLINE

获取或设置单个服务的日志级别

# TLDR

显示服务的**日志级别**

```systemctl service-log-level [service]```

**设置**日志级别

```systemctl service-log-level [service] [emerg|alert|crit|err|warning|notice|info|debug]```

# SYNOPSIS

**systemctl service-log-level** _SERVICE_ [_LEVEL_]

# LOG LEVELS

**emerg** (0) - 系统不可用

**alert** (1) - 需要立即采取行动

**crit** (2) - 严重状况

**err** (3) - 错误状况

**warning** (4) - 警告状况

**notice** (5) - 正常但值得注意

**info** (6) - 信息性消息

**debug** (7) - 调试消息

# DESCRIPTION

**systemctl service-log-level** 通过 D-Bus 获取或设置特定服务的运行时日志级别。这可以在不重启服务、不修改配置的情况下调整服务的日志详细程度。

服务必须支持标准的 D-Bus 日志接口，此功能才能生效。

# CAVEATS

只对暴露了 D-Bus 日志接口的服务有效。更改是临时的，服务重启后会恢复原状。并非所有服务都支持此功能。

# HISTORY

**service-log-level** 子命令提供按服务粒度的日志控制，可以在不影响系统整体详细程度的情况下调试特定服务。

# SEE ALSO

[systemctl-log-level](/man/systemctl-log-level)(1), [systemctl-service-log-target](/man/systemctl-service-log-target)(1), [journalctl](/man/journalctl)(1)
