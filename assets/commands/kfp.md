# TAGLINE

用于管理 Kubernetes 上机器学习工作流的 Kubeflow Pipelines CLI

# TLDR

**从已编译的流水线创建运行**

```kfp run create -e [experiment] -r [run-name] -f [pipeline.yaml] --endpoint [http://localhost:8080]```

**列出流水线**

```kfp pipeline list --endpoint [http://localhost:8080]```

**上传流水线**

```kfp pipeline create -p [pipeline-name] [pipeline.yaml]```

**创建实验**

```kfp experiment create -n [experiment-name] --endpoint [http://localhost:8080]```

**从 Python 编译流水线**

```kfp dsl compile --py [pipeline.py] --output [pipeline.yaml]```

**诊断 KFP 安装**

```kfp diagnose_me```

# SYNOPSIS

**kfp** _command_ [_options_]

# PARAMETERS

**run** create|list|get|archive|unarchive|delete
> 管理流水线运行。

**recurring-run** create|list|get|enable|disable|delete
> 管理周期性计划运行。

**pipeline** create|create-version|list|list-versions|get|delete
> 管理流水线。

**experiment** create|list|get|delete|archive|unarchive
> 管理实验。

**dsl** compile
> 将 Python 流水线定义编译为 YAML。

**component** build
> 从 Python 函数构建容器化组件。

**diagnose_me**
> 运行环境诊断（主要面向 GCP）。

**-e**, **--experiment** _name_
> 实验名称或 ID。

**-r**, **--run-name** _name_
> 运行的名称。

**-f**, **--package-file** _file_
> 已编译的流水线文件（YAML）。

**-p**, **--pipeline-name** _name_
> 流水线名称。

**--endpoint** _url_
> KFP API 端点 URL。

# DESCRIPTION

**kfp** 是 **Kubeflow Pipelines** 的命令行界面。Kubeflow Pipelines 在 Kubernetes 上以有向无环图（DAG）的形式编排机器学习工作流，流水线定义了带有输入、输出和依赖关系的可复用组件。

该 CLI 管理流水线的完整生命周期：将 Python 流水线定义编译为 YAML、上传流水线、创建实验以及提交运行。它通过 `--endpoint` 标志连接到正在运行的 KFP 后端。

Kubeflow 本身使用 Kustomize 清单、通过 `kubectl apply -k` 从 **kubeflow/manifests** 仓库安装。旧的 **kfctl** 部署工具已被弃用并归档。

# CAVEATS

资源消耗大；需要有足够容量的 Kubernetes 集群。`diagnose_me` 命令主要面向 GCP。旧的 `kfp run submit` 语法仍可用，是 `kfp run create` 已弃用的别名。类似地，`kfp pipeline upload` 也被别名为 `kfp pipeline create`。

# HISTORY

Kubeflow 由 **Google** 于 **2017 年**启动，最初是为了在 Kubernetes 上运行 TensorFlow。**2018 年**开源后扩展为支持完整的机器学习生命周期。1.0 版于 **2020 年**发布。该项目现为 **CNCF 孵化项目**。kfp v2 SDK 带来了重新设计的 Python API 和 CLI，包括 `dsl compile` 以及更简化的组件编写方式。

# SEE ALSO

[kubectl](/man/kubectl)(1), [mlflow](/man/mlflow)(1)
