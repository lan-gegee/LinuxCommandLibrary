# TAGLINE

同时跟踪多个 Pod 的日志

# TLDR

**按名称模式跟踪 Pod**

```kubetail [pod-name-prefix]```

**按标签选择器跟踪 Pod**

```kubetail -l [app=myapp]```

**在指定命名空间内跟踪**

```kubetail [pattern] -n [namespace]```

**跟踪指定容器**（可重复）

```kubetail [pattern] -c [container]```

**只显示最近 N 分钟的日志**

```kubetail [pattern] -s [10m]```

**显示时间戳**

```kubetail [pattern] --timestamps```

**用正则表达式匹配跟踪**

```kubetail "[^app1|.*demo.*]" --regex```

**试运行：只列出匹配的 Pod 而不跟踪**

```kubetail [pattern] -d```

# SYNOPSIS

**kubetail** [_pod-pattern_] [_options_]

# PARAMETERS

_PATTERN_
> Pod 名称模式（默认为前缀匹配，配合 --regex 为正则匹配）。

**-c**, **--container** _NAME_
> 容器名称（多个容器时可重复）。

**-t**, **--context** _CONTEXT_
> 要使用的 Kubernetes 上下文。

**-l**, **--selector** _SELECTOR_
> 标签选择器（例如 app=myapp）。

**-n**, **--namespace** _NAMESPACE_
> 目标命名空间。

**-e**, **--regex** _MODE_
> 匹配模式：regex 或 substring。

**-s**, **--since** _DURATION_
> 显示相对时长以来的日志（例如 10m、1h）。

**-p**, **--previous** _BOOL_
> 获取上一个 Pod 实例的日志。

**-f**, **--follow** _BOOL_
> 持续跟踪日志流（默认 true）。

**-d**, **--dry-run**
> 打印匹配的 Pod/容器而不跟踪日志。

**-k**, **--colored-output** _MODE_
> 着色模式：pod、line（默认）、loglevel 或 false。

**-z**, **--skip-colors** _LIST_
> 以逗号分隔的要跳过的颜色索引。

**-P**, **--prefix** _BOOL_
> 开关每行的 Pod 名称前缀。

**-b**, **--line-buffered** _BOOL_
> 控制行缓冲。

**-j**, **--jq** _SELECTOR_
> 对 JSON 日志行应用 jq 选择器。

**-r**, **--cluster** _NAME_
> kubeconfig 中的集群名称。

**--tail** _LINES_
> 限制每个 Pod 的最近行数。

**--timestamps**
> 在日志行上显示时间戳。

**-i**, **--show-color-index** _BOOL_
> 在 Pod 前缀旁显示颜色索引。

**-v**, **--version**
> 显示版本。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**kubetail** 是一个 Bash 脚本，可以同时聚合并跟踪多个 Kubernetes Pod 的日志输出。它按名称前缀、正则表达式或标签选择器匹配 Pod，并将它们的日志流式输出到同一个终端，用颜色编码来区分来自不同 Pod 的行。

在调试分布式应用或微服务时该工具非常有用，因为相关的日志条目往往分散在多个 Pod 副本中。在底层，kubetail 会启动多个 `kubectl logs --follow` 进程并合并其输出，可选按命名空间、容器或时间范围过滤。

大多数标志的默认值可以通过环境变量设置，例如 KUBETAIL_NAMESPACE、KUBETAIL_SINCE、KUBETAIL_TAIL 和 KUBETAIL_COLORED_OUTPUT。

# CAVEATS

第三方 Bash 脚本（不属于 kubectl）。需要配置好集群访问的 `kubectl`。若需要功能类似的 Go 实现，请参考 stern。

# HISTORY

kubetail 由 Johan Haleby 创建，旨在用一条命令简化对多个 Kubernetes Pod 日志的跟踪。

# INSTALL

```brew: brew install kubetail```

```nix: nix profile install nixpkgs#kubetail```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [stern](/man/stern)(1), [k9s](/man/k9s)(1)
