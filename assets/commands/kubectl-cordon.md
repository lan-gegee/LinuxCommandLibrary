# TAGLINE

将节点标记为不可调度

# TLDR

**封锁节点**

```kubectl cordon [node-name]```

**封锁多个节点**

```kubectl cordon [node1] [node2]```

**使用选择器封锁**

```kubectl cordon -l [key=value]```

**试运行**

```kubectl cordon [node-name] --dry-run=client```

# SYNOPSIS

**kubectl cordon** [_options_] _node_

# PARAMETERS

_NODE_
> 要封锁的节点名称。

**-l** _SELECTOR_
> 标签选择器。

**--dry-run** _MODE_
> 模拟操作。

**--help**
> 显示帮助信息。

# DESCRIPTION

**kubectl cordon** 通过在节点对象上设置 `node.kubernetes.io/unschedulable` 污点，将一个或多个 Kubernetes 节点标记为不可调度。节点被封锁后，调度器不会再向该节点放置任何新 Pod，但已在其上运行的现有 Pod 继续正常运行，不受影响。

封锁通常是节点维护工作流的第一步，随后用 `kubectl drain` 优雅地驱逐正在运行的 Pod。它也适用于在排查问题时隔离出现异常的节点（例如资源占用过高或硬件错误），同时不影响已在其中运行的工作负载。

要将被封锁的节点恢复正常调度，请使用 `kubectl uncordon`。可以通过 `kubectl get nodes` 检查节点状态来验证封锁状态，被封锁的节点会显示 `SchedulingDisabled` 状态。

# CAVEATS

kubectl 的子命令。维护时与 drain 配合使用。使用 uncordon 恢复。

# HISTORY

kubectl cordon 为 **Kubernetes** 集群维护提供节点调度控制功能。

# INSTALL

```apt: sudo apt install kubectl```

```pacman: sudo pacman -S kubectl```

```apk: sudo apk add kubectl```

```brew: brew install kubectl```

```nix: nix profile install nixpkgs#kubectl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [kubectl-drain](/man/kubectl-drain)(1), [kubectl-uncordon](/man/kubectl-uncordon)(1)
