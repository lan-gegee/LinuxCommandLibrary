# TAGLINE

显示详细的资源信息

# TLDR

**描述 Pod**

```kubectl describe pod [pod-name]```

**描述节点**

```kubectl describe node [node-name]```

**描述 deployment**

```kubectl describe deployment [deployment-name]```

**使用选择器描述**

```kubectl describe pods -l [app=myapp]```

**在命名空间内描述**

```kubectl describe pod [pod-name] -n [namespace]```

# SYNOPSIS

**kubectl describe** [_options_] _resource_ [_name_]

# PARAMETERS

_RESOURCE_
> 资源类型（pod、node、deployment 等）。

_NAME_
> 资源名称（可选）。

**-l** _SELECTOR_
> 标签选择器。

**-n** _NAMESPACE_
> 目标命名空间。

**--all-namespaces**
> 搜索所有命名空间。

**--help**
> 显示帮助信息。

# DESCRIPTION

**kubectl describe** 为一个或多个 Kubernetes 资源生成详细、人类可读的摘要。与返回结构化数据字段的 `kubectl get` 不同，describe 聚合多次 API 调用的信息，呈现一个全面的视图，包括资源元数据、spec、当前状态、条件、已分配的资源、挂载的卷以及相关事件。

该命令对排查问题特别有价值，因为输出底部的 Events 部分显示了控制器、调度器和 kubelet 最近执行的操作，例如镜像拉取失败、调度决策、就绪探针结果和容器重启。对于节点，它会显示容量、可分配资源、运行中的 Pod 以及系统状况。

describe 的输出面向人类阅读，不应被程序解析。若需要适合脚本处理的结构化数据，请改用 `kubectl get -o json` 或 `kubectl get -o yaml`。

# CAVEATS

kubectl 的子命令。输出不适合解析。结构化数据请使用 get -o json。

# HISTORY

kubectl describe 为 **Kubernetes** 排查问题提供详细的资源检查能力。

# INSTALL

```apt: sudo apt install kubectl```

```pacman: sudo pacman -S kubectl```

```apk: sudo apk add kubectl```

```brew: brew install kubectl```

```nix: nix profile install nixpkgs#kubectl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [kubectl-get](/man/kubectl-get)(1), [kubectl-logs](/man/kubectl-logs)(1)
