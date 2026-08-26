# TAGLINE

多媒体转换与处理工具

# TLDR

**转换视频格式（由扩展名自动判断）**

```ffmpeg -i [input.mp4] [output.avi]```

**提取音频而不重新编码**

```ffmpeg -i [video.mp4] -vn -c:a copy [audio.m4a]```

**将视频调整为 1280x720**

```ffmpeg -i [input.mp4] -vf scale=[1280]:[720] [output.mp4]```

**用 x264 CRF 压缩视频（值越低质量越好）**

```ffmpeg -i [input.mp4] -c:v libx264 -crf [23] -c:a copy [output.mp4]```

**从 00:01:00 开始截取 30 秒**

```ffmpeg -ss [00:01:00] -i [input.mp4] -t [30] -c copy [output.mp4]```

**从视频创建 GIF**

```ffmpeg -i [input.mp4] -vf "fps=10,scale=320:-1" [output.gif]```

**拼接 files.txt 中列出的文件**

```ffmpeg -f concat -safe 0 -i [files.txt] -c copy [output.mp4]```

# SYNOPSIS

**ffmpeg** [_global-options_] [_input-options_] **-i** _input_ [_output-options_] _output_

# PARAMETERS

**-i** _FILE_
> 输入文件（可多次指定）。

**-c:v** _CODEC_
> 视频编解码器（如 libx264、libx265、libvpx-vp9、copy）。

**-c:a** _CODEC_
> 音频编解码器（如 aac、libmp3lame、libopus、copy）。

**-c** _CODEC_
> 设置所有流编解码器的简写（常用作 `-c copy`）。

**-crf** _N_
> x264/x265 的恒定速率因子 CRF（0-51，值越小质量越好，默认为 23）。

**-b:v** _BITRATE_
> 目标视频码率（如 2M）。

**-b:a** _BITRATE_
> 目标音频码率（如 128k）。

**-r** _FPS_
> 输出帧率。

**-s** _WxH_
> 设置输出帧大小（如 1280x720）。

**-vf** _FILTER_
> 视频滤镜图（scale、crop、fps 等）。

**-af** _FILTER_
> 音频滤镜图。

**-ss** _TIME_
> 定位到起始位置。放在 `-i` 之前为快速定位，放在 `-i` 之后为精确定位。

**-to** _TIME_
> 在给定的绝对时间停止写入。

**-t** _DURATION_
> 将输出限制在给定时长内。

**-vn**
> 禁用视频输出。

**-an**
> 禁用音频输出。

**-map** _SPEC_
> 显式地将输入流映射到输出。

**-f** _FORMAT_
> 强制容器格式。

**-y**
> 不询问直接覆盖输出文件。

**-n**
> 绝不覆盖输出文件。

**-loglevel** _LEVEL_
> 日志详细程度（quiet、panic、fatal、error、warning、info、verbose、debug、trace）。

**-h** [_topic_]
> 显示帮助；使用 `-h long` 或 `-h full` 查看更多选项。

# DESCRIPTION

**ffmpeg** 是多媒体处理的瑞士军刀。凭借庞大的编解码器库，它可以对几乎所有格式的音频和视频进行转换、录制、推流和处理。

该工具使用强大的滤镜系统实现缩放、裁剪、色彩校正和特效等变换。从简单的格式转换到复杂的推流部署它都能胜任。

ffmpeg 是众多视频应用的基石，也是命令行多媒体处理事实上的标准。

# CAVEATS

语法复杂，需要学习。质量与大小的权衡因内容而异。某些编解码器存在许可方面的考量。处理过程 CPU 占用较高。

# HISTORY

ffmpeg 由 **Fabrice Bellard** 于 2000 年启动，如今已成为使用最广泛的多媒体框架。从 VLC 到 YouTube 的视频处理流水线，无数应用都依赖它。

# INSTALL

```apt: sudo apt install ffmpeg```

```pacman: sudo pacman -S ffmpeg```

```apk: sudo apk add ffmpeg```

```brew: brew install ffmpeg```

```nix: nix profile install nixpkgs#ffmpeg```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ffprobe](/man/ffprobe)(1), [ffplay](/man/ffplay)(1), [sox](/man/sox)(1), [handbrake](/man/handbrake)(1), [mencoder](/man/mencoder)(1)
