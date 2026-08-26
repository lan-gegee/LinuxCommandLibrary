# TAGLINE

在 Docker 中运行 K3s Kubernetes 集群

# TLDR

**创建集群**

```k3d cluster create [name]```

**创建多节点集群**

```k3d cluster create [name] --agents [3]```

**列出集群**

```k3d cluster list```

**删除集群**

```k3d cluster delete [name]```

**启动已停止的集群**

```k3d cluster start [name]```

**创建带端口映射的集群**

```k3d cluster create [name] -p "[8080:80@loadbalancer]"```

# SYNOPSIS

**k3d** _command_ [_options_]

# PARAMETERS

**cluster create** _NAME_
> 创建新集群。

**cluster delete** _NAME_
> 删除集群。

**cluster list**
> 列出集群。

**cluster start** _NAME_
> 启动集群。

**--agents** _N_
> agent 节点数量。

**-p** _MAPPING_
> 端口映射。

**--help**
> 显示帮助信息。

# DESCRIPTION

**k3d** 在 Docker 中运行 K3s Kubernetes 集群。它为开发提供快速的本地 Kubernetes 环境。

该工具可以轻松管理多个集群，并把容器的端口和卷映射到宿主机。

# CAVEATS

需要 Docker。面向开发场景，不适合生产环境。

# HISTORY

k3d 由 **Rancher** 创建，用于简化在 Docker 容器中运行 K3s 以进行本地 Kubernetes 开发。

# INSTALL

```brew: brew install k3d```

```nix: nix profile install nixpkgs#k3d```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[k3s](/man/k3s)(1), [kubectl](/man/kubectl)(1), [kind](/man/kind)(1), [docker](/man/docker)(1)
