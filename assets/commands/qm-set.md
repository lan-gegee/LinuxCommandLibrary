# TAGLINE

修改 Proxmox 虚拟机的配置设置

# TLDR

设置虚拟机**名称**

```qm set 100 --name vm_name```

启用**自启动**

```qm set 100 --autostart 1```

设置 **CPU 核心数**

```qm set 100 --cores 4```

设置**内存**（MB）

```qm set 100 --memory 8192```

添加**网络**设备

```qm set 100 --net0 virtio,bridge=vmbr0```

**删除**设备

```qm set 100 --delete device_name```

**GPU 直通**

```qm set 100 --hostpci0 0000:00:02,x-vga=1 --bios ovmf```

# SYNOPSIS

**qm set** [_OPTIONS_] _vmid_

# DESCRIPTION

**qm set** 修改 Proxmox VE 中 QEMU/KVM 虚拟机的配置。某些更改可能需要重启虚拟机才能生效。此命令可以配置 CPU、内存、存储、网络和硬件直通选项。

# PARAMETERS

**vmid**
> 虚拟机的数字 ID

**--name** _string_
> 设置 GUI 中显示的虚拟机名称

**--autostart** _boolean_
> 宿主机启动时自动启动虚拟机

**--cores** _number_
> CPU 核心数量

**--memory** _megabytes_
> 以 MB 计的内存大小

**--net**_N_ _config_
> 网络设备配置（N=0-31）

**--scsi**_N_ _config_
> SCSI 磁盘配置

**--hostpci**_N_ _config_
> PCI 设备直通配置

**--delete** _list_
> 要删除的设置的逗号分隔列表

# CAVEATS

某些更改要求先停止虚拟机。硬件直通需要 IOMMU 支持。影响运行中虚拟机的更改可能被标记为待处理，直到重启后才生效。

# HISTORY

**qm set** 是 **Proxmox VE** 虚拟化平台的组成部分，用于管理 QEMU/KVM 虚拟机。

# INSTALL

```dnf: sudo dnf install qm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qm](/man/qm)(1), [qm-config](/man/qm-config)(1), [qm-pending](/man/qm-pending)(1)
