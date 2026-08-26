# TAGLINE

管理 Proxmox 虚拟机的磁盘镜像

# TLDR

为虚拟磁盘增加 **10 GB** 容量

```qm disk resize [100] scsi0 +10G```

将虚拟磁盘**移动**到其他存储

```qm disk move [100] scsi0 [local-lvm]```

移动并**删除**原始副本

```qm disk move [100] scsi0 [local-lvm] --delete```

**导入**指定格式的磁盘镜像

```qm disk import [100] [/path/to/disk.vmdk] [local-lvm] --format qcow2```

**重新扫描**所有存储并更新磁盘大小

```qm disk rescan```

执行**试运行**扫描

```qm disk rescan --dryrun```

针对**特定虚拟机**重新扫描

```qm disk rescan --vmid [100]```

# SYNOPSIS

**qm disk** _command_ [_options_]

# PARAMETERS

**resize** _vmid_ _disk_ _size_
> 调整磁盘大小（用 +nG 表示增加空间）。不支持缩小。

**move** _vmid_ _disk_ _storage_
> 将磁盘移动到其他存储或其他虚拟机。

**import** _vmid_ _source_ _storage_
> 将外部磁盘镜像导入为未使用的磁盘。

**rescan** [_options_]
> 重新扫描存储以发现磁盘变化。

**--format** _format_
> 目标磁盘镜像格式（qcow2、raw、vmdk）。

**--delete**
> 移动后删除源磁盘。

**--dryrun**
> 仅预览更改而不实际应用。

**--vmid** _id_
> 只对指定虚拟机进行重新扫描。

**--disk** _disk_id_
> 导入时分配特定的磁盘 ID（如 scsi0、sata1）。

# DESCRIPTION

**qm disk** 管理 Proxmox VE 虚拟机的磁盘镜像，涵盖调整大小、在存储后端之间移动、导入外部磁盘镜像以及重新扫描存储变化等操作。

它是存储管理和迁移任务的必备工具。

# CAVEATS

resize 操作不能缩小磁盘。导入和移动大容量磁盘可能耗时较长。请确保目标存储有足够的空间。

# HISTORY

属于 **Proxmox VE** 的 QEMU/KVM 管理工具，用于虚拟机管理。

# INSTALL

```dnf: sudo dnf install qm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qm](/man/qm)(1), [qm-create](/man/qm-create)(1), [pvesm](/man/pvesm)(1)
