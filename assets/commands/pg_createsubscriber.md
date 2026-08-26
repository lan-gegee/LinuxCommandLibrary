# TAGLINE

将物理备库转换为逻辑复制订阅端

# TLDR

**把已停止的备库转换为逻辑订阅端**

```pg_createsubscriber -d [dbname] -D [standby_data_dir] -P "[host=primary dbname=app]"```

**只预览将要执行的操作，不做任何更改**

```pg_createsubscriber --dry-run -d [dbname] -D [standby_data_dir] -P "[host=primary dbname=app]"```

**一次转换多个数据库**

```pg_createsubscriber -d [db1] -d [db2] -D [standby_data_dir] -P "[host=primary]"```

# SYNOPSIS

**pg_createsubscriber** [_options_] **-D** _datadir_ **-P** _conninfo_ **-d** _dbname_

# PARAMETERS

**-d**, **--database** _name_
> 为其设置逻辑复制的数据库。有多个数据库时可重复使用。

**-D**, **--pgdata** _dir_
> 目标（备库）服务器的数据目录。服务器必须处于停止状态。

**-P**, **--publisher-server** _conninfo_
> 源（发布者）服务器的连接字符串。

**-p**, **--subscriber-port** _port_
> 目标订阅端服务器在配置期间监听的端口。

**-U**, **--subscriber-username** _name_
> 连接目标订阅端所用的用户名。

**-s**, **--socketdir** _dir_
> 目标服务器 postmaster 套接字所在的目录（默认：当前目录）。

**--publication** _name_
> 要在发布者上创建的发布（publication）名称。可重复使用以对应多个数据库。

**--subscription** _name_
> 要在订阅端创建的订阅（subscription）名称。可重复使用以对应多个数据库。

**--replication-slot** _name_
> 逻辑复制使用的复制槽名称。可重复使用以对应多个数据库。

**-t**, **--recovery-timeout** _seconds_
> 等待备库追平进度的最长秒数，超过即失败。

**-n**, **--dry-run**
> 显示将要执行的操作，但不做任何更改。

**-v**, **--verbose**
> 启用详细输出（重复使用可获得更多细节）。

# DESCRIPTION

**pg_createsubscriber** 把物理备库转换为逻辑复制订阅端。它将现有的流复制备库改造为订阅原主库上发布内容的节点，避免了重新进行一次完整的初始数据拷贝。

运行该工具之前必须停止目标备库。内部它会借助 **pg_ctl** 启动和停止目标服务器，以创建发布、订阅和复制槽。当给出多个 `--database`、`--publication`、`--subscription` 或 `--replication-slot` 选项时，它们的数量和顺序必须一一对应。于 PostgreSQL 17 引入。

# CAVEATS

目标服务器必须是一个曾经运行过、如今已停止的物理备库，转换期间不得被使用。如果指定了 `--publication`、`--subscription` 和 `--replication-slot` 的值，其数量必须与 `--database` 的值相匹配。请务必先用 `--dry-run` 测试。

# INSTALL

```dnf: sudo dnf install postgresql17```

```apk: sudo apk add postgresql17```

```zypper: sudo zypper install postgresql17```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pg_basebackup](/man/pg_basebackup)(1)
