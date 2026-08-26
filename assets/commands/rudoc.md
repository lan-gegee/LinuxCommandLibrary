# TAGLINE

快速的无依赖文档转换器（Pandoc 替代品）

# TLDR

**将 Markdown 转换为 DOCX**（格式根据扩展名自动检测）

```rudoc [README.md] [README.docx]```

**将 DOCX 转换为 PDF**

```rudoc [report.docx] [report.pdf]```

**将 Markdown 转换为 HTML**，显式指定格式

```rudoc -f md -t html [README.md]```

**将输出写入**指定路径

```rudoc [README.md] -o [/tmp/readme.pdf]```

**将 CSV 转换为 XLSX**

```rudoc [data.csv] [report.xlsx]```

**将 Markdown 转换为 PowerPoint 幻灯片**

```rudoc [notes.md] [slides.pptx]```

**将 Markdown 通过管道转为 HTML**输出到 stdout

```cat [README.md] | rudoc -f md -t html```

**合并多个 Markdown 文件**为一个文档

```rudoc [ch1.md] [ch2.md] [ch3.md] -t html -o [book.html]```

# SYNOPSIS

**rudoc** [**-f** _FORMAT_] [**-t** _FORMAT_] [**-o** _FILE_] [_options_] [_input_...]

# PARAMETERS

**-f**, **--from** _FORMAT_

> 输入格式（省略时根据文件扩展名自动检测）。名称不区分大小写；别名包括 **md**/**markdown**/**gfm**、**html**、**txt**、**docx**、**typ**/**typst**、**pdf**、**pptx**、**csv**、**xlsx**、**xml**、**opml**、**json**。

**-t**, **--to** _FORMAT_

> 输出格式（省略时根据输出路径或第二个路径参数自动检测）。

**-o**, **--output** _FILE_

> 输出路径。在格式支持流式处理时默认为 stdout。

**--standalone**

> 输出包含 head 元数据和 CSS 的完整 HTML 文档。

**--slide-level** _N_

> 写入 **pptx** 时开启新幻灯片的标题级别（默认：**1**）。

**--sheet** _NAME_

> XLSX 输入/输出的工作表名称（默认：**Sheet1**）。

**--pdf-paper** _SIZE_

> PDF 纸张尺寸：**a4**、**a3**、**a5**、**us-letter**、**us-legal**（默认：**a4**）。

**--pdf-font** _NAME_

> Typst/PDF 输出的正文字体（默认：**Arial**）。

**--wrap** _COLS_

> **md**/**txt** 输出的换行宽度（**0** = 关闭）。

**-q**, **--quiet**

> 抑制进度信息。

**-v**, **--verbose**

> 显示中间 IR 统计和耗时信息。

**-h**, **--help**

> 打印帮助信息。

**--version**

> 打印版本号。

# DESCRIPTION

**rudoc** 是一个小巧的静态 Rust 文档转换器，专注于人们日常使用的常见转换。它被设计为 **pandoc** 的聚焦替代品：体积只有几 MB，启动时间低于 5 毫秒，无需语言运行时，并提供一组精选格式而非数十种后端。

支持的富文本转换在 **Markdown**、**HTML**、纯文本、**DOCX**、**Typst**（**.typ**）和 **PDF** 之间双向进行（PDF 输入仅支持文本提取，不保留排版布局）。演示文稿支持 **Markdown → PPTX**，由标题级别控制幻灯片边界。表格数据可在 **CSV ↔ XLSX** 之间转换。结构化数据支持 **XML ↔ OPML ↔ JSON** 转换，在该组内部可无损往返。

格式通常从文件扩展名推断，因此许多调用不需要任何标志。显式的 **-f** / **-t** 覆盖、stdin/stdout 管道、多文件 Markdown 合并以及 PDF 纸张/字体选项则覆盖了脚本化和批处理场景。对于 PDF 输出，rudoc 在存在时会优先使用 **typst** CLI；若编译时启用了 **pdf** 特性，也可以使用内置的 printpdf 路径；否则会打印安装指引。

# CAVEATS

Rudoc 有意支持比 pandoc 更少的格式（大约十几种聚焦的转换路径）。PDF **读取**仅提取文本，不保留布局。质量最高的 PDF **写入**需要在 **PATH** 中有 **typst**；如果没有，则需要一个包含可选内置 PDF 特性的构建版本，否则转换会报错停止。演示文稿导出仅支持 Markdown → PPTX（并非完全双向的幻灯片转换）。

# SEE ALSO

[pandoc](/man/pandoc)(1), [typst](/man/typst)(1), [libreoffice](/man/libreoffice)(1), [soffice](/man/soffice)(1)

# RESOURCES

```[Source code](https://github.com/asong56/rudoc)```

<!-- verified: 2026-07-26 -->
