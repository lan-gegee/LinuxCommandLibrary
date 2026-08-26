# TAGLINE

管理 IBM Cloud Kubernetes Service

# TLDR

**列出集群**

```ibmcloud ks clusters```

**创建集群**

```ibmcloud ks cluster create classic --name [my-cluster]```

**获取集群配置**

```ibmcloud ks cluster config --cluster [cluster-name]```

**列出工作节点**

```ibmcloud ks workers --cluster [cluster-name]```

**显示集群信息**

```ibmcloud ks cluster get --cluster [cluster-name]```

# SYNOPSIS

**ibmcloud ks** _command_ [_options_]

# PARAMETERS

_COMMAND_
> Kubernetes Service 命令。

**clusters**
> 列出集群。

**cluster create**
> 创建集群。

**cluster config**
> 获取 kubeconfig。

**workers**
> 列出工作节点。

**cluster get**
> 显示集群信息。

**--help**
> 显示帮助信息。

# DESCRIPTION

**ibmcloud ks** 管理 IBM Cloud Kubernetes Service。它在 IBM Cloud 基础设施上创建和管理 Kubernetes 集群。

该工具处理集群生命周期、工作节点池和配置。它与 kubectl 集成以访问集群。

# CAVEATS

需要安装 IKS 插件。集群会产生费用。提供区域化部署选项。

# HISTORY

ibmcloud ks 是 **IBM Cloud** CLI 的 Kubernetes Service 插件。

# SEE ALSO

[ibmcloud](/man/ibmcloud)(1), [kubectl](/man/kubectl)(1), [ibmcloud-cr](/man/ibmcloud-cr)(1)
