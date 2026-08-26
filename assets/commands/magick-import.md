# TAGLINE

从 X11 显示器捕获屏幕截图

# TLDR

**捕获屏幕截图**

```magick import [screenshot.png]```

**捕获指定窗口**

```magick import -window [window-id] [output.png]```

**捕获根窗口**

```magick import -window root [desktop.png]```

**延迟后捕获**

```magick import -pause [5] [screenshot.png]```

**以指定质量捕获**

```magick import -quality [90] [screenshot.jpg]```

# SYNOPSIS

**magick** **import** [_options_] _output_

# PARAMETERS

**-window** _id_
> 按 ID 或名称捕获指定窗口（使用 "root" 表示整个屏幕）。

**-pause** _seconds_
> 捕获前的延迟秒数。

**-crop** _geometry_
> 将捕获的图像裁剪为指定的尺寸和偏移。

**-frame**
> 捕获时包含窗口管理器的边框。

**-screen**
> 捕获整个屏幕而非单个窗口。

**-border**
> 在输出图像中包含窗口边框。

**-descend**
> 通过向下遍历窗口层级来获取图像。

**-snaps** _value_
> 要拍摄的屏幕快照数量。

**-quality** _value_
> 设置输出压缩质量（例如 JPEG 质量 1-100）。

**-silent**
> 静默操作，不播放提示音。

**-resize** _geometry_
> 调整捕获图像的大小。

# DESCRIPTION

**magick import** 从 X11 显示器捕获屏幕截图。它是 ImageMagick 的一部分，可以捕获整个屏幕、特定窗口或选定的区域，并输出为任何受支持的图像格式。

# INSTALL

```pacman: sudo pacman -S imagemagick```

```apk: sudo apk add imagemagick```

```brew: brew install imagemagick```

```nix: nix profile install nixpkgs#imagemagick```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[magick](/man/magick)(1), [scrot](/man/scrot)(1)
