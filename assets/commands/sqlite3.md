# TAGLINE

交互式 SQLite 数据库 Shell

# TLDR

**打开或创建数据库**

```sqlite3 [database.db]```

**执行 SQL 查询**

```sqlite3 [database.db] "[SELECT * FROM table]"```

**从文件执行 SQL**

```sqlite3 [database.db] < [query.sql]```

**将查询结果导出为 CSV**

```sqlite3 -csv [database.db] "[SELECT * FROM table]" > [output.csv]```

**显示所有表**

```sqlite3 [database.db] ".tables"```

**显示表模式**

```sqlite3 [database.db] ".schema [table_name]"```

**将 CSV 导入表**

```sqlite3 [database.db] ".import [file.csv] [table_name]"```

**打开内存数据库**

```sqlite3 :memory:```

# SYNOPSIS

**sqlite3** [_options_] [_database_] [_sql_]

# PARAMETERS

**-csv**
> 将输出模式设为 CSV

**-json**
> 将输出模式设为 JSON

**-column**
> 将输出模式设为列格式

**-header**
> 在输出中包含列标题

**-line**
> 将输出模式设为每行一个值

**-separator** _sep_
> 设置 CSV 模式的字段分隔符

**-init** _file_
> 启动时从文件执行 SQL

**-batch**
> 批处理模式；出错即退出

**-readonly**
> 以只读模式打开数据库

**-version**
> 显示版本信息

# DOT COMMANDS

**.tables**：列出所有表
**.schema** [_table_]：显示 CREATE 语句
**.headers on|off**：切换列标题显示
**.mode** _mode_：设置输出模式（csv、column、json、line 等）
**.import** _file table_：从文件导入数据
**.output** _file_：将输出重定向到文件
**.read** _file_：从文件执行 SQL
**.dump** [_table_]：以 SQL 形式导出数据库
**.exit** 或 **.quit**：退出 sqlite3
**.help**：显示所有点命令

# DESCRIPTION

**sqlite3** 是 SQLite 的命令行界面。SQLite 是一个自包含、无服务器的 SQL 数据库引擎，其数据库就是单个文件，便于共享和备份。

该工具同时提供交互模式和批处理模式。在交互模式下，输入以分号结尾的 SQL 语句，或使用点命令（dot command）执行管理功能。批处理模式则从参数或 stdin 处理 SQL。

SQLite 支持大多数 SQL 特性，包括事务、触发器、视图和复杂查询。它被嵌入在无数应用之中，非常适合本地存储、测试和小型应用。

# CAVEATS

SQLite 使用动态类型；任何列都可以存储任何类型的数据，而不受声明类型的限制。这与严格的 SQL 数据库不同。

并发写入受限——SQLite 在写入期间会锁定整个数据库。对于高并发应用，请考虑使用客户端-服务器型数据库。

点命令是 sqlite3 特有的，不属于 SQL。它们不能在 SQL 语句或应用程序代码中使用。

# INSTALL

```apt: sudo apt install sqlite3```

```dnf: sudo dnf install sqlite```

```pacman: sudo pacman -S sqlite```

```apk: sudo apk add sqlite```

```zypper: sudo zypper install sqlite3```

```brew: brew install sqlite3```

```nix: nix profile install nixpkgs#sqlite```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mysql](/man/mysql)(1), [psql](/man/psql)(1), [sqlite-utils](/man/sqlite-utils)(1)
