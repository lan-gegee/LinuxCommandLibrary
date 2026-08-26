# TAGLINE

Arduino sketch 的命令行编译器

# TLDR

**编译** sketch

```arduino-builder -hardware [/usr/share/arduino/hardware] -tools [/usr/share/arduino/tools-builder] -libraries [/usr/share/arduino/libraries] -fqbn [arduino:avr:uno] [sketch.ino]```

以**详细输出**模式编译

```arduino-builder -verbose -fqbn [arduino:avr:uno] [sketch.ino]```

# SYNOPSIS

**arduino-builder** [_-hardware path_] [_-tools path_] [_-libraries path_] [_-fqbn board_] [_options_] _sketch_

# DESCRIPTION

**arduino-builder** 是编译 Arduino sketch 的命令行工具。它是 Arduino IDE 所使用的构建系统，也可以单独调用以实现自动化构建。

该工具负责 Arduino sketch 及所需库和核心文件的预处理、编译与链接。

# PARAMETERS

**-hardware** _path_
> 硬件定义目录

**-tools** _path_
> 工具（编译器、上传器）目录

**-libraries** _path_
> 库目录

**-fqbn** _board_
> 完全限定板卡名称

**-build-path** _dir_
> 构建输出目录

**-verbose**
> 详细输出

**-warnings** _level_
> 警告级别（none、default、more、all）

**-prefs** _key=value_
> 构建首选项

# CAVEATS

已被 arduino-cli 取代而弃用。需要指定多个路径。板卡软件包须单独安装。

# HISTORY

**arduino-builder** 是从 Arduino IDE 中抽取出来的独立构建工具。对大多数用例而言，现已被 **arduino-cli** 取代。

# INSTALL

```apt: sudo apt install arduino-builder```

```aur: yay -S arduino-builder```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[arduino](/man/arduino)(1), [arduino-cli](/man/arduino-cli)(1), [avr-gcc](/man/avr-gcc)(1)

# RESOURCES

```[Source code](https://github.com/arduino/arduino-builder)```

```[Homepage](https://www.arduino.cc)```

<!-- verified: 2026-06-11 -->
