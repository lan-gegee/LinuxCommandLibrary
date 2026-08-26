# TAGLINE

在 Proxmox 虚拟机关机后清理其资源

# TLDR

**清理**虚拟机资源

```qm cleanup vmid clean-shutdown guest-requested```

# SYNOPSIS

**qm cleanup** _vmid_ _clean-shutdown_ _guest-requested_

# DESCRIPTION

**qm cleanup** 清理 Proxmox VE 中与 QEMU/KVM 虚拟机关联的资源。它在虚拟机关机、崩溃或被停止之后，负责清理 tap 设备、VGPU 及其他资源。

# PARAMETERS

**vmid**
> 虚拟机的数字 ID

**clean-shutdown**
> 是否为正常关机（0 或 1）

**guest-requested**
> 关机是否由客户机发起（0 或 1）

# CAVEATS

此命令通常由 Proxmox VE 在虚拟机关机事件后自动调用，很少需要手动执行。它是虚拟机生命周期管理系统的一部分。

# HISTORY

**qm cleanup** 是 **Proxmox VE** 虚拟化平台的组成部分，用于管理 QEMU/KVM 虚拟机及其相关资源。

# INSTALL

```dnf: sudo dnf install qm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qm](/man/qm)(1), [qm-start](/man/qm-start)(1), [qm-stop](/man/qm-stop)(1)
