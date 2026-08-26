# TAGLINE

添加或移除节点污点

# TLDR

**为节点添加污点**

```kubectl taint nodes [node-name] [key=value:NoSchedule]```

**移除污点**

```kubectl taint nodes [node-name] [key:NoSchedule-]```

**添加 NoExecute 污点**

```kubectl taint nodes [node-name] [key=value:NoExecute]```

**添加 PreferNoSchedule**

```kubectl taint nodes [node-name] [key=value:PreferNoSchedule]```

**为多个节点添加污点**

```kubectl taint nodes [node1] [node2] [key=value:NoSchedule]```

# SYNOPSIS

**kubectl taint** [_options_] _node_ _key=value:effect_

# PARAMETERS

_NODE_
> 节点名称。

_KEY=VALUE:EFFECT_
> 污点规格。

**NoSchedule**
> 阻止调度。

**NoExecute**
> 驱逐现有 Pod。

**PreferNoSchedule**
> 尽量避免调度（软性）。

**-**（污点键的后缀）
> 移除匹配给定 _key:effect_ 对的污点（例如 **node1 dedicated:NoSchedule-**）。

**--all**
> 将污点操作应用到集群中的每个节点。

**-l**, **--selector** _SELECTOR_
> 只应用于匹配标签选择器的节点（例如 `--selector=role=worker`）。

**--overwrite**
> 允许更新现有污点的值（不加此标志时，尝试添加同键污点会产生错误）。

**--dry-run** _client|server|none_
> 打印将要发生的更改而不修改集群。

**--help**
> 显示帮助信息。

# DESCRIPTION

**kubectl taint** 添加、更新或移除节点污点。污点是附加在节点上的 _key=value:effect_ 三元组；只有当 Pod 的规格中带有匹配的 **toleration**（容忍）时，才会被调度到该节点或继续留在其上。支持的效果包括 **NoSchedule**（阻止不容忍它的新 Pod）、**PreferNoSchedule**（尽力避开）和 **NoExecute**（驱逐不容忍它的运行中 Pod）。

污点是将节点专用于某类工作负载（例如 GPU 节点）、让 Pod 远离控制平面节点，以及结合 **kubectl drain** 为维护优雅清空节点的标准机制。

# CAVEATS

**NoExecute** 会驱逐已调度但缺少匹配容忍的 Pod；在给已有负载的节点打污点前，请确保容忍配置到位。覆盖现有污点需要 **--overwrite**。移除污点时在污点键末尾加 **-**（无需值）。

# HISTORY

kubectl taint 为 **Kubernetes** 高级调度控制提供污点管理能力。

# INSTALL

```apt: sudo apt install kubectl```

```pacman: sudo pacman -S kubectl```

```apk: sudo apk add kubectl```

```brew: brew install kubectl```

```nix: nix profile install nixpkgs#kubectl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [kubectl-cordon](/man/kubectl-cordon)(1), [kubectl-label](/man/kubectl-label)(1)
