# TAGLINE

基于 Docker 的本地开发环境管理器

# TLDR

**启动项目**

```ddev start```

**停止项目**

```ddev stop```

**配置新项目**

```ddev config```

**在浏览器中打开项目**

```ddev launch```

**SSH 进入 web 容器**

```ddev ssh```

**运行 composer 命令**

```ddev composer [install]```

**导入数据库**

```ddev import-db --file=[database.sql.gz]```

**在 web 容器中执行命令**

```ddev exec [command]```

**显示项目状态**

```ddev describe```

**列出所有 DDEV 项目**

```ddev list```

# SYNOPSIS

**ddev** _command_ [_options_]

# SUBCOMMANDS

**start**
> 启动项目容器。

**stop**
> 停止项目容器。

**config**
> 创建或修改项目配置。

**launch**
> 在浏览器中打开项目。

**ssh**
> SSH 进入 web 容器。

**exec**
> 在 web 容器中执行命令。

**composer**
> 运行 Composer 命令。

**mysql**
> 访问 MySQL/MariaDB。

**import-db**
> 导入数据库转储。

**export-db**
> 导出数据库。

**describe**
> 显示项目详情。

**list**
> 列出所有 DDEV 项目。

**restart**
> 重启项目容器。

**delete**
> 移除项目信息（不删除代码）。

**snapshot**
> 创建数据库快照。

# CONFIGURATION

**.ddev/config.yaml**
> 项目配置文件，定义 PHP 版本、Web 服务器类型、数据库设置和项目名称。

**~/.ddev/global_config.yaml**
> DDEV 全局设置，包括默认 Web 服务器、路由器端口和性能选项。

# DESCRIPTION

**ddev** 是一个基于 Docker 的开源本地开发环境。它为 Drupal、WordPress、Laravel、TYPO3、Magento 等 PHP 应用提供预配置的技术栈，同时也支持 Python 和 Node.js 项目，免去了手动配置 Web 服务器、数据库和语言运行时的复杂工作。

该工具自动创建包含相应版本 PHP、Web 服务器（nginx 或 Apache）、数据库（MySQL、MariaDB 或 PostgreSQL）以及 Redis 和 Mailhog 等常用服务的容器。配置保存在 .ddev/config.yaml 中，使开发环境可复现并便于团队共享。

DDEV 通过代理到容器内工具（composer、mysql、npm）的命令简化了常见的开发流程，无需在宿主机上安装这些工具。它支持多个项目同时运行、带受信任证书的自动 HTTPS，以及与开发工具的集成。其环境高度贴近生产配置，同时保持易于搭建和销毁，对于管理多个客户项目的机构或跨技术栈工作的开发者都很有价值。

# CAVEATS

需要已安装并正在运行的 Docker。首次启动可能需要时间下载 Docker 镜像。

# INSTALL

```nix: nix profile install nixpkgs#ddev```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[docker-compose](/man/docker-compose)(1), [lando](/man/lando)(1)
