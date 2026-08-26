# TAGLINE

控制运行中的 xscreensaver 守护进程

# TLDR

**立即激活屏保**

```xscreensaver-command -activate```

**锁定屏幕**

```xscreensaver-command -lock```

**停用屏保**

```xscreensaver-command -deactivate```

**重启屏保守护进程**

```xscreensaver-command -restart```

**退出屏保守护进程**

```xscreensaver-command -exit```

**显示当前状态**

```xscreensaver-command -time```

**监视状态变化**

```xscreensaver-command -watch```

# SYNOPSIS

**xscreensaver-command** [_options_]

# PARAMETERS

**-activate**
> 立即使屏幕变黑。

**-deactivate**
> 模拟用户活动；恢复屏幕显示。

**-lock**
> 立即锁定屏幕。

**-cycle**
> 切换到下一个屏保特效（hack）。

**-next** / **-prev**
> 切换到下一个/上一个特效。

**-select** _n_
> 切换到编号为 n 的特效。

**-restart**
> 用相同参数重启守护进程。

**-exit**
> 退出守护进程（锁定状态下会失败）。

**-time**
> 显示最近一次激活/停用的时间。

**-watch**
> 持续打印状态变化。

**-version**
> 打印正在运行的 xscreensaver 守护进程的版本号。

**-quiet**
> 仅在发生错误时打印输出。

**-verbose**
> 打印详细输出（默认）。

# DESCRIPTION

**xscreensaver-command** 通过发送客户端消息来控制运行中的 xscreensaver 守护进程。它可以激活、停用或锁定屏幕，切换显示模式，以及查询状态。

-watch 选项会流式输出状态变化，适用于需要对屏保事件作出反应的脚本。-deactivate 选项可以被周期性调用，以防视频播放期间屏幕变黑。

配置通过 xscreensaver-settings 完成，偏好设置写入 ~/.xscreensaver。

# CAVEATS

需要 xscreensaver 守护进程处于运行状态。屏保激活时切勿使用 kill -9。屏幕已锁定时 -exit 命令会失败。仅支持 X11。

# HISTORY

**xscreensaver** 由 Jamie Zawinski 于 1992 年创建，数十年来一直是最流行的 X11 屏保框架。其模块化设计将守护进程、显示特效和控制接口分离，支持高度自定义和第三方特效开发。

# INSTALL

```apt: sudo apt install xscreensaver```

```dnf: sudo dnf install xscreensaver```

```pacman: sudo pacman -S xscreensaver```

```apk: sudo apk add xscreensaver```

```zypper: sudo zypper install xscreensaver```

```nix: nix profile install nixpkgs#xscreensaver```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xscreensaver](/man/xscreensaver)(1), [xscreensaver-settings](/man/xscreensaver-settings)(1), [xlock](/man/xlock)(1)
