# TAGLINE

为嵌入式系统提供调试、在系统编程和边界扫描测试

# TLDR

使用接口与目标配置文件**启动**

```openocd -f [interface/stlink.cfg] -f [target/stm32f4x.cfg]```

**烧写 Flash**并进行校验和复位

```openocd -f [interface.cfg] -f [target.cfg] -c "program [firmware.elf] verify reset exit"```

在指定地址**烧写 hex 文件**

```openocd -f [interface.cfg] -f [target.cfg] -c "program [firmware.hex] 0x08000000 verify reset exit"```

使用板级配置**启动**（含接口与目标）

```openocd -f [board/stm32f4discovery.cfg]```

**启动并让 GDB 服务器**监听自定义端口

```openocd -f [config.cfg] -c "gdb_port [4444]"```

将 Flash 内存**转储**为二进制文件

```openocd -f [config.cfg] -c "init" -c "dump_image [output.bin] 0x08000000 0x10000" -c "exit"```

**擦除**整个 Flash 内存

```openocd -f [interface.cfg] -f [target.cfg] -c "init" -c "reset halt" -c "flash erase_sector 0 0 last" -c "exit"```

**启用**详细调试输出

```openocd -d3 -f [interface.cfg] -f [target.cfg]```

# SYNOPSIS

**openocd** [_-f config_] [_-c command_] [_-d level_] [_options_]

# PARAMETERS

**-f** _FILE_
> 配置文件。

**-c** _CMD_
> 运行命令。

**-s** _DIR_
> 搜索目录。

**-d** _LEVEL_
> 调试级别（0-4，默认 2）。数值越大输出越多。

**-l** _FILE_
> 将日志输出到文件而不是 stderr。

**-p**, **--pipe**
> 使用管道而不是 TCP 与 GDB 通信。

**--version**
> 显示版本。

**--help**
> 显示帮助。

# DESCRIPTION

**openocd**（Open On-Chip Debugger）为嵌入式系统提供调试、在系统编程和边界扫描测试。它通过 JTAG、SWD 和其他调试适配器访问微控制器和 FPGA。

配置文件定义调试适配器（interface）和目标设备。安装中自带许多板卡和适配器的预定义配置。

编程模式会将固件烧写到微控制器。verify 用于确认写入成功。reset 用于启动新固件。

作为服务器运行时，OpenOCD 提供 GDB 服务器（端口 3333）和 telnet 接口（端口 4444）。GDB 可连接进行源码级调试。

telnet 接口允许直接执行命令：halt、resume、step、内存读写、寄存器访问和断点管理。

可以同时调试多个目标。支持包含多个设备的 JTAG 链。

# CAVEATS

需要相应的适配器硬件。目标配置必须与设备匹配。某些功能取决于所用的适配器。可能需要 udev 规则才能获得调试权限。

# HISTORY

**OpenOCD** 由 **Dominic Rath** 于 **2005 年**作为大学项目启动。它后来成为事实标准的开源片上调试器，支持数百种目标设备和调试适配器。目前由社区持续治理开发。

# INSTALL

```apt: sudo apt install openocd```

```dnf: sudo dnf install openocd```

```pacman: sudo pacman -S openocd```

```apk: sudo apk add openocd```

```zypper: sudo zypper install openocd```

```brew: brew install openocd```

```nix: nix profile install nixpkgs#openocd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gdb](/man/gdb)(1), [arm-none-eabi-gdb](/man/arm-none-eabi-gdb)(1), [stlink](/man/stlink)(1), [st-flash](/man/st-flash)(1), [avrdude](/man/avrdude)(1), [flashrom](/man/flashrom)(1)
