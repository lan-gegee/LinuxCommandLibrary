# TAGLINE

用 Raspberry Pi 相机拍摄 JPEG 图像

# TLDR

**拍摄**图像并保存到文件

```rpicam-jpeg -o path/to/file.jpg```

按**设定的尺寸**拍摄

```rpicam-jpeg -o path/to/file.jpg --width 1920 --height 1080```

使用**长曝光**和增益拍摄

```rpicam-jpeg -o path/to/file.jpg --shutter 20000 --gain 1.5```

# SYNOPSIS

**rpicam-jpeg** [_options_]

# PARAMETERS

**-o**, **--output** _file_
> 输出文件路径

**--width** _pixels_
> 图像宽度

**--height** _pixels_
> 图像高度

**--shutter** _microseconds_
> 曝光时间

**--gain** _value_
> 传感器增益倍数

# DESCRIPTION

**rpicam-jpeg** 使用 Raspberry Pi 相机模块拍摄并保存 JPEG 图像。它提供对分辨率、曝光以及其他相机设置的控制。

该工具针对快速 JPEG 拍摄进行了优化，并自动完成相关处理。

# CAVEATS

需要兼容的 Raspberry Pi 相机模块。长曝光时间可能引入噪点。

# HISTORY

属于 **rpicam-apps**，即基于 libcamera 的官方 Raspberry Pi 相机应用套件。

# SEE ALSO

[rpicam-still](/man/rpicam-still)(1), [rpicam-hello](/man/rpicam-hello)(1), [rpicam-vid](/man/rpicam-vid)(1)
