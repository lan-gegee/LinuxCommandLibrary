# TAGLINE

将磁盘镜像导入 Proxmox 虚拟机

# TLDR

此命令是 **qm disk import** 的别名

查看原始命令的文档

```tldr qm disk```

# SYNOPSIS

**qm importdisk** _vmid_ _source_ _storage_ [_options_]

# DESCRIPTION

**qm importdisk** 是 **qm disk import** 的别名，用于将外部磁盘镜像导入 Proxmox VE 虚拟机。它支持多种格式，包括 VMDK、qcow2 和 raw。

# INSTALL

```dnf: sudo dnf install qm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qm](/man/qm)(1), [qm-disk](/man/qm-disk)(1)
