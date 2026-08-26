# TAGLINE

将多张图像按网格排布生成合成图像

# TLDR

**创建图像拼贴**

```magick montage [*.jpg] [output.png]```

**设置网格布局**

```magick montage -tile [3x3] [*.jpg] [output.png]```

**设置缩略图尺寸**

```magick montage -geometry [200x200+5+5] [*.jpg] [output.png]```

**添加标签**

```magick montage -label '%f' [*.jpg] [output.png]```

**设置背景颜色**

```magick montage -background white [*.jpg] [output.png]```

**创建带标题和阴影的拼贴**

```magick montage -title "[My Gallery]" -shadow [*.jpg] [output.png]```

# SYNOPSIS

**magick** **montage** [_options_] _images_... _output_

# PARAMETERS

**-tile** _geometry_
> 网格布局（列数 x 行数）。

**-geometry** _geometry_
> 缩略图尺寸与间距。

**-label** _string_
> 为缩略图添加标签。

**-background** _color_
> 背景颜色。

**-border** _geometry_
> 缩略图周围的边框。

**-frame** _geometry_
> 缩略图周围的画框。

**-shadow**
> 为每张缩略图下方添加柔和阴影。

**-title** _string_
> 拼贴图像的标题。

**-font** _name_
> 标签和标题使用的字体。

**-pointsize** _value_
> 标签和标题的字号。

**-mode** _type_
> 边框风格：Frame、Unframe 或 Concatenate。

# DESCRIPTION

**magick montage** 将多张图像按网格排布生成合成图像。它是 ImageMagick 的一部分，适用于制作联系表、图库和图片预览。支持标签和边框。

# INSTALL

```pacman: sudo pacman -S imagemagick```

```apk: sudo apk add imagemagick```

```brew: brew install imagemagick```

```nix: nix profile install nixpkgs#imagemagick```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[magick](/man/magick)(1), [magick-convert](/man/magick-convert)(1)
