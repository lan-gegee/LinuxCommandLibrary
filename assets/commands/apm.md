# TAGLINE

查询高级电源管理状态和电池信息。

# TLDR

**显示** APM 状态（电源/电池）

```apm```

显示**详细**状态

```apm -v```

以**分钟数**显示电池剩余时间

```apm -m```

**持续监控**并更新状态

```apm -M```

**挂起**系统

```sudo apm -s```

# SYNOPSIS

**apm** [_-VvmMsSdin_]

# DESCRIPTION

**apm** 查询 Linux 系统上的高级电源管理（APM）状态。它报告电池电量、交流适配器状态和电源管理能力。

APM 在现代系统上已在很大程度上被 ACPI 取代，但出于兼容性或在旧硬件上，该命令可能仍然可用。

# PARAMETERS

**-V**, **--version**
> 打印程序版本后退出。

**-v**, **--verbose**
> 额外打印 APM 子系统的版本信息。

**-m**, **--minutes**
> 以分钟数而不是 hh:mm 的形式打印剩余时间。

**-M**, **--monitor**
> 持续监控并更新状态信息。

**-s**, **--suspend**
> 请求机器进入 APM 挂起状态。

**-S**, **--standby**
> 请求机器进入 APM 待机状态。

**-d**, **--debug**
> 以更适合调试的格式打印 APM 状态信息。

# CAVEATS

现代系统上 APM 已被弃用，由 ACPI 取代。在仅支持 ACPI 的系统上功能可能受限或不可用。在现代硬件上请使用 **acpi** 命令。

# HISTORY

在 ACPI（Advanced Configuration and Power Interface）于 **21 世纪初**中期成为主流之前，**apm** 是 Linux 的标准电源管理接口。该命令保留至今是为了兼容旧系统。

# SEE ALSO

[acpi](/man/acpi)(1), [upower](/man/upower)(1), [powertop](/man/powertop)(8)
