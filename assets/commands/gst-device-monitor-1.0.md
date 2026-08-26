# TAGLINE

GStreamer 多媒体设备检测工具

# TLDR

**列出所有设备**

```gst-device-monitor-1.0```

**监视设备变化**

```gst-device-monitor-1.0 --follow```

只**列出音频源**

```gst-device-monitor-1.0 Audio/Source```

**列出视频源**

```gst-device-monitor-1.0 Video/Source```

**包含隐藏设备**

```gst-device-monitor-1.0 --include-hidden```

**按能力过滤**

```gst-device-monitor-1.0 Video/Source:video/x-raw```

# SYNOPSIS

**gst-device-monitor-1.0** [_options_] [_filter_]

# PARAMETERS

**-f**, **--follow**
> 持续监视设备变化。

**-i**, **--include-hidden**
> 包含来自隐藏提供者的设备。

**--help**
> 显示帮助概要。

**--version**
> 打印版本并退出。

# DESCRIPTION

**gst-device-monitor-1.0** 是一款 GStreamer 工具，用于检测并列出可用的多媒体设备。它显示音频源（麦克风）、音频输出（扬声器）、视频源（网络摄像头）和其他媒体设备。

默认情况下，它列出所有设备后退出。使用 **--follow** 可持续监视设备的添加和移除。

# CAVEATS

需要 GStreamer 1.4+ 及相应插件。设备检测依赖已安装的插件（ALSA、PulseAudio、V4L2）。检测某些设备可能需要适当的权限。

# INSTALL

```apt: sudo apt install gstreamer1.0-plugins-base-apps```

```pacman: sudo pacman -S gst-plugins-base```

```apk: sudo apk add gst-plugins-base```

```brew: brew install gst-plugins-base```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gst-launch-1.0](/man/gst-launch-1.0)(1), [gst-inspect-1.0](/man/gst-inspect-1.0)(1), [gst-discoverer-1.0](/man/gst-discoverer-1.0)(1)
