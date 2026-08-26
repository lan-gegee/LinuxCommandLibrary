# TAGLINE

与 Proxmox 虚拟机的 guest agent 交互

# TLDR

**查看**命令执行状态

```qm guest exec-status vm_id pid```

交互式**设置**用户密码

```qm guest passwd vm_id username```

设置**哈希过的**密码

```qm guest passwd vm_id username --crypted 1```

执行 **guest agent** 命令

```qm guest cmd vm_id fsfreeze-freeze```

在客户机内**执行**命令

```qm guest exec vm_id command arg1 arg2```

**异步**执行

```qm guest exec vm_id command --synchronous 0```

带**超时**执行

```qm guest exec vm_id command --timeout 10```

转发 **stdin** 执行

```qm guest exec vm_id command --pass-stdin 1```

# SYNOPSIS

**qm guest** _cmd_ _vmid_ [_OPTIONS_]

# DESCRIPTION

**qm guest** 与运行在虚拟机内的 QEMU Guest Agent 交互。它可以执行命令、管理用户账户，以及运行文件系统冻结/解冻等 guest agent 操作，以实现一致的备份。

# PARAMETERS

**cmd**
> 子命令：cmd、exec、exec-status、passwd

**vmid**
> 虚拟机的数字 ID

**--timeout** _seconds_
> 命令执行的超时时间

**--synchronous** _boolean_
> 同步（默认）或异步运行命令

**--pass-stdin** _boolean_
> 将 stdin 转发给 guest agent

**--crypted** _boolean_
> 密码已经是哈希值

# CAVEATS

要求虚拟机内已安装并运行 QEMU Guest Agent（qemu-guest-agent）。还必须在虚拟机配置中启用 guest agent（Agent: Enabled）。通信经由 virtio 串口设备进行，与网络连通性无关。

# HISTORY

**qm guest** 是 **Proxmox VE** 虚拟化平台的组成部分，用于通过 guest agent 管理 QEMU/KVM 虚拟机。

# INSTALL

```dnf: sudo dnf install qm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qm](/man/qm)(1), [qm-start](/man/qm-start)(1), [qm-stop](/man/qm-stop)(1)
