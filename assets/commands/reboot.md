# TAGLINE

重启操作系统

# TLDR

**重启**系统

```reboot```

**关闭**系统电源

```reboot --poweroff```

**停止**系统但不关机

```reboot --halt```

不经过 init **强制立即重启**

```reboot --force```

只写入 **wtmp 记录**而不重启

```reboot --wtmp-only```

重启时不发送 **wall 消息**

```reboot --no-wall```

# SYNOPSIS

**reboot** [_OPTIONS_...]

# DESCRIPTION

**reboot** 用于重启机器。它会与系统管理器（systemd）通信来执行重启。该命令接受的选项与相关的 **poweroff** 和 **halt** 命令相同。

# PARAMETERS

**--halt**
> 停机而不重启

**-p, --poweroff**
> 关机而不是重启

**--reboot**
> 重启机器（默认动作）

**-f, --force**
> 不联络 init 系统，强制立即重启

**-w, --wtmp-only**
> 只写入 wtmp 关机记录，并不真正重启

**-d, --no-wtmp**
> 不写入 wtmp 关机记录

**-n, --no-sync**
> 重启前不同步硬盘

**--no-wall**
> 重启前不发送 wall 消息

# CAVEATS

使用 **--force** 会绕过 init 系统，如果文件系统未正确同步，可能导致数据丢失。**systemctl** 命令提供等效功能且带有更多特性。

# HISTORY

**reboot** 自早期 Unix 系统起就可用。在现代基于 systemd 的系统中，它通常是 **systemctl** 的符号链接。

# INSTALL

```apt: sudo apt install runit-init```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[poweroff](/man/poweroff)(8), [halt](/man/halt)(8), [systemctl](/man/systemctl)(1), [shutdown](/man/shutdown)(8)
