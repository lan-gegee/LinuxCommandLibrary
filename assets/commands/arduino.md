# TAGLINE

Arduino 板卡的集成开发环境

# TLDR

**启动** Arduino IDE

```arduino```

**打开** sketch

```arduino [sketch.ino]```

**编译** sketch

```arduino --verify [sketch.ino]```

**上传**到板卡

```arduino --upload [sketch.ino]```

指定**板卡**和**端口**

```arduino --board [arduino:avr:uno] --port [/dev/ttyACM0] --upload [sketch.ino]```

# SYNOPSIS

**arduino** [_--verify_|_--upload_] [_--board board_] [_--port port_] [_sketch_]

# DESCRIPTION

**arduino** 是用于给 Arduino 微控制器板卡编程的 Arduino 集成开发环境（IDE）。它提供代码编辑器、编译器以及上传 Arduino sketch 的功能。

命令行界面支持无界面的编译与上传，适用于 CI/CD 流水线和脚本编写。

# PARAMETERS

**--verify**
> 只编译 sketch 不上传

**--upload**
> 编译并上传到板卡

**--board** _fqbn_
> 完全限定板卡名称

**--port** _port_
> 上传使用的串口

**--pref** _name=value_
> 设置首选项

**--save-prefs**
> 保存首选项并退出

**--get-pref** _name_
> 打印首选项的值

**--install-boards** _package:platform_
> 安装板卡软件包

**--install-library** _name_
> 安装库

# CONFIGURATION

**~/.arduino15/preferences.txt**
> IDE 首选项文件，包括板卡默认值、编辑器设置和额外的板卡管理器 URL。

# CAVEATS

这些命令行标志属于**旧版 Arduino IDE 1.x**，该版本已不再积极开发。对于无界面构建和脚本编写，推荐使用 Arduino IDE 2.x 和独立的 **arduino-cli**。非 AVR 板卡可能需要安装板卡支持包；在 Linux 上串口权限可能需要将用户加入 **dialout** 组。

# HISTORY

**Arduino** 项目于 **2005** 年始于伊夫雷亚交互设计学院。经典 IDE（及其 `arduino` 命令行接口）曾是主要的开发环境，直到被 **Arduino IDE 2.x** 和 **arduino-cli** 取代。

# INSTALL

```apt: sudo apt install arduino```

```aur: yay -S arduino```

```nix: nix profile install nixpkgs#arduino```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[arduino-cli](/man/arduino-cli)(1), [avrdude](/man/avrdude)(1), [platformio](/man/platformio)(1)

# RESOURCES

```[Source code](https://github.com/arduino/Arduino)```

```[Homepage](https://www.arduino.cc)```

```[Documentation](https://docs.arduino.cc)```

<!-- verified: 2026-06-15 -->
