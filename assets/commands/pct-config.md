# TAGLINE

显示 Proxmox LXC 容器的配置

# TLDR

**显示**容器配置

```pct config 100```

显示**当前**运行配置

```pct config 100 --current```

显示**快照**配置

```pct config 100 --snapshot snapshot_name```

# SYNOPSIS

**pct config** [_OPTIONS_] _vmid_

# DESCRIPTION

**pct config** 显示 Proxmox LXC 容器的配置。默认情况下，它显示已保存的配置，其中包括将在下次启动时应用的待处理更改。

# PARAMETERS

**vmid**
> 容器的唯一数字 ID（整数，100 到 999999999）

**--current**
> 获取当前值而不是待处理值（布尔值，默认 0）

**--snapshot** _name_
> 从给定快照获取配置值

# CAVEATS

默认输出显示包含待处理更改的已保存配置。只想查看活动运行时配置时，请使用 **--current**。

# HISTORY

**pct config** 是 **Proxmox VE** 虚拟化平台中管理 LXC 容器的一部分。

# SEE ALSO

[pct](/man/pct)(1), [pct-set](/man/pct-set)(1), [pct-list](/man/pct-list)(1), [pct-status](/man/pct-status)(1)
