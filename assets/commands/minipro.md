# TAGLINE

TL866II+、TL866A、TL866CS 和 T48 设备的开源编程器

# TLDR

**将芯片读取到文件**

```minipro -p [AT24C256] -r [output.bin]```

**将文件写入芯片**

```minipro -p [AT24C256] -w [firmware.bin]```

**擦除芯片**

```minipro -p [AT24C256] -E```

**校验芯片内容**

```minipro -p [AT24C256] -m [firmware.bin]```

**列出支持的芯片**

```minipro -l```

**搜索芯片**

```minipro -L [AT24]```

**以 Intel HEX 格式读取**

```minipro -p [ATmega328P] -r [output.hex] -f ihex```

**写入时忽略芯片 ID 不匹配**

```minipro -p [AT24C256] -w [firmware.bin] -y```

# SYNOPSIS

**minipro** [_-p device_] [_-r file_] [_-w file_] [_-E_] [_-f format_] [_options_]

# PARAMETERS

**-p** _DEVICE_
> 指定芯片/设备。

**-r** _FILE_
> 将芯片读取到文件。

**-w** _FILE_
> 将文件写入芯片。

**-E**
> 擦除芯片。

**-m** _FILE_
> 与文件进行校验比对。

**-l**
> 列出所有支持的设备。

**-L** _PATTERN_
> 按模式搜索设备。

**-f** _FORMAT_
> 文件格式（raw、ihex、srec）。

**-y**
> 芯片 ID 不匹配时不报错。

**-c** _TYPE_
> 指定存储类型：code、data 或 config。

**-s**
> 文件大小不匹配时不报错（仅警告）。

**-v**
> 写入后不进行校验。

**-e**
> 写入前不擦除设备。

**-i**
> 使用 ICSP 模式。

**-x**
> 不尝试读取芯片 ID（仅限读取模式）。

# DESCRIPTION

**minipro** 是面向 TL866II+、TL866A、TL866CS 和 T48 设备的开源编程器。它可对 EEPROM、闪存、微控制器及其他可编程芯片进行编程。

该工具支持超过 13000 种器件，包括 Atmel AVR、Microchip PIC、EPROM、EEPROM 和各类闪存芯片。器件数据库由社区维护。

读取操作将芯片内容转储到文件。写入操作从二进制或十六进制文件对芯片编程。校验操作确认编程成功。

擦除通常在写入前自动执行，但也可以单独进行。某些芯片需要特定的擦除流程或解锁序列。

微控制器固件支持 Intel HEX 和 Motorola S-Record 格式。原始二进制格式适用于数据存储芯片。

# CAVEATS

需要兼容的 TL866 或 T48 编程器硬件。数据库中并非所有芯片都经过测试。某些芯片需要专用适配座。Linux 上可能需要配置 USB 权限。T56 支持尚属实验性。

# HISTORY

**minipro** 作为 TL866 编程器专有 Windows 软件的开源替代品而创建。开发始于 **2014 年**前后，使这款广受欢迎的经济型编程器得以在 Linux 和 macOS 上使用。

# INSTALL

```dnf: sudo dnf install minipro```

```apk: sudo apk add minipro```

```brew: brew install minipro```

```nix: nix profile install nixpkgs#minipro```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[avrdude](/man/avrdude)(1), [flashrom](/man/flashrom)(8)
