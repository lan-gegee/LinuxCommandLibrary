# TAGLINE

查询系统电源和电池信息

# TLDR

显示**电源**信息

```upower -d```

**列出**电源设备

```upower -e```

**监视**电源变化

```upower -m```

以**详细模式**监视

```upower --monitor-detail```

显示**版本**

```upower -v```

# SYNOPSIS

**upower** [_OPTIONS_]

# PARAMETERS

**-d, --dump**
> 显示全部电源和电池信息

**-e, --enumerate**
> 列出所有电源设备

**-m, --monitor**
> 监视电源状态变化

**--monitor-detail**
> 以详细输出进行监视

**-i** _DEVICE_
> 显示指定设备的信息

**-v, --version**
> 显示版本信息

# DESCRIPTION

**upower** 是一款用于查询电源和电池信息及统计数据的系统工具。它与 UPower 守护进程交互，汇报电池电量、供电来源状态以及其他与电源相关的信息。

该工具常用于监控笔记本电池状态和电源管理事件。

# CAVEATS

需要 UPower 守护进程处于运行状态。可用信息取决于硬件支持程度。部分功能依赖 DBus。

# INSTALL

```apt: sudo apt install upower```

```dnf: sudo dnf install upower```

```pacman: sudo pacman -S upower```

```apk: sudo apk add upower```

```zypper: sudo zypper install upower```

```nix: nix profile install nixpkgs#upower```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[acpi](/man/acpi)(1), [tlp-stat](/man/tlp-stat)(1)
