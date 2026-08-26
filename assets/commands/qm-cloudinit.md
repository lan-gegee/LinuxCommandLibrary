# TAGLINE

管理 Proxmox 虚拟机的 Cloud-Init 设置

# TLDR

为特定配置类型生成 **cloudinit 文件**

```qm cloudinit dump 100 user```

生成 **network** 配置

```qm cloudinit dump 100 network```

生成 **meta** 配置

```qm cloudinit dump 100 meta```

# SYNOPSIS

**qm cloudinit** dump _vmid_ _type_

# PARAMETERS

**dump** _vmid_ _type_
> 为指定类型（meta、network、user）生成 cloudinit 文件

# DESCRIPTION

**qm cloudinit** 管理 Proxmox VE 虚拟机的 Cloud-Init 设置。Cloud-Init 为虚拟机提供初始配置，包括网络设置、用户账户和自定义脚本。

dump 子命令会生成 Cloud-Init 配置文件，供检查和调试使用。

# CAVEATS

要求虚拟机镜像中已安装并配置 Cloud-Init。配置类型必须在虚拟机设置中正确定义。

# HISTORY

属于 **Proxmox VE** 的 QEMU/KVM 管理工具。借助 Cloud-Init 集成，可以像云环境一样自动供应虚拟机。

# INSTALL

```dnf: sudo dnf install qm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qm](/man/qm)(1), [qm-create](/man/qm-create)(1), [cloud-init](/man/cloud-init)(1)
