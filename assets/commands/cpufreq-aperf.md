# TAGLINE

利用硬件计数器计算 CPU 实际频率

# TLDR

开始为**所有 CPU** 计算，间隔 1 秒

```sudo cpufreq-aperf```

为**指定 CPU** 计算

```sudo cpufreq-aperf -c [1]```

将**刷新间隔**设为 3 秒

```sudo cpufreq-aperf -i [3]```

只计算**一次**

```sudo cpufreq-aperf -o```

# SYNOPSIS

**cpufreq-aperf** [_options_]

# DESCRIPTION

**cpufreq-aperf** 使用 APERF/MPERF MSR 寄存器计算一段时间内的平均 CPU 频率。它给出的是实际运行频率，而非请求设置的频率。

可用于验证 CPU 频率调节和睿频加速行为是否正常。

# PARAMETERS

**-c, --cpu** _cpu_
> 要监视的特定 CPU

**-i, --interval** _seconds_
> 刷新间隔（秒）

**-o, --once**
> 只计算一次然后退出

# CAVEATS

需要 root 权限。仅支持带 APERF/MPERF 计数器的 CPU（Intel 和 AMD 处理器）。属于 cpufrequtils 的一部分。

# INSTALL

```apk: sudo apk add cpufrequtils```

```nix: nix profile install nixpkgs#cpufrequtils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cpufreq-info](/man/cpufreq-info)(1), [cpufreq-set](/man/cpufreq-set)(1), [cpupower](/man/cpupower)(1)

# RESOURCES

```[Source code](https://git.kernel.org/pub/scm/utils/kernel/cpufreq/cpufrequtils.git/)```

<!-- verified: 2026-06-23 -->
