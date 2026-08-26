# TAGLINE

在 X11 和 Wayland 上模拟输入

# TLDR

启动**守护进程**

```ydotoold```

**左键点击**

```ydotool click 0xC0```

**右键点击**

```ydotool click 0xC1```

按下 **Alt+F4**

```ydotool key 56:1 62:1 62:0 56:0```

# SYNOPSIS

**ydotool** _COMMAND_ [_OPTIONS_]

# PARAMETERS

**click** _CODE_
> 模拟鼠标点击（0xC0=左键，0xC1=右键，0xC2=中键）

**key** _KEYCODE:STATE..._
> 模拟按键按下/释放（1=按下，0=释放）

**type** _TEXT_
> 输入文本字符串

**mousemove** _X_ _Y_
> 将鼠标移动到指定位置

# DESCRIPTION

**ydotool** 在 Linux 上模拟键盘和鼠标输入。与 xdotool 不同，它通过内核的 uinput 模块工作，因此在 X11 和 Wayland 上都能使用。

需要 ydotoold 守护进程正在运行。

# CAVEATS

需要 ydotoold 守护进程正在运行。需要访问 /dev/uinput。键码是硬件扫描码，而非 X11 keysym。

# INSTALL

```dnf: sudo dnf install ydotool```

```pacman: sudo pacman -S ydotool```

```zypper: sudo zypper install ydotool```

```nix: nix profile install nixpkgs#ydotool```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xdotool](/man/xdotool)(1), [wtype](/man/wtype)(1)
