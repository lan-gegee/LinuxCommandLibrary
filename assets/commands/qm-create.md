# TAGLINE

创建 Proxmox 虚拟机

# TLDR

以**默认设置**创建虚拟机（512MiB 内存、1 个 CPU）

```qm create 100```

指定**名称**创建并自动**启动**

```qm create 100 --name vm_name --start```

指定**内存**和 **CPU 数量**创建

```qm create 100 --memory 8192 --cores 4```

指定**操作系统类型**

```qm create 100 --ostype win10```

从归档中**替换**已有机器

```qm create 100 --archive path/to/backup.tar --force 1```

指定**安装介质**

```qm create 100 --cdrom local:iso/install.iso```

使用**网桥**创建

```qm create 100 --net0 virtio,bridge=vmbr0```

# SYNOPSIS

**qm create** _vmid_ [_options_]

# PARAMETERS

**--name** _name_
> 设置虚拟机名称

**--memory** _mb_
> 以 MB 计的内存大小

**--cores** _count_
> CPU 核心数量

**--ostype** _type_
> 操作系统类型（l24、l26、win10 等）

**--cdrom** _volume_
> 用于安装的 ISO 镜像

**--net0** _config_
> 网络适配器配置

**--start**
> 创建后启动虚拟机

**--archive** _file_
> 从备份归档恢复

**--force** _1|0_
> 强制覆盖已有的虚拟机

# DESCRIPTION

**qm create** 在 Proxmox VE 中创建或恢复 QEMU/KVM 虚拟机。它为 CPU、内存、存储和网络提供了丰富的配置选项。

虚拟机既可以从零创建，也可以从备份归档恢复。

# CAVEATS

VM ID 在整个集群中必须唯一。某些选项需要额外的存储或网络配置。

# HISTORY

属于 **Proxmox VE** 的 QEMU/KVM 管理工具，用于虚拟机管理。

# INSTALL

```dnf: sudo dnf install qm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qm](/man/qm)(1), [qm-clone](/man/qm-clone)(1), [qm-destroy](/man/qm-destroy)(1)
