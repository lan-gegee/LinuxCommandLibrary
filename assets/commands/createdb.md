# TAGLINE

创建新的 PostgreSQL 数据库

# TLDR

**以默认名称（当前用户）创建数据库**

```createdb```

**以指定名称创建数据库**

```createdb [dbname]```

**以指定所有者创建数据库**

```createdb -O [owner] [dbname]```

**以指定编码创建数据库**

```createdb -E [UTF8] [dbname]```

**基于 template0 创建干净的数据库**

```createdb -T [template0] [dbname]```

**在远程服务器上创建数据库**

```createdb -h [hostname] -p [5432] -U [user] [dbname]```

**显示正在执行的 SQL 命令**

```createdb -e [dbname]```

# SYNOPSIS

**createdb** [_options_] [_dbname_] [_description_]

# PARAMETERS

**-D** _tablespace_, **--tablespace** _tablespace_
> 数据库的默认表空间。

**-E** _encoding_, **--encoding** _encoding_
> 数据库的字符编码。

**-l** _locale_, **--locale** _locale_
> 数据库的区域设置（locale）。

**-O** _owner_, **--owner** _owner_
> 数据库所有者用户。

**-T** _template_, **--template** _template_
> 作为复制来源的模板数据库（默认 template1）。

**-e**, **--echo**
> 回显 createdb 发送给服务器的 SQL 命令。

**--icu-locale** _locale_
> 数据库的 ICU 区域设置。

**--icu-rules** _rules_
> 数据库的 ICU 排序规则。

**--locale-provider** _provider_
> 区域设置提供程序（libc 或 icu）。

**--strategy** _strategy_
> 数据库创建策略（wal_log 或 file_copy）。

**-V**, **--version**
> 打印 createdb 版本并退出。

**-h** _host_, **--host** _host_
> 服务器主机名或套接字目录。

**-p** _port_, **--port** _port_
> 服务器端口号。

**-U** _user_, **--username** _user_
> 用于连接的用户名。

**-w**, **--no-password**
> 从不提示输入密码。

**-W**, **--password**
> 强制提示输入密码。

**--maintenance-db** _db_
> 创建新数据库时所要连接的数据库。默认为 postgres，若 postgres 不存在则使用 template1。

# DESCRIPTION

**createdb** 创建一个新的 PostgreSQL 数据库。它是 SQL **CREATE DATABASE** 命令的便捷封装，其命令行接口通常比直接调用 psql 更加方便。

如果不指定数据库名，则默认使用当前系统用户名。还可以将可选的描述（注释）作为第二个参数传入。

# CAVEATS

需要拥有 **CREATEDB** 权限或超级用户角色。默认模板是 template1；如需创建不带本地附加内容的干净数据库，请使用 template0。连接参数也可以通过标准的 PostgreSQL 环境变量（**PGHOST**、**PGPORT**、**PGUSER**、**PGDATABASE**）设置。

# HISTORY

**createdb** 自 PostgreSQL 早期版本起便是其发行版的一员，为 **CREATE DATABASE** SQL 命令提供了简单的命令行接口。

# INSTALL

```apk: sudo apk add postgresql17-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dropdb](/man/dropdb)(1), [psql](/man/psql)(1), [pg_dump](/man/pg_dump)(1)
