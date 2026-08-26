# TAGLINE

带自动补全和语法高亮的 MySQL 客户端

# TLDR

**连接数据库**

```mycli -u [username] [database]```

**连接远程主机**

```mycli -h [hostname] -u [username] [database]```

**以密码提示方式连接**

```mycli -u [username] -p [database]```

**执行 SQL 文件**

```mycli -u [user] [database] < [script.sql]```

**通过套接字连接**

```mycli -S [/var/run/mysqld/mysqld.sock] -u [user]```

**使用指定端口**

```mycli -h [host] -P [3306] -u [user] [database]```

**执行查询后退出**

```mycli -u [user] -e "SELECT * FROM [table]" [database]```

**以 CSV 格式输出结果**

```mycli -u [user] -e "SELECT * FROM [table]" --csv [database]```

# SYNOPSIS

**mycli** [_options_] [_database_]

# PARAMETERS

_DATABASE_
> 要连接的数据库名。

**-h** _HOST_
> MySQL 服务器主机名。

**-u** _USER_
> 用户名。

**-p** [_PASSWORD_]
> 密码（未提供值时提示输入）。

**-P** _PORT_
> 端口号。

**-S** _SOCKET_
> Unix 套接字路径。

**-D** _DATABASE_
> 要连接的数据库名。

**-e** _COMMAND_
> 执行命令后退出。

**-R** _PROMPT_
> 自定义提示符格式。

**--csv**
> 以 CSV 格式输出结果（批处理模式）。

**--table**
> 以表格格式输出结果（批处理模式）。

**--auto-vertical-output**
> 当结果宽度超过终端时自动切换为垂直输出。

**-d** _DSN_
> 使用 myclirc 文件 [alias_dsn] 部分配置的 DSN。

**-l** _FILE_
> 将每条查询及其结果记录到文件。

**-v**, **--verbose**
> 详细输出。

**--myclirc** _FILE_
> 配置文件路径（默认：~/.myclirc）。

**--defaults-file** _FILE_
> 只从给定文件读取 MySQL 选项。

**--warn** / **--no-warn**
> 运行破坏性查询前发出警告。

**--ssh-host** _HOST_
> 要连接的 SSH 服务器主机名。

**--ssh-port** _PORT_
> 要连接的 SSH 服务器端口。

**--ssh-user** _USER_
> 连接 SSH 服务器的用户名。

**--ssh-key-filename** _FILE_
> SSH 连接使用的私钥文件名。

**--ssl-ca** _PATH_
> PEM 格式的 CA 文件。

**--ssl-cert** _PATH_
> PEM 格式的 X509 证书。

**--ssl-key** _PATH_
> PEM 格式的 X509 密钥。

**-V**, **--version**
> 显示版本信息。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mycli** 是面向 MySQL、MariaDB 和 Percona 的命令行客户端，具备智能自动补全和语法高亮。它在你输入时提供针对 SQL 关键字、表名、列名和函数的上下文感知补全。

# CAVEATS

基于 Python；需要有正在运行的 MySQL/MariaDB/Percona 服务器可供连接。配置保存在 ~/.myclirc 中。

# HISTORY

mycli 由 **Amjith Ramanujam** 创建，受 **pgcli** 启发，是一款带自动补全、对用户友好的 MySQL CLI。

# INSTALL

```dnf: sudo dnf install mycli```

```apk: sudo apk add mycli```

```brew: brew install mycli```

```nix: nix profile install nixpkgs#mycli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mysql](/man/mysql)(1), [mariadb](/man/mariadb)(1), [mysqldump](/man/mysqldump)(1), [pgcli](/man/pgcli)(1), [litecli](/man/litecli)(1)
