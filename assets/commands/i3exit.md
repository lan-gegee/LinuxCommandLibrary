# TAGLINE

为 i3 提供系统电源管理和会话控制的脚本

# TLDR

从 i3 **注销**

```i3exit logout```

**锁定**屏幕

```i3exit lock```

**挂起**系统

```i3exit suspend```

**休眠**系统

```i3exit hibernate```

**重启**系统

```i3exit reboot```

**关机**

```i3exit shutdown```

**切换用户**（回到登录界面）

```i3exit switch_user```

# SYNOPSIS

**i3exit** _command_

# PARAMETERS

**logout**
> 退出 i3 并返回显示管理器

**lock**
> 锁定屏幕

**suspend**
> 将系统挂起到内存

**hibernate**
> 将系统休眠到磁盘

**reboot**
> 重启系统

**shutdown**
> 关闭系统电源

**switch_user**
> 返回登录界面以便切换用户

# DESCRIPTION

**i3exit** 是一个为 i3 窗口管理器提供系统电源管理和会话控制的脚本。它将锁定、挂起、休眠和注销等常见操作封装成单条命令。

该脚本通常绑定到键盘快捷键或用于 i3 的模式菜单，无论底层显示管理器或 systemd 配置如何，都能为电源管理操作提供一致的行为。

# CAVEATS

电源管理操作需要相应的权限。具体行为可能因显示管理器和 systemd 配置而异。某些命令可能需要 polkit 身份验证。

# HISTORY

i3exit 为 Manjaro Linux 的 i3 版本开发，旨在为 i3 用户提供便捷的电源管理界面。它屏蔽了不同电源管理后端之间的差异。

# INSTALL

```aur: yay -S i3exit```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[i3](/man/i3)(1), [systemctl](/man/systemctl)(1), [loginctl](/man/loginctl)(1)
