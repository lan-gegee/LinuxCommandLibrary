# TAGLINE

挂起和休眠你的计算机

# TLDR

**挂起到内存（S3 睡眠状态）**

```sudo pm-suspend```

**休眠到磁盘（S4 睡眠状态）**

```sudo pm-hibernate```

**混合挂起（先保存到磁盘再挂起到内存）**

```sudo pm-suspend-hybrid```

**检查是否支持挂起**

```pm-is-supported --suspend && echo "Supported"```

**检查是否支持休眠**

```pm-is-supported --hibernate && echo "Supported"```

**启用省电模式**

```sudo pm-powersave true```

# SYNOPSIS

**pm-suspend** | **pm-hibernate** | **pm-suspend-hybrid** [_options_]

# PARAMETERS

**--quirk-dpms-on**
> 恢复后强制开启 DPMS。

**--quirk-vbe-post**
> 唤醒时重新 POST 视频 BIOS。

**--quirk-vbestate-restore**
> 在挂起/恢复时保存和恢复 VBE 状态。

**--quirk-vbemode-restore**
> 在挂起/恢复时保存和恢复 VBE 模式。

**--quirk-radeon-off**
> 使用 Radeon 显示芯片挂起时关闭屏幕。

**--quirk-s3-bios**
> 挂起时使用 S3 BIOS 模式。

**--quirk-s3-mode**
> 挂起时使用 S3 模式。

# DESCRIPTION

**pm-utils** 是一组 Linux 电源管理工具。它提供挂起、休眠和省电的框架，并支持硬件 quirk。

**pm-suspend** 让系统进入 S3（挂起到内存）。大多数设备被关闭，系统状态保存在 RAM 中，需要持续供电。大多数系统进出挂起状态只需 3 到 5 秒。

**pm-hibernate** 让系统进入 S4（休眠到磁盘）。系统完全断电，状态保存到交换分区。系统可以无限期保持休眠而不耗电。

**pm-suspend-hybrid** 先像休眠一样把状态存入磁盘，然后挂起到内存。供电正常时唤醒更快，断电时则可以从磁盘恢复。

**pm-is-supported** 测试系统是否支持给定的睡眠模式（退出码 0 表示支持）。

**pm-powersave** 启用或禁用省电模式。`/etc/pm/sleep.d/` 和 `/etc/pm/power.d/` 中的钩子脚本会在状态切换时执行，允许在挂起、恢复、休眠和解冻事件上执行自定义操作。

# CAVEATS

已被 systemd 取代（systemd 系统请使用 `systemctl suspend` 或 `systemctl hibernate`）。非 systemd 系统仍在使用。需要 ACPI 支持。休眠需要至少与内存一样大的交换分区。

# HISTORY

**pm-utils** 由 **Peter Jones** 为 **Fedora** 开发，随后被其他 Linux 发行版采纳为标准电源管理接口。它提供了基于钩子的框架来处理挂起/恢复期间的硬件 quirks。随着 systemd 的普及，pm-utils 已基本被 systemd 内置的电源管理取代。

# INSTALL

```aur: yay -S pm-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[systemctl](/man/systemctl)(1), [rtcwake](/man/rtcwake)(8), [acpid](/man/acpid)(8)
