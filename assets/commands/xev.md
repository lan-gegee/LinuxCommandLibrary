# TAGLINE

X11 事件监视工具

# TLDR

**启动 xev**

```xev```

**仅显示键盘事件**

```xev -event keyboard```

**仅显示鼠标按键**事件

```xev -event button```

按 ID **监视特定窗口**

```xev -id [window_id]```

**监视根窗口**事件

```xev -root```

# SYNOPSIS

**xev** [_-event type_] [_-id window_] [_-root_] [_options_]

# PARAMETERS

**-display** _DISPLAY_
> 要连接的 X server。

**-event** _TYPE_
> 事件类型过滤器（可多次指定）。

**-id** _WINDOW_
> 按 ID 监视已有窗口上的事件。

**-root**
> 监视根窗口上的事件。

**-name** _NAME_
> 分配给所创建窗口的名称。

**-geometry** _GEOM_
> 窗口大小和位置。

**-bw** _PIXELS_
> 窗口的边框宽度。

**-bs** _TYPE_
> 后备存储类型（NotUseful、WhenMapped、Always）。默认 NotUseful。

**-rv**
> 以反色显示窗口。

# EVENT TYPES

**keyboard** - 按键按下/释放事件
**mouse** - 所有指针事件
**button** - 鼠标按钮按下/释放事件
**motion** - 指针移动事件
**expose** - 重绘（expose）事件
**visibility** - 可见性变化事件
**structure** - 窗口结构事件
**substructure** - 子结构事件
**focus** - 焦点变化事件
**property** - 属性变化事件
**colormap** - 色彩映射表事件
**owner_grab_button** - 所有者抓取按钮事件
**randr** - RandR 事件

# DESCRIPTION

**xev** 是一个 X11 事件监视工具，用于显示窗口接收到的所有事件。启动后它会打开一个小窗口，并打印该窗口内发生的每个 X 事件的详细信息，包括按键、鼠标移动、按钮点击、窗口重绘以及焦点变化。

该工具主要用于调试 X11 输入问题以及查找键盘配置所需的键码。每个事件都会连同完整细节一起打印，包括键码、键符号、坐标、修饰键状态和时间戳。这使得它在配置窗口管理器的按键绑定或诊断输入问题时不可或缺。

可以使用 **-event** 选项按类型过滤事件，只显示键盘、鼠标、按钮或移动事件。**-id** 选项监视某个特定已有窗口上的事件，而 **-root** 则捕获根窗口上的事件，用于全屏范围的监视。

# CAVEATS

仅支持 X11，不支持 Wayland。会创建一个可见窗口。输出较为冗长。

# HISTORY

**xev** 是标准 X11 工具的一部分。它是理解 X 输入事件和配置按键绑定的必备工具。

# INSTALL

```apt: sudo apt install x11-utils```

```dnf: sudo dnf install xev```

```apk: sudo apk add xev```

```zypper: sudo zypper install xev```

```nix: nix profile install nixpkgs#xev```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xdotool](/man/xdotool)(1), [xmodmap](/man/xmodmap)(1), [xinput](/man/xinput)(1)
