# TAGLINE

兼容 Wlroots 的 Wayland 取色器，为 Hyprland 而设计

# TLDR

以十六进制格式**选取**颜色

```hyprpicker```

以**指定格式**选取颜色

```hyprpicker -f [hex|rgb|hsl|hsv|cmyk]```

选取颜色并**复制**到剪贴板

```hyprpicker -a```

**禁用**彩色输出（仅纯文本）

```hyprpicker -n```

将选到的颜色存入 **shell 变量**

```color=$(hyprpicker -f hex)```

# SYNOPSIS

**hyprpicker** [_options_]

# PARAMETERS

**-f**, **--format** _FORMAT_
> 输出格式：hex、rgb、hsl、hsv 或 cmyk

**-a**, **--autocopy**
> 自动将选中的颜色复制到剪贴板

**-n**, **--no-fancy**
> 禁用彩色输出，仅打印纯文本

**-r**, **--render-inactive**
> 渲染（冻结）非活动显示器

**-z**, **--no-zoom**
> 禁用缩放放大镜

**-q**, **--quiet**
> 禁用大部分日志输出

**-t**, **--no-fractional**
> 禁用分数缩放支持

**-h**, **--help**
> 显示帮助信息

# DESCRIPTION

**hyprpicker** 是一款兼容 wlroots 的 Wayland 取色器，专为 Hyprland 设计。它允许用户选择屏幕上的任意像素，并以多种格式获取其颜色值。

启动后，光标会变成一个放大镜。点击屏幕任意位置即可捕获该像素的颜色并以指定格式输出。该工具与 wl-copy 集成以提供剪贴板支持。

# CAVEATS

需要基于 wlroots 合成器的 Wayland 会话。要使用自动复制功能，必须安装 wl-copy。在 X11 或非 wlroots 的 Wayland 合成器下无法工作。

# HISTORY

hyprpicker 是 Hyprland 生态的一部分，由 Vaxry 与 Hyprland 合成器一同创建。Hyprland 自 **2022 年**起作为高度可定制的动态平铺 Wayland 合成器而广受欢迎。

# INSTALL

```pacman: sudo pacman -S hyprpicker```

```zypper: sudo zypper install hyprpicker```

```nix: nix profile install nixpkgs#hyprpicker```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hyprctl](/man/hyprctl)(1), [hyprshot](/man/hyprshot)(1), [wl-copy](/man/wl-copy)(1)
