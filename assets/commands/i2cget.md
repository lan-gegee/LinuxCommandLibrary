# TAGLINE

从 I2C 设备读取单个寄存器的值

# TLDR

**读取** I2C 设备的某个寄存器

```i2cget [i2cbus] [device_address] [register_address]```

无需**确认**提示直接读取

```i2cget -y [i2cbus] [device_address] [register_address]```

使用**指定模式**读取

```i2cget [i2cbus] [device_address] [register_address] [b|w|c|s|i]```

# SYNOPSIS

**i2cget** [_options_] _i2cbus_ _device_address_ [_register_address_] [_mode_]

# PARAMETERS

**-y**
> 禁用交互式确认（在某些硬件上很危险）

**b**
> 字节模式 — 读取单个字节（默认）

**w**
> 字模式 — 读取 16 位值

**c**
> 连续字节模式

**s**
> SMBus 块模式

**i**
> I2C 块模式

# DESCRIPTION

**i2cget** 从 I2C 设备读取单个寄存器的值。这适用于检查设备的特定配置或状态寄存器，而无需转储整个寄存器映射。

所有地址都应以十六进制表示。总线号标识要使用的 I2C 总线，设备地址指定要与该总线上哪个设备通信。

# CAVEATS

读取 I2C 寄存器可能在某些硬件上引发意外行为。某些寄存器对读取敏感，被读取时可能改变状态或清除标志。需要 root 权限或属于 i2c 组。

# HISTORY

i2cget 是 Linux 上 i2c-tools 软件包的一部分，提供对 I2C 设备的用户态访问。它可用于检查和调试传感器、EEPROM 及其他嵌入式 I2C 外设。

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

[i2cdetect](/man/i2cdetect)(8), [i2cdump](/man/i2cdump)(8), [i2cset](/man/i2cset)(8)
