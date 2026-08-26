# TAGLINE

面向 Wayland 和 X11 的动态菜单

# TLDR

**显示菜单**并输出选中的条目

```echo -e "option1\noption2\noption3" | bemenu```

**显示带提示语的菜单**

```echo -e "firefox\nchromium\nvivaldi" | bemenu -p "Browser:"```

**运行选中的命令**

```echo -e "firefox\nchromium" | bemenu | xargs -r swaymsg exec --```

**用作程序启动器**（配合 dmenu_path）

```dmenu_path | bemenu | sh```

**自定义外观**

```bemenu --fn "monospace 12" --tb "#285577" --tf "#ffffff"```

**列出已安装的应用程序**

```compgen -c | sort -u | bemenu```

**密码输入提示**（隐藏输入内容）

```bemenu --password -p "Password:"```

# SYNOPSIS

**bemenu** [_options_]

**bemenu-run** [_options_]

# DESCRIPTION

**bemenu** 是一个受 dmenu 启发的动态菜单库和客户端程序。它从 stdin 读取条目并以菜单形式呈现，再将选中的条目输出到 stdout。它支持多种后端，包括 Wayland、X11 和 curses。

与只能工作在 X11 上的 dmenu 不同，bemenu 提供原生的 Wayland 支持，因此非常适合 Sway 及其他 Wayland 合成器。渲染由各后端库处理，使同一界面可以跨不同显示服务器使用。

**bemenu-run** 是一个包装器，它会列出 PATH 中的可执行文件并运行选中的那个，可当作简单的应用启动器。

# PARAMETERS

**-p**, **--prompt** _text_
> 设置提示语文本。

**-i**
> 不区分大小写匹配。

**-l**, **--list** _lines_
> 以垂直列表显示条目。

**-b**, **--bottom**
> 显示在屏幕底部。

**-m**, **--monitor** _index_
> 显示在指定显示器上。

**-H**, **--line-height** _height_
> 设置条目高度（像素）。

**--password**
> 隐藏输入内容（密码模式）。

**-w**, **--wrap**
> 光标选择循环换行。

**-f**, **--filter** _text_
> 按给定文本过滤条目。

**--fn** _font_
> 设置字体（Pango 格式，如 "monospace 12"）。

**--tb** _color_
> 标题栏背景色。

**--tf** _color_
> 标题栏前景色。

**--fb** _color_
> 过滤区域背景色。

**--ff** _color_
> 过滤区域前景色。

**--nb** _color_
> 普通条目背景色。

**--nf** _color_
> 普通条目前景色。

**--hb** _color_
> 高亮条目背景色。

**--hf** _color_
> 高亮条目前景色。

# CAVEATS

需要与显示服务器对应的适当后端库（wayland、x11 或 curses）。颜色采用 #RRGGBB 格式。字体规格遵循 Pango 格式。在 Wayland 上，bemenu 需要合成器支持 layer-shell 协议。

# HISTORY

**bemenu** 的创建目的是成为能在 Wayland 合成器上运行的 **dmenu** 跨平台替代品。它作为把传统 X11 工具带入 Wayland 生态的努力的一部分而开发。该项目提供可供其他应用集成的库绑定，采用了比最初的 dmenu 更模块化的设计。

# INSTALL

```apt: sudo apt install bemenu```

```dnf: sudo dnf install bemenu```

```pacman: sudo pacman -S bemenu```

```apk: sudo apk add bemenu```

```zypper: sudo zypper install bemenu```

```nix: nix profile install nixpkgs#bemenu```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[dmenu](/man/dmenu)(1), [rofi](/man/rofi)(1), [fzf](/man/fzf)(1), [wofi](/man/wofi)(1)
