# TAGLINE

对 HWInfo 实时硬件传感器数据进行终端可视化

# TLDR

从 CSV 文件**交互式监控传感器**

```hwinfo-tui monitor [sensors.csv] "[sensor_name]"```

**监控多个传感器**

```hwinfo-tui monitor [sensors.csv] "[CPU Temperature]" "[GPU Temperature]"```

设置自定义**刷新率**

```hwinfo-tui monitor --refresh [0.5] [sensors.csv] "[sensor_name]"```

设置**历史窗口**时长

```hwinfo-tui monitor --history [600] [sensors.csv] "[sensor_name]"```

# SYNOPSIS

**hwinfo-tui** **monitor** [**--refresh** _seconds_] [**--history** _seconds_] _csv_file_ _sensor_names_...

# DESCRIPTION

**hwinfo-tui** 是一个终端可视化工具，用于监控来自 **HWInfo64** 的实时硬件传感器数据。它受 **gping** 启发，提供一个整洁的 TUI，带有交互式图表和统计表，显示每个被监控传感器的最小值、最大值、平均值和 95 百分位数值。

该工具支持带建议的模糊传感器名匹配、可配置的刷新率（0.1-60 秒）以及可调整的历史窗口（10-7200 秒）。它读取由 HWInfo64 导出的 CSV 文件中的传感器数据。

# CAVEATS

**HWInfo64** 仅在 Windows 上可用；在其他平台上，你可以使用预先导出的 CSV 文件来使用本工具。需要 Python 3。内存占用随历史窗口大小和被监控传感器数量而增加。

# HISTORY

**hwinfo-tui** 由 **Juanjo Fuchs** 创建，用 **Python** 编写。其设计灵感来自 gping 的视觉风格，旨在把硬件监控带入终端。

# INSTALL

```apt: sudo apt install hwinfo```

```dnf: sudo dnf install hwinfo```

```pacman: sudo pacman -S hwinfo```

```apk: sudo apk add hwinfo```

```zypper: sudo zypper install hwinfo```

```nix: nix profile install nixpkgs#hwinfo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sensors](/man/sensors)(1), [htop](/man/htop)(1)
