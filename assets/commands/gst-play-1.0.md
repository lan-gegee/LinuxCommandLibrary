# TAGLINE

基于 GStreamer 的简单命令行媒体播放工具

# TLDR

**播放媒体文件**

```gst-play-1.0 [path/to/file.mp4]```

**播放多个文件**

```gst-play-1.0 [file1.mp3] [file2.mp3] [file3.mp3]```

递归**播放目录中的所有媒体文件**

```gst-play-1.0 [path/to/directory]```

**使用指定的视频输出端播放文件**

```gst-play-1.0 --videosink=ximagesink [path/to/file.mp4]```

**随机顺序播放文件**

```gst-play-1.0 --shuffle [file1.mp3] [file2.mp3] [file3.mp3]```

**启用无缝播放模式播放文件**

```gst-play-1.0 --gapless [file1.mp3] [file2.mp3]```

**播放 URI 流**

```gst-play-1.0 [https://example.com/stream.mp3]```

**以一半音量播放文件**

```gst-play-1.0 --volume=0.5 [path/to/file.mp3]```

# SYNOPSIS

**gst-play-1.0** [_options_] _FILE_|_DIRECTORY_|_URI_ [_FILE2_|_DIRECTORY2_|_URI2_ ...]

# PARAMETERS

**--audiosink=**_SINK_
> 使用指定的音频输出端代替 **autoaudiosink**。

**--videosink=**_SINK_
> 使用指定的视频输出端代替 **autovideosink**。

**--volume=**_VOLUME_
> 设置初始播放音量。**0.0** 为静音，**1.0** 为不改变音量（默认）。

**--shuffle**
> 随机顺序播放文件。

**--no-interactive**
> 禁用交互式键盘控制。

**--gapless**
> 启用曲目之间的无缝（gapless）播放。

**-v**, **--verbose**
> 输出状态信息和属性通知。

**-q**, **--quiet**
> 抑制除错误外的所有输出。

**--use-playbin3**
> 使用 playbin3 流水线代替默认的 playbin。

**--wait-on-eos**
> 播放结束后保持最后一帧视频显示，而不是直接关闭。

**--flags**
> 通过 playbin 的 **flags** 属性控制播放行为。

**--version**
> 打印版本信息并退出。

**--help**
> 显示可用选项并退出。

# DESCRIPTION

**gst-play-1.0** 是一款命令行播放测试工具，它使用 GStreamer 的 **playbin** 元素来播放音频和视频文件。它接受单个文件、目录（会递归遍历）和 URI 作为输入。

该工具在播放期间提供交互式键盘控制，可用于暂停、跳转、调节音量、改变播放速度，以及在音频、视频和字幕轨道之间切换。它支持无缝播放以实现曲目间的平滑过渡，并能播放本地文件或网络流中的媒体。

# INTERACTIVE CONTROLS

```
SPACE     Pause / Resume
Arrow Up/Down    Volume up / down
Arrow Left/Right Seek backward / forward 10 seconds
+/-       Increase / decrease playback rate
d         Reverse playback direction
t         Cycle trick modes
a         Cycle audio tracks
s         Cycle subtitle tracks
v         Cycle video tracks
> or n    Next track in playlist
< or b    Previous track in playlist
0         Seek back to beginning
Q or ESC  Quit
```

# CAVEATS

**gst-play-1.0** 定位为测试与调试工具，而非功能完备的媒体播放器。播放能力完全取决于系统上安装了哪些 GStreamer 插件。缺少编解码器会导致播放错误。交互式键盘控制需要终端，当 stdin 不是 TTY 时将被禁用。

# HISTORY

**gst-play-1.0** 作为 **GStreamer** 多媒体框架基础插件的一部分推出。GStreamer 本身由 **Erik Walthinsen** 于 **1999 年**创建，如今已发展为 Linux 上标准的多媒体框架。play 工具提供了一种简单的方式来测试播放流水线，无需通过 **gst-launch-1.0** 手工构建。当 GStreamer 在 **2012 年**过渡到 1.x 系列时，它取代了较旧的 **gst-play-0.10** 工具。

# INSTALL

```apt: sudo apt install gstreamer1.0-plugins-base-apps```

```pacman: sudo pacman -S gst-plugins-base```

```apk: sudo apk add gst-plugins-base```

```brew: brew install gst-plugins-base```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gst-launch-1.0](/man/gst-launch-1.0)(1), [gst-inspect-1.0](/man/gst-inspect-1.0)(1), [gst-discoverer-1.0](/man/gst-discoverer-1.0)(1), [ffplay](/man/ffplay)(1), [mpv](/man/mpv)(1)
