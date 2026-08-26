# TAGLINE

通过命令行查询和转换数据文件

# TLDR

**读取并显示 CSV 文件**

```polars read [file.csv]```

**用 SQL 查询**

```polars sql "SELECT * FROM '[file.csv]' WHERE value > 100"```

**将 CSV 转换为 Parquet**

```polars convert [input.csv] [output.parquet]```

**显示文件的 schema**

```polars schema [file.parquet]```

**过滤并以 JSON 输出**

```polars sql "SELECT name, score FROM '[data.csv]' ORDER BY score DESC LIMIT 10" -o json```

**连接两个文件**

```polars sql "SELECT * FROM '[a.csv]' JOIN '[b.csv]' ON a.id = b.id"```

# SYNOPSIS

**polars** _command_ [_options_] [_args_...]

# COMMANDS

**read** _file_
> 读取并显示数据文件。

**sql** _query_
> 对文件执行 SQL 查询。

**schema** _file_
> 显示 schema/列信息。

**convert** _input_ _output_
> 在不同格式之间转换（CSV、Parquet、JSON、Arrow）。

# PARAMETERS

**-o**, **--output** _format_
> 输出格式：csv、json、parquet、table。

**--delimiter** _char_
> CSV 分隔符字符。

**--no-header**
> CSV 没有表头行。

**-n**, **--limit** _rows_
> 限制输出行数。

**-h**, **--help**
> 显示帮助信息。

**-V**, **--version**
> 显示版本信息。

# DESCRIPTION

**polars** 是 Polars 的命令行界面，Polars 是一个快速的 DataFrame 库。它无需编写代码即可对数据文件进行 SQL 查询和格式转换。

**sql** 命令直接对文件执行 SQL 查询。在查询中用引号将文件名作为表名引用。Polars 的查询引擎会针对大数据集优化执行。

支持的格式包括 CSV、Parquet、JSON 和 Arrow。**convert** 命令可在格式之间转换，适合从 CSV 源生成经过优化的 Parquet 文件。

Polars 内部使用 Apache Arrow 列式格式，能以极小的内存开销高效处理大数据集。查询优化包括谓词下推和投影下推。

# CAVEATS

该 CLI 只提供 Polars 库功能的一个子集。复杂的转换可能需要 Python 或 Rust API。超大文件更适合 Parquet 格式。其 SQL 方言与标准 SQL 存在一些差异。

# HISTORY

Polars 由 **Ritchie Vink** 于 **2020 年**创建，作为 pandas 的快速替代品。它用 Rust 编写并提供 Python 绑定，凭借性能优势迅速流行。这个 DataFrame 库利用 Apache Arrow 和惰性求值。CLI 工具的加入使其能够融入命令行数据工作流。Polars 已成为大规模数据分析的主流选择之一。

# SEE ALSO

[duckdb](/man/duckdb)(1), [xsv](/man/xsv)(1), [miller](/man/miller)(1)
