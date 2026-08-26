# TAGLINE

Python 工作流编排平台

# TLDR

**启动 Prefect 服务器**

```prefect server start```

**部署一个 flow**

```prefect deploy [flow.py:flow_name]```

**在本地运行 flow**

```prefect flow-run create [flow-name]```

**列出部署**

```prefect deployment ls```

**启动一个 worker**

```prefect worker start -p [work-pool]```

**创建工作池**

```prefect work-pool create [pool-name] -t [process]```

**查看 flow 运行记录**

```prefect flow-run ls```

**登录 Prefect Cloud**

```prefect cloud login```

# SYNOPSIS

**prefect** _command_ [_options_]

# COMMANDS

**server** start
> 启动本地 Prefect 服务器。

**deploy** _path_
> 部署一个 flow。

**flow-run** create|ls|cancel
> 管理 flow 运行。

**deployment** ls|run|delete|build|apply
> 管理部署。

**worker** start
> 启动 worker 进程。

**work-pool** create|ls|delete
> 管理工作池。

**block** register|ls|create
> 管理存储和基础设施 block。

**cloud** login|logout|workspace
> Prefect Cloud 身份验证。

**profile** ls|create|use
> 管理配置 profile。

**config** set|unset|view
> 配置管理。

# PARAMETERS

**-p**, **--pool** _name_
> 工作池名称。

**-t**, **--type** _type_
> 工作池类型：process、docker、kubernetes。

**-n**, **--name** _name_
> 部署或资源名称。

**--cron** _schedule_
> 部署的 Cron 调度计划。

**--interval** _seconds_
> 部署的间隔调度计划。

**--limit** _count_
> 限制结果数量。

# DESCRIPTION

**prefect** 是 Prefect 的 CLI。Prefect 是一个 Python 工作流编排框架，用于管理运行数据管道所需的部署、worker 和基础设施。

Flow 是用 @flow 装饰的 Python 函数。**prefect deploy** 将 flow 打包以供远程执行，并附带调度计划、参数和基础设施设置。

Worker 轮询工作池并执行 flow 运行。**prefect worker start** 为特定工作池启动一个 worker。工作池类型定义执行环境：process（本地）、Docker 或 Kubernetes。

**prefect server start** 在本地运行 API 服务器和 UI。生产环境可使用 Prefect Cloud，或使用 PostgreSQL 自托管。UI 展示 flow 运行、日志和任务状态。

Block 用于存储凭据、存储位置和基础设施模板等配置。使用 **block register** 注册 block，并在部署中引用它们。

# CAVEATS

Prefect 2.x 与 Prefect 1.x 差异巨大。Worker 取代了 1.x 的 agent。部署要求代码可访问（Git、Docker、存储）。Cloud 功能需要账户。

# HISTORY

Prefect 由 **Jeremiah Lowin** 于 **2018 年**创立，是 Airflow 的现代替代品。Prefect 1.0（2019 年）引入了本地执行的 Hybrid 模式。Prefect 2.0（2022 年）是一次彻底重写，强调简洁性，将原生 Python 代码直接作为工作流。该公司提供托管编排服务 Prefect Cloud。Prefect 在数据工程和 ML 管道领域日益流行。

# INSTALL

```nix: nix profile install nixpkgs#prefect```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dagster](/man/dagster)(1), [airflow](/man/airflow)(1), [luigi](/man/luigi)(1)
