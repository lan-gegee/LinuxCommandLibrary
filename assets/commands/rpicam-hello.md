# TAGLINE

显示 Raspberry Pi 相机预览

# TLDR

在**指定时长**内显示相机预览（毫秒）

```rpicam-hello -t 5000```

为相机传感器使用**自定义调谐**文件

```rpicam-hello --tuning-file /usr/share/libcamera/ipa/rpi/path/to/config.json```

# SYNOPSIS

**rpicam-hello** [_options_]

# PARAMETERS

**-t**, **--timeout** _ms_
> 预览持续时间（毫秒）

**--tuning-file** _file_
> 相机传感器调谐配置

# DESCRIPTION

**rpicam-hello** 显示来自 Raspberry Pi 相机模块的实时预览画面。它是验证相机功能、查看相机输出的最简单方式。

该工具使用 libcamera 为 Raspberry Pi 提供现代相机支持。

# CAVEATS

需要兼容的 Raspberry Pi 相机模块。显示输出需要正常工作的图形环境或 framebuffer。

# HISTORY

属于 **rpicam-apps**，即官方的 Raspberry Pi 相机应用套件，用于取代旧的 raspistill/raspivid 工具。

# SEE ALSO

[rpicam-still](/man/rpicam-still)(1), [rpicam-vid](/man/rpicam-vid)(1), [rpicam-jpeg](/man/rpicam-jpeg)(1)
