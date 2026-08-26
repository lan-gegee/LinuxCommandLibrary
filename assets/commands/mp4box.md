# TAGLINE

GPAC 框架的多媒体封装工具

# TLDR

**为视频添加音轨**

```mp4box -add [audio.m4a] [video.mp4]```

**合并多个 MP4 文件**

```mp4box -cat [file1.mp4] -cat [file2.mp4] -new [output.mp4]```

**提取指定轨道**

```mp4box -raw [1] [input.mp4]```

**为视频添加字幕**

```mp4box -add [subtitles.srt] [video.mp4]```

**显示文件信息**

```mp4box -info [file.mp4]```

**按时间间隔切分文件**

```mp4box -split [60] [input.mp4]```

**为 DASH 串流进行分片**

```mp4box -dash [4000] [input.mp4]```

**移除指定轨道**

```mp4box -rem [2] [input.mp4]```

# SYNOPSIS

**mp4box** [_-add file_] [_-cat file_] [_-info_] [_-dash duration_] [_options_] _file_

# PARAMETERS

**-add** _file_[:_opts_]
> 向文件添加媒体（导入轨道）。

**-cat** _file_
> 拼接文件。

**-rem** _trackID_
> 按 ID 移除轨道。

**-raw** _trackID_
> 提取原始轨道数据。

**-info** [_trackID_]
> 显示文件或轨道信息。

**-new** _file_
> 创建新的输出文件。

**-out** _file_
> 指定输出文件名。

**-split** _seconds_
> 按时间间隔切分文件。

**-split-size** _KB_
> 按大小切分文件。

**-dash** _ms_
> 创建指定时长（毫秒）的 DASH 分段。

**-frag** _ms_
> 按指定时长（毫秒）对文件分片。

**-rap**
> 仅在随机访问点（关键帧）处切分。

**-flat**
> 以平坦模式存储（非交错）。

**-inter** _ms_
> 以指定时长（毫秒）交错存储。

**-tmp** _dir_
> 使用备选临时目录。

**-nosys**
> 移除系统轨道信息。

**-fps** _rate_
> 为原始导入强制指定帧率。

**-lang** _code_
> 设置轨道语言。

# DESCRIPTION

**MP4Box** 是 GPAC 框架中的多媒体封装工具。它用于处理 MP4/ISO 基础媒体文件——无需重新编码即可添加、移除和编辑轨道。

该工具负责混流（将音频、视频、字幕合并到一个容器）、分离（提取轨道）和文件操作（切分、拼接、分片）。它支持多种导入格式，包括 H.264、H.265、AAC、MP3、SRT 和 WebVTT。

DASH（Dynamic Adaptive Streaming over HTTP）支持可创建用于自适应串流的分段文件。它将内容分片成小块并生成清单文件，使播放器能够根据带宽切换画质。

在串流准备方面，MP4Box 可以对文件分片以支持 HTTP 渐进式下载、为 RTSP 串流添加 hint 轨道，以及为直播工作流创建初始化段。

元数据编辑涵盖 MP4 标签、章节标记和轨道属性。该工具还可以使用各种 DRM 方案加密内容。

# CAVEATS

不做转码——仅重新封装流。某些操作会直接修改原文件。高级操作的命令语法较为复杂。DASH 输出需要正确配置 Web 服务器。大文件可能需要大量临时存储空间。某些格式组合需要特定的编解码器兼容性。

# HISTORY

**MP4Box** 是 **GPAC** 的一部分。GPAC 是一个开源多媒体框架，由 **Jean Le Feuvre** 于 **2000 年**前后在 **ENST Paris** 发起。GPAC 最初专注于 MPEG-4 研究，后来扩展到支持现代串流格式。MP4Box 已被广泛用于 DASH 内容准备，串流服务商和内容创作者都依赖它进行媒体封装。

# INSTALL

```brew: brew install mp4box```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ffmpeg](/man/ffmpeg)(1), [mkvmerge](/man/mkvmerge)(1), [mediainfo](/man/mediainfo)(1), [handbrake](/man/handbrake)(1)
