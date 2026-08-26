# TAGLINE

重启 Proxmox LXC 容器

# TLDR

**重启**容器

```pct reboot 100```

以 60 秒的**超时**时间重启

```pct reboot 100 --timeout 60```

# SYNOPSIS

**pct reboot** _vmid_ [_OPTIONS_]

# DESCRIPTION

**pct reboot** 关机并重启 Proxmox LXC 容器。该命令会先请求容器优雅关机，然后再次启动，从而执行干净的重启。如果容器未能在超时时间内停止，操作将失败。

# PARAMETERS

**vmid**
> 容器的数字 ID（100 或更高）

**--timeout** _seconds_
> 等待关机的秒数，超时则失败。默认为 60 秒。

# CAVEATS

容器必须处于运行状态才能成功重启。如果容器中有阻碍关机的进程，重启可能会超时。与硬复位不同，此命令会先执行优雅关机，因此无响应的容器可能需要改为手动停止再启动。

# HISTORY

**pct reboot** 是用于管理 LXC 容器的 **Proxmox VE** 虚拟化平台的一部分。

# SEE ALSO

[pct](/man/pct)(1), [pct-status](/man/pct-status)(1)
