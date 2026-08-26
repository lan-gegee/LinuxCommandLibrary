# TAGLINE

用于输入调试的 Wayland 事件查看器

# TLDR

监视**所有**事件

```wev```

按**接口**过滤

```wev -f [wl_keyboard]```

过滤特定**事件**

```wev -f [wl_keyboard]:[key]```

**排除**事件

```wev -F [wl_keyboard]:[key]```

将 **keymap** 写入文件

```wev -M [path/to/file]```

打印 **globals**

```wev -g```

# SYNOPSIS

**wev** [_OPTIONS_]

# PARAMETERS

**-f** _INTERFACE[:EVENT]_
> 只包含指定的接口/事件。可多次指定。

**-F** _INTERFACE[:EVENT]_
> 排除指定的接口/事件。可多次指定。

**-M** _FILE_
> 将 keymap 写入文件

**-g**
> 打印 Wayland globals

# DESCRIPTION

**wev** 在默认的 Wayland display 上打开一个 xdg-shell toplevel 窗口（通过 **WAYLAND_DISPLAY** 环境变量），然后打印与该窗口相关的事件。它实时显示键盘、鼠标、触摸等输入事件，类似于 X11 下的 **xev**。

该工具可用于调试 Wayland 输入处理、查找按键码以及理解 Wayland 协议事件。

# CAVEATS

仅限 Wayland。输出可能非常冗长。某些事件需要特定合成器的支持。

# INSTALL

```apt: sudo apt install wev```

```dnf: sudo dnf install wev```

```pacman: sudo pacman -S wev```

```apk: sudo apk add wev```

```zypper: sudo zypper install wev```

```nix: nix profile install nixpkgs#wev```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xev](/man/xev)(1), [libinput](/man/libinput)(1)
