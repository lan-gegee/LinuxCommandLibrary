# TAGLINE

简化基于 Docker 的开发环境

# TLDR

**启动环境**

```kool start```

**停止环境**

```kool stop```

在服务中**运行命令**

```kool run [service] [command]```

在运行中的容器内**执行命令**

```kool exec [service] [command]```

**查看日志**

```kool logs [service]```

从预设模板**创建新项目**

```kool create [preset] [project-name]```

**查看运行中容器的状态**

```kool status```

将 kool **更新到最新版本**

```kool self-update```

# SYNOPSIS

**kool** _command_ [_options_]

# PARAMETERS

**start**
> 启动开发环境容器。

**stop**
> 停止环境容器。

**run** _SERVICE_ _CMD_
> 在服务容器中运行命令。

**exec** _SERVICE_ _CMD_
> 在运行中的容器内执行命令。

**logs** _SERVICE_
> 查看服务日志。

**create** _PRESET_ _NAME_
> 从预设模板创建项目（如 laravel、nextjs、hugo）。

**status**
> 显示运行中容器的状态、端口和状态信息。

**self-update**
> 将 kool 更新到最新版本。

**preset** _NAME_
> 为框架预设自动生成配置文件。

**docker** _IMAGE_ [_CMD_]
> 简化选项后的 `docker run` 辅助工具。

**--verbose**
> 提高输出详细程度。

**--help**
> 显示帮助信息。

# DESCRIPTION

**kool** 简化基于 Docker 的开发环境。它在 Docker Compose 之上封装了对开发者友好的命令，并为 Laravel、Next.js、Hugo、Express.js 等常见框架提供预设模板。

该工具通过 `kool.yml` 配置文件统一各项目的工作流。

# CAVEATS

需要 Docker。为常见技术栈提供预设。是 Docker Compose 的封装。

# HISTORY

kool 的创建目的是通过更简单的命令和框架预设来精简基于 Docker 的开发工作流。

# INSTALL

```brew: brew install kool```

```nix: nix profile install nixpkgs#kool```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[docker](/man/docker)(1), [docker-compose](/man/docker-compose)(1), [ddev](/man/ddev)(1)
