# TAGLINE

CSV 列选择与重排工具

# TLDR

**选择指定列**

```csvcut -c [1,3,5] [data.csv]```

**按名称选择列**

```csvcut -c [name,email] [data.csv]```

**排除列**

```csvcut -C [column] [data.csv]```

**使用其他分隔符**

```csvcut -d ";" -c [1,2] [data.csv]```

**选择列范围**

```csvcut -c [1-5] [data.csv]```

**从 stdin 读取**

```cat [data.csv] | csvcut -c [name]```

# SYNOPSIS

**csvcut** [_options_] _file_

# DESCRIPTION

**csvcut** 是 csvkit（一套 CSV 处理工具）的组成部分。它从 CSV 文件中选取并重排列，功能类似 cut，但能正确处理 CSV 格式（包括带引号的字段）。

该工具能正确处理 CSV 的各种边界情况，例如带引号字段内嵌的逗号和换行符，因此在处理结构化数据时比基于纯文本的工具更可靠。

# PARAMETERS

**-c** _columns_
> 要选取的列（名称或序号）。

**-C** _columns_
> 要排除的列。

**-d** _char_
> 字段分隔符。

**-t** _char_
> 制表符分隔符快捷方式。

**-q** _char_
> 引号字符。

**-e** _encoding_
> 输入文件编码。

**-n**
> 显示列名及其序号。

**-l**
> 插入行号列。

**--no-header-row**
> 输入没有表头行。

# CAVEATS

属于 csvkit，需要 Python 环境。列序号从 1 开始。与原生工具相比，大文件处理可能较慢。内存占用随文件大小增长。

# HISTORY

**csvcut** 是 **csvkit** 的一部分，由 **Christopher Groskopf** 于 **2011** 年创建。这套工具为数据新闻和分析提供可靠的 CSV 处理能力，弥补了传统 Unix 文本工具在结构化数据方面的不足。

# SEE ALSO

[csvlook](/man/csvlook)(1), [csvstat](/man/csvstat)(1), [cut](/man/cut)(1), [awk](/man/awk)(1)

# RESOURCES

```[Source code](https://github.com/wireservice/csvkit)```

```[Documentation](https://csvkit.readthedocs.io)```

<!-- verified: 2026-06-26 -->
