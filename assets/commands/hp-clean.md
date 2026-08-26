# TAGLINE

面向 HPLIP 支持的 HP 喷墨打印机的打印头清洁工具

# TLDR

为默认打印机**清洁打印头**（打开交互式清洁向导）

```hp-clean```

按队列名称**清洁指定的 CUPS 打印机**

```hp-clean -p [printer-name]```

按设备 URI **清洁打印机**

```hp-clean -d [device-uri]```

**以交互方式运行**，在提示时选择清洁级别（1-3）

```hp-clean -i```

**启用调试级别日志**以便排查问题

```hp-clean -g```

# SYNOPSIS

**hp-clean** [_DEVICE-URI_|_PRINTER-NAME_] [_MODE_] [_OPTIONS_]

# PARAMETERS

**-d** _device-uri_, **--device**=_device-uri_
> 按 CUPS 设备 URI 指定目标打印机。

**-p** _printer_, **--printer**=_printer_
> 按 CUPS 队列名称指定目标打印机。

**-i**, **--interactive**
> 以交互模式运行。

**-l** _level_, **--logging**=_level_
> 设置日志详细程度：none、info（默认）、error、warn 或 debug。

**-g**
> 以调试级别日志运行（等价于 **-l debug**）。

**-h**, **--help**
> 显示帮助后退出。

# DESCRIPTION

**hp-clean** 在 HPLIP 支持的 HP 喷墨打印机上执行打印头清洁流程，清除喷嘴上干涸的墨水与碎屑，以恢复打印质量。

不带特定模式启动时，它会进入一个交互式向导，让用户从 1 到 3 中选择清洁级别；级别越高清洁越强力，消耗的墨水也越多，因此通常先尝试级别 1。可以先用 **-p** 或 **-d** 指定目标打印机，否则当安装了多台 HPLIP 设备时 hp-clean 会提示选择。

hp-clean 仅适用于其 HPLIP 插件提供清洁例程的喷墨打印机；激光打印机和部分低端喷墨打印机不支持此功能。

# CAVEATS

属于 HPLIP 软件包。清洁会消耗墨水，只应在打印质量确实下降（出现条纹、缺线）时才运行。并非所有 HPLIP 支持的型号都实现打印头清洁功能。

# HISTORY

**hp-clean** 是 **HPLIP**（HP Linux Imaging and Printing）中设备维护工具之一，与 **hp-align** 和 **hp-linefeedcal** 并列。HPLIP 是 HP 面向 Linux 的开源打印/扫描驱动套件。

# INSTALL

```apt: sudo apt install hplip```

```dnf: sudo dnf install hplip```

```pacman: sudo pacman -S hplip```

```zypper: sudo zypper install hplip```

```nix: nix profile install nixpkgs#hplip```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hp-align](/man/hp-align)(1), [hp-check](/man/hp-check)(1), [hp-levels](/man/hp-levels)(1), [hp-info](/man/hp-info)(1)

# RESOURCES

```[Source code](https://sourceforge.net/projects/hplip/)```

```[Homepage](https://developers.hp.com/hp-linux-imaging-and-printing)```

```[Documentation](https://developers.hp.com/hp-linux-imaging-and-printing/tech_docs/man_pages/index)```

<!-- verified: 2026-07-19 -->
