# TAGLINE

将一个 PostgreSQL 数据目录与另一份副本同步

# TLDR

**针对正在运行的源服务器执行回退**

```pg_rewind -D [target_dir] --source-server="host=[host] user=[rewind_user] dbname=[postgres]"```

**针对本地已关闭的源执行回退**

```pg_rewind -D [target_dir] --source-pgdata=[source_dir]```

**试运行**（不写入任何更改）

```pg_rewind -n -D [target_dir] --source-server="[conninfo]"```

**回退并写入恢复配置**用于备机模式

```pg_rewind -R -D [target_dir] --source-server="[conninfo]"```

复制数据时**显示进度**

```pg_rewind -P -D [target_dir] --source-pgdata=[source_dir]```

从归档中**恢复缺失的 WAL 文件**

```pg_rewind -c -D [target_dir] --source-server="[conninfo]"```

# SYNOPSIS

**pg_rewind** [_option_...] **{-D** | **--target-pgdata}** _directory_ **{--source-pgdata**=_directory_ | **--source-server**=_connstr_**}**

# PARAMETERS

**-D**, **--target-pgdata** _dir_
> 要修改的目标数据目录。必须是干净关闭的状态。

**--source-pgdata** _dir_
> 干净关闭的源集群的文件系统路径。

**--source-server** _connstr_
> 正在运行的源服务器的 libpq 连接字符串。

**-n**, **--dry-run**
> 执行全部工作但不修改目标目录。

**-N**, **--no-sync**
> 不等待更改刷入磁盘即返回。

**-P**, **--progress**
> 复制文件时显示进度。

**-R**, **--write-recovery-conf**
> 创建 `standby.signal` 并将连接设置追加到 `postgresql.auto.conf`。

**-c**, **--restore-target-wal**
> 使用 `restore_command` 获取 `pg_wal` 中缺失的 WAL 文件。

**--config-file** _file_
> 目标集群的主服务器配置文件。

**--no-ensure-shutdown**
> 不运行单用户恢复；如果目标不是干净关闭状态则失败。

**--sync-method** _method_
> 用于刷新更改的方法：`fsync`（默认）或 `syncfs`。

**--debug**
> 输出详细的调试信息。

**-V**, **--version**
> 打印版本信息。

**-?**, **--help**
> 显示帮助。

# DESCRIPTION

**pg_rewind** 用于在时间线分叉之后，将一个 PostgreSQL 数据目录与同一集群的另一份副本重新同步。典型用途是在故障转移后，把原主库（former primary）重新作为备机接入，而无需执行完整的基础备份。

它会找到时间线分叉的点，然后仅从源复制目标在该点之后发生变化的块，以及所有当前的配置、WAL 和其他所需文件。源必须启用 `wal_log_hints` 或在初始化时启用了数据校验和，并且 `full_page_writes` 必须处于开启状态。

# CAVEATS

目标集群必须干净关闭。源必须与目标处于相同的大版本并共享相同的系统标识符。复制槽、统计信息以及 `pg_dynshmem` 的内容不会被复制。在生产数据上运行 pg_rewind 前，务必先备份目标。

# HISTORY

由 Heikki Linnakangas 在 PostgreSQL **9.5**（2016 年）中引入，从一个 contrib 模块并入核心发行版。在 PostgreSQL **13** 中，pg_rewind 新增了写入恢复配置（`-R`）以及从归档恢复缺失 WAL（`-c`）的能力。

# INSTALL

```dnf: sudo dnf install postgresql17```

```apk: sudo apk add postgresql17```

```zypper: sudo zypper install postgresql17```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pg_basebackup](/man/pg_basebackup)(1), [pg_resetwal](/man/pg_resetwal)(1)
