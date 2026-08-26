# TAGLINE

在屏幕上显示一只追逐鼠标光标的可爱小猫

# TLDR

**启动 oneko**

```oneko```

**使用其他角色**

```oneko -tora```

**改用小狗**

```oneko -dog```

**设置前景色**

```oneko -fg [blue]```

**设置动画速度**

```oneko -speed [16]```

**跟随指定窗口**

```oneko -name "[window_name]"```

# SYNOPSIS

**oneko** [_options_]

# PARAMETERS

**-tora**
> 虎纹猫。

**-dog**
> 改用小狗。

**-sakura**
> Sakura 角色。

**-tomoyo**
> Tomoyo 角色。

**-fg** _color_
> 前景色。

**-bg** _color_
> 背景色。

**-speed** _n_
> 动画速度。

**-name** _window_
> 跟随指定名称的窗口。

# DESCRIPTION

**oneko** 在屏幕上显示一只追逐鼠标光标的可爱小猫（neko）。当光标停止移动时，猫会坐下并最终入睡。

这是一个可追溯到早期 Unix 时代的经典 X11 桌面玩具。

# CHARACTERS

```
(default) - Regular cat
-tora     - Striped cat
-dog      - Dog
-sakura   - Sakura
-tomoyo   - Tomoyo
-bsd      - BSD daemon
```

# CAVEATS

仅限 X11。在 Wayland 下可能无法工作。需要 X11 合成器支持。可能分散注意力。

# HISTORY

oneko（お猫，"尊贵的小猫"）起源于日本的 NEC PC-9801。X11 版本由 **Tatsuya Kato** 于 **1991** 年创建。

# INSTALL

```dnf: sudo dnf install oneko```

```zypper: sudo zypper install oneko```

```nix: nix profile install nixpkgs#oneko```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xeyes](/man/xeyes)(1), [xscreensaver](/man/xscreensaver)(1)
