# TAGLINE

Markdown 转 PDF 转换器

# TLDR

将 Markdown 文件**转换为** PDF

```mdpdf [input.md] -o [output.pdf]```

使用指定纸张大小进行**转换**

```mdpdf [input.md] -o [output.pdf] --paper [A4]```

**设置 PDF 元数据**（标题和作者）

```mdpdf [input.md] -o [output.pdf] --title "[title]" --author "[author]"```

为每一页**添加页眉**

```mdpdf [input.md] -o [output.pdf] --header "[header text]"```

为每一页**添加页脚**

```mdpdf [input.md] -o [output.pdf] --footer "[footer text]"```

将多个输入文件**合并转换**为单个 PDF

```mdpdf [file1.md] [file2.md] -o [combined.pdf]```

# SYNOPSIS

**mdpdf** [_options_] [_INPUTS_]...

# PARAMETERS

**-o, --output** _FILE_
> PDF 输出的目标路径（必需）

**-h, --header** _template_
> 为每一页设置页眉模板

**-f, --footer** _template_
> 为每一页设置页脚模板

**-t, --title** _TEXT_
> PDF 标题元数据

**-s, --subject** _TEXT_
> PDF 主题元数据

**-a, --author** _TEXT_
> PDF 作者元数据

**-k, --keywords** _TEXT_
> PDF 关键词元数据

**-p, --paper** _[letter|A4]_
> 纸张大小（默认：letter）

**--version**
> 显示版本信息

**--help**
> 显示帮助消息

# DESCRIPTION

**mdpdf** 是一个用于将 Markdown 文件转换为 PDF 的命令行应用。它支持 CommonMark Markdown 语法，并基于 base-14 PDF 字体生成整洁的左对齐 PDF 输出。

该工具会将 Markdown 标题转换为 PDF 书签以便导航，将文件链接转换为 PDF 附件，并嵌入可附带说明文字和宽度设置的图片。多个输入文件可以合并为单个输出 PDF。

mdpdf 的设计追求简洁和最少依赖，依靠 **commonmark** 解析 Markdown，用 **PyMuPDF** 生成 PDF，并用 **click** 构建命令行界面。

# CAVEATS

mdpdf 采用统一通用的样式方案，不支持自定义 CSS 或模板。需要高级排版控制、复杂布局或自定义样式的用户可以考虑 **Pandoc** 配合 LaTeX、**WeasyPrint** 或 **md-to-pdf** 等替代工具。

# HISTORY

mdpdf 由 **Norman Lorrain** 创建，使用 **Python** 编写。它以 **MIT** 许可证发布，可通过 **pip** 从 PyPI 安装。该项目专注于提供简单直接、依赖精简的 Markdown 转 PDF 工作流。

# SEE ALSO

[pandoc](/man/pandoc)(1), [wkhtmltopdf](/man/wkhtmltopdf)(1), [groff](/man/groff)(1)
