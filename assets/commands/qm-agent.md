# TAGLINE

在 Proxmox VE 中通过 QEMU guest agent 执行命令

# TLDR

**此命令是 `qm guest cmd` 的别名**

```tldr qm guest cmd```

**在虚拟机上执行 guest agent 命令**

```qm agent [vmid] [command]```

**ping guest agent 以检查其是否在运行**

```qm agent [vmid] ping```

**冻结客户机文件系统（用于快照）**

```qm agent [vmid] fsfreeze-freeze```

**快照完成后解冻客户机文件系统**

```qm agent [vmid] fsfreeze-thaw```

# SYNOPSIS

**qm agent** _vmid_ _command_

# DESCRIPTION

**qm agent** 是 Proxmox VE 中 **qm guest cmd** 的别名。它通过运行在虚拟机内的 QEMU guest agent（qemu-ga）执行命令，实现宿主机与客户机之间的通信，支持文件系统冻结/解冻、正常关机以及信息获取等操作。

必须在虚拟机内安装并运行 QEMU guest agent，并且在虚拟机配置中启用 agent 选项。

# CAVEATS

必须在客户机操作系统内安装 QEMU guest agent，并在虚拟机配置中启用它。Linux 客户机需安装 **qemu-guest-agent** 软件包；Windows 客户机的 agent 包含在 VirtIO 驱动中。agent 未运行时通信会失败。

# HISTORY

**qm agent** 属于开源虚拟化平台 **Proxmox VE**。QEMU guest agent 协议提供了超越 ACPI 电源管理的细粒度虚拟机控制能力。

# INSTALL

```dnf: sudo dnf install qm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qm](/man/qm)(1), [qm-guest](/man/qm-guest)(1), [qm-guest-exec](/man/qm-guest-exec)(1)
