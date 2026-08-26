# TAGLINE

构建并运行 GStreamer 多媒体流水线

# TLDR

**播放视频文件**

```gst-launch-1.0 filesrc location=[video.mp4] ! decodebin ! autovideosink```

**显示测试视频图案**

```gst-launch-1.0 videotestsrc ! autovideosink```

**播放音频文件**

```gst-launch-1.0 filesrc location=[audio.mp3] ! decodebin ! autoaudiosink```

**显示摄像头画面**

```gst-launch-1.0 v4l2src ! autovideosink```

**从 RTSP 拉流**

```gst-launch-1.0 rtspsrc location=[rtsp://url] ! decodebin ! autovideosink```

**详细输出**

```gst-launch-1.0 -v videotestsrc ! autovideosink```

**中断时发送 EOS**

```gst-launch-1.0 -e filesrc location=[video.mp4] ! decodebin ! autovideosink```

# SYNOPSIS

**gst-launch-1.0** [_options_] _pipeline-description_

# PARAMETERS

**-v**, **--verbose**
> 详细输出，在流水线运行时打印属性和标签。

**-q**, **--quiet**
> 抑制状态输出（位置、进度）。

**-e**, **--eos-on-shutdown**
> 中断时发送 EOS 以便干净地关闭，而不是突然停止。

**-m**, **--messages**
> 输出发布到流水线总线上的消息。

**-t**, **--tags**
> 输出流中发现的标签（元数据）。

**-f**, **--no-fault**
> 不安装故障处理器（段错误回溯辅助工具）。

**--gst-debug=**_STRING_
> 为特定类别设置调试级别（例如 **GST_SCHEDULING:5**）。

**--gst-debug-level=**_N_
> 设置全局调试级别（0-9）。

**--gst-plugin-path=**_PATH_
> 添加额外目录以扫描插件。

# DESCRIPTION

**gst-launch-1.0** 从命令行构建并运行 GStreamer 多媒体流水线。元素之间用 **!**（感叹号）连接，属性用 **name=value** 语法设置。

Caps 过滤器约束元素之间的格式（例如 **video/x-raw,width=640,height=480**）。使用 **decodebin** 或 **playbin** 可以自动选择编解码器。

# CAVEATS

它面向测试和原型验证流水线，并非健壮的播放应用。按 Ctrl+C 停止；若未加 **-e**，流水线会立即停止而不是排空缓冲数据。

# INSTALL

```apt: sudo apt install gstreamer1.0-tools```

```apk: sudo apk add gstreamer-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gst-inspect-1.0](/man/gst-inspect-1.0)(1), [gst-discoverer-1.0](/man/gst-discoverer-1.0)(1), [ffmpeg](/man/ffmpeg)(1)

# RESOURCES

```[Homepage](https://gstreamer.freedesktop.org/)```

```[Source code](https://gitlab.freedesktop.org/gstreamer/gstreamer)```

```[Documentation](https://gstreamer.freedesktop.org/documentation/tools/gst-launch.html)```

<!-- verified: 2026-07-17 -->
