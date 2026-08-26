# TAGLINE

将 Proxmox 虚拟机回滚到快照

# TLDR

将虚拟机**回滚**到快照

```qm rollback vm_id snap_name```

# SYNOPSIS

**qm rollback** _vmid_ _snapname_

# DESCRIPTION

**qm rollback** 将 Proxmox VE 中的 QEMU/KVM 虚拟机恢复到之前的快照状态。快照之后所做的所有更改都将被丢弃。

# PARAMETERS

**vmid**
> 虚拟机的数字 ID

**snapname**
> 要回滚到的快照名称

# CAVEATS

回滚前必须停止虚拟机。创建快照之后的所有数据和配置更改都会丢失。此操作无法撤销。

# HISTORY

**qm rollback** 是 **Proxmox VE** 虚拟化平台的组成部分，用于管理 QEMU/KVM 虚拟机快照。

# INSTALL

```dnf: sudo dnf install qm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qm](/man/qm)(1), [qm-snapshot](/man/qm-snapshot)(1), [qm-delsnapshot](/man/qm-delsnapshot)(1)
