# TAGLINE

删除 Proxmox 虚拟机快照

# TLDR

**删除**快照

```qm delsnapshot 100 snapshot_name```

**强制**从配置中删除（即使磁盘删除失败）

```qm delsnapshot 100 snapshot_name --force 1```

# SYNOPSIS

**qm delsnapshot** _vmid_ _snapname_ [_options_]

# PARAMETERS

**--force** _boolean_
> 即使删除磁盘快照失败也强制从配置文件中移除

# DESCRIPTION

**qm delsnapshot** 删除 Proxmox VE 中的虚拟机快照。快照记录了虚拟机在某一时间点的状态，不再需要时可以将其删除以回收存储空间。

force 选项允许在底层磁盘快照无法删除的情况下，仍从配置中移除快照引用。

# CAVEATS

删除快照不可逆。删除前请确认不再需要该快照。强制删除可能留下孤立的磁盘数据。

# HISTORY

属于 **Proxmox VE** 的 QEMU/KVM 管理工具，用于虚拟机管理。

# INSTALL

```dnf: sudo dnf install qm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qm](/man/qm)(1), [qm-snapshot](/man/qm-snapshot)(1), [qm-listsnapshot](/man/qm-listsnapshot)(1), [qm-rollback](/man/qm-rollback)(1)
