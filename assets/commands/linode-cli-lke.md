# TAGLINE

管理 Linode Kubernetes Engine 集群

# TLDR

**列出集群**

```linode-cli lke clusters-list```

**创建集群**

```linode-cli lke cluster-create --label [my-cluster] --region [us-east] --k8s_version [1.28]```

**查看集群**

```linode-cli lke cluster-view [cluster_id]```

**获取 kubeconfig**

```linode-cli lke kubeconfig-view [cluster_id] --text```

**列出节点池**

```linode-cli lke pools-list [cluster_id]```

**删除集群**

```linode-cli lke cluster-delete [cluster_id]```

**向集群添加节点池**

```linode-cli lke pool-create [cluster_id] --type [g6-standard-2] --count [3]```

**轮换集群中的所有节点**

```linode-cli lke cluster-nodes-recycle [cluster_id]```

# SYNOPSIS

**linode-cli lke** _subcommand_ [_options_]

# PARAMETERS

_SUBCOMMAND_
> LKE 操作。

**clusters-list**
> 列出所有集群。

**cluster-create**
> 创建新集群。

**cluster-view** _ID_
> 查看集群详情。

**kubeconfig-view** _ID_
> 获取 kubeconfig。

**pools-list** _ID_
> 列出节点池。

**cluster-delete** _ID_
> 删除集群。

**pool-create** _ID_
> 向集群添加节点池。

**cluster-nodes-recycle** _ID_
> 轮换集群中的所有节点。

**--label** _NAME_
> 集群名称。

**--region** _REGION_
> 数据中心所在区域。

**--k8s_version** _VERSION_
> 集群的 Kubernetes 版本。

**--type** _TYPE_
> 节点池节点使用的 Linode 实例类型。

**--count** _N_
> 节点池中的节点数量。

**--text**
> 以纯文本格式输出。

**--json**
> 以 JSON 格式输出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**linode-cli lke** 管理 Linode Kubernetes Engine 集群。LKE 提供托管的 Kubernetes 服务。

该工具可创建集群、管理节点池，并检索 kubeconfig 供 kubectl 访问使用。

# CAVEATS

需要身份验证。节点池会产生费用。支持的 Kubernetes 版本各不相同。

# HISTORY

linode-cli lke 是 **Linode CLI** 的一部分，用于管理 Linode Kubernetes Engine（LKE）集群。

# INSTALL

```brew: brew install linode-cli```

```nix: nix profile install nixpkgs#linode-cli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[linode-cli](/man/linode-cli)(1), [kubectl](/man/kubectl)(1), [helm](/man/helm)(1), [linode-cli-linodes](/man/linode-cli-linodes)(1), [linode-cli-volumes](/man/linode-cli-volumes)(1)
