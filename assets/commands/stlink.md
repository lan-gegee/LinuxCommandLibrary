# TAGLINE

开源 STM32 编程工具集

# TLDR

**将固件烧录到 STM32**

```st-flash write [firmware.bin] 0x08000000```

**读取闪存到文件**

```st-flash read [output.bin] 0x08000000 [size]```

**擦除闪存**

```st-flash erase```

**显示编程器和 MCU 信息**

```st-info --probe```

**烧录前后都复位目标芯片**

```st-flash --reset write [firmware.bin] 0x08000000```

**复位目标 MCU**

```st-flash reset```

**烧录 Intel HEX 文件**

```st-flash --format ihex write [firmware.hex]```

# SYNOPSIS

**st-flash** [_options_] {read|write|erase|reset} [_file_] [_address_] [_size_]

**st-info** [_options_]

# PARAMETERS

**--reset**
> 在烧录前后均触发一次复位。

**--connect-under-reset**
> 在目标保持复位状态时进行连接。

**--hot-plug**
> 不复位直接连接目标。

**--format** _format_
> 文件格式：binary 或 ihex（Intel HEX）。

**--flash** _size_
> 覆盖检测到的闪存大小（以字节为单位，可带 k/M 后缀）。

**--serial** _serial_
> 按序列号使用指定的 ST-LINK。

**--freq** _khz_
> 以 kHz 设置 SWD 频率。

**--opt**
> 启用忽略末尾空字节的优化。

**--debug**
> 启用调试输出。

**--version**
> 显示版本信息。

**--probe**（st-info）
> 显示已连接编程器和目标的信息。

**--chipid**（st-info）
> 显示已连接目标的芯片 ID。

**--descr**（st-info）
> 显示已连接目标的描述信息。

**--flash**（st-info）
> 显示可用的闪存容量。

**--sram**（st-info）
> 显示可用的 SRAM 容量。

**--pagesize**（st-info）
> 显示闪存页大小。

**--serial**（st-info）
> 显示编程器的序列号编码。

# DESCRIPTION

**stlink** 是一套用于通过 ST-LINK 编程器对 STM32 微控制器进行编程和调试的开源工具集。它提供的命令行实用程序支持 ST-LINK/V1、V2、V2-1、V3 以及兼容的克隆编程器。

该工具集包括用于读写闪存的 **st-flash**，以及用于查询编程器和目标信息的 **st-info**。它通过 SWD（Serial Wire Debug）或 JTAG 协议与 STM32 目标通信。

这些工具支持二进制和 Intel HEX 文件格式。闪存操作可以针对主闪存、选项字节或其他存储区域。**--connect-under-reset** 选项对固件有问题或调试访问被锁定的目标很有帮助。

# CAVEATS

在 Linux 上需要配置相应的 udev 规则以支持非 root 访问。某些 ST-LINK 克隆版可能存在兼容性问题。V1 编程器相比 V2/V3 功能有限。选项字节操作不当可能导致设备变砖。对于复杂的编程需求，可考虑使用 STM32CubeProgrammer CLI。

# HISTORY

**stlink** 项目作为 STMicroelectronics 专有工具 ST-LINK Utility 的开源替代方案而创建。它起源于 texane/stlink 仓库，现由 GitHub 上的 stlink-org 社区维护。该项目让 STM32 开发得以在官方工具支持有限的 Linux 和 macOS 上进行。

# INSTALL

```dnf: sudo dnf install stlink```

```pacman: sudo pacman -S stlink```

```zypper: sudo zypper install stlink```

```brew: brew install stlink```

```nix: nix profile install nixpkgs#stlink```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[st-flash](/man/st-flash)(1), [st-info](/man/st-info)(1), [openocd](/man/openocd)(1), [avrdude](/man/avrdude)(1)
