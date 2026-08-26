# TAGLINE

移除备库不再需要的旧 WAL 归档文件

# TLDR

**清理旧的 WAL 文件**

```pg_archivecleanup [archive_dir] [oldest_kept_wal]```

**试运行**

```pg_archivecleanup -n [archive_dir] [oldest_kept_wal]```

**清理时剥离扩展名**

```pg_archivecleanup -x .gz [archive_dir] [oldest_kept_wal]```

# SYNOPSIS

**pg_archivecleanup** [_options_] _archivelocation_ _oldestkeptwalfile_

# PARAMETERS

**-b**, **--clean-backup-history**
> 同时删除备份历史文件。

**-d**, **--debug**
> 在 stderr 上打印调试日志输出。

**-n**, **--dry-run**
> 打印将被删除的文件名（试运行）。

**-V**, **--version**
> 显示版本并退出。

**-x**, **--strip-extension** _extension_
> 在判断是否删除前，从文件名中剥去此扩展名。对压缩归档（如 .gz、.bz2）很有用。

**-?**, **--help**
> 显示帮助并退出。

# DESCRIPTION

**pg_archivecleanup** 移除备库不再需要的旧 WAL 归档文件。它通常作为 **postgresql.conf**（旧版本中是 recovery.conf）里的 **archive_cleanup_command** 使用。它会删除所有早于指定 _oldestkeptwalfile_ 的 WAL 文件。

# INSTALL

```dnf: sudo dnf install postgresql17```

```apk: sudo apk add postgresql17```

```zypper: sudo zypper install postgresql17```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pg_basebackup](/man/pg_basebackup)(1), [pg_receivewal](/man/pg_receivewal)(1)
