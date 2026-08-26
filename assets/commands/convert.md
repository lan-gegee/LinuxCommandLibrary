# TAGLINE

图像处理与格式转换

# TLDR

**转换**图像格式

```convert [input.png] [output.jpg]```

**调整**图像大小

```convert [input.jpg] -resize [800x600] [output.jpg]```

**旋转**图像

```convert [input.jpg] -rotate [90] [output.jpg]```

**添加**边框

```convert [input.jpg] -border [10x10] -bordercolor [black] [output.jpg]```

**压缩**图像

```convert [input.jpg] -quality [85] [output.jpg]```

# SYNOPSIS

**convert** [_options_] _input_ _output_

# DESCRIPTION

**convert** 是 ImageMagick 的主要命令行界面，ImageMagick 是现有最多功能的图像处理工具之一。它支持超过 200 种图像格式，几乎可以执行任何图像变换，包括格式转换、缩放、旋转、裁剪、颜色处理以及应用艺术效果。

该工具的工作方式是读取一张或多张输入图像，应用命令行选项指定的一系列变换，然后将结果写入输出文件。多个操作可以在单条命令中串联，并按指定顺序依次执行。

convert 在 Web 开发中广泛用于生成缩略图，在摄影工作流中用于批量处理，在科学计算中用于图像分析。它的可脚本化特性使之非常适合自动化，不过复杂的操作可能消耗大量内存和 CPU 时间。在 ImageMagick 7 及以上版本中，该命令正被统一的 **magick** 命令取代，但 convert 仍为兼容性而保留。

# PARAMETERS

**-resize** _geometry_
> 调整图像大小（如 50%、800x600、800x）

**-rotate** _degrees_
> 旋转图像

**-crop** _geometry_
> 裁剪图像

**-quality** _value_
> 压缩质量（1-100）

**-scale** _geometry_
> 缩放图像（更快，但质量较低）

**-thumbnail** _geometry_
> 创建缩略图

**-blur** _radius_
> 模糊图像

**-sharpen** _radius_
> 锐化图像

**-negate**
> 反转颜色

**-monochrome**
> 转换为黑白

**-flip**
> 垂直翻转

**-flop**
> 水平翻转

# GEOMETRY SPECIFICATIONS

- **800x600** - 最大尺寸（保持纵横比）
- **800x600!** - 精确尺寸（忽略纵横比）
- **800x600^** - 最小尺寸（裁剪）
- **50%** - 按百分比缩放
- **800x** - 宽度（自动计算高度）
- **x600** - 高度（自动计算宽度）

# WORKFLOW

```bash
# Convert format
convert photo.png photo.jpg

# Resize maintaining aspect ratio
convert input.jpg -resize 800x600 output.jpg

# Exact size (may distort)
convert input.jpg -resize 800x600! output.jpg

# Resize by percentage
convert input.jpg -resize 50% output.jpg

# Thumbnail
convert input.jpg -thumbnail 200x200 thumb.jpg

# Rotate
convert input.jpg -rotate 90 output.jpg

# Crop (width x height + x_offset + y_offset)
convert input.jpg -crop 800x600+100+100 output.jpg

# Quality compression
convert input.jpg -quality 85 output.jpg

# Multiple operations
convert input.jpg -resize 800x600 -rotate 90 -quality 90 output.jpg
```

# BATCH OPERATIONS

```bash
# Convert all PNG to JPG
for img in *.png; do
    convert "$img" "${img%.png}.jpg"
done

# Resize all images
for img in *.jpg; do
    convert "$img" -resize 800x600 "resized_$img"
done
```

# EFFECTS

```bash
# Blur
convert input.jpg -blur 0x8 output.jpg

# Sharpen
convert input.jpg -sharpen 0x1 output.jpg

# Border
convert input.jpg -border 5x5 -bordercolor black output.jpg

# Add text
convert input.jpg -pointsize 36 -fill white \
    -annotate +50+50 'Hello' output.jpg
```

# CAVEATS

大图会消耗内存。复杂操作可能较慢。默认质量设置可能显著减小文件体积。某些操作会改变纵横比。旧版本存在安全漏洞。建议考虑使用 `magick` 命令（ImageMagick 7+）。

# HISTORY

**convert** 是 ImageMagick 的一部分，由 John Cristy 于 **1987** 年创建，如今已成为最多功能的图像处理工具之一。

# INSTALL

```pacman: sudo pacman -S imagemagick```

```apk: sudo apk add imagemagick```

```brew: brew install imagemagick```

```nix: nix profile install nixpkgs#imagemagick```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mogrify](/man/mogrify)(1), [identify](/man/identify)(1), [ffmpeg](/man/ffmpeg)(1)

# RESOURCES

```[Source code](https://github.com/ImageMagick/ImageMagick)```

```[Homepage](https://imagemagick.org)```

```[Documentation](https://imagemagick.org/script/convert.php)```

<!-- verified: 2026-06-23 -->
