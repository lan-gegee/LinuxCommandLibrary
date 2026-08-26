# TAGLINE

访问虚拟机的 QEMU monitor 控制台

# TLDR

进入虚拟机的 **QEMU Monitor** 界面

```qm monitor 100```

# SYNOPSIS

**qm monitor** _vmid_

# DESCRIPTION

**qm monitor** 进入特定虚拟机的 QEMU Monitor 界面。QEMU Monitor 提供对该虚拟机 hypervisor 的底层访问，用于高级调试和管理。

通过 monitor，你可以查看虚拟机状态、管理设备，并直接执行 QEMU 命令。

# CAVEATS

QEMU Monitor 是一个功能强大的界面。错误的命令可能导致虚拟机崩溃或损坏。请谨慎使用，并具备相应的 QEMU 内部机制知识。

# HISTORY

属于 **Proxmox VE** 的 QEMU/KVM 管理工具。QEMU Monitor 提供对 QEMU 管理接口的直接访问。

# INSTALL

```dnf: sudo dnf install qm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qm](/man/qm)(1), [qm-terminal](/man/qm-terminal)(1)
