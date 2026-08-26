# TAGLINE

多功能资源统计工具

# TLDR

显示 **CPU、磁盘、网络、分页、系统**统计信息

```dstat```

每 **5 秒显示一次，共 4 次**

```dstat 5 4```

只显示 **CPU 和内存**

```dstat -c -m```

**列出**可用插件

```dstat --list```

显示占用**内存和 CPU 最高的进程**

```dstat --top-mem --top-cpu```

显示**电池**信息

```dstat --battery --battery-remain```

# SYNOPSIS

**dstat** [_options_] [_delay_] [_count_]

# DESCRIPTION

**dstat** 是一款多功能的系统资源统计生成器，将 vmstat、iostat、netstat 和 ifstat 的功能统一到一个工具中。它实时监控 CPU、内存、磁盘 I/O、网络、进程及其他系统资源，输出彩色且易读。

该工具的插件架构让监控能力可以扩展到标准指标之外。用户可以通过第三方插件显示 CPU 和内存占用大户、电池信息和自定义统计。输出按可配置的间隔刷新，既适合快速系统检查，也适合持续监控。

dstat 的强项在于能在同一个视图中关联不同子系统的指标。例如，你可以同时监控 CPU 使用率、磁盘 I/O 和网络流量来理解系统瓶颈。

重要提示：dstat 已被弃用且不再维护。其 Python 2 代码库没有为现代系统更新过。用户应考虑替代品，如 dool（一个仍在维护的分叉），或使用持续活跃维护的传统 sysstat 工具（vmstat、iostat、sar）。

# PARAMETERS

**-c, --cpu**
> CPU 统计

**-m, --mem**
> 内存统计

**-d, --disk**
> 磁盘统计

**-n, --net**
> 网络统计

**--top-cpu**
> 占用 CPU 最多的进程

**--top-mem**
> 占用内存最多的进程

**--list**
> 列出可用插件

**-a, --all**
> 等价于 **-cdngy**，即默认集合

**-f, --full**
> 将聚合统计展开为每个 CPU、磁盘或接口一列

**--output** _file_
> 同时将统计写入 CSV 文件

# CAVEATS

**dstat 已被弃用且无人维护。**它为 Python 2 编写，虽然各发行版带着补丁使其在 Python 3 下仍可导入，但在现代系统上出的问题上游无人修复。一些插件完全失效，少数插件在新内核上会崩溃。

直接的替代品是 **dool**——一个维护中的 Python 3 分叉，保留了相同的命令行界面，因此 `dool -cdngy` 的行为与你记忆中的 dstat 一致。此外，sysstat 套件（`vmstat`、`iostat`、`sar`、`pidstat`）覆盖同样的场景并持续维护，代价是过去一条命令的事现在需要几条命令。

另请注意，输出的第一行是自启动以来的平均值而非本次区间的测量值，这是它与 `vmstat` 共有的陷阱：丢弃第一行，或者至少计数两次。

# HISTORY

dstat 由 **Dag Wieers** 于 **2004 年**编写，其卖点很直接：`vmstat`、`iostat`、`netstat` 和 `ifstat` 各自只展示画面的一部分，格式不同、刷新节奏不同，在四个终端之间用肉眼对照简直苦不堪言。dstat 把它们放进一张对齐、色彩标记、可插拔扩展的表格里，并共享同一条时间线——事实证明，这正是排查瓶颈的人们想要的。它对 Python 2 的依赖最终比 Python 2 本身活得更久，项目随后退役，由 **dool** 分叉接棒。

# INSTALL

```apt: sudo apt install pcp```

```dnf: sudo dnf install pcp```

```pacman: sudo pacman -S pcp```

```zypper: sudo zypper install pcp```

```brew: brew install pcp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vmstat](/man/vmstat)(8), [iostat](/man/iostat)(1), [sar](/man/sar)(1), [pidstat](/man/pidstat)(1), [htop](/man/htop)(1)

# RESOURCES

```[Source code](https://github.com/dagwieers/dstat)```

<!-- verified: 2026-07-14 -->
