# TAGLINE

移除 Proxmox 虚拟机上的锁

# TLDR

**解锁**虚拟机

```qm unlock 100```

# SYNOPSIS

**qm unlock** _vmid_

# DESCRIPTION

**qm unlock** 移除 Proxmox VE 中虚拟机上的锁。锁用于在迁移或备份等关键任务期间阻止某些操作。

当操作失败或被中断时，可用此命令手动清除锁。

# CAVEATS

只有在确定没有操作正在进行时才能解锁虚拟机。在操作进行中解锁可能导致损坏或数据丢失。

# HISTORY

属于 **Proxmox VE** 的 QEMU/KVM 管理工具，用于虚拟机管理。

# INSTALL

```dnf: sudo dnf install qm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qm](/man/qm)(1)
