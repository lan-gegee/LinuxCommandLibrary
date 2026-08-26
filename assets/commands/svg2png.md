# TAGLINE

将 SVG 矢量图形栅格化为 PNG

# TLDR

**将 SVG 转换为 PNG**

```svg2png [input.svg] [output.png]```

**指定宽度**

```svg2png -w [800] [input.svg] [output.png]```

**指定高度**

```svg2png -h [600] [input.svg] [output.png]```

**缩放倍数**

```svg2png --scale [2] [input.svg] [output.png]```

# SYNOPSIS

**svg2png** [_-w width_] [_-h height_] [_options_] _input_ _output_

# PARAMETERS

**-w** _WIDTH_
> 输出宽度。

**-h** _HEIGHT_
> 输出高度。

**--scale** _FACTOR_
> 缩放倍数。

**--background** _COLOR_
> 背景颜色。

**--help**
> 显示帮助。

# DESCRIPTION

**svg2png** 将 SVG 矢量图形文件转换为 PNG 位图图像。它按指定分辨率将可缩放的矢量内容栅格化，生成适合 Web 使用、文档或任何需要位图图像场景的像素输出。

可以通过指定宽度、高度或相对于原 SVG 视口大小的缩放倍数来控制输出尺寸。默认背景为透明，保留来自 SVG 源的 alpha 通道信息。存在基于不同渲染库（如 librsvg 或 Node.js 引擎）的多种实现。

# CAVEATS

实现方式多样。渲染效果可能有所不同。基于 librsvg 或 Node。

# HISTORY

**svg2png** 存在多种实现版本，用于将 SVG 矢量图形转换为 PNG 位图格式。

# INSTALL

```apt: sudo apt install mapnik-utils```

```dnf: sudo dnf install mapnik-utils```

```brew: brew install svg2png```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[inkscape](/man/inkscape)(1), [convert](/man/convert)(1), [rsvg-convert](/man/rsvg-convert)(1)
