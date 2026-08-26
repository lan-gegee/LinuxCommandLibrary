# TAGLINE

为维护操作驱逐节点上的 Pod

# TLDR

**排空节点**

```kubectl drain [node-name]```

**排空时忽略 DaemonSet**

```kubectl drain [node-name] --ignore-daemonsets```

**强制排空**

```kubectl drain [node-name] --force```

**排空并删除本地数据**

```kubectl drain [node-name] --delete-emptydir-data```

**带超时的排空**

```kubectl drain [node-name] --timeout=[5m]```

**试运行排空**

```kubectl drain [node-name] --dry-run=client```

# SYNOPSIS

**kubectl drain** [_options_] _node_

# PARAMETERS

_NODE_
> 要排空的节点名称。

**--ignore-daemonsets**
> 忽略 DaemonSet 管理的 Pod。

**--force**
> 即使出错也继续。

**--delete-emptydir-data**
> 删除 emptyDir 数据。

**--timeout** _DURATION_
> 排空超时时间。

**--grace-period** _N_
> Pod 终止宽限期。

**--help**
> 显示帮助信息。

# DESCRIPTION

**kubectl drain** 安全地驱逐节点上的所有 Pod，为内核升级、硬件维修或 Kubernetes 版本更新等维护操作做准备。它首先封锁该节点以防止新 Pod 被调度到其上，然后使用 Eviction API 优雅地终止每个 Pod，让它们的控制器将其重新调度到其他可用节点上。

该命令遵循 PodDisruptionBudget（PDB），也就是说，如果驱逐某个 Pod 会违反应用的可用性要求，它会阻塞等待。DaemonSet 管理的 Pod 默认不会被驱逐，因为它们本就应运行在每个节点上；此时需用 `--ignore-daemonsets` 才能不出错地继续。带本地存储（emptyDir 卷）的 Pod 也需要通过 `--delete-emptydir-data` 显式确认，因为它们的数据将会丢失。

维护完成后，必须用 `kubectl uncordon` 解除节点的封锁，才能恢复接受新的 Pod 调度。`--timeout` 标志可以设置排空完成前的最长等待时间，超时则中止。

# CAVEATS

kubectl 的子命令。遵循 PDB。使用 uncordon 恢复。

# HISTORY

kubectl drain 为 **Kubernetes** 集群维护操作提供安全的节点疏散能力。

# INSTALL

```apt: sudo apt install kubectl```

```pacman: sudo pacman -S kubectl```

```apk: sudo apk add kubectl```

```brew: brew install kubectl```

```nix: nix profile install nixpkgs#kubectl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [kubectl-cordon](/man/kubectl-cordon)(1), [kubectl-uncordon](/man/kubectl-uncordon)(1)
