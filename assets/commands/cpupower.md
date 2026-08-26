# TAGLINE

CPU 电源管理与调优工具

# TLDR

**列出**所有 CPU

```sudo cpupower -c all info```

为所有 CPU 设置**省电调频器**

```sudo cpupower -c all frequency-set --governor powersave```

查看 CPU 0 的**可用调频器**

```sudo cpupower -c 0 frequency-info -g | grep "analyzing\|governors"```

获取 CPU 4 的**硬件频率**

```sudo cpupower -c 4 frequency-info -w -m```

# SYNOPSIS

**cpupower** [_-c cpus_] _subcommand_ [_options_]

# DESCRIPTION

**cpupower** 是一组用于 CPU 电源管理和调优的工具。它取代了较旧的 cpufrequtils 软件包，为频率调节、空闲状态和电源特性提供统一的访问入口。

子命令包括 frequency-info、frequency-set、idle-info、idle-set 和 monitor。

# PARAMETERS

**-c, --cpu** _cpus_
> 指定要操作的 CPU（例如 0、1-3、all）

**frequency-info**
> 显示当前频率设置。

**frequency-set**
> 修改频率设置。

**idle-info**
> 显示空闲状态信息。

**idle-set**
> 启用/禁用特定的空闲状态。

**monitor**
> 报告 CPU 频率和空闲驻留统计信息。

**info**
> 显示内核配置和硬件信息。

**-g, --governor**
> 设置频率调频器（配合 frequency-set）或显示可用调频器（配合 frequency-info）。

**-u, --max** _FREQ_
> 设置最大频率（需配合 frequency-set）。

**-d, --min** _FREQ_
> 设置最小频率（需配合 frequency-set）。

**-f, --freq** _FREQ_
> 设置精确频率（需 userspace 调频器）。

**-m, --human**
> 以人类可读的格式输出。

# CAVEATS

设置数值需要 root 权限。可用的调频器和特性取决于硬件与内核配置。取代 cpufreq-info 和 cpufreq-set。

# INSTALL

```apt: sudo apt install linux-cpupower```

```pacman: sudo pacman -S cpupower```

```apk: sudo apk add cpupower```

```zypper: sudo zypper install cpupower```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cpufreq-info](/man/cpufreq-info)(1), [cpufreq-set](/man/cpufreq-set)(1), [turbostat](/man/turbostat)(8)
