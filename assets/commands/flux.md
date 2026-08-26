# TAGLINE

面向 Kubernetes 的 GitOps 持续交付工具

# TLDR

通过 GitHub 在 Kubernetes 集群上**引导安装 Flux**

```flux bootstrap github --owner=[username] --repository=[repo] --path=[clusters/my-cluster]```

**检查** Flux 安装的**前置条件**

```flux check --pre```

**检查 Flux 组件**状态

```flux check```

**获取所有 Flux 资源**的状态

```flux get all```

立即**调和 Kustomization**

```flux reconcile kustomization [name]```

**暂停** Kustomization 的**更新**

```flux suspend kustomization [name]```

**恢复** Kustomization 的**更新**

```flux resume kustomization [name]```

将 **Flux 资源导出**为 YAML

```flux export source git --all```

**查看 Flux 控制器日志**

```flux logs```

# SYNOPSIS

**flux** [_COMMAND_] [_FLAGS_]

# COMMANDS

**bootstrap** _PROVIDER_
> 以 GitOps 方式在集群上部署 Flux（github、gitlab、bitbucket）。

**check**
> 检查前置条件和组件状态。

**install**
> 不经 GitOps 引导直接安装 Flux 组件。

**uninstall**
> 从集群卸载 Flux 组件。

**get** _RESOURCE_
> 获取 Flux 资源的状态（源、kustomization、helmrelease）。

**reconcile** _RESOURCE_ _NAME_
> 触发资源的调和。

**suspend** _RESOURCE_ _NAME_
> 暂停资源的调和。

**resume** _RESOURCE_ _NAME_
> 恢复资源的调和。

**export** _RESOURCE_
> 将资源导出为 YAML 清单。

**create** _RESOURCE_
> 创建 Flux 资源。

**delete** _RESOURCE_
> 删除 Flux 资源。

**logs**
> 显示来自 Flux 控制器的日志。

**trace** _RESOURCE_ _NAME_
> 沿 Flux 依赖图追踪某个对象。

**diff** _RESOURCE_
> 将本地资源与集群状态进行差异比较。

**version**
> 打印 Flux CLI 和控制器的版本。

# PARAMETERS

**--kubeconfig** _FILE_
> kubeconfig 文件的路径。

**-n**, **--namespace** _NAMESPACE_
> CLI 操作使用的命名空间（默认：flux-system）。

**--context** _CONTEXT_
> 要使用的 Kubernetes 上下文。

**--timeout** _DURATION_
> 操作超时时间（默认：5m0s）。

**--verbose**
> 打印生成的对象。

**-h**, **--help**
> 显示命令帮助。

# DESCRIPTION

**Flux** 是一款面向 Kubernetes 的 GitOps 持续交付工具。它自动将集群状态与存储在 Git 仓库中的配置同步，确保实际运行的集群与版本控制中定义的期望状态一致。

Flux 监控 Git 仓库、Helm 仓库和 OCI 镜像仓库的变更。检测到更新后，它会自动将其应用到集群。这实现了遵循 GitOps 原则的声明式、可审计的基础设施管理。

flux CLI 将 Flux 组件引导安装到集群中，并提供针对源、kustomization 和 Helm release 的管理命令。Flux 使用 Kubernetes 自定义资源来定义要同步的内容以及同步方式。

# CAVEATS

需要已配置好集群访问的 kubectl。引导过程默认在 flux-system 命名空间中创建资源。访问 Git 仓库需要相应的凭据或 SSH 密钥。Flux 组件作为控制器在集群中运行，需要足够的 RBAC 权限。

# HISTORY

Flux 由 Weaveworks 于 **2016 年**创建，是最早的 Kubernetes GitOps 工具之一。**Flux v2** 于 **2020 年**发布，是基于 GitOps Toolkit 的完全重写，提供了更模块化、更可扩展的架构。Flux 于 **2022 年**成为 **CNCF 毕业项目**，反映了它在云原生生态中的成熟度和广泛采用。

# INSTALL

```apk: sudo apk add flux```

```brew: brew install flux```

```nix: nix profile install nixpkgs#flux```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [helm](/man/helm)(1), [kustomize](/man/kustomize)(1), [argocd](/man/argocd)(1)
