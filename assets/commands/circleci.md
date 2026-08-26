# TAGLINE

CircleCI 持续集成平台的 CLI

# TLDR

**使用 API 令牌配置 CLI**

```circleci setup```

**校验配置文件**

```circleci config validate```

**在本地运行任务**

```circleci local execute --job [build]```

**处理配置文件**

```circleci config process [.circleci/config.yml]```

**创建新项目**

```circleci project create```

**列出 orbs**

```circleci orb list```

**关注一个项目**

```circleci follow```

**在浏览器中打开 CircleCI**

```circleci open```

# SYNOPSIS

**circleci** [_options_] _command_ [_arguments_]

# DESCRIPTION

**circleci** 是 CircleCI 的官方 CLI，支持本地任务执行、配置校验、流水线管理，以及在终端中与 CircleCI 资源交互。

该 CLI 特别适合以下场景：在推送更改前校验和处理配置文件、在 Docker 容器中本地运行任务以加快开发迭代，以及管理 orbs、上下文和项目设置。它通过 CircleCI API 实现流水线和工作流管理。

本地执行需要 Docker，并在镜像云环境的容器中运行单个任务，但缓存和工作流等功能在本地不可用。

# COMMANDS

**setup**
> 使用 API 令牌配置 CLI

**config validate**
> 校验 config.yml 语法

**config process**
> 处理并展开配置

**local execute**
> 在本地运行任务

**project**
> 管理项目

**context**
> 管理上下文和环境变量

**orb**
> 管理 orbs

**namespace**
> 管理命名空间

**pipeline**
> 管理流水线

**version**
> 显示版本

# PARAMETERS

**--token** _token_
> CircleCI API 令牌

**--host** _url_
> CircleCI 主机 URL

**--debug**
> 启用调试输出

**--skip-update-check**
> 跳过更新检查

# LOCAL EXECUTION

```circleci local execute --job build -e VAR=value```

注意：工作流、缓存及部分功能不支持在本地运行。

# CONFIGURATION

**~/.circleci/cli.yml**
> CLI 配置，包括 API 令牌和主机 URL。

**.circleci/config.yml**
> 项目级 CircleCI 流水线配置，定义任务、工作流和 orbs。

# CAVEATS

本地执行只能运行单个任务，不能运行工作流。本地不支持缓存。某些 CircleCI 功能需要云端执行。

# INSTALL

```brew: brew install circleci```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[docker](/man/docker)(1), [git](/man/git)(1)
