# TAGLINE

图像处理工具套件

# TLDR

**转换图片格式**（v7 语法）

```magick [input.png] [output.jpg]```

**调整图片尺寸**

```magick [input.jpg] -resize [800x600] [output.jpg]```

**创建缩略图**

```magick [input.jpg] -thumbnail [150x150^] -gravity center -extent [150x150] [thumb.jpg]```

**添加文字水印**

```magick [input.jpg] -gravity south -annotate +0+10 "[Copyright]" [output.jpg]```

**水平拼接图片**

```magick [a.jpg] [b.jpg] +append [combined.jpg]```

**从多张图片创建 GIF**

```magick -delay [100] [*.png] [animation.gif]```

**查看图片信息**

```magick identify [image.jpg]```

在当前目录中**批量将所有 PNG 转换为 JPEG**

```magick mogrify -format jpg [*.png]```

# SYNOPSIS

**magick** [_input_] [_operations_] _output_

**magick identify** [_options_] _image_

**magick mogrify** [_options_] _images_

# PARAMETERS

**-resize** _geometry_
> 调整图片尺寸。

**-crop** _geometry_
> 裁剪图片。

**-rotate** _degrees_
> 旋转图片。

**-quality** _value_
> 压缩质量（JPEG：1-100；PNG：0-9，对应 zlib 压缩级别）。

**-gravity** _type_
> 操作的锚点位置。

**-annotate** _geometry_ _text_
> 添加文字标注。

**-blur** _radius_
> 应用模糊效果。

**-sharpen** _radius_
> 锐化图片。

**-colorspace** _type_
> 转换色彩空间。

**-density** _value_
> 设置分辨率（DPI）。

**-strip**
> 移除图片中的所有元数据和配置文件（profiles）。

**-format** _type_
> 设置输出图片格式。

# DESCRIPTION

**ImageMagick** 是一套图像处理工具。它能对超过 200 种格式的图片进行转换、调整尺寸、裁剪、旋转、拼接以及添加特效等操作。

主要工具：**magick**（转换处理，在 v7 中取代 convert）、**identify**（信息查询）、**mogrify**（就地编辑）、**composite**（合成）、**montage**（拼贴）。在 v7 中，所有子命令都通过 `magick` 调用（如 `magick identify`、`magick mogrify`）。

# CAVEATS

大图片会占用大量内存。默认安全策略（policy.xml）可能限制某些操作和文件格式。在 v7 中，`convert` 命令已弃用，推荐使用 `magick`；旧的 v6 语法仍可用但会发出警告。

# HISTORY

ImageMagick 由 **John Cristy** 于 **1987 年**在杜邦公司创建。它持续开发至今，仍是使用最广泛的命令行图像处理工具集。

# INSTALL

```pacman: sudo pacman -S imagemagick```

```brew: brew install imagemagick```

```nix: nix profile install nixpkgs#imagemagick```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[magick](/man/magick)(1), [convert](/man/convert)(1), [identify](/man/identify)(1), [mogrify](/man/mogrify)(1), [composite](/man/composite)(1), [montage](/man/montage)(1), [ffmpeg](/man/ffmpeg)(1)
