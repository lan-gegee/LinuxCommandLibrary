# TAGLINE

克隆 Proxmox 虚拟机

# TLDR

**复制**一台虚拟机

```qm clone 100 101```

以指定**名称**复制

```qm clone 100 101 --name new_vm```

以指定**描述**复制

```qm clone 100 101 --description "Clone of VM 100"```

创建所有磁盘的**完整副本**

```qm clone 100 101 --full```

指定**格式**的完整复制（qcow2、raw、vmdk）

```qm clone 100 101 --full --format qcow2```

复制并加入指定的**资源池**

```qm clone 100 101 --pool pool_name```

# SYNOPSIS

**qm clone** _vmid_ _newid_ [_options_]

# PARAMETERS

**--name** _name_
> 为克隆的虚拟机设置名称

**--description** _text_
> 为克隆的虚拟机设置描述

**--full**
> 创建所有磁盘的完整副本，而不是链接克隆

**--format** _format_
> 磁盘镜像的目标格式（qcow2、raw、vmdk）

**--pool** _name_
> 将克隆的虚拟机加入指定的资源池

# DESCRIPTION

**qm clone** 在 Proxmox VE 中创建 QEMU/KVM 虚拟机的副本。默认创建链接克隆，与原虚拟机共享基础镜像；--full 选项则创建独立的完整副本。

克隆适合用来制作虚拟机模板以及快速部署多台相似的机器。

# CAVEATS

链接克隆依赖原始虚拟机的磁盘。完整克隆需要更多存储空间但相互独立。为保证克隆的一致性，应先停止原始虚拟机或为其创建快照。

# HISTORY

属于 **Proxmox VE** 的 QEMU/KVM 管理工具，用于虚拟机管理。

# INSTALL

```dnf: sudo dnf install qm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qm](/man/qm)(1), [qm-create](/man/qm-create)(1), [qm-destroy](/man/qm-destroy)(1)
