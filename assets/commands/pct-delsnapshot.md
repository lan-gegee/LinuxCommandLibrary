# TAGLINE

删除 Proxmox LXC 容器快照

# TLDR

从容器中**删除**指定名称的快照

```pct delsnapshot [vmid] [snapname]```

磁盘快照清理失败时**强制**从配置中移除

```pct delsnapshot [vmid] [snapname] --force```

# SYNOPSIS

**pct delsnapshot** _vmid_ _snapname_ [_OPTIONS_]

# PARAMETERS

**vmid**
> 容器的数字 ID（100–999999999）

**snapname**
> 要删除的快照名称

**--force**
> 即使移除磁盘快照失败，也将其从配置文件中移除

# DESCRIPTION

**pct delsnapshot** 从 Proxmox VE 容器中删除 LXC 快照。它会移除给定 **vmid** 对应快照的磁盘状态和配置条目。

快照是容器磁盘和配置在某个时间点的副本。删除快照会释放该快照占用的存储空间，且不可逆。删除前请先用 **pct listsnapshot** 列出可用的快照名称。

# CAVEATS

删除快照无法撤销。如果磁盘快照移除失败，除非使用 **--force**，否则配置条目可能会残留；请谨慎使用 force，以避免配置与磁盘不一致。

# HISTORY

**pct delsnapshot** 是 **Proxmox VE** 中用于管理 LXC 容器的 **pct** 工具的一部分。

# SEE ALSO

[pct](/man/pct)(1), [pct-listsnapshot](/man/pct-listsnapshot)(1), [pct-rollback](/man/pct-rollback)(1)

# RESOURCES

```[Documentation](https://pve.proxmox.com/pve-docs/pct.1.html)```

```[Homepage](https://www.proxmox.com)```

<!-- verified: 2026-07-14 -->
