# TAGLINE

向 I2C 设备的指定寄存器写入一个值

# TLDR

**写入** I2C 设备的某个寄存器

```i2cset [i2cbus] [device_address] [register_address] [value]```

无需**确认**提示直接写入

```i2cset -y [i2cbus] [device_address] [register_address] [value]```

使用**指定模式**写入

```i2cset [i2cbus] [device_address] [register_address] [value] [b|w|c|s|i]```

# SYNOPSIS

**i2cset** [_options_] _i2cbus_ _device_address_ _register_address_ _value_ [_mode_]

# PARAMETERS

**-y**
> 禁用交互式确认（在某些硬件上很危险）

**b**
> 字节模式 — 写入单个字节（默认）

**w**
> 字模式 — 写入 16 位值

**c**
> 连续字节模式

**s**
> SMBus 块模式

**i**
> I2C 块模式

# DESCRIPTION

**i2cset** 向 I2C 设备的指定寄存器写入一个值。这可用于配置 I2C 外设、设置参数或控制设备行为。

所有地址和值都应以十六进制表示。除非使用 -y 标志，否则命令在写入前会提示确认。

# CAVEATS

向 I2C 寄存器写入可能导致硬件损坏或意外行为。写入前务必核实设备地址和寄存器含义。某些设备在错误写入后可能失去响应或需要重新上电。需要 root 权限或属于 i2c 组。

# HISTORY

i2cset 是 i2c-tools 软件包的一部分，提供对 I2C 设备的用户态写访问。I2C 协议由飞利浦（现 NXP）于 **1982 年**开发，用于低速外设通信。

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

[i2cdetect](/man/i2cdetect)(8), [i2cdump](/man/i2cdump)(8), [i2cget](/man/i2cget)(8)
