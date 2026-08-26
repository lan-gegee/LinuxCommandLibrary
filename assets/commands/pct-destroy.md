# TAGLINE

移除 Proxmox LXC 容器及其关联的存储

# TLDR

**销毁**容器

```pct destroy 100```

**强制**销毁运行中的容器

```pct destroy 100 --force```

销毁并**清除**相关引用

```pct destroy 100 --purge```

# SYNOPSIS

**pct destroy** _vmid_ [_OPTIONS_]

# DESCRIPTION

**pct destroy** 移除 Proxmox LXC 容器及其关联的存储。默认情况下必须先停止容器，除非使用了 force 选项。

# PARAMETERS

**vmid**
> 容器的数字 ID

**--force**
> 即使容器正在运行也进行销毁

**--purge**
> 同时移除对该容器的所有引用（作业、复制等）

# CAVEATS

此操作不可逆。容器的所有数据都将丢失。与容器关联的快照也会一并移除。使用 **--purge** 可清理计划任务和复制配置。

# HISTORY

**pct destroy** 是用于管理 LXC 容器的 **Proxmox VE** 虚拟化平台的一部分。

# SEE ALSO

[pct](/man/pct)(1), [pct-create](/man/pct-create)(1)
