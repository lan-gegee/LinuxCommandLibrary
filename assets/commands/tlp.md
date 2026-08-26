# TAGLINE

高级笔记本电源管理

# TLDR

**启动**并根据当前电源应用电源设置

```sudo tlp start```

无论当前电源如何，均应用**电池**配置方案

```sudo tlp bat```

无论当前电源如何，均应用 **AC** 配置方案

```sudo tlp ac```

为所有设备启用 **USB 自动挂起**

```sudo tlp usb```

显示用于配置的**磁盘设备 ID**

```sudo tlp diskid```

# SYNOPSIS

**tlp** _COMMAND_

# COMMANDS

**start**
> 根据当前电源应用设置

**bat**
> 应用电池配置方案（忽略实际电源）

**ac**
> 应用 AC 配置方案（忽略实际电源）

**usb**
> 启用 USB 设备自动挂起

**diskid**
> 显示用于配置的磁盘 ID

# DESCRIPTION

**tlp** 是一款面向 Linux 的高级电源管理工具，用于优化笔记本电脑的电池续航。它在电池供电时自动应用省电设置，在接通交流电时自动应用性能设置。

设置在 `/etc/tlp.conf` 中配置，涵盖 CPU 频率、磁盘停转、USB 自动挂起、WiFi 省电等内容。

# CONFIGURATION

**/etc/tlp.conf**
> 主配置文件，定义 AC 和电池模式的电源配置方案，涵盖 CPU 调频器、磁盘设置、USB 自动挂起、WiFi 省电等。

**/etc/tlp.d/*.conf**
> 用于模块化覆盖的下沉式配置目录。

# CAVEATS

可能与其他电源管理工具冲突。某些设置需要特定的硬件支持。在新硬件上请谨慎测试设置。使用 `tlp-stat` 查看当前状态。

# HISTORY

**TLP** 由 **Thomas Koch**（linrunner）创建，旨在为 Linux 笔记本提供全面的电源管理而无需手动配置。

# INSTALL

```dnf: sudo dnf install tlp```

```pacman: sudo pacman -S tlp```

```apk: sudo apk add tlp```

```zypper: sudo zypper install tlp```

```nix: nix profile install nixpkgs#tlp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tlp-stat](/man/tlp-stat)(8), [powertop](/man/powertop)(8)
