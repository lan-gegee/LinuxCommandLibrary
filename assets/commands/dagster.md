# TAGLINE

面向软件定义资产的数据编排平台

# TLDR

**启动开发服务器**

```dagster dev```

**以指定模块启动**

```dagster dev -m [my_project]```

**为计划/传感器启动守护进程**

```dagster-daemon run```

**仅启动 Web 服务器**

```dagster-webserver```

**运行一个作业**

```dagster job execute -m [my_project] -j [job_name]```

**列出作业**

```dagster job list -m [my_project]```

**搭建新项目**

```dagster project scaffold --name [my-project]```

**校验定义**

```dagster definitions validate -m [my_project]```

# SYNOPSIS

**dagster** _command_ [_options_]

**dagster-daemon** run [_options_]

**dagster-webserver** [_options_]

# COMMANDS

**dev**
> 启动开发服务器（Web 服务器 + 守护进程）。

**job** execute|list|print
> 管理和运行作业。

**asset** materialize|list|wipe
> 管理软件定义资产。

**schedule** list|start|stop|preview
> 管理计划。

**sensor** list|start|stop|preview
> 管理传感器。

**project** scaffold|from-example
> 创建新项目。

**definitions** validate
> 校验代码定义。

**instance** info|migrate
> 管理 Dagster 实例。

**run** list|delete|terminate
> 管理流水线运行记录。

# PARAMETERS

**-m**, **--module** _name_
> 包含定义的 Python 模块。

**-f**, **--file** _path_
> 包含定义的 Python 文件。

**-j**, **--job** _name_
> 作业名称。

**-p**, **--port** _port_
> Web 服务器端口。默认：3000。

**-h**, **--host** _host_
> Web 服务器主机。默认：localhost。

**-w**, **--workspace** _file_
> 工作区 YAML 文件。

**-d**, **--working-directory** _path_
> 代码的工作目录。

# DESCRIPTION

**dagster** 是 Dagster 的 CLI。Dagster 是一个围绕软件定义资产构建的数据编排平台，负责管理开发环境、作业执行和基础设施。

**dagster dev** 会同时启动 Web 服务器（UI）和守护进程（计划、传感器），用于本地开发。在生产环境中，应分别运行 **dagster-webserver** 和 **dagster-daemon**。

软件定义资产是核心抽象——即产出数据资产的函数及其依赖关系。资产构成一张由 Dagster 物化的 DAG。作业则将资产分组以便执行。

计划按 cron 模式触发作业；传感器基于外部事件触发。两者都需要守护进程在运行。

Web 服务器提供的 UI 可展示资产血缘、运行历史、日志和指标。资产图可视化呈现数据依赖关系。

# CONFIGURATION

**dagster.yaml**
> 实例配置文件，控制存储、计算和运行设置。

**workspace.yaml**
> 工作区配置，定义代码位置和仓库。

# CAVEATS

计划和传感器需要守护进程。资产的物化状态保存在实例存储中。生产环境的运行存储需要 PostgreSQL。部分功能需要 Dagster+（云服务）。

# HISTORY

Dagster 由 **Elementl** 创建，该公司由 **Nick Schrock**（GraphQL 联合创造者）于 **2018 年**创立。该项目提出软件定义资产的概念，作为对面向任务工作流的改进。1.0 版本于 **2022 年**发布。Dagster 强调开发者体验，提供类型检查、测试工具和本地开发支持。公司还提供用于托管云编排的 Dagster+ 服务。

# SEE ALSO

[prefect](/man/prefect)(1), [airflow](/man/airflow)(1), [dbt](/man/dbt)(1), [argocd](/man/argocd)(1)
