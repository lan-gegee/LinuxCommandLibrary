# TAGLINE

把 WAL 从服务器流式传送到归档

# TLDR

**从远程服务器接收 WAL**并保存到目录

```pg_receivewal -D [wal_dir] -h [host] -U [username]```

**使用复制槽接收**

```pg_receivewal -D [wal_dir] -S [slot_name] -h [host]```

**创建复制槽**然后退出

```pg_receivewal -D [wal_dir] -S [slot_name] --create-slot -h [host]```

**以 gzip 压缩方式接收**

```pg_receivewal -D [wal_dir] -Z [gzip:5] -h [host]```

**遇到连接错误时不循环重试**

```pg_receivewal -D [wal_dir] -n -h [host]```

# SYNOPSIS

**pg_receivewal** [_options_]

# PARAMETERS

**-D**, **--directory** _dir_
> WAL 目标目录（必需）。

**-h**, **--host** _host_
> 服务器主机名或套接字目录。

**-p**, **--port** _port_
> 服务器端口号。

**-U**, **--username** _name_
> 用于连接的用户名。

**-S**, **--slot** _name_
> 使用某个复制槽。

**-Z**, **--compress** _method[:detail]_
> 压缩方法及可选级别（gzip、lz4 或 none）。

**-n**, **--no-loop**
> 遇到连接错误不重试；立即退出。

**-s**, **--status-interval** _seconds_
> 状态包发送间隔的秒数（默认：10）。

**-E**, **--endpos** _lsn_
> 在指定的 LSN 处停止复制。

**--create-slot**
> 创建一个新的物理复制槽，然后退出。

**--drop-slot**
> 删除指定名称的复制槽，然后退出。

**--if-not-exists**
> 与 --create-slot 同用时，若槽已存在则不报错。

**--synchronous**
> 收到 WAL 数据后立即刷写到磁盘。

**--no-sync**
> 不强制把 WAL 数据刷写到磁盘。

# DESCRIPTION

**pg_receivewal** 把 WAL 从服务器流式传输到归档位置。可为时间点恢复建立连续的 WAL 归档。是 archive_command 做 WAL 归档的一种替代方案。

# INSTALL

```apk: sudo apk add postgresql17-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pg_basebackup](/man/pg_basebackup)(1), [pg_archivecleanup](/man/pg_archivecleanup)(1), [pg_recvlogical](/man/pg_recvlogical)(1)
