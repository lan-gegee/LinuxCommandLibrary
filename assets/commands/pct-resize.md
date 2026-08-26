# TAGLINE

更改 Proxmox LXC 容器存储卷的大小

# TLDR

**调整**为绝对大小

```pct resize 100 rootfs 20G```

在现有大小基础上**增加**

```pct resize 100 rootfs +10G```

# SYNOPSIS

**pct resize** _vmid_ _disk_ _size_

# DESCRIPTION

**pct resize** 更改 Proxmox LXC 容器存储卷的大小。容器内的文件系统会随底层存储自动调整大小。

# PARAMETERS

**vmid**
> 容器的数字 ID

**disk**
> 要调整大小的磁盘（rootfs 或挂载点 mpN）

**size**
> 新大小（绝对值如 20G）或相对值（如 +10G）

# CAVEATS

大多数存储类型仅支持扩大容量。缩小卷可能导致数据丢失，且并非所有存储后端都支持。调整大小时容器可以处于运行状态。

# HISTORY

**pct resize** 是用于管理 LXC 容器的 **Proxmox VE** 虚拟化平台的一部分。

# SEE ALSO

[pct](/man/pct)(1), [pct-set](/man/pct-set)(1)
