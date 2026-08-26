# TAGLINE

提取所有 PostgreSQL 数据库，包括角色等集群级对象

# TLDR

**转储所有数据库**

```pg_dumpall > [backup.sql]```

**只转储角色和表空间**

```pg_dumpall --globals-only > [globals.sql]```

**从特定主机转储**

```pg_dumpall -h [hostname] -U [username] > [backup.sql]```

**压缩备份**

```pg_dumpall | gzip > [backup.sql.gz]```

# SYNOPSIS

**pg_dumpall** [_options_]

# PARAMETERS

**-h**, **--host** _host_
> 数据库服务器主机。

**-U**, **--username** _name_
> 以该用户身份连接。

**-p**, **--port** _port_
> 服务器端口。

**-g**, **--globals-only**
> 仅限角色和表空间。

**-r**, **--roles-only**
> 仅限角色。

**-t**, **--tablespaces-only**
> 仅限表空间。

**--clean**
> 添加 DROP 语句。

**-f** _file_
> 输出文件。

# DESCRIPTION

**pg_dumpall** 提取所有 PostgreSQL 数据库，包括角色和表空间等集群级对象。与 pg_dump 不同，它面向的是整个集群。

输出是一个可以用 psql 恢复的 SQL 脚本。
# 全集群备份
pg_dumpall -U postgres > all_databases.sql

# 备份全局对象以便恢复
pg_dumpall -g > globals.sql

# 从备份恢复
psql -U postgres -f all_databases.sql

# 指定编码
pg_dumpall -E UTF8 > backup.sql
```

# CAVEATS

输出只能是纯 SQL（不支持自定义格式）。对于大型数据库，建议按库分别使用 pg_dump。完整备份需要超级用户权限。

# HISTORY

pg_dumpall 属于 **PostgreSQL**，自早期版本起就一直提供集群级的备份能力。

# SEE ALSO

[pg_dump](/man/pg_dump)(1), [pg_restore](/man/pg_restore)(1), [psql](/man/psql)(1), [postgres](/man/postgres)(1)

# INSTALL

```apk: sudo apk add postgresql17-client```

<!-- packages: 2026-07-22 -->
