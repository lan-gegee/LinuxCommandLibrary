# TAGLINE

先挂起，延时后自动休眠

# TLDR

**先挂起再休眠**

```systemctl suspend-then-hibernate```

**强制**执行先挂起再休眠

```systemctl suspend-then-hibernate -f```

# SYNOPSIS

**systemctl suspend-then-hibernate** [_OPTIONS_]

# PARAMETERS

**-f, --force**
> 即使存在抑制锁也强制执行操作

**--no-wall**
> 不向用户发送 wall 消息

# DESCRIPTION

**systemctl suspend-then-hibernate** 先将系统挂起到内存，然后在设定的延时之后自动唤醒并休眠到磁盘。这样既能在刚挂起后不久唤醒时享受快速恢复速度，又能在长时间睡眠期间电池耗尽时防止数据丢失。

进入休眠前的延时可通过 **/etc/systemd/sleep.conf** 中的 **HibernateDelaySec=** 选项配置（默认值因发行版而异）。

# CAVEATS

需要挂起和休眠都能正常工作。休眠需要足够的交换空间。延时计时器会唤醒系统以进行休眠，消耗一些电量。并非在所有硬件上都能可靠工作。

# HISTORY

**suspend-then-hibernate** 子命令结合了挂起快速唤醒的优势与长时空闲时休眠的安全性，非常适合过夜睡眠的笔记本电脑。

# SEE ALSO

[systemctl-suspend](/man/systemctl-suspend)(1), [systemctl-hibernate](/man/systemctl-hibernate)(1), [systemctl-hybrid-sleep](/man/systemctl-hybrid-sleep)(1)
