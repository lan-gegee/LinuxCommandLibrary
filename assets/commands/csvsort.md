# TAGLINE

感知数据类型的 CSV 文件排序工具

# TLDR

按列排序

```csvsort -c [column] [data.csv]```

降序排序

```csvsort -r -c [column] [data.csv]```

按多列排序

```csvsort -c [col1,col2] [data.csv]```

按数值排序

```csvsort -c [amount] [data.csv]```

无表头时排序

```csvsort -H -c [1] [data.csv]```

从 stdin 读取

```cat [data.csv] | csvsort -c [name]```

# SYNOPSIS

**csvsort** [_options_] _file_

# DESCRIPTION

**csvsort** 按一列或多列对 CSV 文件排序。它是 csvkit 的一员，能正确处理 CSV 引号和数据类型，自动识别数字和日期值并进行合适的排序。

该工具在排序过程中维持 CSV 结构，正确保留表头和带引号的字段。

# PARAMETERS

**-c** _columns_
> 用于排序的列。

**-r**, **--reverse**
> 降序排序。

**-H**, **--no-header-row**
> 输入没有表头。

**-d** _char_
> 字段分隔符。

**-q** _char_
> 引号字符。

**-e** _encoding_
> 输入编码。

**-y** _n_
> 用于探测类型的行数。

# CAVEATS

需要把整个文件载入内存。属于 csvkit，需要 Python 环境。类型检测结果不一定总符合预期。大文件可能较慢。

# HISTORY

**csvsort** 是 **csvkit** 的一部分，由 **Christopher Groskopf** 于 **2011** 年创建。它提供类型感知的排序能力，这是 Unix sort 命令处理 CSV 数据时难以轻易做到的。

# SEE ALSO

[csvcut](/man/csvcut)(1), [csvlook](/man/csvlook)(1), [sort](/man/sort)(1), [csvstat](/man/csvstat)(1)

# RESOURCES

```[Source code](https://github.com/wireservice/csvkit)```

```[Documentation](https://csvkit.readthedocs.io)```

<!-- verified: 2026-06-26 -->
