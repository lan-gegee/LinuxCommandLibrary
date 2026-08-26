# TAGLINE

关闭并停机系统

# TLDR

**停机**系统

```systemctl halt```

立即**强制**停机

```systemctl halt -f```

不发送 **wall** 消息停机

```systemctl halt -f --no-wall```

**紧急**停机（危险）

```systemctl halt -ff```

**定时**在指定时刻停机

```systemctl halt --when 23:00```

以**时长**定时停机

```systemctl halt --when +2h```

**取消**已计划的停机

```systemctl halt --when cancel```

# SYNOPSIS

**systemctl halt** [_OPTIONS_]

# PARAMETERS

**-f, --force**
> 跳过服务的优雅关闭

**--force --force** (-ff)
> 立即停机，不做清理（危险）

**--no-wall**
> 不向用户发送 wall 消息

**--when** _TIME_
> 定时在指定时间或偏移量处停机

# DESCRIPTION

**systemctl halt** 关闭并停机系统：停止操作系统内核，但保持硬件通电。这与 poweroff（完全切断机器电源）和 reboot（重启系统）不同。

使用一个 `--force` 时，服务不会被优雅地停止。使用两个 `--force` 标志时，文件系统不会被卸载，可能导致数据丢失。

# CAVEATS

halt 后系统保持通电但无响应；需要手动断电。双重强制模式有数据损坏风险。计划中的操作可用 `--when cancel` 取消。

# HISTORY

**halt** 子命令提供 systemd 原生的系统停机方式，并与定时关机机制和 wall 通知系统集成。

# SEE ALSO

[systemctl-poweroff](/man/systemctl-poweroff)(1), [systemctl-reboot](/man/systemctl-reboot)(1), [halt](/man/halt)(8)
