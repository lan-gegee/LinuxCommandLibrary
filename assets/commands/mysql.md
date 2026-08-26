# TAGLINE

命令行客户端

# TLDR

**连接数据库**

```mysql -u [username] -p [database]```

**连接远程主机**

```mysql -h [hostname] -u [username] -p [database]```

**执行 SQL 命令**

```mysql -u [user] -p -e "[SELECT * FROM table]" [database]```

**执行 SQL 文件**

```mysql -u [user] -p [database] < [script.sql]```

**使用指定端口连接**

```mysql -h [host] -P [3306] -u [user] -p```

**导入数据库转储**

```mysql -u [user] -p [database] < [dump.sql]```

# SYNOPSIS

**mysql** [_options_] [_database_]

# PARAMETERS

_DATABASE_
> 数据库名。

**-h** _HOST_
> 服务器主机名。

**-u** _USER_
> 用户名。

**-p** [_PASSWORD_]
> 密码（留空时提示输入）。

**-P** _PORT_
> 端口号。

**-e** _COMMAND_
> 执行 SQL 后退出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mysql** 是 MySQL 的命令行客户端。它用于连接 MySQL/MariaDB 服务器。

该工具执行 SQL 查询。提供交互式和批处理两种模式。

# CAVEATS

需要服务器访问权限。建议使用密码提示输入。注意脚本中的 SQL 注入风险。

# HISTORY

mysql 是为 **MySQL** 数据库创建的标准 CLI，由 Oracle 和社区共同维护。

# INSTALL

```apt: sudo apt install mariadb-client-core```

```dnf: sudo dnf install mysql```

```apk: sudo apk add mariadb-client```

```zypper: sudo zypper install mariadb-client```

```brew: brew install mysql```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mysqladmin](/man/mysqladmin)(1), [mysqldump](/man/mysqldump)(1), [mycli](/man/mycli)(1), [mariadb](/man/mariadb)(1), [psql](/man/psql)(1), [sqlite3](/man/sqlite3)(1)
