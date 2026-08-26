# TAGLINE

引导启动 Kubernetes 集群

# TLDR

**初始化控制平面**

```sudo kubeadm init```

**加入工作节点**

```sudo kubeadm join [control-plane:6443] --token [token] --discovery-token-ca-cert-hash [hash]```

**创建加入令牌**

```kubeadm token create --print-join-command```

**重置节点**

```sudo kubeadm reset```

**升级集群**

```sudo kubeadm upgrade apply [v1.28.0]```

**生成默认配置**

```kubeadm config print init-defaults```

# SYNOPSIS

**kubeadm** _command_ [_options_]

# PARAMETERS

**init**
> 初始化控制平面。

**join** _ENDPOINT_
> 作为节点加入集群。

**reset**
> 将节点重置到初始化前的状态。

**upgrade**
> 升级集群组件。

**token** _CMD_
> 管理加入令牌。

**config** _CMD_
> 管理配置。

**--help**
> 显示帮助信息。

# DESCRIPTION

**kubeadm** 是官方的 Kubernetes 集群引导工具，可自动完成生产级控制平面的搭建。它负责处理复杂的初始化过程，包括为集群组件生成 TLS 证书、配置 kubelet、将 kube-apiserver、kube-controller-manager 和 kube-scheduler 以静态 Pod 的形式部署，以及安装 CoreDNS 和 kube-proxy 等集群必备组件。

其工作流程围绕两个核心命令展开：`kubeadm init` 在首个节点上创建新的控制平面；`kubeadm join` 使用引导令牌将工作节点或额外的控制平面节点加入现有集群。该工具还管理集群生命周期操作，例如在集群范围内升级 Kubernetes 版本、轮换证书以及将节点重置为干净状态。

kubeadm 遵循 Kubernetes 最佳实践和一致性标准，但有意不负责底层基础设施的供给，也不安装 CNI 网络插件，从而专注于集群引导，同时保持与其他工具的可组合性，以便完成完整的集群管理。

# CAVEATS

需要 root 权限。需要容器运行时。不包含网络插件。

# HISTORY

kubeadm 是为 **Kubernetes** 创建的官方集群引导工具，简化了集群的搭建过程。

# INSTALL

```pacman: sudo pacman -S kubeadm```

```apk: sudo apk add kubeadm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [kops](/man/kops)(1)
