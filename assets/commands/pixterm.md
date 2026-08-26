# TAGLINE

使用 ANSI 颜色在终端中渲染图像

# TLDR

**在终端中显示图像**

```pixterm [image.png]```

**缩放到终端宽度**

```pixterm -s [2] [image.png]```

**设置字符单元大小**

```pixterm -tc [2] -tr [6] [image.png]```

**使用指定颜色深度**

```pixterm -d [24] [image.png]```

**抖动模式**

```pixterm -m [0] [image.png]```

**输出到文件**

```pixterm [image.png] > [output.txt]```

# SYNOPSIS

**pixterm** [_-s scale_] [_-tc cols_] [_-tr rows_] [_-d depth_] [_options_] _image_

# PARAMETERS

**-s** _SCALE_
> 图像的缩放系数。

**-tc** _N_
> 渲染宽度使用的终端列数。

**-tr** _N_
> 渲染高度使用的终端行数。

**-d** _DEPTH_
> 颜色深度：8（256 色）或 24（真彩色）。

**-m** _MODE_
> 抖动模式。使用不同深浅的方块元素或 ASCII 字符进行渲染。

**-noresize**
> 不调整图像尺寸以适应终端。

**-matte** _COLOR_
> 透明图像的背景衬底色。

# DESCRIPTION

**pixterm** 使用 ANSI 转义码和 Unicode 半块字符直接在终端中渲染图像。每个文本字符单元表示两个垂直像素，可获得比纯字符渲染器更高的分辨率。

颜色深度可设为 24 位真彩色以获得最佳质量，或 8 位（256 色）以获得更广的终端兼容性。抖动算法能改善渐变和颜色过渡的渲染效果，但会增加处理时间。

输出是标准 ANSI 文本，可以重定向到文件以便日后显示。scale 和 cell size 参数控制图像如何映射到终端尺寸。

# CAVEATS

质量取决于终端能力。大图像可能较慢。字体影响外观效果。

# HISTORY

**pixterm** 是一个基于 Go 的终端图像查看器，利用现代终端能力提供高质量的图像渲染。

# INSTALL

```aur: yay -S pixterm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[catimg](/man/catimg)(1), [chafa](/man/chafa)(1), [tiv](/man/tiv)(1), [viu](/man/viu)(1)
