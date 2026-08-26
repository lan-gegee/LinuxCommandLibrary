# TAGLINE

从 Raspberry Pi 相机捕获原始传感器数据

# TLDR

**捕获**指定时长（毫秒）的原始视频

```rpicam-raw -t 2000 -o path/to/file.raw```

使用**自定义尺寸**和帧率拍摄

```rpicam-raw -t 5000 --width 4056 --height 3040 -o path/to/file.raw --framerate 8```

# SYNOPSIS

**rpicam-raw** [_options_]

# PARAMETERS

**-t**, **--timeout** _ms_
> 录制时长（毫秒）

**-o**, **--output** _file_
> 输出文件路径

**--width** _pixels_
> 视频宽度

**--height** _pixels_
> 视频高度

**--framerate** _fps_
> 每秒帧数

# DESCRIPTION

**rpicam-raw** 从 Raspberry Pi 相机捕获未经处理的原始视频。原始视频保留全部传感器数据且不做压缩，适合后期处理。

由于原始视频未压缩，输出文件可能会很大。

# CAVEATS

原始视频文件非常庞大。请确保有足够的存储空间和高速的存储介质。查看原始输出需要借助后期处理软件。

# HISTORY

属于 **rpicam-apps**，即基于 libcamera 的官方 Raspberry Pi 相机应用套件。

# SEE ALSO

[rpicam-vid](/man/rpicam-vid)(1), [rpicam-still](/man/rpicam-still)(1)
