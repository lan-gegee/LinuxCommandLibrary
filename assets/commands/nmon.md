# TAGLINE

面向系统管理员、调优和基准测试的工具，可监视并显示系统资源

# TLDR

启动**交互式** nmon

```nmon```

按默认设置将记录保存到**文件**

```nmon -f```

以 **30 秒**间隔、**240 次测量**保存

```nmon -f -s 30 -c 240```

启用**容量规划**模式

```nmon -x```

在输出中包含**最占资源的进程**

```nmon -fdt```

# SYNOPSIS

**nmon** [**-h**] [**-s** _seconds_] [**-c** _count_] [**-f** **-d** _disks_ **-t** **-r** _name_] [**-x**]

# DESCRIPTION

**nmon** 是一款面向系统管理员的调优和基准测试工具，用于监视并显示 CPU、内存、网络、磁盘、文件系统、NFS、最占资源的进程以及资源信息。它既可以交互式运行，也可以将数据输出到电子表格兼容的文件中。

# PARAMETERS

**-h**
> 显示完整帮助信息

**-f**
> 启用电子表格输出格式进行文件记录

**-s SECONDS**
> 设置刷新间隔（秒）（默认：2）

**-c COUNT**
> 设置要捕获的刷新次数

**-d DISKS**
> 增加磁盘监视数量（默认：256）

**-t**
> 在电子表格输出中包含最占资源的进程

**-x**
> 启用容量规划模式：1 天内每 15 分钟一次（-fdt -s 900 -c 96）

**-r NAME**
> 设置输出文件的文件名前缀

# CAVEATS

在交互模式下，按 "h" 可查看可用快捷键的帮助。默认的电子表格模式使用 -s300 -c288（每 5 分钟一次，持续 24 小时）。输出文件为 CSV 格式，适合分析工具处理。

# HISTORY

**nmon** 由 IBM 的 Nigel Griffiths 创建，现已成为 Linux 系统上流行的性能监控工具。

# INSTALL

```apt: sudo apt install nmon```

```dnf: sudo dnf install nmon```

```pacman: sudo pacman -S nmon```

```apk: sudo apk add nmon```

```zypper: sudo zypper install nmon```

```nix: nix profile install nixpkgs#nmon```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[top](/man/top)(1), [vmstat](/man/vmstat)(8), [iostat](/man/iostat)(1), [sar](/man/sar)(1)
