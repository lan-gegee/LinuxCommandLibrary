# TAGLINE

优雅地关闭 Proxmox LXC 容器

# TLDR

干净地**关机**容器

```pct shutdown 100```

以 30 秒的**超时**时间关机

```pct shutdown 100 --timeout 30```

优雅关机失败时强制容器**停止**

```pct shutdown 100 --forceStop```

# SYNOPSIS

**pct shutdown** _vmid_ [_OPTIONS_]

# PARAMETERS

**vmid**
> 容器的数字 ID（100–999999999）

**--timeout** _seconds_
> 等待干净关机的最大秒数（默认 60）

**--forceStop**
> 即使优雅关机失败也确保容器停止

# DESCRIPTION

**pct shutdown** 触发 Proxmox VE LXC 容器的干净关机（通过 **lxc-stop**）。与直接杀死所有进程的 **pct stop** 不同，它请求优雅断电，让服务能够正常退出。

如果容器未能在超时时间内停止，命令将失败，除非设置了 **--forceStop**。

# CAVEATS

容器必须处于运行状态。忽略 SIGTERM 的进程会阻碍关机，直到超时。如需立即硬停止，请改用 **pct stop**。

# HISTORY

**pct shutdown** 是 **Proxmox VE** 中用于管理 LXC 容器的 **pct** 工具的一部分。

# SEE ALSO

[pct](/man/pct)(1), [pct-stop](/man/pct-stop)(1), [pct-start](/man/pct-start)(1), [pct-reboot](/man/pct-reboot)(1), [lxc-stop](/man/lxc-stop)(1)

# RESOURCES

```[Documentation](https://pve.proxmox.com/pve-docs/pct.1.html)```

```[Homepage](https://www.proxmox.com)```

<!-- verified: 2026-07-16 -->
