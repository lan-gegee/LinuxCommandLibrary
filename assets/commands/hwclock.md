# TAGLINE

读取和设置硬件时钟（一种由电池供电的时钟）

# TLDR

显示硬件时钟的**当前时间**

```sudo hwclock```

将**系统时间写入硬件**时钟

```sudo hwclock -w```

将**硬件时间写入系统**时钟

```sudo hwclock -s```

将**硬件时钟设置**为指定时间

```sudo hwclock --set --date="2025-01-15 14:30:00"```

将硬件时钟设为 **UTC 模式**

```sudo hwclock --systohc --utc```

将硬件时钟设为**本地时间**模式（用于与 Windows 双启动）

```sudo hwclock --systohc --localtime```

# SYNOPSIS

**hwclock** [_options_]

# PARAMETERS

**-r**, **--show**
> 读取并显示硬件时钟时间

**-w**, **--systohc**
> 根据系统时间设置硬件时钟

**-s**, **--hctosys**
> 根据硬件时钟设置系统时间

**--set** **--date=**_TIME_
> 将硬件时钟设置为指定时间

**--localtime**
> 硬件时钟使用本地时间

**--utc**
> 硬件时钟使用 UTC

**--adjust**
> 校正系统性漂移

**--verbose**
> 显示 hwclock 正在执行操作的详细信息

**--test**
> 试运行；显示将要执行的操作但不修改任何内容

**-f**, **--rtc** _FILE_
> 使用指定的 RTC 设备（默认：/dev/rtc0）

# DESCRIPTION

**hwclock** 读取并设置硬件时钟（Real-Time Clock/RTC），这是一种由电池供电、在系统断电时仍维持时间的时钟。

硬件时钟可以设为 UTC 或本地时间。Linux 系统通常让硬件时钟使用 UTC，并在显示时转换为本地时间。与 Windows 双启动的系统可能需要硬件时钟使用本地时间，因为 Windows 预期如此。

在启动过程中，系统通常会运行 **hwclock --hctosys** 以根据硬件时钟初始化系统时间，随后 NTP 会校正任何漂移。

# CAVEATS

需要 root 权限。Windows 和 Linux 对 RTC 时区的预期不同——Linux 倾向于 UTC，Windows 倾向于本地时间。在虚拟化系统上，硬件时钟可能是模拟的。现代系统通常使用 systemd-timesyncd 或 NTP 来管理时间。

# HISTORY

自 Linux 早期以来，hwclock 一直是管理硬件时钟的标准 Linux 工具。它属于 util-linux 软件包，取代了 clock 等更早的工具。

# INSTALL

```apt: sudo apt install util-linux-extra```

```apk: sudo apk add util-linux-misc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[timedatectl](/man/timedatectl)(1), [date](/man/date)(1), [ntpd](/man/ntpd)(1), [chrony](/man/chrony)(1)
