# TAGLINE

Flux v1 GitOps 工具的命令行界面

# TLDR

**列出工作负载**

```fluxctl list-workloads```

**列出工作负载的镜像**

```fluxctl list-images --workload=[namespace:deployment/name]```

**发布新镜像**

```fluxctl release --workload=[namespace:deployment/name] --update-image=[image:tag]```

**与 Git 同步**

```fluxctl sync```

**锁定工作负载**

```fluxctl lock --workload=[namespace:deployment/name]```

# SYNOPSIS

**fluxctl** _command_ [_options_]

# PARAMETERS

_COMMAND_
> 操作类型：list-workloads、list-images、release、sync 等。

**list-workloads**
> 显示所有被管理的工作负载。

**list-images** _WORKLOAD_
> 显示可用镜像。

**release**
> 将工作负载更新到新镜像。

**sync**
> 与 Git 仓库同步。

**lock** _WORKLOAD_
> 阻止自动更新。

**unlock** _WORKLOAD_
> 允许自动更新。

**--help**
> 显示帮助信息。

# DESCRIPTION

**fluxctl** 是 Flux v1 的命令行界面，Flux v1 是一款面向 Kubernetes 的 GitOps 工具。它管理工作负载、触发部署，并控制来自容器镜像仓库的自动镜像更新。

该工具连接到运行在 Kubernetes 中的 Flux 守护进程，用于列出资源、发布镜像和触发 Git 同步。它让用户可以在原本自动化的 GitOps 工作流中进行手动干预。

fluxctl 提供了对 Flux 管理的集群的运维控制能力。

# CAVEATS

Flux v1 已弃用，建议改用 Flux v2。需要能够访问 Flux 守护进程。必须先配置好集群上下文。

# HISTORY

fluxctl 是 Weaveworks 出品 **Flux v1** 的一部分。Flux 开创了 Kubernetes 的 GitOps 实践，使用 Git 作为集群状态的唯一可信来源。Flux v2 用 flux CLI 取代了它。

# SEE ALSO

[flux](/man/flux)(1), [kubectl](/man/kubectl)(1), [argocd](/man/argocd)(1)

# RESOURCES

```[Source code](https://github.com/fluxcd/flux)```

<!-- verified: 2026-07-15 -->
