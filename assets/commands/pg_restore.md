# TAGLINE

从 pg_dump 创建的归档中恢复 PostgreSQL 数据库

# TLDR

**从自定义格式恢复**

```pg_restore -d [database] [backup.dump]```

**恢复特定表**

```pg_restore -d [database] -t [tablename] [backup.dump]```

**列出备份的内容**

```pg_restore -l [backup.dump]```

**并行恢复**

```pg_restore -d [database] -j [4] [backup.dump]```

**恢复前先清理**

```pg_restore -d [database] -c [backup.dump]```

# SYNOPSIS

**pg_restore** [_options_] [_file_]

# PARAMETERS

**-d**, **--dbname** _name_
> 要恢复到的数据库。

**-t**, **--table** _name_
> 恢复特定的表。

**-n**, **--schema** _name_
> 恢复特定的模式。

**-j**, **--jobs** _num_
> 并行任务数。

**-c**, **--clean**
> 在创建对象前先删除它们。

**-C**, **--create**
> 创建数据库。

**-l**, **--list**
> 列出归档内容。

**-L** _file_
> 使用指定的目录清单文件。

# DESCRIPTION

**pg_restore** 从 pg_dump 生成的自定义、目录或 tar 格式归档中恢复 PostgreSQL 数据库。它无法恢复纯 SQL 格式的转储（那种请用 psql）。

该工具可以借助目录清单文件有选择地恢复对象，能够并行执行多个任务（仅限目录格式），还可以在恢复前按需创建目标数据库。

# CAVEATS

无法恢复纯 SQL 转储。并行恢复要求目录格式。某些对象可能需要超级用户权限。

# HISTORY

pg_restore 属于 **PostgreSQL**，与 pg_dump 相辅相成，负责自定义格式备份的恢复。

# INSTALL

```apk: sudo apk add postgresql17-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pg_dump](/man/pg_dump)(1), [pg_dumpall](/man/pg_dumpall)(1), [psql](/man/psql)(1)
