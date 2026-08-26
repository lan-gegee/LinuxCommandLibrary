# TAGLINE

将音频编码为 Opus 格式

# TLDR

**编码为 Opus**

```opusenc [input.wav] [output.opus]```

**设置比特率**

```opusenc --bitrate [128] [input.wav] [output.opus]```

**设置质量**

```opusenc --vbr --comp [10] [input.wav] [output.opus]```

**添加元数据**

```opusenc --title "[title]" --artist "[artist]" [input.wav] [output.opus]```

**从管道编码**

```ffmpeg -i [input] -f wav - | opusenc - [output.opus]```

# SYNOPSIS

**opusenc** [_options_] _input_ _output_

# PARAMETERS

_INPUT_
> 输入音频文件。

_OUTPUT_
> 输出的 Opus 文件。

**--bitrate** _KBPS_
> 目标比特率，单位 kbit/s。单声道默认为 64，立体声默认为 96。

**--vbr**
> 使用可变比特率（默认）。

**--cvbr**
> 使用受限可变比特率。

**--hard-cbr**
> 使用硬性恒定比特率。

**--comp** _LEVEL_
> 编码复杂度，0（最快）到 10（最慢、质量最佳）。默认为 10。

**--framesize** _MS_
> 帧大小，单位 ms（2.5、5、10、20、40、60）。默认为 20。

**--music** / **--speech**
> 针对音乐或语音调整编码器。

**--downmix-mono** / **--downmix-stereo**
> 强制单声道或立体声输出。

**--title** _TITLE_, **--artist** _NAME_, **--album** _NAME_
> 设置 Vorbis 风格的元数据标签。

**--raw**, **--raw-rate** _HZ_, **--raw-chan** _N_
> 将输入视为无文件头 PCM，并按给定的采样率和声道数处理。

**--help**
> 显示帮助信息。

# DESCRIPTION

**opusenc** 将原始或容器化音频（WAV、AIFF、FLAC 或原始 PCM）编码为 Ogg 容器内的 Opus 编解码格式。Opus 是一种低延迟、免版税的编解码器，在 6 至 510 kbit/s 的比特率范围内同时适合音乐和语音。

默认情况下 opusenc 使用复杂度 10 的 VBR，以 CPU 时间为代价换取同等体积下的最佳音质。从 `-` 读取输入让你可以从 `ffmpeg`、`sox` 等工具通过管道传入数据。

# CAVEATS

随 **opus-tools** 一同发布。输入必须是 WAV、AIFF、FLAC 或原始 PCM；MP3 及其他有损格式应先解码（通常通过 ffmpeg）。Opus 是有损压缩：从其他有损来源重新编码会加剧失真。

# HISTORY

opusenc 为将音频编码为 **Opus 编解码器**格式而创建。

# INSTALL

```apt: sudo apt install opus-tools```

```dnf: sudo dnf install opus-tools```

```pacman: sudo pacman -S opus-tools```

```apk: sudo apk add opus-tools```

```zypper: sudo zypper install opus-tools```

```brew: brew install opus-tools```

```nix: nix profile install nixpkgs#opus-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[opusdec](/man/opusdec)(1), [ffmpeg](/man/ffmpeg)(1), [lame](/man/lame)(1)
