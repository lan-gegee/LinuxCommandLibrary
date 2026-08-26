# TAGLINE

X11 的交互式屏幕区域选择工具

# TLDR

获取**屏幕选区**并输出几何信息

```slop```

用**双击**代替点击拖拽

```slop -D```

以**高亮**方式显示选区而非描边

```slop -l```

指定**输出格式**

```slop -f "%g"```

设置选区**颜色**

```slop -c [red],[green],[blue],[alpha]```

设置**边框粗细**

```slop -b [thickness]```

# SYNOPSIS

**slop** [**-klqnD**] [_OPTIONS_]

# PARAMETERS

**-f, --format** _string_
> 输出格式，可用占位符：%x、%y、%w、%h、%i（窗口 ID）、%c（取消）、%g（几何信息）

**-b, --bordersize** _float_
> 选区矩形的边框厚度

**-p, --padding** _float_
> 选区周围的留白（负值表示收缩）

**-c, --color** _r,g,b,a_
> 选区框颜色，RGBA 浮点数（0.0-1.0）

**-t, --tolerance** _float_
> 区分点击与拖拽的像素阈值

**-D, --nodrag**
> 使用两次点击模式代替点击拖拽

**-l, --highlight**
> 填充选区区域而不是绘制边框

**-n, --nodecorations** _int_
> 窗口装饰移除的激进程度（0-2）

**-k, --nokeyboard**
> 禁用键盘取消

**-q, --quiet**
> 抑制警告消息

**-r, --shader** _string_
> 来自 ~/.config/slop 的自定义着色器

**-o, --noopengl**
> 禁用 OpenGL 加速

**-x, --xdisplay** _display_
> 指定要使用的 X display

**-v, --version**
> 显示版本

**-h, --help**
> 显示帮助

# DESCRIPTION

**slop**（Select Operation）让用户选择一个屏幕区域，并将几何信息输出到 stdout。用户可以点击并拖拽创建选择矩形，也可以直接选中现有窗口。输出格式可配置，便于与其他工具集成。

常见用途包括截图区域选择、窗口几何信息捕获以及与录屏工具集成。脚本可以解析其输出，对选定区域执行操作。

# CAVEATS

需要 X11；在没有 XWayland 的情况下无法在 Wayland 上工作。OpenGL 加速需要相应的驱动。自定义着色器必须放在 ~/.config/slop 目录中。除非使用 **-n** 标志，否则选区可能包含窗口装饰。

# HISTORY

**slop** 由 **naelstrof** 创建，是 **scrot** 中选区功能的继任者。该工具的设计目标是模块化，并通过 shell 管道与其他实用程序集成。它常与 **maim**（用于截图）及各种录屏工具搭配使用。

# INSTALL

```apt: sudo apt install slop```

```dnf: sudo dnf install slop```

```pacman: sudo pacman -S slop```

```apk: sudo apk add slop```

```zypper: sudo zypper install slop```

```nix: nix profile install nixpkgs#slop```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[maim](/man/maim)(1), [scrot](/man/scrot)(1), [xdotool](/man/xdotool)(1), [xwininfo](/man/xwininfo)(1)
