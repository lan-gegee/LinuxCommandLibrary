# TAGLINE

将 Proxmox 虚拟机转换为模板

# TLDR

从虚拟机创建**模板**

```qm template 100```

# SYNOPSIS

**qm template** _vmid_

# DESCRIPTION

**qm template** 在 Proxmox VE 中将虚拟机转换为模板。模板是只读的基础镜像，可用于快速克隆新的虚拟机。

转换为模板后，该虚拟机无法直接启动，必须通过克隆来创建新的可运行实例。

# CAVEATS

模板转换是永久性的。原虚拟机变为只读，无法恢复为普通虚拟机。转换前请确保虚拟机配置正确。

# HISTORY

属于 **Proxmox VE** 的 QEMU/KVM 管理工具。模板让高效的虚拟机部署流程成为可能。

# INSTALL

```dnf: sudo dnf install qm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qm](/man/qm)(1), [qm-clone](/man/qm-clone)(1)
