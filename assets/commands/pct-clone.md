# TAGLINE

创建现有 Proxmox LXC 容器的副本

# TLDR

**克隆**容器（默认为链接克隆）

```pct clone [template_id] [new_id]```

以自定义**主机名**克隆

```pct clone [template_id] [new_id] --hostname [name]```

创建**完整（独立）副本**

```pct clone [template_id] [new_id] --full```

克隆到**指定存储**

```pct clone [template_id] [new_id] --full --storage [storage_name]```

克隆时附加**说明性备注**

```pct clone [template_id] [new_id] --description "[note]"```

# SYNOPSIS

**pct clone** _vmid_ _newid_ [_OPTIONS_]

# DESCRIPTION

**pct clone** 创建现有 Proxmox LXC 容器的副本。适用于从配置好的模板容器创建多个容器，或用于备份目的。

# PARAMETERS

**vmid**
> 源容器的数字 ID

**newid**
> 克隆出的容器的数字 ID

**--hostname** _name_
> 为克隆设置自定义主机名

**--full**
> 创建完整副本而不是链接克隆

**--target** _node_
> 克隆的目标节点

**--storage** _storage_
> 克隆磁盘所用的存储

# CAVEATS

为保证克隆的一致性，应先停止源容器。链接克隆与原始容器共享基础存储。完整克隆相互独立，但需要更多磁盘空间。

# HISTORY

**pct clone** 是 **Proxmox VE** 虚拟化平台中管理 LXC 容器的一部分。

# SEE ALSO

[pct](/man/pct)(1), [pct-create](/man/pct-create)(1)
