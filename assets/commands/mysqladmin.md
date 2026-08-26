# TAGLINE

管理 MySQL 服务器

# TLDR

**查看服务器状态**

```mysqladmin -u [user] -p status```

**创建数据库**

```mysqladmin -u [user] -p create [database_name]```

**删除数据库**

```mysqladmin -u [user] -p drop [database_name]```

**修改密码**

```mysqladmin -u [user] -p password "[newpassword]"```

**显示变量**

```mysqladmin -u [user] -p variables```

**显示进程列表**

```mysqladmin -u [user] -p processlist```

**关闭服务器**

```mysqladmin -u [root] -p shutdown```

**探测服务器**

```mysqladmin -u [user] -p ping```

# SYNOPSIS

**mysqladmin** [_options_] _command_

# PARAMETERS

_COMMAND_
> 管理命令。

**-u** _USER_
> 用户名。

**-p** [_PASSWORD_]
> 密码。

**-h** _HOST_
> 服务器主机名。

**status**
> 显示服务器状态。

**create** _DB_
> 创建数据库。

**drop** _DB_
> 删除数据库。

**flush-privileges**
> 重新加载授权表。

**extended-status**
> 显示服务器状态变量。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mysqladmin** 是用于在 MySQL 服务器上执行管理操作的命令行客户端。它可以检查服务器状态、创建和删除数据库、重新加载权限、刷新日志以及关闭服务器。

常见的管理任务包括：检查服务器是否存活（**ping**）、查看服务器变量和状态计数器（**variables**、**extended-status**）、权限变更后重新加载授权表（**flush-privileges**），以及监视活动连接（**processlist**）。

# CAVEATS

需要管理员权限。存在危险操作（drop）。在生产环境中请谨慎使用。

# HISTORY

mysqladmin 是 **MySQL** 发行版的组成部分，自早期版本起就提供命令行管理功能。

# INSTALL

```apt: sudo apt install mariadb-client```

```apk: sudo apk add mariadb-client```

```zypper: sudo zypper install mariadb-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mysql](/man/mysql)(1), [mysqldump](/man/mysqldump)(1), [mysqlcheck](/man/mysqlcheck)(1)
