# TAGLINE

对 CSV、JSON、LTSV、YAML 和 TBLN 文件执行 SQL 查询

# TLDR

查询 CSV

```trdsql "SELECT * FROM [file.csv]"```

查询 JSON

```trdsql -ijson "SELECT * FROM [file.json]"```

输出为 JSON

```trdsql -ojson "SELECT * FROM [file.csv]"```

带表头

```trdsql -ih "SELECT name FROM [file.csv]"```

连接多个文件

```trdsql "SELECT * FROM [a.csv] JOIN [b.csv] ON [a.id]=[b.id]"```

查询 LTSV

```trdsql -iltsv "SELECT * FROM [file.ltsv]"```

输出为 Markdown 表格

```trdsql -omd "SELECT * FROM [file.csv]"```

查询 YAML

```trdsql -iyaml "SELECT * FROM [file.yaml]"```

# SYNOPSIS

**trdsql** [_-i format_] [_-o format_] [_options_] _query_

# PARAMETERS

**-i** _FORMAT_
> 输入格式 (csv, json, ltsv, yaml, tbln)。

**-o** _FORMAT_
> 输出格式 (csv, json, jsonl, ltsv, raw, md, at, vf, tbln)。

**-ih**
> 输入包含表头行。

**-oh**
> 输出带表头。

**-id** _DELIM_
> 输入分隔符字符。

**-od** _DELIM_
> 输出分隔符字符。

**-driver** _DRIVER_
> 数据库驱动 (sqlite3, postgres, mysql)。

**-dsn** _DSN_
> 数据库连接字符串。

**-debug**
> 显示调试输出。

# DESCRIPTION

**trdsql** 可以直接对 CSV、JSON、LTSV、YAML 和 TBLN 等结构化数据文件执行 SQL 查询，无需先将它们导入数据库。文件名可直接用作 SQL 语句中的表名，让你用熟悉的 SQL 语法轻松完成数据的过滤、聚合和转换。

该工具支持跨多个文件连接数据，只需一条命令即可在不同数据源之间执行关系型查询。输入和输出格式可以独立指定，因此查询的同时还能顺带完成格式转换。

在底层，trdsql 默认使用 SQLite 作为查询引擎，但也可以连接 PostgreSQL 和 MySQL 以使用更高级的 SQL 特性。配合 **-ih** 标志，CSV 文件的表头可用作列名。

# CAVEATS

基于 Go 的工具。大文件会被载入内存。需要具备 SQL 知识。默认数据库引擎为 SQLite。

# HISTORY

**trdsql** 的设计目的是对 CSV 和 JSON 等各种结构化数据格式执行 SQL 查询。

# INSTALL

```brew: brew install trdsql```

```nix: nix profile install nixpkgs#trdsql```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[textql](/man/textql)(1), [q](/man/q)(1), [miller](/man/miller)(1)
