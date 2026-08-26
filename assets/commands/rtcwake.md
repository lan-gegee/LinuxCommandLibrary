# TAGLINE

利用 RTC 闹钟安排系统从睡眠状态唤醒

# TLDR

**查看**闹钟状态

```sudo rtcwake -m show -v```

挂起到**内存**并在 10 秒后唤醒

```sudo rtcwake -m mem -s 10```

挂起到**磁盘**并在 15 分钟后唤醒

```sudo rtcwake -m disk --date +15min```

**冻结**并在指定时间唤醒

```sudo rtcwake -m freeze --date [YYYYMMDDhhmm]```

**禁用**闹钟

```sudo rtcwake -m disable```

**试运行**而不真正挂起

```sudo rtcwake -m mem -s 600 -n```

**列出当前内核支持的唤醒模式**

```rtcwake --list-modes```

# SYNOPSIS

**rtcwake** [_options_] [**-d** _device_] [**-m** _mode_] {**-s** _seconds_ | **-t** _time_t_ | **--date** _timestamp_}

# MODES

**standby**
> ACPI S1 —— 节能有限但确有实效。省略 **-m** 时的默认模式。

**mem**
> 挂起到内存（ACPI S3）。

**disk**
> 挂起到磁盘 / 休眠（ACPI S4）。

**freeze**
> 挂起到空闲（S0ix），需要内核 3.9 及以上版本。

**off**
> 切断系统电源（ACPI S5）。

**no**
> 只设置 RTC 闹钟，既不挂起也不关机。

**on**
> 不进入睡眠；改为轮询 RTC 直到闹钟触发（调试用）。

**show**
> 显示当前设置的闹钟。

**disable**
> 取消尚未触发的闹钟。

# PARAMETERS

**-m**, **--mode** _mode_
> 睡眠/动作模式（参见 **MODES**）。

**-s**, **--seconds** _sec_
> 从现在起 _sec_ 秒后唤醒。

**-t**, **--time** _time_t_
> 在绝对 Unix 时间戳 _time_t_ 时唤醒。

**--date** _timestamp_
> 在给定的时间点唤醒（例如 `+5min`、`2026-04-30 18:00`、`tomorrow 03:00`）。

**-d**, **--device** _rtc_
> 使用指定的 RTC 设备（默认 **/dev/rtc0**）。

**-l**, **--local**
> 将硬件时钟解释为本地时间。

**-u**, **--utc**
> 将硬件时钟解释为 UTC。

**-a**, **--auto**
> 从 **/etc/adjtime** 读取时钟的解释方式（默认）。

**-A**, **--adjfile** _file_
> 使用 _file_ 代替 **/etc/adjtime**。

**-n**, **--dry-run**
> 测试模式 —— 设置好闹钟但不真正挂起或关机。

**--list-modes**
> 打印当前运行的内核所支持的模式。

**-v**, **--verbose**
> 详细输出。

**-V**, **--version**
> 打印版本信息并退出。

# DESCRIPTION

**rtcwake** 让系统进入睡眠状态，并配置 RTC（实时时钟）在指定时刻唤醒系统。它非常适合计划任务、节省电能和自动唤醒等场景。

该工具支持多种睡眠模式，各自在功耗与唤醒速度之间有不同的取舍。RTC 闹钟带有电池后备，即使系统断电也依然有效。

# CAVEATS

需要 root 权限。并非所有硬件都支持所有模式。时间相对于硬件时钟（通常为 UTC）。BIOS/UEFI 必须支持 RTC 唤醒。

# HISTORY

**rtcwake** 属于 **util-linux** 软件包，为 Linux 的 RTC 唤醒功能提供标准接口，可用于定时唤醒和自动化电源管理。

# INSTALL

```apt: sudo apt install util-linux```

```dnf: sudo dnf install util-linux```

```pacman: sudo pacman -S util-linux```

```apk: sudo apk add util-linux-misc```

```zypper: sudo zypper install util-linux```

```brew: brew install util-linux```

```nix: nix profile install nixpkgs#util-linux```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[systemctl](/man/systemctl)(1), [hwclock](/man/hwclock)(8), [pm-suspend](/man/pm-suspend)(8)
