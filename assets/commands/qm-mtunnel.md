# TAGLINE

Proxmox 虚拟机的内部迁移隧道

# TLDR

**qmigrate** 在数据迁移期间使用的命令

```qm mtunnel```

# SYNOPSIS

**qm mtunnel**

# DESCRIPTION

**qm mtunnel** 由 qmigrate 在内部使用，用于主机间的数据迁移。它创建一条隧道，在动态迁移期间传输虚拟机数据。

此命令不应手动调用；它由迁移进程自动调用。

# CAVEATS

仅供内部使用。手动调用可能干扰正在进行的迁移或导致意外行为。

# HISTORY

属于 **Proxmox VE** 的 QEMU/KVM 管理工具。为虚拟机迁移提供数据传输机制。

# SEE ALSO

[qm](/man/qm)(1), [qm-migrate](/man/qm-migrate)(1)
