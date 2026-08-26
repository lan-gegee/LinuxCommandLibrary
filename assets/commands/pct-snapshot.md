# TAGLINE

创建 Proxmox LXC 容器的快照

# TLDR

**创建**名为 pre-upgrade 的快照

```pct snapshot 100 pre-upgrade```

创建带**描述**的快照

```pct snapshot 100 pre-upgrade --description "before package upgrade"```

# SYNOPSIS

**pct snapshot** _vmid_ _snapname_ [_OPTIONS_]

# PARAMETERS

**vmid**
> 容器的数字 ID（100–999999999）

**snapname**
> 新快照的名称

**--description** _text_
> 快照的文字描述或备注

# DESCRIPTION

**pct snapshot** 为 Proxmox VE LXC 容器创建快照，将其磁盘和配置状态保存到给定名称下。之后可以用 **pct listsnapshot** 列出快照、用 **pct rollback** 恢复，或用 **pct delsnapshot** 删除。

# CAVEATS

快照支持取决于底层存储（例如 LVM-thin、ZFS 或 Ceph）。并非所有存储类型都支持快照。在容器写入负载较高时创建快照可能会短暂影响 I/O。

# HISTORY

**pct snapshot** 是 **Proxmox VE** 中用于管理 LXC 容器的 **pct** 工具的一部分。

# SEE ALSO

[pct](/man/pct)(1), [pct-listsnapshot](/man/pct-listsnapshot)(1), [pct-rollback](/man/pct-rollback)(1), [pct-delsnapshot](/man/pct-delsnapshot)(1)

# RESOURCES

```[Documentation](https://pve.proxmox.com/pve-docs/pct.1.html)```

```[Homepage](https://www.proxmox.com)```

<!-- verified: 2026-07-16 -->
