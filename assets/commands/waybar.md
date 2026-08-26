# TAGLINE

可定制的 Wayland 状态栏

# TLDR

**启动 waybar**

```waybar```

**使用指定的配置文件启动**

```waybar -c [~/.config/waybar/config]```

**使用指定的样式文件启动**

```waybar -s [~/.config/waybar/style.css]```

**在指定的栏上启动**

```waybar -b [bar-0]```

**记录日志到文件**

```waybar -l [/tmp/waybar.log]```

# SYNOPSIS

**waybar** [_-c config_] [_-s style_] [_-b bar_] [_-l log_] [_options_]

# PARAMETERS

**-c** _FILE_
> 配置文件。

**-s** _FILE_
> 样式文件（CSS）。

**-b** _BAR_
> 栏名称。

**-l** _FILE_
> 日志文件。

**-h**, **--help**
> 显示帮助。

**-v**, **--version**
> 显示版本。

# DESCRIPTION

**waybar** 是一款适用于 Wayland 合成器的可定制状态栏。它支持 Sway、Hyprland 以及其他基于 wlroots 的合成器。

配置采用 JSON/JSON5 格式。模块定义内容：工作区、时钟、电池、网络、CPU、内存等众多模块。

样式基于 CSS。颜色、字体、内边距和布局均可自定义。不同模块可以应用不同的样式。

内置模块覆盖常见需求。自定义模块可通过执行脚本提供专门信息。

点击模块可运行命令。右键、中键和滚轮动作均可配置。

状态栏响应式更新。系统变化会触发更新，尽可能避免轮询。

# CAVEATS

仅限 Wayland——不支持 X11。部分模块依赖于特定合成器。高级样式定制时 CSS 可能变得复杂。

# HISTORY

**Waybar** 由 **Alex D.**（Alexays）于 **2018 年**前后为 Sway 和其他 wlroots 合成器创建。它成为 Wayland 上标准的 status bar，地位类似于 polybar 在 X11 上的角色。

# INSTALL

```apt: sudo apt install waybar```

```dnf: sudo dnf install waybar```

```pacman: sudo pacman -S waybar```

```apk: sudo apk add waybar```

```zypper: sudo zypper install waybar```

```nix: nix profile install nixpkgs#waybar```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sway](/man/sway)(1), [polybar](/man/polybar)(1), [i3status](/man/i3status)(1), [hyprland](/man/hyprland)(1)
