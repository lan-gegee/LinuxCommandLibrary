# TAGLINE

列出 Proxmox 虚拟机

# TLDR

列出**所有虚拟机**

```qm list```

为运行中的虚拟机列出**完整状态**

```qm list --full 1```

# SYNOPSIS

**qm list** [_options_]

# PARAMETERS

**--full** _0|1_
> 为运行中的虚拟机显示完整状态信息

# DESCRIPTION

**qm list** 显示 Proxmox VE 节点上的所有虚拟机。它展示包括 VM ID、名称和状态在内的基本信息。

使用 full 选项时，会为运行中的虚拟机显示更多细节，包括资源使用情况。

# INSTALL

```dnf: sudo dnf install qm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qm](/man/qm)(1), [qm-status](/man/qm-status)(1)
