# TAGLINE

交互式电池监控工具

# TLDR

显示**电池**信息

```battop```

使用 **SI** 单位代替人类可读的数值

```battop -u si```

将**刷新间隔**设为 5 秒

```battop -d 5```

# SYNOPSIS

**battop** [**-u** _units_] [**-d** _delay_] [**-v**]

# DESCRIPTION

**battop** 是一个系统电池的交互式查看器。它在终端界面中实时显示电池状态、电量、容量和功耗信息，并随时间绘制图表。当存在多块电池时，可用左右方向键在电池之间切换。

它可运行于 Linux、macOS、FreeBSD 和 DragonFlyBSD。

# PARAMETERS

**-u, --units** _units_
> 显示的度量单位：**human**（默认）或 **si**。

**-d, --delay** _seconds_
> 更新间隔，以秒为单位（默认 **1**）。

**-v, --verbose**
> 提高输出详细程度，最多可重复五次（**-vvvvv**）。日志输出到 stderr。

# KEYBINDINGS

- **Left / Right arrows** - 在电池之间切换
- **q** - 退出

# CAVEATS

在 Linux 上，它从 /sys/class/power_supply 读取电池信息，因此只能在有电池的系统（笔记本、平板）上工作。信息准确性取决于电池硬件报告的内容。

# HISTORY

**battop** 由 svartalf 使用 Rust 编写，提供现代化的跨平台电池监控界面。

# INSTALL

```aur: yay -S battop```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[acpi](/man/acpi)(1), [upower](/man/upower)(1)

# RESOURCES

```[Source code](https://github.com/svartalf/rust-battop)```

<!-- verified: 2026-06-19 -->
