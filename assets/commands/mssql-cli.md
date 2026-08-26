# TAGLINE

交互式 Microsoft SQL Server 命令行查询工具

# TLDR

**连接**到服务器

```mssql-cli -S [server] -U [user] -d [database]```

**运行查询**后退出

```mssql-cli -S [server] -U [user] -d [db] -Q "[SELECT 1]"```

# SYNOPSIS

**mssql-cli** [*options*]

# DESCRIPTION

**mssql-cli** 是一款 dbcli 风格的 SQL Server 交互式客户端，具有多行编辑、自动补全和美观的结果表格。通过 **pip install mssql-cli** 安装。属于更广泛的 dbcli 家族（**pgcli**、**mycli**）。

# PARAMETERS

**-S** *server*

> SQL Server 主机。

**-U** *user* / **-P** *password*

> 凭据（优先使用环境变量或交互提示，避免留在 shell 历史中）。

**-d** *database*

> 数据库名称。

**-Q** *query*

> 以非交互方式执行查询。

**-E**

> 在支持的情况下使用集成身份验证。

完整选项见：**mssql-cli --help**。

# CAVEATS

请确认项目在你的平台上是否仍在维护；Microsoft 也提供 **sqlcmd** 和 Azure Data Studio。请安全地保管凭据。

# SEE ALSO

[sqlcmd](/man/sqlcmd)(1), [pgcli](/man/pgcli)(1), [mycli](/man/mycli)(1)

# RESOURCES

```[Source code](https://github.com/dbcli/mssql-cli)```

<!-- verified: 2026-07-19 -->
