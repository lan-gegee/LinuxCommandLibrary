# TAGLINE

在各种图像格式之间转换并应用变换处理

# TLDR

**转换图像格式**

```magick convert [input.png] [output.jpg]```

**调整图像大小**

```magick convert [input.png] -resize [800x600] [output.png]```

**更改质量**

```magick convert [input.png] -quality [85] [output.jpg]```

**转换为灰度图**

```magick convert [input.png] -colorspace Gray [output.png]```

**旋转图像**

```magick convert [input.png] -rotate [90] [output.png]```

**添加边框**

```magick convert [input.png] -border [10x10] -bordercolor black [output.png]```

# SYNOPSIS

**magick** **convert** [_options_] _input_ _output_

# PARAMETERS

**-resize** _geometry_
> 调整图像大小。

**-quality** _value_
> JPEG/PNG 质量（1-100）。

**-colorspace** _type_
> 转换色彩空间。

**-rotate** _degrees_
> 旋转图像。

**-crop** _geometry_
> 裁剪图像。

**-border** _geometry_
> 添加边框。

**-flip**
> 垂直翻转。

**-flop**
> 水平翻转。

**-strip**
> 移除元数据（EXIF、配置档案）。

**-density** _DPI_
> 设置图像分辨率。

**-gravity** _type_
> 设置放置基准方位（Center、NorthWest 等）。

**-compose** _operator_
> 设置图像合成操作符。

**-extent** _geometry_
> 设置图像尺寸，必要时用背景色填充。

**-background** _color_
> 设置背景色。

**-alpha** _type_
> 启用、禁用或重置 alpha 通道（on、off、remove、set）。

**-auto-orient**
> 根据 EXIF 方向信息自动旋转图像。

# DESCRIPTION

**magick convert** 在各种图像格式之间转换并应用变换处理，是 **ImageMagick** 套件的一部分。它支持数百种格式，包括 PNG、JPEG、GIF、TIFF、PDF、SVG 和 WebP。

多个操作可以在同一行命令中串联，按顺序应用多种变换。该工具读取输入图像，按顺序应用所有指定的操作，然后将结果写入输出文件。输出格式由文件扩展名决定。

# CAVEATS

在 ImageMagick 7 中，独立的 `convert` 命令已被弃用，建议改用 `magick convert` 或直接使用 `magick`。新工作请直接使用 `magick`。大图的内存占用可能很高。PDF 操作需要 Ghostscript。`-limit` 选项可以限制内存、磁盘等资源用量。

# HISTORY

**ImageMagick** 由 **John Cristy** 于 **1987 年**在杜邦公司创建。convert 命令在其整个发展历程中一直是主要的图像转换工具。

# INSTALL

```pacman: sudo pacman -S imagemagick```

```apk: sudo apk add imagemagick```

```brew: brew install imagemagick```

```nix: nix profile install nixpkgs#imagemagick```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[magick](/man/magick)(1), [magick-mogrify](/man/magick-mogrify)(1)
