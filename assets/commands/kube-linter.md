# TAGLINE

分析 Kubernetes YAML 文件和 Helm chart 的安全性与最佳实践

# TLDR

**对 Kubernetes 清单进行静态检查**

```kube-linter lint [path/to/manifests]```

**对 Helm chart 进行静态检查**

```kube-linter lint [path/to/chart]```

**列出可用的检查项**

```kube-linter checks list```

**使用指定检查项进行静态检查**

```kube-linter lint --include [no-read-only-root-fs] [path]```

**排除检查项**

```kube-linter lint --exclude [run-as-non-root] [path]```

**以 JSON 格式输出**

```kube-linter lint --format json [path]```

# SYNOPSIS

**kube-linter** _command_ [_options_]

# PARAMETERS

**lint** _path_
> 对清单或 chart 进行静态检查。

**checks list**
> 列出可用的检查项。

**--include** _checks_
> 只运行指定的检查项。

**--exclude** _checks_
> 跳过指定的检查项。

**--config** _file_
> 配置文件。

**--format** _format_
> 输出格式：plain、json、sarif。

**--fail-on-invalid-resource**
> 遇到无效 YAML 时失败。

# DESCRIPTION

**kube-linter** 分析 Kubernetes YAML 文件和 Helm chart 的安全性与最佳实践。它能发现缺失安全上下文、资源限制以及权限提升风险等配置错误。

该工具专为 CI/CD 集成而设计，帮助在部署前发现问题。

# CHECKS EXAMPLES

```
no-read-only-root-fs      Root filesystem not read-only
run-as-non-root           Container runs as root
unset-cpu-requirements    CPU limits not set
unset-memory-requirements Memory limits not set
latest-tag                Using 'latest' image tag
```

# CONFIGURATION

```yaml
# .kube-linter.yaml
checks:
  addAllBuiltIn: true
  exclude:
    - "latest-tag"
```

# CAVEATS

可能产生误报。并非所有检查项都适用于所有工作负载。自定义检查需要 Go。Helm chart 检查需要 Helm。

# HISTORY

kube-linter 由 **StackRox**（已被 Red Hat 收购）开发，旨在通过静态分析改善 Kubernetes 的安全状况。

# INSTALL

```pacman: sudo pacman -S kube-linter```

```zypper: sudo zypper install kube-linter```

```brew: brew install kube-linter```

```nix: nix profile install nixpkgs#kube-linter```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [kubeaudit](/man/kubeaudit)(1), [helm](/man/helm)(1)
