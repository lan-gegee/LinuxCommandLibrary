# TAGLINE

同时挂起到内存和磁盘

# TLDR

进入**混合睡眠**

```systemctl hybrid-sleep```

**强制**混合睡眠

```systemctl hybrid-sleep -f```

不发送 **wall** 消息进入睡眠

```systemctl hybrid-sleep --no-wall```

# SYNOPSIS

**systemctl hybrid-sleep** [_OPTIONS_]

# PARAMETERS

**-f, --force**
> 即使存在抑制锁也强制睡眠

**--no-wall**
> 不向已登录用户发送 wall 消息

# DESCRIPTION

**systemctl hybrid-sleep** 使系统进入混合睡眠，它结合了挂起到内存和休眠。系统状态会同时保存到内存和磁盘，然后系统进入低功耗挂起模式。

如果电力得以维持，系统能从内存快速唤醒。如果断电，系统仍可从磁盘上的休眠镜像恢复。这兼顾了两者的优点，代价是更长的入睡时间。

# CONFIGURATION

**/etc/systemd/sleep.conf**
> 通过 HybridSleepMode、HybridSleepState 和 AllowHybridSleep 设置控制混合睡眠行为。

# CAVEATS

要求硬件同时支持挂起和休眠。由于要将休眠镜像写入磁盘，比常规挂起耗时更长。需要足够的 swap 空间用于休眠。在某些系统上启用安全启动时可能无法工作。

# HISTORY

混合睡眠的引入是为了应对笔记本电池完全耗尽时挂起中数据丢失的风险，将快速恢复与休眠的安全性结合起来。

# SEE ALSO

[systemctl-suspend](/man/systemctl-suspend)(1), [systemctl-hibernate](/man/systemctl-hibernate)(1), [systemctl-suspend-then-hibernate](/man/systemctl-suspend-then-hibernate)(1), [systemctl](/man/systemctl)(1)
