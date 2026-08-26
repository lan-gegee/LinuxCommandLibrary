# TAGLINE

创建虚拟 Kubernetes 集群

# TLDR

**创建集群**

```vcluster create [name]```

**连接到集群**

```vcluster connect [name]```

**列出集群**

```vcluster list```

**删除集群**

```vcluster delete [name]```

**断开连接**

```vcluster disconnect```

**暂停集群**

```vcluster pause [name]```

# SYNOPSIS

**vcluster** _command_ [_options_] [_name_]

# PARAMETERS

**create**
> 创建虚拟集群。

**connect**
> 连接 kubectl。

**list**
> 列出集群。

**delete**
> 移除集群。

**disconnect**
> 断开 kubectl 连接。

**--namespace** _NS_
> Kubernetes 命名空间。

# DESCRIPTION

**vcluster** 创建运行在现有 Kubernetes 集群内部的轻量级虚拟 Kubernetes 集群。每个虚拟集群拥有自己的 API 服务器和控制平面，但共享底层宿主集群的计算资源和网络。

这种方式为多租户、开发和测试提供完整的 Kubernetes 隔离，而无需承担独立物理集群的开销。虚拟集群可在数秒内创建，不使用时可暂停以释放资源。

# CAVEATS

需要 Kubernetes。需要宿主集群。Loft Labs 出品。

# HISTORY

**vcluster** 由 **Loft Labs** 创建，用于在现有集群内部运行轻量级虚拟 Kubernetes 集群。

# INSTALL

```brew: brew install vcluster```

```nix: nix profile install nixpkgs#vcluster```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [k3s](/man/k3s)(1), [kind](/man/kind)(1)
