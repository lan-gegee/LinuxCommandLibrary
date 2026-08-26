# TAGLINE

从网页中提取正文内容

# TLDR

**从 URL 提取文本**

```trafilatura -u [https://example.com]```

**从本地 HTML 文件提取**

```trafilatura -i [page.html]```

**输出 JSON 并附带元数据**

```trafilatura -u [https://example.com] --json --with-metadata```

提取时**不含评论或表格**

```trafilatura -u [https://example.com] --no-comments --no-tables```

从文件批量处理 URL 并输出到目录

```trafilatura -i [urls.txt] -o [output_dir]```

**偏重精确率而非召回率**

```trafilatura -u [https://example.com] --precision```

# SYNOPSIS

**trafilatura** [_-u url_] [_-i file_] [_options_]

# PARAMETERS

**-u, --URL** _URL_
> 抓取并处理一个 URL。

**-i, --input-file** _FILE_
> 输入文件（HTML 文件或用于批量处理的 URL 列表）。

**-o, --output-dir** _DIR_
> 将结果写入指定目录。

**--output-format** _FORMAT_
> 输出格式：txt、csv、json、html、markdown、xml、xmltei。

**--json**
> JSON 输出的简写形式。

**--xml**
> XML 输出的简写形式。

**--csv**
> CSV 输出的简写形式。

**--no-comments**
> 提取时排除评论。

**--no-tables**
> 提取时排除表格元素。

**--with-metadata**
> 提取元数据并将其包含在输出中。

**--precision**
> 偏重提取精确率（噪声更少，文本更少）。

**--recall**
> 偏重提取召回率（文本更多，可能噪声也更多）。

**-f, --fast**
> 快速提取，不做后备检测。

**--formatting**
> 保留文本格式（粗体、斜体等）。

**--links**
> 在输出中包含链接及其目标。

**--deduplicate**
> 过滤重复的文档和段落。

**--feed** [_URL_]
> 查找 feed 或将 feed URL 作为输入传入。

**--sitemap** [_URL_]
> 查找站点地图或输入站点地图 URL。

**--parallel** _N_
> 用于下载和处理的核心/线程数。

# DESCRIPTION

**trafilatura** 从网页中提取正文内容，自动去除导航栏、广告、页眉、页脚和其他样板元素。它可以直接从 URL 抓取页面，也可以处理本地 HTML 文件。

输出支持纯文本、CSV、JSON、HTML、Markdown、XML 或 XML-TEI 格式。该工具还能提取发布日期、作者和页面标题等元数据。批量处理可以从列表文件读取多个 URL，因此适合网页抓取和语料库构建。内置了通过 feed、站点地图和爬取进行的链接发现功能。

# CAVEATS

需要 Python。提取质量因网站结构而异。抓取 URL 需要网络连接。

# HISTORY

**trafilatura** 由 **Adrien Barbaresi** 创建，最初是一个用于网页抓取和文本提取的学术项目，使用 **Python** 编写。

# INSTALL

```brew: brew install trafilatura```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[curl](/man/curl)(1), [wget](/man/wget)(1), [scrapy](/man/scrapy)(1), [lynx](/man/lynx)(1)
