# TAGLINE

查找 Kubernetes 用户的 RBAC 角色

# TLDR

**查找用户的角色**

```rbac-lookup [user@example.com]```

**查找服务账号的角色**

```rbac-lookup [service-account-name] --kind serviceaccount```

**查找组的角色**

```rbac-lookup [group-name] --kind group```

**以宽格式输出**

```rbac-lookup [subject] -o wide```

**在命名空间内搜索**

```rbac-lookup [subject] -n [namespace]```

**主体的所有绑定**

```rbac-lookup [subject] --all-namespaces```

# SYNOPSIS

**rbac-lookup** [_--kind type_] [_-n namespace_] [_-o format_] [_options_] _subject_

# PARAMETERS

**--kind** _TYPE_
> 主体类型（user、group、serviceaccount）。

**-n**, **--namespace** _NS_
> 要搜索的命名空间。

**-A**, **--all-namespaces**
> 所有命名空间。

**-o**, **--output** _FORMAT_
> 输出格式。

**--gke**
> GKE 专用模式。

**-k**, **--kubeconfig** _FILE_
> Kubeconfig 文件。

# DESCRIPTION

**rbac-lookup** 查询 Kubernetes 集群，找出与给定主体关联的所有 RBAC 角色绑定，回答"这个用户、组或服务账号拥有哪些权限"的问题。它会同时搜索 ClusterRoleBinding 和命名空间级的 RoleBinding，完整呈现主体在整个集群中的访问权限。

该工具通过 **--kind** 标志支持按用户身份、组成员关系和服务账号名称进行查找。宽输出格式（**-o wide**）会显示详细的绑定信息，包括每项权限授予所在的命名空间、角色类型和来源绑定。这使它特别适合用于安全审计，以及在 RBAC 配置复杂的集群中排查访问问题。

# CONFIGURATION

**~/.kube/config**
> 默认的 kubeconfig 文件，指定集群连接、身份验证凭据和上下文选择。可用 **-k** 标志覆盖。

# CAVEATS

需要集群读取权限。大型集群可能较慢。聚合角色不会被展开。

# HISTORY

**rbac-lookup** 由 **FairwindsOps** 创建，用于 Kubernetes RBAC 审计。它简化了对复杂角色绑定关系的理解。

# SEE ALSO

[kubectl](/man/kubectl)(1), [rbac-tool](/man/rbac-tool)(1), [kubeaudit](/man/kubeaudit)(1)
