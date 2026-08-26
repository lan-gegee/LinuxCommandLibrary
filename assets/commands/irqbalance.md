# TAGLINE

在多个 CPU 之间分配硬件中断

# TLDR

**启动 irqbalance**

```sudo irqbalance```

**在前台运行**

```sudo irqbalance --foreground```

**一次性均衡**

```sudo irqbalance --oneshot```

**调试模式**

```sudo irqbalance --debug```

**禁止特定 IRQ**

```sudo irqbalance --banirq=[irq_num]```

# SYNOPSIS

**irqbalance** [_options_]

# PARAMETERS

**--foreground**
> 在前台运行。

**--oneshot**
> 均衡一次后退出。

**--debug**
> 启用调试输出。

**--banirq** _IRQ_
> 将 IRQ 排除在均衡之外。

**--policyscript** _SCRIPT_
> 自定义放置策略。

**--pid** _FILE_
> PID 文件位置。

**--help**
> 显示帮助信息。

# DESCRIPTION

**irqbalance** 在多个 CPU 之间分配硬件中断。它为多处理器系统优化中断处理。

该守护进程监控 IRQ 模式并迁移中断以实现更好的负载分布。它可提升多核系统的性能。

# CAVEATS

以守护进程方式运行。可能与手动设置的 IRQ 亲和性冲突。仅限 Linux。

# HISTORY

irqbalance 的创建目的是自动在多个 CPU 之间均衡 IRQ 负载，取代手动配置 smp_affinity 的做法。

# INSTALL

```apt: sudo apt install irqbalance```

```dnf: sudo dnf install irqbalance```

```pacman: sudo pacman -S irqbalance```

```apk: sudo apk add irqbalance```

```zypper: sudo zypper install irqbalance```

```nix: nix profile install nixpkgs#irqbalance```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cpupower](/man/cpupower)(1), [taskset](/man/taskset)(1)
