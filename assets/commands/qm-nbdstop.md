# TAGLINE

停止 Proxmox 虚拟机的内嵌 NBD 服务器

# TLDR

**停止 VM 100 的内嵌 NBD 服务器**

```qm nbdstop [100]```

# SYNOPSIS

**qm nbdstop** _vmid_

# PARAMETERS

**_vmid_**
> 虚拟机的唯一 ID（整数，100 到 999999999）。

# DESCRIPTION

**qm nbdstop** 停止虚拟机的内嵌 NBD（Network Block Device）服务器。NBD 服务器在备份和动态迁移等磁盘操作期间于内部使用，用于通过网络导出虚拟机磁盘镜像。

此命令会终止指定虚拟机的所有活动 NBD 导出。

# CAVEATS

在数据传输进行中停止 NBD 服务器可能导致数据损坏或备份不完整。停止前请确保没有操作正在使用 NBD 连接。需要 Proxmox VE 宿主机上的 root 权限。

# HISTORY

属于 **Proxmox VE** 的 QEMU/KVM 管理工具，用于虚拟机管理。NBD 停止命令的加入是为了支持高级存储管理和动态迁移工作流。

# INSTALL

```dnf: sudo dnf install qm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qm](/man/qm)(1), [qm-migrate](/man/qm-migrate)(1), [qm-start](/man/qm-start)(1), [qm-stop](/man/qm-stop)(1), [qm-monitor](/man/qm-monitor)(1)
