# TAGLINE

显示 WAL 摘要文件的内容

# TLDR

**显示 WAL 摘要**

```pg_walsummary [summary_file]```

**显示逐块明细**

```pg_walsummary -i [summary_file]```

**校验 WAL 摘要文件而不打印内容**

```pg_walsummary -q [summary_file]```

# SYNOPSIS

**pg_walsummary** [_options_] [_file_...]

# PARAMETERS

**-i**, **--individual**
> 为每个被修改的块单独打印一行，而不是把连续的块合并成范围。

**-q**, **--quiet**
> 除错误信息外不打印任何输出。可用于验证文件能否被解析。

**-V**, **--version**
> 显示版本信息后退出。

# DESCRIPTION

**pg_walsummary** 用于打印 WAL 摘要文件的内容。这些二进制文件位于数据目录的 pg_wal/summaries 子目录中，记录了哪些块被修改过，为 PostgreSQL 17 引入的增量备份功能提供支持。

# INSTALL

```dnf: sudo dnf install postgresql17```

```apk: sudo apk add postgresql17```

```zypper: sudo zypper install postgresql17```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pg_waldump](/man/pg_waldump)(1), [pg_combinebackup](/man/pg_combinebackup)(1), [pg_basebackup](/man/pg_basebackup)(1)
