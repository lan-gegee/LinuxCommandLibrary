# TAGLINE

启动本地 Kubernetes 集群

# TLDR

**启动 minikube 集群**

```minikube start```

**以指定驱动启动**

```minikube start --driver=[docker]```

**以指定 Kubernetes 版本启动**

```minikube start --kubernetes-version=[v1.28.0]```

**以更多资源启动**

```minikube start --cpus=[4] --memory=[8192]```

**以指定配置档案启动**

```minikube start -p [profile-name]```

# SYNOPSIS

**minikube** **start** [_options_]

# PARAMETERS

**--driver** _name_
> VM 驱动（docker、virtualbox、kvm2）。

**--kubernetes-version** _version_
> Kubernetes 版本。

**--cpus** _count_
> CPU 数量。

**--memory** _mb_
> 内存大小（MB）。

**-p**, **--profile** _name_
> 配置档案名称。

**--nodes** _count_
> 节点数量。

# DESCRIPTION

**minikube start** 启动本地 Kubernetes 集群。创建运行 Kubernetes 的 VM 或容器。默认驱动取决于平台。支持多个配置档案以管理不同集群。

# INSTALL

```pacman: sudo pacman -S minikube```

```zypper: sudo zypper install minikube```

```brew: brew install minikube```

```nix: nix profile install nixpkgs#minikube```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[minikube](/man/minikube)(1), [kubectl](/man/kubectl)(1)
