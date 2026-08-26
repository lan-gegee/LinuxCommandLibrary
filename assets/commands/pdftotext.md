# TAGLINE

将便携式文档格式（PDF）文件转换为纯文本

# TLDR

**提取 PDF 文本**到标准输出

```pdftotext [file.pdf] -```

**提取文本**到文本文件

```pdftotext [file.pdf] [output.txt]```

**提取文本并保留布局**

```pdftotext -layout [file.pdf] [output.txt]```

**从指定页面提取文本**

```pdftotext -f [1] -l [5] [file.pdf] [output.txt]```

**提取原始文本**（不带格式）

```pdftotext -raw [file.pdf] [output.txt]```

**从受密码保护的 PDF 提取文本**

```pdftotext -upw [password] [file.pdf] [output.txt]```

# SYNOPSIS

**pdftotext** [_options_] _PDF-file_ [_text-file_]

# PARAMETERS

**-f** _number_
> 要转换的第一页（默认：第 1 页）

**-l** _number_
> 要转换的最后一页（默认：最后一页）

**-layout**
> 保持原文本的物理布局

**-simple**
> 简单的单栏页面布局

**-table**
> 表格模式，类似 layout 但针对表格优化

**-lineprinter**
> 行式打印机模式，使用等宽字体度量

**-raw**
> 按内容流中的顺序保留字符串

**-fixed** _number_
> 按指定字符宽度假定为等宽字体

**-enc** _encoding_
> 输出文本编码（Latin1、UTF-8 等）

**-nopgbrk**
> 不在页面之间插入分页符

**-opw** _password_
> 加密 PDF 的所有者密码

**-upw** _password_
> 加密 PDF 的用户密码

**-q**
> 安静模式，抑制消息和错误

**-v**
> 显示版本信息

**-h**
> 显示用法信息

# DESCRIPTION

**pdftotext** 将便携式文档格式（PDF）文件转换为纯文本。它从 PDF 文档中提取文本内容，同时可以选择尝试保留原文档的视觉布局。

该程序是 **poppler-utils** 软件包的一部分（在较旧的系统上是 **xpdf-utils**），能够满足大多数 PDF 文本提取需求。只要提供正确的密码，它可以处理加密的 PDF，并支持多种输出编码。

常见用途包括让 PDF 内容可搜索、提取文本以供进一步处理、创建文档的无障碍版本，以及将 PDF 内容送入文本分析流水线。

# CAVEATS

无法从扫描文档或基于图像的 PDF 中提取文本（这类文件请使用 **tesseract** 等 OCR 工具）。对于复杂的多栏文档，布局保持可能不够完美。嵌入了没有 Unicode 映射字体的文本可能无法正确提取。连字和特殊字符在某些输出编码下可能无法正常显示。

# HISTORY

**pdftotext** 最初是 **Derek Noonburg** 于上世纪 90 年代末在 **Xpdf** 项目中开发的。该工具后来被并入 **Poppler** 库——这是 Xpdf 的一个分支，如今已成为许多 Linux 发行版上的标准 PDF 渲染库。两个版本目前都在维护，其中 Poppler 开发更为活跃，并已成为大多数现代系统上的默认选择。

# INSTALL

```apt: sudo apt install poppler-utils```

```dnf: sudo dnf install poppler-utils```

```apk: sudo apk add poppler-utils```

```nix: nix profile install nixpkgs#poppler-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pdfinfo](/man/pdfinfo)(1), [pdfimages](/man/pdfimages)(1), [pdftops](/man/pdftops)(1), [tesseract](/man/tesseract)(1), [mutool](/man/mutool)(1)
