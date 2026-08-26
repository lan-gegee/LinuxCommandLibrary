# TAGLINE

报告虚拟内存与系统统计信息

# TLDR

显示**虚拟内存**统计信息

```vmstat```

每 **2 秒**显示一次报告，共 5 次

```vmstat 2 5```

显示**活动/非活动**内存

```vmstat -a```

显示**磁盘**统计信息

```vmstat -d```

显示 **slab** 信息

```vmstat -m```

显示**事件计数器**和内存统计

```vmstat -s```

带**时间戳**显示

```vmstat -t 1```

# SYNOPSIS

**vmstat** [_options_] [_delay_ [_count_]]

# DESCRIPTION

**vmstat** 报告有关进程、内存、分页、块 IO、陷阱、磁盘和 CPU 活动的信息。第一份报告显示自启动以来的平均值；后续报告显示采样期间内的活动情况。

# PARAMETERS

**-a, --active**
> 显示活动内存和非活动内存

**-f, --forks**
> 显示自启动以来的 fork 次数

**-m, --slabs**
> 显示 slab 信息

**-s, --stats**
> 显示事件计数器和内存统计信息

**-d, --disk**
> 报告磁盘统计信息

**-D, --disk-sum**
> 报告磁盘统计摘要

**-p, --partition DEVICE**
> 详细的分区统计信息

**-n, --one-header**
> 只打印一次表头

**-t, --timestamp**
> 在每行末尾附加时间戳

**-w, --wide**
> 宽输出模式

**-y, --no-first**
> 省略第一份报告（启动统计）

**-S, --unit UNIT**
> 切换输出单位（k、K、m、M）

# OUTPUT FIELDS

**Procs**：r（可运行）、b（阻塞）
**Memory**：swpd、free、buff、cache
**Swap**：si（换入）、so（换出）
**IO**：bi（读入的块）、bo（写出的块）
**System**：in（中断）、cs（上下文切换）
**CPU**：us（用户态）、sy（系统态）、id（空闲）、wa（等待）、st（被窃取）

# CAVEATS

第一份报告显示自启动以来的平均值。使用 **-y** 可将其省略。对于大内存系统，建议使用宽输出模式（**-w**）。

# HISTORY

**vmstat** 属于 **procps-ng**，自早期 Unix 系统起就提供虚拟内存统计功能。

# INSTALL

```apt: sudo apt install procps```

```dnf: sudo dnf install procps-ng```

```pacman: sudo pacman -S procps-ng```

```apk: sudo apk add procps-ng```

```zypper: sudo zypper install procps```

```brew: brew install procps```

```nix: nix profile install nixpkgs#procps```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[free](/man/free)(1), [iostat](/man/iostat)(1), [mpstat](/man/mpstat)(1), [ps](/man/ps)(1), [top](/man/top)(1)
