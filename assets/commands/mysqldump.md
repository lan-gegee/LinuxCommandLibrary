# TAGLINE

创建 MySQL 数据库的逻辑备份

# TLDR

**转储数据库**

```mysqldump -u [user] -p [database] > [backup.sql]```

**转储指定的表**

```mysqldump -u [user] -p [database] [table1] [table2] > [backup.sql]```

**转储所有数据库**

```mysqldump -u [user] -p --all-databases > [all.sql]```

**压缩转储**

```mysqldump -u [user] -p [database] | gzip > [backup.sql.gz]```

**只转储结构**（不含数据）

```mysqldump -u [user] -p --no-data [database] > [schema.sql]```

**只转储数据**（不含结构）

```mysqldump -u [user] -p --no-create-info [database] > [data.sql]```

**连同存储过程和触发器一起转储**

```mysqldump -u [user] -p --routines --triggers [database] > [backup.sql]```

**用于复制的转储**

```mysqldump -u [user] -p --single-transaction --master-data [database] > [backup.sql]```

# SYNOPSIS

**mysqldump** [_-u user_] [_-p_] [_--all-databases_] [_--single-transaction_] [_options_] [_database_] [_tables_]

# PARAMETERS

**-u** _USER_, **--user** _USER_
> MySQL 用户名。

**-p**[_PASSWORD_], **--password**[=_PASS_]
> 提示输入或指定密码。

**-h** _HOST_, **--host** _HOST_
> 服务器主机名。

**-P** _PORT_, **--port** _PORT_
> 服务器端口。

**--all-databases**, **-A**
> 转储所有数据库。

**--databases**, **-B**
> 转储多个指定名称的数据库。

**--no-data**, **-d**
> 不转储表数据。

**--no-create-info**, **-t**
> 不转储 CREATE TABLE 语句。

**--single-transaction**
> 为 InnoDB 提供一致性快照。

**--routines**, **-R**
> 包含存储过程/函数。

**--triggers**
> 包含触发器（默认开启）。

**--events**, **-E**
> 包含事件。

**--add-drop-table**
> 在 CREATE 之前添加 DROP TABLE。

**--add-drop-database**
> 在 CREATE 之前添加 DROP DATABASE。

**--master-data**[=_VALUE_]
> 包含二进制日志位置。

**--quick**, **-q**
> 不做缓冲，直接写入。

**--lock-tables**, **-l**
> 转储期间锁定表。

# DESCRIPTION

**mysqldump** 创建 MySQL 数据库的逻辑备份。其输出是 SQL 语句，执行后可以重建数据库的结构和数据。

--single-transaction 选项为 InnoDB 表提供不锁表的一致性备份。它会启动一个事务并在该时间点转储数据，允许其他操作继续进行。

对于 MyISAM 或混合存储引擎，--lock-tables 可在转储期间阻止写入。这保证了一致性，但会阻塞写入。

默认情况下不包括存储例程（存储过程、函数）和事件。要备份这些对象，需显式使用 --routines 和 --events。

--master-data 选项会记录二进制日志坐标，这是配置复制从库或进行基于时间点恢复的关键。

输出是纯 SQL 文本，可用 gzip 轻松压缩。对于超大型数据库，可考虑 mysqlpump（并行）或 Percona XtraBackup 等物理备份工具。

# CAVEATS

不适合超大型数据库——应考虑物理备份。不使用 --quick 时内存占用可能很高。恢复耗时可能较长。可能出现字符集问题。二进制数据以 SQL 形式编码。加锁可能影响生产环境。

# HISTORY

**mysqldump** 自早期版本起就是 MySQL 的组成部分，由 MySQL AB 开发，后来归属 Oracle。它仍是 MySQL 和 MariaDB 的标准逻辑备份工具。虽然大型数据库更倾向于使用物理备份工具，但 mysqldump 凭借简单和可移植的特点依然广受欢迎。

# INSTALL

```apt: sudo apt install mariadb-client```

```apk: sudo apk add mariadb-client```

```zypper: sudo zypper install mariadb-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mysql](/man/mysql)(1), [pg_dump](/man/pg_dump)(1)
