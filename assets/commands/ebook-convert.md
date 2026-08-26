# TAGLINE

电子书格式转换器

# TLDR

**将 EPUB 转换为 MOBI**

```ebook-convert [book.epub] [book.mobi]```

**将 PDF 转换为 EPUB**

```ebook-convert [book.pdf] [book.epub]```

**设置输出配置**

```ebook-convert [input.epub] [output.mobi] --output-profile [kindle]```

**使用自定义封面转换**

```ebook-convert [book.epub] [book.mobi] --cover [cover.jpg]```

**设置元数据**

```ebook-convert [book.epub] [book.mobi] --authors "[Author Name]" --title "[Book Title]"```

**将 HTML 转换为 EPUB**

```ebook-convert [book.html] [book.epub]```

# SYNOPSIS

**ebook-convert** _input_ _output_ [_options_]

# DESCRIPTION

**ebook-convert** 是 Calibre 的命令行电子书格式转换工具。它支持多种格式，包括 EPUB、MOBI、PDF、AZW3、HTML 等。

该工具处理格式特定的优化，并允许自定义输出，包括字体、边距、封面和元数据。

# PARAMETERS

**--output-profile** _profile_
> 设备配置（kindle、ipad 等）。

**--cover** _file_
> 使用自定义封面图像。

**--authors** _names_
> 设置作者元数据。

**--title** _title_
> 设置书名。

**--base-font-size** _size_
> 基础字号（磅）。

**--embed-all-fonts**
> 嵌入所有字体。

**--change-justification** _type_
> 文本对齐方式。

**--margin-top/bottom/left/right** _pts_
> 设置边距。

**--list-recipes**
> 列出新闻订阅源配方。

**--input-encoding** _enc_
> 输入文件编码。

# CAVEATS

PDF 转换可能丢失格式。复杂排版可能无法很好地转换。某些格式功能支持有限。大文件转换可能较慢。

# HISTORY

**ebook-convert** 是 **Calibre** 的一部分，由 **Kovid Goyal** 自 **2006 年**起创建。Calibre 最初面向 Sony Reader 设备，后来发展为支持数十种格式和设备的综合性电子书管理系统。

# SEE ALSO

[calibre](/man/calibre)(1), [ebook-meta](/man/ebook-meta)(1), [pandoc](/man/pandoc)(1)
