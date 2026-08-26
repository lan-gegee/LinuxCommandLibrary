# TAGLINE

报告处理器相关统计信息，包括 CPU 利用率

# TLDR

每 2 秒显示一次 **CPU 统计信息**

```mpstat 2```

以 2 秒为间隔显示 **5 次报告**

```mpstat 2 5```

显示**指定处理器**的统计信息

```mpstat -P 0 2 5```

显示**所有处理器**的统计信息

```mpstat -P ALL 2```

显示每个处理器的**中断**统计

```mpstat -I ALL 2```

# SYNOPSIS

**mpstat** [_options_] [_interval_ [_count_]]

# DESCRIPTION

**mpstat** 报告处理器相关统计信息，包括 CPU 利用率、中断以及其他每处理器指标。它可以显示单个处理器的统计信息，也可以显示所有处理器的汇总。

# PARAMETERS

**-A**
> 等价于 -n -u -I ALL -P ALL

**-I {SUM|CPU|SCPU|ALL}**
> 报告中断统计信息

**-n**
> 报告 NUMA 节点分布统计

**-o JSON**
> 以 JSON 格式输出

**-P {processor|ALL}**
> 指定处理器编号或 ALL

**-u**
> 报告 CPU 利用率（默认）

**-V**
> 打印版本号

# OUTPUT FIELDS

**%usr**: 用户态（应用程序）
**%nice**: nice 优先级的用户态
**%sys**: 系统态（内核）
**%iowait**: 等待 I/O
**%irq**: 硬件中断
**%soft**: 软件中断
**%steal**: 被 hypervisor 占用的时间
**%guest**: 运行虚拟处理器的时间
**%gnice**: 运行带 nice 优先级虚拟机的时间
**%idle**: 空闲时间

# CAVEATS

第一次报告显示的是自启动以来的统计。处理器编号从 0 开始。在虚拟机上，%steal 表示被 hypervisor 占用的 CPU 时间。

# HISTORY

**mpstat** 是 **sysstat** 软件包的一部分，为 SMP 系统提供多处理器统计。

# INSTALL

```apt: sudo apt install sysstat```

```dnf: sudo dnf install sysstat```

```pacman: sudo pacman -S sysstat```

```apk: sudo apk add sysstat```

```zypper: sudo zypper install sysstat```

```brew: brew install sysstat```

```nix: nix profile install nixpkgs#sysstat```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sar](/man/sar)(1), [iostat](/man/iostat)(1), [vmstat](/man/vmstat)(8), [top](/man/top)(1)
