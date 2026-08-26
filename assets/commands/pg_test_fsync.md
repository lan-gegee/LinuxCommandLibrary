# TAGLINE

对多种 fsync 方法进行基准测试

# TLDR

**测试 fsync 方法**

```pg_test_fsync```

**使用指定文件测试**

```pg_test_fsync -f [testfile]```

# SYNOPSIS

**pg_test_fsync** [_options_]

# PARAMETERS

**-f**, **--filename** _file_
> 测试文件路径。

**-s**, **--secs-per-test** _n_
> 每项测试持续的秒数。

# DESCRIPTION

**pg_test_fsync** 对当前平台上可用的 fsync/flush 方法进行基准测试，报告每种方法每秒的操作数。测试结果可用于指导 PostgreSQL `wal_sync_method`（如 `fsync`、`fdatasync`、`open_sync`、`open_datasync`）的选择。请在承载 WAL 的真实文件系统上运行，才能得到有意义的数据；缓存或虚拟化的存储会使结果失真。

# CAVEATS

需要对目标目录有写权限。结果会受到缓存层（硬件、虚拟化、文件系统）的影响——要在真实生产存储上进行基准测试以获得准确的比较结果。

# INSTALL

```dnf: sudo dnf install postgresql17```

```apk: sudo apk add postgresql17```

```zypper: sudo zypper install postgresql17```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pg_test_timing](/man/pg_test_timing)(1), [postgres](/man/postgres)(1)
