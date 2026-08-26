# TAGLINE

在安装后提升 MySQL 安全性

# TLDR

**运行安全安装向导**

```mysql_secure_installation```

**使用套接字运行**

```mysql_secure_installation --socket=[/var/run/mysqld/mysqld.sock]```

**使用 defaults 文件运行**

```mysql_secure_installation --defaults-file=[/etc/mysql/my.cnf]```

# SYNOPSIS

**mysql_secure_installation** [_options_]

# PARAMETERS

**--socket** _path_
> 连接 localhost 使用的 Unix 套接字文件。

**--host** _host_
> MySQL 服务器主机名。

**--port** _port_
> TCP/IP 端口号。

**--user**, **-u** _user_
> 用于连接服务器的 MySQL 用户名。

**--defaults-file** _file_
> 只读取指定的选项文件。

**--no-defaults**
> 不读取任何选项文件。

**--use-default**
> 以默认答案非交互式执行。适用于无人值守安装。

**--password**, **-p** _password_
> 当前用于连接的密码。

# DESCRIPTION

**mysql_secure_installation** 在安装后提升 MySQL 的安全性。该交互式向导会执行以下步骤：设置或更改 root 密码、移除匿名用户、禁止 root 远程登录、移除 test 数据库，以及重新加载权限表。建议所有新安装都运行它。

程序会从选项文件中读取 **[mysql_secure_installation]** 和 **[client]** 组的配置。

# INSTALL

```apk: sudo apk add mariadb-client```

```zypper: sudo zypper install mariadb-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mysql](/man/mysql)(1), [mysqladmin](/man/mysqladmin)(1)
