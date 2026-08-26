# TAGLINE

使用 ImageMagick 6 合成图像

# TLDR

**将一张图像叠加**到另一张上

```composite.im6 [overlay.png] [background.png] [output.png]```

**将叠加图像放置在指定位置**

```composite.im6 -geometry +[100]+[50] [overlay.png] [background.png] [output.png]```

**以透明度混合图像**

```composite.im6 -blend [50]% [image1.png] [image2.png] [output.png]```

**应用正片叠底（multiply）**混合模式

```composite.im6 -compose multiply [overlay.png] [background.png] [output.png]```

**将叠加图像溶解**进背景

```composite.im6 -dissolve [75]% [overlay.png] [background.png] [output.png]```

**使叠加图像居中于背景**

```composite.im6 -gravity center [overlay.png] [background.png] [output.png]```

# SYNOPSIS

**composite.im6** [_options_] _overlay_ _background_ [_mask_] _output_

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

**-quality** _VALUE_
> 输出压缩质量（0-100）。

**-stegano** _OFFSET_
> 使用隐写术将水印隐藏在图像中。

**-stereo** _+X+Y_
> 由两张图像创建立体红蓝图（anaglyph）。

**-alpha** _TYPE_
> 启用、禁用或重置 alpha 通道。

# DESCRIPTION

**composite.im6** 是 ImageMagick 第 6 版中用于通过合成操作组合图像的命令。它在功能上与 **composite** 完全相同，但显式指向 ImageMagick 6 的安装，适用于同时安装了 ImageMagick 6 和 7 的系统。

该工具使用各种混合模式和定位选项将一张图像叠加到另一张之上。它支持基于蒙版的合成、添加水印，以及数十种媲美专业图像编辑能力的合成算子。

在大多数系统上，这个带版本号的命令是为了确保为 ImageMagick 6 编写的脚本在同时存在 ImageMagick 7 时仍能正常运行。**im6** 后缀表示旧版 API 版本。

# CAVEATS

ImageMagick 6 处于维护模式；新功能只加入 ImageMagick 7。某些系统可能只安装了其中一个版本。显式调用 **composite.im6** 的脚本在只安装了 ImageMagick 7 的系统上会失败。

# HISTORY

ImageMagick 由 John Cristy 于 **1990 年**创建。第 6 版是长期稳定的发布版本。当 ImageMagick 7 于 **2016 年**引入破坏性变更后，带版本号的命令名被加入以允许两个版本共存，**.im6** 后缀表示第 6 版的命令。

# SEE ALSO

[composite](/man/composite)(1), [convert](/man/convert)(1), [mogrify.im6](/man/mogrify.im6)(1), [display.im6](/man/display.im6)(1), [magick](/man/magick)(1)
