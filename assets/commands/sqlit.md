# TAGLINE

Lazygit 风格的 SQL 数据库 TUI

# TLDR

**启动交互式 TUI**

```sqlit```

**连接已保存的连接**

```sqlit -c "[MyConnection]"```

**从 CLI 运行查询**

```sqlit query -c "[MyConnection]" -q "[SELECT * FROM Users]" --format csv```

# SYNOPSIS

**sqlit** [**-c** _connection_name_]

**sqlit** **query** [**-c** _connection_name_] [**-q** _query_] [**--format** _format_]

# PARAMETERS

**-c** _CONNECTION_
> 使用已保存的连接名进行连接。

**-q** _QUERY_
> 要执行的 SQL 查询（与 **query** 子命令配合使用）。

**--format** _FORMAT_
> 查询结果的输出格式：**table**、**csv**、**json**（与 **query** 子命令配合使用）。

# DESCRIPTION

**sqlit** 是一个轻量、键盘驱动的 TUI，用于在终端中连接和查询 SQL 数据库。它支持 20 多种数据库系统，包括 PostgreSQL、MySQL、SQLite、DuckDB、BigQuery、ClickHouse 和 Snowflake。功能包括查询历史、自动补全、Vim 风格编辑、SSH 隧道、Docker 容器自动发现以及安全的凭据存储。

# HISTORY

**sqlit** 由 **Maxteabag**（Peter Adams）创建，使用 **Python** 编写。

# INSTALL

```aur: yay -S sqlit```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[litecli](/man/litecli)(1), [harlequin](/man/harlequin)(1), [usql](/man/usql)(1), [pgcli](/man/pgcli)(1), [mycli](/man/mycli)(1)
