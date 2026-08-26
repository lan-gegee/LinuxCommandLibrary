# TAGLINE

已弃用的 HTTP/RTSP 流媒体服务器

# TLDR

启动流媒体服务器

```ffserver -f [ffserver.conf]```

后台运行

```ffserver -f [ffserver.conf] &```

指定日志级别

```ffserver -f [ffserver.conf] -loglevel [verbose]```

# SYNOPSIS

**ffserver** [_options_]

# PARAMETERS

**-f** _FILE_
> 配置文件。

**-n**
> 不启动（仅解析配置）。

**-d**
> 调试模式。

**-loglevel** _LEVEL_
> 日志详细程度：quiet、error、warning、info、verbose。

**--help**
> 显示帮助信息。

# CONFIGURATION

**ffserver.conf**
> 服务器配置，定义输入馈送、输出流、格式和码率。

# DESCRIPTION

**ffserver** 曾是 ffmpeg 自带的 HTTP/RTSP 流媒体服务器。它接收来自 ffmpeg 编码器的馈送并将其提供给客户端，用于搭建直播流方案。

该服务器支持多路流和按需重新编码。配置中定义来自 ffmpeg 的输入馈送，以及面向客户端、具有不同格式和码率的输出流。

ffserver 为网络摄像头、屏幕采集和视频文件提供了完整的流媒体解决方案。

# CAVEATS

已在 ffmpeg 4.0 中**弃用并移除**。请改用 nginx-rtmp 或 GStreamer 等替代品。其配置较为复杂。

# HISTORY

ffserver 从早期版本起就是 ffmpeg 的一部分，直到 **2018 年被移除**（ffmpeg 4.0）。由于维护负担过重而被弃用，建议改用专门的流媒体服务器。

# SEE ALSO

[ffmpeg](/man/ffmpeg)(1), [nginx](/man/nginx)(1), [vlc](/man/vlc)(1)

# RESOURCES

```[Homepage](https://ffmpeg.org/)```

<!-- verified: 2026-07-15 -->
