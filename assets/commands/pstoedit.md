# TAGLINE

将 PostScript 和 PDF 转换为矢量格式

# TLDR

将 PDF 页面转换为 **PNG 或 JPEG**

```pstoedit -page [1] -f magick [file.pdf] [output.png]```

将**多页**转换为带编号的图像

```pstoedit -f magick [file.pdf] [page%d.png]```

# SYNOPSIS

**pstoedit** [**-page** _num_] [**-f** _format_] _input_ _output_

# PARAMETERS

**-page _num_**
> 要转换的页码（从 1 开始）

**-f _format_**
> 输出格式驱动

**-dt**
> 将文字绘制为多边形

**-adt**
> 用直线近似曲线

**-flat _value_**
> 曲线近似的平整度

# DESCRIPTION

**pstoedit** 将 PostScript 和 PDF 文件转换为多种矢量与位图格式。它使用针对特定格式的驱动程序，生成适合不同应用的输出。

该工具可以转换为 SVG、DXF 等格式，也可通过 ImageMagick 转换为光栅格式。适用于从 PDF 文档中提取图形。

# CAVEATS

转换质量取决于源 PDF 的复杂程度。文字可能被转为轮廓线。部分格式需要额外的驱动程序。复杂渐变可能无法良好转换。

# HISTORY

**pstoedit** 由 **Wolfgang Glunz** 创建，用于将 PostScript 图形转换为可编辑的矢量格式。自 20 世纪 90 年代以来持续维护，支持多种输出格式。

# INSTALL

```apt: sudo apt install pstoedit```

```dnf: sudo dnf install pstoedit```

```pacman: sudo pacman -S pstoedit```

```zypper: sudo zypper install pstoedit```

```brew: brew install pstoedit```

```nix: nix profile install nixpkgs#pstoedit```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ps2pdf](/man/ps2pdf)(1), [pdf2svg](/man/pdf2svg)(1), [convert](/man/convert)(1)
