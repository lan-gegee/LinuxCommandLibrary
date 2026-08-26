# TAGLINE

将各种格式的表格数据转换为 CSV

# TLDR

**将 Excel 转换为 CSV**

```in2csv [data.xlsx] > [output.csv]```

**转换特定工作表**

```in2csv --sheet [Sheet1] [data.xlsx]```

**将 JSON 转换为 CSV**

```in2csv [data.json] > [output.csv]```

**指定输入格式**

```in2csv -f [xlsx|json|ndjson] [input]```

**转换固定宽度文件**

```in2csv -f fixed -s [schema.csv] [data.txt]```

# SYNOPSIS

**in2csv** [_options_] _file_

# PARAMETERS

**-f** _FORMAT_
> 输入格式（csv、xlsx、xls、json、ndjson、fixed）。

**--sheet** _NAME_
> Excel 文件的工作表名称。

**-s** _SCHEMA_
> 固定宽度输入的模式文件。

**-H**, **--no-header-row**
> 输入没有标题行。

**-K** _N_
> 跳过开头的 N 行。

**--help**
> 显示帮助信息。

# DESCRIPTION

**in2csv** 将各种格式的表格数据转换为 CSV。它是用于处理 CSV 文件的 csvkit 工具集的一员。

该工具可处理 Excel、JSON、固定宽度等多种格式。它支持将数据通过管道传给其他 csvkit 工具进行分析。

# CAVEATS

属于 csvkit。基于 Python。大文件可能较慢。

# HISTORY

in2csv 是 **csvkit** 的一部分，由 **Christopher Groskopf** 为记者和数据分析人员创建。

# SEE ALSO

[csvcut](/man/csvcut)(1), [csvlook](/man/csvlook)(1), [csvstat](/man/csvstat)(1), [csvsql](/man/csvsql)(1)
