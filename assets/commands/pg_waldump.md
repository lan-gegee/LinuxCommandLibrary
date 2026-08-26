# TAGLINE

以人类可读的格式显示 WAL 文件内容

# TLDR

**转储 WAL 文件**

```pg_waldump [walfile]```

**转储并显示记录详情**

```pg_waldump -r [record_type] [walfile]```

**转储指定范围**

```pg_waldump -s [start_lsn] -e [end_lsn] [walfile]```

# SYNOPSIS

**pg_waldump** [_options_] [_startseg_] [_endseg_]

# PARAMETERS

**-p**, **--path** _dir_
> WAL 目录。

**-r**, **--rmgr** _name_
> 按资源管理器过滤。

**-s**, **--start** _lsn_
> 起始 LSN。

**-e**, **--end** _lsn_
> 结束 LSN。

**-n**, **--limit** _n_
> 限制记录数量。

# DESCRIPTION

**pg_waldump** 以人类可读的格式显示 WAL 文件内容，展示事务细节和操作。可用于调试和理解 WAL 活动。

# INSTALL

```dnf: sudo dnf install postgresql17```

```apk: sudo apk add postgresql17```

```zypper: sudo zypper install postgresql17```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pg_walsummary](/man/pg_walsummary)(1), [pg_receivewal](/man/pg_receivewal)(1)
