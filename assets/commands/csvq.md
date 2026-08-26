# TAGLINE

面向 CSV 文件的 SQL 查询引擎

# TLDR

用 SQL 查询 CSV 文件

```csvq "SELECT * FROM [data.csv]"```

用 WHERE 过滤行

```csvq "SELECT * FROM [data.csv] WHERE [column] = '[value]'"```

聚合数据

```csvq "SELECT [category], COUNT(*) FROM [data.csv] GROUP BY [category]"```

连接多个 CSV 文件

```csvq "SELECT * FROM [a.csv] JOIN [b.csv] ON [a.id] = [b.id]"```

对结果排序

```csvq "SELECT * FROM [data.csv] ORDER BY [column] DESC"```

输出为 JSON

```csvq -f json "SELECT * FROM [data.csv]"```

通过管道从 stdin 读取

```cat [data.csv] | csvq "SELECT * FROM STDIN"```

启动交互模式

```csvq```

# SYNOPSIS

**csvq** [_options_] [_query_]

# PARAMETERS

**-f**, **--format** _format_
> 输出格式：CSV、TSV、FIXED、JSON、JSONL、LTSV、GFM、ORG、BOX、TEXT（默认：TEXT）。

**-d**, **--delimiter** _char_
> 字段分隔符（默认：逗号）。

**-o**, **--out** _file_
> 输出到文件而不是 stdout。

**-e**, **--encoding** _encoding_
> 输入文件编码（AUTO、UTF8、UTF8M、UTF16、SJIS 等）。

**-n**, **--no-header**
> 将第一行视为数据；字段自动命名为 c1、c2 等。

**-N**, **--without-header**
> 导出结果时不带表头行。

**-l**, **--line-break** _type_
> 输出换行类型：CRLF、CR、LF（默认：LF）。

**-E**, **--write-encoding** _encoding_
> 输出文件编码。

**-s**, **--source** _file_
> 从文件加载查询语句。

**-r**, **--repository** _path_
> 存放数据文件的目录（默认：当前目录）。

**-q**, **--quiet**
> 抑制操作日志消息。

**-P**, **--pretty-print**
> 对 JSON 输出进行美化打印。

# DESCRIPTION

**csvq** 是一款可以对 CSV 文件执行 SQL 查询的命令行工具。它把 CSV 文件当作数据库表，支持 SELECT、INSERT、UPDATE、DELETE 以及带 JOIN、子查询和聚合函数的复杂查询。

列名来自 CSV 表头行（无表头文件也可另行指定）。支持标准 SQL 语法，包括 WHERE、GROUP BY、HAVING、ORDER BY、LIMIT、UNION 和窗口函数。

多个 CSV 文件可以通过 JOIN 一起查询。结果可以多种格式输出，包括 CSV、JSON 和格式化表格，因此很适合数据转换管道。

# SQL FEATURES

**聚合函数**: COUNT, SUM, AVG, MIN, MAX
**字符串**: CONCAT, SUBSTR, UPPER, LOWER, TRIM
**日期**: NOW, DATETIME, DATE_FORMAT
**条件**: CASE, IF, COALESCE, NULLIF
**窗口函数**: ROW_NUMBER, RANK, LAG, LEAD

# CAVEATS

大型 CSV 文件会被整体载入内存。与真正的数据库相比，在大文件上运行复杂查询可能较慢。含空格或特殊字符的列名需要加引号。该工具是单线程的。

# HISTORY

csvq 由 **Mithrandie** 创建，是以 Go 编写的开源项目。它的设计目标是将 SQL 的易用性带到临时性的 CSV 数据分析中，填补 awk 等简单命令行工具与完整数据库导入之间的空白。该项目持续维护，定期更新并不断增加 SQL 特性。

# INSTALL

```apk: sudo apk add csvq```

```brew: brew install csvq```

```nix: nix profile install nixpkgs#csvq```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[q](/man/q)(1), [textql](/man/textql)(1), [sqlite3](/man/sqlite3)(1), [miller](/man/miller)(1)
