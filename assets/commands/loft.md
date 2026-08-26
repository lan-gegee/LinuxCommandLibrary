# TAGLINE

管理虚拟 Kubernetes 集群和命名空间

# TLDR

**启动 Loft**

```loft start```

**登录 Loft**

```loft login [https://loft.example.com]```

**创建虚拟集群**

```loft create vcluster [name]```

**列出虚拟集群**

```loft list vclusters```

**连接到空间**

```loft use space [name]```

**创建空间**

```loft create space [name]```

# SYNOPSIS

**loft** _command_ [_options_]

# PARAMETERS

_COMMAND_
> Loft 操作。

**start**
> 启动 Loft 服务器。

**login** _URL_
> 登录 Loft 实例。

**create** _TYPE_ _NAME_
> 创建资源。

**list** _TYPE_
> 列出资源。

**use** _TYPE_ _NAME_
> 切换上下文。

**--help**
> 显示帮助信息。

# DESCRIPTION

**loft** 管理虚拟 Kubernetes 集群和命名空间，为团队提供自助式的 Kubernetes 服务。

该工具在共享集群上实现多租户，能快速创建隔离的虚拟集群。

# CAVEATS

需要 Kubernetes 集群。需要 Loft 平台。商业产品。

# HISTORY

Loft 由 **Loft Labs** 创建，旨在为开发者提供虚拟集群技术和自助式 Kubernetes。

# SEE ALSO

[kubectl](/man/kubectl)(1), [vcluster](/man/vcluster)(1), [helm](/man/helm)(1)
