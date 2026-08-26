# TAGLINE

在 Proxmox 虚拟机内运行命令

# TLDR

通过 guest agent **执行**命令

```qm guest exec 100 command arg1 arg2```

**异步**执行

```qm guest exec 100 command --synchronous 0```

以 10 秒的**超时**执行

```qm guest exec 100 command --timeout 10```

执行并将 **stdin 转发**给客户机

```qm guest exec 100 command --pass-stdin 1```

# SYNOPSIS

**qm guest exec** _vmid_ _command_ [_arguments_...] [_options_]

# PARAMETERS

**--synchronous** _0|1_
> 等待命令完成（默认 _1_）。设为 _0_ 时，**qm guest exec** 立即返回 PID；稍后用 **qm guest exec-status** 获取输出。

**--timeout** _seconds_
> 同步等待的最长时间（默认 _30_）。超时后强制转为异步运行。

**--pass-stdin** _0|1_
> 将宿主机的 stdin 转发给客户机命令（默认 _0_）。

# DESCRIPTION

**qm guest exec** 通过 QEMU guest agent 在虚拟机内执行命令。这样无需网络访问虚拟机，就能从宿主机层面控制客户机操作。

前提是虚拟机内必须安装并运行 guest agent。

# CAVEATS

要求虚拟机内已安装并运行 QEMU guest agent。某些命令可能需要客户机操作系统内的特定权限。

# HISTORY

属于 **Proxmox VE** 的 QEMU/KVM 管理工具。guest agent 通信提供了带外管理能力。

# INSTALL

```dnf: sudo dnf install qm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qm](/man/qm)(1), [qm-agent](/man/qm-agent)(1)
