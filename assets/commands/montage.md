# TAGLINE

通过拼接多张图片创建合成图像

# TLDR

**创建图片网格**

```montage [*.jpg] [output.jpg]```

**指定平铺布局**

```montage [*.jpg] -tile [3x2] [output.jpg]```

**设置缩略图尺寸**

```montage [*.jpg] -geometry [200x200+5+5] [output.jpg]```

**添加标签**

```montage [*.jpg] -label "%f" [output.jpg]```

**设置背景颜色**

```montage [*.jpg] -background [white] [output.jpg]```

**添加边框**

```montage [*.jpg] -border [5] -bordercolor [gray] [output.jpg]```

# SYNOPSIS

**montage** [_options_] _input-files_ _output-file_

# DESCRIPTION

**montage** 通过拼接多张图片创建合成图像。它是 ImageMagick 的一部分，可将图片排成网格，并可选地附加标签、边框和阴影。

该工具适合制作索引图（contact sheet）、缩略图画廊和图片拼贴。

# PARAMETERS

**-tile** _cols_x_rows_
> 网格布局。

**-geometry** _WxH+x+y_
> 缩略图尺寸和间距。

**-label** _string_
> 每张图片的标签。

**-title** _string_
> 拼贴图的标题。

**-background** _color_
> 背景颜色。

**-border** _geometry_
> 边框尺寸。

**-bordercolor** _color_
> 边框颜色。

**-shadow**
> 添加阴影。

**-frame** _geometry_
> 添加相框。

**-mode** _type_
> 相框样式。

# CAVEATS

大量图片可能占用很多内存。标签格式化有特殊语法。输出格式由扩展名决定。质量设置会影响文件大小。

# HISTORY

**montage** 是 **ImageMagick** 的一部分，由 **John Cristy** 创建于 **1987 年**。它提供摄影工作流中常见的索引图功能。

# INSTALL

```pacman: sudo pacman -S imagemagick```

```apk: sudo apk add imagemagick```

```brew: brew install imagemagick```

```nix: nix profile install nixpkgs#imagemagick```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[convert](/man/convert)(1), [magick](/man/magick)(1), [identify](/man/identify)(1), [display](/man/display)(1)
