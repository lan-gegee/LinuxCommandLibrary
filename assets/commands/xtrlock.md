# TAGLINE

透明的 X 显示锁屏工具

# TLDR

**锁定**显示器

```xtrlock```

锁定时同时使屏幕**变黑**

```xtrlock -b```

锁定并 **fork** 到后台

```xtrlock -f```

# SYNOPSIS

**xtrlock** [_OPTIONS_]

# PARAMETERS

**-b**
> 锁定的同时使屏幕变黑

**-f**
> fork 到后台并立即返回

# DESCRIPTION

**xtrlock** 锁定 X 显示，直到用户输入密码为止。锁定期间，光标变为挂锁图标，键盘输入会被捕获用于身份验证。

这种锁是透明的：桌面仍然可见，但无法交互。

# CAVEATS

仅支持 X11。默认不会使屏幕变黑。身份验证需要正确的 PAM 配置。

# INSTALL

```apt: sudo apt install xtrlock```

```dnf: sudo dnf install xtrlock```

```pacman: sudo pacman -S xtrlock```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xlock](/man/xlock)(1), [i3lock](/man/i3lock)(1), [vlock](/man/vlock)(1)
