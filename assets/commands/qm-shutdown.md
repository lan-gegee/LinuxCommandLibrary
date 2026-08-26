# TAGLINE

正常关闭 Proxmox 虚拟机

# TLDR

**关闭**虚拟机

```qm shutdown vm_id```

带**超时**关闭

```qm shutdown --timeout 10 vm_id```

**保持**存储处于活动状态

```qm shutdown --keepActive true vm_id```

**跳过**锁检查

```qm shutdown --skiplock true vm_id```

关机后**强制**停止

```qm shutdown --forceStop true vm_id```

# SYNOPSIS

**qm shutdown** [_OPTIONS_] _vmid_

# DESCRIPTION

**qm shutdown** 向 Proxmox VE 中的 QEMU/KVM 虚拟机发送 ACPI 关机信号以正常关机。客户机操作系统必须响应 ACPI 事件，此操作才能正常进行。

# PARAMETERS

**vmid**
> 虚拟机的数字 ID

**--timeout** _seconds_
> 等待虚拟机关机的最长时间

**--keepActive** _boolean_
> 关机后不停用存储卷

**--skiplock** _boolean_
> 跳过锁检查（仅限 root）

**--forceStop** _boolean_
> 若虚拟机不响应关机信号则强制停止

# CAVEATS

客户机操作系统必须启用 ACPI 支持并能响应关机事件。如果客户机忽略 ACPI 信号，请改用 **--forceStop** 或 **qm stop**。Windows 客户机可能需要正确的 ACPI 驱动。

# HISTORY

**qm shutdown** 是 **Proxmox VE** 虚拟化平台的组成部分，用于管理 QEMU/KVM 虚拟机。

# INSTALL

```dnf: sudo dnf install qm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qm](/man/qm)(1), [qm-start](/man/qm-start)(1), [qm-stop](/man/qm-stop)(1)
