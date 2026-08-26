# TAGLINE

显示 Proxmox 虚拟机的待处理配置更改

# TLDR

**显示虚拟机的待处理配置更改**

```qm pending [vm_id]```

# SYNOPSIS

**qm pending** _vmid_

# DESCRIPTION

**qm pending** 显示虚拟机配置，同时列出当前值和将在下次启动时应用的待处理更改。这有助于在配置生效前进行审查。

# PARAMETERS

**vmid**
> 虚拟机的数字 ID

# CAVEATS

某些配置更改需要重启虚拟机才能生效。pending 命令会显示当前运行状态与下次将应用的值之间的差异。

# HISTORY

**qm pending** 是 **Proxmox VE** 虚拟化平台的组成部分，用于管理 QEMU/KVM 虚拟机。

# INSTALL

```dnf: sudo dnf install qm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qm](/man/qm)(1), [qm-config](/man/qm-config)(1), [qm-set](/man/qm-set)(1), [qm-start](/man/qm-start)(1)
