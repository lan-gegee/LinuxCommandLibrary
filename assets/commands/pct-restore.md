# TAGLINE

从 Proxmox 备份文件恢复 LXC 容器

# TLDR

**从备份恢复容器**

```pct restore [VMID] [/path/to/backup.tar.zst]```

**恢复到指定存储**

```pct restore [VMID] [backup.tar.zst] --storage [local-lvm]```

**恢复后不启动**

```pct restore [VMID] [backup.tar.zst] --start 0```

**使用新主机名恢复**

```pct restore [VMID] [backup.tar.zst] --hostname [newname]```

**恢复为非特权容器**

```pct restore [VMID] [backup.tar.zst] --unprivileged 1```

# SYNOPSIS

**pct restore** _vmid_ _backup_ [_options_]

# PARAMETERS

**vmid**
> 新容器 ID。

**backup**
> 备份文件路径。

**--storage** _name_
> 目标存储。

**--hostname** _name_
> 设置主机名。

**--start** _bool_
> 恢复后启动。

**--unprivileged** _bool_
> 非特权容器。

**--rootfs** _spec_
> 根文件系统规格（例如 local-lvm:20 表示 20GB）。

**--memory** _MB_
> 设置容器内存限制。

**--pool** _name_
> 将容器添加到指定的资源池。

**--force** _bool_
> 允许覆盖现有容器。

**--ignore-unpack-errors** _bool_
> 忽略备份解包期间的错误。

# DESCRIPTION

**pct restore** 从 Proxmox 备份文件恢复 LXC 容器。它可以恢复为新的 VMID、不同的存储，或修改过的设置。

# EXAMPLE

```bash
# Restore to container 200
pct restore 200 /var/lib/vz/dump/vzdump-lxc-100.tar.zst

# Restore with 20GB disk
pct restore 200 backup.tar.zst --rootfs local-lvm:20
```

# CAVEATS

VMID 不能已存在。存储必须有可用空间。网络配置可能需要调整。

# HISTORY

pct restore 是 **Proxmox VE** 备份与恢复基础设施的一部分，配合 vzdump 备份工作。

# SEE ALSO

[pct](/man/pct)(1), [pct-enter](/man/pct-enter)(1), [vzdump](/man/vzdump)(1), [qmrestore](/man/qmrestore)(1)
