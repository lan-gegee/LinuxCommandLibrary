# TAGLINE

从 V4L 设备捕获视频

# TLDR

**捕获单张 JPEG 图像**

```streamer -o [image.jpeg]```

**从指定视频设备捕获**

```streamer -c /dev/video[0] -o [image.jpeg]```

**录制视频到 AVI 文件**

```streamer -o [video.avi] -f mjpeg -t [00:30]```

**以指定分辨率捕获**

```streamer -s [640x480] -o [image.jpeg]```

**捕获图像序列**

```streamer -o [frame000.jpeg] -t [00:10] -r [5]```

**录制带音频的视频**

```streamer -o [video.avi] -f mjpeg -F stereo -t [01:00]```

**设置颜色深度**

```streamer -b [24] -o [image.jpeg]```

# SYNOPSIS

**streamer** [_options_]

# PARAMETERS

**-o** _file_
> 输出文件名。序列捕获时使用编号模式（file000.jpeg）。

**-c** _device_
> 视频捕获设备（默认为 /dev/video0）。

**-s** _WxH_
> 捕获分辨率（例如 320x240、640x480、720x480）。

**-r** _fps_
> 视频捕获的每秒帧数。

**-t** _time_
> 录制时长，采用 HH:MM:SS 或 MM:SS 格式。

**-f** _format_
> 输出格式：jpeg、ppm、pgm、mjpeg、rgb24、raw、avi。

**-F** _audio_
> 音频格式：mono 或 stereo。

**-b** _bpp_
> 颜色深度，单位为位/像素（15、16、24 或 32）。

**-n** _norm_
> 电视制式：ntsc、pal 或 secam。

**-i** _input_
> 视频输入源编号。

**-q**
> 静默模式，不显示输出消息。

**-h**
> 显示帮助信息。

# DESCRIPTION

**streamer** 是一个命令行实用程序，用于从网络摄像头、电视调谐器和其他 Video4Linux 设备捕获静态图像和视频。它是 xawtv 软件包的一部分，提供可脚本化的视频捕获功能，无需图形界面。

该工具可以捕获单张图像、定时图像序列或连续视频录制。输出格式包括用于图像的 JPEG 和用于视频的 MJPEG AVI。捕获图像序列时，如果输出文件名中包含零（例如 frame000.jpeg），则会自动生成带编号的文件名。

使用兼容的捕获设备时可支持视频录制的音频捕获。该工具适用于延时摄影、监控和自动化图像采集场景。

# CAVEATS

需要 Video4Linux（V4L/V4L2）兼容的捕获设备。某些发行版将 streamer 与 xawtv 分开打包为 xawtv-tools 或 v4l-tools。格式支持取决于硬件能力。对于现代网络摄像头，建议使用 ffmpeg，它提供更多格式选项。

# HISTORY

**streamer** 作为 xawtv 项目的一部分开发，xawtv 是一套面向 Linux 的模拟电视和视频采集工具。它在图形化的 xawtv 应用之外提供了命令行捕获功能。该工具早于许多现代采集工具出现，在简单的基于 V4L 的采集任务中仍然有用。

# INSTALL

```apt: sudo apt install streamer```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ffmpeg](/man/ffmpeg)(1), [v4l2-ctl](/man/v4l2-ctl)(1), [cheese](/man/cheese)(1)
