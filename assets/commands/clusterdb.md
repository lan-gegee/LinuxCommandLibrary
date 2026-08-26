# TAGLINE

PostgreSQL 表重聚类工具

# TLDR

对数据库中的所有表**执行聚类**

```clusterdb [database_name]```

**对特定表执行聚类**

```clusterdb --table [table_name] [database_name]```

对服务器上的所有数据库**执行聚类**

```clusterdb --all```

**带连接选项执行聚类**

```clusterdb --host [hostname] --port [5432] --username [user] [database]```

**以详细输出模式执行聚类**

```clusterdb --verbose [database_name]```

**使用指定索引执行聚类**

```clusterdb --table [table_name] --index [index_name] [database_name]```

**回显正在执行的命令**

```clusterdb --echo [database_name]```

# SYNOPSIS

**clusterdb** [_-a_] [_-d dbname_] [_-t table_] [_-i index_] [_-v_] [_-e_] [_connection-options_] [_dbname_]

# PARAMETERS

**-a**, **--all**
> 对服务器上的所有数据库执行聚类。

**-d**, **--dbname** _dbname_
> 要聚类的数据库。

**-t**, **--table** _table_
> 仅对指定的表执行聚类。

**-i**, **--index** _index_
> 使用指定的索引对表进行聚类。

**-v**, **--verbose**
> 在处理过程中打印详细信息。

**-e**, **--echo**
> 回显发送到服务器的命令。

**-q**, **--quiet**
> 不显示进度消息。

**-h**, **--host** _hostname_
> 数据库服务器主机（默认：本地套接字或 localhost）。

**-p**, **--port** _port_
> 数据库服务器端口（默认：5432）。

**-U**, **--username** _username_
> 用于连接的用户名。

**-w**, **--no-password**
> 从不提示输入密码。

**-W**, **--password**
> 强制提示输入密码。

**--maintenance-db** _dbname_
> 使用 `-a`/`--all` 时要连接的数据库（默认为 `postgres` 或 `template1`）。

**-V**, **--version**
> 打印版本信息。

**-?**, **--help**
> 显示命令行参数的帮助信息。

# DESCRIPTION

**clusterdb** 是一个 PostgreSQL 工具，用于对数据库中的表重新聚类。聚领会按照某个索引的顺序物理重排表的数据行，从而显著提升使用该索引的范围查询性能。

当表基于某个索引聚类后，数据行会在磁盘上按索引顺序物理排序。这可以减少扫描索引值范围的查询产生的磁盘 I/O，因为顺序磁盘访问比随机访问更快。然而，随着行的插入、更新或删除，聚类顺序会随时间逐渐退化。

该命令是 SQL **CLUSTER** 命令的封装，提供了一种从命令行聚类表的便捷方式。在不使用 **-t** 选项时，它会对数据库中所有之前已聚类的表执行聚类。

聚类是一次性操作，不会随时间维持物理顺序。对于更新频繁的表，可能需要定期重新聚类。该操作需要对表的独占访问，并且对大表而言可能非常消耗资源。

# CAVEATS

操作期间需要对表持有独占锁，会阻塞所有其他访问。大表可能耗费大量时间和临时磁盘空间。后续修改不会维持聚类顺序。一张表只能由一个索引定义其聚类顺序。

# HISTORY

**clusterdb** 自早期版本起就是 PostgreSQL 发行版的组成部分，为 CLUSTER 功能提供命令行入口。CLUSTER 命令本身可以追溯到 PostgreSQL 在 UC Berkeley 作为研究数据库的起源时期。该工具遵循 PostgreSQL 一贯的模式，即为常见管理任务提供命令行封装。

# INSTALL

```apk: sudo apk add postgresql17-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[psql](/man/psql)(1), [vacuumdb](/man/vacuumdb)(1), [reindexdb](/man/reindexdb)(1)
