# TAGLINE

获取或设置 systemd 日志目的地

# TLDR

显示**当前的**日志目标

```systemctl log-target```

**设置**日志目标

```systemctl log-target [journal-or-kmsg|journal|kmsg|console|syslog|null|auto]```

# SYNOPSIS

**systemctl log-target** [_TARGET_]

# LOG TARGETS

**journal-or-kmsg** - 可用时使用 Journal，否则使用内核环形缓冲区

**journal** - 仅使用 systemd journal

**kmsg** - 内核环形缓冲区（dmesg）

**console** - 系统控制台

**syslog** - 传统 syslog

**null** - 丢弃所有日志

**auto** - 自动选择

# DESCRIPTION

**systemctl log-target** 获取或设置 systemd 服务管理器发送日志消息的目的地。不带参数时，显示当前目标。带目标参数时，在运行时重定向日志。

它控制的是 systemd 自身消息的去向，与各个服务日志的发送位置相互独立。

# CAVEATS

更改是临时的，重启后会恢复原状。向控制台输出日志会拖慢系统并刷屏。null 目标会丢弃所有 systemd 诊断输出。

# HISTORY

**log-target** 子命令提供对 systemd 日志目的地的运行时控制，适用于调试启动问题或在特定环境中重定向日志。

# SEE ALSO

[systemctl-log-level](/man/systemctl-log-level)(1), [journalctl](/man/journalctl)(1), [systemctl](/man/systemctl)(1)
