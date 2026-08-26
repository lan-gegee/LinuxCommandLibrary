# TAGLINE

显示 Proxmox LXC 容器的运行状态

# TLDR

**查看**容器状态（输出例如 `status: running`）

```pct status [100]```

**显示详细的**运行时与配置信息

```pct status [100] --verbose```

# SYNOPSIS

**pct status** [_OPTIONS_] _vmid_

# DESCRIPTION

**pct status** 显示 Proxmox LXC 容器的当前状态，指示其正在运行、已停止还是处于其他状态。

# PARAMETERS

**vmid**
> 容器的数字 ID

**--verbose**
> 显示包括资源使用在内的详细状态信息

# CAVEATS

状态是从 Proxmox 的视角报告的。显示为 running 的容器内部可能存在此命令无法发现的问题。

# HISTORY

**pct status** 是用于管理 LXC 容器的 **Proxmox VE** 虚拟化平台的一部分。

# SEE ALSO

[pct](/man/pct)(1), [pct-list](/man/pct-list)(1)
