# TAGLINE

Canonical 面向 Kubernetes 笔记本环境的数据科学栈 CLI

# TLDR

在 Canonical Kubernetes 集群上**初始化 DSS**

```dss initialize --kubeconfig "$(sudo k8s config)"```

使用指定镜像**创建** Jupyter notebook

```dss create [my-notebook] --image=pytorch```

**列出** DSS 环境中的所有 notebook

```dss list```

**显示** MLflow、GPU 和核心组件的状态

```dss status```

打印指定 notebook 的日志

```dss logs [my-notebook]```

打印 MLflow 部署的日志

```dss logs --mlflow```

**停止**运行中的 notebook

```dss stop [my-notebook]```

**启动**先前停止的 notebook

```dss start [my-notebook]```

**移除**单个 notebook

```dss remove [my-notebook]```

**清除**所有 DSS 组件和全部 notebook（破坏性操作）

```dss purge```

# SYNOPSIS

**dss** _command_ [_options_]

# PARAMETERS

**initialize** [_--kubeconfig_ _file_]
> 存储集群凭据，为 notebook 分配持久存储，并部署 MLflow 模型注册表。

**create** _name_ [_--image_ _image_]
> 创建一个指定 _name_ 的新 Jupyter notebook，并连接到共享的 MLflow 实例。_image_ 可以是简写（**pytorch**、**tensorflow**），也可以是形如 **kubeflownotebookswg/jupyter-scipy:v1.8.0** 的完整镜像名。

**list**
> 列出当前集群中 DSS 跟踪的所有 notebook。

**status**
> 显示部署状态、MLflow URL 以及检测到的 GPU 可用情况。

**logs** [_name_] [_--kubeconfig_ _file_] [_--all_] [_--mlflow_]
> 打印指定 notebook、**--mlflow**（MLflow pod）或 **--all** 全部组件的日志。

**start** _name_
> 启动已停止的 notebook。

**stop** _name_
> 停止运行中的 notebook。

**remove** _name_
> 删除单个 notebook 及其持久卷声明。

**purge**
> 拆除所有 DSS 组件（notebook、MLflow 及配套资源）。**不可逆**——所有已存数据都会丢失。

**--kubeconfig** _file_
> kubeconfig 文件路径。当用户尚未通过集群身份验证时，由 **initialize** 和 **logs** 使用。

**--help**
> 显示 **dss** 或特定子命令的用法。

# DESCRIPTION

**dss** 是 **Canonical 数据科学栈（Data Science Stack）**的命令行前端——这是一个以 **snap** 形式分发、观点鲜明的组合包，包含 **Jupyter Notebook** 镜像、**MLflow** 模型跟踪和 Kubernetes 基础设施。它面向本地 Canonical Kubernetes（**k8s** snap）集群，但也能对接任何可以承载底层组件的 Kubernetes。

执行 **dss initialize** 后，集群会运行共享的 MLflow 服务器并准备就绪以承载 notebook pod。**dss create** 启动一个 notebook，由可配置的容器镜像、持久存储和能访问 MLflow 的服务账户支撑。其余生命周期命令（**list**、**status**、**logs**、**start**、**stop**、**remove**、**purge**）对这些 notebook 进行操作，无需直接使用 **kubectl**。

DSS 致力于成为搭建带 GPU 支持和实验跟踪的可复现本地数据科学环境的最简途径，同时仍让高级用户能够直接访问底层 Kubernetes 资源。

# CAVEATS

**dss purge** 会删除所有 notebook 和 MLflow 注册表；必须事先备份。默认的 Kubernetes 目标是 **k8s** snap；在其他发行版上需显式传入 **--kubeconfig**。**pytorch** 和 **tensorflow** 等镜像简写跟随不断变动的上游标签，可能在 **dss** 版本之间发生变化。

**dss** 这个名字存在重载——**Dataiku Data Science Studio** 提供独立的 **dsscli** 和 **dssadmin** 二进制文件，Open-E 的 **dss_cli** 则面向无关的 DSS 存储服务器。本页面介绍的是 Canonical 的 snap 版本。

# CONFIGURATION

DSS 状态（存储类、MLflow 端点、kubeconfig 引用）持久化在 snap 的数据目录下，通常为 **/var/snap/data-science-stack/current/**。notebook 资源（包括 MLflow 部署）位于所连 Kubernetes 集群内的专用命名空间中。

# HISTORY

**Data Science Stack** 由 **Canonical** 以 **data-science-stack** snap 形式发布。它作为完整 **Charmed Kubeflow** 发行版的精简替代方案问世，聚焦于单机工作流：在 **k8s** snap 之上将 Jupyter 与 MLflow 配对。

# SEE ALSO

[kubectl](/man/kubectl)(1), [snap](/man/snap)(1), [mlflow](/man/mlflow)(1), [jupyter](/man/jupyter)(1)
