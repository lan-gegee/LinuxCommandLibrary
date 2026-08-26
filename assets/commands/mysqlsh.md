# TAGLINE

MySQL Shell 客户端

# TLDR

**启动 MySQL Shell**

```mysqlsh```

**连接服务器**

```mysqlsh -u [username] -h [hostname]```

**使用 URI 连接**

```mysqlsh [mysql://user@host:3306/database]```

**以 SQL 模式执行**

```mysqlsh --sql -u [user] -e "[SELECT 1]"```

**JavaScript 模式**

```mysqlsh --js```

**Python 模式**

```mysqlsh --py```

**运行脚本**

```mysqlsh -f [script.js]```

# SYNOPSIS

**mysqlsh** [_options_] [_uri_]

# PARAMETERS

_URI_
> 连接 URI。

**-u** _USER_
> 用户名。

**-h** _HOST_
> 主机名。

**--sql**
> SQL 模式。

**--js**
> JavaScript 模式。

**--py**
> Python 模式。

**-f** _FILE_
> 执行脚本文件。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mysqlsh** 是 MySQL Shell 客户端。它提供 SQL、JavaScript 和 Python 三种接口。

该工具支持 MySQL 8.0 的特性。包含用于集群管理的 AdminAPI。

# CAVEATS

需要 MySQL 8.0 及以上版本。提供三种语言模式。针对新特性可替代旧版 mysql 客户端。

# HISTORY

MySQL Shell 随 **MySQL 8.0** 推出，是支持多种脚本语言的现代客户端。

# SEE ALSO

[mysql](/man/mysql)(1), [mysqladmin](/man/mysqladmin)(1), [mycli](/man/mycli)(1)
