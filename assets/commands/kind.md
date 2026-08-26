# TAGLINE

在 Docker 容器中运行 Kubernetes 集群

# TLDR

**创建集群**

```kind create cluster```

**创建指定名称的集群**

```kind create cluster --name [my-cluster]```

**使用配置文件创建**

```kind create cluster --config [kind-config.yaml]```

**列出集群**

```kind get clusters```

**删除集群**

```kind delete cluster --name [my-cluster]```

**向集群加载镜像**

```kind load docker-image [myimage:tag] --name [my-cluster]```

# SYNOPSIS

**kind** _command_ [_options_]

# PARAMETERS

**create cluster**
> 创建新集群。可接受 --name、--config、--image、--kubeconfig、--wait、--retain 等标志。

**delete cluster**
> 按名称删除集群。

**delete clusters**
> 删除所有 kind 集群。

**get clusters**
> 列出当前正在运行的 kind 集群。

**get nodes**
> 列出充当给定集群节点的 Docker 容器。

**get kubeconfig**
> 将集群的 kubeconfig 打印到 stdout。

**export kubeconfig** **--name** _NAME_
> 将集群的凭据合并到当前使用的 kubeconfig 文件中。

**export logs** _DIR_
> 将集群所有节点的日志导出到 _DIR_。

**load docker-image** _IMAGE_
> 将本地 Docker 镜像旁路加载到集群节点。

**load image-archive** _FILE_
> 将镜像归档（docker save 的输出）旁路加载到集群节点。

**build node-image**
> 从 Kubernetes 源码或发行包构建 kind 节点镜像。

**version**
> 打印 kind 版本。

**--name** _NAME_
> 集群名称（默认 **kind**）。

**--config** _FILE_
> kind 配置 YAML 文件的路径。

**--image** _IMAGE_
> 要使用的节点镜像（覆盖默认的 kindest/node 镜像）。

**--kubeconfig** _FILE_
> 将集群 kubeconfig 写入 _FILE_ 而非默认位置。

**--wait** _DURATION_
> 等待控制平面就绪，最长等待 _DURATION_。

**--retain**
> 集群创建失败时保留节点（便于调试）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**kind**（Kubernetes IN Docker）使用 Docker 容器作为节点来创建和管理本地 Kubernetes 集群。每个集群节点都作为独立的 Docker 容器运行，内含 systemd、kubelet 和 containerd，为本地开发和 CI/CD 测试提供了 minikube 等基于虚拟机方案的轻量替代。

该工具支持多节点集群，包括用于测试高可用配置的多个控制平面节点，并接受 YAML 配置文件来自定义节点数量、端口映射、挂载卷和 Kubernetes 特性开关。本地 Docker 镜像可以直接加载到集群中而无需推送到镜像仓库，从而加快内部开发循环。

kind 由 Kubernetes SIG Testing 团队创建，被 Kubernetes 项目自身的 CI 流水线广泛使用。它针对集群的快速创建与销毁进行了优化，非常适合自动化测试工作流，但不用于生产环境。

# CAVEATS

需要 Docker。面向开发场景。不适用于生产环境。

# HISTORY

kind（Kubernetes IN Docker）由 **Kubernetes** SIG Testing 创建，用作测试 Kubernetes 本身的工具。

# INSTALL

```apt: sudo apt install kind```

```dnf: sudo dnf install kind```

```pacman: sudo pacman -S kind```

```apk: sudo apk add kind```

```zypper: sudo zypper install kind```

```brew: brew install kind```

```nix: nix profile install nixpkgs#kind```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [k3d](/man/k3d)(1), [minikube](/man/minikube)(1), [docker](/man/docker)(1)
