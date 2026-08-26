# TAGLINE

重置预写日志和控制信息

# TLDR

**重置 WAL（试运行）**

```pg_resetwal -n [data_dir]```

**重置 WAL**

```pg_resetwal [data_dir]```

**强制重置**

```pg_resetwal -f [data_dir]```

# SYNOPSIS

**pg_resetwal** [_options_] [**-D**] _datadir_

# PARAMETERS

**-D**, **--pgdata** _dir_
> 数据目录。

**-n**, **--dry-run**
> 只显示将要执行的操作。

**-f**, **--force**
> 强制重置。

**-e**, **--epoch** _epoch_
> 设置下一个事务 ID 纪元。

**-x**, **--next-transaction-id** _xid_
> 设置下一个事务 ID。

**-o**, **--next-oid** _oid_
> 设置下一个 OID。

**-m**, **--multixact-ids** _mxid,mxid_
> 设置下一个和最旧的多事务 ID。

**-O**, **--multixact-offset** _mxoff_
> 设置下一个多事务偏移量。

**-c**, **--commit-timestamp-ids** _xid,xid_
> 设置提交时间戳所对应的最旧和最新事务 ID。

**-u**, **--oldest-transaction-id** _xid_
> 设置最旧的未冻结事务 ID。

**-l**, **--next-wal-file** _walfile_
> 强制设定最小的 WAL 起始位置。

**--wal-segsize** _size_
> 以 MB 为单位设置 WAL 段大小。

# DESCRIPTION

**pg_resetwal** 用于重置预写日志（WAL）和控制信息。这是 WAL 损坏时的最后手段式恢复方法。可能造成数据丢失。运行前必须停止服务器。

# CAVEATS

只有在 WAL 损坏或 pg_controldata 显示数据不一致时，才把它当作最后手段使用。可能引起数据丢失和事务完整性问题。运行之前必须先停止 PostgreSQL 服务器。

# INSTALL

```dnf: sudo dnf install postgresql17```

```apk: sudo apk add postgresql17```

```zypper: sudo zypper install postgresql17```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pg_controldata](/man/pg_controldata)(1), [pg_rewind](/man/pg_rewind)(1)
