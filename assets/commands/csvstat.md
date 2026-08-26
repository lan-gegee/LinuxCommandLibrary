# TAGLINE

CSV 列描述性统计计算器

# TLDR

**显示**所有列的**统计信息**

```csvstat [data.csv]```

特定列的**统计信息**

```csvstat -c [column1,column2] [data.csv]```

只显示某项统计值

```csvstat --mean -c [column] [data.csv]```

统计唯一值数量

```csvstat --unique -c [column] [data.csv]```

显示值的频次

```csvstat --freq -c [column] [data.csv]```

显示数据类型

```csvstat --type [data.csv]```

以 JSON 格式输出统计结果

```csvstat --json [data.csv]```

显示列名和列序号

```csvstat -n [data.csv]```

# SYNOPSIS

**csvstat** [_options_] _file_

# DESCRIPTION

**csvstat** 计算 CSV 文件中各列的描述性统计信息。它是 csvkit 的一部分，会自动检测数据类型并给出相应的统计数据。

该工具报告计数、唯一值、最小值/最大值、均值、中位数、标准差以及高频值，可快速概览数据特征。

# PARAMETERS

**-c** _columns_
> 要分析的列。

**--type**
> 只显示各列的数据类型。

**--unique**
> 只显示唯一值的数量。

**--min**
> 只显示最小值。

**--max**
> 只显示最大值。

**--mean**
> 只显示均值。

**--median**
> 只显示中位数。

**--stdev**
> 只显示标准差。

**--freq**
> 只显示高频值。

**--count**
> 只显示行数。

**--sum**
> 只显示总和。

**--len**
> 只显示最大字符串长度。

**--nulls**
> 只显示空值数量。

**--csv**
> 以 CSV 表格形式输出结果。

**--json**
> 以 JSON 形式输出结果。

**-n**
> 只显示列名和列序号。

**-d** _char_
> 字段分隔符。

**-e** _encoding_
> 输入文件的字符编码。

**-y** _n_
> 类型检测的嗅探行数上限（0 表示禁用）。

**-I**
> 禁用类型推断；将所有列视为文本。

# CAVEATS

会将整个文件载入内存。大文件处理可能较慢。类型检测可能误判混合数据。属于 csvkit，需要 Python 环境。

# HISTORY

**csvstat** 是 **csvkit** 的组成部分，由 **Christopher Groskopf** 于 **2011 年**创建。它把类似 pandas 的汇总统计带到了命令行，是数据初探与校验的必备工具。

# SEE ALSO

[csvcut](/man/csvcut)(1), [csvlook](/man/csvlook)(1), [csvclean](/man/csvclean)(1), [wc](/man/wc)(1)
