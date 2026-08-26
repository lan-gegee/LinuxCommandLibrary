# TAGLINE

将 HTML 和 CSS 转换为 PDF 文档

# TLDR

**将 HTML 转换为 PDF**

```prince [input.html] -o [output.pdf]```

**应用 CSS 样式表**

```prince -s [style.css] [input.html] -o [output.pdf]```

**从 URL 转换**

```prince [https://example.com] -o [page.pdf]```

**多个输入**

```prince [page1.html] [page2.html] -o [combined.pdf]```

# SYNOPSIS

**prince** [_options_] _files_... [**-o** _output.pdf_]

# PARAMETERS

**-o**, **--output** _file_
> 输出 PDF 文件。

**-s**, **--style** _file_
> 附加的 CSS 文件。

**--javascript**
> 启用 JavaScript。

**--media** _type_
> CSS 媒体类型。

**--page-size** _size_
> 页面尺寸。

**--page-margin** _margin_
> 页边距。

**--encrypt**
> 加密 PDF。

# DESCRIPTION

**Prince** 是一款商业 HTML/CSS 转 PDF 转换器，对标准的遵循度极高。它生成的高质量 PDF 适用于印刷出版。

# EXAMPLES

```bash
# Basic conversion
prince document.html -o document.pdf

# With custom styles
prince -s print.css report.html -o report.pdf

# From URL
prince https://example.com/page -o page.pdf

# Multiple files combined
prince cover.html content.html appendix.html -o book.pdf

# With JavaScript
prince --javascript dynamic.html -o output.pdf

# Custom page size
prince --page-size="A4" document.html -o a4.pdf
```

# CAVEATS

生产使用需要商业许可。非商业用途免费。对 CSS Paged Media 的支持非常出色。

# HISTORY

Prince 由 **YesLogic** 自 2003 年起开发，是一款面向出版领域的高质量 HTML 转 PDF 转换器。

# SEE ALSO

[wkhtmltopdf](/man/wkhtmltopdf)(1), [weasyprint](/man/weasyprint)(1), [pandoc](/man/pandoc)(1)
