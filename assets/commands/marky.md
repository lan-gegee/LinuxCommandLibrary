# TAGLINE

将多种格式的文档转换为 Markdown

# TLDR

**转换 PDF** 并将 Markdown 打印到 stdout

```marky [document.pdf]```

**转换 Word 文档**并保存到文件

```marky [document.docx] --output [converted.md]```

**转换 Excel 表格**，使用输出标志的简写形式

```marky [data.xlsx] -o [table.md]```

**转换 PowerPoint 演示文稿**

```marky [presentation.pptx] -o [slides.md]```

**将 HTML 页面转换为 Markdown**

```marky [webpage.html] -o [content.md]```

**转换 Jupyter 笔记本**

```marky [notebook.ipynb] -o [notebook.md]```

# SYNOPSIS

**marky** _INPUT_ [**-o** _OUTPUT_]

# PARAMETERS

**-o** _FILE_, **--output** _FILE_
> 将生成的 Markdown 写入 _FILE_。不使用此标志时结果打印到标准输出。

**-h**, **--help**
> 显示用法信息。

**-v**, **--version**
> 打印版本并退出。

# DESCRIPTION

**marky** 是一个小巧的 Go 命令行工具（也是可嵌入的库），可将文档转换为整洁易读的 **Markdown**。它支持 CSV、EPUB、HTML、Jupyter 笔记本（_.ipynb_）、Microsoft Word（_.docx_）、Microsoft Excel（_.xlsx_）、PDF 和 PowerPoint（_.pptx_）文件。

输入格式根据文件扩展名自动检测，因此通常一条命令——_marky somefile.ext_——就够了。不带 **-o** 时，Markdown 输出到 stdout，方便 marky 与其他工具串联使用（_marky report.pdf | pandoc -o report.html_）。该项目还提供一个配套的 **marky-mcp**，通过 Model Context Protocol 暴露相同的转换功能，供编程智能体使用。

# INSTALLATION

**marky** 以 Go 程序的形式分发：

```
go install github.com/flaviodelgrosso/marky/cmd/marky@latest
```

需要 Go 1.24 或更新版本的工具链。配套的 MCP 服务器通过以下命令安装：

```
go install github.com/flaviodelgrosso/marky/marky-mcp@latest
```

# CAVEATS

转换保真度取决于底层库（html-to-markdown、excelize、PDF 解析器）；复杂的排版、公式和内嵌图片可能无法完美还原。非常大的 Excel 工作簿可能占用大量内存，因为 marky 在转换前会将整个文档载入内存。

# HISTORY

**marky** 由 **Flavio Del Grosso** 编写，以 **ISC 许可证**发布。它将多个现有的 Go 库整合为一个统一的 CLI 和 MCP 服务器，让向 AI 智能体提供文档变得简单直接。

# SEE ALSO

[pandoc](/man/pandoc)(1), [pdftotext](/man/pdftotext)(1)
