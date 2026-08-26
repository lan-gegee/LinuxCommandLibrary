# TAGLINE

基于容器的持续集成服务器

# TLDR

**启动快速上手的一体化** Concourse 实例

```concourse quickstart --add-local-user [admin]:[password] --main-team-local-user [admin]```

**配合 PostgreSQL 启动 web 节点**

```concourse web --postgres-host [localhost] --postgres-user [concourse] --postgres-password [password]```

**启动 worker 节点**

```concourse worker --work-dir [/var/lib/concourse/worker] --tsa-host [127.0.0.1:2222]```

**生成 RSA 会话签名密钥**

```concourse generate-key -t rsa -f [/path/to/session_signing_key]```

为 TSA 主机或 worker **生成 SSH 密钥**

```concourse generate-key -t ssh -f [/path/to/tsa_host_key]```

**执行数据库迁移**

```concourse migrate --postgres-host [localhost] --postgres-user [concourse]```

**优雅退役一个 worker**

```concourse retire-worker --name [worker-name]```

**显示**命令的帮助信息

```concourse [web|worker|quickstart] --help```

# SYNOPSIS

**concourse** _COMMAND_ [_OPTIONS_]

# COMMANDS

**quickstart**
> 启动包含 web 和 worker 组件的一体化 Concourse 实例。

**web**
> 启动 Concourse web 节点（ATC/TSA）。

**worker**
> 启动 Concourse worker 节点。

**migrate**
> 执行数据库迁移。

**generate-key**
> 为 Concourse 组件生成加密密钥。

**land-worker**
> 安全地排空并停止一个 worker。

**retire-worker**
> 从集群中移除一个 worker。

# PARAMETERS

**--add-local-user** _USER_:_PASSWORD_
> 添加用于认证的本地用户。

**--main-team-local-user** _USER_
> 向本地用户授予 main team 的访问权限。

**--postgres-host** _HOST_
> PostgreSQL 服务器主机名。

**--postgres-user** _USER_
> PostgreSQL 用户名。

**--postgres-password** _PASSWORD_
> PostgreSQL 密码。

**--external-url** _URL_
> Concourse web UI 对外可达的 URL。

**--work-dir** _PATH_
> worker 存储容器数据的目录。

**--tsa-host** _HOST_:_PORT_
> 用于 worker 注册的 TSA 主机（默认：127.0.0.1:2222）。

**--session-signing-key** _PATH_
> 用于签名和验证用户会话令牌的 RSA 密钥（web 节点）。

**--tsa-host-key** _PATH_
> TSA worker 注册网关的 SSH 私钥（web 节点）。

**--tsa-authorized-keys** _PATH_
> 包含已授权 worker 公钥的文件（web 节点）。

**--tsa-public-key** _PATH_
> 用于验证的 TSA 主机公钥（worker 节点）。

**--tsa-worker-private-key** _PATH_
> 用于向 TSA 认证的 worker 私钥（worker 节点）。

**--runtime** _RUNTIME_
> 要使用的容器运行时（guardian 或 containerd）。

**--help**
> 显示命令的帮助信息。

# DESCRIPTION

**Concourse** 是一个基于容器的持续集成系统。concourse CLI 用于运行和管理 Concourse 的服务器组件，包括 web 节点（负责调度的 ATC 和负责 worker 注册的 TSA）和 worker 节点（用于运行流水线任务）。

所有配置均通过旗标或环境变量定义。每个旗标都有对应的环境变量，格式为 **CONCOURSE_FLAG_NAME**（全大写，用下划线代替连字符）。

对于典型用法，**quickstart** 命令提供适合开发的一体化环境。生产部署通常分别运行 web 和 worker 进程，且往往位于不同机器上。

用户通过 **fly** CLI 与 Concourse 交互，而不是直接使用 concourse 命令。

# CAVEATS

quickstart 命令面向开发和测试，不适合生产环境。生产部署需要独立配置 web 和 worker 节点，并进行妥善的安全配置，包括 TLS 证书和密钥管理。worker 节点需要足够的磁盘空间和容器运行时权限。

# HISTORY

Concourse 由 Pivotal（现为 VMware Tanzu）创建，首次发布于 **2014** 年。它被设计为一套"以流水线为核心"的 CI/CD 系统，一切皆以代码形式配置。与传统 CI 系统不同，Concourse 没有插件——所有功能都来自资源（带版本的工件）和任务（容器中的脚本）。该项目已开源，并在 GitHub 上持续活跃开发。

# INSTALL

```aur: yay -S concourse```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fly](/man/fly)(1), [docker](/man/docker)(1), [podman](/man/podman)(1), [jenkins](/man/jenkins)(1)
