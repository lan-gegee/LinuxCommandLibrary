# TAGLINE

进程控制与自动重启守护进程

# TLDR

**启动 supervisord**

```supervisord```

**使用配置文件**

```supervisord -c [/etc/supervisor/supervisord.conf]```

**在前台运行**

```supervisord -n```

**调试模式**

```supervisord -e debug```

**检查配置**

```supervisord -c [supervisord.conf] -t```

# SYNOPSIS

**supervisord** [_-c config_] [_-n_] [_-e level_] [_options_]

# PARAMETERS

**-c** _FILE_
> 配置文件。

**-n**
> 在前台运行。

**-e** _LEVEL_
> 日志级别。

**-t**
> 测试配置。

**-d** _DIR_
> 工作目录。

**-u** _USER_
> 以指定用户身份运行。

**-j** _FILE_
> PID 文件路径。

# DESCRIPTION

**supervisord** 是一个进程控制守护进程，用于管理长期运行的进程，并在它们崩溃或意外退出时自动重启。它被广泛用于运行应用服务器、后台工作进程以及其他需要可靠进程监管的服务。

配置文件定义各个程序及其命令、环境变量、用户权限和重启策略。程序可以组织成组以便协同管理。守护进程会捕获受管进程的 stdout 和 stderr，将其写入支持可配置轮转的日志文件。

事件监听器允许自定义脚本响应崩溃或状态转换等进程状态变化。守护进程通过 Unix 套接字或 TCP 连接与 supervisorctl 通信，并提供可选的 Web 界面进行进程管理。

# CONFIGURATION

**/etc/supervisor/supervisord.conf**
> 定义程序、分组、日志和套接字设置的主配置文件。

**/etc/supervisor/conf.d/*.conf**
> 存放各程序配置文件的插入式目录。

# CAVEATS

不能替代 init 系统。存在单点故障。需要对它自身进行监控。

# HISTORY

**Supervisor** 由 **Chris McDonough**（Agendaless Consulting）创建。它为 Python 应用及其他程序提供简单的进程管理。

# INSTALL

```dnf: sudo dnf install supervisor```

```pacman: sudo pacman -S supervisor```

```apk: sudo apk add supervisor```

```zypper: sudo zypper install supervisor```

```brew: brew install supervisor```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[supervisorctl](/man/supervisorctl)(1)
