# TAGLINE

快速的 CSV 命令行工具集

# TLDR

**显示 CSV 表头**

```xsv headers [file.csv]```

**选择特定列**

```xsv select [Name,Age] [file.csv]```

**将 CSV 格式化为对齐的表格**

```xsv table [file.csv]```

**获取所有列的统计信息**

```xsv stats [file.csv]```

在 CSV 中**搜索匹配模式**

```xsv search "[pattern]" [file.csv]```

**按列排序**

```xsv sort -s [column] [file.csv]```

**统计行数**

```xsv count [file.csv]```

**随机抽样若干行**

```xsv sample [10] [file.csv]```

# SYNOPSIS

**xsv** _command_ [_options_] [_input_]

# PARAMETERS

**cat**
> 按行或按列连接 CSV 文件。

**count**
> 统计 CSV 文件的行数。

**fixlengths**
> 强制所有行具有相同的长度。

**flatten**
> 将每一行显示为单行。

**fmt**
> 格式化 CSV 输出（分隔符、引号）。

**frequency**
> 显示各列的频率表。

**headers**
> 显示列标题。

**index**
> 创建索引以支持快速随机访问。

**input**
> 以特殊方式读取 CSV 数据。

**join**
> 按某一列连接两个 CSV 文件。

**sample**
> 随机抽取行样本。

**search**
> 搜索匹配正则表达式的行。

**select**
> 选择特定列。

**slice**
> 从 CSV 中切取部分行。

**sort**
> 按列排序行。

**split**
> 将 CSV 拆分为多个文件。

**stats**
> 计算各列的统计信息。

**table**
> 格式化为对齐的 ASCII 表格。

**-d**, **--delimiter** _char_
> 字段分隔符（默认：逗号）。

**--no-headers**
> 输入没有标题行。

**-o**, **--output** _file_
> 将输出写入文件。

# DESCRIPTION

**xsv** 是一个用 Rust 编写的高速 CSV 命令行工具集。它提供索引用于索引、切片、分析、拆分和连接 CSV 文件的命令，在大数据集上表现出色。

该工具通过创建索引实现快速随机访问和统计收集。各命令设计为可通过 Unix 管道组合使用，同时保持高性能。

xsv 能处理各种 CSV 方言，支持不同的分隔符、引号风格以及带或不带标题行的文件。

# CAVEATS

xsv 针对格式规范的 CSV 文件优化。格式错误的输入可能产生意外结果。先用 **xsv index** 创建索引可显著加速后续对大文件的操作。

# HISTORY

xsv 由 **Andrew Gallant**（BurntSushi）创建，于 **2014 年**首次发布。它最初是为了展示 Rust 在命令行工具和 CSV 处理方面的性能潜力而开发的。该项目影响了其他 Rust CSV 工具的设计，并确立了高性能 CSV 处理的模式。

# INSTALL

```pacman: sudo pacman -S xsv```

```apk: sudo apk add xsv```

```zypper: sudo zypper install xsv```

```brew: brew install xsv```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[csvkit](/man/csvkit)(1), [miller](/man/miller)(1), [awk](/man/awk)(1), [cut](/man/cut)(1)
