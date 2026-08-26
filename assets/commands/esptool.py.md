# TAGLINE

ESP8266 与 ESP32 系列烧录工具

# TLDR

向 ESP 开发板**烧录固件**

```esptool.py --port [/dev/ttyUSB0] write_flash 0x0 [firmware.bin]```

**读取芯片信息和** MAC 地址

```esptool.py --port [/dev/ttyUSB0] chip_id```

**擦除整个**闪存

```esptool.py --port [/dev/ttyUSB0] erase_flash```

**将闪存读取到**文件

```esptool.py --port [/dev/ttyUSB0] read_flash 0x0 0x100000 [backup.bin]```

**识别 SPI** 闪存芯片

```esptool.py --port [/dev/ttyUSB0] flash_id```

**设置波特率**以加快烧录速度

```esptool.py --port [/dev/ttyUSB0] --baud [921600] write_flash 0x0 [firmware.bin]```

**读取 MAC** 地址

```esptool.py --port [/dev/ttyUSB0] read_mac```

# SYNOPSIS

**esptool.py** [_options_] _command_ [_args_]

# PARAMETERS

_COMMAND_
> 操作：write_flash、read_flash、erase_flash、chip_id、flash_id、read_mac 等。

**--port** _PORT_
> 串口设备（例如 /dev/ttyUSB0、COM3）。

**--baud** _RATE_
> 串口波特率（默认：115200）。

**--chip** _CHIP_
> 目标芯片类型（auto、esp8266、esp32、esp32s2、esp32s3、esp32c3 等）。

**--before** _ACTION_
> 连接前的动作：default_reset、no_reset、no_reset_no_sync。

**--after** _ACTION_
> 操作完成后的动作：hard_reset（默认）、soft_reset、no_reset、no_reset_stub。

**--no-stub**
> 禁用 stub 加载器；直接与 ROM bootloader 通信。

**write_flash** _ADDR_ _FILE_ [_ADDR_ _FILE_ ...]
> 将一个或多个二进制文件写入指定地址处的闪存。

**read_flash** _ADDR_ _SIZE_ _FILE_
> 将闪存内容读出到文件。

**erase_flash**
> 擦除整个闪存。

**erase_region** _ADDR_ _SIZE_
> 擦除指定的闪存区域（必须按 4096 字节的扇区对齐）。

**chip_id**
> 读取芯片 ID。

**flash_id**
> 读取 SPI 闪存的厂商 ID 和设备 ID。

**read_mac**
> 显示固化在芯片中的 MAC 地址。

**image_info** _FILE_
> 显示二进制镜像文件的元数据。

**merge_bin** _-o_ _OUTPUT_ _ADDR_ _FILE_ [_ADDR_ _FILE_ ...]
> 将多个二进制文件合并为单个可烧录文件。

**--help**
> 显示帮助信息。

# DESCRIPTION

**esptool.py** 是 Espressif ESP8266、ESP32、ESP32-S2、ESP32-S3、ESP32-C3 等 ESP 系列芯片的官方烧录工具。它通过串口通信来烧录固件、读写闪存并管理启动过程。

该工具处理 bootloader 通信、闪存布局以及各种芯片特定的要求。支持多种闪存容量、频率和模式（qio、qout、dio、dout）。默认情况下，数据传输时会进行压缩以提高性能。

esptool.py 是 ESP 开发不可或缺的工具，Arduino IDE、PlatformIO 和 ESP-IDF 都用它来部署固件。

# CAVEATS

需要 USB 转接器的串口驱动（例如 CP210x、CH340）。某些开发板上可能需要手动控制 GPIO0 才能进入引导模式。闪存地址因芯片而异。更高的波特率可以提升速度，但可能降低可靠性。erase_region 的地址和大小必须按 4096 字节扇区边界对齐。

# HISTORY

esptool.py 由 **Espressif Systems** 开发，是其 ESP8266 和 ESP32 系列 WiFi/蓝牙微控制器的官方工具，在物联网项目中广泛使用。它是开源软件，可通过 PyPI 安装（`pip install esptool`）。

# SEE ALSO

[platformio](/man/platformio)(1), [arduino-cli](/man/arduino-cli)(1)
