# TAGLINE

显示树莓派软硬件信息

# TLDR

显示**系统信息**

```raspinfo```

以**分页方式**显示系统信息

```raspinfo | more```

# SYNOPSIS

**raspinfo**

# DESCRIPTION

**raspinfo** 显示树莓派设备的全面系统信息。它收集并展示硬件细节、OS 版本、内存使用、CPU 信息和其他诊断数据。

输出内容包括树莓派型号识别、固件版本、温度读数和配置设置。它适合用于故障排查和系统文档记录。

# OUTPUT

显示内容：
- 树莓派型号与修订版本
- OS 和内核版本
- CPU 和内存信息
- 视频配置
- 网络接口
- USB 设备
- 温度和电压
- 时钟频率与内存分配

# CAVEATS

仅适用于树莓派的工具，即使在 Lite 版镜像中也默认安装。输出格式为提交技术支持工单而设计。某些信息需要 root 权限才能显示完整细节。

# HISTORY

**raspinfo** 是 Raspberry Pi 工具包的一部分，由 Raspberry Pi 基金会创建，帮助用户收集系统信息以便进行故障排查和技术支持。

# SEE ALSO

[raspi-config](/man/raspi-config)(1), [vcgencmd](/man/vcgencmd)(1), [pinout](/man/pinout)(1)
