# TAGLINE

轻量级独立系统托盘面板

# TLDR

运行 trayer

```trayer```

将位置设为某条**边**

```trayer --edge [left|right|top|bottom]```

设置**尺寸**

```trayer --width [10] --height [32]```

设置宽度的**类型**和数值

```trayer --widthtype [pixel|percent] --width [72]```

对齐面板

```trayer --align [left|center|right]```

设置图标**间距**

```trayer --iconspacing [10]```

# SYNOPSIS

**trayer** [_OPTIONS_]

# PARAMETERS

**--edge** _POSITION_
> 将面板放置在 _left_、_right_、_top_、_bottom_ 或 _none_（默认：_bottom_）

**--align** _DIRECTION_
> 图标对齐方式：_left_、_center_、_right_ 或 _none_（默认：_center_）

**--widthtype** _TYPE_
> 宽度的解释方式：_request_、_pixel_、_percent_ 或 _none_（默认：_percent_）

**--width** _N_
> 面板宽度数值，按 **--widthtype** 解释（默认：_100_）

**--heighttype** _TYPE_
> 高度的解释方式：_request_、_pixel_、_percent_ 或 _none_（默认：_pixel_）

**--height** _N_
> 面板高度数值（默认：_26_）

**--margin** _N_
> 距屏幕边缘的边距，单位为像素（默认：_0_）

**--distance** _N_
> trayer 窗口与屏幕边缘的距离，单位为像素（默认：_0_）

**--distancefrom** _EDGE_
> **--distance** 从哪条边算起：_top_、_bottom_、_left_、_right_（默认：_top_）

**--padding** _N_
> 边框与图标之间的额外像素间距（默认：_0_）

**--iconspacing** _N_
> 图标之间的间距，单位为像素

**--monitor** _N_
> 目标显示器，按索引 (0..N) 或 _primary_（默认：_0_）

**--transparent** _BOOL_
> 启用透明：_true_ 或 _false_（默认：_false_）

**--alpha** _N_
> 透明程度 (0 = 不透明，255 = 完全透明；默认：_127_)

**--tint** _COLOR_
> 背景色调，十六进制值，例如 _0xFFFFFFFF_

**--expand** _BOOL_
> 允许 trayer 扩展以利用多余空间（默认：_true_）

**--SetDockType** _BOOL_
> 将面板窗口标识为 dock 类型的窗口（默认：_true_）

**--SetPartialStrut** _BOOL_
> 保留面板空间，避免其他窗口与其重叠（默认：_false_）

# DESCRIPTION

**trayer** 是一个基于 GTK-2 的轻量级系统托盘面板。它提供一个独立的系统托盘，可用于那些自身不带系统托盘实现的极简窗口管理器。

该面板显示来自应用程序的系统托盘图标，并可根据用户偏好调整位置和大小。

# CAVEATS

需要 GTK-2。可能不支持所有现代托盘图标特性。透明效果需要合成器支持。某些窗口管理器可能与面板定位冲突。

# HISTORY

**trayer** 作为独立系统托盘开发，供缺乏内置系统托盘支持的平铺式和极简窗口管理器使用。

# INSTALL

```apt: sudo apt install trayer```

```nix: nix profile install nixpkgs#trayer```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[stalonetray](/man/stalonetray)(1)
