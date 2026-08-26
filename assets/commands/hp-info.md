# TAGLINE

查询 HP 打印机的静态型号信息、动态状态和 CUPS 设置

# TLDR

为默认/唯一安装的打印机**显示信息**

```hp-info```

**显示指定 CUPS 打印机的信息**

```hp-info -p [printer-name]```

**按设备 URI 显示信息**

```hp-info -d [device-uri]```

**只打印设备 ID 字符串**（交互模式）

```hp-info -i --id```

**以交互方式运行**，从列表中选择打印机

```hp-info -i```

# SYNOPSIS

**hp-info** [_DEVICE-URI_|_PRINTER-NAME_] [_MODE_] [_OPTIONS_]

# PARAMETERS

**-d** _device-uri_, **--device**=_device-uri_
> 按 CUPS 设备 URI 指定目标打印机。

**-p** _printer_, **--printer**=_printer_
> 按 CUPS 队列名称指定目标打印机。

**-i**, **--interactive**
> 以交互模式运行，提示选择设备。

**--id**
> 只打印设备 ID 字符串后退出（仅限交互模式）。

**-x**
> 允许使用尚未安装到 CUPS 的打印机设备 URI（仅限交互模式）。

**-l** _level_, **--logging**=_level_
> 设置日志详细程度：none、info（默认）、error、warn 或 debug。

**-g**
> 以调试级别日志运行（等价于 **-l debug**）。

**-h**, **--help**
> 显示帮助后退出。

# DESCRIPTION

**hp-info** 查询 HPLIP 支持的 HP 打印机，报告静态型号信息（型号名称、支持的数据类型、插件要求）、动态状态（在线/离线、纸盒与耗材状态）以及对应的 CUPS 打印机队列设置。

它主要是一个诊断工具：用 **-p** 或 **-d** 指向某台打印机即可转储 HPLIP 所知的该设备的一切信息，这在提交错误报告或编写设备发现脚本时很有用。

# CAVEATS

属于 HPLIP 软件包。打印机必须可达（已开机并通过 USB 或网络连接），动态状态字段才会有内容；即使设备离线，静态型号数据也会从 HPLIP 本地的型号数据库读取。

# HISTORY

**hp-info** 是 **HPLIP**（HP Linux Imaging and Printing）中的设备查询工具之一。HPLIP 是 HP 面向 Linux 的开源打印/扫描驱动套件。

# INSTALL

```apt: sudo apt install hplip```

```dnf: sudo dnf install hplip```

```pacman: sudo pacman -S hplip```

```zypper: sudo zypper install hplip```

```nix: nix profile install nixpkgs#hplip```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hp-check](/man/hp-check)(1), [hp-levels](/man/hp-levels)(1), [hp-query](/man/hp-query)(1), [lpstat](/man/lpstat)(1)

# RESOURCES

```[Source code](https://sourceforge.net/projects/hplip/)```

```[Homepage](https://developers.hp.com/hp-linux-imaging-and-printing)```

```[Documentation](https://developers.hp.com/hp-linux-imaging-and-printing/tech_docs/man_pages/index)```

<!-- verified: 2026-07-19 -->
