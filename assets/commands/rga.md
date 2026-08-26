# TAGLINE

搜索 PDF、归档和文档内部内容

# TLDR

**在所有文件中搜索**

```rga [pattern]```

**在目录中搜索**

```rga [pattern] [directory/]```

**只在 PDF 中搜索**

```rga --type pdf [pattern]```

**带上下文搜索**

```rga -C [3] [pattern]```

**列出支持的类型**

```rga --list-adapters```

**禁用缓存**

```rga --no-cache [pattern]```

**不区分大小写**

```rga -i [pattern]```

# SYNOPSIS

**rga** [_--type type_] [_-C context_] [_options_] _pattern_ [_paths_]

# PARAMETERS

**--type** _TYPE_
> 文件类型过滤器。

**-C**, **--context** _N_
> 上下文行数。

**-i**, **--ignore-case**
> 不区分大小写。

**--no-cache**
> 禁用缓存。

**--list-adapters**
> 显示适配器。

**--rga-cache-max-blob-len** _SIZE_
> 最大缓存大小。

**-l**, **--files-with-matches**
> 只显示文件名。

**-c**, **--count**
> 统计匹配数。

# SUPPORTED FORMATS

**PDF** - Via pdftotext
**Office** - Word, Excel, PowerPoint
**Archives** - zip, tar, gz
**EPUB** - E-books
**SQLite** - Databases
**Images** - OCR via tesseract

# DESCRIPTION

**rga**（ripgrep-all）扩展了 ripgrep，可以搜索纯文本搜索无法触及的文件格式，包括 PDF、Word 文档、Excel 表格、PowerPoint 演示文稿、zip 归档、tar 文件、电子书，甚至 SQLite 数据库。它使用由 pdftotext 和 pandoc 等外部工具支撑的格式专用适配器，从这些文件中提取可搜索的文本。

提取的文本会缓存到磁盘，因此对相同文件的后续搜索几乎瞬时完成。该工具可以深入压缩归档，无需手动解压即可搜索嵌套文件。所有标准 ripgrep 功能均可用，包括正则表达式模式、彩色输出、上下文行和文件类型过滤，无论底层文件格式如何都提供一致的搜索界面。

当 tesseract 等可选依赖可用时，rga 还能对图像文件执行 OCR，让扫描文档也可被搜索。

# CONFIGURATION

**~/.cache/rga/**
> 缓存目录，存放从二进制文件格式提取的文本。可加速对相同文件的重复搜索。

**--rga-cache-max-blob-len**
> 控制缓存提取文本的最大文件大小。超过此阈值的文件在每次搜索时都会重新提取。

# CAVEATS

某些格式需要外部工具。大文件的首次搜索较慢。缓存会占用磁盘空间。

# HISTORY

**rga** 由 **phiresky** 创建，用于扩展 ripgrep 的搜索能力。它在保持 ripgrep 速度和界面的同时增加了文档格式支持。

# INSTALL

```brew: brew install rga```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rg](/man/rg)(1), [pdftotext](/man/pdftotext)(1), [grep](/man/grep)(1)
