# TAGLINE

用于初始化、启动、停止和控制 PostgreSQL 的实用工具

# TLDR

**启动 PostgreSQL**

```pg_ctl start -D [/var/lib/postgresql/data]```

**停止 PostgreSQL**

```pg_ctl stop -D [/var/lib/postgresql/data]```

**重启 PostgreSQL**

```pg_ctl restart -D [/var/lib/postgresql/data]```

**重新加载配置**

```pg_ctl reload -D [/var/lib/postgresql/data]```

**检查状态**

```pg_ctl status -D [/var/lib/postgresql/data]```

# SYNOPSIS

**pg_ctl** _action_ [**-D** _datadir_] [_options_]

# PARAMETERS

**start**
> 启动服务器。

**stop**
> 停止服务器。

**restart**
> 先停止再启动。

**reload**
> 重新加载配置。

**status**
> 检查服务器状态。

**-D** _directory_
> 数据目录。

**-m** _mode_
> 关机模式（smart、fast、immediate）。

**-l** _file_
> 日志文件。

**-w**
> 等待操作完成。

# DESCRIPTION

**pg_ctl** 是用于初始化、启动、停止和控制 PostgreSQL 数据库服务器的工具。它是管理 PostgreSQL 服务的首选方法。
# 以日志启动
pg_ctl start -D /data -l /var/log/postgresql.log

# 快速关机
pg_ctl stop -D /data -m fast

# 初始化新集群
pg_ctl initdb -D /data

# 提升备库
pg_ctl promote -D /data
```

# SHUTDOWN MODES

```
smart     - Wait for clients to disconnect
fast      - Rollback active transactions (default)
immediate - Abort immediately (may corrupt)
```

# CAVEATS

必须以 PostgreSQL 用户身份运行。需要数据目录。systemd 系统上可改用 systemctl。

# HISTORY

pg_ctl 是 **PostgreSQL** 的一部分，后者是一款开源数据库，最早源于加州大学伯克利分校的 POSTGRES 项目。

# SEE ALSO

[postgres](/man/postgres)(1), [pg_dump](/man/pg_dump)(1), [pg_restore](/man/pg_restore)(1), [initdb](/man/initdb)(1)

# INSTALL

```dnf: sudo dnf install postgresql17```

```apk: sudo apk add postgresql17```

```zypper: sudo zypper install postgresql17```

<!-- packages: 2026-07-22 -->
