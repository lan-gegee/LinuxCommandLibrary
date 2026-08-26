# TAGLINE

X11 屏保与锁屏工具

# TLDR

**启动屏保守护进程**

```xscreensaver &```

**启动时不显示启动画面**

```xscreensaver --no-splash &```

**立即激活屏保**

```xscreensaver-command -activate```

**锁定屏幕**

```xscreensaver-command -lock```

**停用屏保**（无需密码提示即解锁）

```xscreensaver-command -deactivate```

**打开偏好设置图形界面**

```xscreensaver-settings```

**预览特定屏保**

```xscreensaver-command -select [saver_number]```

**用新设置重启守护进程**

```xscreensaver-command -restart```

# SYNOPSIS

**xscreensaver** [_--no-splash_] [_--verbose_] [_--log file_]

**xscreensaver-command** [_-activate_] [_-lock_] [_-deactivate_] [_-restart_] [_-exit_] [_-select n_]

# PARAMETERS

**--no-splash**
> 启动时不显示启动画面。

**--verbose**
> 将诊断信息打印到 stderr。

**--log** _file_
> 将诊断信息追加到指定的日志文件。

**-display** _host:n_
> 连接到指定的 X display。

# COMMANDS (xscreensaver-command)

**-activate**
> 立即开启屏保。

**-deactivate**
> 若屏保处于激活状态则关闭它。

**-lock**
> 立即锁定屏幕。

**-select** _n_
> 切换到编号为 n 的屏保。

**-next**
> 切换到轮换序列中的下一个屏保。

**-prev**
> 切换到上一个屏保。

**-restart**
> 用当前设置重启屏保守护进程。

**-exit**
> 终止 xscreensaver 守护进程。

**-time**
> 打印距离上次用户活动的时间。

**-watch**
> 每当屏保状态变化时打印一行信息。

# DESCRIPTION

**XScreenSaver** 是 X Window System 的标准屏保和锁屏程序。它由一个监视用户活动并触发屏保的后台守护进程，以及 200 多个显示特效（独立的屏保程序）组成。

守护进程应在登录时启动，通常通过 **.xinitrc**、**.xsession** 或桌面环境的自动启动项。它监视键盘和鼠标活动来判断空闲时间。达到空闲阈值后，它会将屏幕变黑并运行屏保。可以在额外空闲时间后自动锁屏，也可以手动触发锁屏。

配置通过 **xscreensaver-settings**（原名 xscreensaver-demo）管理，这是一个基于 GTK 的 GUI，可以选择运行哪些屏保、调整计时以及预览效果。设置保存在 **~/.xscreensaver** 中。

该项目包含的屏保从经典特效（飞行烤面包机、Matrix）到 OpenGL 可视化和物理模拟应有尽有。每个屏保都是独立的可执行文件，也可以单独运行。

# CAVEATS

所有命令都需要守护进程正在运行才能生效。某些桌面环境（GNOME、KDE）有自己的锁屏工具，可能会产生冲突。OpenGL 屏保需要可用的 3D 加速。守护进程必须重启才能应用配置更改。电源管理（DPMS）设置可能与屏保计时产生意外的相互影响。

# HISTORY

**XScreenSaver** 由 Jamie Zawinski（jwz）创建，于 **1992 年**首次发布。它取代了早期零散的解决方案，成为 Unix 系统上事实标准的屏保。该项目已持续维护超过 30 年，定期添加新屏保和安全修复。Zawinski 一直强调 XScreenSaver 安全模型的重要性，尤其是锁屏方面。

# INSTALL

```apt: sudo apt install xscreensaver```

```dnf: sudo dnf install xscreensaver```

```pacman: sudo pacman -S xscreensaver```

```apk: sudo apk add xscreensaver```

```zypper: sudo zypper install xscreensaver```

```nix: nix profile install nixpkgs#xscreensaver```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xscreensaver-command](/man/xscreensaver-command)(1), [xscreensaver-settings](/man/xscreensaver-settings)(1), [xlock](/man/xlock)(1), [xset](/man/xset)(1)
