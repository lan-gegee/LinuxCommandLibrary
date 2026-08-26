# TAGLINE

GStreamer 媒体文件元数据分析器

# TLDR

**显示媒体文件信息**

```gst-discoverer-1.0 [video.mp4]```

**显示详细信息**

```gst-discoverer-1.0 -v [video.mp4]```

**分析整个目录**

```gst-discoverer-1.0 [/path/to/directory]```

**从 URL 分析**

```gst-discoverer-1.0 [https://example.com/video.webm]```

**显示目录（TOC）信息**

```gst-discoverer-1.0 -c [video.mp4]```

**设置超时时间**

```gst-discoverer-1.0 -t [30] [video.mp4]```

# SYNOPSIS

**gst-discoverer-1.0** [_options_] _file_|_directory_|_uri_ ...

# PARAMETERS

**-v**, **--verbose**
> 输出所有可用信息。

**-a**, **--async**
> 使用异步代码路径。

**-t**, **--timeout** _seconds_
> 以秒为单位的超时时间（默认 10 秒）。

**-c**, **--toc**
> 输出 TOC（章节和版本）。

**--help**
> 打印帮助并退出。

# DESCRIPTION

**gst-discoverer-1.0** 显示媒体文件的元数据和流信息。它分析容器、编解码器、时长、分辨率、采样率、比特率等属性，无需播放文件。

该工具适用于调试多媒体问题和了解媒体结构。给定目录路径时会递归处理子目录。

# INSTALL

```apt: sudo apt install gstreamer1.0-plugins-base-apps```

```pacman: sudo pacman -S gst-plugins-base```

```apk: sudo apk add gst-plugins-base```

```brew: brew install gst-plugins-base```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gst-launch-1.0](/man/gst-launch-1.0)(1), [gst-inspect-1.0](/man/gst-inspect-1.0)(1), [mediainfo](/man/mediainfo)(1)

# RESOURCES

```[Homepage](https://gstreamer.freedesktop.org/)```

```[Source code](https://gitlab.freedesktop.org/gstreamer/gstreamer)```

```[Documentation](https://gstreamer.freedesktop.org/documentation/)```

<!-- verified: 2026-07-17 -->
