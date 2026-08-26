# TAGLINE

就地修改图像

# TLDR

**就地调整图像大小**

```magick mogrify -resize [800x600] [*.jpg]```

**就地转换格式**

```magick mogrify -format png [*.jpg]```

**更改所有 JPEG 的质量**

```magick mogrify -quality [85] [*.jpg]```

**旋转图像**

```magick mogrify -rotate [90] [*.png]```

**移除元数据**

```magick mogrify -strip [*.jpg]```

# SYNOPSIS

**magick** **mogrify** [_options_] _image_...

# PARAMETERS

**-resize** _geometry_
> 调整图像大小。

**-format** _format_
> 转换为指定格式。

**-quality** _value_
> 设置输出质量。

**-rotate** _degrees_
> 旋转图像。

**-strip**
> 移除元数据。

**-path** _dir_
> 输出目录。

# DESCRIPTION

**magick mogrify** 就地修改图像。它是 ImageMagick 的一部分。与 convert 不同，mogrify 直接对文件本身操作。可使用 -path 保存到其他目录。适合高效的批处理。

# CAVEATS

默认直接修改原文件。如需保留原始文件，请使用 -path。

# INSTALL

```pacman: sudo pacman -S imagemagick```

```apk: sudo apk add imagemagick```

```brew: brew install imagemagick```

```nix: nix profile install nixpkgs#imagemagick```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[magick](/man/magick)(1), [magick-convert](/man/magick-convert)(1)
