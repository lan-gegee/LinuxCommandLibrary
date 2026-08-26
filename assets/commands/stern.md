# TAGLINE

多 Pod Kubernetes 日志跟踪

# TLDR

**跟踪 Pod 日志**

```stern [pod-query]```

**指定命名空间跟踪日志**

```stern -n [namespace] [pod-query]```

**所有命名空间**

```stern --all-namespaces [pod-query]```

**指定容器**

```stern -c [container] [pod-query]```

**从某时间段开始**

```stern --since [10m] [pod-query]```

**显示时间戳**

```stern -t [pod-query]```

**正则匹配 Pod**

```stern --selector [app=nginx]```

**输出格式**

```stern -o json [pod-query]```

# SYNOPSIS

**stern** [_-n namespace_] [_-c container_] [_--since duration_] [_options_] _pod-query_

# PARAMETERS

**-n**, **--namespace** _NS_
> Kubernetes 命名空间。

**--all-namespaces**, **-A**
> 所有命名空间。

**-c**, **--container** _NAME_
> 容器名称。

**--since** _DURATION_
> 从指定时长之前开始输出日志。

**-t**, **--timestamps**
> 显示时间戳。

**-o**, **--output** _FORMAT_
> 输出格式。

**-s**, **--selector** _SELECTOR_
> 标签选择器。

**--tail** _N_
> 每个容器显示的行数。

# DESCRIPTION

**stern** 允许你同时跟踪多个 Kubernetes Pod 和容器的日志输出。它接受一个 Pod 名称查询（可以是正则表达式），并流式输出所有匹配 Pod 的日志行，自动纳入新出现的 Pod 并移除已终止的 Pod。

每个 Pod 和容器在输出中会被分配一种独特的颜色，便于直观区分日志行的来源。stern 支持按命名空间、容器名和标签选择器进行过滤，并能以多种格式输出日志，包括用于结构化处理的 JSON。

该工具对于调试微服务特别有用，因为相关功能往往分布在多个 Pod 或 Deployment 上。与一次只能跟随单个 Pod 的 `kubectl logs` 不同，stern 可以聚合任意数量匹配 Pod 的日志，并实时优雅地处理 Pod 重启和扩缩容事件。

# CAVEATS

需要 kubectl 访问权限。Pod 过多可能造成压力。网络延迟会影响流式输出。

# HISTORY

**stern** 由 **Wercker**（现属 Oracle）创建，用于 Kubernetes 日志跟踪。它简化了同时查看多个 Pod 日志的操作。

# INSTALL

```pacman: sudo pacman -S stern```

```zypper: sudo zypper install stern```

```brew: brew install stern```

```nix: nix profile install nixpkgs#stern```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [kubetail](/man/kubetail)(1), [k9s](/man/k9s)(1)
