# TAGLINE

列出 Proxmox 虚拟机的快照

# TLDR

**列出 VMID 为 100 的虚拟机的所有快照**

```qm listsnapshot [100]```

# SYNOPSIS

**qm listsnapshot** _vmid_

# PARAMETERS

_vmid_
> 虚拟机的数字 ID（100 或更大）。

# DESCRIPTION

**qm listsnapshot** 列出 Proxmox VE 中特定虚拟机的所有快照。它以树形结构显示快照名称、创建时间和描述，展示快照之间的父子关系。

输出中会用箭头标记指示当前快照。这有助于识别可用的还原点，并在执行回滚或删除之前管理快照存储。

# INSTALL

```dnf: sudo dnf install qm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qm](/man/qm)(1), [qm-snapshot](/man/qm-snapshot)(1), [qm-delsnapshot](/man/qm-delsnapshot)(1), [qm-rollback](/man/qm-rollback)(1), [qm-clone](/man/qm-clone)(1)
