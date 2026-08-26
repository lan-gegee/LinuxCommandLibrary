# TAGLINE

删除 Kubernetes 资源

# TLDR

**删除 Pod**

```kubectl delete pod [pod-name]```

**从清单删除**

```kubectl delete -f [manifest.yaml]```

**删除所有 Pod**

```kubectl delete pods --all```

**按标签删除**

```kubectl delete pods -l [app=myapp]```

**强制删除**

```kubectl delete pod [pod-name] --force --grace-period=0```

**删除命名空间**

```kubectl delete namespace [namespace]```

# SYNOPSIS

**kubectl delete** [_options_] _resource_ [_name_]

# PARAMETERS

_RESOURCE_
> 资源类型。

_NAME_
> 资源名称。

**-f** _FILE_
> 从文件删除。

**-l** _SELECTOR_
> 标签选择器。

**--all**
> 删除所有资源。

**--force**
> 强制删除。

**--grace-period** _N_
> 宽限秒数。

**--help**
> 显示帮助信息。

# DESCRIPTION

**kubectl delete** 从 Kubernetes 集群中移除一个或多个资源。它可以按名称、标签选择器定位资源，也可以引用创建它们时使用的同一清单文件，因此可以轻松拆除 YAML 文件或目录中定义的所有内容。

默认情况下，该命令会发送优雅终止信号，并等待资源的宽限期（Pod 通常为 30 秒）后才强制移除。在此期间，Pod 会收到 SIGTERM，可以执行清理操作，例如排空连接或保存状态。`--force --grace-period=0` 标志会跳过优雅关闭，立即从 API 服务器移除资源，这适用于卡死的 Pod，但可能导致数据丢失。

删除 deployment 或 statefulset 等高层资源时，默认会级联删除其管理的 Pod。删除命名空间会移除其中的所有资源，因此在共享环境中应谨慎使用此操作。

# CAVEATS

kubectl 的子命令。破坏性操作。建议先使用 --dry-run。

# HISTORY

kubectl delete 为 **Kubernetes** 集群管理提供资源移除功能。

# INSTALL

```apt: sudo apt install kubectl```

```pacman: sudo pacman -S kubectl```

```apk: sudo apk add kubectl```

```brew: brew install kubectl```

```nix: nix profile install nixpkgs#kubectl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [kubectl-apply](/man/kubectl-apply)(1), [kubectl-create](/man/kubectl-create)(1)
