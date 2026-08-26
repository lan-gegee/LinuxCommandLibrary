# TAGLINE

重启 Proxmox 虚拟机

# TLDR

**重启虚拟机**

```qm reboot [vmid]```

**以正常关机的超时时间重启**

```qm reboot [vmid] --timeout [seconds]```

# SYNOPSIS

**qm reboot** _vmid_ [_options_]

# PARAMETERS

**--timeout** _seconds_
> 在强制重启之前最多等待 _seconds_ 秒让客户机正常关机。整数，0 或更大。

# DESCRIPTION

**qm reboot** 先正常关闭虚拟机，然后再次启动，从而完成重启。在此过程中，所有待处理的配置更改都会被应用。

_vmid_ 是虚拟机的唯一整数标识符（100–999999999）。正常关机依赖客户机操作系统的 ACPI 支持。如果客户机在超时时间内没有响应，虚拟机将被强制停止并重启。

# CAVEATS

要实现正常关机，客户机操作系统必须支持 ACPI。没有 ACPI 时，关机信号可能被忽略。如需不依赖 ACPI 的硬重置，请使用 `qm reset`。

# HISTORY

属于 **Proxmox VE** 的 QEMU/KVM 管理工具集，用于在 Proxmox hypervisor 平台上管理虚拟机。

# INSTALL

```dnf: sudo dnf install qm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qm](/man/qm)(1), [qm-reset](/man/qm-reset)(1), [qm-shutdown](/man/qm-shutdown)(1), [qm-start](/man/qm-start)(1), [qm-stop](/man/qm-stop)(1)
