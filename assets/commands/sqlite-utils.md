# TAGLINE

SQLite 数据库操作 CLI 与程序库

# TLDR

**将 JSON 导入 SQLite**

```sqlite-utils insert [database.db] [table] [data.json]```

**将 CSV 导入 SQLite**

```sqlite-utils insert [database.db] [table] [data.csv] --csv```

**用 SQL 查询**

```sqlite-utils [database.db] "[SELECT * FROM table]"```

**查询并以 JSON 输出**

```sqlite-utils [database.db] "[SELECT * FROM table]" --json```

**列出表**

```sqlite-utils tables [database.db]```

**显示模式（schema）**

```sqlite-utils schema [database.db]```

**创建 FTS 全文搜索索引**

```sqlite-utils enable-fts [database.db] [table] [column1] [column2]```

**将表导出为 JSON**

```sqlite-utils rows [database.db] [table] > [data.json]```

**Upsert 数据**（冲突时插入或更新）

```sqlite-utils upsert [database.db] [table] [data.json] --pk [id]```

用内存数据库**处理来自 stdin 的数据**

```cat [data.json] | sqlite-utils memory - "[SELECT * FROM stdin]"```

# SYNOPSIS

**sqlite-utils** _command_ [_database_] [_options_] [_arguments_]

# PARAMETERS

**insert** _DB_ _TABLE_ [_FILE_]
> 从 JSON、CSV 或 stdin 插入数据。

**rows** _DB_ _TABLE_
> 以 JSON 输出行。

**tables** _DB_
> 列出表。

**schema** _DB_
> 显示数据库模式。

**query** _DB_ _SQL_
> 运行 SQL 查询。

**upsert** _DB_ _TABLE_ [_FILE_]
> 插入或更新数据（需要 --pk）。

**memory** _SQL_
> 对内存数据库运行 SQL（可从文件或 stdin 读取）。

**enable-fts** _DB_ _TABLE_ _COLUMNS_
> 启用全文搜索。

**search** _DB_ _TABLE_ _QUERY_
> 全文搜索。

**create-table** _DB_ _TABLE_ _COLUMNS_
> 用指定列创建表。

**drop-table** _DB_ _TABLE_
> 删除表。

**add-column** _DB_ _TABLE_ _COL_ [_TYPE_]
> 向表添加列。

**indexes** _DB_ [_TABLE_]
> 列出索引。

**--csv**
> 输入为 CSV。

**--tsv**
> 输入为 TSV。

**--nl**
> 输入为换行分隔的 JSON。

**--pk** _COLUMN_
> 主键列。

**--json**
> 以 JSON 输出。

**--table**
> 以表格输出。

**-c**, **--csv**
> 以 CSV 输出。

**--flatten**
> 将嵌套的 JSON 对象展平为列。

**--batch-size** _N_
> 每个插入批次的行数。

# DESCRIPTION

**sqlite-utils** 提供用于操作 SQLite 数据库的 CLI 和 Python 库。它简化了常见任务：导入数据、运行查询和管理模式。

数据导入支持 JSON、CSV、TSV 和换行分隔的 JSON。类型会自动推断。可以指定主键和外键。现有表会按配置进行更新或替换。

查询支持 SQL 以及多种输出格式。memory 子命令对内存数据库执行查询，适合无需持久文件的快速数据处理。

全文搜索（FTS）提供快速的文本搜索能力。enable-fts 为指定列创建虚拟表。搜索查询使用 SQLite 的 FTS5 语法进行相关性排序。

表管理包括创建、修改和检查。schema 命令显示 CREATE 语句。可以在不重建表的情况下添加列。

该工具与 Unix 管道配合良好。数据从 curl 或其他工具流入，经过处理后输出给后续命令。

# CAVEATS

大批量插入可能需要调整 --batch-size。FTS 会增大数据库体积。类型推断不一定总是正确。部分功能要求 SQLite 3.25 及以上版本。内存占用会随大数据集增长。

# HISTORY

**sqlite-utils** 由 **Simon Willison** 于 **2019 年**前后创建，是 Datasette 生态系统的一部分。它以命令行方式提供了此前必须借助 Python 脚本或其他独立工具才能完成的 SQLite 操作。该库也可以在 Python 中调用，以编程方式操作数据库。

# INSTALL

```brew: brew install sqlite-utils```

```nix: nix profile install nixpkgs#sqlite-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sqlite3](/man/sqlite3)(1), [jq](/man/jq)(1), [datasette](/man/datasette)(1), [csvkit](/man/csvkit)(1)
