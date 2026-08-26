# TAGLINE

基于 ffmpeg 库的简易媒体播放器

# TLDR

**播放媒体文件**

```ffplay [video.mp4]```

以指定尺寸播放

```ffplay -x [640] -y [480] [video.mp4]```

**循环播放**

```ffplay -loop [0] [video.mp4]```

只播音频

```ffplay -nodisp [audio.mp3]```

定位到指定位置

```ffplay -ss [00:01:30] [video.mp4]```

# SYNOPSIS

**ffplay** [_options_] _input_

# PARAMETERS

_INPUT_
> 要播放的媒体文件或流。

**-x** _WIDTH_
> 显示宽度。

**-y** _HEIGHT_
> 显示高度。

**-loop** _N_
> 循环次数（0 = 无限）。

**-nodisp**
> 禁用显示（仅音频）。

**-ss** _TIME_
> 起始位置。

**-t** _DURATION_
> 播放时长。

**-vf** _FILTER_
> 视频滤镜。

**-af** _FILTER_
> 音频滤镜。

**-fs**
> 以全屏启动。

**--help**
> 显示帮助信息。

# DESCRIPTION

**ffplay** 是一个基于 ffmpeg 库的简易媒体播放器。它可以播放 ffmpeg 支持的几乎所有音视频格式，因此适合测试滤镜和预览编码效果。

播放器通过键盘提供基本控制：空格暂停、方向键定位、q 退出。它可以实时应用滤镜，在编码前预览效果。

ffplay 主要是一个开发和测试工具，而非全功能媒体播放器。

# CAVEATS

与完整播放器相比界面极简。不支持播放列表。滤镜预览可能与最终输出不完全一致。

# HISTORY

ffplay 作为演示 ffmpeg 解码能力的参考播放器而创建。它既是测试工具，也是播放其他播放器可能不支持的格式的简易选择。

# INSTALL

```apt: sudo apt install ffmpeg```

```pacman: sudo pacman -S ffmpeg```

```apk: sudo apk add ffmpeg7```

```brew: brew install ffmpeg```

```nix: nix profile install nixpkgs#ffmpeg```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ffmpeg](/man/ffmpeg)(1), [mpv](/man/mpv)(1), [vlc](/man/vlc)(1)

# RESOURCES

```[Homepage](https://ffmpeg.org/)```

```[Documentation](https://ffmpeg.org/ffplay.html)```

<!-- verified: 2026-07-15 -->
