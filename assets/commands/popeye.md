# TAGLINE

扫描 Kubernetes 集群中的问题

# TLDR

**扫描 Kubernetes 集群**

```popeye```

**扫描特定命名空间**

```popeye -n [namespace]```

**使用特定上下文扫描**

```popeye --context [context]```

**以 JSON 格式输出**

```popeye -o json```

**将报告保存到文件**

```popeye --save --out [dir]```

# SYNOPSIS

**popeye** [_options_]

# PARAMETERS

**-n**, **--namespace** _NS_
> 扫描特定命名空间。

**--context** _CTX_
> Kubernetes 上下文。

**-o**, **--out** _FORMAT_
> 输出格式（json、yaml、html）。

**--save**
> 将报告保存到文件。

**-A**, **--all-namespaces**
> 扫描所有命名空间。

# DESCRIPTION

**popeye** 扫描运行中的 Kubernetes 集群，报告潜在问题、错误配置和资源问题。它依据最佳实践和常见陷阱检查 pod、service、deployment 等资源。

结果按严重程度用颜色标记（OK、info、warning、error）。使用 **-n** 扫描特定命名空间，**-o** 指定机器可读的输出格式（JSON、YAML、HTML），**--save** 将报告写入磁盘。所有操作均为只读。

# CAVEATS

需要集群访问权限。操作均为只读。

# HISTORY

Popeye 作为 **Kubernetes 集群清理器**和 linter 而创建。

# INSTALL

```pacman: sudo pacman -S popeye```

```zypper: sudo zypper install popeye```

```brew: brew install popeye```

```nix: nix profile install nixpkgs#popeye```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [kube-linter](/man/kube-linter)(1)
