# TAGLINE

在隔离的 Docker 容器中运行不受信任的代码

# TLDR

**拉取执行器镜像**并验证 Docker

```tako-vm setup```

**启动 REST API 服务器**

```tako-vm server```

在自定义端口上**启动服务器**

```tako-vm server --port [8000]```

为开发**同时启动本地 PostgreSQL 和服务器**

```tako-vm dev up --with-server```

**查看当前配置**

```tako-vm config```

检查服务器健康状况

```tako-vm status```

# SYNOPSIS

**tako-vm** [**--config** _file_] _command_ [_options_]

# DESCRIPTION

**tako-vm** 是一个自托管平台，可在相互隔离的 **Docker** 容器中运行不受信任的或 AI 生成的 **Python** 代码，并支持可选的 **gVisor** 沙箱和 seccomp 过滤。它内置了任务排队、执行历史、重试逻辑与重放功能，因此无需单独搭建 Redis、Celery 或自定义基础设施。

每个任务都在自己的容器中运行，**默认进行网络隔离**，并支持按任务类型配置可选的允许列表。服务器暴露一个 REST API：代码提交到 /execute 端点后即会在沙箱内运行。PostgreSQL 负责存储任务状态，并在服务器运行时通过 Docker 自动启动。

# COMMANDS

**setup**
> 拉取执行器 Docker 镜像并验证 Docker 安装。

**server** [**--port** _port_]
> 启动 REST API 服务器（自动通过 Docker 启动 PostgreSQL）。

**dev up** [**--with-server**]
> 启动用于开发的本地 PostgreSQL，可选择同时启动 API 服务器。

**dev status**
> 检查本地 PostgreSQL 状态。

**dev down**
> 停止本地 PostgreSQL。

**config** [**--json**]
> 显示当前配置，可以 JSON 格式输出。

**validate** [_file_]
> 校验当前的或指定的配置文件。

**status**
> 检查服务器健康状况。

**version**
> 显示版本信息。

# CAVEAT

需要可用的 **Docker** 安装；请先运行 **tako-vm setup**。隔离能力建立在 Docker 加可选的 gVisor 与 seccomp 之上，因此在运行不受信任的代码时，请保持执行器镜像和 Docker 及时更新。

# HISTORY

**tako-vm** 是由开发者 **las7** 用 **Python** 编写的开源执行平台，通过 **pip install "tako-vm[server]"** 安装，以 **Apache-2.0** 许可证分发。

# SEE ALSO

[docker](/man/docker)(1), [podman](/man/podman)(1), [firejail](/man/firejail)(1), [bwrap](/man/bwrap)(1)
