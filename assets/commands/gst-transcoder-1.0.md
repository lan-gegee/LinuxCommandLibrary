# TAGLINE

GStreamer 媒体转码器

# TLDR

**将视频文件转码**为 WebM 格式（根据扩展名自动检测）

```gst-transcoder-1.0 file:///[path/to/input.mp4] file:///[path/to/output.webm]```

**以指定的编码格式转码**

```gst-transcoder-1.0 file:///[path/to/input.mp4] file:///[path/to/output.mkv] "[encoding_format]"```

**转码并调整尺寸**，将视频缩放到指定帧大小

```gst-transcoder-1.0 -s [1280x720] file:///[path/to/input.mp4] file:///[path/to/output.mp4]```

**以指定的视频帧率转码**

```gst-transcoder-1.0 -f [30/1] file:///[path/to/input.mp4] file:///[path/to/output.mp4]```

**列出所有可用的编码目标**

```gst-transcoder-1.0 -l```

转码期间**限制 CPU 占用**

```gst-transcoder-1.0 -c [50] file:///[path/to/input.mp4] file:///[path/to/output.mp4]```

# SYNOPSIS

**gst-transcoder-1.0** [_options_] _input-uri_ _output-uri_ [_encoding-format_[/_profile-name_]]

# PARAMETERS

**-h**, **--help**
> 显示帮助选项。

**--help-all**
> 显示所有帮助选项。

**--help-gst**
> 显示 GStreamer 特有选项。

**-c**, **--cpu-usage** _PERCENT_
> 转码进程的目标 CPU 占用百分比。

**-l**, **--list-targets**
> 列出所有可用的编码目标并退出。

**-s**, **--size** _WxH_
> 设置输出的视频帧大小（例如 1280x720）。

**-r**, **--audio-rate** _HZ_
> 设置音频采样率（Hz）。

**-f**, **--framerate** _FRACTION_
> 以分数（例如 24/1）或单个数字（例如 24）设置视频帧率。

**-v**, **--video-encoder** _ENCODER_
> 指定要使用的视频编码器元素。

# DESCRIPTION

**gst-transcoder-1.0** 是一款命令行工具，它使用 GStreamer 框架将多媒体流从一种格式转码为另一种格式。它从输入 URI 读取、处理媒体，并以指定的编码格式写入输出 URI。

编码格式可以显式指定为序列化字符串（例如 **muxer_caps:video_caps:audio_caps**），也可以是来自 **.gep** 配置文件的命名目标，还可以完全省略，让工具根据输出文件扩展名推测格式。

该工具内部使用 GStreamer Transcoder API，借助 **decodebin** 和 **encodebin** 元素实现自动格式检测和编码。

# CAVEATS

输入和输出路径必须以 **file:///** 前缀的 URI 形式给出，而不是普通文件路径。可用的编码格式取决于系统上安装了哪些 GStreamer 插件。CPU 占用限制只是近似值，并受系统负载影响。复杂的转码场景可能需要显式指定编码格式字符串，而不能依赖扩展名检测。

# HISTORY

**gst-transcoder-1.0** 最初作为 **Pitivi** 视频编辑器项目的一部分开发，用于提供转码功能。它后来被整合进 **gst-plugins-bad**，成为标准的 GStreamer 工具。该工具构建在 GstTranscoder 库之上，后者在 GStreamer 的流水线框架之上提供了简化后的高级媒体转码 API。

# INSTALL

```apt: sudo apt install gstreamer1.0-plugins-bad-apps```

```pacman: sudo pacman -S gst-plugins-bad```

```apk: sudo apk add gst-plugins-bad```

```brew: brew install gst-plugins-bad```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gst-launch-1.0](/man/gst-launch-1.0)(1), [gst-inspect-1.0](/man/gst-inspect-1.0)(1), [ges-launch-1.0](/man/ges-launch-1.0)(1), [ffmpeg](/man/ffmpeg)(1)
