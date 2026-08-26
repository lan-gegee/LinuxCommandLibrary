# TAGLINE

将 HPLIP 支持的 HP 打印机和传真安装到 CUPS 打印池

# TLDR

**启动图形化设置向导**（未指定模式时的默认行为）

```hp-setup```

**运行基于文本的交互式向导**

```hp-setup -i```

**自动设置 USB 打印机**，无提示，使用 lsusb 中的 bus:device ID

```hp-setup -i -a [001:002]```

**按 IP 地址设置网络打印机**，自动进行且不打印测试页

```hp-setup -i -a -x [192.168.1.100]```

**移除已安装的打印机**

```hp-setup -r -p [printer-name]```

# SYNOPSIS

**hp-setup** [_MODE_] [_OPTIONS_] [_SERIAL-NO_|_USB-BUS:DEVICE_|_IP_|_DEVNODE_]

# PARAMETERS

**-u**, **--gui**
> 运行图形（Qt）设置向导。未指定模式时这是默认行为。

**-i**, **--interactive**
> 运行基于文本的交互式设置向导。

**-a**, **--auto**
> 非交互式自动设置，跳过提示（仅限交互模式）。

**-x**
> 自动模式下跳过打印测试页（仅限交互模式）。

**-p** _printer_, **--printer**=_printer_
> 设置 CUPS 打印机队列名称（仅限交互模式）。

**-f** _fax_, **--fax**=_fax_
> 设置 CUPS 传真队列名称（仅限交互模式）。

**-t** _typelist_, **--type**=_typelist_
> 要创建的队列类型：print、fax（仅限交互模式）。

**-d** _device-uri_, **--device**=_device-uri_
> 直接指定设备 URI（仅限 GUI 模式）。

**-r**, **--rm**, **--remove**
> 移除打印机/传真队列而不是安装。

**--port**=_port_
> 多端口 JetDirect 的端口号：1（默认）、2 或 3。

**-l** _level_, **--logging**=_level_
> 设置日志详细程度：none、info、error、warn 或 debug。

**-g**
> 以调试级别日志运行（等价于 **-l debug**）。

**-h**, **--help**
> 显示帮助后退出。

# DESCRIPTION

**hp-setup** 发现 HP 打印机（USB、网络/JetDirect 或并口），并将其安装到 CUPS 打印池中，自动选择合适的 PPD/驱动；对于支持传真的机型，还会设置传真队列和基本传真参数。它还可以在安装过程中打印测试页。

不带参数运行时，它会打开 Qt 图形向导。对于脚本化或无头（headless）安装，使用 **-i** 进入文本向导，加 **-a** 跳过所有交互提示，可选加 **-x** 跳过测试页。可以通过 USB bus:device ID（来自 **lsusb**）、IP 地址、主机名、序列号或并口设备节点直接指定目标设备；若不指定，hp-setup 会探测 USB 和并行总线以寻找兼容的打印机。

# CAVEATS

属于 HPLIP 软件包。安装打印队列通常需要 root 权限或用户属于 CUPS 的 **lpadmin** 组。某些型号需要 HP 的专有二进制插件，hp-setup 会通过 **hp-plugin** 提示下载并安装（需要联网）。

# HISTORY

**hp-setup** 是 **HPLIP**（HP Linux Imaging and Printing）中的主要安装工具。HPLIP 是 HP 面向 Linux 的开源打印/扫描驱动套件。

# INSTALL

```apt: sudo apt install hplip```

```dnf: sudo dnf install hplip```

```pacman: sudo pacman -S hplip```

```zypper: sudo zypper install hplip```

```nix: nix profile install nixpkgs#hplip```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hp-check](/man/hp-check)(1), [hp-plugin](/man/hp-plugin)(1), [hp-info](/man/hp-info)(1), [lpadmin](/man/lpadmin)(1)

# RESOURCES

```[Source code](https://sourceforge.net/projects/hplip/)```

```[Homepage](https://developers.hp.com/hp-linux-imaging-and-printing)```

```[Documentation](https://developers.hp.com/hp-linux-imaging-and-printing/tech_docs/man_pages/index)```

<!-- verified: 2026-07-19 -->
