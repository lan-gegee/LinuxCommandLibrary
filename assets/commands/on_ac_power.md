# TAGLINE

检测系统是否由交流电源供电

# TLDR

**检查是否使用交流电源**

```on_ac_power && echo "AC" || echo "Battery"```

**在脚本中按条件使用**

```on_ac_power && backup.sh```

**检查退出码**

```on_ac_power; echo $?```

# SYNOPSIS

**on_ac_power**

# EXIT CODES

**0**
> 系统使用交流电源。

**1**
> 系统使用电池供电。

**255**
> 无法确定电源状态。

# DESCRIPTION

**on_ac_power** 检测系统是否由交流（市电）电源供电，并返回指示电源状态的退出码。

该工具专为脚本设计。退出码 0 表示已连接交流电源。退出码 1 表示正在使用电池。其他任何退出码均表示无法确定电源状态。

常见用途包括：只在接通电源时调度重负载任务、根据电源调整备份频率，以及具备电源感知能力的 cron 作业。

该命令会检查包括 ACPI、APM 和 sysfs 在内的多种电源子系统来确定状态。它适用于笔记本电脑和配备备用电池的系统。

在没有电池或没有电源状态信息的系统上，结果可能不可靠。

# CAVEATS

并非在所有系统上都可用。不带 UPS 的台式机通常返回 "AC"。结果取决于内核的电源上报情况。某些虚拟机会报告状态未知。

# HISTORY

**on_ac_power** 属于 Debian 系系统的 **powermgmt-base** 软件包。它为电源感知脚本提供了简单接口，无需直接解析 ACPI 或 sysfs。

# INSTALL

```apk: sudo apk add pm-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[acpi](/man/acpi)(1), [upower](/man/upower)(1), [tlp](/man/tlp)(8), [pm-utils](/man/pm-utils)(8)
