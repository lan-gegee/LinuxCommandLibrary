# TAGLINE

恢复已挂起的 Proxmox 虚拟机

# TLDR

**恢复**已挂起的虚拟机

```qm resume 100```

恢复时**忽略锁**（仅限 root）

```sudo qm resume 100 --skiplock true```

# SYNOPSIS

**qm resume** _vmid_ [_options_]

# PARAMETERS

_vmid_
> 虚拟机的数字 ID（100 - 999999999）。

**--nocheck** _boolean_
> 恢复时跳过所有状态检查（默认：0）。

**--skiplock** _boolean_
> 忽略锁并强制恢复。仅 root 允许使用此选项。

# DESCRIPTION

**qm resume** 恢复已挂起（暂停）的虚拟机，使其回到运行状态。虚拟机会从暂停的位置精确地继续执行。

此命令用于 **qm suspend** 暂停虚拟机之后。对已经在运行或已停止的虚拟机没有效果。

# CAVEATS

要求虚拟机处于挂起（暂停）状态。**--skiplock** 选项需要 root 权限。VM ID 必须是 Proxmox 范围内（100 及以上）的有效整数。

# HISTORY

属于 **Proxmox VE** 的 QEMU/KVM 管理工具，用于虚拟机管理。

# INSTALL

```dnf: sudo dnf install qm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qm](/man/qm)(1), [qm-suspend](/man/qm-suspend)(1), [qm-start](/man/qm-start)(1), [qm-stop](/man/qm-stop)(1), [qm-shutdown](/man/qm-shutdown)(1)
