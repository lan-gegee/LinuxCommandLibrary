# TAGLINE

列出 Proxmox LXC 容器的快照

# TLDR

**列出**某个容器的全部快照

```pct listsnapshot [vmid]```

# SYNOPSIS

**pct listsnapshot** _vmid_

# PARAMETERS

**vmid**
> 容器的数字 ID（100–999999999）

# DESCRIPTION

**pct listsnapshot** 列出 Proxmox VE LXC 容器的所有快照。输出通常包含快照名称和相关元数据，便于你为 **pct rollback** 或 **pct delsnapshot** 选择快照。

# HISTORY

**pct listsnapshot** 是 **Proxmox VE** 中用于管理 LXC 容器的 **pct** 工具的一部分。

# SEE ALSO

[pct](/man/pct)(1), [pct-delsnapshot](/man/pct-delsnapshot)(1), [pct-rollback](/man/pct-rollback)(1)

# RESOURCES

```[Documentation](https://pve.proxmox.com/pve-docs/pct.1.html)```

```[Homepage](https://www.proxmox.com)```

<!-- verified: 2026-07-14 -->
