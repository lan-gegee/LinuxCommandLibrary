# TAGLINE

PDF 处理命令行工具集

# TLDR

**从 PDF 提取文本**

```pdftotext [document.pdf] [output.txt]```

**获取 PDF 信息**

```pdfinfo [document.pdf]```

**将 PDF 转换为图片**

```pdftoppm [document.pdf] [output] -png```

**从 PDF 提取图片**

```pdfimages [document.pdf] [prefix]```

**合并 PDF 文件**

```pdfunite [file1.pdf] [file2.pdf] [output.pdf]```

# SYNOPSIS

来自 Poppler 库的 PDF 实用工具集合

# UTILITIES

**pdftotext**
> 提取文本内容。

**pdfinfo**
> 显示 PDF 元数据。

**pdftoppm**
> 转换为 PPM/PNG/JPEG 图片。

**pdfimages**
> 提取内嵌图片。

**pdfunite**
> 合并多个 PDF。

**pdfseparate**
> 将 PDF 拆分为单页。

**pdffonts**
> 列出所使用的字体。

**pdfdetach**
> 提取附件。

**pdfattach**
> 向 PDF 添加附件。

**pdftocairo**
> 使用 Cairo 将 PDF 转换为图片格式。

**pdftohtml**
> 将 PDF 转换为 HTML。

**pdftops**
> 将 PDF 转换为 PostScript。

# DESCRIPTION

**poppler-utils** 是一组用于处理 PDF 文件的命令行工具，基于 Poppler PDF 渲染库。它提供提取、转换和处理功能。

# CAVEATS

文本提取质量因 PDF 结构而异。有些 PDF 只包含图片。需安装 poppler-utils 软件包。

# HISTORY

Poppler 从 **Derek Noonburg** 的 **Xpdf** 分叉而来，由 freedesktop.org 项目维护。

# INSTALL

```dnf: sudo dnf install poppler-utils```

```nix: nix profile install nixpkgs#poppler-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pdftotext](/man/pdftotext)(1), [pdftoppm](/man/pdftoppm)(1), [pdfinfo](/man/pdfinfo)(1), [pdftk](/man/pdftk)(1), [gs](/man/gs)(1), [qpdf](/man/qpdf)(1)
