# TAGLINE

校准 HP 打印机的打印墨盒

# TLDR

**校准打印头**

```hp-align```

**指定打印机**

```hp-align -p [printer-name]```

**交互模式**

```hp-align -i```

**指定设备 URI**

```hp-align -d [hp:/usb/Deskjet_Printer?serial=XYZ]```

**启用调试日志**

```hp-align -g```

# SYNOPSIS

**hp-align** [_options_]

# PARAMETERS

**-p** _PRINTER_, **--printer=**_PRINTER_
> CUPS 打印机名称。

**-d** _URI_, **--device=**_URI_
> 设备 URI（例如 `hp:/usb/...`）。

**-i**, **--interactive**
> 以交互模式运行。

**-l** _LEVEL_, **--logging=**_LEVEL_
> 日志级别：none、info、error、warn、debug。

**-g**
> 调试模式（等价于 `-l debug`）。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**hp-align** 校准 HP 打印机上的打印墨盒。它运行对齐程序以确保最佳打印质量。

该工具支持自动和交互两种对齐模式。交互模式会显示对齐图案并要求选择最匹配的一项。

# CAVEATS

属于 HPLIP 软件包。会消耗纸张和墨水。可能需要手动选择。

# HISTORY

hp-align 是 **HPLIP**（HP Linux Imaging and Printing）的一部分，这是 HP 官方的 Linux 打印机驱动项目。

# INSTALL

```apt: sudo apt install hplip```

```dnf: sudo dnf install hplip```

```pacman: sudo pacman -S hplip```

```zypper: sudo zypper install hplip```

```nix: nix profile install nixpkgs#hplip```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hp-check](/man/hp-check)(1), [hp-clean](/man/hp-clean)(1), [hp-setup](/man/hp-setup)(1)
