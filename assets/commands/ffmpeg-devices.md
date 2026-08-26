# TAGLINE

ffmpeg 的硬件采集设备支持

# TLDR

**列出可用设备**

```ffmpeg -devices```

从摄像头**采集**

```ffmpeg -f v4l2 -i [/dev/video0] [output.mp4]```

录制屏幕（X11）

```ffmpeg -f x11grab -i [:0.0] [screen.mp4]```

**采集音频设备**

```ffmpeg -f alsa -i [hw:0] [audio.wav]```

列出摄像头支持的格式

```ffmpeg -f v4l2 -list_formats all -i [/dev/video0]```

# SYNOPSIS

**ffmpeg** **-f** _device_ [_options_] **-i** _source_ _output_

# PARAMETERS

**-f** _DEVICE_
> 设备类型：v4l2、x11grab、alsa、pulse、dshow。

**-i** _SOURCE_
> 设备路径或标识符。

**v4l2**
> Video4Linux2 摄像头采集。

**x11grab**
> X11 屏幕采集。

**alsa**
> ALSA 音频采集。

**pulse**
> PulseAudio 采集。

**dshow**
> DirectShow（Windows）采集。

**-list_devices**
> 列出可用设备。

# DESCRIPTION

**ffmpeg devices** 支持从摄像头、麦克风和屏幕等硬件源采集。设备特定的输入格式提供对系统多媒体硬件的访问。

不同平台有不同的设备类型：Linux 上是 v4l2 和 x11grab，macOS 上是 avfoundation，Windows 上是 dshow。每种设备类型都有针对分辨率、帧率和格式的特定选项。

设备采集支持对实时输入源进行录制、推流和实时处理。

# CAVEATS

设备名称因平台而异。可能需要相应权限。屏幕采集性能取决于系统。音频同步可能较难处理。

# HISTORY

ffmpeg 的设备支持随多媒体硬件 API 一同演进。V4L2 支持随 Linux 视频设备而来，而屏幕抓取能力则是为录制和推流场景而添加的。

# INSTALL

```apt: sudo apt install ffmpeg```

```pacman: sudo pacman -S ffmpeg```

```apk: sudo apk add ffmpeg```

```brew: brew install ffmpeg```

```nix: nix profile install nixpkgs#ffmpeg```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ffmpeg](/man/ffmpeg)(1), [ffprobe](/man/ffprobe)(1), [v4l2-ctl](/man/v4l2-ctl)(1)

# RESOURCES

```[Homepage](https://ffmpeg.org/)```

```[Documentation](https://ffmpeg.org/ffmpeg-devices.html)```

<!-- verified: 2026-07-15 -->
