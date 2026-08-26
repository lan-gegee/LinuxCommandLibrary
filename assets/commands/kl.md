# TAGLINE

终端中的交互式 Kubernetes 日志查看器

# TLDR

**查看**当前 Kubernetes 上下文的日志

```kl```

**查看指定命名空间的日志**

```kl -n [namespace]```

**查看匹配某个模式的日志**

```kl [pattern]```

# SYNOPSIS

**kl** [_options_] [_pattern_]

# DESCRIPTION

**kl** 是一款面向终端的交互式 Kubernetes 日志查看器。它让你可以跨多个容器、Pod、命名空间和集群查看日志，既可以通过交互方式选择容器，也可以按名称和标签自动进行模式匹配。

功能包括实时日志流、容器过滤、日志归档、剪贴板复制和全屏视图。你可以聚焦特定容器的日志、按标签过滤，并切换不同的 Kubernetes 上下文来缩小想要查看的日志范围。

# CAVEATS

需要可用的 kubectl 配置。日志的可用性取决于 Kubernetes 集群设置和 Pod 日志保留策略。

# HISTORY

**kl** 由 **robinovitch61** 创建，以 **Go** 编写。它的定位是比通用 Kubernetes 管理工具更专注的替代品，专门针对日志查看工作流进行了优化。

# INSTALL

```zypper: sudo zypper install kl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [k9s](/man/k9s)(1), [stern](/man/stern)(1)
