# TAGLINE

报告 CPU 频率、功耗和空闲统计信息

# TLDR

每 5 秒**显示**一次统计信息

```sudo turbostat```

每隔指定秒数**显示**一次统计信息

```sudo turbostat -i [n_seconds]```

**显示**统计信息但不输出表头

```sudo turbostat --quiet```

对特定 CPU 每秒**显示**一次有用的信息

```sudo turbostat --quiet -i 1 --cpu 0-[CPU_count] --show "PkgWatt","Busy%","Core","CoreTmp"```

# SYNOPSIS

**turbostat** [_options_] [_command_...]

# PARAMETERS

**-i, --interval _seconds_**
> 采样间隔（默认：5 秒）

**--quiet**
> 不打印系统配置表头

**--cpu _list_**
> 指定要监控的 CPU

**--show _columns_**
> 选择要显示的列

**--hide _columns_**
> 隐藏指定的列

**--out _file_**
> 将输出写入文件

**--debug**
> 启用调试输出

# DESCRIPTION

**turbostat** 报告 Intel 和 AMD 处理器的拓扑结构、频率、温度、功耗和空闲统计信息。它读取硬件性能计数器和型号专用寄存器（MSR）。

该工具有助于了解负载下的 CPU 行为、发现热节流现象以及分析功耗。它会显示每个核心和每个封装（package）的统计数据。

# CAVEATS

需要 root 权限和访问 MSR（Model Specific Registers）的权限。在 Intel 处理器上效果最佳；AMD 支持程度不一。某些功能需要特定的 CPU 型号。属于 Linux 内核工具。

# INSTALL

```apt: sudo apt install linux-cpupower```

```pacman: sudo pacman -S cpupower```

```apk: sudo apk add cpupower```

```zypper: sudo zypper install cpupower```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cpupower](/man/cpupower)(1), [lscpu](/man/lscpu)(1), [sensors](/man/sensors)(1), [powertop](/man/powertop)(8)
