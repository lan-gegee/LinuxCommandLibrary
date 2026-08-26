# TAGLINE

轻量级文本转语音合成

# TLDR

**朗读文本**

```flite -t "[Hello world]"```

**从文件朗读**

```flite -f [text.txt]```

**保存为音频文件**

```flite -t "[Hello world]" -o [output.wav]```

**使用指定音色**

```flite -voice [rms] -t "[Hello world]"```

**列出可用音色**

```flite -lv```

**将输入按音素朗读**

```flite -p "[pau hh ax l ow w er l d]"```

**从文件读取 SSML 输入**

```flite -ssml -f [input.ssml]```

# SYNOPSIS

**flite** [_options_] [_text_]

# PARAMETERS

_TEXT_
> 要朗读的文本。如果其中包含空格，则被视为字面文本字符串而不是文件名。

**-t** _TEXT_
> 显式设置输入的文本字符串。

**-f** _FILE_
> 显式设置输入文件名。

**-o** _FILE_
> 将音频输出到文件（WAV 格式）。如果省略或设为 "play"，音频将在默认音频设备上播放。设为 "none" 则丢弃输出。

**-p** _PHONES_
> 将输入作为音素进行合成。

**-voice** _NAME_
> 要使用的音色（名称、文件名或 URL）。

**-voicedir** _DIR_
> 包含语音数据的目录。

**-lv**
> 列出可用音色。

**-ssml**
> 以 SSML 模式读取输入文本/文件。

**-b**
> 基准测试模式。

**-l**
> 无限循环播放。

**-s** _F=V_
> 将特性设置为指定值（自动猜测类型）。

**-v**
> 详细输出模式。

**--version**
> 显示版本号。

**--help**
> 显示帮助信息。

# DESCRIPTION

**flite**（Festival Lite）是由卡内基梅隆大学开发的小型快速文本转语音合成引擎。它使用拼接式合成技术将文本转换为音频，通过录制片段生成语音。

该引擎专为资源有限的嵌入式系统设计，在运行时开销很小的情况下提供尚可的音质。它提供多种具有不同特点的音色。

flite 可以离线工作，无需互联网连接，适合无障碍应用和音频生成场景。

# CAVEATS

与神经网络 TTS 相比，语音自然度有限。可选音色较少。输出质量因文本类型而异。

# HISTORY

flite 由**卡内基梅隆大学**开发，是 Festival 语音合成系统的轻量版本。它被用于无障碍应用、嵌入式系统和离线 TTS 场景。

# INSTALL

```apt: sudo apt install flite```

```dnf: sudo dnf install flite```

```pacman: sudo pacman -S flite```

```apk: sudo apk add flite```

```zypper: sudo zypper install flite```

```nix: nix profile install nixpkgs#flite```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[espeak](/man/espeak)(1), [espeak-ng](/man/espeak-ng)(1), [festival](/man/festival)(1), [say](/man/say)(1), [spd-say](/man/spd-say)(1)
