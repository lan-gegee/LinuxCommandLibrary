# TAGLINE

ImageMagick 第 6 版图像查看器

# TLDR

**显示一张图片**（ImageMagick 6）

```display.im6 [image.jpg]```

**带标题显示**

```display.im6 -title "[Title]" [image.jpg]```

**调整大小后显示**

```display.im6 -resize [50%] [image.jpg]```

**显示多张图片**

```display.im6 [image1.jpg] [image2.jpg]```

# SYNOPSIS

**display.im6** [_options_] _file_...

# PARAMETERS

_FILE_
> 要显示的图像文件。

**-resize** _GEOMETRY_
> 调整图像大小。

**-title** _STRING_
> 设置窗口标题。

**-geometry** _GEOMETRY_
> 窗口几何尺寸。

**-delay** _TICKS_
> 幻灯片中图像之间的延迟，单位为百分之一秒。

**-density** _GEOMETRY_
> 设置图像渲染分辨率（DPI）。

**-rotate** _DEGREES_
> 将图像旋转指定角度。

**-help**
> 显示帮助信息。

# DESCRIPTION

**display.im6** 是 ImageMagick 第 6 版的图像查看器，用于在系统同时安装 ImageMagick 6 和 7 时保持兼容。它的功能与 display 命令完全相同，但明确使用第 6 版的库。

这种带版本号的命令允许脚本和用户在两个版本都可用时指定使用哪个 ImageMagick 版本，确保行为不受系统默认设置影响而保持一致。

标准 display 命令的所有功能均可用，包括交互式查看、图像处理、格式转换和幻灯片放映。

# CAVEATS

需要已安装 ImageMagick 6。行为可能与 ImageMagick 7 版本不同。主要作为过渡期的兼容手段存在。

# HISTORY

.im6 后缀是在 **ImageMagick 7** 引入与第 6 版不兼容的变更时添加的。这种命名约定让两个版本得以共存，im6 明确调用旧版本。

# SEE ALSO

[display](/man/display)(1), [identify.im6](/man/identify.im6)(1)
