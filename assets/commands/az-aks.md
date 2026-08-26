# TAGLINE

管理 Azure Kubernetes Service 集群

# TLDR

**创建 Kubernetes 集群**

```az aks create -g [resource-group] -n [cluster-name] --generate-ssh-keys```

**获取 kubectl 凭证**

```az aks get-credentials -g [resource-group] -n [cluster-name]```

**列出资源组中的所有集群**

```az aks list -g [resource-group] -o table```

**显示集群详情**

```az aks show -g [resource-group] -n [cluster-name]```

**缩放节点池**

```az aks nodepool scale -g [resource-group] --cluster-name [cluster-name] --name [nodepool1] --node-count [5]```

**将集群升级到更新的 Kubernetes 版本**

```az aks upgrade -g [resource-group] -n [cluster-name] --kubernetes-version [1.28.0]```

**停止运行中的集群以节省成本**

```az aks stop -g [resource-group] -n [cluster-name]```

**启动已停止的集群**

```az aks start -g [resource-group] -n [cluster-name]```

# SYNOPSIS

**az aks** _subcommand_ [_options_]

# DESCRIPTION

**az aks** 管理 Azure Kubernetes Service（AKS）集群，提供一种托管的 Kubernetes 环境，降低集群部署与管理的复杂度。

AKS 负责健康监视、维护和升级等关键任务。Azure 管理 Kubernetes 控制平面，而你只需管理和为代理节点付费。

# SUBCOMMANDS

**Cluster Management**
> create, delete, show, list, update, start, stop, upgrade, rotate-certs

**Credentials**
> get-credentials, get-versions, get-upgrades, install-cli

**Node Pools**
> nodepool add, nodepool delete, nodepool scale, nodepool upgrade, nodepool list, nodepool show

**Networking**
> check-network, check-acr, approuting enable, approuting disable

**Addons**
> addon enable, addon disable, addon list, addon show, addon update

**Advanced**
> mesh enable, mesh disable, pod-identity add, command invoke

# PARAMETERS

**-g**, **--resource-group** _VALUE_
> 资源组的名称。

**-n**, **--name** _VALUE_
> 托管集群的名称。

**--kubernetes-version** _VALUE_
> 集群使用的 Kubernetes 版本。

**--node-count** _VALUE_
> 默认节点池中的节点数量。

**--node-vm-size** _VALUE_
> 作为 Kubernetes 节点创建的虚拟机大小。

**--generate-ssh-keys**
> 若不存在则生成 SSH 密钥文件。

**--network-plugin** _VALUE_
> Kubernetes 网络插件（azure、kubenet、none）。

**--admin**
> 获取集群管理员凭证而非用户凭证。

**--overwrite-existing**
> 覆盖 kubeconfig 中已有的集群条目。

**-o**, **--output** _FORMAT_
> 输出格式（json、jsonc、table、tsv、yaml、yamlc、none）。

# CAVEATS

停止集群会释放计算资源但保留集群配置；此期间不收取计算费用。升级 Kubernetes 版本是不可逆的单向操作。get-credentials 默认会覆盖已有的 kubeconfig 条目；使用 **--overwrite-existing** 或 **--file** 来控制这一行为。**command invoke** 子命令可在私有集群上运行命令。

# HISTORY

Azure Kubernetes Service（AKS）于 **2018** 年 **6** 月正式发布。它由支持多种编排器的 Azure Container Service（ACS）演变而来。AKS 专注于 Kubernetes，并与 Azure 深度集成。

# INSTALL

```dnf: sudo dnf install azure-cli```

```pacman: sudo pacman -S azure-cli```

```zypper: sudo zypper install azure-cli```

```brew: brew install azure-cli```

```nix: nix profile install nixpkgs#azure-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[az](/man/az)(1), [az-acr](/man/az-acr)(1), [kubectl](/man/kubectl)(1), [helm](/man/helm)(1)
