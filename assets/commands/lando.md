# TAGLINE

提供基于 Docker 的开发环境

# TLDR

**初始化项目**

```lando init```

**启动环境**

```lando start```

**停止环境**

```lando stop```

**重建环境**

```lando rebuild```

**在容器中运行命令**

```lando [npm|composer|php] [command]```

**SSH 进入容器**

```lando ssh```

**查看日志**

```lando logs```

# SYNOPSIS

**lando** _command_ [_options_]

# PARAMETERS

**init**
> 初始化 Lando 项目。

**start**
> 启动容器。

**stop**
> 停止容器。

**rebuild**
> 重建容器。

**ssh** [_SERVICE_]
> SSH 进入服务。

**logs** [_SERVICE_]
> 查看日志。

**destroy**
> 移除容器。

**--help**
> 显示帮助信息。

# DESCRIPTION

**Lando** 提供基于 Docker 的开发环境。它能创建出一致的本地开发环境。

该工具通过 recipe 支持众多框架，并自动处理网络、服务和工具链。

# CAVEATS

需要 Docker。内存开销较大。采用基于 recipe 的配置方式。

# HISTORY

Lando 由 **Tandem** 创建，旨在为各类技术栈简化基于 Docker 的开发环境搭建。

# INSTALL

```aur: yay -S lando```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[docker-compose](/man/docker-compose)(1), [ddev](/man/ddev)(1), [docker](/man/docker)(1)
