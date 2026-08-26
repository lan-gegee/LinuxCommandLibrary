# TAGLINE

为 Proxmox 虚拟机代理 VNC 连接

# TLDR

为虚拟机**代理** VNC 流量

```qm vncproxy 100```

# SYNOPSIS

**qm vncproxy** _vmid_

# DESCRIPTION

**qm vncproxy** 将虚拟机的 VNC（Virtual Network Computing，虚拟网络计算）流量代理到 stdin/stdout。这使 VNC 客户端能够通过 Proxmox VE 基础设施连接到虚拟机。

该代理负责处理 VNC 会话的身份验证和连接建立。

# CAVEATS

通常由 Proxmox Web 界面在内部使用。直接使用需要了解 VNC 协议和连接处理机制。

# HISTORY

属于 **Proxmox VE** 的 QEMU/KVM 管理工具。为基于 Web 的 VNC 控制台访问提供后端支持。

# INSTALL

```dnf: sudo dnf install qm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qm](/man/qm)(1), [qm-terminal](/man/qm-terminal)(1)
