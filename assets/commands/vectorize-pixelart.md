# TAGLINE

将像素画转换为 SVG 矢量图

# TLDR

**转换像素画**

```vectorize-pixelart [input.png] [output.svg]```

**指定缩放**

```vectorize-pixelart -s [4] [input.png] [output.svg]```

**简化曲线**

```vectorize-pixelart --simplify [input.png] [output.svg]```

# SYNOPSIS

**vectorize-pixelart** [_-s scale_] [_options_] _input_ _output_

# PARAMETERS

**-s** _SCALE_
> 输出缩放倍数。

**--simplify**
> 简化路径。

**--help**
> 显示帮助。

# DESCRIPTION

**vectorize-pixelart** 将像素画图像转换为可缩放矢量图形（SVG）。与通用图像描摹工具不同，它专为像素画设计，能够保留定义这一风格的锐利边缘和干净的几何形状。

生成的 SVG 文件可以缩放到任意分辨率而不会出现模糊或锯齿。这使该工具非常适合为高分辨率显示器、印刷媒体或网页准备像素画素材，在多种尺寸下都能清晰呈现。

# CAVEATS

仅适用于像素画。不适合照片。Rust 实现。

# HISTORY

**vectorize-pixelart** 为将像素画图像转换为可缩放矢量图形而生。

# SEE ALSO

[potrace](/man/potrace)(1), [inkscape](/man/inkscape)(1), [convert](/man/convert)(1)
