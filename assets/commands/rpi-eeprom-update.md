# TAGLINE

更新 Raspberry Pi 引导加载器 EEPROM 固件

# TLDR

打印**当前 EEPROM** 版本和更新状态

```sudo rpi-eeprom-update```

如有更新的固件则**应用**更新

```sudo rpi-eeprom-update -a```

**取消**待处理的更新

```sudo rpi-eeprom-update -r```

使用指定的**固件目录**进行更新

```sudo rpi-eeprom-update -d [/lib/firmware/raspberrypi/bootloader/stable]```

显示**帮助**

```rpi-eeprom-update -h```

# SYNOPSIS

**rpi-eeprom-update** [_options_]

# PARAMETERS

**-a**
> 如有更新版本则应用更新。更新将在下次重启时安装。

**-d** _directory_
> 使用指定的固件镜像目录而非默认目录。

**-j** _file_
> 以 JSON 格式将输出写入文件（输出到 stdout 请用 /dev/stdout）。

**-l**
> 仅显示更新状态，不检查是否存在更新的固件。

**-m**
> 显示有关 recovery.bin 引导加载器更新文件的信息。

**-r**
> 取消待处理的更新，并恢复为当前的 EEPROM 内容。

**-h**
> 显示帮助。

# DESCRIPTION

**rpi-eeprom-update** 管理 Raspberry Pi 4、400、Compute Module 4 和 Pi 5 型号上的引导加载器 EEPROM 固件。EEPROM 包含在操作系统加载之前初始化系统的引导代码，包括 USB 启动、网络启动和 NVMe 启动支持。

固件镜像位于 **/lib/firmware/raspberrypi/bootloader/** 目录下，划分为多个发布通道：**critical**（极少更新，稳定性最高）、**stable**（默认，推荐）、**beta**（包含新功能，测试较少）和 **latest**（最新版本）。

更新可以提升启动可靠性、增加新的启动模式等特性，并修复底层引导固件中的缺陷。

# CAVEATS

EEPROM 更新会在下次重启时应用。更新过程中断电可能需要使用 recovery.bin 通过 SD 卡进行恢复。只使用官方更新源。可通过编辑 **/etc/default/rpi-eeprom-update** 来更改更新通道。

# HISTORY

随 **Raspberry Pi 4**（2019 年）引入，该型号采用基于 EEPROM 的启动方式，取代了早期型号使用的 SD 卡启动。后来扩展到支持 Raspberry Pi 5 和 Compute Module 各个变体。

# SEE ALSO

[raspi-config](/man/raspi-config)(1), [vcgencmd](/man/vcgencmd)(1), [rpi-otp-private-key](/man/rpi-otp-private-key)(1)
