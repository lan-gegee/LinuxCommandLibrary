# TAGLINE

将 PDF 转换为 PostScript 格式

# TLDR

**将 PDF 转换为 PostScript**

```pdftops [input.pdf] [output.ps]```

**转换指定页面**

```pdftops -f [1] -l [10] [input.pdf] [output.ps]```

**Level 2 PostScript 输出**

```pdftops -level2 [input.pdf] [output.ps]```

**针对打印进行优化**

```pdftops -optimizecolorspace [input.pdf] [output.ps]```

# SYNOPSIS

**pdftops** [_options_] _PDF-file_ [_PS-file_]

# PARAMETERS

**-f** _num_
> 第一页。

**-l** _num_
> 最后一页。

**-level1**, **-level2**, **-level3**
> PostScript 级别。

**-eps**
> 生成 EPS。

**-optimizecolorspace**
> 优化颜色。

**-paper** _size_
> 纸张尺寸。

**-r** _dpi_
> 图像分辨率。

# DESCRIPTION

**pdftops** 将 PDF 转换为 PostScript 格式。它是 Poppler 工具集的一部分，对大多数文档来说，其输出质量优于 Ghostscript 的 pdf2ps。
# 基本转换
pdftops document.pdf document.ps

# 从第一页创建 EPS
pdftops -eps -f 1 -l 1 figure.pdf figure.eps

# 打印到 PostScript 打印机
pdftops document.pdf - | lpr -P ps_printer
```

# POSTSCRIPT LEVELS

```
Level 1 - Maximum compatibility
Level 2 - Color, compression
Level 3 - Smooth shading, masks
```

# CAVEATS

输出可能很大。EPS 模式仅适用于单页。属于 poppler-utils 软件包。

# HISTORY

pdftops 是 **Poppler** 的一部分，Poppler 是从 **Derek Noonburg** 的 **Xpdf** 分叉出来的 PDF 渲染库。

# SEE ALSO

[pdf2ps](/man/pdf2ps)(1), [pdftotext](/man/pdftotext)(1), [ps2pdf](/man/ps2pdf)(1), [poppler-utils](/man/poppler-utils)(1)

# INSTALL

```apt: sudo apt install poppler-utils```

```dnf: sudo dnf install poppler-utils```

```apk: sudo apk add poppler-utils```

```nix: nix profile install nixpkgs#poppler-utils```

<!-- packages: 2026-07-22 -->
