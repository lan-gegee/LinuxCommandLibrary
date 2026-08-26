# TAGLINE

以条形图显示 HP 打印机当前的墨水或碳粉余量

# TLDR

为默认/唯一安装的打印机**显示墨水/碳粉余量**

```hp-levels```

**显示指定 CUPS 打印机的余量**

```hp-levels -p [printer-name]```

**按设备 URI 显示余量**

```hp-levels -d [device-uri]```

**以交互方式运行**，从列表中选择打印机

```hp-levels -i```

**绘制更宽的条形图**（默认宽度为 51 个字符）

```hp-levels -s [80]```

# SYNOPSIS

**hp-levels** [_DEVICE-URI_|_PRINTER-NAME_] [_MODE_] [_OPTIONS_]

# PARAMETERS

**-d** _device-uri_, **--device**=_device-uri_
> 按 CUPS 设备 URI 指定目标打印机。

**-p** _printer_, **--printer**=_printer_
> 按 CUPS 队列名称指定目标打印机。

**-i**, **--interactive**
> 以交互模式运行，提示选择设备。

**-s** _size_, **--size**=_size_
> 条形图宽度（字符数，默认 51）。

**-c**, **--color**
> 使用彩色条形图（默认已启用彩色）。

**-a** _char_, **--char**=_char_
> 用于绘制条形图的字符（默认 **/**）。

**-l** _level_, **--logging**=_level_
> 设置日志详细程度：none、info（默认）、error、warn 或 debug。

**-g**
> 以调试级别日志运行（等价于 **-l debug**）。

**-h**, **--help**
> 显示帮助后退出。

# DESCRIPTION

**hp-levels** 查询 HPLIP 支持的 HP 打印机当前的墨水或碳粉余量，并在终端中以文本条形图呈现，每个已安装的墨盒或墨仓对应一条。

用 **-p** 或 **-d** 指向某台打印机；若未给出目标，则使用唯一已安装的 HPLIP 设备，或在配置了多台时提示选择。它相当于 HPLIP 工具箱 GUI 中耗材面板的命令行版本。

# CAVEATS

属于 HPLIP 软件包。余量报告的准确性和粒度因打印机型号而异；一些廉价机型只报告正常/偏低/耗尽而非百分比，少数机型完全不报告。

# HISTORY

**hp-levels** 是 **HPLIP**（HP Linux Imaging and Printing）中的耗材监控工具之一。HPLIP 是 HP 面向 Linux 的开源打印/扫描驱动套件。

# INSTALL

```apt: sudo apt install hplip```

```dnf: sudo dnf install hplip```

```pacman: sudo pacman -S hplip```

```zypper: sudo zypper install hplip```

```nix: nix profile install nixpkgs#hplip```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hp-info](/man/hp-info)(1), [hp-check](/man/hp-check)(1), [lpstat](/man/lpstat)(1)

# RESOURCES

```[Source code](https://sourceforge.net/projects/hplip/)```

```[Homepage](https://developers.hp.com/hp-linux-imaging-and-printing)```

```[Documentation](https://developers.hp.com/hp-linux-imaging-and-printing/tech_docs/man_pages/index)```

<!-- verified: 2026-07-19 -->
