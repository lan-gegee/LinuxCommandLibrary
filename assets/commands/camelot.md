# TAGLINE

从 PDF 文件中提取表格

# TLDR

**从 PDF 提取表格**

```camelot read -p [1] [document.pdf]```

**提取表格并保存为 CSV**

```camelot read -p [1] [document.pdf] -o [output.csv]```

**从多个页面提取表格**

```camelot read -p [1,2,3] [document.pdf]```

**使用 stream 模式提取**（适用于无边框表格）

```camelot read -p [1] -flavor stream [document.pdf]```

**指定表格区域提取**

```camelot read -p [1] -T [50,700,500,100] [document.pdf]```

**生成可视化调试报告**

```camelot read -p [1] -plot text [document.pdf]```

**导出为多种格式**

```camelot read -p [1] -f [json] [document.pdf]```

# SYNOPSIS

**camelot** _command_ [_options_] _pdffile_

# PARAMETERS

**read**
> 从 PDF 文件读取表格。

**-p**, **--pages** _pages_
> 要处理的页码（如 "1"、"1-5"、"1,3,5"）。

**-o**, **--output** _file_
> 输出文件路径。

**-f**, **--format** _format_
> 输出格式：csv、excel、html、json、markdown、sqlite。

**-flavor** _mode_
> 提取模式：lattice（有边框）或 stream（无边框）。

**-T**, **--table-areas** _coords_
> 表格边界，格式为 x1,y1,x2,y2。

**-C**, **--columns** _coords_
> stream 模式的列分隔位置。

**-plot** _type_
> 生成调试图：text、grid、contour、joint、line。

**-compress**
> 压缩输出文件。

**-split**
> 将输出按表格拆分为单独的文件。

# DESCRIPTION

**Camelot** 是一个用于从 PDF 文件提取表格数据的 Python 库和 CLI 工具。它利用计算机视觉和格线检测算法识别表格，并将其内容提取为结构化格式。

有两种提取方式：**lattice** 模式通过查找相交线来检测有可见边框的表格；**stream** 模式基于空白模式寻找表格，适用于无边框表格。

该工具支持多页提取、合并单元格以及多种输出格式。可视化调试有助于理解表格是如何被检测的，并可为难以处理的 PDF 调整提取参数。

# CAVEATS

Camelot 只能处理文本型 PDF；扫描文档需先进行 OCR。包含嵌套表格或结构不规则的复杂表格布局可能需要手动调参。stream 模式的准确率很大程度上取决于间距的一致性。大型 PDF 可能消耗大量内存。

# HISTORY

Camelot 由 **Vinayak Mehta** 创建，于 **2019** 年发布，是商业 PDF 表格提取工具的开源替代品。它以传说中的城堡命名，目标是成为“PDF 表格提取的 Excalibur”。该项目让表格提取变得易用且可编程，填补了 Python 数据科学生态系统的空白，因而广受欢迎。

# INSTALL

```aur: yay -S camelot```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tabula](/man/tabula)(1), [pdftotext](/man/pdftotext)(1)
