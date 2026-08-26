# TAGLINE

将 Proxmox LXC 容器转换为模板

# TLDR

将容器**转换**为模板

```pct template 100```

# SYNOPSIS

**pct template** _vmid_

# DESCRIPTION

**pct template** 将 Proxmox LXC 容器转换为模板。模板是只读的基础镜像，可通过克隆快速创建新容器。

# PARAMETERS

**vmid**
> 要转换的容器的数字 ID

# CAVEATS

转换前必须停止容器。此操作不可逆——容器变为模板后无法再次启动。模板只能被克隆，不能直接运行。

# HISTORY

**pct template** 是用于管理 LXC 容器的 **Proxmox VE** 虚拟化平台的一部分。

# SEE ALSO

[pct](/man/pct)(1), [pct-clone](/man/pct-clone)(1), [pct-create](/man/pct-create)(1)
