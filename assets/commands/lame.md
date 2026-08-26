# TAGLINE

高质量 MP3 编码器

# TLDR

**编码为 MP3**

```lame [input.wav] [output.mp3]```

**设置比特率**

```lame -b [320] [input.wav] [output.mp3]```

**可变比特率**

```lame -V [2] [input.wav] [output.mp3]```

**高质量预设**

```lame --preset extreme [input.wav] [output.mp3]```

**添加 ID3 标签**

```lame --tt "[title]" --ta "[artist]" [input.wav] [output.mp3]```

**将 MP3 解码为 WAV**

```lame --decode [input.mp3] [output.wav]```

# SYNOPSIS

**lame** [_options_] _input_ [_output_]

# PARAMETERS

_INPUT_
> 输入音频文件。

_OUTPUT_
> 输出的 MP3 文件。

**-b** _BITRATE_
> 固定比特率（kbps）。

**-V** _QUALITY_
> 可变比特率（0-9，0 表示最佳）。

**--preset** _NAME_
> 质量预设（extreme、insane）。

**--tt** _TITLE_
> 歌曲标题。

**--ta** _ARTIST_
> 艺术家名称。

**--decode**
> 将 MP3 解码为 WAV。

**--help**
> 显示帮助信息。

# DESCRIPTION

**LAME** 是一款高质量的 MP3 编码器。它在各种比特率下都能产生出色的音质。

该编码器同时支持固定比特率和可变比特率模式。它被广泛认为是最好的开源 MP3 编码器。

# CAVEATS

默认只能编码。音质与体积之间需要权衡。推荐使用 VBR。

# HISTORY

LAME（Lame Ain't an MP3 Encoder）始于 1998 年，后成为领先的开源 MP3 编码器。

# INSTALL

```apt: sudo apt install lame```

```dnf: sudo dnf install lame```

```pacman: sudo pacman -S lame```

```apk: sudo apk add lame```

```zypper: sudo zypper install lame```

```brew: brew install lame```

```nix: nix profile install nixpkgs#lame```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ffmpeg](/man/ffmpeg)(1), [sox](/man/sox)(1)
