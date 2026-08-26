# TAGLINE

设置 X 根窗口外观

# TLDR

**设置纯色背景**

```xsetroot -solid [blue]```

**设置灰色背景**

```xsetroot -gray```

**从位图设置背景**

```xsetroot -bitmap [pattern.xbm]```

**创建格纹图案**

```xsetroot -mod [4] [4] -fg [red] -bg [white]```

**按名称设置光标**

```xsetroot -cursor_name [left_ptr]```

**重置为默认值**

```xsetroot -def```

**设置根窗口名称**

```xsetroot -name "[status text]"```

# SYNOPSIS

**xsetroot** [_options_]

# PARAMETERS

**-solid** _color_
> 将背景设置为纯色。

**-gray**, **-grey**
> 将背景设置为灰色网格图案。

**-bitmap** _file_
> 用位图文件平铺背景。

**-mod** _x_ _y_
> 创建格纹图案（x、y：1-16）。

**-fg**, **-foreground** _color_
> 图案的前景色。

**-bg**, **-background** _color_
> 图案的背景色。

**-rv**, **-reverse**
> 交换前景色和背景色。

**-cursor** _font_ _mask_
> 从字体字形设置光标。

**-cursor_name** _name_
> 按标准 X 光标名设置光标。

**-xcf** _file_ _size_
> 从 Xcursor 文件设置光标。

**-def**, **-default**
> 重置为默认设置。

**-name** _string_
> 设置根窗口的 name 属性。

**-d**, **-display** _display_
> 要连接的 X server。

**-help**
> 显示帮助信息。

**-version**
> 显示版本信息。

# DESCRIPTION

**xsetroot** 配置 X 根窗口（桌面背景）的外观。它可以设置纯色、图案、位图平铺以及根窗口的光标。

该工具常用于窗口管理器的启动脚本中，以设定初始背景外观。一次只能使用一个背景选项（-solid、-gray、-bitmap 或 -mod）。

-name 选项设置根窗口的 WM_NAME 属性，某些窗口管理器会用它来显示状态（例如 dwm 会将其显示在状态栏中）。

如需更复杂的背景，可以考虑使用 feh 或 nitrogen 等工具。

# CAVEATS

位图文件必须是 XBM 格式。颜色使用 X 颜色名或十六进制值（#RRGGBB）。某些合成型窗口管理器可能会覆盖根窗口的外观。-name 选项被 dwm 用作状态栏文本。

# HISTORY

**xsetroot** 自早期版本起就是 X Window System 的一部分。它遵循 Unix 哲学，提供简单而专注的根窗口定制功能。现在许多用户更喜欢 feh 等功能更丰富的壁纸工具。

# INSTALL

```apt: sudo apt install x11-xserver-utils```

```dnf: sudo dnf install xsetroot```

```apk: sudo apk add xsetroot```

```zypper: sudo zypper install xsetroot```

```nix: nix profile install nixpkgs#xsetroot```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[feh](/man/feh)(1), [nitrogen](/man/nitrogen)(1), [xwallpaper](/man/xwallpaper)(1), [hsetroot](/man/hsetroot)(1)
