# TAGLINE

管理 Proxmox LXC 容器模板

# TLDR

**更新**容器模板数据库

```pveam update```

列出**可用的**模板

```pveam available```

**下载**模板

```pveam download local [template_name]```

列出**已下载的**模板

```pveam list local```

列出**特定分区**中的模板

```pveam available --section [system|turnkeylinux|mail]```

**移除**模板

```pveam remove local:vztmpl/[template_name]```

# SYNOPSIS

**pveam** _command_ [_options_]

# PARAMETERS

**update**, **u**
> 从 Proxmox 服务器更新模板数据库

**available**, **a**
> 列出可供下载的模板

**download**, **d** _storage_ _template_
> 将模板下载到指定存储

**list**, **l** _storage_
> 列出指定存储中的模板

**remove**, **r** _volume_
> 移除模板

**--section** _section_
> 按分区过滤可用模板（system、turnkeylinux、mail）

# DESCRIPTION

**pveam**（Proxmox VE Appliance Manager）管理 LXC 容器模板。它从 Proxmox 模板仓库下载和管理预构建的容器镜像，包括标准 Linux 发行版和 TurnKey Linux 应用设备。

模板存储在配置好的存储位置，可用于通过 pct create 快速部署新容器。

# CAVEATS

更新数据库和下载模板需要联网。存储必须配置为允许 vztmpl 内容类型。模板从 Proxmox 基础设施下载。

# HISTORY

属于 **Proxmox VE**，提供对精选容器模板的便捷访问。与 TurnKey Linux 集成，提供开箱即用的应用容器。

# SEE ALSO

[pct](/man/pct)(1), [pvesm](/man/pvesm)(1), [pvesh](/man/pvesh)(1)
