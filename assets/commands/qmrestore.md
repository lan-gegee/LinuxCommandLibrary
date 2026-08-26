# TAGLINE

从备份归档恢复 Proxmox 虚拟机

# TLDR

从原始存储上的备份**恢复**虚拟机

```qmrestore path/to/vzdump-qemu-100.vma.lzo 100```

**强制**覆盖已有虚拟机

```qmrestore path/to/vzdump-qemu-100.vma.lzo 100 --force true```

恢复到**指定存储**

```qmrestore path/to/vzdump-qemu-100.vma.lzo 100 --storage local```

从 Proxmox Backup Server **动态恢复**

```qmrestore path/to/vzdump-qemu-100.vma.lzo 100 --live-restore true```

# SYNOPSIS

**qmrestore** _archive_ _vmid_ [_options_]

# PARAMETERS

**--force** _true|false_
> 覆盖具有相同 ID 的已有虚拟机

**--storage** _name_
> 恢复磁盘的目标存储

**--live-restore** _true|false_
> 在后台恢复的同时立即启动虚拟机（仅限 PBS）

# DESCRIPTION

**qmrestore** 从 vzdump 备份归档恢复 QEMU 虚拟机。它可以恢复到原始存储，也可以恢复到不同的目标存储。

动态恢复功能允许在后台继续恢复的同时立即启动虚拟机，该功能仅在 Proxmox Backup Server 上可用。

# CAVEATS

除非使用 --force，否则 VM ID 必须可用。动态恢复仅适用于 Proxmox Backup Server 备份。

# HISTORY

属于 **Proxmox VE** 备份与恢复基础设施。兼容 vzdump 备份文件和 Proxmox Backup Server。

# SEE ALSO

[qm](/man/qm)(1), [vzdump](/man/vzdump)(1), [pct-restore](/man/pct-restore)(1)
