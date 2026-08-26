# TAGLINE

永久移除 Proxmox 虚拟机

# TLDR

**销毁**指定的虚拟机

```qm destroy 100```

销毁并从已启用的存储中移除所有**未引用的磁盘**

```qm destroy 100 --destroy-unreferenced-disks```

销毁并从备份、复制任务和 HA 配置中**清除**该虚拟机

```qm destroy 100 --purge```

带**清除**地销毁并移除未引用的磁盘

```qm destroy 100 --purge --destroy-unreferenced-disks```

忽略锁**强制**销毁（仅限 root）

```sudo qm destroy 100 --skiplock```

# SYNOPSIS

**qm destroy** _vmid_ [_OPTIONS_]

# PARAMETERS

**--destroy-unreferenced-disks** _boolean_
> 设置后，还会从所有已启用的存储中额外销毁未在配置中引用但 VMID 匹配的所有磁盘。默认：0。

**--purge** _boolean_
> 从备份任务、复制任务和 HA 等配置中移除该 VMID。

**--skiplock** _boolean_
> 忽略锁。仅 root 允许使用此选项。

# DESCRIPTION

**qm destroy** 永久移除 Proxmox VE 中的虚拟机及其所有关联卷。该操作同时会移除所有针对该虚拟机的权限和防火墙规则。

**--purge** 选项将 VMID 从备份任务、复制任务和高可用配置中移除。**--destroy-unreferenced-disks** 选项会移除未在虚拟机配置中引用但 VMID 匹配的磁盘，范围覆盖所有已启用的存储。**--skiplock** 选项绕过安全锁，但需要 root 权限。

# CAVEATS

销毁是永久性的且无法撤销。销毁重要虚拟机前请确保已有备份。VMID 必须在 100-999999999 范围内。

# HISTORY

属于 **Proxmox VE** 的 QEMU/KVM 管理工具，用于虚拟机管理。

# INSTALL

```dnf: sudo dnf install qm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qm](/man/qm)(1), [qm-create](/man/qm-create)(1), [qm-clone](/man/qm-clone)(1), [qm-stop](/man/qm-stop)(1), [qm-shutdown](/man/qm-shutdown)(1)
