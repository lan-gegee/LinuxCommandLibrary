# TAGLINE

将系统挂起到内存

# TLDR

**挂起**系统

```systemctl suspend```

**强制**挂起

```systemctl suspend -f```

# SYNOPSIS

**systemctl suspend** [_OPTIONS_]

# PARAMETERS

**-f, --force**
> 即使存在抑制锁也强制挂起

**--no-wall**
> 不向用户发送 wall 消息

# DESCRIPTION

**systemctl suspend** 将系统置于挂起模式（挂起到内存），这是一种低功耗状态，系统内容保留在内存中。由于无需从磁盘恢复系统状态，唤醒速度很快。

内存保持供电以维持系统状态。这是笔记本电脑和台式机的标准睡眠模式。

# CAVEATS

如果挂起期间断电，系统状态会丢失。挂起期间电池仍会（缓慢）耗电。某些硬件可能无法可靠支持挂起。唤醒设备（键盘、电源键）需要另行配置。

# HISTORY

**suspend** 子命令将系统睡眠功能整合进 systemd 命令界面，与电源管理和抑制锁机制协同工作。

# SEE ALSO

[systemctl-hibernate](/man/systemctl-hibernate)(1), [systemctl-hybrid-sleep](/man/systemctl-hybrid-sleep)(1), [systemctl-suspend-then-hibernate](/man/systemctl-suspend-then-hibernate)(1)
