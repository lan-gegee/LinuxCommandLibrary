# TAGLINE

为克隆准备虚拟机镜像

# TLDR

**列出**可用操作

```virt-sysprep --list-operations```

移除**敏感**数据

```sudo virt-sysprep -a [path/to/image.qcow2]```

按域名执行**试运行**

```sudo virt-sysprep -d [vm_name] -n```

运行指定的**操作**

```sudo virt-sysprep -d [vm_name] --operations [operation1,operation2]```

设置**主机名**和 machine-id

```sudo virt-sysprep -d [vm_name] --enable customizations --hostname [host_name] --operation machine-id```

# SYNOPSIS

**virt-sysprep** [_OPTIONS_]

# PARAMETERS

**-a, --add** _IMAGE_
> 添加磁盘镜像

**-d, --domain** _VM_
> 按名称指定虚拟机

**-n, --dry-run**
> 显示将要执行的操作但不做更改

**--operations** _OPS_
> 仅运行指定的操作

**--list-operations**
> 列出所有支持的操作

**--hostname** _NAME_
> 设置主机名

**--enable** _FEATURE_
> 启用特定功能

# DESCRIPTION

**virt-sysprep** 重置、取消配置或定制虚拟机镜像，以便克隆或部署。它会移除特定于机器的数据，如 SSH 密钥、日志和持久化设备名。

它通过移除那些每台机器都应唯一的信息，将虚拟机镜像准备为模板。

# CAVEATS

虚拟机必须处于关机状态。通常需要 root 权限。某些操作使用不当可能导致虚拟机损坏。处理前请务必备份镜像。

# INSTALL

```apt: sudo apt install guestfs-tools```

```dnf: sudo dnf install guestfs-tools```

```pacman: sudo pacman -S guestfs-tools```

```zypper: sudo zypper install guestfs-tools```

```nix: nix profile install nixpkgs#guestfs-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[virt-clone](/man/virt-clone)(1), [virt-customize](/man/virt-customize)(1)
