# TAGLINE

将 Opus 音频文件解码为 WAV 或原始 PCM

# TLDR

**将 Opus 解码为 WAV**

```opusdec [input.opus] [output.wav]```

**解码为原始 PCM**

```opusdec --raw [input.opus] [output.pcm]```

**解码到 stdout**

```opusdec [input.opus] - | aplay```

**设置输出采样率**

```opusdec --rate [48000] [input.opus] [output.wav]```

**强制立体声输出**

```opusdec --force-stereo [input.opus] [output.wav]```

# SYNOPSIS

**opusdec** [_options_] _input_ [_output_]

# PARAMETERS

**--rate** _Hz_
> 输出采样率。

**--raw**
> 输出原始 PCM。

**--force-stereo**
> 强制立体声输出。

**--float**
> 32 位浮点输出。

**--gain** _dB_
> 应用增益。

**--no-dither**
> 禁用抖动（dithering）。

**--force-wav**
> 强制在输出中包含 WAV 头（即使采样率非标准）。

**--packet-loss** _%_
> 模拟丢包百分比，用于测试。

**--quiet**
> 抑制程序输出。

**--save-range** _FILE_
> 将解码器范围数据保存到文件以供调试。

# DESCRIPTION

**opusdec** 将 Opus 音频文件解码为 WAV 或原始 PCM。若未指定输出文件，opusdec 会尝试直接播放音频。stdin/stdout 使用 `-` 表示。Opus 是一种同时为语音和音乐设计的通用音频编解码器，广泛应用于 WebRTC 和流媒体领域。

# EXAMPLE

```bash
# Decode to WAV
opusdec music.opus music.wav

# Play directly
opusdec music.opus - | aplay -f cd

# Convert with specific rate
opusdec --rate 44100 input.opus output.wav
```

# CAVEATS

输出默认与输入具有相同的声道数。重采样可能影响音质。需要最高精度时请使用 --float。

# HISTORY

Opus 由 **IETF** 编解码器工作组开发，于 **2012 年**标准化为 RFC 6716，融合了 SILK 和 CELT 两项技术。

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

[opusenc](/man/opusenc)(1), [ffmpeg](/man/ffmpeg)(1)
