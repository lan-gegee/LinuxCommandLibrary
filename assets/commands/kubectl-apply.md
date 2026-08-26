# TAGLINE

创建或更新 Kubernetes 资源

# TLDR

**应用清单**

```kubectl apply -f [manifest.yaml]```

**应用目录**

```kubectl apply -f [manifests/]```

**从 URL 应用**

```kubectl apply -f [https://example.com/manifest.yaml]```

**使用 kustomization 应用**

```kubectl apply -k [directory/]```

**试运行**

```kubectl apply -f [manifest.yaml] --dry-run=client```

**服务端应用**

```kubectl apply -f [manifest.yaml] --server-side```

# SYNOPSIS

**kubectl apply** [_options_] **-f** _filename_

# PARAMETERS

**-f** _FILE_
> 文件、目录或 URL。

**-k** _DIR_
> Kustomization 目录。

**--dry-run** _MODE_
> client、server 或 none。

**--server-side**
> 服务端应用。

**--force-conflicts**
> 冲突时强制应用。

**-n** _NAMESPACE_
> 目标命名空间。

**--help**
> 显示帮助信息。

# DESCRIPTION

**kubectl apply** 使用声明式配置文件创建或更新 Kubernetes 资源。它将 YAML 或 JSON 清单中定义的期望状态与集群的当前状态进行比较，采用三方合并策略（综合考虑 last-applied 配置、实时状态和新清单），只做必要的更改来消除差异。

该命令接受来自本地文件、目录、URL 或 Kustomize overlay 的清单，非常适合集群状态纳入版本控制的 GitOps 工作流。它同时支持客户端和服务端两种应用模式，其中服务端应用通过字段所有权跟踪，在多个参与者管理同一资源时能提供更好的冲突检测。

这是在生产环境中管理 Kubernetes 资源的推荐方式，因为它会保留其他控制器所做的更改，并支持增量更新而无需替换完整的资源定义。

# CAVEATS

kubectl 的子命令。使用 last-applied 注解。管理资源时优先于 create 使用。

# HISTORY

kubectl apply 为 **Kubernetes** 实现了声明式资源管理，使 GitOps 工作流成为可能。

# INSTALL

```apt: sudo apt install kubectl```

```pacman: sudo pacman -S kubectl```

```apk: sudo apk add kubectl```

```brew: brew install kubectl```

```nix: nix profile install nixpkgs#kubectl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [kubectl-create](/man/kubectl-create)(1), [kubectl-delete](/man/kubectl-delete)(1)
