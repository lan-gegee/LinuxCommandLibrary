# TAGLINE

MySQL 服务器守护进程

# TLDR

**启动 MySQL 服务器**

```mysqld```

**以指定配置启动**

```mysqld --defaults-file=[/etc/mysql/my.cnf]```

**指定数据目录启动**

```mysqld --datadir=[/var/lib/mysql]```

**以安全模式运行**

```mysqld_safe```

**初始化数据目录**

```mysqld --initialize```

**以指定用户运行**

```mysqld --user=[mysql]```

**详细日志输出**

```mysqld --verbose```

# SYNOPSIS

**mysqld** [_options_]

# PARAMETERS

**--defaults-file** _FILE_
> 配置文件。

**--datadir** _DIR_
> 数据目录路径。

**--user** _USER_
> 以指定用户身份运行。

**--initialize**
> 初始化数据目录。

**--port** _PORT_
> 监听端口。

**--verbose**
> 详细模式。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mysqld** 是 MySQL 的服务器守护进程。它负责数据库存储和查询处理。

该工具是核心数据库引擎。管理连接、查询和数据。

# CAVEATS

需要正确的配置。资源消耗大。安全设置至关重要。

# HISTORY

mysqld 是 **MySQL** 数据库服务器，最初由 MySQL AB 开发，现由 Oracle 维护。

# INSTALL

```apt: sudo apt install mariadb-server-core```

```dnf: sudo dnf install mariadb```

```pacman: sudo pacman -S mariadb```

```apk: sudo apk add mariadb```

```zypper: sudo zypper install mariadb```

```brew: brew install mariadb```

```nix: nix profile install nixpkgs#mariadb```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mysql](/man/mysql)(1), [mysqladmin](/man/mysqladmin)(1)
