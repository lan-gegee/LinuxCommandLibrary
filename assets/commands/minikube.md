# TAGLINE

运行本地单节点 Kubernetes 集群

# TLDR

**以默认驱动启动集群**

```minikube start```

**以指定的驱动启动**

```minikube start --driver=[docker]```

**以固定的 Kubernetes 版本启动**

```minikube start --kubernetes-version=[v1.30.0]```

**停止正在运行的集群**

```minikube stop```

**删除集群及其数据**

```minikube delete```

**检查集群状态**

```minikube status```

**在浏览器中打开 Kubernetes 仪表板**

```minikube dashboard```

**SSH 进入集群节点**

```minikube ssh```

**获取暴露在集群内的服务 URL**

```minikube service [service_name] --url```

**启用内置插件**

```minikube addons enable [ingress]```

# SYNOPSIS

**minikube** _command_ [_options_]

# PARAMETERS

**start**
> 创建并启动本地 Kubernetes 集群。

**stop**
> 停止集群，同时保留其状态。

**delete**
> 删除集群，释放所有 VM 和磁盘资源。

**status**
> 显示主机、kubelet、apiserver 和 kubeconfig 的状态。

**dashboard**
> 启动 Kubernetes Web 仪表板。

**ssh**
> 在底层 VM 或容器上打开 Shell。

**service** _NAME_
> 打印 Kubernetes 服务的 URL，可选择在浏览器中打开。

**addons** _SUBCOMMAND_
> 管理内置插件（ingress、metrics-server、registry 等）。

**tunnel**
> 为 LoadBalancer 服务创建通往集群内部的路由。

**profile** _NAME_
> 在 minikube 管理的多个命名集群之间切换。

**--driver** _NAME_
> 选择虚拟机监控程序或运行时：docker、podman、kvm2、hyperkit、virtualbox、qemu、vfkit、parallels、hyperv、none。

**--cpus** _N_
> 分配给节点的 CPU 数量。

**--memory** _MB_
> 内存大小，单位 MB（或带后缀如 4g）。

**--disk-size** _SIZE_
> 节点的磁盘大小，例如 **20g**。

**--container-runtime** _RUNTIME_
> containerd（自 v1.24 起为默认）、cri-o 或 docker。

**--kubernetes-version** _VERSION_
> 要部署的 Kubernetes 版本，例如 **v1.30.0**。

**--addons** _LIST_
> 启动时启用的插件列表，逗号分隔。

**--help**
> 显示帮助信息。

# DESCRIPTION

**minikube** 提供并运行适合开发、学习和 CI 的本地单节点（或小型多节点）Kubernetes 集群。它抽象了底层计算平台：根据 **--driver** 参数，它可以启动一台承载 Kubernetes 组件的 VM（kvm2、virtualbox、hyperkit、qemu）或容器（docker、podman），然后将上下文写入 **~/.kube/config**，使 **kubectl** 可以透明地指向该集群。

Minikube 附带可选插件（ingress、metrics-server、registry、storage-provisioner），可用 **minikube addons enable** 启用。**service** 和 **tunnel** 命令将集群网络桥接到主机，使集群内运行的应用可以从开发者机器访问。

多个集群可通过 **--profile** 共存，每个集群拥有自己的 VM、插件和 kubeconfig 上下文。

# CAVEATS

默认为单节点；多节点集群（**--nodes=N**）存在但仅用于本地测试。资源消耗大：典型集群至少需要 2 个 CPU 和 2 GiB 内存。**none** 驱动直接在宿主机上运行 Kubernetes，会破坏现有系统配置。在 macOS Apple Silicon 上优先使用 **docker**、**qemu** 或 **vfkit** 驱动；**hyperkit** 仅支持 x86。

# HISTORY

**minikube** 由 Kubernetes 社区创建，旨在提供可靠的笔记本本地开发体验。它从 **kubernetes-incubator** 毕业进入 **kubernetes** 主 GitHub 组织，自 **0.1** 版本（2016 年）起紧跟上游 Kubernetes 发布。

# INSTALL

```pacman: sudo pacman -S minikube```

```zypper: sudo zypper install minikube```

```brew: brew install minikube```

```nix: nix profile install nixpkgs#minikube```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [kind](/man/kind)(1), [k3s](/man/k3s)(1), [k3d](/man/k3d)(1)
