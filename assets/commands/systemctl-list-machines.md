# TAGLINE

列出已注册的机器与容器

# TLDR

列出**所有**机器

```systemctl list-machines```

列出**特定**机器

```systemctl list-machines [machine]```

列出**多个**机器

```systemctl list-machines [machine1 machine2 ...]```

按**模式**过滤

```systemctl list-machines [pattern*]```

# SYNOPSIS

**systemctl list-machines** [_PATTERN_...]

# DESCRIPTION

**systemctl list-machines** 显示本机以及向 systemd-machined 注册的所有正在运行的本地容器和虚拟机。它会显示机器名称、状态和失败单元的数量。

这提供了所有由 systemd 管理的机器的概览，包括本地主机和 systemd-nspawn 容器。

# CAVEATS

只显示向 systemd-machined 注册的机器。外部容器（Docker、未集成 systemd 的 Podman）不会被列出。本地主机始终显示为第一条。

# HISTORY

**list-machines** 子命令将容器和虚拟机管理整合进标准的 systemctl 界面，提供跨主机及其管理的机器的统一监控。

# SEE ALSO

[systemctl](/man/systemctl)(1), [machinectl](/man/machinectl)(1), [systemd-nspawn](/man/systemd-nspawn)(1)
