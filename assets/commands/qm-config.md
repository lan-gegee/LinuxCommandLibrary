# TAGLINE

显示 Proxmox 虚拟机配置

# TLDR

**显示**虚拟机配置

```qm config vm_id```

仅显示**当前**生效的值

```qm config --current true vm_id```

显示**快照**的配置

```qm config --snapshot snapshot_name vm_id```

# SYNOPSIS

**qm config** [_OPTIONS_] _vmid_

# DESCRIPTION

**qm config** 显示 Proxmox VE 中 QEMU/KVM 虚拟机的配置。默认输出包含将在下次启动时应用的待处理配置更改。

# PARAMETERS

**vmid**
> 虚拟机的数字 ID

**--current** _boolean_
> 显示当前生效的配置值而非待处理的值

**--snapshot** _name_
> 显示来自指定快照的配置

# CAVEATS

默认输出包含待处理的更改。使用 **--current** 只查看当前生效的配置。如需比较当前值和待处理值，请改用 **qm pending**。

# HISTORY

**qm config** 是 **Proxmox VE** 虚拟化平台的组成部分，用于管理 QEMU/KVM 虚拟机。

# INSTALL

```dnf: sudo dnf install qm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qm](/man/qm)(1), [qm-set](/man/qm-set)(1), [qm-pending](/man/qm-pending)(1)
