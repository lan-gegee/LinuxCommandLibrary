# TAGLINE

管理 Raspberry Pi Pico 和 RP2040 设备

# TLDR

**显示设备信息**

```picotool info```

**载入二进制文件**

```picotool load [firmware.uf2]```

**保存 flash 内容**

```picotool save -a [backup.bin]```

**校验二进制文件**

```picotool verify [firmware.uf2]```

**重启设备**

```picotool reboot```

**显示二进制信息**

```picotool info [firmware.elf]```

**擦除 flash**

```picotool load --erase```

# SYNOPSIS

**picotool** _command_ [_options_] [_file_]

# PARAMETERS

**info**
> 显示设备/文件信息。

**load**
> 将二进制文件载入设备。

**save**
> 从设备保存内容。

**verify**
> 校验设备内容。

**reboot**
> 重启设备。

**version**
> 显示版本。

**-a**, **--all**
> 全部 flash 内容。

**-x**, **--execute**
> 载入后执行。

**-f**, **--force**
> 强制操作。

# DESCRIPTION

**picotool** 管理 Raspberry Pi Pico 和 RP2040 设备。它可以载入固件、读取设备信息并控制启动模式。

设备信息显示芯片细节和正在运行的程序。二进制信息展示内嵌的元数据。

载入操作将固件写入 flash。支持 UF2 和 ELF 格式。

保存操作提取 flash 内容用于备份。可以转储整个 flash 或特定区域。

校验操作将设备内容与文件进行比较。适合确认编程是否成功。

# CAVEATS

许多操作要求设备处于 BOOTSEL 模式。需要 USB 连接。某些操作会擦除现有固件。

# HISTORY

**picotool** 由 **Raspberry Pi** 为其 RP2040 微控制器创建。随 Pico 于 **2021 年**发布，提供官方的设备管理工具。

# INSTALL

```apt: sudo apt install picotool```

```zypper: sudo zypper install picotool```

```brew: brew install picotool```

```nix: nix profile install nixpkgs#picotool```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[openocd](/man/openocd)(1), [gdb](/man/gdb)(1), [stlink](/man/stlink)(1)
