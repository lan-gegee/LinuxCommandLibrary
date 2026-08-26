# TAGLINE

Google Compute Engine 资源管理

# TLDR

**列出虚拟机实例**

```gcloud compute instances list```

**创建实例**

```gcloud compute instances create [name] --zone=[zone]```

**SSH 连接到实例**

```gcloud compute ssh [instance] --zone=[zone]```

**停止实例**

```gcloud compute instances stop [name] --zone=[zone]```

**列出磁盘**

```gcloud compute disks list```

# SYNOPSIS

**gcloud compute** _resource_ _command_ [_options_]

# SUBCOMMANDS

**instances** _CMD_
> 虚拟机实例生命周期（create、list、start、stop、delete、describe）。

**disks** _CMD_
> 持久磁盘操作。

**images** _CMD_
> 管理自定义和公共虚拟机镜像。

**snapshots** _CMD_
> 创建和管理磁盘快照。

**networks** _CMD_
> VPC 网络、子网和对等连接。

**firewall-rules** _CMD_
> 管理 VPC 防火墙规则。

**ssh** _INSTANCE_
> SSH 进入实例（自动管理密钥）。

**scp** _SRC_ _DEST_
> 通过 SSH 在实例与本地之间复制文件。

# PARAMETERS

**--zone** _ZONE_
> 资源所在的计算区域（如 us-central1-a）。

**--region** _REGION_
> 区域性资源所在的计算大区。

**--project** _PROJECT_
> 要操作的 Google Cloud 项目 ID。

**--format** _FORMAT_
> 输出格式（json、yaml、table、value）。

**--filter** _EXPR_
> 按表达式过滤结果。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gcloud compute** 是 Google Compute Engine 的命令行界面，Compute Engine 是 Google 的基础设施即服务产品。它提供对虚拟机、持久磁盘、网络、负载均衡器及其他基础设施要素的完整控制。

instances 子命令处理虚拟机生命周期操作，包括使用自定义机型创建实例、启动和停止实例以及删除。VPC、子网、防火墙规则和路由等网络资源通过各自对应的子命令管理。

一些便利特性包括：内置的 gcloud compute ssh 可自动管理 SSH 密钥和连接细节；gcloud compute scp 支持安全的文件传输。该命令组还支持自定义镜像、快照、实例组以及用于自动扩缩的代管实例组等高级功能。所有操作都遵循区域和大区概念，必须逐命令指定或通过配置默认值指定。

# CAVEATS

资源会产生费用。区域选择影响可用性。某些操作耗时较长。

# HISTORY

gcloud compute 属于 **Google Cloud SDK**，用于管理 Compute Engine——Google 用于运行虚拟机的基础设施即服务产品。

# SEE ALSO

[gcloud](/man/gcloud)(1), [gcloud-container](/man/gcloud-container)(1)
