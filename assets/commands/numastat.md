# TAGLINE

显示 NUMA 系统的内存统计信息

# TLDR

**显示 NUMA 统计信息**

```numastat```

**显示每个进程的 NUMA 内存**

```numastat -p [pid]```

**显示每节点内存信息**

```numastat -m```

**显示紧凑输出**

```numastat -c```

**显示某命令的统计信息**

```numastat -p $(pgrep [process_name])```

# SYNOPSIS

**numastat** [_options_] [_pattern_|_pid_...]

# PARAMETERS

**-p** _pid_
> 显示按进程的统计信息。

**-m**
> 显示内存信息。

**-c**
> 紧凑输出。

**-n**
> 显示原始格式。

**-s** _node_
> 按节点排序。

**-z**
> 跳过零值。

# DESCRIPTION

**numastat** 显示 NUMA（非一致性内存访问）系统的内存统计信息，包括每节点的内存分配、命中数、未命中数以及进程内存分布。

理解 NUMA 统计信息有助于优化多路（multi-socket）系统上的应用程序性能。

# STATISTICS EXPLAINED

```
numa_hit   - Allocation on intended node
numa_miss  - Allocation on different node
numa_foreign - Other node allocations here
interleave_hit - Interleave policy success
local_node - Local allocations
other_node - Remote allocations
```

# EXAMPLE OUTPUT

```
                 node0       node1
numa_hit        1234567      987654
numa_miss           100         200
local_node      1234467      987454
other_node          100         200
```

# CAVEATS

仅在 NUMA 系统上有意义。统计自系统启动起累计。需要 /sys/devices/system/node/。

# HISTORY

numastat 属于 **numactl** 软件包，提供类似于原始 SGI IRIX numastat 命令的 NUMA 统计功能。

# INSTALL

```apt: sudo apt install numactl```

```dnf: sudo dnf install numactl```

```pacman: sudo pacman -S numactl```

```apk: sudo apk add numactl-tools```

```zypper: sudo zypper install numactl```

```brew: brew install numactl```

```nix: nix profile install nixpkgs#numactl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[numactl](/man/numactl)(8), [migratepages](/man/migratepages)(8)
