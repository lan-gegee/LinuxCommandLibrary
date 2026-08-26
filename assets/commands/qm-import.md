# TAGLINE

将外部虚拟机镜像导入 Proxmox VE

# TLDR

将磁盘镜像**导入**到新建或已有虚拟机的存储布局中

```qm import [100] [storage_name]:import/[file_name] --storage [destination_storage]```

# SYNOPSIS

**qm import** _vmid_ _source_ [_OPTIONS_]

# PARAMETERS

**vmid**
> 目标虚拟机 ID

**source**
> 源卷或路径（通常位于某个存储的 `import` 内容位置下）

**--storage** _storage_
> 导入磁盘的目标存储

# DESCRIPTION

**qm import** 将受支持的虚拟机镜像（来自 VMware、VirtualBox 等类似 hypervisor）导入 Proxmox VE。源镜像通常先放置在允许 `import` 内容类型的存储上，然后以 `storage:import/filename` 的形式引用。

该命令会在目标存储上创建或挂接磁盘镜像，并使虚拟机准备好在 `qm` 下进行配置。确切支持的格式和工作流程请参考与你 VE 版本对应的 Proxmox 导入文档。

# CAVEATS

导入的客户机通常需要调整驱动或启动方式（VirtIO 与旧式硬件的区别）。大镜像要求目标存储有足够的可用空间。导出前最好先停止源虚拟机，以获得一致的镜像。

# HISTORY

属于 **Proxmox VE** 的 QEMU/KVM 管理工具（`qm`）的一部分。

# INSTALL

```dnf: sudo dnf install qm```

<!-- packages: 2026-07-28 -->

# SEE ALSO

[qm](/man/qm)(1), [qm-importovf](/man/qm-importovf)(1), [qm-importdisk](/man/qm-importdisk)(1)

# RESOURCES

```[Homepage](https://www.proxmox.com)```

```[Documentation](https://pve.proxmox.com/pve-docs/qm.1.html)```

<!-- verified: 2026-07-28 -->
