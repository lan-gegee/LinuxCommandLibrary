# TAGLINE

按列值过滤 CSV 行的工具

# TLDR

**按列匹配值过滤行**

```csvgrep -c [column] -m "[value]" [data.csv]```

**使用正则表达式过滤**

```csvgrep -c [column] -r "[pattern]" [data.csv]```

**按列序号而非名称过滤**

```csvgrep -c [1] -m "[value]" [data.csv]```

**反转匹配**（排除匹配的行）

```csvgrep -c [column] -m "[value]" -i [data.csv]```

**同时匹配多个列**

```csvgrep -c "[col1,col2]" -m "[value]" [data.csv]```

不区分大小写匹配

```csvgrep -c [column] -r "(?i)[pattern]" [data.csv]```

# SYNOPSIS

**csvgrep** [_options_] _file_

# PARAMETERS

**-c** _COLUMN_, **--columns** _COLUMN_
> 要搜索的列名或列序号（多列用逗号分隔）。

**-m** _STRING_, **--match** _STRING_
> 要搜索的确切字符串。

**-r** _REGEX_, **--regex** _REGEX_
> 用于匹配的正则表达式。

**-f** _FILE_, **--file** _FILE_
> 存放待匹配值的文件（每行一个）。

**-i**, **--invert-match**
> 选择不匹配的行。

**-a**, **--any-match**
> 任一列匹配即算匹配（用于多列场景）。

**-d** _CHAR_, **--delimiter** _CHAR_
> 字段分隔符（默认：逗号）。

**-e** _ENCODING_, **--encoding** _ENCODING_
> 输入文件编码。

# DESCRIPTION

**csvgrep** 是 csvkit 的组成部分，根据列值过滤 CSV 行。与标准 grep 不同，它理解 CSV 结构，可以针对特定列进行匹配，同时保持输出仍是合法的 CSV。

该工具同时支持精确字符串匹配和正则表达式。可以搜索多个列，还可以反转匹配语义以排除行。这使它成为按条件抽取数据子集的理想选择。

csvgrep 能正确处理带引号的字段，确保字段内的逗号不会破坏搜索。结果包含表头行，维持合法的 CSV 结构。

# CAVEATS

正则表达式采用 Python 语法。列名区分大小写。由于要处理整个文件，大文件可能较慢。某些操作的内存占用会随文件大小增长。

# HISTORY

csvgrep 是 **csvkit** 的一部分，由 Christopher Groskopf 于 **2011** 年创建。它提供感知 CSV 结构的 grep 式功能，解决了在不破坏内嵌分隔符的前提下搜索表格数据的常见难题。

# SEE ALSO

[csvcut](/man/csvcut)(1), [csvsort](/man/csvsort)(1), [grep](/man/grep)(1), [csvkit](/man/csvkit)(1)

# RESOURCES

```[Source code](https://github.com/wireservice/csvkit)```

```[Documentation](https://csvkit.readthedocs.io)```

<!-- verified: 2026-06-26 -->
