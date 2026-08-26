# TAGLINE

解析 RDF 数据并在不同格式间转换

# TLDR

**解析 RDF/XML 并输出为 N-Triples**

```rapper [input.rdf]```

**将 Turtle 转换为 RDF/XML**

```rapper -i turtle -o rdfxml [input.ttl]```

**将 RDF/XML 转换为 Turtle 格式**

```rapper -i rdfxml -o turtle [input.rdf]```

**统计 RDF 文件中的三元组数量**而不产生输出

```rapper -c [input.rdf]```

**从 URL 解析**

```rapper [https://example.org/data.rdf]```

**根据文件扩展名或内容猜测输入格式**

```rapper -g [input_file]```

**校验 RDF 而不产生输出**

```rapper -c -q [input.rdf]```

# SYNOPSIS

**rapper** [_options_] _INPUT-URI_ [_INPUT-BASE-URI_]

# PARAMETERS

**-i**, **--input** _FORMAT_
> 设置输入格式：rdfxml、ntriples、turtle、rss-tag-soup、rdfa、grddl、guess

**-o**, **--output** _FORMAT_
> 设置输出格式：ntriples（默认）、rdfxml、rdfxml-abbrev、turtle、rss-1.0、atom、dot、json、json-triples

**-c**, **--count**
> 只统计三元组数量，不产生输出

**-g**, **--guess**
> 根据 URI 或内容类型猜测解析器

**-q**, **--quiet**
> 抑制提示信息

**-e**, **--ignore-errors**
> 出错时继续解析

**-w**, **--ignore-warnings**
> 忽略警告消息

**-f**, **--feature** _FEATURE_
> 设置解析器/序列化器特性

**-v**, **--version**
> 打印版本并退出

**-h**, **--help**
> 显示帮助信息

# DESCRIPTION

**rapper** 是 Raptor RDF Parser Toolkit 提供的命令行工具，用于解析和序列化 RDF（Resource Description Framework，资源描述框架）数据。它读取各种格式的 RDF 内容，并以选定的序列化格式输出三元组。

该工具支持多种 RDF 语法，包括 RDF/XML、N-Triples、Turtle、RDFa 以及 RSS/Atom 订阅源。输入可以来自本地文件、标准输入（使用 '-'），或在 Raptor 构建时启用网络支持的情况下来自远程 URI。

常见用途包括在 RDF 序列化格式之间转换、校验 RDF 文件、统计三元组数量以进行分析，以及从包含 RDFa 标记的网页中提取 RDF 数据。

# CAVEATS

默认输入格式为 RDF/XML，默认输出格式为 N-Triples。在不同格式之间转换时务必用 **-i** 和 **-o** 明确指定格式。

大型 RDF 文件可能占用大量内存，因为某些序列化格式需要加载整个图。N-Triples 输出采用流式方式，内存效率更高。

某些功能取决于 Raptor 的编译方式。获取网络 URI 需要在构建时支持 libcurl 或类似的库。

# HISTORY

Raptor 由 **Dave Beckett** 于 **2000 年**起开发，是 Redland RDF 库项目的一部分。该工具包成为使用最广泛的 RDF 解析库之一，为许多语义网应用提供了基础。Raptor 这个名字是 "RDF Parser Toolkit for Redland" 的缩写。

# INSTALL

```apt: sudo apt install raptor2-utils```

```dnf: sudo dnf install raptor2```

```apk: sudo apk add raptor2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rdfproc](/man/rdfproc)(1), [redland](/man/redland)(3), [roqet](/man/roqet)(1)
