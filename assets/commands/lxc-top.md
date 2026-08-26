# TAGLINE

以类似 top 监视进程的方式显示 LXC 容器的实时资源使用情况

# TLDR

启动 **lxc-top**

```lxc-top```

设置刷新**间隔**

```lxc-top --delay 5```

按条件**排序**

```lxc-top --sort [n|c|b|m|k]```

# SYNOPSIS

**lxc-top** [_options_]

# DESCRIPTION

**lxc-top** 以类似 top 监视进程的方式显示 LXC 容器的实时资源使用情况。它展示所有运行中容器的 CPU、内存和 I/O 统计信息。

# PARAMETERS

**-d, --delay SECONDS**
> 刷新间隔（默认：3）

**-s, --sort CRITERIA**
> 排序依据：n(名称)、c(CPU)、b(块设备 I/O)、m(内存)、k(内核内存)

**-r, --reverse**
> 反转排序顺序

**-?, --help**
> 显示帮助信息

# DISPLAY COLUMNS

**Container**: 容器名称
**CPU**: CPU 使用率百分比
**MemUse**: 内存使用量
**MemLim**: 内存上限
**BLKIO**: 块设备 I/O 统计

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

[lxc-info](/man/lxc-info)(1), [lxc-ls](/man/lxc-ls)(1), [top](/man/top)(1)
