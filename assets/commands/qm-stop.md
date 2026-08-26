# TAGLINE

强制停止 Proxmox 虚拟机

# TLDR

立即**停止虚拟机**

```qm stop [vm_id]```

带**超时时间停止**（最多等待 N 秒）

```qm stop [vm_id] --timeout [30]```

**跳过锁检查**（仅限 root）

```qm stop [vm_id] --skiplock true```

停止后**保持存储卷处于活动状态**

```qm stop [vm_id] --keepActive true```

**覆盖仍在进行的关机任务**并立即停止

```qm stop [vm_id] --overrule-shutdown true```

# SYNOPSIS

**qm stop** [_OPTIONS_] _vmid_

# DESCRIPTION

**qm stop** 立即停止 Proxmox VE 中运行中的 QEMU/KVM 虚拟机。这相当于直接拔掉电源线的硬关机；如果客户机操作系统未先正常关闭，可能导致数据丢失。

# PARAMETERS

**vmid**
> 虚拟机的数字 ID。

**--timeout** _seconds_
> 等待虚拟机停止指定的秒数。

**--skiplock** _boolean_
> 跳过锁检查（仅 root 可使用此选项）。

**--keepActive** _boolean_
> 停止后不停用存储卷。

**--overrule-shutdown** _boolean_
> 覆盖仍在运行的关机任务，强制立即停止。

# CAVEATS

这是强制性停止，不会干净地关闭客户机操作系统。要通过 ACPI 正常关机请使用 **qm shutdown**。客户机中存在未保存数据时可能丢失数据。

# INSTALL

```dnf: sudo dnf install qm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qm](/man/qm)(1), [qm-start](/man/qm-start)(1), [qm-shutdown](/man/qm-shutdown)(1)
