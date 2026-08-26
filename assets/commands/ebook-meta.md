# TAGLINE

电子书元数据编辑器

# TLDR

**显示元数据**

```ebook-meta [book.epub]```

**设置标题**

```ebook-meta [book.epub] --title "[New Title]"```

**设置作者**

```ebook-meta [book.epub] --authors "[Author Name]"```

**设置封面**

```ebook-meta [book.epub] --cover [cover.jpg]```

**提取封面图像**

```ebook-meta [book.epub] --get-cover [cover.jpg]```

**设置多个字段**

```ebook-meta [book.epub] --title "[Title]" --authors "[Author]" --publisher "[Publisher]"```

# SYNOPSIS

**ebook-meta** _file_ [_options_]

# DESCRIPTION

**ebook-meta** 读写电子书文件中的元数据。作为 Calibre 的一部分，它支持包括 EPUB、MOBI、AZW3 和 PDF 在内的多种格式。

该工具可以显示现有元数据，并修改标题、作者、出版商、日期和封面图等字段，而无需转换文件。

# PARAMETERS

**--title** _title_
> 设置书名。

**--authors** _names_
> 设置作者（逗号分隔）。

**--publisher** _name_
> 设置出版商。

**--date** _date_
> 设置出版日期。

**--isbn** _isbn_
> 设置 ISBN。

**--tags** _tags_
> 设置标签（逗号分隔）。

**--series** _name_
> 设置丛书名。

**--series-index** _n_
> 设置在丛书中的位置。

**--cover** _file_
> 从图像设置封面。

**--get-cover** _file_
> 将封面提取到文件。

**--language** _lang_
> 设置语言。

**--comments** _text_
> 设置描述/评论。

**--rating** _n_
> 设置评分（1 到 5）。

**--author-sort** _name_
> 设置按作者排序所用的字符串。

**--to-opf** _file.opf_
> 将该书的元数据写入 OPF 文件。

**--from-opf** _file.opf_
> 从 OPF 文件读取元数据并应用到该书。

**--identifier** _id:value_
> 设置标识符，例如 `--identifier doi:10.1234/foo`。可重复使用。

# CAVEATS

并非所有格式都支持所有元数据字段。PDF 的元数据有限。默认直接修改原文件。某些元数据需要特定格式的支持。

# HISTORY

**ebook-meta** 是 **Calibre** 的一部分，由 **Kovid Goyal** 于 **2006 年**创建。它以命令行方式提供 Calibre 的元数据编辑功能，对批处理和脚本化操作至关重要。

# SEE ALSO

[ebook-convert](/man/ebook-convert)(1), [calibre](/man/calibre)(1), [exiftool](/man/exiftool)(1)

# RESOURCES

```[Source code](https://github.com/kovidgoyal/calibre)```

```[Homepage](https://calibre-ebook.com/)```

```[Documentation](https://manual.calibre-ebook.com/generated/en/ebook-meta.html)```

<!-- verified: 2026-07-14 -->
