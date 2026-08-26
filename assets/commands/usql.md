# TAGLINE

通用命令行数据库客户端

# TLDR

**连接 PostgreSQL**

```usql postgres://[user]:[pass]@[host]/[database]```

**连接 MySQL**

```usql mysql://[user]:[pass]@[host]/[database]```

**连接 SQLite**

```usql sqlite:[database.db]```

**执行查询**

```usql [connection_url] -c "[SELECT * FROM table]"```

**执行文件**

```usql [connection_url] -f [script.sql]```

**列出数据库**

```usql [connection_url] -c "\\l"```

**查看表结构**

```usql [connection_url] -c "\\d [table_name]"```

# SYNOPSIS

**usql** [_-c command_] [_-f file_] [_options_] _connection_url_

# PARAMETERS

**-c** _CMD_
> 执行命令后退出。

**-f** _FILE_
> 执行指定文件。

**-o** _FILE_
> 输出到文件。

**-w**, **--no-password**
> 绝不提示输入密码。

**-W**, **--password**
> 总是提示输入密码。

**-X**, **--no-rc**
> 不读取 rc 文件。

**-t**, **--tuples-only**
> 只输出数据行。

**-q**, **--quiet**
> 安静模式。

**-v** _NAME=VALUE_
> 设置变量。

**--help**
> 显示帮助。

**--version**
> 显示版本。

# DESCRIPTION

**usql** 是一款面向 SQL 数据库的通用命令行界面。它能够以一致的、仿照 psql 设计的界面连接 PostgreSQL、MySQL、SQLite、SQL Server、Oracle 以及众多其他数据库（包括 NoSQL 数据库）。

连接字符串遵循 URL 格式，协议头标识数据库类型：postgres://、mysql://、sqlite:、mssql://、oracle:// 等。若未提供协议头，usql 会自动检测：目录视为 PostgreSQL，普通文件则视为 SQLite3 或 DuckDB。

反斜杠命令可以跨数据库使用：\\l 列出数据库，\\dt 列出表，\\d 查看对象结构，\\drivers 列出可用的数据库驱动。

查询结果可以格式化为表格、CSV、JSON 等多种形式。Tab 补全能辅助输入表名和列名，命令历史还会跨会话保存。

# CAVEATS

并非所有数据库都支持全部功能。某些驱动需要单独安装。复杂查询可能带有特定数据库专用的语法。

# HISTORY

**usql** 由 **Kenneth Shaw** 于 **2017 年**左右创建，目标是做一个通用 SQL 客户端。它用一个统一一致的工具化解了各家数据库 CLI 分裂割据的局面。

# INSTALL

```nix: nix profile install nixpkgs#usql```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[psql](/man/psql)(1), [mysql](/man/mysql)(1), [sqlite3](/man/sqlite3)(1), [sqlcmd](/man/sqlcmd)(1)
