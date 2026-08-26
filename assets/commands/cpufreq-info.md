# TAGLINE

显示 CPU 频率调节信息

# TLDR

显示**所有 CPU** 的频率信息

```cpufreq-info```

显示**指定 CPU** 的信息

```cpufreq-info -c 0```

显示**硬件限制**（最小/最大频率）

```cpufreq-info -l```

以表格形式显示当前**策略**

```cpufreq-info -o```

显示可用的 **governor**

```cpufreq-info -g```

显示**当前频率**（人类可读格式）

```cpufreq-info -f -m```

从**硬件**读取频率（仅限 root）

```sudo cpufreq-info -w -m```

显示正在使用的**驱动**

```cpufreq-info -d```

# SYNOPSIS

**cpufreq-info** [_options_]

# DESCRIPTION

**cpufreq-info** 是一个从内核打印 CPU 频率调节信息的实用工具。它显示当前频率、可用的 governor、硬件限制以及其他与 cpufreq 相关的数据。

# PARAMETERS

**-c, --cpu CPU**
> 针对指定的处理器编号

**-f, --freq**
> 显示内核报告的当前 CPU 频率

**-w, --hwfreq**
> 直接从硬件读取当前频率（仅限 root）

**-l, --hwlimits**
> 显示硬件频率的上下限

**-d, --driver**
> 显示当前启用的 cpufreq 内核驱动

**-p, --policy**
> 显示当前的频率调节策略

**-g, --governors**
> 列出可用的频率 governor

**-a, --related-cpus**
> 显示共享相同硬件频率的 CPU

**-s, --stats**
> 显示频率调节统计信息

**-y, --latency**
> 显示频率切换的最大延迟

**-o, --proc**
> 以 /proc/cpufreq 格式显示设置

**-m, --human**
> 以人类可读的形式格式化输出（用于 -f、-w、-s、-y）

# CAVEATS

一次调用中不能组合多个输出类选项。-w 选项需要 root 权限才能直接从硬件读取频率。-o 选项与 -c 不兼容。

# HISTORY

**cpufreq-info** 是 **cpufrequtils** 软件包的一部分，为 Linux CPU 频率调节提供用户态工具。

# INSTALL

```apk: sudo apk add cpufrequtils```

```nix: nix profile install nixpkgs#cpufrequtils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cpufreq-set](/man/cpufreq-set)(1), [cpupower](/man/cpupower)(1), [auto-cpufreq](/man/auto-cpufreq)(1)

# RESOURCES

```[Source code](https://git.kernel.org/pub/scm/utils/kernel/cpufreq/cpufrequtils.git/)```

<!-- verified: 2026-06-23 -->
