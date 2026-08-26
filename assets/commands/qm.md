# TAGLINE

管理 Proxmox VE 虚拟机

# TLDR

**列出**所有虚拟机

```qm list```

**创建**虚拟机

```qm create 100 --scsi0 local-lvm:4 --net0 e1000 --cdrom local:iso/image.iso```

**显示**虚拟机配置

```qm config 100```

**启动**虚拟机

```qm start 100```

**关机**并**等待**

```qm shutdown 100 && qm wait 100```

**销毁**虚拟机

```qm destroy 100 --purge```

# SYNOPSIS

**qm** _command_ [_OPTIONS_] [_vmid_]

# DESCRIPTION

**qm** 是面向 Proxmox VE 的 QEMU/KVM 虚拟机管理器。它提供完整的命令行界面，用于创建、配置、启动、停止和管理虚拟机。

# PARAMETERS

**list**
> 列出所有虚拟机

**create** _vmid_
> 创建新虚拟机

**config** _vmid_
> 显示虚拟机配置

**set** _vmid_
> 修改虚拟机配置

**start** _vmid_
> 启动虚拟机

**stop** _vmid_
> 停止虚拟机（硬关机）

**shutdown** _vmid_
> 通过 ACPI 正常关机

**destroy** _vmid_
> 移除虚拟机

**snapshot** _vmid_ _name_
> 创建快照

**rollback** _vmid_ _name_
> 回滚到快照

**clone** _vmid_ _newid_
> 克隆虚拟机

**migrate** _vmid_ _target_
> 将虚拟机迁移到其他节点

**--purge**
> 销毁时移除所有相关资源

# CONFIGURATION

**/etc/pve/qemu-server/<vmid>.conf**
> 每台虚拟机的配置文件，包含硬件设置、磁盘定义、网络接口和启动选项。

**/etc/pve/datacenter.cfg**
> 影响默认虚拟机设置和迁移行为的集群级数据中心配置。

# CAVEATS

VM ID 在整个 Proxmox 集群中必须唯一。某些操作需要 root 权限。有些命令要求虚拟机处于特定状态（运行中或已停止）。

# HISTORY

**qm** 属于 **Proxmox VE** 虚拟化平台，该平台将 KVM hypervisor 和 LXC 容器与基于 Web 的管理界面结合在一起。

# INSTALL

```dnf: sudo dnf install qm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qm-start](/man/qm-start)(1), [qm-stop](/man/qm-stop)(1), [qm-config](/man/qm-config)(1), [pct](/man/pct)(1)
