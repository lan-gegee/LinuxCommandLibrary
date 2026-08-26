# TAGLINE

扫描 I2C 总线以检测已连接的设备

# TLDR

列出**活动的 I2C 总线**

```i2cdetect -l```

在 I2C 总线 1 上**扫描设备**

```i2cdetect -y 1```

**使用 SMBus quick write** 命令扫描（更安全的默认模式）

```i2cdetect -y -q 1```

**使用 SMBus read byte** 命令扫描

```i2cdetect -y -r 1```

**扫描所有地址**，包括保留地址（0x00-0x7f）

```i2cdetect -y -a 1```

**显示适配器功能**

```i2cdetect -F 1```

# SYNOPSIS

**i2cdetect** [_options_] _i2cbus_

# PARAMETERS

**-l**
> 列出可用的 I2C 总线

**-y**
> 禁用交互模式（不显示确认提示）

**-a**
> 扫描所有地址（0x00-0x7f 而非 0x03-0x77）

**-q**
> 使用 SMBus quick write 命令进行探测

**-r**
> 使用 SMBus read byte 命令进行探测

**-F**
> 显示适配器的功能

# DESCRIPTION

**i2cdetect** 扫描 I2C 总线以检测已连接的设备。它常用于调试 I2C 硬件、识别设备地址以及在嵌入式系统和单板计算机上验证硬件连接。

输出是一个显示 0x00-0x7f 地址的网格。检测到的设备会显示其地址，空位显示 "--"。标记为 "UU" 的地址正被某个内核驱动占用。

在 Raspberry Pi 等开发板上，I2C 常用于传感器、显示器和其他外设。常见设备包括：
- 0x27/0x3f — LCD 显示屏
- 0x48-0x4f — 温度传感器
- 0x50-0x57 — EEPROM
- 0x68 — 实时时钟

# CAVEATS

需要 root 权限或属于 i2c 组。扫描可能干扰敏感设备；在生产环境中使用 **-y** 时请谨慎。某些设备可能不会响应探测。

# HISTORY

i2cdetect 是 i2c-tools 的一部分，这是一套用于 Linux 上 I2C 总线访问的工具。I2C（Inter-Integrated Circuit）由飞利浦于 **1982 年**开发，随后在嵌入式系统中被广泛采用。

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

[i2cget](/man/i2cget)(8), [i2cset](/man/i2cset)(8), [i2cdump](/man/i2cdump)(8), [modprobe](/man/modprobe)(8), [dmesg](/man/dmesg)(1)
