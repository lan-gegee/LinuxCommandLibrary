# TAGLINE

立即停止 Proxmox LXC 容器

# TLDR

立即**停止**容器

```pct stop 100```

停止前中止进行中的**关机**任务

```pct stop 100 --overrule-shutdown```

# SYNOPSIS

**pct stop** _vmid_ [_OPTIONS_]

# PARAMETERS

**vmid**
> 容器的数字 ID（100–999999999）

**--overrule-shutdown**
> 尝试在停止前中止进行中的 vzshutdown 任务（默认关闭）

**--skiplock**
> 忽略锁；仅 root 允许使用此选项

# DESCRIPTION

**pct stop** 强行停止 Proxmox VE LXC 容器中运行的所有进程。与请求干净断电的 **pct shutdown** 不同，这是相当于直接拔电源的硬停止：进程无法正常刷写数据或干净退出。

需要优雅停止时请使用 **pct shutdown**；当容器无响应或需要立即中止时再使用 **pct stop**。

# CAVEATS

硬停止可能使应用丢失未保存的数据或留下不一致的文件。日常操作请优先使用 **pct shutdown**。并发管理任务持有的锁可能阻碍该命令，除非由 root 谨慎使用 **--skiplock**。

# HISTORY

**pct stop** 是 **Proxmox VE** 中用于管理 LXC 容器的 **pct** 工具的一部分。

# SEE ALSO

[pct](/man/pct)(1), [pct-shutdown](/man/pct-shutdown)(1), [pct-start](/man/pct-start)(1), [pct-status](/man/pct-status)(1)

# RESOURCES

```[Documentation](https://pve.proxmox.com/pve-docs/pct.1.html)```

```[Homepage](https://www.proxmox.com)```

<!-- verified: 2026-07-16 -->
