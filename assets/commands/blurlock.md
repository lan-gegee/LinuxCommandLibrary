# TAGLINE

以模糊截图为背景锁定屏幕

# TLDR

用模糊截图**锁定**屏幕

```blurlock```

锁屏并**禁用解锁指示器**

```blurlock -u```

锁屏且**不隐藏**鼠标指针

```blurlock -p default```

锁屏并**显示失败次数**

```blurlock -f```

# SYNOPSIS

**blurlock** [_options_]

# DESCRIPTION

**blurlock** 是 **i3lock** 的封装工具：它截取当前屏幕的截图，应用模糊效果，并将其用作锁定屏幕的背景。这样既能遮挡屏幕内容，又能获得美观的锁屏画面。

该工具通常与 i3 窗口管理器及相关平铺式窗口管理器配合使用。

# PARAMETERS

**-u, --no-unlock-indicator**
> 禁用解锁指示器（按键时无反馈）。

**-p, --pointer** _mode_
> 控制鼠标指针的可见性（默认隐藏指针）。

**-f, --show-failed-attempts**
> 显示登录失败的次数。

# CAVEATS

需要 i3lock 以及 ImageMagick 或类似工具来实现模糊效果。截图会使锁定前稍有延迟。在多显示器环境下可能无法正常工作。

# SEE ALSO

[i3lock](/man/i3lock)(1), [xscreensaver](/man/xscreensaver)(1)
