# TAGLINE

提供 Kubernetes 资源请求、限制和使用率的简单视图

# TLDR

**显示集群容量**

```kube-capacity```

**显示 Pod 资源使用情况**

```kube-capacity --pods```

**显示使用率百分比**

```kube-capacity --util```

**显示指定命名空间**

```kube-capacity --namespace [default]```

**显示容器详情**

```kube-capacity --containers```

# SYNOPSIS

**kube-capacity** [_options_]

# PARAMETERS

**--pods**
> 显示 Pod 级别的资源使用情况。

**--containers**
> 显示容器级别的详细信息。

**--util**
> 显示使用率百分比。

**--namespace** _name_
> 按命名空间过滤。

**--node-labels** _selector_
> 按节点标签过滤。

**--sort** _field_
> 按字段对输出排序。

# DESCRIPTION

**kube-capacity** 提供 Kubernetes 资源请求、限制和使用率的简单视图。跨节点、Pod 和容器显示 CPU 和内存分配情况，帮助识别过度配置或利用率不足的资源。

# INSTALL

```nix: nix profile install nixpkgs#kube-capacity```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [kubectl-top](/man/kubectl-top)(1)
