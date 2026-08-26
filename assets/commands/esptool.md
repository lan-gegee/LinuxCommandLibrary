# TAGLINE

Espressif 芯片固件烧录工具

# TLDR

在指定偏移处**烧录固件**

```esptool --port [/dev/ttyUSB0] write-flash 0x00000 [firmware.bin]```

**读取芯片信息**

```esptool --port [/dev/ttyUSB0] chip-id```

**擦除闪存**

```esptool --port [/dev/ttyUSB0] erase-flash```

**读取闪存到文件**

```esptool --port [/dev/ttyUSB0] read-flash 0 0x400000 [backup.bin]```

**以指定波特率烧录**

```esptool --port [/dev/ttyUSB0] --baud [921600] write-flash 0x0 [firmware.bin]```

**读取 MAC 地址**

```esptool --port [/dev/ttyUSB0] read-mac```

# SYNOPSIS

**esptool** [_options_] _command_ [_args_]

# PARAMETERS

**--port** _port_, **-p** _port_
> 串口设备。

**--baud** _rate_, **-b** _rate_
> 波特率（默认 115200）。

**--chip** _name_, **-c** _name_
> 目标芯片：esp8266、esp32、esp32s3 等。默认自动检测。

**--before** _action_ / **--after** _action_
> 连接前和完成后的复位行为（如 default-reset、hard-reset、no-reset）。

**chip-id**
> 读取芯片 ID。

**flash-id**
> 读取闪存芯片 ID 和容量。

**read-mac**
> 读取 MAC 地址。

**write-flash** _addr_ _file_
> 将二进制文件写入指定地址处的闪存。

**read-flash** _addr_ _size_ _file_
> 将闪存内容读出到文件。

**erase-flash**
> 擦除整个闪存。

**erase-region** _addr_ _size_
> 擦除闪存的某个区域。

**verify-flash** _addr_ _file_
> 将闪存内容与文件进行比对。

# DESCRIPTION

**esptool** 是向 Espressif 芯片（ESP8266、ESP32、ESP32-S2、ESP32-S3、ESP32-C3 等）烧录固件的官方工具。它通过串口通信来读取、写入和校验闪存。

该工具是 ESP32/ESP8266 开发不可或缺的部分，用于上传 Arduino sketch、MicroPython、ESPHome 及其他固件。多数情况下它会自动检测芯片类型和闪存参数。

# CAVEATS

需要 Python 和 pyserial。设备必须处于引导加载模式（复位时拉低 GPIO0，或在带 USB 转串口芯片的开发板上通过 RTS/DTR 线自动复位）。需要对串口的写权限，在 Linux 上通常意味着要加入 dialout 组。一次失败的烧录可能导致设备无法启动，但重新进入引导加载模式即可恢复。

自 **esptool v5** 起，所有命令和选项都改用连字符而非下划线（`write-flash` 而非 `write_flash`），推荐的调用方式是不带 `.py` 后缀的 `esptool`。旧的 `esptool.py` 名称和下划线写法仍然有效，但会打印弃用警告并计划移除。write-flash 的 `--verify` 选项已被删除，因为校验现在会自动执行。

# HISTORY

esptool 始于 **esptool.py**，由 **Espressif Systems** 开发，是其 ESP8266 和 ESP32 系列 WiFi/蓝牙微控制器的官方烧录工具。它是开源软件，与 ESP-IDF 框架一同积极维护。

# INSTALL

```dnf: sudo dnf install esptool```

```pacman: sudo pacman -S esptool```

```brew: brew install esptool```

```nix: nix profile install nixpkgs#esptool```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[python](/man/python)(1), [platformio](/man/platformio)(1), [arduino-cli](/man/arduino-cli)(1)

# RESOURCES

```[Source code](https://github.com/espressif/esptool)```

```[Documentation](https://docs.espressif.com/projects/esptool/)```

<!-- verified: 2026-07-14 -->
