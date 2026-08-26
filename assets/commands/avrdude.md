# TAGLINE

对 AVR 微控制器的 flash 和熔丝位编程

# TLDR

向 Arduino **上传**固件

```avrdude -p [atmega328p] -c [arduino] -P [/dev/ttyUSB0] -U flash:w:[firmware.hex]```

**读取**flash 存储器

```avrdude -p [atmega328p] -c [usbasp] -U flash:r:[backup.hex]:i```

设置**熔丝位**

```avrdude -p [atmega328p] -c [usbasp] -U lfuse:w:[0xE2]:m```

只**校验**而不写入

```avrdude -p [atmega328p] -c [arduino] -P [/dev/ttyUSB0] -U flash:v:[firmware.hex]```

# SYNOPSIS

**avrdude** -p _partno_ -c _programmer_ [_options_]

# DESCRIPTION

**avrdude**（AVR Downloader Uploader）是一款用于对 Atmel AVR 微控制器编程的工具。它支持众多编程器，可以读写 flash、EEPROM、熔丝位和锁定位。

该工具是 Arduino 开发以及基于 AVR 芯片的嵌入式系统工作的必备工具。

# PARAMETERS

**-p** _partno_
> 指定 AVR 器件（如 atmega328p、attiny85）

**-c** _programmer_
> 编程器类型（arduino、usbasp、avrisp2）

**-P** _port_
> 通信端口（/dev/ttyUSB0、COM3）

**-U** _memtype:op:file:format_
> 存储器操作（flash:w:file.hex:i）

**-b** _baudrate_
> 为串口连接覆盖 RS-232 波特率

**-B** _bitclock_
> JTAG/ISP 位时钟周期（微秒或频率）

**-e**
> 执行整片擦除，将 flash 和 EEPROM 重置为 0xFF

**-D**
> 禁用写入 flash 前的自动整片擦除

**-V**
> 跳过写入存储器后的自动校验

**-v**
> 详细输出（重复使用可获得更多信息）

**-n**
> 试运行，不实际写入器件

**-F**
> 强制操作，覆盖签名和初始化检查

**-t**
> 进入交互式终端模式，手动执行存储器操作

# MEMORY OPERATIONS

**flash**
> 程序存储器

**eeprom**
> 数据存储器

**lfuse**, **hfuse**, **efuse**
> 配置熔丝

**lock**
> 锁定位

操作类型：**r**（读取）、**w**（写入）、**v**（校验）

# CONFIGURATION

**/etc/avrdude.conf**
> 全系统配置，定义编程器类型、器件定义和默认设置。

**~/.avrduderc**
> 每用户配置覆盖。可以添加自定义编程器定义或修改器件设置。

# CAVEATS

错误的熔丝设置可能把器件变砖。串口需要适当的权限。选错编程器会导致失败。修改熔丝前务必备份。某些平台上 USB 连接问题很常见。

# HISTORY

**avrdude** 由 Brian Dean 于 **2003** 年创建，作为 Atmel 专有编程工具的开源替代品。它已成为 AVR 编程的标准工具。

# INSTALL

```apt: sudo apt install avrdude```

```dnf: sudo dnf install avrdude```

```pacman: sudo pacman -S avrdude```

```apk: sudo apk add avrdude```

```zypper: sudo zypper install avrdude```

```brew: brew install avrdude```

```nix: nix profile install nixpkgs#avrdude```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[arduino-cli](/man/arduino-cli)(1), [avr-gcc](/man/avr-gcc)(1), [platformio](/man/platformio)(1), [minicom](/man/minicom)(1)

# RESOURCES

```[Source code](https://github.com/avrdudes/avrdude)```

```[Documentation](https://avrdudes.github.io/avrdude/)```

<!-- verified: 2026-06-17 -->
