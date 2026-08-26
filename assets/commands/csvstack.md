# TAGLINE

垂直拼接 CSV 文件

# TLDR

**堆叠多个 CSV 文件**

```csvstack [file1.csv] [file2.csv] > [combined.csv]```

**添加分组列以标识来源文件**

```csvstack -g [source1,source2] [file1.csv] [file2.csv]```

**为分组列命名**

```csvstack -g [a,b] -n [source] [file1.csv] [file2.csv]```

**自动以文件名作为分组值**

```csvstack --filenames [file1.csv] [file2.csv]```

**堆叠没有表头行的文件**

```csvstack -H [file1.csv] [file2.csv]```

**堆叠分号分隔的文件**

```csvstack -d ";" [file1.csv] [file2.csv]```

# SYNOPSIS

**csvstack** [_options_] _files_...

# DESCRIPTION

**csvstack** 将多个 CSV 文件垂直（按行）拼接在一起。它是 csvkit 的一部分，会按表头名对齐各列，并可添加一个分组列来记录数据来源文件。

该工具通过匹配表头名来处理列顺序不同的文件，因此在合并来自不同来源的数据集时非常稳健。

# PARAMETERS

**-g** _names_
> 添加带有指定值的分组列。

**-n** _name_
> 分组列的名称。

**-H**, **--no-header-row**
> 输入没有表头行。

**--filenames**
> 用文件名作为分组值。

**-d** _char_
> 字段分隔符。

**-q** _char_
> 引号字符。

**-e** _encoding_
> 输入编码。

# CAVEATS

要获得整洁的输出，所有文件应具有匹配的列。缺失的列将以空值填充。属于 csvkit，需要 Python 环境。若表头不同，则使用第一个文件的表头。

# HISTORY

**csvstack** 是 **csvkit** 的组成部分，由 **Christopher Groskopf** 于 **2011 年**创建。它简化了合并多个数据文件的操作——这是数据处理与分析流程中常见的任务。

# SEE ALSO

[csvcut](/man/csvcut)(1), [csvlook](/man/csvlook)(1), [csvjoin](/man/csvjoin)(1), [csvgrep](/man/csvgrep)(1), [csvstat](/man/csvstat)(1)
