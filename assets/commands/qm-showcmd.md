# TAGLINE

显示 Proxmox 虚拟机的 QEMU 命令行

# TLDR

显示启动虚拟机所用的**命令行**

```qm showcmd 100```

以**增强可读性**的方式显示（每个选项一行）

```qm showcmd 100 --pretty 1```

显示来自**特定快照**的命令行

```qm showcmd 100 --snapshot snapshot_name```

# SYNOPSIS

**qm showcmd** _vmid_ [_options_]

# PARAMETERS

**--pretty** _boolean_
> 为提高可读性，将每个选项单独放一行。默认为 0。

**--snapshot** _string_
> 从给定快照获取配置

# DESCRIPTION

**qm showcmd** 显示用于启动虚拟机的命令行。这有助于调试虚拟机配置，并了解 QEMU 是如何被调用的。

输出会基于虚拟机的当前配置或特定快照，展示所有 QEMU 选项和参数。

# CAVEATS

仅为调试信息；实际运行时的命令可能有所不同。配置更改需要重启虚拟机才能生效。

# HISTORY

属于 **Proxmox VE** 的 QEMU/KVM 管理工具，用于调试虚拟机配置。

# INSTALL

```dnf: sudo dnf install qm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qm](/man/qm)(1), [qm-config](/man/qm-config)(1)
