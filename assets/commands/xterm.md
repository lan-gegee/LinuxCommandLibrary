# TAGLINE

标准 X11 终端模拟器

# TLDR

以指定**标题**打开终端

```xterm -T [Example]```

以**全屏**模式打开终端

```xterm -fullscreen```

使用**自定义颜色**打开（深蓝背景、黄色文字）

```xterm -bg darkblue -fg yellow```

以指定**几何尺寸**打开（100x35 字符，位于位置 200,20）

```xterm -geometry 100x35+200+20```

使用**特定字体**和字号打开

```xterm -fa '[Serif]' -fs 20```

# SYNOPSIS

**xterm** [**-toolkitoption** ...] [**-option** ...] [_shell_]

# PARAMETERS

**-T** _string_
> 设置窗口标题

**-geometry** _WxH+X+Y_
> 设置窗口大小和位置

**-bg** _color_
> 背景色

**-fg** _color_
> 前景（文字）色

**-fa** _font_
> TrueType 字体名

**-fs** _size_
> TrueType 字号（磅）

**-fn** _font_
> 位图字体名

**-fullscreen**
> 以全屏模式启动

**-rv**
> 反显（交换前景/背景色）

**-sb**
> 启用滚动条

**-sl** _lines_
> 回滚缓冲区保存的行数

**-e** _program_ [_args_]
> 运行指定程序而不是 shell

**-hold**
> 命令退出后保持窗口打开

**-class** _class_
> X 资源类名

# DESCRIPTION

**xterm** 是 X Window System 的标准终端模拟器，在图形环境中提供文本终端界面。它支持 VT102、VT220 和 Tektronix 4014 终端仿真，并提供丰富的自定义选项。

功能包括多种字体、可配置的颜色、回滚缓冲区、选择与粘贴、Tektronix 图形模式以及完整的国际化支持。可以通过命令行、X 资源或控制菜单（Ctrl+点击）进行配置。

# CAVEATS

需要 X11 显示。默认外观刻意保持极简；通过 ~/.Xresources 进行深度定制很常见。某些现代特性（如 256 色）需要特定的资源设置。位图字体和 TrueType 字体的配置方式不同。

# HISTORY

最初由 Mark Vandevoorde 于 20 世纪 80 年代中期在 MIT 作为 **Project Athena** 的一部分编写，后来成为 X Window System 发行版的一部分。它是持续维护时间最长的 X 应用程序之一。Thomas Dickey 自 **1996 年**起一直是主要维护者。

# INSTALL

```apt: sudo apt install xterm```

```dnf: sudo dnf install xterm```

```pacman: sudo pacman -S xterm```

```apk: sudo apk add xterm```

```zypper: sudo zypper install xterm```

```brew: brew install xterm```

```nix: nix profile install nixpkgs#xterm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[uxterm](/man/uxterm)(1), [konsole](/man/konsole)(1), [gnome-terminal](/man/gnome-terminal)(1)
