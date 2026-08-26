# TAGLINE

重建 PostgreSQL 数据库索引

# TLDR

**重建数据库索引**

```reindexdb [database_name]```

**重建指定表的索引**

```reindexdb -t [table_name] [database_name]```

**重建指定索引**

```reindexdb -i [index_name] [database_name]```

**重建所有数据库的索引**

```reindexdb -a```

**重建系统目录索引**

```reindexdb -s [database_name]```

**以指定用户连接**

```reindexdb -U [username] [database_name]```

**并发重建索引**

```reindexdb --concurrently [database_name]```

# SYNOPSIS

**reindexdb** [_-t table_] [_-i index_] [_-a_] [_-s_] [_options_] [_database_]

# PARAMETERS

**-t**, **--table** _NAME_
> 重建指定表的索引。

**-i**, **--index** _NAME_
> 重建指定索引。

**-a**, **--all**
> 所有数据库。

**-s**, **--system**
> 仅系统目录。

**--concurrently**
> 并发重建。

**-U**, **--username** _USER_
> 以指定用户连接。

**-h**, **--host** _HOST_
> 数据库服务器。

**-p**, **--port** _PORT_
> 服务器端口。

**-j**, **--jobs** _N_
> 并行任务数。

# DESCRIPTION

**reindexdb** 用于重建 PostgreSQL 索引。它是 SQL REINDEX 命令的封装。

整库重建会重建所有索引，可修复损坏并减少膨胀。

针对特定表的重建可聚焦问题区域，比整库重建更快。

并发模式允许在重建期间继续操作。索引保持可用，但重建速度较慢。

并行任务可加速多表重建。每张表单独建立索引。

# CAVEATS

非并发重建期间会锁定表。大型索引耗时较长。需要足够的磁盘空间。

# HISTORY

**reindexdb** 是 **PostgreSQL** 的组成部分，为 REINDEX SQL 命令提供命令行入口。它简化了数据库维护操作。

# INSTALL

```apk: sudo apk add postgresql17-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vacuumdb](/man/vacuumdb)(1), [psql](/man/psql)(1), [pg_dump](/man/pg_dump)(1)
