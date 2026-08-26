# TAGLINE

在 Astronomer 平台上部署和管理 Apache Airflow

# TLDR

> 该 CLI 的二进制名称为 **astro**。

**初始化**一个新的 Airflow 项目

```astro dev init```

**启动**本地 Airflow 环境

```astro dev start```

**停止**本地环境

```astro dev stop```

**登录** Astronomer

```astro login```

将代码**部署**到 Deployment

```astro deploy```

# SYNOPSIS

**astro** _command_ [_subcommand_] [_options_]

# DESCRIPTION

**astro** 是 Astronomer 的命令行界面，Astronomer 是一个运行 Apache Airflow 的平台。它简化了 Airflow DAG 的创建、测试与部署，提供了基于 Docker 的本地 Airflow 开发工具、向 Astro 或 Astronomer Software 的部署功能，以及对工作空间和 Deployment 的管理能力。

该工具让 Airflow 工作流程更加顺畅，覆盖从本地测试到生产部署的全过程。

# PARAMETERS

**dev init**
> 在当前目录创建新 Airflow 项目所需的文件。

**dev start**
> 构建项目并在 Docker 容器中启动本地 Airflow 环境。

**dev stop**
> 暂停运行本地 Airflow 环境的 Docker 容器。

**dev restart**
> 停止、重建并重启本地环境。

**deploy**
> 将项目代码部署到 Deployment。

**login**
> 登录 Astro CLI 进行身份认证。

**logout**
> 从 Astro CLI 登出。

**workspace list**
> 列出可用的工作空间。

**deployment list**
> 列出 Deployment。

**version**
> 显示 CLI 版本。

# CAVEATS

本地开发需要 Docker。部署需要 Astronomer 账户。部分命令仅适用于 Astro（云版）或 Astronomer Software 其中之一。

# HISTORY

**Astro CLI** 由 Astronomer 开发（astronomer/astro-cli），旨在简化 Apache Airflow 的部署与管理。统一的 **astro** 可执行文件自 1.0 版起推出，为 Astronomer 各产品线提供共享框架。

# SEE ALSO

[airflow](/man/airflow)(1), [docker](/man/docker)(1)

# RESOURCES

```[Source code](https://github.com/astronomer/astro-cli)```

```[Documentation](https://www.astronomer.io/docs/astro/cli/overview)```

<!-- verified: 2026-06-17 -->
