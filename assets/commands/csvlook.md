# TAGLINE

供终端查看的 CSV 表格渲染工具

# TLDR

**将 CSV 显示为表格**

```csvlook [data.csv]```

限制显示的行数

```csvlook --max-rows [10] [data.csv]```

限制列宽

```csvlook --max-column-width [20] [data.csv]```

隐藏行号

```csvlook --no-number [data.csv]```

使用其他分隔符

```csvlook -d ";" [data.csv]```

从 stdin 读取

```cat [data.csv] | csvlook```

# SYNOPSIS

**csvlook** [_options_] _file_

# DESCRIPTION

**csvlook** 将 CSV 数据渲染成定宽表格供终端查看。它是 csvkit 的一部分，提供了一种快速预览 CSV 文件的可读方式。

该工具根据内容自动调整列宽，并使用 ASCII 边框显示数据，便于检查数据结构和取值。

# PARAMETERS

**-H**, **--no-header-row**
> 输入没有表头行。

**--max-rows** _n_
> 最大显示行数。

**--max-column-width** _n_
> 列在该宽度处截断。

**--max-columns** _n_
> 最大显示列数。

**-y** _n_, **--snifflimit** _n_
> 用于探测分隔符的行数。

**--no-number**
> 不显示行号。

**-d** _char_
> 字段分隔符。

**-q** _char_
> 引号字符。

**-e** _encoding_
> 输入编码。

# CAVEATS

大文件渲染可能较慢。宽表格在终端中可能会折行。属于 csvkit，需要安装 Python。

# HISTORY

**csvlook** 是 **csvkit** 的一部分，由 **Christopher Groskopf** 于 **2011** 年创建。它提供的快速数据预览能力是数据分析工作流中不可或缺的一环，与 csvkit 其他 CSV 处理工具相辅相成。

# SEE ALSO

[csvcut](/man/csvcut)(1), [csvstat](/man/csvstat)(1), [column](/man/column)(1), [less](/man/less)(1)

# RESOURCES

```[Source code](https://github.com/wireservice/csvkit)```

```[Documentation](https://csvkit.readthedocs.io)```

<!-- verified: 2026-06-26 -->
