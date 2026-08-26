# TAGLINE

在预先配置好的 Docker 容器内运行开发依赖

# TLDR

**安装 Jeeves**（来自其 Git 仓库）

```pip install git+https://github.com/fhsinchy/jeeves.git#egg=jeeves```

通过交互式向导**启动服务**（如 MySQL）

```jeeves start [mysql]```

**使用默认设置启动服务**（跳过提示）

```jeeves start [mysql] --default```

**停止运行中的服务**并移除其容器

```jeeves stop [mysql]```

**列出活跃的 Jeeves 容器**

```jeeves list```

**一次性启动多个服务**

```jeeves start [mysql] && jeeves start [redis] && jeeves start [mongo]```

# SYNOPSIS

**jeeves** _command_ [_arguments_] [_options_]

# COMMANDS

**start** _SERVICE_
> 为指定服务创建并启动容器。除非提供 **--default**，否则会询问版本、端口、密码和卷名。

**stop** _SERVICE_
> 停止并移除指定服务的容器。

**list**
> 打印 Jeeves 管理的容器表格。

**--help**, **-h**
> 显示命令或子命令的帮助。

# PARAMETERS

**--default**
> 跳过交互式配置提示，使用合理的默认值。

# DESCRIPTION

**jeeves** 是一个基于 Python 的命令行管家，封装了 **Docker**，让开发者可以通过单行命令启动常见的本地依赖（**MySQL**、**PostgreSQL**、**MongoDB**、**Redis**、**Memcached**、**Mailhog** 等）。每个服务都在自己的容器中启动，并使用命名的 Docker 卷持久化数据，因此数据在重启之后依然保留。

由于 Jeeves 底层使用的是常规 Docker 容器，标准 Docker 工具（**docker ps**、**docker logs**、**docker exec**）仍然可以配合使用——Jeeves 只负责声明和生命周期管理，并不重新实现容器管理功能。

# REQUIREMENTS

- **Python 3**
- 本地正在运行的 **Docker** 守护进程

# CAVEATS

该项目标记为**实验性**，不建议用于生产负载。它深受 **Tighten/Takeout** 和更早的 **fhsinchy/Tent** 的启发。由于 Jeeves 默认以交互方式提问，脚本化使用时应始终传入 **--default**。

# HISTORY

**jeeves** 由 **Farhan Hasin Chowdhury (fhsinchy)** 创建，是 Tighten 公司仅限 macOS 的 **Takeout** 工具的跨平台后继者，目标是让基于 Docker 的本地开发环境在 Windows、Linux 和 macOS 上同样好用。

# SEE ALSO

[docker](/man/docker)(1), [docker-compose](/man/docker-compose)(1), [takeout](/man/takeout)(1), [lando](/man/lando)(1)
