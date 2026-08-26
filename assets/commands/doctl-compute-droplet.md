# TAGLINE

管理 DigitalOcean Droplet 虚拟机

# TLDR

**列出所有 droplet**

```doctl compute droplet list```

**创建一个 droplet**

```doctl compute droplet create [name] --size [s-1vcpu-1gb] --image [ubuntu-22-04-x64] --region [nyc1]```

**获取 droplet 详情**

```doctl compute droplet get [droplet_id]```

**删除一个 droplet**

```doctl compute droplet delete [droplet_id]```

**通过 SSH 连接到 droplet**

```doctl compute ssh [droplet_name]```

**列出 droplet 的快照**

```doctl compute droplet snapshots [droplet_id]```

**创建带标签和监控的 droplet**

```doctl compute droplet create [name] --size [s-1vcpu-1gb] --image [ubuntu-22-04-x64] --region [nyc1] --tag-name [web] --enable-monitoring```

# SYNOPSIS

**doctl compute droplet** _command_ [_options_]

# PARAMETERS

_COMMAND_
> 操作：list、create、get、delete、ssh 等。

**list**
> 列出所有 droplet。

**create** _NAME_
> 创建新的 droplet。

**--size** _SLUG_
> Droplet 规格标识。

**--image** _IMAGE_
> 操作系统镜像标识或 ID。

**--region** _REGION_
> 数据中心区域。

**--ssh-keys** _IDS_
> SSH 密钥 ID 或指纹。

**--vpc-uuid** _UUID_
> 用于创建 Droplet 的非默认 VPC 的 UUID。

**--enable-backups**
> 启用每日自动备份。

**--enable-monitoring**
> 安装 DigitalOcean 监控代理。

**--tag-name** _TAG_
> 为 Droplet 应用标签。

**--user-data** _DATA_
> 首次启动时运行的 shell 脚本或 cloud-init 数据。

**--wait**
> 等待 Droplet 创建完成后再返回。

**delete** _ID_
> 删除 droplet。

**ssh** _NAME_
> 通过 SSH 连接到 droplet。

**--help**
> 显示帮助信息。

# DESCRIPTION

**doctl compute droplet** 管理 DigitalOcean Droplet（虚拟机），提供云服务器的完整生命周期控制，包括创建、配置、监控和删除。

Droplet 可以按各种配置创建，指定规格、区域、镜像和网络选项。该命令支持重启、断电重启、调整大小和创建快照等操作。

与 SSH 密钥集成可实现安全访问，ssh 子命令支持按名称便捷地直接连接到 droplet。

# CAVEATS

Droplet 创建后立即产生费用。删除操作不可逆。某些操作需要先关闭 droplet 电源。不同规格和镜像在各个区域的可用性有所差异。

# HISTORY

doctl compute droplet 是 **doctl** CLI 的核心组件，自该工具最初发布起就提供对 DigitalOcean 主要计算服务的命令行管理。

# SEE ALSO

[doctl](/man/doctl)(1), [ssh](/man/ssh)(1)
