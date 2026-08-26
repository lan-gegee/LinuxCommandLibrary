# TAGLINE

对 PostgreSQL 数据库进行垃圾回收和分析

# TLDR

**清理数据库**

```vacuumdb [database]```

**清理所有数据库**

```vacuumdb --all```

**清理并更新优化器统计信息**

```vacuumdb --analyze [database]```

**完全清理**（重写表并回收磁盘空间）

```vacuumdb --full [database]```

**清理指定的表**

```vacuumdb -t [table_name] [database]```

**以多作业并行执行清理**

```vacuumdb -j [4] [database]```

**积极冻结元组**以防止事务 ID 回绕

```vacuumdb --freeze [database]```

**只更新统计信息**而不进行清理

```vacuumdb --analyze-only [database]```

**在远程服务器上带身份验证执行清理**

```vacuumdb -h [hostname] -p [5432] -U [username] [database]```

# SYNOPSIS

**vacuumdb** [_-a_] [_-z_] [_-f_] [_-F_] [_-t table_] [_-j jobs_] [_options_] [_dbname_]

# PARAMETERS

**-a**, **--all**
> 清理所有数据库。

**-d** _DBNAME_, **--dbname** _DBNAME_
> 要清理或分析的数据库。

**-z**, **--analyze**
> 同时计算供优化器使用的统计信息。

**-Z**, **--analyze-only**
> 只计算统计信息，不执行清理。

**--analyze-in-stages**
> 以三个阶段进行分析，统计目标逐步提高。适用于没有统计信息或统计信息完全错误的数据库。

**-f**, **--full**
> 执行完全清理（重写表，回收磁盘空间）。

**-F**, **--freeze**
> 积极冻结元组以防止事务 ID 回绕。

**-t** _TABLE_, **--table** _TABLE_
> 只清理指定的表。可以多次指定。

**-n** _SCHEMA_, **--schema** _SCHEMA_
> 只清理或分析指定模式中的所有表。可以多次指定。

**-N** _SCHEMA_, **--exclude-schema** _SCHEMA_
> 排除指定模式中的表。

**-j** _N_, **--jobs** _N_
> 通过同时运行 N 个作业来并行执行清理或分析命令。

**-P** _N_, **--parallel** _N_
> 指定每次清理操作的并行 worker 数量。

**--skip-locked**
> 跳过无法立即加锁的关系。

**--no-index-cleanup**
> 不移除指向死元组的索引条目。

**--no-truncate**
> 不截断表末尾的空页。

**--disable-page-skipping**
> 禁用基于可见性映射的页面跳过。

**--min-xid-age** _AGE_
> 只处理事务 ID 年龄至少为 AGE 的表。

**--min-mxid-age** _AGE_
> 只处理 multixact ID 年龄至少为 AGE 的表。

**-e**, **--echo**
> 回显发送到服务器的命令。

**-q**, **--quiet**
> 不显示进度消息。

**-v**, **--verbose**
> 处理过程中输出详细信息。

**-h** _HOST_, **--host** _HOST_
> 数据库服务器主机。

**-p** _PORT_, **--port** _PORT_
> 服务器端口。

**-U** _USER_, **--username** _USER_
> 用于连接的用户名。

**-w**, **--no-password**
> 绝不提示输入密码。

**-W**, **--password**
> 强制提示输入密码。

**--maintenance-db** _DBNAME_
> 使用 --all 时要连接的数据库。

# DESCRIPTION

**vacuumdb** 清理并分析 PostgreSQL 数据库。它是 SQL VACUUM 和 ANALYZE 命令的包装器，为脚本和定时任务提供了便捷的选项。

常规清理将死元组标记为可复用。它不会回收磁盘空间，但能防止表无限膨胀。

完全清理会重写表，从而回收磁盘空间。它需要对表加排他锁，耗时也比常规清理更长。

Analyze 更新查询规划器使用的统计信息。准确的统计信息能带来更好的查询计划和性能。

使用 **-j** 进行并行清理可同时处理多个表。**-P** 选项控制每次清理操作内部的并行 worker 数量。

# CAVEATS

完全清理会以排他方式锁定表，并且需要额外的磁盘空间来完成重写。常规清理应当频繁运行。对于繁忙的数据库，**--freeze** 选项对防止事务 ID 回绕非常重要。

# HISTORY

**vacuumdb** 从早期版本起就是 **PostgreSQL** 的一部分。它提供了命令行方式的 vacuum 操作，这对数据库维护至关重要。

# INSTALL

```apk: sudo apk add postgresql17-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[psql](/man/psql)(1), [pg_dump](/man/pg_dump)(1), [reindexdb](/man/reindexdb)(1), [clusterdb](/man/clusterdb)(1), [createdb](/man/createdb)(1)
