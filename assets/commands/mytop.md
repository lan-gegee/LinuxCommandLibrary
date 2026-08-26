# TAGLINE

实时显示 MySQL 服务器活动，类似面向进程的 top

# TLDR

**监视 MySQL 查询**

```mytop```

**连接指定数据库**

```mytop -u [user] -p [password] -d [database]```

**连接远程服务器**

```mytop -h [hostname] -u [user] -p [password]```

**慢查询模式**（阈值单位为秒）

```mytop -s [5]```

**显示空闲连接**

```mytop -i```

**以秒为单位指定刷新间隔**

```mytop --delay [3]```

**批处理模式**（运行一次后退出）

```mytop --batch```

**通过套接字连接**

```mytop -S [/var/run/mysqld/mysqld.sock]```

# SYNOPSIS

**mytop** [_-u user_] [_-p pass_] [_-h host_] [_-d database_] [_options_]

# PARAMETERS

**-u** _USER_
> MySQL 用户名。

**-p** _PASS_
> MySQL 密码。

**-h** _HOST_
> MySQL 服务器主机名。

**-d** _DB_
> 默认数据库。

**-P** _PORT_
> MySQL 端口。

**-s** _SECONDS_
> 慢查询阈值。

**-i**
> 显示空闲连接。

**--delay** _SECONDS_
> 刷新间隔。

**--color**
> 使用 ANSI 颜色。

**-S** _SOCKET_
> MySQL 套接字路径。

**--batch**
> 批处理模式（只运行一次，不清屏）。

**--nocolor**
> 禁用 ANSI 彩色输出。

# KEY COMMANDS

**q**
> 退出。

**k**
> 终止某个查询/线程。

**f**
> 切换完整查询显示。

**s**
> 更改排序列。

**r**
> 反转排序顺序。

**p**
> 暂停显示。

**?**
> 帮助。

# DESCRIPTION

**mytop** 实时显示 MySQL 服务器的活动，类似于面向进程的 top。它显示正在运行的查询、连接和服务器统计信息。

显示内容包括各查询线程及其状态、执行时间和 SQL 文本。长时间运行的查询会格外显眼，便于关注。

服务器统计信息展示每秒查询数、慢查询数量、已连接线程数以及缓存命中率。这些指标有助于发现性能问题。

慢查询模式将显示过滤为超过时间阈值的查询。这能让注意力集中在有问题的操作上。

kill 命令可终止失控的查询。结合过滤功能，它有助于应对查询过载的情况。

连接远程服务器后，可以在一处监视多个数据库。

# CAVEATS

需要 MySQL PROCESS 权限。某些功能需要 SUPER 权限。已不再积极维护——可考虑 innotop 等替代工具。可能不支持所有 MariaDB 特性。也可以从 ~/.mytop 文件读取配置。

# HISTORY

**mytop** 由 **Jeremy Zawodny** 在 **2000 年**前后于 Yahoo 工作期间编写。它曾是 MySQL 管理员的标准工具，在此类功能被内置到管理工具之前填补了实时服务器监控的空白。

# INSTALL

```apt: sudo apt install mariadb-client```

```dnf: sudo dnf install mytop```

```pacman: sudo pacman -S mariadb-mytop```

```apk: sudo apk add mariadb-mytop```

```zypper: sudo zypper install mariadb-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mysql](/man/mysql)(1), [mysqladmin](/man/mysqladmin)(1)
