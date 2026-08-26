# TAGLINE

使用 Cairo 图形库将 PDF 页面转换为多种图像和矢量格式

# TLDR

**将 PDF 转换为 PNG**

```pdftocairo -png [document.pdf] [output_prefix]```

**将 PDF 转换为 SVG**

```pdftocairo -svg [document.pdf] [output.svg]```

**将 PDF 转换为 EPS**

```pdftocairo -eps [document.pdf] [output.eps]```

**转换指定页面**

```pdftocairo -png -f [1] -l [1] [document.pdf] [output]```

**以指定分辨率转换**

```pdftocairo -png -r [300] [document.pdf] [output]```

**转换为 JPEG**

```pdftocairo -jpeg [document.pdf] [output]```

**缩放到指定尺寸**

```pdftocairo -png -scale-to [800] [document.pdf] [output]```

# SYNOPSIS

**pdftocairo** [_-png_] [_-svg_] [_-eps_] [_-pdf_] [_-r dpi_] [_-f first_] [_-l last_] [_options_] _input.pdf_ _output_

# PARAMETERS

**-png**
> 输出为 PNG。

**-jpeg**
> 输出为 JPEG。

**-tiff**
> 输出为 TIFF。

**-svg**
> 输出为 SVG。

**-eps**
> 输出为 EPS。

**-ps**
> 输出为 PostScript。

**-pdf**
> 输出为 PDF。

**-r** _DPI_
> 分辨率（DPI）。

**-f** _PAGE_
> 第一页。

**-l** _PAGE_
> 最后一页。

**-scale-to** _SIZE_
> 缩放到指定像素尺寸。

**-x** _N_
> X 偏移。

**-y** _N_
> Y 偏移。

**-W** _N_
> 宽度。

**-H** _N_
> 高度。

**-transp**
> 透明背景。

**-antialias** _MODE_
> 抗锯齿模式（default、none、gray、subpixel）。

# DESCRIPTION

**pdftocairo** 使用 Cairo 图形库将 PDF 页面转换为多种图像和矢量格式。它生成适合打印和网络的高质量输出。

PNG 输出按指定分辨率生成光栅图像。更高的 DPI 会产生更大、更精细的图像。默认为 150 DPI。

SVG 输出生成可缩放的矢量图形，保留文本和形状。非常适合编辑或嵌入网页。

EPS 输出生成封装 PostScript，适用于打印流程。可与 LaTeX 及专业出版工具集成。

透明背景可用于 PNG 叠加与合成。JPEG 输出体积更小但会丢失透明度。

页面范围选择可提取特定页面。结合脚本即可轻松批量转换大型文档。

# CAVEATS

矢量输出在复杂字体上可能出现问题。非常高的 DPI 会占用大量内存。某些 PDF 特性可能无法完美转换。

# HISTORY

**pdftocairo** 是 **poppler-utils** 的一部分，使用 **Cairo** 图形库。借助 Cairo 成熟的渲染能力，它比旧的光栅化工具提供更高质量的输出。

# INSTALL

```apt: sudo apt install poppler-utils```

```dnf: sudo dnf install poppler-utils```

```apk: sudo apk add poppler-utils```

```nix: nix profile install nixpkgs#poppler-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pdftoppm](/man/pdftoppm)(1), [convert](/man/convert)(1), [inkscape](/man/inkscape)(1), [pdfimages](/man/pdfimages)(1)
