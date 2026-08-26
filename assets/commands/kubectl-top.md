# TAGLINE

显示节点或 Pod 的资源使用情况

# TLDR

**显示节点资源使用情况**

```kubectl top nodes```

**显示 Pod 资源使用情况**

```kubectl top pods```

**显示命名空间内的 Pod 使用情况**

```kubectl top pods -n [namespace]```

**显示容器级别的使用情况**

```kubectl top pods --containers```

**按 CPU 排序**

```kubectl top pods --sort-by=cpu```

# SYNOPSIS

**kubectl** **top** _type_ [_options_]

# PARAMETERS

**nodes**
> 显示节点资源使用情况。

**pods**
> 显示 Pod 资源使用情况。

**--containers**
> 显示容器级别的指标。

**--sort-by** _field_
> 按 cpu 或 memory 排序。

**-n**, **--namespace** _name_
> Kubernetes 命名空间。

**-A**, **--all-namespaces**
> 显示所有命名空间。

# DESCRIPTION

**kubectl top** 显示节点或 Pod 的资源使用情况（CPU 和内存）。需要集群中运行 metrics-server。有助于监控资源消耗并找出占用资源较多的工作负载。

# CAVEATS

需要在集群中安装 metrics-server。指标可能有一分钟以内的延迟。

# INSTALL

```apt: sudo apt install kubectl```

```pacman: sudo pacman -S kubectl```

```apk: sudo apk add kubectl```

```brew: brew install kubectl```

```nix: nix profile install nixpkgs#kubectl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [kube-capacity](/man/kube-capacity)(1)
