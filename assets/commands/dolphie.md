# TAGLINE

MySQL/MariaDB/ProxySQL 实时监控 TUI

# TLDR

**连接** MySQL 服务器并进行监控

```dolphie -u [username] --ask-pass -h [host]```

使用 URI **连接**

```dolphie mysql://[user]:[pass]@[host]:[port]```

使用配置文件**连接**

```dolphie -c [config.ini]```

**监控** ProxySQL 实例

```dolphie --host [host] --port 6032 -u [user] --ask-pass```

每 2 秒**自动刷新**

```dolphie -r 2 -h [host] -u [user]```

从 MySQL 配置文件**读取凭据**

```dolphie -m ~/.my.cnf -h [host]```

**录制**会话以便日后回放

```dolphie -R -h [host] -u [user]```

# SYNOPSIS

**dolphie** [_options_] [_uri_]

# PARAMETERS

**-u**, **--user** _USERNAME_
> 数据库用户名。

**-p**, **--password** _PASSWORD_
> 数据库密码。建议改用 **--ask-pass** 或配置文件，以免密码泄露到 Shell 历史记录中。

**--ask-pass**
> 以交互方式提示输入密码。

**-h**, **--host** _HOST_
> 数据库主机（默认：localhost）。

**-P**, **--port** _PORT_
> 数据库端口（默认：3306；ProxySQL 为 6032）。

**-S**, **--socket** _SOCKET_
> Unix 套接字文件路径。

**-c**, **--config-file** _FILE_
> Dolphie 配置文件的路径。

**-m**, **--mycnf-file** _FILE_
> 用于读取凭据的 MySQL 风格配置文件。

**-l**, **--login-path** _NAME_
> `~/.mylogin.cnf` 中的登录路径。

**-C**, **--cred-profile** _NAME_
> 在 Dolphie 配置文件中定义的具名凭据配置档。

**-r**, **--refresh-interval** _SECONDS_
> 数据采集周期（默认：1）。

**--panels** _LIST_
> 启动时要显示的面板，以逗号分隔（dashboard、processlist、graphs、replication 等）。

**--graph-marker** _MARKER_
> 图表标记点使用的样式（默认：braille）。

**--ssl-mode** _MODE_
> REQUIRED、VERIFY_CA 或 VERIFY_IDENTITY。

**--ssl-ca** _FILE_
> SSL CA 证书文件。

**--ssl-cert** _FILE_
> SSL 客户端证书文件。

**--ssl-key** _FILE_
> SSL 客户端私钥文件。

**-H**, **--hostgroup** _NAME_
> 连接到配置中定义的一组主机。

**--heartbeat-table** _TABLE_
> 用于复制延迟检测的 pt-heartbeat 表引用（仅限 MySQL）。

**-R**, **--record**
> 将会话录制到磁盘，供日后回放。

**-D**, **--daemon**
> 以无界面的守护进程模式运行；录制会自动启用。

**--replay-file** _FILE_
> 回放之前录制的会话。

**--show-trxs-only**
> 将进程列表过滤为仅显示活动事务。

**-V**, **--version**
> 显示版本并退出。

**--help**
> 显示帮助并退出。

# DESCRIPTION

**dolphie** 是一个用于监控 MySQL、MariaDB 和 ProxySQL 的实时终端用户界面。它可以显示仪表盘、图表、进程列表、复制状态、锁等待、事务和资源使用情况，定位类似于 **mytop** 和 **innotop**，但构建在现代 TUI 框架之上。

除实时监控外，dolphie 还可以把会话录制到磁盘并在之后回放、以守护进程模式持续采集指标，以及通过 hostgroup 聚合多台主机。

# CAVEATS

在 MySQL 上需要 **PROCESS**、**REPLICATION CLIENT** 权限，执行 **KILL** 还需要 **SUPER** 权限。以极低的刷新间隔持续轮询会给被监控的服务器增加负载。在命令行上传入 **-p** 会把密码暴露在 `ps` 输出和 Shell 历史记录中：建议改用 **--ask-pass**、配置文件或登录路径。

# HISTORY

**dolphie** 由 **Charles Thompson** 开发，是基于 Python 的现代替代品，用于取代 **mytop** 和 **innotop**，对 MySQL 8、MariaDB 和 ProxySQL 提供一流支持，并具备会话录制、守护进程模式和 SSL/TLS 连接等特性。

# INSTALL

```brew: brew install dolphie```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mysql](/man/mysql)(1), [mytop](/man/mytop)(1), [htop](/man/htop)(1)
