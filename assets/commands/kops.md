# TAGLINE

管理生产级 Kubernetes 集群

# TLDR

**创建集群**

```kops create cluster --name=[cluster.example.com] --zones=[us-east-1a]```

**更新集群**

```kops update cluster [cluster.example.com] --yes```

**验证集群**

```kops validate cluster [cluster.example.com]```

**删除集群**

```kops delete cluster [cluster.example.com] --yes```

**编辑集群**

```kops edit cluster [cluster.example.com]```

**导出 kubeconfig**

```kops export kubeconfig [cluster.example.com]```

# SYNOPSIS

**kops** _command_ [_options_]

# PARAMETERS

**create cluster**
> 创建集群配置。

**update cluster**
> 应用集群变更。

**validate cluster**
> 验证集群健康状况。

**delete cluster**
> 删除集群。

**--name** _NAME_
> 集群名称。

**--zones** _ZONES_
> 可用区。

**--yes**
> 确认变更。

**--help**
> 显示帮助信息。

# DESCRIPTION

**kops** 管理生产级 Kubernetes 集群。它可以在云提供商上创建、更新和销毁集群。

该工具负责网络、节点组和附加组件的处理。它支持 AWS、GCE 以及其他云平台。

# CAVEATS

需要云提供商凭据。需要进行 DNS 配置。面向生产的工具。

# HISTORY

kops (Kubernetes Operations) 的创建目的是帮助管理云基础设施上的生产级 Kubernetes 集群。

# INSTALL

```brew: brew install kops```

```nix: nix profile install nixpkgs#kops```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [eksctl](/man/eksctl)(1), [kubeadm](/man/kubeadm)(1)
