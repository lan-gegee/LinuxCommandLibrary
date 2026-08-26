# TAGLINE

SQLite 数据库的图形界面编辑器

# TLDR

**打开数据库文件**

```sqlitebrowser [database.db]```

**以只读模式打开数据库**

```sqlitebrowser -R [database.db]```

**打开后执行 SQL 文件**

```sqlitebrowser -s [script.sql] [database.db]```

**导入 CSV 文件**

```sqlitebrowser --import-csv [data.csv] [database.db]```

**直接打开特定表**

```sqlitebrowser -t [tablename] [database.db]```

# SYNOPSIS

**sqlitebrowser** [_options_] [_database_]

# PARAMETERS

**-h**, **--help**
> 显示命令行选项。

**-v**, **--version**
> 显示版本。

**-q**, **--quit**
> 执行完脚本后退出。

**-s** _FILE_, **--sql** _FILE_
> 打开数据库后执行 SQL 文件。

**--import-csv** _FILE_
> 将 CSV 文件导入数据库。

**-t** _TABLE_, **--table** _TABLE_
> 启动时浏览特定表。

**-R**, **--read-only**
> 以只读模式打开数据库。

**-S** _FILE_, **--settings** _FILE_
> 使用指定的设置文件。

**-o** _SETTING_, **--option** _SETTING_
> 临时设置某个选项（group/setting=value）。

**--in-memory**
> 以内存数据库启动。

# DESCRIPTION

**sqlitebrowser**（DB Browser for SQLite）是一个用于创建、设计和编辑 SQLite 数据库文件的可视化开源工具。它提供类似电子表格的数据浏览界面、用于运行查询的 SQL 编辑器，以及管理表、索引和触发器的工具。

尽管是图形应用程序，它也支持实用的命令行选项以便自动化操作，例如导入 CSV 文件、执行 SQL 脚本和打开特定表。

# CAVEATS

这是一个 GUI 应用，需要显示服务器。命令行选项只决定图形窗口如何启动。它不能替代 **sqlite3** 命令行 Shell。

# INSTALL

```apt: sudo apt install sqlitebrowser```

```dnf: sudo dnf install sqlitebrowser```

```pacman: sudo pacman -S sqlitebrowser```

```apk: sudo apk add sqlitebrowser```

```zypper: sudo zypper install sqlitebrowser```

```nix: nix profile install nixpkgs#sqlitebrowser```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sqlite3](/man/sqlite3)(1), [mdb-sql](/man/mdb-sql)(1)
