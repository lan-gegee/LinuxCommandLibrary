# TAGLINE

解码并显示内存 SPD EEPROM 信息

# TLDR

显示 **DIMM 信息**

```decode-dimms```

**并排**显示多个 DIMM 便于比较

```decode-dimms --side-by-side```

即使在**校验和失败**时也进行解码

```decode-dimms -c```

从 **hexdump 文件**而非运行中的系统读取

```decode-dimms -x```

显示**帮助**

```decode-dimms -h```

# SYNOPSIS

**decode-dimms** [_options_]

# DESCRIPTION

**decode-dimms** 解码并显示存储在内存模块 SPD（Serial Presence Detect）EEPROM 中的信息，包括内存类型、速度、制造商、容量和时序信息。

适用于识别已安装内存的规格以及验证内存兼容性。

# PARAMETERS

**-h**, **--help**
> 显示用法摘要。

**-c**, **--checksum**
> 即使校验和失败也完整解码。

**-f**, **--format**
> 以 HTML 格式打印输出。

**-b**, **--bodyonly**
> 不打印 HTML 头部（便于后处理）。

**--side-by-side**
> 尽可能并排显示所有 DIMM。

**-x**
> 从 hexdump 文件而非运行中的系统读取数据。

**-X**
> 与 -x 相同，但将多字节十六进制数据视为小端序。

# CAVEATS

需要加载 eeprom、at24 或 ee1004（DDR4 用）内核模块。可能还需要 i2c 内核模块。需要 root 权限或对 i2c 设备有适当权限。属于 i2c-tools 软件包。

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

[dmidecode](/man/dmidecode)(8), [lshw](/man/lshw)(1), [free](/man/free)(1), [i2cdetect](/man/i2cdetect)(8)
