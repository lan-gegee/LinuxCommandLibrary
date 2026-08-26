# TAGLINE

显示 PostgreSQL 集群控制信息

# TLDR

**显示集群控制数据**

```pg_controldata [data_dir]```

**通过 PGDATA 环境变量显示**

```pg_controldata```

# SYNOPSIS

**pg_controldata** [_option_] [**-D**] _datadir_

# PARAMETERS

**-D**, **--pgdata** _dir_
> 数据目录。

# DESCRIPTION

**pg_controldata** 显示 PostgreSQL 集群的控制信息。包括 WAL 位置、检查点信息和数据库状态。对灾难恢复和调试很有帮助。

# INSTALL

```dnf: sudo dnf install postgresql17```

```apk: sudo apk add postgresql17```

```zypper: sudo zypper install postgresql17```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pg_resetwal](/man/pg_resetwal)(1), [pg_rewind](/man/pg_rewind)(1)
