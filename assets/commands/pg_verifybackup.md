# TAGLINE

校验 PostgreSQL 集群基础备份的完整性

# TLDR

**校验一个备份**

```pg_verifybackup [backup_dir]```

**校验并显示进度**

```pg_verifybackup -P [backup_dir]```

**跳过 WAL 校验**

```pg_verifybackup -n [backup_dir]```

**跳过数据文件校验和校验**（更快）

```pg_verifybackup -s [backup_dir]```

**使用来自其他位置的清单文件**

```pg_verifybackup -m [/path/to/backup_manifest] [backup_dir]```

**使用单独目录中的 WAL 文件进行校验**

```pg_verifybackup -w [/path/to/wal_dir] [backup_dir]```

# SYNOPSIS

**pg_verifybackup** [_options_] _backupdir_

# PARAMETERS

**-e**, **--exit-on-error**
> 一旦检测到问题就立即退出，而不是继续报告所有错误。

**--ignore**=_path_
> 与清单比对时忽略指定的文件或目录（相对路径）。

**-m** _path_, **--manifest-path**=_path_
> 使用指定路径的清单文件，而不是备份根目录下的清单。

**-n**, **--no-parse-wal**
> 跳过解析恢复所需的预写日志（WAL）数据。

**-P**, **--progress**
> 校验校验和时显示进度。不能与 `--quiet` 同用。

**-q**, **--quiet**
> 备份成功通过校验时不打印任何内容。

**-s**, **--skip-checksums**
> 跳过数据文件校验和校验。文件的存在性和大小仍会被检查。

**-w** _dir_, **--wal-directory**=_dir_
> 从指定目录解析 WAL 文件，而不是备份中的 `pg_wal`。

# DESCRIPTION

**pg_verifybackup** 用于校验通过 **pg_basebackup** 创建的备份的完整性。它会检查备份清单是否完整，并验证文件的校验和。在备份完成后运行此工具有助于确保备份可恢复。

默认情况下，它还会解析从备份恢复所需的全部 WAL 文件，以确认它们存在且未损坏。

# INSTALL

```apk: sudo apk add postgresql17-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pg_basebackup](/man/pg_basebackup)(1), [pg_dump](/man/pg_dump)(1)
