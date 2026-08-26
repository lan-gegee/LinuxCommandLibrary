# TAGLINE

ImageMagick 6 版本的 import 屏幕截图工具

# TLDR

**捕获整个屏幕**

```import.im6 screenshot.png```

**点击窗口进行捕获**

```import.im6 window.png```

**捕获根窗口**

```import.im6 -window root screen.png```

**带延迟捕获**

```import.im6 -pause [3] screenshot.png```

# SYNOPSIS

**import.im6** [_options_] _output_file_

# PARAMETERS

**-window** _ID_
> 捕获特定窗口或 "root"。

**-pause** _SECONDS_
> 捕获前的延迟时间。

**-frame**
> 包含窗口框架。

**-crop** _GEOMETRY_
> 裁剪捕获的图像。

**--help**
> 显示帮助信息。

# DESCRIPTION

**import.im6** 是 ImageMagick 6 版本的 import 屏幕截图工具。它将 X Window 屏幕截图保存为各种图像格式。

保留这一旧版本是为了兼容依赖 ImageMagick 6 行为的脚本。

# CAVEATS

旧版 ImageMagick 6 版本。仅支持 X11。较新的系统请使用 import。

# HISTORY

import.im6 是 **ImageMagick 6** 中 import 的带版本后缀名称，以便与 ImageMagick 7 共存。

# SEE ALSO

[import](/man/import)(1), [display.im6](/man/display.im6)(1)
