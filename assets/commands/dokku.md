# TAGLINE

基于 Docker 的自托管平台即服务

# TLDR

**创建应用**

```dokku apps:create [app_name]```

**通过 git push 部署**

```git push dokku main```

**列出所有应用**

```dokku apps:list```

**查看应用日志**

```dokku logs [app_name]```

**设置环境变量**

```dokku config:set [app_name] [KEY]=[value]```

**关联数据库**

```dokku postgres:link [db_name] [app_name]```

**伸缩应用进程**

```dokku ps:scale [app_name] web=[2]```

**添加域名**

```dokku domains:add [app_name] [example.com]```

使用 Let's Encrypt 证书**启用 HTTPS**

```dokku letsencrypt:enable [app_name]```

**安装插件**（以 root 身份）

```sudo dokku plugin:install [https://github.com/dokku/dokku-postgres.git]```

# SYNOPSIS

**dokku** _plugin_:_command_ [_app_] [_arguments_]

大多数命令遵循 `namespace:verb` 的命名模式，其中 namespace 就是提供该命令的插件。

# COMMANDS

**apps:create** _app_ / **apps:list** / **apps:destroy** _app_
> 创建、列出和销毁应用。

**apps:rename** _app_ _new-name_
> 重命名应用并重新构建。

**config:set** _app_ _KEY=VALUE_ / **config:unset** _app_ _KEY_ / **config:show** _app_
> 管理环境变量。设置或取消设置都会重启应用，除非传入 **--no-restart**。

**ps:scale** _app_ _proc_=_n_
> 将 Procfile 中的某个进程类型伸缩为 _n_ 个容器。

**ps:restart** _app_ / **ps:rebuild** _app_ / **ps:stop** _app_
> 重启正在运行的容器、从源码重建应用或将其停止。

**logs** _app_
> 显示应用日志。**-t** 持续跟踪日志，**-n** _N_ 限制行数。

**domains:add** _app_ _domain_ / **domains:remove** _app_ _domain_ / **domains:report** _app_
> 管理路由到该应用的虚拟主机。

**letsencrypt:enable** _app_
> 申请并安装 Let's Encrypt 证书（需要 `dokku-letsencrypt` 插件）。

**proxy:ports-add** _app_ _scheme_:_host-port_:_container-port_
> 将外部端口映射到容器端口。

**run** _app_ _command_
> 用应用镜像在新容器中运行一次性命令。

**enter** _app_ [_process_]
> 在运行中的容器内打开 Shell。

**postgres:create** _service_ / **postgres:link** _service_ _app_
> 创建数据库服务并将其凭据提供给应用。`mysql`、`redis`、`mongo` 等也有对应命令，各自来自独立的插件。

**plugin:install** _git-url_ / **plugin:list**
> 安装和列出插件。必须以 root 身份运行。

**version**
> 打印已安装的 Dokku 版本。

# DESCRIPTION

**Dokku** 是一个自托管的平台即服务（PaaS），在单台机器上实现了类似 Heroku 的工作流。把服务器添加为 git remote 并向其推送代码就是全部的部署过程：Dokku 会检测应用类型、构建镜像，然后将流量切换到新容器。

应用可以使用 **Herokuish** buildpacks、**Dockerfile** 或 Cloud Native Buildpacks 构建，随后作为 Docker 容器运行在 nginx 反向代理之后（代理配置由 Dokku 自动完成）。`Procfile` 定义进程类型，**ps:scale** 将其转换为容器数量。

核心之外的一切几乎都是插件：`dokku-postgres`、`dokku-mysql`、`dokku-redis` 等提供后端服务，并作为环境变量关联到应用；`dokku-letsencrypt` 则自动管理 TLS 证书。这种设计使基础安装保持精简，同时覆盖了 Heroku 的大部分能力。

# CAVEATS

Dokku 面向单台主机：没有内置的跨机集群或零停机故障转移，所谓伸缩也只是同一台机器上更多的容器。它要求全新的服务器，因为会接管 nginx 和 Docker 配置。插件命令必须以 **root** 身份安装，尽管应用命令以 `dokku` 用户运行。零停机部署依赖正确配置的 `CHECKS` 文件，否则推送期间会短暂丢失请求；构建过程也可能非常吃内存，在没有 swap 的最小规格 VPS 上可能失败。

# HISTORY

Dokku 由 **Jeff Lindsay** 于 **2013 年**创建，最初是一个只用几百行 Shell 写成的"docker 驱动的迷你 Heroku"。项目很快超越了这一规模，维护工作移交给了至今仍领导项目的 **Jose Diaz-Gonzalez**。它至今仍是最流行的自托管 PaaS 方案之一，其 git push 工作流刻意与 Heroku 保持接近，方便应用在两者之间迁移。

# INSTALL

```aur: yay -S dokku```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[docker](/man/docker)(1), [git](/man/git)(1), [heroku](/man/heroku)(1), [caprover](/man/caprover)(1)

# RESOURCES

```[Source code](https://github.com/dokku/dokku)```

```[Homepage](https://dokku.com)```

```[Documentation](https://dokku.com/docs/)```

<!-- verified: 2026-07-14 -->
