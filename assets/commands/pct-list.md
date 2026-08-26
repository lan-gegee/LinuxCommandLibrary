# TAGLINE

显示 Proxmox VE 主机上的所有 LXC 容器

# TLDR

**列出当前节点上的所有容器**

```pct list```

# SYNOPSIS

**pct list**

# DESCRIPTION

**pct list** 以表格形式显示当前 Proxmox VE 节点上的所有 LXC 容器。它显示容器的 VMID、状态（running/stopped）、锁定状态和名称。

# CAVEATS

仅显示本地节点上的容器。如需集群范围的容器列表，请使用 **pvesh**。需要 Proxmox VE 环境。

# HISTORY

pct 命令套件是 **Proxmox VE** 的一部分，自 Proxmox 采用 LXC 以来一直提供全面的 LXC 容器管理功能。

# SEE ALSO

[pct](/man/pct)(1), [pct-create](/man/pct-create)(1), [pct-config](/man/pct-config)(1), [pct-status](/man/pct-status)(1), [pct-enter](/man/pct-enter)(1), [pct-destroy](/man/pct-destroy)(1), [pct-restore](/man/pct-restore)(1), [pvesh](/man/pvesh)(1), [lxc-ls](/man/lxc-ls)(1)
