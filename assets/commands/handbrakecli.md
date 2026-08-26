# TAGLINE

HandBrake 的命令行界面，一款强大的开源视频转码器

# TLDR

使用预设**转换视频**

```HandBrakeCLI -i [input.mkv] -o [output.mp4] --preset="[Fast 1080p30]"```

**列出可用预设**

```HandBrakeCLI --preset-list```

**使用指定视频编码器转换**

```HandBrakeCLI -i [input.mkv] -o [output.mp4] -e [x264]```

**设置视频质量**（数值越低质量越好，通常取 18-28）

```HandBrakeCLI -i [input.mkv] -o [output.mp4] -q [22]```

**转换 DVD** 或蓝光目录

```HandBrakeCLI -i [/path/to/VIDEO_TS] -o [output.mp4] --preset="[Fast 1080p30]"```

从光盘**提取指定标题**

```HandBrakeCLI -i [/dev/dvd] -t [1] -o [output.mp4]```

转换时**选择音频和字幕**轨道

```HandBrakeCLI -i [input.mkv] -o [output.mp4] -a [1,2] -s [1]```

**扫描输入**以查看标题和轨道

```HandBrakeCLI -i [input.mkv] --scan```

# SYNOPSIS

**HandBrakeCLI** [_-i input_] [_-o output_] [_--preset name_] [_-e encoder_] [_-q quality_] [_options_]

# PARAMETERS

**-i**, **--input** _source_
> 输入文件、目录或设备。

**-o**, **--output** _file_
> 输出文件路径。

**-Z**, **--preset** _name_
> 使用命名预设（参见 --preset-list）。

**-z**, **--preset-list**
> 列出可用预设。

**-t**, **--title** _number_
> 选择标题编号（用于 DVD/蓝光）。

**--scan**
> 只扫描输入而不转码。

**-e**, **--encoder** _codec_
> 视频编码器：x264、x265、nvenc_h264、nvenc_h265、vce_h264、vce_h265、svt_av1。

**-q**, **--quality** _RF_
> 恒定质量（RF 值，数值越低质量越好）。

**-b**, **--vb** _kbps_
> 视频码率（kbps）。

**-r**, **--rate** _fps_
> 帧率。

**-a**, **--audio** _tracks_
> 要包含的音频轨道（逗号分隔）。

**-E**, **--aencoder** _codec_
> 音频编码器：copy、aac、ac3、mp3、opus、flac。

**-s**, **--subtitle** _tracks_
> 要包含的字幕轨道。

**--crop** _top:bottom:left:right_
> 裁剪值。

**-w**, **--width** _pixels_
> 输出宽度。

**-l**, **--height** _pixels_
> 输出高度。

**--multi-pass**
> 启用多趟编码（取代旧的 --two-pass 标志）。

# DESCRIPTION

**HandBrakeCLI** 是 HandBrake 的命令行界面。HandBrake 是一款强大的开源视频转码器，可以在不同格式之间转换视频、抓取 DVD 和蓝光光盘，并能在保持质量的同时显著减小文件体积。

该工具使用预设来简化常见的编码场景。内置预设针对特定设备（Apple TV、Android、Roku）或质量级别（Fast 1080p30、HQ 1080p30 Surround）。自定义预设可以从 GUI 导出，再导入 CLI 工作流中使用。

对于基于质量的编码，RF（Rate Factor）值控制质量与体积之间的权衡。对 x264/x265 而言，18-22 可提供高质量，23-28 则产生更小且质量尚可接受的文件。数值越低意味着质量越高、文件越大。

HandBrake 在受支持的系统上支持硬件加速：NVIDIA NVENC、AMD VCE/VCN、Intel QuickSync 以及 Apple VideoToolbox。硬件编码器速度更快，但在同等质量下可能产生更大的文件。

音频和字幕轨道可以被选择、转换或直接传递。可以包含多条采用不同编码的音频轨道。字幕既可以烧录进画面，也可以保留为软字幕。

# CAVEATS

无法输出到某些受专利限制的格式。DVD/蓝光解密需要 libdvdcss。质量设置在不同编码器之间不能直接换算。硬件编码的可用性取决于 GPU 和驱动。多趟编码比单趟耗时更长。

# HISTORY

**HandBrake** 最初由 Eric Petit（titer）于 **2003 年**为 BeOS 创建，当时名为 "MediaFork"，随后更名并在其他平台上继续开发。该项目在一段沉寂之后由开源社区复兴。如今它已成为最受欢迎的开源视频转码器之一，以功能与易用性的良好平衡著称。

# SEE ALSO

[handbrake](/man/handbrake)(1), [ffmpeg](/man/ffmpeg)(1), [ffprobe](/man/ffprobe)(1), [mkvmerge](/man/mkvmerge)(1), [mediainfo](/man/mediainfo)(1)

# RESOURCES

```[Source code](https://github.com/HandBrake/HandBrake)```

```[Homepage](https://handbrake.fr/)```

```[Documentation](https://handbrake.fr/docs/)```

<!-- verified: 2026-07-17 -->
