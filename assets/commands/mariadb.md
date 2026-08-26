# TAGLINE

MariaDB 数据库服务器的命令行客户端

# TLDR

**连接数据库**

```mariadb -u [user] -p [database]```

**连接远程服务器**

```mariadb -h [hostname] -u [user] -p [database]```

**执行 SQL 命令**

```mariadb -u [user] -p -e "[SELECT * FROM table]" [database]```

**执行 SQL 文件**

```mariadb -u [user] -p [database] < [script.sql]```

**通过套接字连接**

```mariadb -S [/var/run/mysqld/mysqld.sock] -u [user] -p```

**将查询结果导出到文件**

```mariadb -u [user] -p -e "[SELECT * FROM table]" [database] > [output.txt]```

**使用 SSL 连接**

```mariadb --ssl -u [user] -p [database]```

**导入 SQL 转储并显示进度**

```mariadb -u [user] -p [database] < [dump.sql]```

# SYNOPSIS

**mariadb** [_-u user_] [_-p_] [_-h host_] [_-e command_] [_options_] [_database_]

# PARAMETERS

**-u** _USER_, **--user** _USER_
> 连接用的用户名。

**-p**[_PASSWORD_], **--password**[=_PASS_]
> 提示输入或指定密码。

**-h** _HOST_, **--host** _HOST_
> 服务器主机名。

**-P** _PORT_, **--port** _PORT_
> 服务器端口。

**-S** _SOCKET_, **--socket** _SOCKET_
> Unix 套接字文件。

**-D** _DB_, **--database** _DB_
> 要使用的数据库。

**-e** _CMD_, **--execute** _CMD_
> 执行命令后退出。

**-B**, **--batch**
> 批处理模式（无格式化）。

**-N**, **--skip-column-names**
> 不显示列名。

**-t**, **--table**
> 以表格形式输出。

**--ssl**
> 为连接启用 SSL。

**--quick**
> 不缓存结果集，逐行打印。适用于大型结果集。

**-A**, **--no-auto-rehash**
> 禁用自动补全以加快启动速度。

**--safe-updates**
> 防止意外的大规模更新。

**-v**, **--verbose**
> 详细输出。

# DESCRIPTION

**mariadb** 是 MariaDB 数据库服务器的命令行客户端。它提供交互式 SQL shell，也可以从文件或命令行执行命令。

该客户端可连接 MariaDB 或 MySQL 服务器，因为 MariaDB 保持了线上协议的兼容性。交互模式提供命令历史、编辑和 Tab 补全功能。

批处理模式（-B）产生适合脚本的制表符分隔输出。配合 -N 跳过表头，输出即可交由其他工具处理。

安全更新模式阻止不带 WHERE 子句的 UPDATE 和 DELETE，防止意外的数据丢失。

SSL 连接会加密客户端与服务器之间的流量。可为生产环境配置证书验证。

该客户端支持从文件管道式导入 SQL，可用于自动化数据库迁移和备份恢复。

# CAVEATS

命令行上的密码会在进程列表中可见——请使用不带参数的 -p。大型结果集可能耗尽内存。交互功能需要 readline 支持。

# HISTORY

在 **Oracle** 于 **2010 年**收购 **MySQL** 之后，**Michael Widenius**（Monty）创建了 **MariaDB**。MariaDB 是一个社区开发的分支，旨在保持自由开源。在最近的版本中，mariadb 客户端取代 mysql 成为默认客户端名称。

# INSTALL

```apt: sudo apt install mariadb-client-core```

```dnf: sudo dnf install mariadb```

```pacman: sudo pacman -S mariadb```

```apk: sudo apk add mariadb-client```

```zypper: sudo zypper install mariadb-client```

```brew: brew install mariadb```

```nix: nix profile install nixpkgs#mariadb```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mysql](/man/mysql)(1), [mysqldump](/man/mysqldump)(1), [mysqladmin](/man/mysqladmin)(1)
