# TAGLINE

管理 Amazon Elastic Container Service 资源

# TLDR

**列出所有 ECS 集群**

```aws ecs list-clusters```

**列出集群中的服务**

```aws ecs list-services --cluster [cluster_name]```

**查看服务详情**

```aws ecs describe-services --cluster [cluster_name] --services [service_name]```

**列出集群中运行中的任务**

```aws ecs list-tasks --cluster [cluster_name]```

**使用任务定义运行新任务**

```aws ecs run-task --cluster [cluster_name] --task-definition [task_def:revision]```

**更新服务以强制重新部署**

```aws ecs update-service --cluster [cluster_name] --service [service_name] --force-new-deployment```

**在运行中的容器内执行命令**

```aws ecs execute-command --cluster [cluster_name] --task [task_id] --container [container_name] --interactive --command "/bin/sh"```

**停止运行中的任务**

```aws ecs stop-task --cluster [cluster_name] --task [task_arn]```

# SYNOPSIS

**aws ecs** _subcommand_ [_options_]

# DESCRIPTION

**aws ecs** 是 AWS CLI 的子命令，用于管理 Amazon Elastic Container Service——一项全托管的容器编排服务。ECS 可在 EC2 实例集群上运行 Docker 容器，也可通过 Fargate 以无服务器方式运行。

核心概念包括：**集群（cluster）**（资源的逻辑分组）、**任务定义（task definition）**（容器的蓝图）、**任务（task）**（任务定义的运行实例）和 **服务（service）**（维持任务的目标数量）。ECS 与负载均衡器、自动扩缩和 IAM 集成，可支撑生产工作负载。

ECS Exec 支持以交互式 Shell 访问运行中的容器进行调试，类似于 docker exec，但通过 SSM 代理实现。

# PARAMETERS

**list-clusters**
> 列出该区域的所有 ECS 集群。

**describe-clusters**
> 获取集群的详细信息。

**create-cluster**
> 创建新的 ECS 集群。

**delete-cluster**
> 删除空集群。

**list-services**
> 列出集群中运行的服务。

**describe-services**
> 获取服务的详情、部署和事件。

**create-service**
> 创建新服务。

**update-service**
> 修改服务配置或触发部署。

**delete-service**
> 从集群中删除服务。

**list-tasks**
> 列出集群或服务中的任务。

**describe-tasks**
> 获取任务详情和容器状态。

**run-task**
> 启动独立任务。

**stop-task**
> 终止运行中的任务。

**execute-command**
> 在容器中运行交互式命令。

**register-task-definition**
> 创建新的任务定义修订版本。

**deregister-task-definition**
> 注销任务定义修订版本。

**list-task-definitions**
> 列出已注册的任务定义系列或修订版本。

**describe-task-definition**
> 获取任务定义的完整详情。

**tag-resource**
> 为 ECS 资源添加标签。

**wait**
> 等待直到满足条件（如 services-stable、tasks-stopped）。

**--cluster** _name_
> 目标集群的名称或 ARN。

**--service** _name_
> 目标服务的名称或 ARN。

**--task-definition** _name:revision_
> 任务定义系列及修订版本。

**--desired-count** _number_
> 要运行的任务实例数量。

**--force-new-deployment**
> 强制服务拉取新镜像并重新部署。

# CAVEATS

删除集群前必须先停止所有任务并删除所有服务。任务定义无法删除，只能注销。ECS Exec 需要 SSM 代理以及任务角色上的相应 IAM 权限。Fargate 任务必须在任务级指定 CPU 和内存。

# HISTORY

Amazon ECS 在 **AWS re:Invent 2014** 上发布，并于 **2015 年 4 月** 正式推出，是 AWS 的首个容器编排服务。无服务器计算 **Fargate** 于 **2017 年 11 月** 加入。用于交互式调试的 ECS Exec 于 **2021 年 3 月** 引入。该服务随 AWS 的容器战略持续演进，包括与 EKS 的集成。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [aws-ecr](/man/aws-ecr)(1), [aws-eks](/man/aws-eks)(1), [docker](/man/docker)(1), [kubectl](/man/kubectl)(1)
