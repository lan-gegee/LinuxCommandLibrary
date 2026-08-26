# TAGLINE

用于捕获 X Window 屏幕截图的 ImageMagick 工具

# TLDR

**点击窗口捕获**（交互式十字准线选择器）

```import screenshot.png```

**捕获整个屏幕**

```import -window root screenshot.png```

**捕获特定窗口**

```import -window [window_id] screenshot.png```

**延迟捕获**

```import -pause [5] screenshot.png```

**捕获区域**

```import -crop [640x480+100+100] screenshot.png```

**设置图像格式**

```import screenshot.[jpg|png|gif]```

# SYNOPSIS

**import** [_options_] _output_file_

# PARAMETERS

**-window** _ID_
> 捕获特定的窗口 ID，"root" 表示全屏。

**-pause** _SECONDS_
> 捕获前的延迟时间。

**-crop** _GEOMETRY_
> 裁剪到指定的几何尺寸。

**-frame**
> 包含窗口框架。

**-border**
> 包含窗口边框。

**-screen**
> 从虚拟根窗口捕获。

**-silent**
> 不显示进度监视器。

**--help**
> 显示帮助信息。

# DESCRIPTION

**import** 是一款用于捕获 X Window 屏幕截图的 ImageMagick 工具。它可以捕获整个屏幕、特定窗口或用户选择的区域。

该工具支持由文件扩展名决定的各种输出格式。它与 ImageMagick 处理流水线集成，可立即进行处理操作。

# CAVEATS

仅支持 X11。需要安装 ImageMagick。默认行为是点击选择。

# HISTORY

import 是 **ImageMagick** 套件的一部分，由 **John Cristy** 于 1987 年创建，用于 X Window 屏幕捕获。

# INSTALL

```pacman: sudo pacman -S imagemagick```

```apk: sudo apk add imagemagick```

```brew: brew install imagemagick```

```nix: nix profile install nixpkgs#imagemagick```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[convert](/man/convert)(1), [display](/man/display)(1), [scrot](/man/scrot)(1)
