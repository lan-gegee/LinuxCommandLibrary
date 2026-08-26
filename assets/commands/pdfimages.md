# TAGLINE

提取 PDF 文件中嵌入的图像

# TLDR

**从 PDF 提取图像**

```pdfimages [document.pdf] [output_prefix]```

**提取为 PNG**

```pdfimages -png [document.pdf] [output_prefix]```

**提取为 JPEG**

```pdfimages -j [document.pdf] [output_prefix]```

**从指定页面范围提取**

```pdfimages -f [1] -l [5] [document.pdf] [output_prefix]```

**只列出图像而不提取**

```pdfimages -list [document.pdf]```

**保留原始格式提取**

```pdfimages -all [document.pdf] [output_prefix]```

# SYNOPSIS

**pdfimages** [_-f first_] [_-l last_] [_-png_] [_-j_] [_-all_] [_options_] _file.pdf_ _prefix_

# PARAMETERS

**-f** _PAGE_
> 开始提取的第一页。

**-l** _PAGE_
> 结束提取的最后一页。

**-png**
> 输出为 PNG。

**-tiff**
> 输出为 TIFF。

**-j**
> 输出为 JPEG。

**-jp2**
> 输出为 JPEG2000。

**-jbig2**
> 输出为 JBIG2。

**-ccitt**
> 输出为 CCITT 传真格式。

**-all**
> 尽可能以原始格式写出图像。

**-list**
> 列出图像详情而不提取。

**-p**
> 在输出文件名中加入页码。

**-q**
> 安静模式，抑制消息和错误。

**-opw** _PASSWORD_
> 加密 PDF 的所有者密码。

**-upw** _PASSWORD_
> 加密 PDF 的用户密码。

# DESCRIPTION

**pdfimages** 提取 PDF 文件中嵌入的图像。每张图像都会保存为一个带有顺序编号的单独文件。

默认输出为 PPM/PBM 格式。-png、-j 等格式选项可转换为常见格式。-all 选项尽可能保留原始压缩方式。

列表模式在不提取的情况下显示图像详情：尺寸、色彩空间、压缩方式和大小。这有助于在提取前了解 PDF 内容。

页面范围选项可将提取限定于特定页面。对于只需其中某些页面的大文档很有用。

PDF 中的图像可能被拆分为多个对象，或使用特殊的色彩空间。该工具能透明地处理这些情况。

输出文件以给定前缀开头，后跟序号和格式扩展名。

# CAVEATS

由于 PDF 变换的影响，某些图像提取后可能出现意外的尺寸或颜色。内联图像可能无法正确提取。蒙版和透明度需要特殊处理。

# HISTORY

**pdfimages** 是 **poppler-utils** 的一部分，源自 **Derek Noonburg** 的 **Xpdf** 项目。这些工具提供了通过命令行操作 PDF 内容的能力。

# INSTALL

```apt: sudo apt install poppler-utils```

```dnf: sudo dnf install poppler-utils```

```apk: sudo apk add poppler-utils```

```nix: nix profile install nixpkgs#poppler-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pdftotext](/man/pdftotext)(1), [pdfinfo](/man/pdfinfo)(1), [pdftoppm](/man/pdftoppm)(1), [convert](/man/convert)(1)
