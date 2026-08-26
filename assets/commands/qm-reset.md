# TAGLINE

硬重置 Proxmox 虚拟机

# TLDR

**重置**虚拟机

```qm reset 100```

重置并**跳过锁**（仅限 root）

```qm reset --skiplock true 100```

# SYNOPSIS

**qm reset** [_options_] _vmid_

# PARAMETERS

**--skiplock** _true|false_
> 忽略锁并强制重置（仅限 root）

# DESCRIPTION

**qm reset** 对虚拟机执行硬重置，相当于按下物理硬件上的复位按钮。它会立即重启虚拟机，不进行正常关机。

当客户机操作系统无响应且无法正常重启时使用此命令。

# CAVEATS

如果文件系统未正确同步，硬重置可能导致客户机内数据丢失。skiplock 选项需要 root 权限。

# HISTORY

属于 **Proxmox VE** 的 QEMU/KVM 管理工具，用于虚拟机管理。

# INSTALL

```dnf: sudo dnf install qm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qm](/man/qm)(1), [qm-reboot](/man/qm-reboot)(1), [qm-shutdown](/man/qm-shutdown)(1)
