# TAGLINE

ImageMagick 7+ 的主命令，取代 convert、mogrify 和 identify

# TLDR

**转换图像格式**

```magick [input.png] [output.jpg]```

**调整图像大小**

```magick [input.jpg] -resize [800x600] [output.jpg]```

**创建缩略图**

```magick [input.jpg] -thumbnail [100x100] [thumb.jpg]```

**旋转图像**

```magick [input.jpg] -rotate [90] [output.jpg]```

**添加文字水印**

```magick [input.jpg] -gravity south -annotate +0+10 "[text]" [output.jpg]```

**批量转换**

```magick mogrify -format jpg [*.png]```

**创建拼贴**

```magick montage [*.jpg] -geometry +2+2 [montage.jpg]```

# SYNOPSIS

**magick** [_options_] _input_ [_operations_] _output_

# DESCRIPTION

**magick** 是 ImageMagick 7+ 的主命令，取代了 convert、mogrify 和 identify。它执行图像处理操作，包括格式转换、调整大小和图像合成。

该工具支持超过 200 种图像格式，并提供丰富的变换能力。

# PARAMETERS

**-resize** _geometry_
> 调整图像大小。

**-crop** _geometry_
> 裁剪图像。

**-rotate** _degrees_
> 旋转图像。

**-flip**
> 垂直翻转。

**-flop**
> 水平翻转。

**-quality** _n_
> JPEG/PNG 质量。

**-strip**
> 移除元数据。

**-colorspace** _space_
> 转换色彩空间。

**-density** _dpi_
> 设置分辨率。

**-gravity** _type_
> 定位基准方位。

**-annotate** _+x+y_ _text_
> 添加文字。

**-composite**
> 合成图像。

**-blur** _radius_x_sigma_
> 模糊图像。

**-sharpen** _radius_x_sigma_
> 锐化图像。

**-auto-orient**
> 根据 EXIF 数据调整方向。

**-format** _type_
> 设置输出格式（配合 mogrify 使用）。

# CAVEATS

复杂操作需要加引号。大图会占用大量内存。某些格式存在限制。PDF 支持可能需要 Ghostscript。

# HISTORY

**ImageMagick** 由 **John Cristy** 于 **1987 年**创建。magick 命令在 ImageMagick 7（2016 年）中引入，用于将各种实用工具命令统一到单一接口之下。

# INSTALL

```pacman: sudo pacman -S imagemagick```

```apk: sudo apk add imagemagick```

```brew: brew install imagemagick```

```nix: nix profile install nixpkgs#imagemagick```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[convert](/man/convert)(1), [identify](/man/identify)(1), [mogrify](/man/mogrify)(1), [montage](/man/montage)(1)
