# TAGLINE

Docksal Docker 开发环境 CLI

# TLDR

**列出项目**

```fin project list```

**启动项目**

```fin project start```

**停止项目**

```fin project stop```

**SSH 进入容器**

```fin bash```

**运行 drush 命令**

```fin drush [status]```

# SYNOPSIS

**fin** _command_ [_options_] [_arguments_]

# PARAMETERS

_COMMAND_
> 操作类型：project、bash、drush、exec 等。

**project** _ACTION_
> 管理 Docksal 项目。

**bash**
> SSH 进入 CLI 容器。

**drush** _CMD_
> 运行 Drush 命令。

**exec** _CMD_
> 在容器中执行命令。

**up**
> 启动项目容器。

**stop**
> 停止项目容器。

**--help**
> 显示帮助信息。

# CONFIGURATION

**.docksal/docksal.yml**
> 项目专属的 Docksal 配置，描述容器与服务。

**.docksal/docksal.env**
> 项目使用的环境变量。

# DESCRIPTION

**fin** 是 Docksal 的命令行工具，用于管理基于 Docker 的开发环境。它简化了 Web 开发项目的容器编排，尤其面向 Drupal、WordPress 及其他 PHP 应用。

该工具负责创建项目、启动/停止容器、在容器内执行命令，以及管理数据库、邮件捕获器等开发服务。

fin 把 Docker 的复杂性抽象掉，为常见任务提供简单的命令。

# CAVEATS

需要安装 Docksal 和 Docker。配置方式为 Docksal 专属。项目必须先经过初始化。

# HISTORY

fin 是 **Docksal** 的一部分；Docksal 是一款基于 Docker 的开发环境工具。它诞生的目的是简化本地开发环境的搭建，特别是 Drupal 项目，让团队每个成员都能获得一致的环境。

# SEE ALSO

[docker](/man/docker)(1), [docker-compose](/man/docker-compose)(1), [drush](/man/drush)(1)

# RESOURCES

```[Source code](https://github.com/docksal/docksal)```

<!-- verified: 2026-07-15 -->
