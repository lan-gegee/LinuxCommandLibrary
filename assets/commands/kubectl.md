# TAGLINE

Kubernetes 命令行工具

# TLDR

**获取资源**

```kubectl get [pods|deployments|services|nodes]```

**描述资源**

```kubectl describe [pod] [name]```

**应用清单**

```kubectl apply -f [manifest.yaml]```

**删除资源**

```kubectl delete [pod] [name]```

**查看日志**

```kubectl logs [pod-name]```

**在 Pod 中执行命令**

```kubectl exec -it [pod-name] -- [/bin/bash]```

**端口转发**

```kubectl port-forward [pod-name] [8080:80]```

# SYNOPSIS

**kubectl** [_options_] _command_ [_type_] [_name_] [_flags_]

# PARAMETERS

**get** _TYPE_ [_NAME_]
> 列出指定类型的资源。

**describe** _TYPE_ _NAME_
> 显示资源的详细信息。

**apply** **-f** _FILE_
> 从文件或目录应用配置。

**delete** _TYPE_ _NAME_
> 删除资源。

**logs** _POD_ [**-c** _container_]
> 显示 Pod 日志，可选指定容器。

**exec** [**-it**] _POD_ **--** _COMMAND_
> 在容器中执行命令。

**port-forward** _POD_ _LOCAL:REMOTE_
> 将本地端口转发到 Pod 端口。

**scale** _TYPE/NAME_ **--replicas**=_N_
> 将资源伸缩到 N 个副本。

**create** _TYPE_ _NAME_
> 以命令式方式创建资源。

**edit** _TYPE_ _NAME_
> 在默认编辑器中编辑资源。

**-n**, **--namespace** _NAMESPACE_
> 目标命名空间。

**-o**, **--output** _FORMAT_
> 输出格式：json、yaml、wide、name。

**-l**, **--selector** _LABEL_
> 按标签选择器过滤。

**--context** _CONTEXT_
> 要使用的 kubeconfig 上下文。

**-A**, **--all-namespaces**
> 跨所有命名空间列出资源。

# DESCRIPTION

**kubectl** 是 Kubernetes 的官方命令行界面，用于与集群的 API 服务器通信以管理和检查资源。它支持 Kubernetes 对象的完整生命周期，包括通过声明式清单或命令式命令创建、读取、更新和删除 Pod、deployment、service、configmap 等各类资源。

该工具从 kubeconfig 文件读取连接详情，其中定义的集群、用户和上下文决定了 kubectl 面向哪个集群和命名空间。除了基本的资源管理外，kubectl 还提供日志获取和 exec 会话调试、工作负载伸缩、滚动更新（rollout）、向 Pod 端口转发，以及应用 YAML 或 JSON 清单中的配置更改等能力。集群侧基于角色的访问控制（RBAC）决定每个已认证用户可以执行哪些操作。

# CAVEATS

需要 kubeconfig。上下文决定目标集群。RBAC 影响访问权限。

# HISTORY

kubectl 是 **Kubernetes** 的官方 CLI，作为主要的集群管理界面而开发。

# INSTALL

```apt: sudo apt install kubectl```

```pacman: sudo pacman -S kubectl```

```apk: sudo apk add kubectl```

```brew: brew install kubectl```

```nix: nix profile install nixpkgs#kubectl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubeadm](/man/kubeadm)(1), [k9s](/man/k9s)(1), [helm](/man/helm)(1), [kubectx](/man/kubectx)(1)
