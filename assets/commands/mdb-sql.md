# TAGLINE

面向 Access 数据库的 MDB Tools SQL 接口

# TLDR

**启动交互式 SQL 会话**

```mdb-sql [database.mdb]```

**执行来自 stdin 的 SQL**

```echo "SELECT * FROM [table_name]" | mdb-sql [database.mdb]```

**美化打印输出**（ASCII 表格格式）

```mdb-sql -p [database.mdb]```

**执行文件中的 SQL**

```mdb-sql -i [query.sql] [database.mdb]```

**指定列分隔符**并抑制表头

```mdb-sql -d [,] -H [database.mdb]```

**将输出写入文件**

```mdb-sql -o [output.csv] [database.mdb]```

# SYNOPSIS

**mdb-sql** [_options_] _database_

# PARAMETERS

_DATABASE_
> Microsoft Access 数据库文件（.mdb 或 .accdb）。

**-H**, **--no-header**
> 抑制列标题行。

**-F**, **--no-footer**
> 抑制页脚行。

**-p**, **--no-pretty-print**
> 输出制表符分隔的内容而不是 ASCII 表格格式。

**-d**, **--delimiter** _DELIM_
> 使用替代的列分隔符。

**-i**, **--input** _FILE_
> 从输入文件读取 SQL。

**-o**, **--output** _FILE_
> 将结果写入输出文件。

**--version**
> 打印 mdbtools 版本并退出。

# INTERACTIVE COMMANDS

**list tables**: 列出数据库中可用的表。
**describe table** _name_: 显示表的列信息。
**go**: 执行当前 SQL 批处理。
**reset**: 清除当前 SQL 批处理。
**connect** _database_: 连接到数据库（或切换数据库）。
**disconnect**: 断开与当前数据库的连接。

# DESCRIPTION

**mdb-sql** 提供 Microsoft Access 数据库的 SQL 接口。它可以交互式运行，也可以处理来自 stdin 或文件的 SQL。在交互模式下，SQL 批处理以 **go** 命令结束。

该工具是 **mdbtools** 套件的一部分。它支持对 MDB/ACCDB 文件执行 SELECT 查询。

# CAVEATS

与完整的 Access SQL 相比 SQL 支持有限。属于 mdbtools 的一部分。可能不支持所有 Access 特性或数据类型。

# HISTORY

mdb-sql 是 **mdbtools** 的一部分，用于在 Linux/Unix 上访问 Microsoft Access 数据库。

# INSTALL

```apt: sudo apt install mdbtools```

```dnf: sudo dnf install mdbtools```

```apk: sudo apk add mdbtools-utils```

```zypper: sudo zypper install mdbtools```

```brew: brew install mdbtools```

```nix: nix profile install nixpkgs#mdbtools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mdbtools](/man/mdbtools)(1)
