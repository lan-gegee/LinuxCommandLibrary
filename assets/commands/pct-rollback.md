# TAGLINE

将 Proxmox LXC 容器恢复到快照

# TLDR

将容器**回滚**到指定名称的快照

```pct rollback [vmid] [snapname]```

回滚并在恢复后**启动**容器

```pct rollback [vmid] [snapname] --start```

# SYNOPSIS

**pct rollback** _vmid_ _snapname_ [_OPTIONS_]

# PARAMETERS

**vmid**
> 容器的数字 ID（100–999999999）

**snapname**
> 要恢复的快照名称

**--start**
> 回滚成功后启动容器（默认：关闭）

# DESCRIPTION

**pct rollback** 将 Proxmox VE 上的 LXC 容器恢复到指定快照所记录的磁盘和配置状态。快照之后的容器当前状态将被丢弃。

使用 **pct listsnapshot** 查看可用的快照名称。根据存储类型和快照类型，回滚可能要求容器处于停止状态；请查阅 Proxmox 文档了解你的存储后端。

# CAVEATS

回滚对快照之后所做的更改具有破坏性。请确认选择了正确的 **snapname**。根据存储特性（例如线性快照链），回滚可能影响更新的快照。

# HISTORY

**pct rollback** 是 **Proxmox VE** 中用于管理 LXC 容器的 **pct** 工具的一部分。

# SEE ALSO

[pct](/man/pct)(1), [pct-listsnapshot](/man/pct-listsnapshot)(1), [pct-delsnapshot](/man/pct-delsnapshot)(1)

# RESOURCES

```[Documentation](https://pve.proxmox.com/pve-docs/pct.1.html)```

```[Homepage](https://www.proxmox.com)```

<!-- verified: 2026-07-14 -->
