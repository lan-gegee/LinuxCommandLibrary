# TAGLINE

启动 Proxmox LXC 容器

# TLDR

**启动**容器

```pct start 100```

以**详细调试**日志启动

```pct start 100 --debug```

# SYNOPSIS

**pct start** _vmid_ [_OPTIONS_]

# PARAMETERS

**vmid**
> 容器的数字 ID（100–999999999）

**--debug**
> 启动时启用非常详细的调试日志级别（默认关闭）

**--skiplock**
> 忽略锁；仅 root 允许使用此选项

# DESCRIPTION

**pct start** 启动当前已停止的 Proxmox VE LXC 容器。它会应用待生效的配置更改、搭建容器环境，并启动来宾 init 进程。

如果启动失败，**--debug** 会产生更详细的日志。排查启动问题时，也可以通过相关的 LXC 工具以前台/调试模式启动。

# CAVEATS

容器不能已在运行中。其他 **pct** 操作（备份、迁移、快照等）产生的锁会阻碍启动，除非由 root 谨慎使用 **--skiplock**。资源限制（内存、CPU、存储）以及缺失的卷可能导致启动失败。

# HISTORY

**pct start** 是 **Proxmox VE** 中用于管理 LXC 容器的 **pct** 工具的一部分。

# SEE ALSO

[pct](/man/pct)(1), [pct-stop](/man/pct-stop)(1), [pct-shutdown](/man/pct-shutdown)(1), [pct-status](/man/pct-status)(1), [pct-reboot](/man/pct-reboot)(1)

# RESOURCES

```[Documentation](https://pve.proxmox.com/pve-docs/pct.1.html)```

```[Homepage](https://www.proxmox.com)```

<!-- verified: 2026-07-16 -->
