# TAGLINE

带自动补全和语法高亮的增强版 PostgreSQL 客户端

# TLDR

**连接数据库**

```pgcli [database]```

**以用户名和主机连接**

```pgcli -h [hostname] -u [user] [database]```

**通过 URL 连接**

```pgcli postgresql://[user]:[password]@[host]/[database]```

**通过套接字连接**

```pgcli -h /var/run/postgresql [database]```

**执行单条查询**

```pgcli -c "[SELECT * FROM table]" [database]```

**执行文件**

```pgcli [database] < [script.sql]```

**列出数据库**

```pgcli --list```

# SYNOPSIS

**pgcli** [_-h host_] [_-p port_] [_-u user_] [_-c command_] [_options_] [_database_]

# PARAMETERS

**-h** _HOST_, **--host** _HOST_
> 数据库服务器主机。

**-p** _PORT_, **--port** _PORT_
> 数据库端口。

**-u** _USER_, **--user** _USER_
> 用户名。

**-W**, **--password**
> 提示输入密码。

**-d** _DB_, **--dbname** _DB_
> 数据库名称。

**-c** _CMD_
> 执行命令后退出。

**--list**
> 列出数据库。

**--auto-vertical-output**
> 对过宽的输出自动切换纵向显示。

**--row-limit** _N_
> 限制显示的行数。

**-l**, **--log-file** _FILE_
> 记录日志到文件。

**--pgclirc** _FILE_
> 配置文件路径。

**--version**
> 显示版本。

# DESCRIPTION

**pgcli** 是一款带自动补全和语法高亮的增强版 PostgreSQL 客户端，比 psql 提供更友好的使用体验。

自动补全会在输入时提示表名、列名、SQL 关键字和函数名。上下文感知的建议能够理解连接、子查询和复杂表达式。

语法高亮让查询更易读，SQL 中的错误在执行前就能看出来。

多行编辑支持复杂查询。历史搜索可以找到之前输入的命令。输出可以保存到文件。

为了兼容性，界面支持 psql 的反斜杠命令（\d、\dt、\l 等）。另有针对 pgcli 特有功能的附加命令。

配置项控制颜色、按键绑定和行为。pgclirc 文件可定制使用环境。

# CAVEATS

需要 Python。部分 psql 功能尚未实现。大结果集的显示可能较慢。

# HISTORY

**pgcli** 由 **Amjith Ramanujam** 于 **2014 年**前后创建，灵感来自面向 MySQL 的 mycli。它把现代 CLI 特性带入 PostgreSQL，重点改进了基础 psql 客户端的易用性。

# INSTALL

```dnf: sudo dnf install pgcli```

```pacman: sudo pacman -S pgcli```

```apk: sudo apk add pgcli```

```brew: brew install pgcli```

```nix: nix profile install nixpkgs#pgcli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[psql](/man/psql)(1), [mycli](/man/mycli)(1), [litecli](/man/litecli)(1), [pg_dump](/man/pg_dump)(1)
