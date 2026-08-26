# TAGLINE

支持多种数据库后端的终端 SQL IDE

# TLDR

**连接 DuckDB 数据库**

```harlequin [database.db]```

**连接 SQLite 数据库**

```harlequin -a sqlite [database.sqlite]```

**连接 PostgreSQL**

```harlequin -a postgres -h [localhost] -p [5432] -U [user] -d [database]```

**连接 MySQL**

```harlequin -a mysql -h [localhost] -p [3306] -U [user] --database [database]```

**打开内存中的 DuckDB**

```harlequin```

**查询 Parquet 文件**

```harlequin [data.parquet]```

**使用连接字符串连接**

```harlequin "postgresql://[user]:[pass]@[host]/[db]"```

**设置只读模式**

```harlequin --read-only [database.db]```

# SYNOPSIS

**harlequin** [_options_] [_connection_]

# PARAMETERS

**-a**, **--adapter** _name_
> 数据库适配器：duckdb（默认）、sqlite、postgres、mysql、bigquery。

**-h**, **--host** _host_
> 数据库主机。

**-p**, **--port** _port_
> 数据库端口。

**-U**, **--user** _user_
> 数据库用户名。

**-d**, **--database** _name_
> 数据库名称。

**--password** _password_
> 数据库密码。

**--read-only**
> 以只读模式打开连接。

**-t**, **--theme** _theme_
> 配色主题名称（任意 Textual 主题）。

**--limit** _rows_
> 默认的结果行数上限。

**-f**, **--profile** _name_
> 从配置文件加载指定的命名配置档案。

**--no-download-tzdata**
> 跳过为 DuckDB 下载时区数据。

**--help**
> 显示帮助信息。

**--version**
> 显示版本信息。

# KEYBOARD COMMANDS

**Ctrl+Enter**
> 执行查询。

**Ctrl+j**
> 执行查询（备选按键）。

**Ctrl+o**
> 打开查询文件。

**Ctrl+s**
> 将查询保存到文件。

**F1-F10**
> 在查询标签页之间切换。

**Ctrl+n**
> 新建查询标签页。

**Ctrl+w**
> 关闭当前标签页。

**Ctrl+e**
> 导出结果。

**Ctrl+q**
> 退出。

# DESCRIPTION

**harlequin** 是一款基于终端的 SQL IDE，支持多种数据库后端。它提供丰富的界面，可用于编写查询、浏览模式和查看结果。

界面包含模式浏览器、带语法高亮的查询编辑器和结果面板。多查询标签页让你可以同时处理多条查询。

DuckDB 是默认适配器，可直接查询 Parquet、CSV 和 JSON 文件。其他适配器则用于连接 PostgreSQL、MySQL 和 SQLite 等传统数据库。

查询结果显示在可滚动的表格中，并带有导出选项。历史记录和自动补全辅助编写查询。模式浏览器会显示表、列和类型。

可以通过配置文件或环境变量进行配置，为主题、行数限制和连接偏好设置默认值。

# CAVEATS

部分适配器需要额外安装软件包。较大的结果集可能影响终端性能。键盘快捷键可能与终端模拟器的绑定冲突。具体功能因适配器而异。

# HISTORY

Harlequin 由 **Ted Conbeer** 创建，首次发布于 **2023 年**。它基于 Textual 框架构建，带来现代化的终端 SQL 体验。该项目源于作者对缺乏视觉反馈的 CLI 数据库工具的不满。它以 DuckDB 生态为核心，同时支持传统数据库。目前仍在积极开发中，不断推出新的适配器和功能。

# INSTALL

```brew: brew install harlequin```

```nix: nix profile install nixpkgs#harlequin```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[duckdb](/man/duckdb)(1), [psql](/man/psql)(1), [mysql](/man/mysql)(1), [sqlite3](/man/sqlite3)(1)
