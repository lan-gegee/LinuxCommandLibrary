# TAGLINE

将 HTML 和 CSS 渲染为 PDF 和 PNG

# TLDR

**将 HTML 转换为 PDF**

```weasyprint [input.html] [output.pdf]```

**从 URL 转换**

```weasyprint [https://example.com] [output.pdf]```

**将 HTML 转换为 PNG**

```weasyprint [input.html] [output.png]```

**指定样式表**

```weasyprint -s [style.css] [input.html] [output.pdf]```

**设置资源的 base URL**

```weasyprint -u [https://example.com/] [input.html] [output.pdf]```

**以指定分辨率渲染**

```weasyprint -r [150] [input.html] [output.png]```

**多个样式表**

```weasyprint -s [base.css] -s [print.css] [input.html] [output.pdf]```

# SYNOPSIS

**weasyprint** [_-s stylesheet_] [_-u base_url_] [_-r resolution_] [_options_] _input_ _output_

# PARAMETERS

**-s**, **--stylesheet** _FILE_
> 添加 CSS 样式表。

**-u**, **--base-url** _URL_
> 相对资源的 base URL。

**-m**, **--media-type** _TYPE_
> 媒体类型（默认：print）。

**-r**, **--resolution** _DPI_
> PNG 输出的分辨率。

**-a**, **--attachment** _FILE_
> 将文件附加到 PDF。

**-p**, **--presentational-hints**
> 遵循 HTML 表现性提示。

**--pdf-identifier** _ID_
> PDF 文档标识符。

**--pdf-variant** _VARIANT_
> PDF 变体：pdf/a-1b、pdf/a-2b、pdf/a-3b、pdf/ua-1。

**--pdf-version** _VERSION_
> PDF 版本：1.4、1.5、1.6、1.7、2.0。

**--pdf-forms**
> 启用 PDF 表单。

**--optimize-images**
> 无损优化图片。

**--hinting**
> 启用字体微调（hinting）。

**-e**, **--encoding** _ENCODING_
> 输入编码。

**-v**, **--verbose**
> 详细输出。

# DESCRIPTION

**WeasyPrint** 将 HTML/CSS 渲染为 PDF 和 PNG。它专为从网页内容创建可打印文档而设计，支持用于分页媒体的 CSS。

该工具处理 HTML 时提供完整的 CSS 支持，包括现代特性：flexbox、grid、CSS 变量和媒体查询。打印专用 CSS（分页、边距、页眉/页脚）也能正确工作。

CSS Paged Media 支持复杂的印刷排版：多栏布局、页码、页眉页脚、交叉引用和脚注。@page 规则控制页面大小和边距。

PDF 输出包含内部链接、由标题生成的书签，以及可选的文件附件。PDF/A 变体可确保长期存档的质量。

输入可以是文件、URL 或标准输入。外部样式表可以覆盖或扩展文档样式。base URL 用于解析相对资源路径。

图片优化可在不损失质量的前提下减小文件体积。字体嵌入确保无论系统安装了什么字体都能一致渲染。

# CAVEATS

大型文档可能占用大量内存。某些复杂 CSS 的渲染效果可能与浏览器不一致。不支持 JavaScript——仅支持静态 HTML。PDF 表单支持较为基础。字体渲染与浏览器存在一些差异。

# HISTORY

**WeasyPrint** 由 **Kozea**（Simon Sapin 等人）于 **2011 年**前后创建。它被设计为 wkhtmltopdf 的替代品，使用原生 Python 库而不是无头浏览器。对 CSS Paged Media 的专注使其特别适合文档生成。

# INSTALL

```dnf: sudo dnf install weasyprint```

```apk: sudo apk add weasyprint```

```brew: brew install weasyprint```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wkhtmltopdf](/man/wkhtmltopdf)(1), [pandoc](/man/pandoc)(1), [prince](/man/prince)(1), [puppeteer](/man/puppeteer)(1)
