# TAGLINE

Kubernetes 集群安全评估

# TLDR

**运行 Kubernetes 安全评估**

```prowler kubernetes```

**使用特定上下文运行**

```prowler kubernetes --context [my-cluster]```

**运行特定检查项**

```prowler kubernetes --checks [pod_security_policy]```

**输出为 JSON**

```prowler kubernetes -M json -o [results/]```

# SYNOPSIS

**prowler kubernetes** [_options_]

# PARAMETERS

**--checks** _checks_
> 要运行的特定检查项。

**--context** _name_
> Kubernetes 上下文。

**--namespace** _name_
> 目标命名空间。

**--compliance** _framework_
> 合规框架。

**-M**, **--output-modes** _format_
> 输出格式。

**-o**, **--output-directory** _dir_
> 输出目录。

# DESCRIPTION

**prowler kubernetes** 对 Kubernetes 集群执行安全评估。它检查配置错误、RBAC 问题、Pod 安全违规，并对照 CIS Kubernetes Benchmark 等安全最佳实践进行合规性评估。

该工具使用当前的 kubeconfig 上下文连接集群，并跨命名空间评估资源。结果可以按特定检查项、命名空间或合规框架过滤。

# CAVEATS

需要具有读取集群资源的相应 RBAC 权限。部分检查需要 cluster-admin 访问权限。结果反映扫描时的当前状态。`--context` 标志必须与现有的 kubeconfig 上下文匹配。

# INSTALL

```brew: brew install prowler```

```nix: nix profile install nixpkgs#prowler```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[prowler](/man/prowler)(1), [kubectl](/man/kubectl)(1)
