# TAGLINE

ffmpeg 处理的实用工具函数

# TLDR

获取媒体信息

```ffprobe [input.mp4]```

显示流详情

```ffprobe -show_streams [input.mp4]```

以 JSON 输出

```ffprobe -print_format json -show_format [input.mp4]```

分析帧

```ffprobe -show_frames [input.mp4]```

只获取时长

```ffprobe -v quiet -show_entries format=duration -of csv=p=0 [input.mp4]```

只显示视频流信息

```ffprobe -hide_banner -select_streams v:0 -show_streams [input.mp4]```

# SYNOPSIS

**ffprobe** [_options_] _input_

# PARAMETERS

_INPUT_
> 要分析的媒体文件。

**-show_format**
> 显示容器格式信息。

**-show_streams**
> 显示流信息。

**-show_frames**
> 显示帧信息。

**-print_format** _FORMAT_
> 输出格式：json、xml、csv、flat。

**-show_entries** _ENTRIES_
> 选择要显示的特定条目。

**-of** _FORMAT_
> 输出格式（print_format 的别名）。

**-select_streams** _SPEC_
> 只选择指定的流（如 v:0 表示第一个视频流，a 表示所有音频流）。

**-show_chapters**
> 显示章节信息。

**-hide_banner**
> 不打印包含版权和构建信息的横幅。

**-v** _LEVEL_
> 设置日志详细程度（如 quiet、error、warning、info）。

**-count_frames**
> 统计每个流的帧数（需要解码，速度慢）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**ffprobe**（ffmpeg 工具集的一部分）从多媒体流中收集信息，并以人类或机器可读的格式打印。它揭示编解码器细节、时长、码率、分辨率和元数据。

该工具对于编写视频工作流脚本、在处理前检查文件属性以及调试编码问题至关重要。结构化的输出格式便于其他工具解析。

ffprobe 提供详细的流分析且不修改文件，因此用于检查任务是安全的。

# CAVEATS

完整的帧分析可能较慢。某些格式的元数据不完整。输出格式因文件类型而异。

# HISTORY

ffprobe 加入 ffmpeg 是为了提供专门的媒体分析功能，将检查与处理分离。它已成为程序化媒体文件分析的标准工具。

# INSTALL

```apt: sudo apt install ffmpeg```

```pacman: sudo pacman -S ffmpeg```

```apk: sudo apk add ffmpeg```

```brew: brew install ffmpeg```

```nix: nix profile install nixpkgs#ffmpeg```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ffmpeg](/man/ffmpeg)(1), [ffplay](/man/ffplay)(1), [mediainfo](/man/mediainfo)(1), [exiftool](/man/exiftool)(1)
