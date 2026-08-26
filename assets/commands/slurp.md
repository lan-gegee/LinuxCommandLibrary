# TAGLINE

Wayland 区域选择工具

# TLDR

**选择一个区域**并打印到 stdout

```slurp```

选择区域时**显示尺寸**

```slurp -d```

选择**单个点**而不是区域

```slurp -p```

选择一个**输出设备**并打印其名称

```slurp -o -f '%o'```

选择区域并用 grim 拍摄**无边框截图**

```grim -g "$(slurp -w 0)"```

选择区域并用 wf-recorder **录制视频**

```wf-recorder -g "$(slurp -w 0)"```

# SYNOPSIS

**slurp** [_options_]

# PARAMETERS

**-d**
> 显示选区的尺寸

**-p**
> 选择单个点而不是区域

**-o**
> 选择整个输出设备（显示器）

**-r**
> 要求选区位于单个输出设备之内

**-b** _color_
> 设置选区框的背景颜色

**-c** _color_
> 设置选区框的边框颜色

**-s** _color_
> 设置选区颜色

**-w** _width_
> 设置选区边框宽度（0 表示无边框）

**-f** _format_
> 输出格式字符串（%x、%y、%w、%h、%o）

**-a** _ratio_
> 强制宽高比（如 16:9）

# DESCRIPTION

**slurp** 允许用户在 Wayland 合成器上交互式地选择一个区域。它以其他工具可用的格式输出所选区域的坐标，例如配合 **grim** 截图或 **wf-recorder** 录屏。

该工具渲染一层半透明遮罩，让用户点击并拖拽来选择矩形区域。它的设计目的是通过 shell 命令替换与其他 Wayland 原生工具组合使用。

# CAVEATS

仅支持 Wayland；需要支持 layer-shell 协议的合成器。它本身不捕获图像；截图请配合 **grim** 使用。颜色值使用 #RRGGBBAA 格式。

# HISTORY

由 **Simon Ser**（emersion）编写，是 Wayland 的 sway/wlroots 生态的一部分。它提供相当于 X11 上 **scrot -s** 的区域选择功能，并适配了 Wayland 的安全模型。

# INSTALL

```apt: sudo apt install slurp```

```dnf: sudo dnf install slurp```

```pacman: sudo pacman -S slurp```

```apk: sudo apk add slurp```

```zypper: sudo zypper install slurp```

```nix: nix profile install nixpkgs#slurp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[grim](/man/grim)(1), [wf-recorder](/man/wf-recorder)(1), [scrot](/man/scrot)(1)
