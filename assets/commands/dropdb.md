# TAGLINE

删除 PostgreSQL 数据库

# TLDR

**删除数据库**

```dropdb [database_name]```

**删除前弹出确认**提示

```dropdb -i [database_name]```

在**远程主机上删除**

```dropdb -h [hostname] -p [5432] [database_name]```

以**指定用户**身份删除

```dropdb -U [username] [database_name]```

**存在才删除**（不存在时不报错）

```dropdb --if-exists [database_name]```

**强制断开**活动连接

```dropdb --force [database_name]```

# SYNOPSIS

**dropdb** [_options_] _dbname_

# PARAMETERS

_DBNAME_
> 要删除的数据库名。

**-h**, **--host** _HOST_
> 服务器主机名。

**-p**, **--port** _PORT_
> 服务器端口。

**-U**, **--username** _USER_
> 以该用户身份连接。

**-i**, **--interactive**
> 删除前提示确认。

**--if-exists**
> 数据库不存在时不报错。

**--force**
> 终止已有连接。

**-w**, **--no-password**
> 从不提示输入密码。

**-W**, **--password**
> 强制提示输入密码。

**--maintenance-db** _dbname_
> 用于执行删除操作的连接数据库（默认：postgres）。

**-e**, **--echo**
> 显示执行的 SQL 命令。

**-V**, **--version**
> 打印版本并退出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**dropdb** 是一个用于删除数据库的 PostgreSQL 实用工具。它是 SQL DROP DATABASE 命令的封装，为数据库删除提供了便捷的命令行界面。

该工具连接到 postgres 数据库来执行删除。--force 选项会终止与目标数据库的现有连接，从而允许删除仍有活动会话的数据库。

dropdb 需要相应的权限——通常是超级用户或数据库所有者权限。

# CAVEATS

不可逆操作。没有 --force 时无法删除有活动连接的数据库。需要超级用户或所有者权限。无法删除模板数据库。

# HISTORY

dropdb 是 **PostgreSQL** 客户端实用工具的一部分，自 PostgreSQL 早期版本起就提供命令行数据库管理功能。它简化了常见的管理任务，无需直接编写 SQL。

# INSTALL

```apk: sudo apk add postgresql17-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[createdb](/man/createdb)(1), [psql](/man/psql)(1), [dropuser](/man/dropuser)(1), [pg_dump](/man/pg_dump)(1)
