# TAGLINE

不重启内核而重启用户空间

# TLDR

**软重启**（仅用户空间）

```systemctl soft-reboot```

**强制**软重启

```systemctl soft-reboot -f```

**安排**软重启

```systemctl soft-reboot --when "[timestamp]"```

**取消**已安排的软重启

```systemctl soft-reboot --when cancel```

# SYNOPSIS

**systemctl soft-reboot** [_OPTIONS_]

# PARAMETERS

**-f, --force**
> 即使存在抑制锁也强制重启

**--when** _TIMESTAMP_
> 在指定时间安排重启或取消

# DESCRIPTION

**systemctl soft-reboot** 关闭并重启用户空间，同时保持内核继续运行。由于跳过了 BIOS/固件初始化和内核引导，这比完整重启快得多。

内核持续运行；只有 systemd 和所有用户服务被重启。这适用于快速测试服务配置或应用无需更换内核的更新。

# CAVEATS

需要内核支持。当需要应用内核更新时不适用。部分硬件状态可能不恰当地保留下来。这是较新的功能，需要较新版本的 systemd。

# HISTORY

**soft-reboot** 子命令在 systemd **254** 中加入，用于在只需用户空间更改生效的场景下实现更快的系统重启。

# SEE ALSO

[systemctl-reboot](/man/systemctl-reboot)(1), [systemctl-kexec](/man/systemctl-kexec)(1), [systemctl](/man/systemctl)(1)
