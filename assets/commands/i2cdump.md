# TAGLINE

读取并显示连接到指定总线的 I2C 设备的所有寄存器

# TLDR

**转储** I2C 设备的所有寄存器

```i2cdump [i2cbus] [device_address]```

无需**确认**提示直接转储

```i2cdump -y [i2cbus] [device_address]```

使用**指定模式**转储

```i2cdump [i2cbus] [device_address] [b|w|c|s|i]```

转储一个**范围**内的寄存器

```i2cdump -r [start]-[end] [i2cbus] [device_address]```

# SYNOPSIS

**i2cdump** [_options_] _i2cbus_ _device_address_ [_mode_]

# PARAMETERS

**-y**
> 禁用交互式确认（在某些硬件上很危险）

**-r** _START-END_
> 将转储限制在指定范围内的寄存器

**b**
> 字节模式（大多数设备的默认值）

**w**
> 字模式（16 位值）

**c**
> 连续字节模式

**s**
> SMBus 块模式

**i**
> I2C 块模式

# DESCRIPTION

**i2cdump** 读取并显示连接到指定总线的 I2C 设备的所有寄存器。它输出一张十六进制表，展示寄存器地址及其内容，可用于调试 I2C 硬件。

所有地址都应以十六进制表示。总线号可通过 i2cdetect -l 确定，设备地址可通过 i2cdetect 查找。

# CAVEATS

访问 I2C 设备可能在某些系统上造成硬件问题。使用 -y 标志时务必谨慎。读取某些寄存器可能产生副作用。需要适当的权限（通常是 root 或属于 i2c 组）。

# HISTORY

i2cdump 是 i2c-tools 软件包的一部分，提供对 I2C 总线的用户态访问。I2C 总线协议由飞利浦半导体（现 NXP）于 **1982 年**开发，用于芯片间通信。

# INSTALL

```apt: sudo apt install i2c-tools```

```dnf: sudo dnf install i2c-tools```

```pacman: sudo pacman -S i2c-tools```

```apk: sudo apk add i2c-tools```

```zypper: sudo zypper install i2c-tools```

```brew: brew install i2c-tools```

```nix: nix profile install nixpkgs#i2c-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[i2cdetect](/man/i2cdetect)(8), [i2cget](/man/i2cget)(8), [i2cset](/man/i2cset)(8)
