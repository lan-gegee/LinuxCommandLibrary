# TAGLINE

显示 X11 窗口信息

# TLDR

**点击窗口获取其信息**

```xwininfo```

**获取根窗口信息**

```xwininfo -root```

**获取点击所选窗口的全部信息**

```xwininfo -all```

**按窗口 ID 获取**

```xwininfo -id [0x12345]```

**按窗口名称获取**

```xwininfo -name "[Window Name]"```

从根窗口开始递归**显示完整窗口树**

```xwininfo -root -tree```

以十进制而非十六进制**显示窗口 ID**

```xwininfo -int```

为特定窗口**显示窗口管理器提示**

```xwininfo -wm -id [0x12345]```

# SYNOPSIS

**xwininfo** [_-help_] [_-id wid_] [_-root_] [_-name wdname_] [_-int_] [_-children_] [_-tree_] [_-stats_] [_-bits_] [_-events_] [_-size_] [_-wm_] [_-shape_] [_-frame_] [_-all_] [_-english_] [_-metric_] [_-display host:dpy_] [_-version_]

# PARAMETERS

**-root**
> 不用光标选择，直接以根窗口为目标。

**-id** _wid_
> 按 X 窗口 ID 指定目标窗口。

**-name** _wdname_
> 按名称指定目标窗口。

**-int**
> 将所有 X 窗口 ID 显示为整数值。默认为十六进制。

**-children**
> 显示根窗口、父窗口和子窗口的 ID 与名称。

**-tree**
> 类似 -children，但递归显示所有子窗口。

**-stats**
> 显示位置和外观属性，包括大小、位置、色深和 visual 信息。未指定选项时这是默认行为。

**-bits**
> 显示位重力、窗口重力、backing-store 和 save-under 属性。

**-events**
> 显示所选窗口的事件掩码。

**-size**
> 显示尺寸提示，包括最小、最大尺寸和调整步长。

**-wm**
> 显示窗口管理器提示，包括输入模式、图标信息和初始状态。

**-shape**
> 显示窗口和边框形状的范围。

**-frame**
> 手动选择窗口时考虑窗口管理器的边框。

**-metric**
> 以毫米以及像素数两种单位显示尺寸。

**-english**
> 以英寸以及像素数两种单位显示尺寸。

**-all**
> 显示所有可用信息。

**-display** _host:dpy_
> 指定要连接的 X server。

**-version**
> 打印版本信息并退出。

# DESCRIPTION

**xwininfo** 显示 X11 窗口的详细信息，包括几何属性（大小和位置）、窗口 ID、色深、visual 类和 colormap。不带参数运行时，它会显示一个十字光标，供点击交互式选择窗口。

可以使用 **-id** 指定窗口 ID、**-name** 指定窗口标题或 **-root** 指定根窗口来定位特定窗口。**-tree** 选项显示完整的窗口层级，展示窗口之间的嵌套关系。如果未指定任何信息选项，则默认采用 **-stats**。该工具常用于调试窗口管理器以及编写 X11 窗口操作脚本。

# CAVEATS

仅支持 X11。不适用于 Wayland。属于 x11-utils 软件包（Arch 上为 xorg-xwininfo）。

# HISTORY

**xwininfo** 是用于显示窗口信息的标准 X11 工具。

# INSTALL

```apt: sudo apt install x11-utils```

```dnf: sudo dnf install xwininfo```

```apk: sudo apk add xwininfo```

```zypper: sudo zypper install xwininfo```

```brew: brew install xwininfo```

```nix: nix profile install nixpkgs#xwininfo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xprop](/man/xprop)(1), [xdotool](/man/xdotool)(1), [xlsclients](/man/xlsclients)(1), [xdpyinfo](/man/xdpyinfo)(1), [xkill](/man/xkill)(1), [wmctrl](/man/wmctrl)(1)
