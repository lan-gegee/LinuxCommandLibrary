# TAGLINE

PostgreSQL 交互式终端客户端

# TLDR

**连接到数据库**

```psql -d [database]```

**连接远程服务器**

```psql -h [host] -U [user] -d [database]```

**执行 SQL 命令**

```psql -c "SELECT * FROM [table]" [database]```

**执行 SQL 文件**

```psql -f [script.sql] [database]```

**列出数据库**

```psql -l```

**交互模式**

```psql [database]```

# SYNOPSIS

**psql** [_options_] [_dbname_]

# PARAMETERS

_DBNAME_
> 数据库名称。

**-h** _HOST_
> 服务器主机名。

**-p** _PORT_
> 端口号。

**-U** _USER_
> 用户名。

**-d** _DBNAME_
> 数据库名称。

**-c** _COMMAND_
> 执行命令。

**-f** _FILE_
> 执行文件。

**-l**
> 列出数据库。

# DESCRIPTION

**psql** 是 PostgreSQL 官方的交互式终端。它提供命令行界面，用于连接数据库、执行 SQL 查询和管理数据库对象。在交互模式下，它提供制表符补全、命令历史记录和格式化的查询结果输出等功能。

除交互使用外，psql 可以用 **-f** 执行 SQL 文件、用 **-c** 运行单条命令，因此也适合脚本化和自动化场景。内置的反斜杠命令（如 **\dt** 列出表、**\d** 描述对象、**\l** 列出数据库）无需编写 SQL 即可快速访问数据库元数据。

连接参数可以通过命令行标志、环境变量（**PGHOST**、**PGUSER**、**PGDATABASE**、**PGPORT**）或 **~/.pgpass** 文件（用于免密码认证）来指定。

# CONFIGURATION

**~/.pgpass**
> 用于自动认证的密码文件，每行格式为 `hostname:port:database:username:password`。

**~/.psqlrc**
> psql 启动时执行的启动文件，用于设置格式选项、自定义提示符和默认配置。

**PGHOST**, **PGUSER**, **PGDATABASE**, **PGPORT**
> 提供默认连接参数的环境变量。

# CAVEATS

PostgreSQL 专用。需要连接服务器。

# HISTORY

psql 是 **官方 PostgreSQL** 命令行客户端。

# INSTALL

```apk: sudo apk add postgresql17-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pg_dump](/man/pg_dump)(1), [createdb](/man/createdb)(1), [mysql](/man/mysql)(1)
