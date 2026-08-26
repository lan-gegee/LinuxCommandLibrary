# TAGLINE

连接到 Proxmox 虚拟机的串口控制台

# TLDR

**连接**到虚拟机的串口控制台

```qm terminal 100```

**连接**到指定的串口接口

```qm terminal 100 -iface serial1```

从终端**断开**

```Ctrl+o```

# SYNOPSIS

**qm terminal** _vmid_ [**-iface** _serial0..3_]

# DESCRIPTION

**qm terminal** 连接到虚拟机的串口控制台。它无需网络连通性或 VNC 即可提供对虚拟机的直接控制台访问。

使用 Ctrl+o 可从终端会话断开，且不影响虚拟机。

# PARAMETERS

**-iface** _serial0..3_
> 选择要连接的串口设备（serial0、serial1、serial2 或 serial3）。默认为第一个可用的串口控制台。

# CAVEATS

要求虚拟机已配置串口控制台（串口设备类型为 "socket"），并且虚拟机显示设置为 "Serial Terminal"。客户机操作系统必须启用串口控制台输出才能进行有意义的交互。

# HISTORY

属于 **Proxmox VE** 的 QEMU/KVM 管理工具，用于虚拟机管理。

# INSTALL

```dnf: sudo dnf install qm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qm](/man/qm)(1), [qm-monitor](/man/qm-monitor)(1), [qm-vncproxy](/man/qm-vncproxy)(1)
