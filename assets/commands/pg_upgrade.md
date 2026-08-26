# TAGLINE

将 PostgreSQL 原地升级到新的主版本

# TLDR

**升级集群**

```pg_upgrade -b [old_bindir] -B [new_bindir] -d [old_datadir] -D [new_datadir]```

**只检查兼容性而不升级**

```pg_upgrade --check -b [old_bindir] -B [new_bindir] -d [old_datadir] -D [new_datadir]```

**使用硬链接加速升级**

```pg_upgrade --link -b [old_bindir] -B [new_bindir] -d [old_datadir] -D [new_datadir]```

**使用文件克隆升级**（reflinks，近乎瞬时）

```pg_upgrade --clone -b [old_bindir] -B [new_bindir] -d [old_datadir] -D [new_datadir]```

**使用并行作业升级**

```pg_upgrade -j [4] -b [old_bindir] -B [new_bindir] -d [old_datadir] -D [new_datadir]```

# SYNOPSIS

**pg_upgrade** [_options_]

# PARAMETERS

**-b**, **--old-bindir** _dir_
> 旧版 PostgreSQL 可执行文件目录。

**-B**, **--new-bindir** _dir_
> 新版 PostgreSQL 可执行文件目录。默认为 pg_upgrade 所在目录。

**-d**, **--old-datadir** _dir_
> 旧数据库集群的配置目录。

**-D**, **--new-datadir** _dir_
> 新数据库集群的配置目录。

**-c**, **--check**
> 仅检查集群，不改动任何数据。

**-k**, **--link**
> 使用硬链接代替将文件复制到新集群。

**--clone**
> 使用高效的文件克隆（reflink）代替复制。在支持的文件系统（Btrfs、XFS、macOS APFS）上几乎瞬时完成。

**--copy**
> 将文件复制到新集群。这是默认行为。

**-j**, **--jobs** _njobs_
> 用于并行复制/链接文件以及并行转储/恢复模式的并发进程数量。

**-p**, **--old-port** _port_
> 旧集群的端口号。

**-P**, **--new-port** _port_
> 新集群的端口号。

**-U**, **--username** _name_
> 集群的安装用户名。

**-r**, **--retain**
> 即使成功完成后也保留 SQL 和日志文件。

**-s**, **--socketdir** _dir_
> 升级期间 postmaster 套接字所在的目录。默认为当前工作目录。

**-N**, **--no-sync**
> 不等待文件安全地写入磁盘。

**-v**, **--verbose**
> 启用详细的内部日志记录。

**-o**, **--old-options** _options_
> 直接传递给旧 postgres 命令的选项。

**-O**, **--new-options** _options_
> 直接传递给新 postgres 命令的选项。

# DESCRIPTION

**pg_upgrade** 可将 PostgreSQL 原地升级到新的主版本。对于大型数据库而言比转储/恢复更快，并尽可能保留数据文件。务必先使用 **--check** 运行以验证兼容性，再执行实际升级。

# INSTALL

```dnf: sudo dnf install postgresql17```

```apk: sudo apk add postgresql17```

```zypper: sudo zypper install postgresql17```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pg_dump](/man/pg_dump)(1), [pg_restore](/man/pg_restore)(1), [pg_ctl](/man/pg_ctl)(1), [pg_dumpall](/man/pg_dumpall)(1)
