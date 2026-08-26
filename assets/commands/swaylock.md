# TAGLINE

Sway Wayland 合成器的屏幕锁定工具

# TLDR

**锁定屏幕**

```swaylock```

**使用纯色**

```swaylock -c [1a1a2e]```

**使用图像**

```swaylock -i [wallpaper.jpg]```

**每个输出使用不同图像**

```swaylock -i [HDMI-A-1:wallpaper.jpg]```

**模糊效果**

```swaylock --effect-blur [7x5]```

**显示失败次数**

```swaylock -f --show-failed-attempts```

**以守护进程方式运行**

```swaylock -f```

# SYNOPSIS

**swaylock** [_-c color_] [_-i image_] [_-f_] [_options_]

# PARAMETERS

**-c**, **--color** _COLOR_
> 背景颜色。

**-i**, **--image** _IMAGE_
> 背景图像。

**-f**, **--daemonize**
> 以守护进程方式运行。

**-s**, **--scaling** _MODE_
> 图像缩放方式。

**--effect-blur** _PARAMS_
> 模糊效果。

**--show-failed-attempts**
> 显示失败情况。

**--indicator-radius** _N_
> 指示器大小。

# DESCRIPTION

**swaylock** 是面向 Sway 和其他 Wayland 合成器的屏幕锁定工具，通过基于 PAM 的认证提供安全的会话锁定。它会在所有输出上渲染锁屏界面，并要求输入用户密码才能解锁。

锁屏背景可以自定义纯色或图像，多显示器环境中还支持为每个输出指定不同图像。指示环会显示当前状态：空闲、正在输入、密码验证中以及密码错误。swaylock-effects 分支增加了模糊等更多视觉效果。

daemonize 参数使 swaylock 在显示锁屏后 fork 到后台运行。与 swayidle 的 before-sleep 事件配合使用时，这一选项至关重要，可确保系统挂起前屏幕已锁定。

# CAVEATS

仅支持 Wayland/Sway。需要配置 PAM。某些效果需要 swaylock-effects 分支。

# HISTORY

**swaylock** 是 **Sway** 合成器的屏幕锁定工具，是 i3lock 在 Wayland 上的替代品。

# INSTALL

```apt: sudo apt install swaylock```

```dnf: sudo dnf install swaylock```

```pacman: sudo pacman -S swaylock```

```apk: sudo apk add swaylock```

```zypper: sudo zypper install swaylock```

```nix: nix profile install nixpkgs#swaylock```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sway](/man/sway)(1), [swaybg](/man/swaybg)(1), [i3lock](/man/i3lock)(1)
