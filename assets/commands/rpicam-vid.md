# TAGLINE

用 Raspberry Pi 相机录制视频

# TLDR

**录制**一段 10 秒的视频

```rpicam-vid -t 10000 -o path/to/file.h264```

# SYNOPSIS

**rpicam-vid** [_options_]

# PARAMETERS

**-t**, **--timeout** _ms_
> 录制时长（毫秒）

**-o**, **--output** _file_
> 输出文件路径（.h264、.mp4 等）

# DESCRIPTION

**rpicam-vid** 使用 Raspberry Pi 相机录制编码后的视频。默认生成 H.264 编码的视频，可直接播放或进一步处理。

该工具支持多种输出格式和编码选项，以适应不同的使用场景。

# CAVEATS

H.264 裸流在某些播放器中可能需要封装容器。如有需要，可用 ffmpeg 或类似工具将其转换为 MP4。

# HISTORY

属于 **rpicam-apps**，即基于 libcamera 的官方 Raspberry Pi 相机应用套件。取代旧的 raspivid。

# SEE ALSO

[rpicam-raw](/man/rpicam-raw)(1), [rpicam-still](/man/rpicam-still)(1), [vlc](/man/vlc)(1), [ffmpeg](/man/ffmpeg)(1)
