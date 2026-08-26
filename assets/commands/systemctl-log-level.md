# TAGLINE

获取或设置 systemd 日志详细程度

# TLDR

显示**当前的**日志级别

```systemctl log-level```

**设置**日志级别

```systemctl log-level [emerg|alert|crit|err|warning|notice|info|debug]```

# SYNOPSIS

**systemctl log-level** [_LEVEL_]

# LOG LEVELS

**emerg** - 系统不可用

**alert** - 需要立即采取行动

**crit** - 严重状况

**err** - 错误状况

**warning** - 警告状况

**notice** - 正常但值得注意

**info** - 信息性消息

**debug** - 调试级别消息

# DESCRIPTION

**systemctl log-level** 获取或设置 systemd 服务管理器（PID 1）的日志详细程度。不带参数时，显示当前级别。带级别参数时，在运行时更改详细程度。

更高的详细程度（debug、info）会产生更多日志输出，有助于诊断问题。更低的级别（err、crit）可减少生产环境中的日志噪音。

# CAVEATS

更改是临时的，重启后会恢复原状。若要永久更改，请修改 systemd 配置。debug 级别会产生大量日志并影响性能。

# HISTORY

**log-level** 子命令提供对 systemd 详细程度的运行时控制，无需修改配置或重启即可进行临时调试。

# SEE ALSO

[systemctl-log-target](/man/systemctl-log-target)(1), [journalctl](/man/journalctl)(1), [systemctl](/man/systemctl)(1)
