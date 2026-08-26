# TAGLINE

用于编写、调度和监控数据工作流的平台

# TLDR

**启动 Airflow 调度器**

```airflow scheduler```

**在指定端口启动 Web 服务器**

```airflow webserver --port [8080]```

**列出所有 DAG**

```airflow dags list```

**触发一次 DAG 运行**

```airflow dags trigger [dag_id]```

**触发 DAG** 并附带配置参数

```airflow dags trigger [dag_id] --conf '{"key": "value"}'```

**测试 DAG 中指定的任务**

```airflow tasks test [dag_id] [task_id] [execution_date]```

**暂停 DAG**（停止调度）

```airflow dags pause [dag_id]```

**恢复 DAG**（继续调度）

```airflow dags unpause [dag_id]```

**列出指定 DAG 的所有运行记录**

```airflow dags list-runs -d [dag_id]```

**初始化数据库**

```airflow db migrate```

# SYNOPSIS

**airflow** _command_ [_subcommand_] [_options_]

# PARAMETERS

**scheduler**
> 启动 Airflow 调度器守护进程以触发 DAG 运行

**webserver**
> 启动 Airflow Web 界面服务器

**triggerer**
> 为可延迟操作符（deferrable operators）启动异步触发服务

**dags**
> 管理 DAG（list、trigger、pause、unpause、test、delete、backfill）

**tasks**
> 管理并测试单个任务（run、test、clear、list、render）

**db**
> 数据库操作（migrate、reset、clean、check、shell）

**connections**
> 管理连接配置（add、delete、list、export、import）

**variables**
> 管理 Airflow 变量（get、set、delete、list、export、import）

**pools**
> 管理资源池，用于控制任务并发

**users**
> 管理 Airflow 用户（create、delete、list）

**config**
> 查看和管理配置设置

**providers**
> 显示已安装 provider 的信息

**info**
> 显示系统和环境信息

**version**
> 显示 Airflow 版本

**-o**, **--output** _format_
> 输出格式：table、json、yaml、plain

**-v**, **--verbose**
> 启用详细日志输出

# DESCRIPTION

**Apache Airflow** 是一个以编程方式编写、调度和监控工作流的平台。该 CLI 提供对 DAG（有向无环图）、任务、连接以及 Airflow 各服务的全面控制。

工作流以 Python 代码定义，创建出描述任务应如何组织和执行的 DAG。调度器根据定义的计划和依赖关系触发任务，而 Web 界面则提供监控和人工干预能力。

该工具管理到外部系统（数据库、API、云服务）的连接以及用于配置的变量。资源池可用于控制任务并发。数据库存储有关 DAG 运行、任务状态和历史记录的元数据。

常见流程包括：使用 **db migrate** 初始化数据库，启动 **scheduler** 和 **webserver**，以及使用 **dags trigger** 手动启动 DAG 运行。可以使用 **tasks test** 单独测试任务而不影响生产状态。

# CONFIGURATION

**~/airflow/airflow.cfg**
> 主配置文件，控制执行器类型、数据库连接、Web 服务器设置、调度器行为和日志。也可通过以 AIRFLOW__ 为前缀的环境变量覆盖。

**~/airflow/webserver_config.py**
> Web 服务器的认证与安全配置，包括 RBAC 设置和认证后端。

# CAVEATS

首次使用前需要通过 **airflow.cfg** 或环境变量完成正确配置。DAG 要按计划执行必须保持调度器运行。启动服务之前必须先用 **airflow db migrate** 初始化数据库。某些功能需要额外的依赖或执行器配置（Celery、Kubernetes）。

# HISTORY

Apache Airflow 由 Maxime Beauchemin 于 **2014** 年在 **Airbnb** 创建，用于管理其复杂的数据管道。它于 **2015** 年开源，**2016** 年成为 Apache 孵化器项目，**2019** 年毕业为 Apache 顶级项目。该平台已发展成为使用最广泛的工作流编排工具之一：**2020 年 12 月**发布的 2.0 版本带来了重大架构改进，3.0 版本进一步增强。

# SEE ALSO

[luigi](/man/luigi)(1), [prefect](/man/prefect)(1), [dagster](/man/dagster)(1), [cron](/man/cron)(8), [docker](/man/docker)(1), [kubectl](/man/kubectl)(1)
