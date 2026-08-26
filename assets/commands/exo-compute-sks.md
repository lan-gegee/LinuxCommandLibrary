# TAGLINE

Exoscale 托管 Kubernetes 集群管理

# TLDR

**列出 SKS 集群**

```exo compute sks list```

**创建 SKS 集群**

```exo compute sks create [cluster_name] --zone [ch-gva-2]```

**获取 kubeconfig**

```exo compute sks kubeconfig [cluster_name]```

**添加节点池**

```exo compute sks nodepool add [cluster_name] [nodepool_name]```

**伸缩节点池**

```exo compute sks nodepool scale [cluster_name] [nodepool_name] [5]```

**删除集群**

```exo compute sks delete [cluster_name]```

# SYNOPSIS

**exo compute sks** _action_ [_options_]

# PARAMETERS

_ACTION_
> 操作：list、create、delete、kubeconfig、nodepool。

**create** _NAME_
> 创建新的 SKS 集群。

**kubeconfig** _NAME_
> 获取集群的 kubeconfig。

**nodepool add** _CLUSTER_ _POOL_
> 向集群添加节点池。

**nodepool scale** _CLUSTER_ _POOL_ _SIZE_
> 伸缩节点池。

**--zone** _ZONE_
> 可用区。

**--help**
> 显示帮助信息。

# DESCRIPTION

**exo compute sks** 用于管理 Exoscale SKS（Scalable Kubernetes Service）集群。SKS 提供托管 Kubernetes，控制平面自动管理。

命令涵盖集群生命周期、节点池管理和 kubeconfig 获取。节点池允许同一集群内使用不同的实例配置。

SKS 与 Exoscale 的基础设施集成，提供存储、网络和负载均衡能力。

# CAVEATS

Kubernetes 集群会产生费用。控制平面由平台托管，但工作节点需要计费。可用区决定可用的功能。kubeconfig 提供集群的完整访问权限。

# HISTORY

SKS 是 Exoscale 的托管 Kubernetes 服务，在 Exoscale 的欧洲云基础设施上提供通过 CNCF 认证的 Kubernetes 集群。

# INSTALL

```dnf: sudo dnf install exo```

```pacman: sudo pacman -S exo```

```apk: sudo apk add exoscale```

```nix: nix profile install nixpkgs#exo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[exo](/man/exo)(1), [exo-compute](/man/exo-compute)(1), [kubectl](/man/kubectl)(1)

# RESOURCES

```[Source code](https://github.com/exoscale/cli)```

```[Homepage](https://www.exoscale.com/)```

<!-- verified: 2026-07-15 -->
