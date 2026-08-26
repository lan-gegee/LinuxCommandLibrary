# TAGLINE

TLP 电源管理状态报告

# TLDR

生成**完整**状态报告

```sudo tlp-stat```

显示**电池**信息

```sudo tlp-stat -b```

显示**处理器**可调参数

```sudo tlp-stat -p```

显示**磁盘**设备可调参数

```sudo tlp-stat -d```

显示**配置**

```sudo tlp-stat -c```

显示与默认值的**配置差异**

```sudo tlp-stat --cdiff```

显示**温度**和风扇转速

```sudo tlp-stat -t```

显示**系统**信息和 TLP 状态

```sudo tlp-stat -s```

监控电源供电的 **udev 事件**

```sudo tlp-stat -P```

# SYNOPSIS

**tlp-stat** [_OPTIONS_]

# PARAMETERS

**-b, --battery**
> 电池数据

**-c, --config**
> 当前生效的配置

**--cdiff**
> 默认值与用户配置之间的差异

**-d, --disk**
> 磁盘设备可调参数

**-e, --pcie**
> PCIe 设备可调参数

**-g, --graphics**
> 显卡可调参数

**-p, --processor**
> 处理器可调参数

**-r, --rfkill**
> 无线设备状态和可调参数

**-s, --system**
> 系统信息和 TLP 状态

**-t, --temp**
> 温度和风扇转速

**-u, --usb**
> USB 设备可调参数

**-v, --verbose**
> 在支持的类别中显示更多细节

**-q, --quiet**
> 省略版本头并精简处理器输出

**-P, --pev**
> 监控电源供电 udev 事件

**--psup**
> 电源诊断

**-T, --trace**
> 跟踪输出

**--udev**
> 检查 udev 规则是否已激活

**-w, --warn**
> 关于 SATA 磁盘的警告

**--version**
> 打印 TLP 版本

# DESCRIPTION

**tlp-stat** 为 TLP 电源管理生成状态报告。它显示当前生效的设置、电池健康度、功耗和硬件状态。其输出有助于诊断电源问题并验证 TLP 配置。

# CAVEATS

部分信息需要 root 权限。并非所有硬件都提供电池统计信息。需要详细诊断时请使用详细模式。一些选项（如 --cdiff、--version 和 -q）需要 TLP 1.7 或更高版本。

# HISTORY

**tlp-stat** 是 **TLP** 的配套诊断工具，由 **Thomas Koch** 创建，用于监控和排查 Linux 笔记本的电源管理问题。

# INSTALL

```dnf: sudo dnf install tlp```

```pacman: sudo pacman -S tlp```

```apk: sudo apk add tlp```

```zypper: sudo zypper install tlp```

```nix: nix profile install nixpkgs#tlp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tlp](/man/tlp)(8), [powertop](/man/powertop)(8), [rfkill](/man/rfkill)(8)
