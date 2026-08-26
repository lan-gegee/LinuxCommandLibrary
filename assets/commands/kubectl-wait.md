# TAGLINE

阻塞直到满足条件为止

# TLDR

**等待 Pod 就绪**

```kubectl wait --for=condition=Ready pod/[pod-name]```

**等待删除完成**

```kubectl wait --for=delete pod/[pod-name]```

**等待创建完成**

```kubectl wait --for=create secret/[name]```

**带超时等待**

```kubectl wait --for=condition=Ready pod/[pod-name] --timeout=[60s]```

**等待 deployment 可用**

```kubectl wait --for=condition=Available deployment/[name]```

**用标签选择器跨资源等待**

```kubectl wait --for=condition=Ready pods -l [app=myapp]```

**等待某个 JSONPath 值**

```kubectl wait --for=jsonpath='{.status.phase}'=Running pod/[name]```

**跨所有命名空间等待**

```kubectl wait --for=condition=Ready pods --all -A```

# SYNOPSIS

**kubectl wait** [_options_] _resource_

# PARAMETERS

_RESOURCE_
> 要等待的资源，例如 `pod/busybox`、`deployment/web`，或 `pods` 这类类型。

**--for** _EXPR_
> 要等待的条件。接受 `create`、`delete`、`condition=<name>[=<value>]` 或 `jsonpath='{...}'[=<value>]`。条件值默认为 `true`。

**--timeout** _DURATION_
> 最长等待时间（例如 30s、5m）。默认为 30s。零表示只检查一次；负值最多等待一周。

**--all**
> 选择命名空间中给定类型的所有资源。

**-A**, **--all-namespaces**
> 跨所有命名空间操作。

**-l**, **--selector** _QUERY_
> 用于过滤资源的标签选择器。

**--field-selector** _QUERY_
> 用于过滤资源的字段选择器。

**-f**, **--filename** _FILE_
> 通过清单文件或目录标识资源。

**-n**, **--namespace** _NS_
> 目标命名空间。

**-o**, **--output** _FORMAT_
> 输出格式（json、yaml、name、go-template、jsonpath 等）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**kubectl wait** 会阻塞执行，直到一个或多个 Kubernetes 资源达到指定条件，是 Shell 脚本、CI/CD 流水线和自动化工作流中不可或缺的同步原语。它不会反复轮询 `kubectl get`，而是高效地监视资源，一旦条件满足或超时即返回。

该命令支持内置的条件检查（如 `condition=Ready` 和 `condition=Available`）、通过 `--for=delete` 监听资源删除事件，以及通过 JSONPath 表达式（如 `jsonpath='{.status.phase}'=Running`）进行任意字段匹配。它可以按名称定位单个资源，也可以定位由标签选择器匹配到的资源组；除非用 --timeout 覆盖，默认超时始终为 30 秒。

# CAVEATS

kubectl 的子命令。会阻塞执行。请设置合理的超时时间。

# HISTORY

kubectl wait 为 **Kubernetes** 自动化和脚本编写提供同步能力。

# INSTALL

```apt: sudo apt install kubectl```

```pacman: sudo pacman -S kubectl```

```apk: sudo apk add kubectl```

```brew: brew install kubectl```

```nix: nix profile install nixpkgs#kubectl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [kubectl-get](/man/kubectl-get)(1), [kubectl-apply](/man/kubectl-apply)(1), [kubectl-rollout](/man/kubectl-rollout)(1), [kubectl-describe](/man/kubectl-describe)(1)
