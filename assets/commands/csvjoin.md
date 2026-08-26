# TAGLINE

面向 CSV 文件的 SQL 风格连接工具

# TLDR

基于公共列连接**两个 CSV 文件**

```csvjoin -c [id] [file1.csv] [file2.csv]```

两个文件使用不同的列名进行连接

```csvjoin -c "[id1,id2]" [file1.csv] [file2.csv]```

执行左外连接

```csvjoin --left -c [id] [file1.csv] [file2.csv]```

执行右外连接

```csvjoin --right -c [id] [file1.csv] [file2.csv]```

执行全外连接

```csvjoin --outer -c [id] [file1.csv] [file2.csv]```

基于多列连接

```csvjoin -c "[col1,col2]" [file1.csv] [file2.csv]```

# SYNOPSIS

**csvjoin** [_options_] _file1_ _file2_

# PARAMETERS

**-c** _COLUMN_, **--columns** _COLUMN_
> 用于连接的列。两文件列名不同时用逗号分隔。

**--left**
> 执行左外连接（保留第一个文件的所有行）。

**--right**
> 执行右外连接（保留第二个文件的所有行）。

**--outer**
> 执行全外连接（保留两个文件的所有行）。

**-d** _CHAR_, **--delimiter** _CHAR_
> 字段分隔符（默认：逗号）。

**-e** _ENCODING_, **--encoding** _ENCODING_
> 输入文件编码。

**-H**, **--no-inference**
> 禁用类型推断。

**--no-header-row**
> 文件没有表头行。

# DESCRIPTION

**csvjoin** 是 csvkit 的组成部分，对 CSV 文件执行 SQL 风格的连接。它基于指定列中的匹配值合并两个文件的数据，类似于数据库中的 JOIN 操作。

默认是内连接，只返回两个文件中都有匹配的行。左连接、右连接和全外连接会保留来自其中一个或两个文件的未匹配行，缺失值以空字符串填充。

当连接列的名称不同时，需用逗号分隔指定两个名称。也可以使用多列作为复合键，实现更复杂的连接。

# CAVEATS

连接时两个文件都必须能装入内存。列匹配是精确比较；建议先清理数据。连接列大量不匹配会产生笛卡尔积。输出列顺序为先第一个文件再第二个文件。

# HISTORY

csvjoin 是 **csvkit** 的一部分，由 Christopher Groskopf 于 **2011** 年创建。它把数据库风格的连接操作带到了命令行 CSV 处理中，无需导入数据库即可完成数据合并。

# SEE ALSO

[csvstack](/man/csvstack)(1), [csvsql](/man/csvsql)(1), [join](/man/join)(1), [csvkit](/man/csvkit)(1)

# RESOURCES

```[Source code](https://github.com/wireservice/csvkit)```

```[Documentation](https://csvkit.readthedocs.io)```

<!-- verified: 2026-06-26 -->
