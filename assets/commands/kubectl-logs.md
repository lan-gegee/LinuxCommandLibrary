# TAGLINE

输出 Pod 中容器的日志

# TLDR

**查看 Pod 日志**

```kubectl logs [pod-name]```

**实时跟踪日志**

```kubectl logs -f [pod-name]```

**查看指定容器的日志**

```kubectl logs [pod-name] -c [container]```

**查看上一个容器的日志**

```kubectl logs [pod-name] --previous```

**显示最后 N 行**

```kubectl logs [pod-name] --tail=[100]```

**查看最近一小时的日志**

```kubectl logs [pod-name] --since=[1h]```

# SYNOPSIS

**kubectl** **logs** [_options_] _pod-name_

# PARAMETERS

**-f**, **--follow**
> 持续流式输出日志。

**-c**, **--container** _name_
> 容器名称。

**--previous**
> 输出上一个容器的日志。

**--tail** _lines_
> 从末尾开始的行数。

**--since** _duration_
> 显示比该时长更新的日志。

**--timestamps**
> 包含时间戳。

# DESCRIPTION

**kubectl logs** 检索并显示 Kubernetes Pod 内运行容器的标准输出和标准错误流。它是调试应用行为、诊断崩溃以及监控集群环境中运行时输出的主要工具之一。

该命令支持使用 -f 标志进行实时日志流式传输，类似于 `tail -f`，并且可以使用 -c 选项定位多容器 Pod 中的特定容器。你还可以查看上一个容器实例的日志（通过 --previous 检查崩溃循环很有用）、用 --tail 限制输出到最近的条目，或用 --since 和 --since-time 按时间窗口过滤。配合标签选择器使用时，它可以同时聚合多个 Pod 的日志。

# INSTALL

```apt: sudo apt install kubectl```

```pacman: sudo pacman -S kubectl```

```apk: sudo apk add kubectl```

```brew: brew install kubectl```

```nix: nix profile install nixpkgs#kubectl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [kubectl-exec](/man/kubectl-exec)(1)
