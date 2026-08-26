# TAGLINE

显示 OpenRC 服务和运行级状态

# TLDR

**显示**服务及其状态的摘要

```rc-status```

**包含**所有运行级中的服务

```rc-status -a```

**列出**已崩溃的服务

```rc-status -c```

**列出**手动启动的服务

```rc-status -m```

**列出**受监管的服务

```rc-status -S```

**显示**当前运行级

```rc-status -r```

**列出**所有运行级

```rc-status -l```

# SYNOPSIS

**rc-status** [_options_] [_runlevel_]

# PARAMETERS

**-a, --all**
> 显示所有运行级中的全部服务

**-c, --crashed**
> 列出已崩溃的服务

**-l, --list**
> 列出所有已定义的运行级

**-m, --manual**
> 列出手动启动的服务

**-r, --runlevel**
> 显示当前运行级

**-s, --servicelist**
> 显示指定运行级的服务列表

**-S, --supervised**
> 列出受监管的服务

**-u, --unused**
> 列出未分配到任何运行级的服务

# DESCRIPTION

**rc-status** 显示 OpenRC 运行级和服务状态的信息。默认情况下，它会显示当前运行级中的服务及其状态（started、stopped、crashed 等）。

该命令便于系统管理员快速检查哪些服务正在运行、找出崩溃的服务，或者核实当前的运行级配置。

# CAVEATS

仅在以 OpenRC 作为 init 系统的系统（Gentoo、Alpine、Artix 等）上可用。服务状态反映的是 OpenRC 记录的状态；如果服务意外崩溃，该状态可能与实际进程状态不一致。

# INSTALL

```apt: sudo apt install openrc```

```apk: sudo apk add openrc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rc-service](/man/rc-service)(8), [rc-update](/man/rc-update)(8), [openrc](/man/openrc)(8)
