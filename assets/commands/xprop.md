# TAGLINE

显示 X11 窗口属性

# TLDR

**点击选择窗口**并显示其属性

```xprop```

**显示根窗口的属性**

```xprop -root```

**按 ID 显示窗口属性**

```xprop -id [0x200007]```

**按名称显示窗口属性**

```xprop -name "[window_name]"```

**显示特定属性**

```xprop -root WM_NAME```

持续**监视属性变化**

```xprop -spy -id [window_id]```

**设置窗口上的某个属性**

```xprop -root -set [PROPERTY_NAME] "[value]"```

**移除窗口上的某个属性**

```xprop -root -remove [PROPERTY_NAME]```

# SYNOPSIS

**xprop** [_-display display_] [_-id id_] [_-name name_] [_-root_] [_-frame_] [_-spy_] [_property ..._]

# PARAMETERS

**-display** _display_
> 连接到指定的 X server。

**-id** _id_
> 按数字 ID 查询窗口（十进制或带 0x 前缀的十六进制）。

**-name** _name_
> 按窗口的 WM_NAME 属性（标题）查询窗口。

**-root**
> 显示根窗口（桌面）的属性。

**-frame**
> 选择窗口管理器的边框而不是客户端窗口。

**-len** _n_
> 将每个属性的输出限制在前 n 个字节内。

**-notype**
> 不打印属性类型，只打印名称和值。

**-spy**
> 持续监视属性变化事件。

**-set** _property_ _value_
> 在窗口上设置属性。

**-remove** _property_
> 从窗口上移除属性。

**-f** _atom_ _format_ [_dformat_]
> 指定解释属性所用的格式。

**-version**
> 打印版本号并退出。

# DESCRIPTION

**xprop** 显示 X Window System 窗口的属性。属性是应用程序和窗口管理器用来通信的任意数据，例如窗口标题（WM_NAME）、窗口类（WM_CLASS）和窗口状态。

在不带 **-id**、**-name** 或 **-root** 的情况下调用时，xprop 会显示一个十字光标，允许点击交互式选择窗口。可以在参数中列出特定属性，从而只显示这些属性。

常见属性包括 WM_NAME（标题）、WM_CLASS（应用类）、WM_STATE、_NET_WM_PID 以及各种扩展窗口管理器提示（Extended Window Manager Hints，_NET_WM_*）。

# CAVEATS

xprop 仅适用于 X11 窗口；Wayland 应用程序可能不会以相同方式暴露属性。窗口 ID 可以通过 **xwininfo** 或 **xdotool** 获得。属性名区分大小写。

# HISTORY

xprop 是标准 X.Org 工具集的一部分，自 **20 世纪 80 年代**早期 X11 发布以来就随 X Window System 发行版一同提供。它至今仍是 X11 环境中不可或缺的调试和脚本编写工具。

# INSTALL

```apt: sudo apt install x11-utils```

```dnf: sudo dnf install xprop```

```apk: sudo apk add xprop```

```zypper: sudo zypper install xprop```

```brew: brew install xprop```

```nix: nix profile install nixpkgs#xprop```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xwininfo](/man/xwininfo)(1), [xdotool](/man/xdotool)(1), [wmctrl](/man/wmctrl)(1), [xdpyinfo](/man/xdpyinfo)(1)
