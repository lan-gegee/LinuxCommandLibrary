# TAGLINE

列出 Kubernetes 资源

# TLDR

**列出 Pod**

```kubectl get pods```

**列出所有资源**

```kubectl get all```

**将指定 Pod 输出为 YAML**

```kubectl get pod [pod-name] -o yaml```

**将所有 Pod 输出为 JSON**

```kubectl get pods -o json```

**监视 Pod 的变化**

```kubectl get pods --watch```

**跨所有命名空间列出 Pod**

```kubectl get pods -A```

**按标签过滤 Pod**

```kubectl get pods -l [app=nginx]```

**列出 Pod 并附加额外列**（节点、IP）

```kubectl get pods -o wide```

**自定义列输出**

```kubectl get pods -o custom-columns=NAME:.metadata.name,STATUS:.status.phase```

**从文件获取资源**

```kubectl get -f [path/to/manifest.yaml]```

# SYNOPSIS

**kubectl get** [_options_] _TYPE_[._VERSION_][._GROUP_] [_NAME_ | **-l** _label_]

# PARAMETERS

_RESOURCE_
> 资源类型（pods、deployments、services 等）。

_NAME_
> 资源名称（可选）。

**-o**, **--output** _FORMAT_
> 输出格式：json、yaml、wide、name、custom-columns、jsonpath、go-template 等。

**-w**, **--watch**
> 列出请求的对象之后持续监视变化。

**--watch-only**
> 只监视变化，不先列出/获取。

**-A**, **--all-namespaces**
> 跨所有命名空间列出对象。

**-l**, **--selector** _SELECTOR_
> 标签选择器（支持 =、==、!=、in、notin）。

**-n**, **--namespace** _NAMESPACE_
> 本次请求的命名空间范围。

**-f**, **--filename** _FILE_
> 标识资源的文件名、目录或 URL。

**-k**, **--kustomize** _DIR_
> 处理 kustomization 目录。

**--sort-by** _JSONPATH_
> 按指定的 JSONPath 表达式对列表输出排序。

**--field-selector** _SELECTOR_
> 按字段选择器过滤（例如 status.phase=Running）。

**-L**, **--label-columns** _LABELS_
> 以逗号分隔的标签列表，作为列展示。

**--show-labels**
> 在输出的最后一列显示所有标签。

**--show-kind**
> 为请求的对象列出资源类型。

**--no-headers**
> 输出中省略表头。

**--chunk-size** _N_
> 分块返回大列表而不是一次性全部返回（默认 500）。

**--ignore-not-found**
> 获取特定资源时抑制 NotFound 错误。

**-R**, **--recursive**
> 递归处理 -f 使用的目录。

**--help**
> 显示帮助信息。

# DESCRIPTION

**kubectl get** 从集群中检索并显示一个或多个 Kubernetes 资源。它是检查集群状态最常用的 kubectl 子命令，支持所有资源类型，包括 Pod、deployment、service、节点、configmap 以及 CRD 定义的自定义资源。

该命令通过 `-o` 标志提供灵活的输出格式，包括人类可读的表格、YAML、JSON、JSONPath 表达式和自定义列定义。结果可以按标签选择器、字段选择器和命名空间过滤，也可以用 `-A` 标志跨所有命名空间检索。`--watch` 标志通过 Kubernetes watch API 实现实时流式的资源变化推送。

默认情况下，输出显示包含名称、状态、存活时间等关键字段的摘要表格。`wide` 输出格式会增加额外的列，例如节点分配和 IP 地址；而 YAML 和 JSON 等结构化格式则返回完整的资源规格，适合脚本处理和自动化。

# CAVEATS

kubectl 的子命令。默认只显示当前命名空间中的资源；使用 `-A` 查看所有命名空间。`--watch` 标志使用 Kubernetes watch API，短暂断连期间可能丢失事件。`--chunk-size` 标志（默认 500）控制大结果集的分页。

# HISTORY

kubectl get 是 **Kubernetes** 集群检查的主要资源列举命令。

# INSTALL

```apt: sudo apt install kubectl```

```pacman: sudo pacman -S kubectl```

```apk: sudo apk add kubectl```

```brew: brew install kubectl```

```nix: nix profile install nixpkgs#kubectl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [kubectl-describe](/man/kubectl-describe)(1), [kubectl-apply](/man/kubectl-apply)(1), [kubectl-delete](/man/kubectl-delete)(1), [kubectl-logs](/man/kubectl-logs)(1)
