# TAGLINE

嵌入式分析型数据库引擎

# TLDR

**启动交互式 SQL shell**

```duckdb```

**打开或创建数据库文件**

```duckdb [path/to/database.db]```

**执行 SQL 查询后退出**

```duckdb -c "[SELECT * FROM table_name]"```

**直接查询 CSV 文件**

```duckdb -c "[SELECT * FROM 'data.csv']"```

**查询 Parquet 文件**

```duckdb -c "[SELECT * FROM 'data.parquet']"```

**从文件执行 SQL**

```duckdb -f [path/to/script.sql]```

**将查询结果导出为 CSV**

```duckdb -csv -c "[COPY (SELECT * FROM table) TO 'output.csv' (HEADER)]"```

**以只读模式启动**

```duckdb -readonly [database.db]```

**以 JSON 格式输出结果**

```duckdb -json -c "[SELECT * FROM 'data.csv' LIMIT 10]"```

# SYNOPSIS

**duckdb** [_options_] [_database_file_] [_sql_commands_]

# PARAMETERS

**-c** _COMMAND_
> 执行指定的 SQL 命令并退出。

**-s** _COMMAND_
> 执行指定的 SQL 语句并退出（**-c** 的别名）。

**-cmd** _COMMAND_
> 在读取标准输入之前运行命令。

**-f** _FILENAME_
> 从文件执行 SQL（在处理 ~/.duckdbrc 之后）。

**-init** _FILENAME_
> 启动时运行指定脚本，代替 ~/.duckdbrc。

**-readonly**
> 以只读模式打开数据库。

**-no-stdin**
> 处理完选项后退出，不读取标准输入。

**-json**
> 以 JSON 格式输出结果。

**-csv**
> 以 CSV 格式输出结果。

**-table**
> 以 ASCII 表格输出结果。

**-box**
> 使用制表线字符输出结果（默认）。

**-markdown**
> 以 Markdown 表格输出结果。

**-line**
> 以行模式输出结果（每行一个值）。

**-column**
> 以列式格式输出结果。

**-ascii**
> 以 ASCII 表格格式输出结果。

**-html**
> 以 HTML 格式输出结果。

**-list**
> 以列表格式输出结果。

**-separator** _SEP_
> 设置列分隔符（默认：|）。

**-newline** _SEP_
> 设置行分隔符（默认：\n）。

**-nullvalue** _TEXT_
> 设置 NULL 值显示的文本。

**-header**
> 输出中包含列头。

**-noheader**
> 输出中不包含列头。

**-echo**
> 执行前先打印命令。

**-bail**
> 遇到错误后停止。

**-batch**
> 强制批量 I/O。

**-interactive**
> 强制交互式 I/O。

**-unsigned**
> 允许加载未签名的扩展。

**-nofollow**
> 拒绝打开指向数据库文件的符号链接。

**-version**
> 打印版本并退出。

**-help**
> 显示可用选项。

# CONFIGURATION

**~/.duckdbrc**
> 初始化文件，其中的 SQL 命令会在 shell 启动时执行，用于设置偏好和默认值。

# DESCRIPTION

**DuckDB** 是一个嵌入式分析型数据库，专为快速在线分析处理（OLAP）工作负载而设计。它可以完全在进程内运行而无需单独的服务器，因此非常适合数据分析和脚本编写。

它的一个关键特性是无需导入即可直接查询文件：CSV、Parquet、JSON 等格式可以直接用在 SQL 查询中，并自动检测类型。这使 DuckDB 成为探索性数据分析和 ETL 任务的利器。

该数据库支持带分析扩展的标准 SQL，包括窗口函数、CTE 和复杂聚合。它通过向量化执行和列式存储实现高性能，专门针对大型数据集上的聚合查询做了优化。

在交互模式下，DuckDB 提供功能完整的 SQL shell，支持 Tab 补全、命令历史以及用于设置的点命令。结果可以多种格式输出，包括表格、JSON、CSV 和 Markdown。默认输出模式是 **duckbox**，一种制表线格式。

DuckDB 可以作为库用于 Python、R、Java、Node.js 等语言，也可以通过 CLI 独立使用。数据库文件可跨平台和跨版本移植。

# CAVEATS

内存数据库在进程退出后即丢失。写操作会锁定数据库文件，限制并发写入。未做适当配置时，超大数据集可能耗尽可用内存。部分 SQL 语法与其他数据库略有差异。

# HISTORY

**DuckDB** 由 Mark Raasveldt 和 Hannes Mühleisen 在阿姆斯特丹 CWI（PostgreSQL 的诞生地）创建。开发始于 **2018 年**前后，目标是打造一个可嵌入的分析型数据库，类似"analytics 界的 SQLite"。该项目自 **2020 年**起在数据科学社区获得广泛采用。

# INSTALL

```pacman: sudo pacman -S duckdb```

```brew: brew install duckdb```

```nix: nix profile install nixpkgs#duckdb```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sqlite3](/man/sqlite3)(1), [psql](/man/psql)(1), [csvq](/man/csvq)(1), [jq](/man/jq)(1)
