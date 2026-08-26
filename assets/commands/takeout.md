# TAGLINE

基于 Docker 的开发服务管理器

# TLDR

**启用服务**

```takeout enable [mysql]```

以默认设置**启用服务**

```takeout enable [mysql] --default```

**启用多个**服务

```takeout enable [mysql] [redis] [meilisearch]```

**禁用服务**

```takeout disable [mysql]```

**列出服务**

```takeout list```

启动所有已启用的服务

```takeout start```

停止全部服务

```takeout stop```

**查看状态**

```takeout status```

# SYNOPSIS

**takeout** _command_ [_service_]

# PARAMETERS

**enable** _SERVICE..._
> 通过交互式提示启用并启动服务容器。

**disable** _SERVICE_
> 停止并移除服务容器。

**--default**
> 启用时接受默认参数（跳过提示）。

**start**
> 启动服务。

**stop**
> 停止服务。

**list**
> 列出可用的服务。

**status**
> 显示状态。

# DESCRIPTION

**takeout** 是一个简化开发依赖管理的 CLI 工具，基于 Docker 容器实现。它不把数据库和服务直接装在机器上，而是把它们作为相互隔离的 Docker 容器运行，用简单的命令即可启用或禁用。

支持的服务包括 MySQL、PostgreSQL、MariaDB、Redis、Memcached、Elasticsearch、MeiliSearch、MinIO 等等。每个服务都在自己的容器中以合理的默认值运行，Takeout 会自动处理端口映射、卷持久化和容器生命周期管理。

Takeout 由 **Tighten** 为 Laravel 生态而创建，同样适用于任何 PHP 开发工作流乃至更广泛的场景。**enable** 命令会拉取并启动服务容器，并通过交互式提示询问版本和配置；**disable** 则停止并移除容器。**start** 和 **stop** 命令可以同时控制所有已启用的服务。

# CAVEATS

需要 Docker。适用于 macOS/Linux。由 Tighten 创建的工具。

# HISTORY

**Takeout** 由 **Tighten** 创建，旨在利用 Docker 简化本地开发服务的管理。

# SEE ALSO

[docker](/man/docker)(1), [docker-compose](/man/docker-compose)(1), [valet](/man/valet)(1)
