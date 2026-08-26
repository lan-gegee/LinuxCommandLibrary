# TAGLINE

分析 PDF 文件结构

# TLDR

**解析 PDF 结构**

```pdf-parser [file.pdf]```

**搜索关键字**

```pdf-parser -s [keyword] [file.pdf]```

**显示指定对象**

```pdf-parser -o [5] [file.pdf]```

**提取流**

```pdf-parser -d [output.bin] -o [5] [file.pdf]```

**显示统计信息**

```pdf-parser -a [file.pdf]```

**按对象类型过滤**

```pdf-parser -t [/JavaScript] [file.pdf]```

**解码流**

```pdf-parser -f [file.pdf]```

# SYNOPSIS

**pdf-parser** [_-s search_] [_-o id_] [_-t type_] [_-f_] [_options_] _file_

# PARAMETERS

**-s** _STRING_
> 搜索字符串。

**-o** _ID_
> 按 ID 选择对象。

**-t** _TYPE_
> 按类型过滤。

**-f**
> 应用流过滤器。

**-d** _FILE_
> 将流转储到文件。

**-a**
> 统计与分析。

**-w**
> 原始输出。

**-r** _N_
> 引用对象。

**-c**
> 内容流。

**-v**
> 详细输出。

# DESCRIPTION

**pdf-parser** 分析 PDF 文件结构。用于恶意软件分析和取证。

对象枚举显示所有 PDF 对象。每个对象的类型和内容都会展示。

搜索可找出嵌入的脚本、URL 或可疑内容。JavaScript 和启动动作是常见的恶意软件载体。

流提取会转储压缩或编码的数据。过滤器可解压 FlateDecode 及其他编码。

统计信息汇总现有对象的类型。这能快速识别结构异常的文件。

引用跟踪可梳理对象间的关系。交叉引用揭示文档结构。

# CAVEATS

恶意 PDF 可能使解析器崩溃。输出可能非常大。并非支持所有 PDF 特性。

# HISTORY

**pdf-parser** 由 **Didier Stevens** 为 PDF 恶意软件分析而创建。它是他分析可疑文档工具集的一部分，广泛用于事件响应。

# INSTALL

```nix: nix profile install nixpkgs#pdf-parser```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pdfinfo](/man/pdfinfo)(1), [pdftotext](/man/pdftotext)(1), [pdfid](/man/pdfid)(1), [strings](/man/strings)(1)
