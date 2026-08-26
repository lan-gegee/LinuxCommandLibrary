# TAGLINE

在 Proxmox LXC 容器内打开 shell 会话

# TLDR

**进入容器的交互式 shell**

```pct enter [VMID]```

**在容器内运行单条命令**（使用 pct exec）

```pct exec [VMID] -- [ls -la]```

# SYNOPSIS

**pct enter** _vmid_

# PARAMETERS

**vmid**
> 容器的数字 ID（例如 100）。

# DESCRIPTION

**pct enter** 在运行中的 Proxmox LXC 容器内打开交互式 shell 会话。它无需 SSH 即可提供直接的控制台访问，类似于 **lxc-attach** 或 **docker exec**。若要运行非交互式的单条命令，请改用 **pct exec**。

# RELATED COMMANDS

```
pct enter   - Interactive shell session
pct exec    - Run a single command in a container
pct console - Full console access (login prompt)
```

# CAVEATS

容器必须处于运行状态。需要 Proxmox VE 主机访问权限。非交互式或脚本化的命令请使用 **pct exec**。

# HISTORY

pct 命令是 **Proxmox VE** 的一部分，由 **Proxmox Server Solutions GmbH** 开发，用于在其虚拟化平台中管理 LXC 容器。

# SEE ALSO

[pct](/man/pct)(1), [pct-exec](/man/pct-exec)(1), [pct-console](/man/pct-console)(1), [pct-list](/man/pct-list)(1), [lxc-attach](/man/lxc-attach)(1)
