# TAGLINE

等待 Proxmox 虚拟机停止

# TLDR

**等待**虚拟机停止

```qm wait [vmid]```

以 60 秒的**超时**等待

```qm wait --timeout 60 [vmid]```

先**关机**再等待虚拟机停止

```qm shutdown [vmid] && qm wait --timeout 60 [vmid]```

# SYNOPSIS

**qm wait** [_options_] _vmid_

# PARAMETERS

**--timeout** _seconds_
> 同步等待的最长时间，超过即返回。设为 0 表示禁用。到达时限时命令会带着 PID 返回。

# DESCRIPTION

**qm wait** 阻塞直到虚拟机进入停止状态。这在脚本中很有用，可确保虚拟机完全停止后再执行后续操作。

与 shutdown 结合使用，可以实现正常停止虚拟机并等待完成。

# CAVEATS

不设置超时的话，如果虚拟机一直不停止，命令可能无限阻塞。脚本中应始终使用超时以获得可预期的行为。

# HISTORY

属于 **Proxmox VE** 的 QEMU/KVM 管理工具，用于虚拟机管理。

# INSTALL

```dnf: sudo dnf install qm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qm](/man/qm)(1), [qm-shutdown](/man/qm-shutdown)(1), [qm-stop](/man/qm-stop)(1)
