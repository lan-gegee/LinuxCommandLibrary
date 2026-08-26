# TAGLINE

对 Proxmox LXC 卷运行文件系统检查

# TLDR

检查容器的**所有卷**

```pct fsck [100]```

检查**指定卷**设备

```pct fsck [100] --device [mp0|mp1|rootfs|...]```

# SYNOPSIS

**pct fsck** _vmid_ [_OPTIONS_]

# PARAMETERS

**vmid**
> 要检查卷的容器的数字 ID

**--device** _volume_
> 将检查限制在单个卷上（例如 `rootfs`、`mp0`、`mp1`）

# DESCRIPTION

**pct fsck** 对 Proxmox VE LXC 容器的一个或多个卷运行文件系统一致性检查。若未指定 `--device`，则会检查该容器的所有已配置卷。

在不正常关机、存储出现问题，或容器因文件系统错误而无法启动时使用此命令。底层使用的检查工具取决于每个卷的文件系统类型（ext 系列文件系统通常为 `fsck`）。

# CAVEATS

运行文件系统检查前应先**停止**容器。对已挂载的活动卷运行 `fsck` 可能导致数据损坏。请确保容器磁盘所在的节点上有可用的存储空间。

# HISTORY

属于 **Proxmox VE** LXC 管理（`pct`）的一部分。

# SEE ALSO

[pct](/man/pct)(1), [fsck](/man/fsck)(8)

# RESOURCES

```[Homepage](https://www.proxmox.com)```

```[Documentation](https://pve.proxmox.com/pve-docs/pct.1.html)```

<!-- verified: 2026-07-28 -->
