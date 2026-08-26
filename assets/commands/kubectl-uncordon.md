# TAGLINE

将节点标记为可调度

# TLDR

**解除节点封锁**

```kubectl uncordon [node-name]```

**解除多个节点的封锁**

```kubectl uncordon [node1] [node2]```

**使用选择器解除封锁**

```kubectl uncordon -l [key=value]```

**试运行**

```kubectl uncordon [node-name] --dry-run=client```

# SYNOPSIS

**kubectl uncordon** [_options_] _node_

# PARAMETERS

_NODE_
> 要解除封锁的节点名称。

**-l** _SELECTOR_
> 标签选择器。

**--dry-run** _MODE_
> 模拟操作。

**--help**
> 显示帮助信息。

# DESCRIPTION

**kubectl uncordon** 将节点标记为可调度。它会撤销 cordon 的效果。

该命令在节点维护完成后使用。解除封锁后即可调度新 Pod。

# CAVEATS

kubectl 的子命令。只标记为可调度。Pod 不会自动迁回。

# HISTORY

kubectl uncordon 为 **Kubernetes** 在维护后恢复节点调度提供支持。

# INSTALL

```apt: sudo apt install kubectl```

```pacman: sudo pacman -S kubectl```

```apk: sudo apk add kubectl```

```brew: brew install kubectl```

```nix: nix profile install nixpkgs#kubectl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [kubectl-cordon](/man/kubectl-cordon)(1), [kubectl-drain](/man/kubectl-drain)(1)
