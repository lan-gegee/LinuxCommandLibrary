# TAGLINE

文本界面音频播放器与音乐可视化工具

# TLDR

**播放音乐文件**

```ocp [path/to/file]```

**播放目录中的文件**

```ocp [path/to/directory]```

# SYNOPSIS

**ocp** [_options_] [_files_...]

# DESCRIPTION

**opencubicplayer**（命令为 **ocp**）是一个文本界面的音频播放器和音乐可视化工具，支持跟踪器音乐格式（MOD、XM、S3M、IT）、chiptune、SID、MP3、OGG、FLAC 等。它提供 FFT 频谱分析器、示波器、相位查看器和通道查看器等可视化效果。

它最初源自 DOS 时代的 demoscene，Unix/Linux 分支保留了经典的文本模式界面，同时支持现代编解码器。

# CAVEATS

部分可视化模式需要支持颜色的终端。跟踪格式的播放质量取决于可用的解码库。

# HISTORY

**Open Cubic Player** 的 Unix 分支由 **Stian Sebastian Skjelstad**（mywave82）维护，使用 **C** 语言编写。

# SEE ALSO

[cmus](/man/cmus)(1), [mpv](/man/mpv)(1), [musikcube](/man/musikcube)(1)
