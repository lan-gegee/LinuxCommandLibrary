# TAGLINE

用 Raspberry Pi 相机拍摄静态图像

# TLDR

**立即**拍摄图像（无预览）

```rpicam-still -n -o path/to/file.jpg```

以**不同的编码**格式拍摄

```rpicam-still -e png -o path/to/file.png```

拍摄**原始图像**（在 JPEG 之外附带 DNG）

```rpicam-still -r -o path/to/file.jpg```

以微秒级的**长曝光**拍摄

```rpicam-still --shutter 100000 -o path/to/file.jpg```

按**指定尺寸**拍摄

```rpicam-still --width 1920 --height 1080 -o path/to/file.jpg```

拍摄**延时序列**（10 分钟内每 10 秒一张）

```rpicam-still -t 600000 --timelapse 10000 -o image%04d.jpg```

# SYNOPSIS

**rpicam-still** [_options_]

# PARAMETERS

**-o**, **--output** _file_
> 输出文件路径（延时摄影编号请使用 _%d_）。

**-e**, **--encoding** _format_
> 输出格式（jpg、png、bmp、rgb、yuv420）。

**-r**, **--raw**
> 同时将原始 Bayer 传感器数据保存为 DNG 文件。

**-n**, **--nopreview**
> 禁用预览窗口。

**-t**, **--timeout** _ms_
> 拍摄前预览持续的时间（毫秒）（默认：5000）。

**--immediate**
> 跳过预览阶段并立即拍摄。

**--timelapse** _ms_
> 每 _ms_ 毫秒拍摄一张图像，直到超时为止。

**--width** _px_, **--height** _px_
> 输出图像尺寸。

**-q**, **--quality** _0-100_
> JPEG 压缩质量。

**--shutter** _microseconds_
> 手动曝光时间。

**--gain** _value_
> 模拟增益（ISO 倍数）。

**--awb** _mode_
> 自动白平衡模式（auto、incandescent、tungsten、fluorescent、indoor、daylight、cloudy）。

# DESCRIPTION

**rpicam-still** 用于拍摄照片，并提供 rpicam-jpeg 所没有的更多格式选项和功能。它支持多种输出格式以及原始传感器数据采集。

比起更简单的 rpicam-jpeg，该工具对图像拍摄提供了更多控制。

# CAVEATS

原始图像会在主图像之外附带 DNG 数据。某些格式生成的文件比 JPEG 更大。

# HISTORY

属于 **rpicam-apps**，即基于 libcamera 的官方 Raspberry Pi 相机应用套件。取代旧的 raspistill。

# SEE ALSO

[rpicam-jpeg](/man/rpicam-jpeg)(1), [rpicam-hello](/man/rpicam-hello)(1), [rpicam-vid](/man/rpicam-vid)(1)
