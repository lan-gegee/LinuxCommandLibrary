# TAGLINE

面向 CSV 文件的交互式 Python shell

# TLDR

在 Python shell 中打开 CSV 文件

```csvpy [data.csv]```

以制表符为分隔符打开

```csvpy -t [data.tsv]```

加载为 agate Table 以便分析

```csvpy --agate [data.csv]```

加载为 DictReader（每行为字典）

```csvpy --dict [data.csv]```

以自定义编码打开

```csvpy -e [latin1] [data.csv]```

打开无表头的文件

```csvpy -H [data.csv]```

以自定义分隔符打开

```csvpy -d "[;]" [data.csv]```

# SYNOPSIS

**csvpy** [_options_] _file_

# PARAMETERS

_FILE_
> 要载入 Python 环境的 CSV 文件。也接受来自 stdin 的管道输入。

**-d** _CHAR_, **--delimiter** _CHAR_
> 字段分隔符（默认：逗号）。

**-t**, **--tabs**
> 使用制表符作为字段分隔符。

**-q** _CHAR_, **--quotechar** _CHAR_
> 用于给字段加引号的字符。

**-e** _ENCODING_, **--encoding** _ENCODING_
> 指定输入文件编码（如 utf-8、latin1）。

**-H**, **--no-header-row**
> 表明文件没有表头行。

**-K** _N_, **--skip-lines** _N_
> 处理前先跳过输入的前 N 行。

**--agate**
> 将文件加载为 agate Table 而非 csv.reader 对象。数据可通过名为 **table** 的变量访问。

**--dict**
> 加载为 csv.DictReader，每一行都是一个以列名作为键的字典。

**-I**, **--no-inference**
> 与 --agate 一起使用时禁用类型推断，所有值保持为字符串。

**-S**
> 禁用 CSV 方言探测。

**--blanks**
> 不把空字符串转换为 None。

**--null-value** _VALUES_
> 将指定值转换为 None（可指定多个）。

**-y** _N_, **--sniff-limit** _N_
> 限制用于 CSV 方言探测的字节数。

**-l**, **--linenumbers**
> 在输出开头插入一列行号。

**-z** _N_, **--field-size-limit** _N_
> 输入 CSV 中单个字段的最大长度。

**-V**, **--version**
> 显示版本信息。

# DESCRIPTION

**csvpy** 是 csvkit 的组成部分，可将 CSV 文件载入交互式 Python shell 进行探索和分析。如果安装了 IPython，它会用 IPython 作为 shell 以获得更丰富的体验。

默认模式下，CSV 数据被载入名为 **reader** 的变量，这是一个 csv.reader 对象。使用 **--dict** 时，它变成 DictReader，每行是一个字典。使用 **--agate** 时，它变成功能完备的 **table** 变量，支持排序、过滤和聚合等分析操作。

这款工具适合快速探索数据、测试数据转换以及编写分析原型。交互式环境让你在处理数据时能立即得到反馈。

# CAVEATS

整体加载大文件可能占用大量内存。默认的 csv.reader 迭代一次即耗尽；需要重复使用数据时请用 **--agate**。要高效使用需要熟悉 Python。

# HISTORY

**csvpy** 是 **csvkit** 的一部分，由 Christopher Groskopf 于 **2011** 年创建。它让用户可以免于编写样板式的文件加载代码，直接进入 Python 做临时数据分析。

# SEE ALSO

[csvkit](/man/csvkit)(1), [csvlook](/man/csvlook)(1), [csvstat](/man/csvstat)(1), [csvcut](/man/csvcut)(1), [csvgrep](/man/csvgrep)(1), [python](/man/python)(1), [ipython](/man/ipython)(1)
