# TAGLINE

用于备份 PostgreSQL 数据库的工具

# TLDR

**转储数据库**

```pg_dump [database_name] > [backup.sql]```

**以压缩方式转储**

```pg_dump -Fc [database_name] > [backup.dump]```

**转储特定表**

```pg_dump -t [table_name] [database_name] > [table.sql]```

**只转储模式**

```pg_dump -s [database_name] > [schema.sql]```

**只转储数据**

```pg_dump -a [database_name] > [data.sql]```

**带连接参数转储**

```pg_dump -h [host] -p [5432] -U [username] [database_name] > [backup.sql]```

**以目录格式转储**（并行）

```pg_dump -Fd -j [4] [database_name] -f [backup_dir]```

**排除表后转储**

```pg_dump --exclude-table=[pattern] [database_name] > [backup.sql]```

# SYNOPSIS

**pg_dump** [_options_] [_dbname_]

# DESCRIPTION

**pg_dump** 是用于备份 PostgreSQL 数据库的工具。即使在数据库正被使用的情况下，它也能在转储开始的那一刻创建数据库的一致性快照。

输出可以是 SQL 脚本格式（纯文本），也可以是支持压缩和并行恢复的自定义归档格式。SQL 脚本用 psql 恢复，归档格式则使用 pg_restore。

pg_dump 在转储过程中不会阻塞读取方或写入方，因此适合生产环境的备份。

# PARAMETERS

**-F** _format_
> 输出格式（p=plain，c=custom，d=directory，t=tar）。

**-f** _file_
> 输出文件或目录。

**-t** _table_
> 转储特定的表。

**-T** _table_
> 排除特定的表。

**-n** _schema_
> 转储特定的模式。

**-N** _schema_
> 排除特定的模式。

**-s**, **--schema-only**
> 只转储模式，不含数据。

**-a**, **--data-only**
> 只转储数据，不含模式。

**-c**, **--clean**
> 包含 DROP 命令。

**-C**, **--create**
> 包含 CREATE DATABASE 命令。

**-j** _jobs_
> 并行转储的任务数（目录格式）。

**-h** _host_
> 数据库服务器主机。

**-p** _port_
> 数据库服务器端口。

**-U** _user_
> 以该用户身份连接。

**-W**
> 强制提示输入密码。

**-Z** _level_
> 压缩级别（0-9）。

# CAVEATS

不会转储角色和表空间（那要用 pg_dumpall）。纯文本格式无法并行恢复。大型数据库建议使用自定义格式。大型数据库可能需要大量磁盘空间。

# HISTORY

**pg_dump** 自 PostgreSQL 最早的发布以来就是其中一部分，源自 **20 世纪 80 年代**加州大学伯克利分校的原始 **POSTGRES** 项目。随着 PostgreSQL 成长为主流数据库系统，它陆续获得了并行转储、自定义归档格式和选择性备份选项等特性。

# INSTALL

```apk: sudo apk add postgresql17-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pg_restore](/man/pg_restore)(1), [pg_dumpall](/man/pg_dumpall)(1), [psql](/man/psql)(1), [createdb](/man/createdb)(1)
