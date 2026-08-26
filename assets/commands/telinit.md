# TAGLINE

更改 SysV init 运行级别

# TLDR

**关机**

```telinit 0```

**重启**

```telinit 6```

更改**运行级别**

```telinit [2|3|4|5]```

进入**救援**模式

```telinit 1```

**重新加载**守护进程配置

```telinit q```

重启/关机时**不发送 wall** 消息

```telinit --no-wall [0|6]```

# SYNOPSIS

**telinit** [_OPTIONS_] _COMMAND_

# RUNLEVELS

**0** - 关机

**1** - 单用户/救援模式

**2, 3, 4** - 多用户模式

**5** - 带 GUI 的多用户模式

**6** - 重启

**q, Q** - 重新加载配置

# PARAMETERS

**--no-wall**
> 重启/关机前不发送 wall 消息

# DESCRIPTION

**telinit** 用于更改 SysV init 运行级别。在 systemd 系统上，运行级别请求会被透明地转换为 systemd target 的激活：

- 0 → poweroff.target
- 1 → rescue.target
- 2-4 → multi-user.target
- 5 → graphical.target
- 6 → reboot.target

# CAVEATS

SysV 运行级别的概念在 systemd 系统上已经过时。原生的 systemd 操作请改用 `systemctl` 命令。该命令仅为向后兼容而提供。

# HISTORY

**telinit** 起源于早于 systemd 的 SysV init。在 systemd 系统上，它是一个兼容性包装器，把运行级别转换为 systemd target。

# INSTALL

```apt: sudo apt install systemd-sysv```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[systemctl](/man/systemctl)(1), [init](/man/init)(1), [runlevel](/man/runlevel)(8)
