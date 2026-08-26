# TAGLINE

从 PDF 文档提取表格

# TLDR

**从 PDF 提取表格**

```tabula [document.pdf]```

输出为 CSV

```tabula -o [output.csv] [document.pdf]```

指定页码

```tabula -p [1,2,3] [document.pdf]```

JSON 输出

```tabula -f JSON [document.pdf]```

所有页面

```tabula -p all [document.pdf]```

指定区域

```tabula -a [0,0,100,100] [document.pdf]```

# SYNOPSIS

**tabula** [_-p pages_] [_-o file_] [_-f format_] [_options_] _pdf_

# PARAMETERS

**-p** _PAGES_
> 页码。

**-o** _FILE_
> 输出文件。

**-f** _FORMAT_
> 输出格式（CSV、JSON、TSV）。

**-a** _AREA_
> 提取区域。

**-g**
> 猜测表格区域。

**-l**
> 强制 lattice 模式（带分隔线的表格）。

**-s**
> 强制 stream 模式（不带分隔线的表格）。

# DESCRIPTION

**tabula** 从 PDF 文档中提取表格数据，并将其转换为 CSV、JSON 或 TSV 等结构化格式。它的设计目标是解放困在 PDF 里的数据——这些表格只是视觉上呈现出来，并没有存储为真正的数据结构。

该工具提供两种提取模式：lattice 模式通过查找单元格之间的分隔线来检测表格；stream 模式则利用空白和文本对齐来确定列边界。自动检测会选出最合适的方式，但对于特定的文档版式，手动选择模式往往能提高准确性。当目标表格只占页面的一部分时，area 选项可用于定位页面的特定区域。

Tabula 以 Java 应用运行，可处理指定页面或整个文档。它最初是作为一个 Web 应用诞生的，供需要从政府报告和财务披露文件中提取数据的记者使用；命令行版本提供同样的提取引擎，适合脚本和自动化工作流。

# CAVEATS

需要 Java 运行环境。表格检测的准确率因 PDF 版式而异；手动指定 **-l**（lattice）或 **-s**（stream）模式通常能改善结果。无法从扫描件/图像型 PDF 中提取表格（请先用 OCR 工具处理）。

# HISTORY

**Tabula** 由 **ProPublica** 和《纽约时报》的新闻记者们创建，用于从 PDF 文档中提取数据。

# INSTALL

```aur: yay -S tabula```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pdftotext](/man/pdftotext)(1), [camelot](/man/camelot)(1), [pdf2json](/man/pdf2json)(1)
