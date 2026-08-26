# TAGLINE

创建 Proxmox 虚拟机的快照

# TLDR

**创建**快照

```qm snapshot vm_id snapshot_name```

带**描述**创建快照

```qm snapshot vm_id snapshot_name --description "description"```

包含 **vmstate**

```qm snapshot vm_id snapshot_name --vmstate 1```

**列出**快照

```qm listsnapshot 100```

**回滚**到快照

```qm rollback vm_id snap_name```

# SYNOPSIS

**qm snapshot** [_OPTIONS_] _vmid_ _snapname_

# DESCRIPTION

**qm snapshot** 在 Proxmox VE 中为 QEMU/KVM 虚拟机创建时间点快照。快照记录磁盘状态，也可选择记录虚拟机内存状态，以便日后回滚到该时间点。

# PARAMETERS

**vmid**
> 虚拟机的数字 ID

**snapname**
> 快照名称（必须以字母开头）

**--description** _text_
> 快照的描述文本

**--vmstate** _boolean_
> 将虚拟机内存状态包含在快照中

# CAVEATS

快照名称必须以字母开头。包含 vmstate 可以恢复运行状态，但需要更多存储空间。快照采用写时复制机制，因此随着更改累积，磁盘空间占用会不断增长。

# HISTORY

**qm snapshot** 是 **Proxmox VE** 虚拟化平台的组成部分，用于管理 QEMU/KVM 虚拟机快照。

# INSTALL

```dnf: sudo dnf install qm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qm](/man/qm)(1), [qm-rollback](/man/qm-rollback)(1), [qm-delsnapshot](/man/qm-delsnapshot)(1)
