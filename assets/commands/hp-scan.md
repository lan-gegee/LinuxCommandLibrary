# TAGLINE

从 HP 多功能一体机扫描文档

# TLDR

**扫描文档**

```hp-scan```

**指定输出文件**

```hp-scan -o [output.pdf]```

**扫描为 JPEG**

```hp-scan -t jpeg -o [output.jpg]```

**指定分辨率**

```hp-scan -r [300]```

**使用自动进纸器**

```hp-scan --adf```

# SYNOPSIS

**hp-scan** [_options_]

# PARAMETERS

**-o**, **--output** _FILE_
> 输出文件名。

**-t**, **--type** _TYPE_
> 输出格式（pdf、jpeg、png）。

**-r**, **--resolution** _DPI_
> 扫描分辨率。

**--adf**
> 使用自动文档进纸器（ADF）。

**-p** _PRINTER_
> 打印机/扫描仪名称。

**-d** _DEVICE_
> 设备 URI。

**--help**
> 显示帮助信息。

# DESCRIPTION

**hp-scan** 从 HP 多功能一体机扫描文档。它支持多种输出格式和分辨率。

该工具可以使用平板或自动文档进纸器。它是图形扫描界面的命令行替代方案。

# CAVEATS

属于 HPLIP 软件包。部分型号需要插件。需要具备扫描功能的设备。

# HISTORY

hp-scan 是 **HPLIP**（HP Linux Imaging and Printing）的一部分，用于在 HP 多功能设备上进行扫描。

# INSTALL

```apt: sudo apt install hplip```

```dnf: sudo dnf install hplip```

```pacman: sudo pacman -S hplip```

```zypper: sudo zypper install hplip```

```nix: nix profile install nixpkgs#hplip```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hp-setup](/man/hp-setup)(1), [scanimage](/man/scanimage)(1)
