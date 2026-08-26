# TLDR

**显示设备信息**

```st-info --probe```

**显示闪存大小**

```st-info --flash```

**显示 SRAM 大小**

```st-info --sram```

**显示芯片 ID**

```st-info --chipid```

**显示描述**

```st-info --descr```

**显示序列号**

```st-info --serial```

# SYNOPSIS

**st-info** [_--probe_] [_--flash_] [_--sram_] [_options_]

# PARAMETERS

**--probe**
> 探测已连接的设备。

**--flash**
> 闪存大小。

**--sram**
> SRAM 大小。

**--chipid**
> 芯片标识符。

**--descr**
> 设备描述。

**--serial**
> 编程器序列号。

# DESCRIPTION

**st-info** 通过 ST-Link 编程器/调试器查询 STM32 微控制器的信息。它报告设备识别详情，包括芯片 ID、设备描述、闪存大小、SRAM 大小以及编程器的序列号。

该工具可用于验证硬件连接、识别未知的 STM32 型号，以及在编程前确认内存大小。**--probe** 选项提供所有已连接设备的综合摘要。它是开源 stlink 工具集的一部分。

# CAVEATS

需要 ST-Link。必须连接设备。仅支持 STM32。

# HISTORY

**st-info** 是 **stlink** 工具集的一部分，为通过 ST-Link 连接的 STM32 微控制器提供设备信息。

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

[st-flash](/man/st-flash)(1), [st-util](/man/st-util)(1), [openocd](/man/openocd)(1)
