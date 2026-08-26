# TAGLINE

支持多种数据库的交互式 SQL 客户端

# TLDR

**连接到数据库**

```rsql --url [postgres://user:pass@host/db]```

**执行查询**

```rsql --url [postgres://user:pass@host/db] -c "[SELECT * FROM users]"```

**运行 SQL 文件**

```rsql --url [postgres://user:pass@host/db] -f [query.sql]```

**以 CSV 格式输出**

```rsql --url [postgres://user:pass@host/db] -c "[query]" --csv```

**以 JSON 格式输出**

```rsql --url [postgres://user:pass@host/db] -c "[query]" --json```

# SYNOPSIS

**rsql** [**--url** _url_] [_-c query_ | _-f file_] [_options_]

# PARAMETERS

**--url** _URL_
> 数据库连接 URL（例如 `postgres://user:pass@host/db`、`mysql://...`、`sqlite://path`）。

**-c**, **--commands** _QUERY_
> 执行一条或多条以分号分隔的 SQL 命令后退出。

**-f**, **--file** _FILE_
> 执行 SQL 脚本文件中的命令后退出。

**--format** _FORMAT_
> 输出格式：ascii、csv、expanded、html、json、jsonl、markdown、plain、psql、sqlite、tsv、unicode、xml、yaml。

**--csv**
> `--format csv` 的简写。

**--json**
> `--format json` 的简写。

**--color** _WHEN_
> 是否给输出着色：always、auto 或 never。

**--theme** _THEME_
> 语法高亮主题（例如 solarized-dark、base16-ocean.dark）。

**--echo** _MODE_
> 执行前回显命令：on、off、prompt。

**--timer**
> 打印每条命令的耗时。

**--history**
> 启用命令历史记录。

**--help**
> 显示帮助信息。

**--version**
> 显示版本信息。

# DESCRIPTION

**rsql** 是一个用 Rust 编写的命令行 SQL 客户端，为连接众多数据库引擎提供统一界面，包括 PostgreSQL、MySQL、MariaDB、SQLite、DuckDB、Redshift、Snowflake、SQL Server 等。它同时支持用于探索式查询的交互模式，以及在脚本中运行 SQL 文件和单条命令的批处理模式。

输出可以格式化为 CSV、JSON、Markdown、HTML 或排版整齐的表格，因此既适合人工阅读，也便于接入数据管道。**--url** 标志指定数据库连接 URL；**-c** 直接执行查询，**-f** 则对指定的数据库运行 SQL 文件。

# CAVEATS

必须提供连接字符串。需要相应的数据库驱动。基于 Rust 的工具。

# HISTORY

**rsql** 是一个用 Rust 编写的命令行 SQL 客户端，为多种数据库类型提供统一的使用界面。

# INSTALL

```brew: brew install rsql```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[psql](/man/psql)(1), [mysql](/man/mysql)(1), [sqlite3](/man/sqlite3)(1)
