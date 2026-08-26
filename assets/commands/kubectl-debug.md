# TAGLINE

创建临时调试容器

# TLDR

**调试 Pod**

```kubectl debug [pod-name] -it --image=[busybox]```

**复制 Pod 进行调试**

```kubectl debug [pod-name] -it --copy-to=[debug-pod]```

**用不同的容器调试**

```kubectl debug [pod-name] -it --container=[container] --image=[image]```

**调试节点**

```kubectl debug node/[node-name] -it --image=[busybox]```

**共享进程命名空间**

```kubectl debug [pod-name] -it --image=[busybox] --share-processes```

# SYNOPSIS

**kubectl debug** [_options_] _resource_

# PARAMETERS

_RESOURCE_
> 要调试的 Pod 或节点。

**--image** _IMAGE_
> 调试容器的镜像。

**-it**
> 交互式 TTY。

**--copy-to** _NAME_
> 创建调试副本。

**--container** _NAME_
> 目标容器。

**--share-processes**
> 共享进程命名空间。

**--help**
> 显示帮助信息。

# DESCRIPTION

**kubectl debug** 在运行中的 Pod 或节点内创建临时容器，用于交互式排查问题，且无需修改原始 Pod 规格。这对调试缺少 Shell 和诊断工具的极简镜像或 distroless 镜像尤其有用，因为调试容器可以基于 busybox 或 alpine 等功能齐全的镜像，同时共享目标 Pod 的网络和进程命名空间。

该命令支持多种调试策略。可以将临时容器直接注入现有 Pod，也可以使用 `--copy-to` 复制 Pod，创建一个隔离的调试克隆而不干扰原始工作负载。对于节点级排查，`kubectl debug node/` 会在指定节点上创建一个特权 Pod 并挂载主机文件系统，从而访问节点的操作系统以诊断系统级问题。`--share-processes` 标志启用进程命名空间共享，使调试容器能够查看并操作同一 Pod 中其他容器内的进程。

# CAVEATS

kubectl 的子命令。需要临时容器（ephemeral containers）支持。镜像必须包含所需的工具。

# HISTORY

kubectl debug 被加入 **Kubernetes**，用于对运行中的工作负载进行非侵入式调试。

# INSTALL

```apt: sudo apt install kubectl```

```pacman: sudo pacman -S kubectl```

```apk: sudo apk add kubectl```

```brew: brew install kubectl```

```nix: nix profile install nixpkgs#kubectl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [kubectl-exec](/man/kubectl-exec)(1)
