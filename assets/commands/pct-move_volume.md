# TAGLINE

pct move-volume 的替代形式，用于移动容器卷

# TLDR

将容器卷**移动**到其他存储

```pct move_volume [100] [rootfs] [local-lvm]```

将某个卷**移动**到另一个容器

```pct move_volume [100] [mp0] --target-vmid [200] --target-volume [mp1]```

复制完成后**移动并删除**原卷

```pct move_volume [100] [mp0] [local-zfs] --delete 1```

带 **I/O** 带宽限制地移动

```pct move_volume [100] [rootfs] [local-lvm] --bwlimit [10240]```

# SYNOPSIS

**pct move_volume** _vmid_ _volume_ [_storage_] [_options_]

# PARAMETERS

_vmid_
> 容器 ID（100-999999999）。

_volume_
> 要移动的卷（rootfs、mp0-mp255 或 unused0-unused255）。

_storage_
> 目标存储标识符。

**--bwlimit** _number_
> 覆盖 I/O 带宽限制，单位为 KiB/s（默认：取自数据中心或存储配置）。

**--delete** _boolean_
> 复制成功后删除原始卷。默认保留原卷作为 unused 卷条目（默认：0）。

**--digest** _string_
> 若当前配置文件的 SHA1 摘要不同则阻止更改。

**--target-digest** _string_
> 若目标容器配置文件的 SHA1 摘要不同则阻止更改。

**--target-vmid** _vmid_
> 目标容器 ID（用于将卷移动到另一个容器）。

**--target-volume** _volume_
> 目标卷键（默认与源卷键相同）。

# DESCRIPTION

**pct move_volume** 是 **pct move-volume** 的替代形式，用于在 Proxmox VE 中将容器卷移动到不同的存储后端。提供下划线变体是为了兼容性。它可以在同一容器内的存储之间移动卷，也可以完全移动到另一个容器。

# SEE ALSO

[pct](/man/pct)(1), [pct-move-volume](/man/pct-move-volume)(1), [pvesm](/man/pvesm)(1)
