# TAGLINE

更新资源字段

# TLDR

**设置镜像**

```kubectl set image deployment/[name] [container]=[image:tag]```

**设置环境变量**

```kubectl set env deployment/[name] [KEY=value]```

**设置资源限制**

```kubectl set resources deployment/[name] -c [container] --limits=[cpu=200m,memory=512Mi]```

**设置服务账户**

```kubectl set serviceaccount deployment/[name] [sa-name]```

**设置选择器**

```kubectl set selector service/[name] [app=myapp]```

# SYNOPSIS

**kubectl set** _command_ [_options_]

# PARAMETERS

**image** _RESOURCE_ _CONTAINER=IMAGE_
> 更新容器镜像。

**env** _RESOURCE_ _VAR=VALUE_
> 设置环境变量。

**resources** _RESOURCE_
> 设置资源限制。

**serviceaccount** _RESOURCE_ _SA_
> 设置服务账户。

**selector** _RESOURCE_ _LABELS_
> 设置选择器。

**--help**
> 显示帮助信息。

# DESCRIPTION

**kubectl set** 更新资源字段。它修改运行中工作负载的特定方面。

对于针对性的更改，该命令比完整的 apply 更快。它会触发 deployment 的发布。

# CAVEATS

kubectl 的子命令。会触发发布。声明式管理请考虑使用 apply。

# HISTORY

kubectl set 为 **Kubernetes** 运维任务提供有针对性的资源更新。

# INSTALL

```apt: sudo apt install kubectl```

```pacman: sudo pacman -S kubectl```

```apk: sudo apk add kubectl```

```brew: brew install kubectl```

```nix: nix profile install nixpkgs#kubectl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [kubectl-apply](/man/kubectl-apply)(1), [kubectl-rollout](/man/kubectl-rollout)(1)
