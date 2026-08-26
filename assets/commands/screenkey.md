# TAGLINE

在屏幕上显示按键，用于屏幕录制

# TLDR

在屏幕上显示**按键**

```screenkey```

显示按键和**鼠标**按钮

```screenkey -M```

打开**设置**菜单

```screenkey --show-settings```

设置显示**位置**

```screenkey -p bottom```

设置**修饰键**显示格式

```screenkey --mods-mode emacs```

自定义**外观**

```screenkey --bg-color "#000000" -f "Monospace" --font-color yellow --opacity 0.8```

以**固定**位置和几何尺寸显示

```screenkey -p fixed -g 400x100+100+100```

# SYNOPSIS

**screenkey** [_options_]

# DESCRIPTION

**screenkey** 是一款录屏工具，它将按下的按键以叠加层形式显示在屏幕上，让观众在屏幕录制、教程和现场演示期间能够看到键盘输入。它捕获整个系统的所有按键，并在一个可自定义的浮动窗口中进行渲染。

显示支持多种修饰键格式（Emacs、Mac、Windows 风格）、可配置的位置、自定义字体和颜色以及可调节的不透明度。鼠标按钮点击也可以与键盘输入一同显示。叠加层窗口可以放置在固定的屏幕位置，或使用自定义几何尺寸。

通过 **--show-settings** 可以打开设置图形界面进行交互式配置。该工具集成于 X11 并作为后台进程运行，实时显示按键，并在可配置的超时后将其淡出。

# PARAMETERS

**-M, --mouse**
> 显示鼠标按钮点击

**--show-settings**
> 启动设置菜单

**-p, --position POSITION**
> 设置显示位置（top、center、bottom、fixed）

**-g, --geometry GEOMETRY**
> 设置窗口几何尺寸（用于固定位置）

**--mods-mode MODE**
> 设置修饰键显示格式（normal、emacs、mac、win、tux）

**--bg-color COLOR**
> 设置背景颜色（十六进制格式）

**-f, --font FONT**
> 设置显示字体

**--font-color COLOR**
> 设置字体颜色

**--opacity VALUE**
> 设置窗口不透明度（0.0 到 1.0）

**-t, --timeout SECONDS**
> 每个按键的显示时长

**--key-mode MODE**
> 设置按键显示模式（composed、translated、raw、keysyms）

**--no-systray**
> 不显示系统托盘图标

**-d, --debug**
> 启用调试输出

# CAVEATS

需要 X11；在没有 XWayland 的 Wayland 环境下可能无法正常工作。该工具会捕获整个系统的所有按键，可能存在安全隐患。可以配合 slop 自定义选择窗口几何区域。

# HISTORY

**screenkey** 为录屏和教学目的而创建，让演示者能够直观地向观众展示键盘输入。

# INSTALL

```dnf: sudo dnf install screenkey```

```pacman: sudo pacman -S screenkey```

```zypper: sudo zypper install screenkey```

```nix: nix profile install nixpkgs#screenkey```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[slop](/man/slop)(1), [xdotool](/man/xdotool)(1)
