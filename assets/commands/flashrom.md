# TAGLINE

闪存芯片的读取、写入与校验

# TLDR

**探测**芯片以确保接线正确

```flashrom -p [programmer]```

**读取**闪存内容并保存到文件

```flashrom -p [programmer] -r [path/to/backup.bin]```

将文件**写入**闪存芯片

```flashrom -p [programmer] -w [path/to/firmware.bin]```

将闪存内容与文件进行**校验**

```flashrom -p [programmer] -v [path/to/file.bin]```

**擦除**闪存芯片

```flashrom -p [programmer] -E```

使用 **Raspberry Pi** SPI 进行探测

```flashrom -p linux_spi:dev=/dev/spidev0.0```

根据布局文件只写入**指定区域**

```flashrom -p [programmer] -l [layout.txt] -i [region_name] -w [file.bin]```

# SYNOPSIS

**flashrom** [**-p** _programmer_] [**-r**|**-w**|**-v**|**-E**] [_file_] [_options_]

# PARAMETERS

**-p, --programmer** _name[:params]_
> 指定编程器设备（访问芯片时必需）

**-r, --read** _file_
> 读取闪存 ROM 内容并保存到文件

**-w, --write** _file_
> 将文件内容写入闪存 ROM

**-v, --verify** _file_
> 将闪存 ROM 内容与文件进行校验

**-E, --erase**
> 擦除整个闪存芯片

**-c, --chip** _name_
> 仅探测指定的闪存芯片型号

**-l, --layout** _file_
> 从文件读取 ROM 布局以进行局部刷写

**-i, --include** _region_
> 只对指定区域执行读取、写入或校验

**-f, --force**
> 覆盖安全检查（谨慎使用）

**-n, --noverify**
> 写入后跳过自动校验

**--flash-name**
> 显示检测到的闪存芯片名称

**--flash-size**
> 显示检测到的闪存芯片容量

# DESCRIPTION

**Flashrom** 是一款用于识别、读取、写入、校验和擦除闪存芯片的工具。它支持直接在主板上刷写 BIOS/EFI 固件（在线编程），也支持通过 USB、SPI 或并口连接的外部编程器。

该工具支持 500 多种闪存芯片和 40 多种编程器类型，包括主板内置访问、USB 设备（CH341A、Dediprog）、SPI 编程器（Raspberry Pi、Bus Pirate）以及基于网卡的编程器。

# CAVEATS

在使用 **-r** 写入新固件之前**务必先创建备份**。错误的刷写可能导致设备变砖。笔记本电脑的内置刷写风险尤其高，需要显式使用 **-f** 标志。某些操作需要 root 权限。尝试写入之前请先确认编程器与你的闪存芯片兼容。

# HISTORY

Flashrom 起源于 **2005 年**前后的 **LinuxBIOS**（现 coreboot）项目，最初是用于刷写开源固件的工具。后来它发展为一个独立项目，支持广泛的硬件。该项目由社区维护，已成为固件开发、coreboot 安装和芯片恢复操作的重要工具。

# INSTALL

```apt: sudo apt install flashrom```

```dnf: sudo dnf install flashrom```

```pacman: sudo pacman -S flashrom```

```apk: sudo apk add flashrom```

```zypper: sudo zypper install flashrom```

```brew: brew install flashrom```

```nix: nix profile install nixpkgs#flashrom```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dd](/man/dd)(1), [hexdump](/man/hexdump)(1)
