# TAGLINE

在 X11 窗口中显示 GIF 图片和动画

# TLDR

**查看 GIF**

```gifview [image.gif]```

**以动画方式查看**

```gifview -a [image.gif]```

**指定最小帧延迟**（单位为百分之一秒）

```gifview --min-delay [10] [image.gif]```

**以未优化帧查看**以获得忠实的显示效果

```gifview -U [image.gif]```

**禁用交互控制**

```gifview +e [image.gif]```

# SYNOPSIS

**gifview** [_options_] _files_

# PARAMETERS

_FILES_
> 要显示的 GIF 文件。

**-a**, **--animate**
> 播放多图像 GIF 动画（大多数构建版本中的默认行为）。

**+a**, **--no-animate**
> 以幻灯片形式显示各帧，而不是播放动画。

**-U**, **--unoptimize**
> 将多图像 GIF 按未优化状态显示，以忠实呈现每一帧。

**--min-delay** _DELAY_
> 帧之间的最小延迟，单位为百分之一秒（默认：0）。

**--fallback-delay** _DELAY_
> 未指定延迟的帧所使用的延迟，单位为百分之一秒。

**+e**, **--no-interactive**
> 忽略鼠标和键盘输入。

**-w** _WINDOW_, **--window** _WINDOW_
> 在已有的 X 窗口（ID 或 'root'）中显示。

**--new-window** _WINDOW_
> 在已有 X 窗口的新子窗口中显示。

**--geometry** _GEOMETRY_
> 设置窗口大小和位置。

**--title** _TITLE_
> 设置窗口标题。

**--bg** _COLOR_, **--background** _COLOR_
> 透明像素使用的背景颜色。

**-i**, **--install-colormap**
> 为每个窗口使用私有调色板。

**--memory-limit** _LIM_
> 最多缓存 LIM 兆字节的图像（默认：40）。

**-d** _DISPLAY_, **--display** _DISPLAY_
> 使用指定的 X 显示服务器。

**--name** _NAME_
> 设置用于资源查找的应用程序名称。

**--version**
> 打印版本号并退出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gifview** 在 X11 窗口中显示 GIF 图片和动画。它是 gifsicle 软件包的一部分，提供简单的 GIF 查看功能，支持动画播放和可配置的播放速度。

该查看器可以显示特定帧以供检查，并支持基本的窗口管理选项。它能按照正确的帧时序处理动画 GIF。

# CAVEATS

需要 X11 显示。属于 gifsicle 软件包的一部分。仅支持 GIF 格式。

# HISTORY

gifview 是由 **Eddie Kohler** 创建的 GIF 处理工具集 **gifsicle** 的组成部分。

# INSTALL

```apt: sudo apt install gifsicle```

```dnf: sudo dnf install gifsicle```

```pacman: sudo pacman -S gifsicle```

```apk: sudo apk add gifsicle```

```zypper: sudo zypper install gifsicle```

```brew: brew install gifsicle```

```nix: nix profile install nixpkgs#gifsicle```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gifsicle](/man/gifsicle)(1), [feh](/man/feh)(1), [display](/man/display)(1)
