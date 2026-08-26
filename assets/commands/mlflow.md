# TAGLINE

MLflow 的命令行界面，MLflow 是一个开源的机器学习全生命周期平台

# TLDR

**启动 MLflow 追踪服务器**

```mlflow server --host [0.0.0.0] --port [5000]```

为本地实验**启动 UI**

```mlflow ui```

**运行 MLflow 项目**

```mlflow run [project-uri] -P [param=value]```

**从 Git 运行项目**

```mlflow run https://github.com/[user]/[repo]```

**创建新实验**

```mlflow experiments create -n [experiment-name]```

**列出实验**

```mlflow experiments search```

**部署模型服务**

```mlflow models serve -m [models:/model-name/version] -p [5001]```

**为模型构建 Docker 镜像**

```mlflow models build-docker -m [models:/model-name/version] -n [image-name]```

# SYNOPSIS

**mlflow** _command_ [_options_]

# COMMANDS

**server**
> 启动追踪服务器。

**ui**
> 启动本地追踪 UI。

**run** _uri_
> 运行 MLflow 项目。

**experiments** create|search|delete|rename
> 管理实验。

**runs** list|describe|delete
> 管理运行记录。

**models** serve|build-docker|predict
> 模型部署。

**artifacts** download|list|log-artifacts
> 管理工件（artifact）。

**recipes** run
> 运行机器学习配方（recipe）。

**deployments** create|update|delete|list|predict
> 管理模型部署。

**doctor**
> 诊断 MLflow 安装情况。

# SERVER OPTIONS

**--host** _address_
> 绑定地址。默认：127.0.0.1。

**--port** _port_
> 服务器端口。默认：5000。

**--backend-store-uri** _uri_
> 存储实验/运行数据的数据库 URI。

**--default-artifact-root** _path_
> 默认的工件存储位置。

**--workers** _count_
> gunicorn worker 数量。

# RUN OPTIONS

**-P**, **--param** _key=value_
> 项目参数。

**-e**, **--entry-point** _name_
> 入口点。默认：main。

**--experiment-name** _name_
> 本次运行所属的实验名称。

**--env-manager** _type_
> 环境管理器：local、conda、virtualenv。

# DESCRIPTION

**mlflow** 是 MLflow 的 CLI，MLflow 是一个用于机器学习全生命周期管理的开源平台。它可以追踪实验、打包代码并部署模型。

**追踪服务器**存储实验元数据、参数、指标和工件。本地开发使用 **mlflow ui**，团队部署使用 **mlflow server**。

**mlflow run** 执行 MLflow 项目——即包含 MLproject 文件（定义入口点、参数和环境）的目录或 Git 仓库，以保证可复现性。

用 **models serve** 部署模型会创建用于预测的 REST 端点。**models build-docker** 将模型打包为容器。Models 组件支持多种机器学习框架。

工件包括数据集、模型和输出结果。追踪服务器只存引用；实际文件保存在所配置的存储中（本地、S3、GCS、Azure Blob）。

# CAVEATS

追踪服务器默认使用的 SQLite 不适合生产环境；请改用 PostgreSQL/MySQL。大型工件需要对象存储。某些功能需要特定的 Python 包。模型部署使用的是 Flask 开发服务器。

# HISTORY

MLflow 由 **Databricks** 创建，于 **2018 年 6 月**开源。它在 **2020 年**成为 **LF AI & Data 基金会**项目。该平台源自 Databricks 内部用于管理机器学习工作流的工具。2.0 版（2022 年）增加了 MLflow Recipes 并改进了模型注册表。MLflow 在实验追踪与模型管理领域被广泛采用。

# SEE ALSO

[dvc](/man/dvc)(1)
