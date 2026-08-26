# TAGLINE

改进版的屏幕锁定工具

# TLDR

以白色背景**锁定屏幕**

```i3lock```

以纯色背景**锁定**

```i3lock -c [000000]```

以背景图片**锁定**

```i3lock -i [path/to/image.png]```

以平铺的背景图片**锁定**

```i3lock -t -i [path/to/image.png]```

**锁定**且不显示解锁指示器

```i3lock -u```

**锁定**并显示失败的认证尝试次数

```i3lock -f```

**锁定**且不派生到后台

```i3lock -n```

# SYNOPSIS

**i3lock** [_options_]

# PARAMETERS

**-v**, **--version**
> 显示 i3lock 的版本。

**-n**, **--nofork**
> 启动后不派生。适合与其他命令组合使用。

**-b**, **--beep**
> 认证失败时发出蜂鸣声。

**-c** _RRGGBB_, **--color** _RRGGBB_
> 以 6 字节十六进制格式设置背景颜色（默认：白色）。

**-i** _PATH_, **--image** _PATH_
> 显示指定的 PNG 图片作为背景，而非空白屏幕。

**-t**, **--tiling**
> 将图片平铺到整个屏幕。

**-u**, **--no-unlock-indicator**
> 禁用输入时显示的解锁指示圆圈。

**-f**, **--show-failed-attempts**
> 显示认证失败的次数。

**-p** _win|default_, **--pointer** _win|default_
> 控制鼠标指针可见性。"default" 显示指针，"win" 显示 Windows 风格的指针。

**-e**, **--ignore-empty-password**
> 不校验空密码。

**--raw** _FORMAT_
> 以原始字节而非 PNG 格式读取 --image 给出的图片。

**--debug**
> 启用调试日志。注意：这会将密码记录到 stdout。

# DESCRIPTION

**i3lock** 是一款基于 slock 的改进版屏幕锁定工具。它显示空白屏幕或图片，并要求通过 PAM 认证（通常是输入密码）来解锁。在可配置的超时后，屏幕会通过 DPMS 关闭。

输入时会显示一个解锁指示圆圈：验证期间填充为绿色，失败时填充为红色，空闲时清空。该指示器在不暴露密码长度的情况下提供视觉反馈。

此锁屏工具为 i3 窗口管理器设计，但可在任何 X11 会话中使用。

# CAVEATS

仅支持 X11；Wayland 请改用 **swaylock**。仅支持 PNG 图片（除非使用 --raw）。**i3lock-color** 分支增加了许多额外功能，例如自定义圆环颜色和时钟显示。

# HISTORY

**i3lock** 由 Michael Stapelberg 创建，作为 **i3** 窗口管理器的锁屏工具，注重简洁与安全。它是 **slock** 的显著改进版本，加入了解锁指示器和 PAM 支持等特性。

# INSTALL

```apt: sudo apt install i3lock```

```dnf: sudo dnf install i3lock```

```pacman: sudo pacman -S i3lock```

```apk: sudo apk add i3lock```

```zypper: sudo zypper install i3lock```

```nix: nix profile install nixpkgs#i3lock```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[i3](/man/i3)(1), [swaylock](/man/swaylock)(1), [xlock](/man/xlock)(1), [xdotool](/man/xdotool)(1)
