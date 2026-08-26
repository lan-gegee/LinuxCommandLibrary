# TAGLINE

ImageMagick 6 版本的 mogrify

# TLDR

**将所有 JPEG 图片原地缩放到 800x600 以内**

```mogrify.im6 -resize [800x600] [*.jpg]```

**把所有 JPEG 图片转换为 PNG 格式**

```mogrify.im6 -format [png] [*.jpg]```

**转换格式并将输出写入指定目录**

```mogrify.im6 -format [png] -path [output_dir] [*.jpg]```

**将所有图片顺时针旋转 90 度**

```mogrify.im6 -rotate [90] [*.jpg]```

**设置 JPEG 压缩质量（0-100）**

```mogrify.im6 -quality [80] [*.jpg]```

**去除图片的所有元数据和配置档案**

```mogrify.im6 -strip [*.jpg]```

**将图片裁剪到指定区域**

```mogrify.im6 -crop [640x480+50+50] [*.jpg]```

# SYNOPSIS

**mogrify.im6** [_options_] _files_

# PARAMETERS

_FILES_
> 要原地修改的图片文件。

**-resize** _GEOMETRY_
> 将图片缩放到指定尺寸以内（如 800x600、50%）。

**-format** _TYPE_
> 把图片转换为指定格式（如 png、gif、tiff）。输出文件与原文件放在一起，使用新扩展名。

**-path** _DIRECTORY_
> 将输出文件写到指定目录，而不是覆盖原文件。

**-rotate** _DEGREES_
> 将图片顺时针旋转指定的角度。

**-quality** _VALUE_
> 设置压缩质量（JPEG/PNG 为 0-100，数值越高质量越好）。

**-strip**
> 移除所有图片配置档案、注释和元数据。

**-crop** _GEOMETRY_
> 按指定几何参数（WxH+X+Y）裁剪图片。

**-blur** _RADIUS_x_SIGMA_
> 以给定的半径和 sigma 应用高斯模糊。

**-colorspace** _TYPE_
> 设置图像色彩空间（如 sRGB、Gray、CMYK）。

**-auto-orient**
> 根据 EXIF 方向标签旋转图片并移除该标签。

**-thumbnail** _GEOMETRY_
> 缩放并去除配置档案，为生成缩略图做了优化。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mogrify.im6** 是 ImageMagick 6 版本的 mogrify。它原地修改图片，不像 convert 那样写到另一个输出文件。它专为批量处理设计，可一次对多个文件应用同一组变换。

使用 **-format** 更改输出类型时会创建带相应扩展名的新文件。使用 **-path** 可将转换后的文件写到单独的目录，避免覆盖原文件。

# CAVEATS

默认覆盖原始文件，除非使用了 **-format** 或 **-path**。这是 ImageMagick 6 专有的变体；ImageMagick 7 请使用 **mogrify**。

# SEE ALSO

[mogrify](/man/mogrify)(1), [convert](/man/convert)(1), [identify](/man/identify)(1), [composite.im6](/man/composite.im6)(1), [identify.im6](/man/identify.im6)(1)
