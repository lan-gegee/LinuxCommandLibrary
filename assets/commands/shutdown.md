# TAGLINE

安全地关机或重启系统

# TLDR

立即**关机**

```shutdown -h now```

立即**重启**

```shutdown -r now```

5 分钟后**重启**

```shutdown -r +5 &```

在下午 1 点**关机**（24 小时制）

```shutdown -h 13:00```

**取消**挂起的关机/重启

```shutdown -c```

# SYNOPSIS

**shutdown** [_options_] [_time_] [_message_]

# PARAMETERS

**-h, --halt**
> 关机后停止系统

**-P, --poweroff**
> 关闭系统电源（-h 的默认行为）

**-r, --reboot**
> 重启系统

**-c**
> 取消挂起的关机

**-k**
> 只发送警告消息但不真正关机

**now**
> 立即执行

**+_m_**
> m 分钟后执行

**_hh:mm_**
> 在指定时间执行（24 小时制）

# DESCRIPTION

**shutdown** 以安全方式关闭系统。它会通知所有已登录用户、阻止新登录，并通知运行中的进程优雅地终止。

时间参数指定何时关机：**now** 表示立即执行，**+m** 表示从现在起 m 分钟后，**hh:mm** 表示具体时间。还可以向所有用户广播一条可选消息。

# CAVEATS

需要 root 权限。计划中的关机可用 **-c** 取消。在 systemd 系统上，此命令通常是 **systemctl poweroff/reboot** 的封装。

# HISTORY

**shutdown** 命令起源于早期 Unix 系统。它从一个简单的系统停机工具演变为带用户通知功能的完整系统安全关机工具。

# INSTALL

```apt: sudo apt install runit-init```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[reboot](/man/reboot)(8), [halt](/man/halt)(8), [poweroff](/man/poweroff)(8), [systemctl](/man/systemctl)(1)
