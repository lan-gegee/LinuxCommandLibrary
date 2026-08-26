# TAGLINE

将增量备份与全量备份合并

# TLDR

**合并增量备份**

```pg_combinebackup [full_backup] [incr_backup] -o [output_dir]```

**合并多个增量备份**

```pg_combinebackup [full] [incr1] [incr2] -o [output]```

# SYNOPSIS

**pg_combinebackup** [_options_] _backup_dir_... **-o** _output_dir_

# PARAMETERS

**-o**, **--output** _dir_
> 合并结果备份的输出目录。必须尚不存在。

**-n**, **--dry-run**
> 只显示将要执行的操作，不实际写入输出。

**-T** _olddir=newdir_
> 在合并过程中重定位表空间目录。

**--no-sync**
> 跳过对输出目录的 fsync（更快但不太安全）。

**--sync-method** _method_
> 同步方法：**fsync**（默认）或 **syncfs**。

**--manifest-checksums** _algorithm_
> 备份清单的校验和算法：**CRC32C**（默认）、**SHA224**、**SHA256**、**SHA384**、**SHA512** 或 **NONE**。

**--no-manifest**
> 不在输出中生成备份清单。

**-d**, **--debug**
> 打印调试输出。

**-V**, **--version**
> 显示版本并退出。

# DESCRIPTION

**pg_combinebackup** 把基础（全量）备份与一个或多个由 **pg_basebackup --incremental** 生成的增量备份合并，重建出完整的备份。各备份目录必须按时间先后顺序列出：先是全量备份，然后按生成顺序排列各个增量备份。

输出是一个合成的全量备份，可以直接配合 **pg_restore** 使用，也可以作为将来增量备份的新的基础。于 PostgreSQL 17 引入。

# CAVEATS

输出目录必须不存在。备份链中的所有备份都必须齐全并按顺序列出。全量备份必须是带 **--manifest**（默认行为）生成的。增量备份支持要求 PostgreSQL 17 或更高版本。

# INSTALL

```dnf: sudo dnf install postgresql17```

```apk: sudo apk add postgresql17```

```zypper: sudo zypper install postgresql17```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pg_basebackup](/man/pg_basebackup)(1)
