# TAGLINE

将 Proxmox 虚拟机迁移到其他节点

# TLDR

将虚拟机**迁移**到另一个节点

```qm migrate 100 target_node```

以**带宽限制**（10 KiB/s）迁移

```qm migrate 100 target_node --bwlimit 10```

带本地设备地**强制**迁移

```qm migrate 100 target_node --force true```

对运行中的虚拟机使用**在线/动态**迁移

```qm migrate 100 target_node --online true```

为本地磁盘启用动态**存储迁移**

```qm migrate 100 target_node --with-local-disks true```

# SYNOPSIS

**qm migrate** _vmid_ _target_ [_options_]

# PARAMETERS

**--bwlimit** _kbps_
> 以 KiB/s 计的带宽限制

**--force** _true|false_
> 允许携带本地设备迁移（仅限 root）

**--online** _true|false_
> 对运行中的虚拟机使用在线/动态迁移

**--with-local-disks** _true|false_
> 为本地磁盘启用动态存储迁移

# DESCRIPTION

**qm migrate** 将虚拟机迁移到 Proxmox VE 集群中的另一个节点。它同时支持离线迁移和针对运行中虚拟机的在线（live）迁移。

在线迁移可以在停机时间极小的情况下在节点间移动虚拟机。存储迁移则让带有本地磁盘的虚拟机也能移动。

# CAVEATS

在线迁移需要共享存储或 --with-local-disks 选项。网络带宽和延迟会影响迁移耗时。force 选项需要 root 权限。

# HISTORY

属于 **Proxmox VE** 的 QEMU/KVM 管理工具。虚拟机迁移是集群维护和负载均衡的关键能力。

# INSTALL

```dnf: sudo dnf install qm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qm](/man/qm)(1), [pvecm](/man/pvecm)(1)
