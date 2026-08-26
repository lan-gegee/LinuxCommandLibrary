# TAGLINE

MLT 命令行视频编辑器

# TLDR

**播放视频**

```melt [video.mp4]```

**渲染到文件**

```melt [input.mp4] -consumer avformat:[output.mp4]```

**添加滤镜**

```melt [video.mp4] -filter [sepia]```

**混合音频**

```melt [video.mp4] -mix [10] -mixer [mix:-1]```

**设置输出 profile**

```melt -profile [atsc_1080p_25] [input.mp4]```

**拼接片段**

```melt [clip1.mp4] [clip2.mp4] -consumer avformat:[output.mp4]```

# SYNOPSIS

**melt** [_options_] _input_ [_filters_]

# PARAMETERS

_INPUT_
> 输入媒体文件。

**-consumer** _TYPE_
> 输出消费者（consumer）。

**-filter** _NAME_
> 应用滤镜。

**-profile** _NAME_
> 使用指定的 profile。

**-mix** _FRAMES_
> 过渡帧数。

**--help**
> 显示帮助信息。

# DESCRIPTION

**melt** 是 MLT 的命令行视频编辑器，可通过滤镜和过渡处理视频。

该工具是 MLT 框架自带的实用程序，用于脚本化的视频编辑与特效制作。

# CAVEATS

语法复杂。了解 MLT 框架会有帮助。属于 MLT 软件包的一部分。

# HISTORY

melt 是 **MLT 多媒体框架**的命令行工具，被 Kdenlive 和 Shotcut 所使用。

# INSTALL

```apt: sudo apt install melt```

```dnf: sudo dnf install mlt```

```pacman: sudo pacman -S mlt```

```apk: sudo apk add mlt```

```zypper: sudo zypper install melt```

```brew: brew install melt```

```nix: nix profile install nixpkgs#melt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ffmpeg](/man/ffmpeg)(1), [kdenlive](/man/kdenlive)(1), [shotcut](/man/shotcut)(1)
