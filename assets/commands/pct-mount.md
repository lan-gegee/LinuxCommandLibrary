# TAGLINE

将已停止容器的文件系统挂载到 Proxmox 主机上

# TLDR

**挂载**容器文件系统

```pct mount 100```

# SYNOPSIS

**pct mount** _vmid_

# DESCRIPTION

**pct mount** 将已停止容器的文件系统挂载到 Proxmox 主机上。这样无需启动容器即可直接访问容器文件，用于维护、恢复或检查。

# PARAMETERS

**vmid**
> 容器的数字 ID

# CAVEATS

挂载文件系统前必须停止容器。挂载点通常位于 /var/lib/lxc/VMID/rootfs。启动容器前务必先用 **pct unmount** 卸载。

# HISTORY

**pct mount** 是用于管理 LXC 容器的 **Proxmox VE** 虚拟化平台的一部分。

# SEE ALSO

[pct](/man/pct)(1), [pct-unmount](/man/pct-unmount)(1)
