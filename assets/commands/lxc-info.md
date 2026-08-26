# TAGLINE

显示 Linux 容器的信息，包括状态、PID、IP 地址等

# TLDR

获取容器**信息**

```sudo lxc-info [container_name]```

显示**帮助**

```lxc-info --help```

# SYNOPSIS

**lxc-info** **-n** _name_ [_options_]

# DESCRIPTION

**lxc-info** 显示 Linux 容器的信息，包括其状态、PID、IP 地址以及 CPU 和内存使用情况。

# PARAMETERS

**-n, --name NAME**
> 容器名称

**-s, --state**
> 仅显示状态

**-p, --pid**
> 仅显示 PID

**-i, --ips**
> 仅显示 IP 地址

**-c, --config KEY**
> 显示指定的配置项值

**-S, --stats**
> 显示使用统计信息

**-?, --help**
> 显示帮助信息

# OUTPUT

**Name**: 容器名称
**State**: RUNNING、STOPPED、FROZEN
**PID**: 容器 init 进程的 PID
**IP**: IP 地址
**CPU use**: CPU 使用率
**Memory use**: 内存使用量

# INSTALL

```apt: sudo apt install lxc```

```dnf: sudo dnf install lxc```

```pacman: sudo pacman -S lxc```

```apk: sudo apk add lxc```

```zypper: sudo zypper install lxc```

```brew: brew install lxc```

```nix: nix profile install nixpkgs#lxc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lxc-ls](/man/lxc-ls)(1), [lxc-start](/man/lxc-start)(1), [lxc-attach](/man/lxc-attach)(1)
