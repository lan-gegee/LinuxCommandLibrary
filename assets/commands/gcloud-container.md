# TAGLINE

Google Kubernetes Engine 集群管理

# TLDR

**创建 GKE 集群**

```gcloud container clusters create [name] --zone=[zone]```

**列出集群**

```gcloud container clusters list```

**获取凭据**

```gcloud container clusters get-credentials [name] --zone=[zone]```

**删除集群**

```gcloud container clusters delete [name] --zone=[zone]```

**调整节点池大小**

```gcloud container clusters resize [name] --node-pool=[pool] --num-nodes=[3]```

# SYNOPSIS

**gcloud container** _resource_ _command_ [_options_]

# PARAMETERS

_RESOURCE_
> 资源类型：clusters、node-pools、images。

**clusters** _CMD_
> GKE 集群管理。

**node-pools** _CMD_
> 节点池操作。

**images** _CMD_
> 容器镜像操作。

**get-credentials** _CLUSTER_
> 为集群配置 kubectl。

**--zone** _ZONE_
> 集群所在区域。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gcloud container** 为 Google Kubernetes Engine（GKE）——Google 托管的 Kubernetes 服务——提供全面的管理能力。它处理 Kubernetes 集群的完整生命周期，无需手动搭建主节点或控制平面组件。

clusters 子命令创建并管理 GKE 集群，可自定义节点配置、网络设置和 Kubernetes 版本。节点池允许构建异构集群，为不同负载类型使用不同机型或配置。扩缩容操作通过修改节点池大小来调整集群容量。

一个关键特性是 get-credentials，它将集群身份验证信息写入 kubeconfig 文件来配置 kubectl，从而无缝连接标准 Kubernetes CLI 工具与你的 GKE 集群。该命令与 Google Container Registry 集成以支持私有镜像存储，并支持集群自动扩缩、节点自动修复以及 Kubernetes 版本自动升级等高级功能。

# CAVEATS

集群会产生费用。创建需要时间。访问需要先完成 kubectl 配置。

# HISTORY

gcloud container 属于 **Google Cloud SDK**，用于管理 GKE——Google 用于运行容器化应用的托管 Kubernetes 服务。

# SEE ALSO

[gcloud](/man/gcloud)(1), [kubectl](/man/kubectl)(1), [gcloud-compute](/man/gcloud-compute)(1)

# RESOURCES

```[Documentation](https://cloud.google.com/sdk/gcloud/reference/container)```

<!-- verified: 2026-07-15 -->
