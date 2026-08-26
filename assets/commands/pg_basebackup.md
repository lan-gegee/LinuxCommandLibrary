# TAGLINE

创建 PostgreSQL 集群的基础备份

# TLDR

**创建备份**

```pg_basebackup -D [backup_dir] -h [host] -U [user]```

**带进度显示地备份**

```pg_basebackup -D [backup_dir] -P```

**备份为 tar 格式**

```pg_basebackup -D [backup_dir] -Ft```

**以 WAL 流方式备份**

```pg_basebackup -D [backup_dir] -X stream```

# SYNOPSIS

**pg_basebackup** [_options_]

# PARAMETERS

**-D**, **--pgdata** _dir_
> 备份的目标位置。

**-h**, **--host** _host_
> 数据库服务器主机。

**-U**, **--username** _user_
> 数据库用户。

**-P**, **--progress**
> 显示进度。

**-F**, **--format** _fmt_
> 输出格式（p=plain，t=tar）。

**-X**, **--wal-method** _method_
> WAL 包含方式（fetch、stream、none）。

**-z**
> 压缩 tar 输出。

**-Z** _level_
> 压缩级别。

# DESCRIPTION

**pg_basebackup** 创建 PostgreSQL 集群的基础备份。它是时间点恢复和流复制搭建的基础。包含全部数据库文件。

# INSTALL

```apk: sudo apk add postgresql17-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pg_dump](/man/pg_dump)(1), [pg_restore](/man/pg_restore)(1)
