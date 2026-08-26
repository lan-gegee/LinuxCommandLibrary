# TAGLINE

测量系统功耗统计信息

# TLDR

以**默认设置**测量功耗

```powerstat```

以自定义的**间隔和采样数**测量

```powerstat [10] [20]```

使用 **RAPL** 接口

```powerstat -R [10] [20]```

显示**直方图**

```powerstat -H [10] [20]```

启用**全部**统计项

```powerstat -a [10] [20]```

# SYNOPSIS

**powerstat** [**-a**] [**-H**] [**-R**] [_interval_] [_samples_]

# PARAMETERS

**interval**
> 两次测量之间的秒数（默认：10）

**samples**
> 测量次数（默认：10）

**-a**
> 启用所有统计信息的收集

**-H**
> 显示测量结果的直方图

**-R**
> 使用 Intel RAPL 接口而不是电池

**-d**
> 显示分布统计

**-z**
> 显示零负载/空闲功耗估计值

# DESCRIPTION

**powerstat** 通过电池放电速率或 Intel 的 RAPL（Running Average Power Limit）接口测量系统功耗。它提供随时间变化的功耗统计分析。

该工具适用于评估应用、内核设置或硬件配置在笔记本电脑和服务器上的能效表现。

# CAVEATS

电池模式要求系统由电池供电。RAPL 需要 Intel CPU 支持 RAPL。测量结果可能因系统负载而异。为获得准确结果请多次采样。

# HISTORY

**powerstat** 由 **Colin Ian King** 编写，是其电源管理测试工具的一部分。它常用于 Ubuntu 的电源测试与优化工作中。

# INSTALL

```apt: sudo apt install powerstat```

```dnf: sudo dnf install powerstat```

```zypper: sudo zypper install powerstat```

```nix: nix profile install nixpkgs#powerstat```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[powertop](/man/powertop)(8), [turbostat](/man/turbostat)(8), [cpupower](/man/cpupower)(1)
