# TAGLINE

用于剪切、滤镜和编码的免费视频编辑器

# TLDR

**打开**视频文件

```avidemux [video.mp4]```

**转换**为其他格式

```avidemux --load [input.avi] --save [output.mp4] --quit```

**剪切**片段而不重新编码（直接复制流）

```avidemux --load [video.mp4] --output-format MKV --video-codec copy --audio-codec copy --begin [100] --end [500] --save [clip.mkv] --quit```

配合脚本以**无界面 CLI 模式**运行

```avidemux3_cli --load [input.mp4] --run [project.py] --save [output.mp4] --quit```

# SYNOPSIS

**avidemux** [_options_] [_file_]

# DESCRIPTION

**avidemux** 是一款免费的视频编辑器，适用于剪切、滤镜和编码任务。它支持多种文件格式，并提供图形界面和命令行两种视频处理方式。

该工具擅长简单的编辑任务，比如剪掉广告、应用滤镜以及在不同格式之间转换，无需复杂的时间线编辑。

# PARAMETERS

**--load** _file_
> 加载视频文件

**--save** _file_
> 保存输出文件

**--video-codec** _codec_
> 设置视频编解码器（copy、x264、xvid 等）

**--audio-codec** _codec_
> 设置音频编解码器（copy、aac、mp3 等）

**--begin** _frame_
> 将剪切起点标记设为指定帧号。

**--end** _frame_
> 将剪切终点标记设为指定帧号。

**--run** _script_
> 加载并运行 Avidemux 项目或 Python（Tinypy/JS）脚本。

**--quit**
> 操作完成后退出（无人值守运行时必须）。

**--output-format** _format_
> 设置容器格式（MKV、MP4、AVI、TS、PS、OGM）。

**--rebuild-index**
> 使用正确的帧类型重建索引。

**--autoindex**
> 按需生成所需的索引文件。

# FEATURES

- 无需重新编码即可剪切和拼接视频
- 应用视频滤镜（调整大小、降噪、锐化）
- 音频处理与同步
- 通过脚本进行批处理
- 多音轨
- 字幕支持

# CAVEATS

图形界面可能不够直观。某些编解码器需要额外的库。复杂的剪辑更适合专业非线性编辑软件。脚本功能使用自定义的 Python 绑定。

# HISTORY

**Avidemux** 由 Mean（化名）创建，于 **2001** 年首次发布，是一款用于基本视频编辑任务的简单工具，避开了专业编辑器的复杂性。

# INSTALL

```nix: nix profile install nixpkgs#avidemux```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[ffmpeg](/man/ffmpeg)(1), [handbrake](/man/handbrake)(1), [kdenlive](/man/kdenlive)(1)

# RESOURCES

```[Source code](https://github.com/mean00/avidemux2)```

```[Homepage](https://avidemux.sourceforge.net/)```

```[Documentation](https://www.avidemux.org/admWiki/doku.php?id=using:command_line_usage)```

<!-- verified: 2026-06-17 -->
