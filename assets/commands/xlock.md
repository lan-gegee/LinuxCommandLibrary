# TAGLINE

用屏幕保护程序锁定 X 显示器

# TLDR

**立即锁定屏幕**

```xlock```

**以指定模式锁定**

```xlock -mode [blank]```

**锁定并显示消息**

```xlock -message "[Away from desk]"```

**无需密码锁定（演示模式）**

```xlock -nolock```

**以指定超时时间锁定**

```xlock -timeout [30]```

**列出可用模式**

```xlock -help```

# SYNOPSIS

**xlock** [_options_]

# PARAMETERS

**-mode** _name_
> 显示模式（blank、life、maze 等）。

**-message** _text_
> 锁屏上显示的消息。

**-nolock**
> 演示模式；无需密码。

**-timeout** _seconds_
> 密码输入超时时间（秒）。

**-echokeys**
> 输入密码时回显字符。

**-usefirst**
> 使用密码提示时输入的首个字符。

**-allowaccess**
> 锁定期间允许 X 客户端访问。

**-remote**
> 允许远程锁定。

# DESCRIPTION

**xlock** 会锁定 X 显示器，直到用户输入密码。锁定期间屏幕显示可配置的动画或图案，并且拒绝新的 X server 连接。

多种显示模式可在锁定期间提供视觉效果。blank 模式只是让屏幕变黑，其他模式则显示生命模拟、迷宫或几何图案等动画。

该工具会将屏幕变黑、隐藏鼠标光标，并要求用户输入系统密码才能解锁。在身份验证成功之前，所有键盘和鼠标输入都会被捕获。

# CAVEATS

X11 屏幕锁定器存在根本性的安全局限。有更高安全需求时可考虑 xsecurelock。-allowaccess 之类的设置会降低安全性。可能无法阻止 X11 上的所有绕过手段。

# HISTORY

**xlock** 自 X Window System 早期起就是 X11 工具的一部分。虽然它仍然可用，但 xsecurelock 等现代替代品解决了 X11 架构固有的各种安全问题，这些问题是传统屏幕锁定器无法完全消除的。

# SEE ALSO

[xscreensaver](/man/xscreensaver)(1), [physlock](/man/physlock)(1), [i3lock](/man/i3lock)(1)
