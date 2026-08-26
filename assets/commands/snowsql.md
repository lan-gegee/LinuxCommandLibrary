# TAGLINE

Snowflake 云数据仓库 CLI 客户端

# TLDR

**连接到 Snowflake**

```snowsql -a [account] -u [username]```

**执行查询**

```snowsql -a [account] -u [user] -q "[SELECT * FROM table]"```

**运行 SQL 文件**

```snowsql -a [account] -u [user] -f [script.sql]```

**指定数据库**

```snowsql -a [account] -u [user] -d [database]```

**指定仓库**

```snowsql -a [account] -u [user] -w [warehouse]```

**指定角色**

```snowsql -a [account] -u [user] -r [role]```

**以 CSV 格式输出**

```snowsql -a [account] -u [user] -o output_format=[csv]```

**使用配置中的命名连接**

```snowsql -c [connection_name]```

# SYNOPSIS

**snowsql** [_-a account_] [_-u user_] [_-d database_] [_options_]

# PARAMETERS

**-a**, **--accountname** _ACCOUNT_
> Snowflake 账户。

**-u**, **--username** _USER_
> 用户名。

**-d**, **--dbname** _DB_
> 数据库。

**-w**, **--warehouse** _WH_
> 仓库。

**-s**, **--schemaname** _SCHEMA_
> 模式。

**-q**, **--query** _SQL_
> 执行查询。

**-f**, **--filename** _FILE_
> 运行 SQL 文件。

**-r**, **--rolename** _ROLE_
> 要使用的默认角色。

**-c**, **--connection** _NAME_
> 使用配置文件中的命名连接。

**-D**, **--variable** _KEY=VALUE_
> 定义变量（在查询中以 &KEY 引用）。

**-o** _OPTION=VALUE_
> 设置选项（例如 output_format=csv、quiet=true、friendly=false）。

**--version**
> 显示 SnowSQL 版本。

**--upgrade**
> 强制升级到最新的 SnowSQL 版本。

**--config** _FILE_
> 配置文件的路径。

# DESCRIPTION

**snowsql** 是 Snowflake（一个基于云的数据仓库平台）的官方命令行客户端。它提供交互式 SQL shell，用于查询、管理数据库以及在 Snowflake 账户上执行管理任务。

连接需要 Snowflake 账户名和凭据，可以通过命令行提供、交互式输入，或者保存在配置文件中。客户端支持在连接时指定数据库、模式、仓库和角色上下文。

SQL 查询可以在 shell 中交互执行，通过 **-q** 直接传入，或用 **-f** 从脚本文件批量运行以实现自动化。使用 **-o output_format** 选项可以将输出格式化为表格、CSV、TSV 等格式，因此很适合数据导出和流水线集成。

# CONFIGURATION

**~/.snowsql/config**
> SnowSQL 会话的连接配置档、默认设置和保存的凭据。

**SNOWSQL_ACCOUNT**
> 指定默认 Snowflake 账户名的环境变量。

**SNOWSQL_PWD**
> 指定默认密码的环境变量。

**SNOWSQL_ROLE**
> 指定默认角色的环境变量。

# CAVEATS

需要 Snowflake 账户。大结果集可能较慢。可能需要 MFA。

# HISTORY

**SnowSQL** 是 **Snowflake** 云数据仓库的官方 CLI。它提供对 Snowflake SQL 引擎的终端访问。

# INSTALL

```nix: nix profile install nixpkgs#snowsql```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[psql](/man/psql)(1), [mysql](/man/mysql)(1), [bq](/man/bq)(1)
