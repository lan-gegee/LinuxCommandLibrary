# TAGLINE

管理 DigitalOcean Kubernetes 集群

# TLDR

**列出 Kubernetes 集群**

```doctl kubernetes cluster list```

**创建一个集群**

```doctl kubernetes cluster create [name] --region [nyc1] --node-pool "name=pool;size=s-2vcpu-4gb;count=3"```

**获取集群信息**

```doctl kubernetes cluster get [cluster_id]```

**删除一个集群**

```doctl kubernetes cluster delete [cluster_id]```

**获取 kubeconfig**

```doctl kubernetes cluster kubeconfig save [cluster_id]```

**升级集群版本**

```doctl kubernetes cluster upgrade [cluster_id] --version [1.28]```

# SYNOPSIS

**doctl** **kubernetes** **cluster** _command_ [_options_]

# SUBCOMMANDS

**list**
> 列出集群。

**create**
> 创建一个集群。

**get**
> 获取集群详情。

**delete**
> 删除一个集群。

**kubeconfig**
> 管理 kubeconfig。

**upgrade**
> 升级集群版本。

**node-pool**
> 管理节点池。

# DESCRIPTION

**doctl kubernetes cluster** 管理 DigitalOcean Kubernetes（DOKS）集群，为托管的 Kubernetes 部署提供完整的生命周期管理，包括创建、配置、升级和删除。

该命令负责按指定的节点池开通集群、配置供 kubectl 使用的 kubeconfig 文件以及管理版本升级。DOKS 抽象了控制平面的管理工作，让用户可以专注于应用部署，而由 DigitalOcean 负责集群基础设施、etcd 备份和控制平面更新。

集群操作包括伸缩节点池、管理工作节点组成以及就地执行 Kubernetes 版本升级。kubeconfig 子命令将集群与本地 kubectl 工具集成，实现无缝的集群访问。

# SEE ALSO

[kubectl](/man/kubectl)(1)
