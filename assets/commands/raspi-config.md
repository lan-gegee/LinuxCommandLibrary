# TAGLINE

树莓派系统配置工具

# TLDR

启动 **raspi-config** 工具

```sudo raspi-config```

# SYNOPSIS

**raspi-config** [_nonint_options_]

# DESCRIPTION

**raspi-config** 是运行 Raspberry Pi OS 的树莓派的官方配置工具。它提供基于 ncurses 的菜单界面，用于设置常见的系统选项。

配置选项包括网络设置、显示选项、接口启用（SSH、VNC、SPI、I2C）、性能调优、本地化和系统更新。许多原本需要手动编辑文件才能完成的设置都可以通过该工具完成。

# MENU CATEGORIES

- **System Options（系统选项）**: 主机名、密码、启动行为、网络启动
- **Display Options（显示选项）**: 分辨率、过扫描（overscan）、像素加倍
- **Interface Options（接口选项）**: SSH、VNC、SPI、I2C、串口、1-Wire、GPIO 远程
- **Performance Options（性能选项）**: GPU 内存、风扇控制、overlay 文件系统
- **Localization Options（本地化选项）**: 区域设置、时区、键盘、WLAN 国家
- **Advanced Options（高级选项）**: 扩展文件系统、网络代理、启动顺序

# CONFIGURATION

**/boot/firmware/config.txt**
> 硬件配置文件，控制 GPU 内存、显示设置、设备树 overlay 和启动参数，raspi-config 会修改其中的内容。

**/etc/default/locale**
> 通过本地化菜单管理的系统区域设置。

# CAVEATS

仅适用于树莓派，其他系统不可用。需要 root 权限。某些更改需要重启才能生效。提供非交互模式以便脚本化使用。

# HISTORY

**raspi-config** 由 Raspberry Pi 基金会开发，是 Raspberry Pi OS 的一部分，旨在为不熟悉 Linux 命令行管理的用户简化配置。

# SEE ALSO

[pinout](/man/pinout)(1), [vcgencmd](/man/vcgencmd)(1), [raspi-gpio](/man/raspi-gpio)(1)
