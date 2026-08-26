# TAGLINE

通过混合与合成操作组合图像

# TLDR

**将一张图像叠加**到另一张上

```composite [overlay.png] [background.png] [output.png]```

**将叠加图像放置在指定位置**

```composite -geometry +[100]+[50] [overlay.png] [background.png] [output.png]```

**以透明度混合图像**

```composite -blend [50]% [image1.png] [image2.png] [output.png]```

**使用蒙版进行合成**

```composite [overlay.png] [background.png] [mask.png] [output.png]```

**应用正片叠底（multiply）**混合模式

```composite -compose multiply [overlay.png] [background.png] [output.png]```

**将叠加图像溶解**进背景

```composite -dissolve [75]% [overlay.png] [background.png] [output.png]```

**使叠加图像居中于背景**

```composite -gravity center [overlay.png] [background.png] [output.png]```

# SYNOPSIS

**composite** [_options_] _overlay_ _background_ [_mask_] _output_

# PARAMETERS

**-compose** _METHOD_
> 合成算子：over、multiply、screen、overlay、darken、lighten 等。

**-geometry** _GEOMETRY_
> 叠加图的位置偏移（+X+Y 格式）。

**-gravity** _TYPE_
> 锚点：center、north、south、east、west、northeast 等。

**-blend** _GEOMETRY_
> 源图与目标图的混合百分比。

**-dissolve** _PERCENT_
> 按指定百分比将叠加图溶解进背景。

**-watermark** _BRIGHTNESS_
> 以给定亮度将叠加图作为水印应用。

**-tile**
> 将叠加图像平铺铺满背景。

**-stegano** _OFFSET_
> 将叠加图隐藏在背景图像中（隐写术）。

**-stereo** _OFFSET_
> 创建立体红蓝图（anaglyph）。

**-density** _VALUE_
> 设置图像分辨率。

**-quality** _VALUE_
> 输出压缩质量（0-100）。

# DESCRIPTION

**composite** 是 ImageMagick 中用于将两张或多张图像组合成单张图像的工具。它提供类似于图形编辑器图层混合的大量合成操作，可以在命令行完成复杂的图像处理。

叠加图像按照指定的 compose 方法和定位方式覆盖在背景图像之上。可选的蒙版图像可以控制叠加图的哪些部分影响最终结果。常见用途包括添加水印、制作图像拼贴以及应用视觉效果。

gravity 选项提供便捷的定位方式（居中、四角、四边），而 geometry 则支持像素级精确摆放。multiply、screen、overlay 等混合模式遵循标准的图形合成数学规则。

# CAVEATS

图像顺序很重要：命令中叠加图位于背景图之前。默认情况下，输出继承背景图像的尺寸。alpha 通道会影响合成结果；需要精确控制请使用 **-alpha** 相关选项。批量处理建议改用 **mogrify** 或 **magick** 以获得更好性能。

# HISTORY

composite 是 **ImageMagick** 的一部分，后者由 John Cristy 于 **1990 年**创建。它已发展为支持数十种合成算子，能力媲美专业图像编辑软件。对于需要脚本化的图像处理，该工具依然不可或缺。

# INSTALL

```pacman: sudo pacman -S imagemagick```

```apk: sudo apk add imagemagick```

```brew: brew install imagemagick```

```nix: nix profile install nixpkgs#imagemagick```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[convert](/man/convert)(1), [montage](/man/montage)(1), [mogrify](/man/mogrify)(1), [magick](/man/magick)(1)

# RESOURCES

```[Source code](https://github.com/ImageMagick/ImageMagick)```

```[Homepage](https://imagemagick.org)```

```[Documentation](https://imagemagick.org/script/composite.php)```

<!-- verified: 2026-06-22 -->
