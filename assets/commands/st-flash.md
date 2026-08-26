# TLDR

**烧录二进制文件**

```st-flash write [firmware.bin] [0x8000000]```

**读取闪存**

```st-flash read [output.bin] [0x8000000] [0x1000]```

**擦除闪存**

```st-flash erase```

**复位设备**

```st-flash reset```

**校验写入**

```st-flash --verify write [firmware.bin] [0x8000000]```

# SYNOPSIS

**st-flash** [_--verify_] _command_ [_file_] [_address_] [_size_]

# PARAMETERS

**write**
> 写入闪存。

**read**
> 从闪存读取。

**erase**
> 擦除全部闪存。

**reset**
> 复位芯片。

**--verify**
> 写入后进行校验。

**--reset**
> 操作完成后复位。

**--serial** _SN_
> 设备序列号。

# DESCRIPTION

**st-flash** 是一款命令行工具，可通过 ST-Link 编程器/调试器读取、写入和擦除 STM32 微控制器的闪存。它是开源 stlink 工具集的一部分。

该工具处理原始二进制文件，读写操作需要显式指定内存地址。大多数 STM32 设备的闪存基地址为 **0x8000000**。可以使用 **--verify** 启用写入校验，以确认烧录的数据与输入文件一致。erase 命令会清除整个闪存，reset 则会在编程完成后重启微控制器。

# CAVEATS

需要 ST-Link。仅适用于 STM32。需要正确的地址。

# HISTORY

**st-flash** 是 **stlink** 工具集的一部分，后者是一套通过 ST-Link 对 STM32 微控制器编程的开源工具。

# INSTALL

```apt: sudo apt install stlink-tools```

```dnf: sudo dnf install stlink```

```pacman: sudo pacman -S stlink```

```apk: sudo apk add stlink```

```zypper: sudo zypper install stlink```

```brew: brew install stlink```

```nix: nix profile install nixpkgs#stlink```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[st-info](/man/st-info)(1), [st-util](/man/st-util)(1), [openocd](/man/openocd)(1)
