# TAGLINE

卸载之前挂载到 Proxmox 主机上的容器文件系统

# TLDR

**卸载**容器文件系统

```pct unmount 100```

# SYNOPSIS

**pct unmount** _vmid_

# DESCRIPTION

**pct unmount** 卸载之前用 **pct mount** 挂载到 Proxmox 主机上的容器文件系统。重新启动容器前必须执行此操作。

# PARAMETERS

**vmid**
> 容器的数字 ID

# CAVEATS

卸载前请确保没有进程正在访问已挂载的文件系统。启动容器前未卸载可能导致数据损坏。

# HISTORY

**pct unmount** 是用于管理 LXC 容器的 **Proxmox VE** 虚拟化平台的一部分。

# SEE ALSO

[pct](/man/pct)(1), [pct-mount](/man/pct-mount)(1)
