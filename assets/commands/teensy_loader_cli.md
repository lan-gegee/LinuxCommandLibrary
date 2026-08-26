# TAGLINE

命令行 Teensy 微控制器固件烧录器

# TLDR

**烧录** Teensy 3.2/3.1 的 hex 文件（等待按钮按下）

```teensy_loader_cli --mcu=mk20dx256 -w [blink.hex]```

**使用开发板名称别名烧录**

```teensy_loader_cli --mcu=TEENSY32 -w [firmware.hex]```

**烧录 Teensy 4.0**

```teensy_loader_cli --mcu=TEENSY40 -w [firmware.hex]```

**软重启**后烧录（Linux）

```teensy_loader_cli --mcu=TEENSY32 -s -w [firmware.hex]```

**烧录后不重启**进入应用程序

```teensy_loader_cli --mcu=TEENSY32 -n -w [firmware.hex]```

**详细模式**烧录

```teensy_loader_cli --mcu=TEENSY32 -v -w [firmware.hex]```

# SYNOPSIS

**teensy_loader_cli** **--mcu=**_MCU_ [**-w**] [**-r**] [**-s**] [**-n**] [**-v**] *file.hex*

# DESCRIPTION

**teensy_loader_cli** 是 PJRC 的命令行版 Teensy Loader，用于自动化固件上传（通常在 Makefile 中调用）。大多数交互式用户更偏好处于自动模式的图形化烧录器；这个 CLI 面向高级/CI 工作流。

必须用 **--mcu=** 指定目标 MCU。取值可以是 gcc 风格的芯片名或逻辑板卡名，例如 **TEENSY32**、**TEENSY40**、**TEENSY41**、**TEENSYLC** 等，完整列表见项目 README。

在 Linux 上，非 root 访问通常需要安装 https://www.pjrc.com/teensy/00-teensy.rules 提供的 Teensy udev 规则。从源码构建需要 **gcc**，通常还需要 libusb 开发包（Debian/Ubuntu 上为 **libusb-dev**）。

# PARAMETERS

**--mcu=**_MCU_

> 必需。目标处理器或板卡别名（例如 **mk20dx256**、**TEENSY32**、**TEENSY40**、**imxrt1062**、**mkl26z64**、**atmega32u4**）。

**-w**

> 等待设备出现（HalfKay / 按钮按下）。hex 文件会在等待前读取一次，检测到设备后再读取一次。

**-r**

> 通过另一块运行 rebootor 代码的 Teensy 进行硬重启（C7 引脚接复位）。可实现完全无人值守烧录。

**-s**

> Linux 上的软重启请求：查找正在运行 Teensyduino USB Serial 的 Teensy 并请求其重启进入引导加载程序。

**-n**

> 烧录后不重启进入应用程序；让 HalfKay 继续运行。

**-v**

> 详细的状态输出。

*file.hex*

> 要烧录的 Intel HEX 固件映像。

# CAVEATS

烧录为错误芯片编译的 HEX 可能使 USB PLL 初始化挂起并干扰主机的 USB 端口；恢复时可能需要在连接 USB 前按住复位按钮。请使用匹配的 udev 规则。一次性烧录用图形化烧录器更简单。

# INSTALL

```apt: sudo apt install teensy-loader-cli```

```pacman: sudo pacman -S teensy_loader_cli```

```brew: brew install teensy_loader_cli```

```nix: nix profile install nixpkgs#teensy-loader-cli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[avrdude](/man/avrdude)(1), [dfu-util](/man/dfu-util)(1), [openocd](/man/openocd)(1)

# RESOURCES

```[Source code](https://github.com/PaulStoffregen/teensy_loader_cli)```

```[Homepage](https://www.pjrc.com/teensy/loader_cli.html)```

<!-- verified: 2026-07-19 -->
