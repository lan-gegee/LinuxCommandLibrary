# TAGLINE

Linux 视频流处理工具

# TLDR

**使用指定导出模块转码视频文件**

```transcode -i [input.avi] -y [xvid] -o [output.avi]```

**显式指定导入和导出模块转码**

```transcode -i [input.vob] -x [vob] -y [xvid,lame] -o [output.avi]```

**将音频提取到单独的文件**

```transcode -i [video.avi] -y null,tcaud -m [audio.mp3]```

**使用滤镜缩放调整视频尺寸**

```transcode -i [input.avi] -Z [640x480] -y [xvid] -o [output.avi]```

**设置视频码率并编码指定的帧范围**

```transcode -i [input.avi] -w [1500] -c [0-5000] -y [xvid] -o [output.avi]```

**从视频上下各裁剪 16 像素**

```transcode -i [input.avi] -j [16,0] -y [xvid] -o [output.avi]```

# SYNOPSIS

**transcode** **-i** _input_ [**-o** _output_] [**-y** _export_module_] [_options_]

# PARAMETERS

**-i** _FILE_
> 输入文件（必需）。唯一强制要求的选项。

**-o** _FILE_
> 输出文件。

**-x** _MODULE_
> 导入模块（如 vob、dvd、raw）。决定输入如何解码。

**-y** _MODULE_[,_AMODULE_]
> 视频导出模块，可选配单独的音频导出模块（如 xvid,lame）。

**-Z** _WxH_[,_MODE_]
> 使用缩放调整视频尺寸。附加 "fast" 表示快速缩放模式（如 640x480,fast）。

**-j** _TOP_,_LEFT_[,_BOTTOM_,_RIGHT_]
> 从图像边缘裁剪像素。只给两个值时会对称扩展。

**-w** _BITRATE_
> 视频编码器码率（kbps）。

**-b** _BITRATE_
> 音频编码器码率（kbps）。

**-m** _FILE_
> 将音频输出写入单独的文件。

**-p** _FILE_
> 从外部文件而不是主输入读取音频。

**-c** _RANGE_
> 只编码指定的帧范围（如 0-5000 或 0:05:00-0:10:00）。

**-s** _FACTOR_
> 按给定系数调整音量（例如增大音量用 4.47）。

**-R** _N_[,_FILE_]
> 多遍编码。第一遍用 -R 1，第二遍用 -R 2。

**-T** _TITLE_
> 选择要处理的 DVD 标题。

**--multi_input**
> 启用多输入文件的批处理。

# DESCRIPTION

**transcode** 是一个 Linux 视频流处理工具，用于在视频和音频格式之间转换。它采用模块化架构，针对不同的编解码器和容器使用独立的导入和导出模块。

该工具支持缩放、裁剪、去隔行扫描和音量调整等滤镜操作。它可以单独提取音轨，并通过多遍编码获得更好的质量。Transcode 已在很大程度上被 **FFmpeg** 取代，后者支持更广泛的格式且开发更为活跃。

# CAVEATS

这是一个不再积极开发的遗留工具。新项目通常首选 FFmpeg。模块化架构意味着可用的编解码器取决于已安装的模块。唯一的强制选项是 **-i**，其余均为可选。

# INSTALL

```aur: yay -S transcode```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ffmpeg](/man/ffmpeg)(1), [mencoder](/man/mencoder)(1), [mplayer](/man/mplayer)(1)
