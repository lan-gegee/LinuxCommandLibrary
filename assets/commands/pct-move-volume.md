# TAGLINE

将容器的存储卷移动到其他 Proxmox 存储位置

# TLDR

将 rootfs **移动**到其他存储

```pct move-volume 100 rootfs storage_id```

移动并**删除**旧卷

```pct move-volume 100 rootfs storage_id --delete```

# SYNOPSIS

**pct move-volume** _vmid_ _volume_ _storage_ [_OPTIONS_]

# DESCRIPTION

**pct move-volume** 将容器的存储卷移动到其他 Proxmox 存储位置。适用于在不同存储后端之间迁移容器，或释放特定存储上的空间。

# PARAMETERS

**vmid**
> 容器的数字 ID

**volume**
> 要移动的卷（rootfs 或挂载点 mpN）

**storage**
> 目标存储 ID

**--delete**
> 移动成功后删除源卷

**--target-vmid** _id_
> 将卷移动到另一个容器

# CAVEATS

为确保卷的安全移动，应先停止容器。不使用 **--delete** 时旧卷会保留，必须手动移除。移动到不同类型的存储可能影响性能。

# HISTORY

**pct move-volume** 是用于管理 LXC 容器的 **Proxmox VE** 虚拟化平台的一部分。

# SEE ALSO

[pct](/man/pct)(1), [pct-resize](/man/pct-resize)(1)
