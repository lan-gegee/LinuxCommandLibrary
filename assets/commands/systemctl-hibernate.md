# TAGLINE

将系统休眠到磁盘

# TLDR

立即**休眠**系统

```systemctl hibernate```

**强制**休眠，忽略抑制锁

```systemctl hibernate --force```

不向已登录用户发送 **wall 消息**休眠

```systemctl hibernate --no-wall```

# SYNOPSIS

**systemctl hibernate** [_OPTIONS_]

# DESCRIPTION

**systemctl hibernate** 将系统休眠：把当前状态保存到磁盘（swap）后断电。再次开机时，系统会从上次中断的地方恢复。

# PARAMETERS

**-f, --force**
> 即使存在抑制锁（阻止睡眠的程序）也强制休眠。指定两次时，操作将在不联系登录管理器的情况下执行。

**--no-wall**
> 休眠前不向已登录用户发送 wall 消息

**-i, --ignore-inhibitors**
> 执行休眠操作时忽略抑制锁

# CAVEATS

需要足够的 swap 空间来容纳内存内容。硬件层面必须支持休眠。某些系统可能需要额外的内核参数才能正常休眠。

# HISTORY

**systemctl hibernate** 是 Linux 系统与服务管理器 **systemd** 的一部分，提供现代电源管理能力。

# SEE ALSO

[systemctl](/man/systemctl)(1), [systemctl-suspend](/man/systemctl-suspend)(1), [systemctl-hybrid-sleep](/man/systemctl-hybrid-sleep)(1), [systemctl-suspend-then-hibernate](/man/systemctl-suspend-then-hibernate)(1), [systemctl-poweroff](/man/systemctl-poweroff)(1)
