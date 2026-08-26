# TAGLINE

多媒体流分析器

# TLDR

**显示媒体文件的信息**

```ffprobe [path/to/file.mp4]```

**以 JSON 格式显示信息**

```ffprobe -v quiet -print_format json -show_format -show_streams [file.mp4]```

**获取视频时长**（秒）

```ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 [file.mp4]```

**获取视频分辨率**

```ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=s=x:p=0 [file.mp4]```

**获取编解码器信息**

```ffprobe -v error -select_streams v:0 -show_entries stream=codec_name -of default=noprint_wrappers=1:nokey=1 [file.mp4]```

**获取音频采样率**

```ffprobe -v error -select_streams a:0 -show_entries stream=sample_rate -of default=noprint_wrappers=1:nokey=1 [file.mp4]```

**显示所有流信息**

```ffprobe -v error -show_streams [file.mp4]```

**分析网络流**

```ffprobe [https://example.com/stream.m3u8]```

# SYNOPSIS

**ffprobe** [_options_] [_input_file_]

# PARAMETERS

**-v** _level_
> 设置日志详细程度（quiet、panic、fatal、error、warning、info、verbose、debug）。

**-show_format**
> 显示容器格式信息。

**-show_streams**
> 显示流信息（视频、音频、字幕轨）。

**-show_entries** _section_
> 只显示指定的条目（如 stream=codec_name,bit_rate）。

**-select_streams** _specifier_
> 选择特定流（v:0 为第一个视频流，a:0 为第一个音频流）。

**-print_format**, **-of** _format_
> 输出格式：default、json、xml、csv、flat、ini。

**-count_frames**
> 统计并报告总帧数（大文件较慢）。

**-count_packets**
> 统计每个流中的包数。

**-show_chapters**
> 显示章节信息。

**-show_programs**
> 显示节目信息。

**-show_error**
> 显示有关错误的信息。

**-show_data**
> 以十六进制和 ASCII 转储形式显示载荷数据。

**-i** _input_
> 输入文件（可选，也可直接指定文件）。

**-hide_banner**
> 不打印横幅/配置信息。

**-pretty**
> 使用 SI 前缀和单位美化显示的值。

**-sexagesimal**
> 时间值使用六十进制格式 HH:MM:SS.MICROSECONDS。

**-bitexact**
> 强制输出与具体构建无关的位精确结果。

# DESCRIPTION

**ffprobe** 是 FFmpeg 项目中的多媒体流分析器。它检查媒体文件和流，报告容器格式、编解码器、码率、分辨率、时长、元数据等详细技术信息。

该工具读取媒体文件而不进行解码，因此分析速度很快。它支持 FFmpeg 处理的几乎所有音视频格式，包括本地文件、网络流和设备。

输出可以格式化为人类可读的文本、JSON、XML、CSV 或其他格式，便于脚本集成。**-show_entries** 选项可提取特定值，无需解析冗长的输出。

常见用途包括：验证转码结果、为媒体库提取元数据、调试播放问题、在处理前分析流特性，以及编写媒体管理脚本。

对于网络流（HLS、DASH、RTSP 等），ffprobe 可分析远程内容，适用于监控推流基础设施。结合 FFmpeg 的其他工具，它可以实现完整的媒体检查和处理。

# CAVEATS

帧统计（-count_frames）需要解码，速度较慢。某些格式可能无法准确报告时长。受保护/DRM 内容可能无法分析。网络流分析需要稳定的连接。

# HISTORY

**ffprobe** 是 **FFmpeg** 项目的一部分，该项目始于 **2000 年**。FFmpeg 提供完整的多媒体处理套件。ffprobe 作为专门的分析工具出现，将检查功能从 ffmpeg 的转换能力中分离出来。FFmpeg 是使用最广泛的开源多媒体框架之一。

# INSTALL

```apt: sudo apt install ffmpeg```

```pacman: sudo pacman -S ffmpeg```

```apk: sudo apk add ffmpeg```

```brew: brew install ffmpeg```

```nix: nix profile install nixpkgs#ffmpeg```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ffmpeg](/man/ffmpeg)(1), [ffplay](/man/ffplay)(1), [mediainfo](/man/mediainfo)(1), [exiftool](/man/exiftool)(1)
