# TAGLINE

列出集群事件

# TLDR

在当前命名空间内**显示事件**

```kubectl events```

在指定命名空间内**显示事件**

```kubectl events -n [namespace]```

跨所有命名空间**显示事件**

```kubectl events -A```

**限定于特定资源的事件**

```kubectl events --for [pod/pod-name]```

**实时监视事件**的到来

```kubectl events --watch```

**仅显示 Warning**（按事件类型过滤）

```kubectl events --types=[Warning]```

按时间先后**对事件排序**（最早的在前）

```kubectl events --sort-by=[lastTimestamp]```

**以 JSON 格式输出**

```kubectl events -o json```

# SYNOPSIS

**kubectl events** [_options_]

# PARAMETERS

**-n** _NAMESPACE_
> 目标命名空间（默认：当前上下文的命名空间）。

**-A**, **--all-namespaces**
> 列出所有命名空间的事件。

**--for** _KIND/NAME_
> 只显示 **involvedObject** 匹配给定资源的事件（例如 **pod/web-0**）。

**--watch**, **-w**
> 持续流式输出新事件，而不是输出一次快照后退出。

**--types** _TYPES_
> 逗号分隔的事件类型（Normal、Warning）。

**--sort-by** _FIELD_
> 按 JSONPath 字段排序，通常为 **.lastTimestamp** 或 **.metadata.creationTimestamp**。

**-o** _FORMAT_
> 输出格式（wide、json、yaml、jsonpath 等）。

**--no-headers**
> 不显示列标题行。

**--help**
> 显示帮助信息。

# DESCRIPTION

**kubectl events** 是用于列出 Kubernetes Event 对象的现代专用子命令。它在 **kubectl 1.23** 中作为 alpha 功能加入，并在 **1.27** 中转为 GA，取代了较旧的 **kubectl get events** 形式，提供更整洁的默认输出和实时监视支持。

事件是由各控制器（kubelet、调度器、controller-manager、自定义 operator 等）发出的短期记录，描述值得注意的状态变化，例如 Pod 调度、镜像拉取、存活探针失败或 HPA 扩缩容决策。使用 **--for** 跟踪特定的 Pod、Deployment 或 Job，使用 **--watch** 进行实时调试，并使用 **--sort-by** 将最新事件放在底部以便按时间顺序阅读。

# CAVEATS

事件会在 **--event-ttl**（默认 **1 小时**）后过期；历史事件需要外部聚合器（Loki、Elasticsearch、Datadog）或对 Events API 的持久化存储。**--for** 是精确匹配：监视子资源 Pod 时不会显示父资源（Deployment）上发出的事件。在某些较旧的发行版中，**kubectl events** 是一个独立插件；在这些环境中请回退到 **kubectl get events**。

# HISTORY

**kubectl events** 作为 alpha 命令随 **Kubernetes 1.23**（2021 年 12 月）发布，在 **1.25** 中进入 beta，并于 **1.27**（2023 年 4 月）正式可用。它的推出是为了整合此前 **kubectl get events** 所需的多种标志，让临时性的集群调试更符合人体工学。

# INSTALL

```apt: sudo apt install kubectl```

```pacman: sudo pacman -S kubectl```

```apk: sudo apk add kubectl```

```brew: brew install kubectl```

```nix: nix profile install nixpkgs#kubectl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [kubectl-describe](/man/kubectl-describe)(1), [kubectl-logs](/man/kubectl-logs)(1)
