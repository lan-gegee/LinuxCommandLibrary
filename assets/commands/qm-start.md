# TAGLINE

启动 Proxmox 虚拟机

# TLDR

**启动**虚拟机

```qm start 100```

指定 **machine** 类型

```qm start 100 --machine q35```

带**超时**启动

```qm start 100 --timeout 60```

# SYNOPSIS

**qm start** [_OPTIONS_] _vmid_

# DESCRIPTION

**qm start** 启动 Proxmox VE 中的 QEMU/KVM 虚拟机。虚拟机必须已存在且未在运行中。各种启动选项可以控制模拟的机器类型、超时和其他参数。

# PARAMETERS

**vmid**
> 虚拟机的数字 ID

**--machine** _type_
> 指定 QEMU 机器类型（如 q35、pc、pc-i440fx）

**--timeout** _seconds_
> 启动操作的超时时间（秒）

**--skiplock** _boolean_
> 跳过锁检查（仅限 root）

**--stateuri** _uri_
> 用于从迁移或快照恢复状态的 URI

# CAVEATS

虚拟机必须处于停止状态才能启动。如果虚拟机有待处理的配置更改，将在启动时应用。请确保有足够的资源（CPU、内存、存储）可用。

# HISTORY

**qm start** 是 **Proxmox VE** 虚拟化平台的组成部分，用于管理 QEMU/KVM 虚拟机。

# INSTALL

```dnf: sudo dnf install qm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qm](/man/qm)(1), [qm-stop](/man/qm-stop)(1), [qm-shutdown](/man/qm-shutdown)(1)
