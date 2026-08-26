# TAGLINE

附加到容器的 TTY 控制台，提供直接的终端访问

# TLDR

按 ID **附加**到容器控制台

```pct console [100]```

# SYNOPSIS

**pct console** _vmid_

# DESCRIPTION

**pct console** 附加到容器的 TTY 控制台，提供直接的终端访问。适用于访问没有网络连接的容器，或排查启动问题。

# PARAMETERS

**vmid**
> 容器的数字 ID

# CAVEATS

按 **Ctrl+a** 再按 **q** 可脱离控制台而不终止会话。容器必须处于运行状态。若要非交互式地执行命令，请改用 **pct exec**。若要直接进入容器的命名空间，请使用 **pct enter**。

# HISTORY

**pct console** 是用于管理 LXC 容器的 **Proxmox VE** 虚拟化平台的一部分。

# SEE ALSO

[pct](/man/pct)(1), [pct-enter](/man/pct-enter)(1), [pct-exec](/man/pct-exec)(1)
