# TAGLINE

显示 Proxmox 虚拟机的运行状态

# TLDR

显示虚拟机的**状态**

```qm status 100```

显示**详细状态**

```qm status --verbose true 100```

# SYNOPSIS

**qm status** [_options_] _vmid_

# PARAMETERS

**--verbose** _true|false_
> 显示详细的状态信息

# DESCRIPTION

**qm status** 显示虚拟机的当前状态。基本输出展示运行状态（running、stopped、paused）。verbose 模式会显示运行时长和资源使用情况等更多细节。

# INSTALL

```dnf: sudo dnf install qm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qm](/man/qm)(1), [qm-list](/man/qm-list)(1)
