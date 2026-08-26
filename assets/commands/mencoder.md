# TAGLINE

MPlayer 的视频编码工具

# TLDR

**转换视频**

```mencoder [input.avi] -o [output.mp4] -ovc lavc -oac mp3lame```

**提取音频**

```mencoder [video.avi] -o [audio.mp3] -ovc copy -oac mp3lame```

**调整视频尺寸**

```mencoder [input.avi] -o [output.avi] -vf scale=[640:480] -ovc lavc -oac copy```

**两遍编码**

```mencoder [input.avi] -o /dev/null -ovc lavc -lavcopts vpass=1 && mencoder [input.avi] -o [output.avi] -ovc lavc -lavcopts vpass=2```

**拼接视频**

```mencoder -ovc copy -oac copy -o [joined.avi] [file1.avi] [file2.avi]```

# SYNOPSIS

**mencoder** [_options_] _input_ -o _output_

# PARAMETERS

_INPUT_
> 输入媒体文件。

**-o** _FILE_
> 输出文件。

**-ovc** _CODEC_
> 视频编解码器。

**-oac** _CODEC_
> 音频编解码器。

**-vf** _FILTERS_
> 视频滤镜。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mencoder** 是 MPlayer 的视频编码工具，可在不同格式间转换并应用滤镜。

该工具属于 MPlayer 项目。在许多场景下已被 FFmpeg 取代。

# CAVEATS

属于 MPlayer 项目（已过时）。通常更推荐 FFmpeg。选项复杂。

# HISTORY

mencoder 是 **MPlayer** 的编码配套工具，提供视频转换功能。

# INSTALL

```apt: sudo apt install mencoder```

```pacman: sudo pacman -S mencoder```

```apk: sudo apk add mplayer```

```brew: brew install mplayer```

```nix: nix profile install nixpkgs#mplayer```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ffmpeg](/man/ffmpeg)(1), [mplayer](/man/mplayer)(1), [handbrake](/man/handbrake)(1)
