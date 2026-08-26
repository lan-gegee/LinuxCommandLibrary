# TAGLINE

将磁盘与 Proxmox 虚拟机解除关联

# TLDR

**将磁盘与虚拟机解除关联**

```qm unlink [vmid] --idlist [unused0]```

**解除关联并强制从配置中移除磁盘**

```qm unlink [vmid] --idlist [scsi0] --force```

**一次解除多个磁盘的关联**

```qm unlink [vmid] --idlist [scsi0;scsi1]```

# SYNOPSIS

**qm unlink** _vmid_ **--idlist** _string_ [**--force** _boolean_]

# PARAMETERS

_vmid_
> 虚拟机的唯一数字 ID（100-999999999）。

**--idlist** _string_
> 要解除关联的磁盘 ID 的分号分隔列表（如 `unused0`、`scsi0`、`virtio1`）。

**--force** _boolean_
> 强制移除。允许移除仍在虚拟机配置中被引用但未标记为未使用的磁盘。默认：`0`。

# DESCRIPTION

**qm unlink** 是 **qm disk unlink** 的别名，用于将磁盘从虚拟机配置中移除，但不删除底层存储卷。该磁盘变为未使用状态，但仍保留在存储中，可以重新挂接回同一台或其他虚拟机。

它适合在跨虚拟机移动磁盘之前安全地分离磁盘，或在清理虚拟机配置时避免丢失数据。

# INSTALL

```dnf: sudo dnf install qm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qm](/man/qm)(1), [qm-disk](/man/qm-disk)(1)
