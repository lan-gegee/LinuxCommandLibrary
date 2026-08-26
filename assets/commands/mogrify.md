# TAGLINE

原地修改图片

# TLDR

**原地缩放图片**

```mogrify -resize [800x600] [*.jpg]```

**转换格式**

```mogrify -format [png] [*.jpg]```

**旋转图片**

```mogrify -rotate [90] [*.jpg]```

**添加水印**

```mogrify -draw "text 10,10 'Copyright'" [*.jpg]```

**压缩质量**

```mogrify -quality [80] [*.jpg]```

**去除元数据**

```mogrify -strip [*.jpg]```

# SYNOPSIS

**mogrify** [_options_] _files_

# PARAMETERS

_FILES_
> 要修改的图片文件。

**-resize** _GEOM_
> 缩放的几何参数。

**-format** _FMT_
> 输出格式。

**-rotate** _DEG_
> 旋转角度。

**-quality** _NUM_
> 压缩质量。

**-strip**
> 移除元数据（EXIF、色彩配置档案）。

**-crop** _GEOM_
> 将图片裁剪到给定区域（例如 `100x100+10+10`）。

**-thumbnail** _GEOM_
> 更快的缩放，同时去除元数据。

**-flip** / **-flop**
> 垂直 / 水平镜像。

**-trim**
> 裁掉均匀的边缘（例如空白边框）。

**-path** _DIR_
> 将输出文件写到 DIR 而不是覆盖原文件。

**-auto-orient**
> 按 EXIF 方向旋转，使图片正确显示。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mogrify** 原地修改图片。它是 ImageMagick 的批量处理工具。

该工具一次变换多张图片。与 convert 不同，它会覆盖原始文件。

# CAVEATS

会覆盖原始文件。属于 ImageMagick。使用前请先备份。

# HISTORY

mogrify 是 **ImageMagick** 的一部分，自 1990 年起就提供原地图像变换能力。

# INSTALL

```pacman: sudo pacman -S imagemagick```

```apk: sudo apk add imagemagick```

```brew: brew install imagemagick```

```nix: nix profile install nixpkgs#imagemagick```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[convert](/man/convert)(1), [identify](/man/identify)(1), [magick](/man/magick)(1)
