# TAGLINE

指示系统停止所有进程并暂停 CPU

# TLDR

**停机**系统

```halt```

**关闭电源**（等同于 poweroff）

```halt -p```

**重启**系统（等同于 reboot）

```halt --reboot```

**立即停机**，不联系系统管理器

```halt -f```

仅写入 wtmp 关机记录而**不实际停机**

```halt -w```

# SYNOPSIS

**halt** [_options_]

# PARAMETERS

**-p**, **--poweroff**
> 关闭机器电源（等同于 poweroff）

**--reboot**
> 重启机器（等同于 reboot）

**--halt**
> 停机，无论调用的是哪个命令

**-f**, **--force**
> 强制立即停机，不联系 init 系统

**-w**, **--wtmp-only**
> 仅写入 wtmp 记录，并不真正停机

**-d**, **--no-wtmp**
> 不写入 wtmp 记录

**--no-wall**
> 停机前不发送 wall 消息

# DESCRIPTION

**halt** 指示系统停止所有进程并暂停 CPU。在使用 systemd 的现代系统上，halt 是指向 systemctl 的符号链接，会触发正常的关机流程。

halt、poweroff 和 reboot 的区别：
- **halt** - 停止 CPU，但电源可能保持开启
- **poweroff** - 停止 CPU 并切断机器电源
- **reboot** - 重启机器

实际上，大多数系统对 halt 和 poweroff 的处理类似，都会关闭机器电源。

# CAVEATS

使用 **-f** 会绕过正常的关机流程，可能导致数据丢失。在 systemd 系统上，这些命令都是 systemctl 的封装。运行 halt 通常需要 root 权限。

# HISTORY

halt 是一个可以追溯到早期 Unix 系统的传统 Unix 命令。在使用 systemd 的现代 Linux 发行版上，halt、poweroff 和 reboot 都是指向 systemctl 的符号链接，在使用 systemd 关机机制的同时提供了向后兼容性。

# INSTALL

```apt: sudo apt install runit-init```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[poweroff](/man/poweroff)(8), [reboot](/man/reboot)(8), [shutdown](/man/shutdown)(8), [systemctl](/man/systemctl)(1)
