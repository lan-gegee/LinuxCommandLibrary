# TAGLINE

紧凑的开源语音合成器

# TLDR

**朗读文本**

```espeak "[Hello world]"```

**从文件朗读**

```espeak -f [text.txt]```

**设置语音/语言**

```espeak -v [en-us] "[Hello]"```

**调整语速**

```espeak -s [150] "[Hello]"```

**保存到音频**文件

```espeak -w [output.wav] "[Hello]"```

**列出可用语音**

```espeak --voices```

**调整音高**

```espeak -p [50] "[Hello]"```

# SYNOPSIS

**espeak** [_options_] [_words_]

# PARAMETERS

_WORDS_
> 要朗读的文本。

**-f** _FILE_
> 从文件读取文本。

**-v** _VOICE_
> 语音名称或语言。

**-s** _SPEED_
> 语速，以每分钟单词数计。

**-p** _PITCH_
> 音高（0-99）。

**-w** _FILE_
> 将输出写入 WAV 文件。

**--voices**
> 列出可用的语音。

**-a** _AMPLITUDE_
> 振幅/音量（0 到 200，默认 100）。

**-g** _GAP_
> 单词间隔，以 10 毫秒为单位。

**-m**
> 解析输入中的 SSML 标记。

**-x**
> 将音素助记符写到标准输出，而不是朗读出来。

**--stdout**
> 将 WAV 音频写到标准输出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**eSpeak** 是一个紧凑的开源文本转语音合成器，支持多种语言。它采用共振峰合成，声音带有独特的机械感，但资源占用极小。

该工具可将文本转换为通过扬声器播放或写入音频文件的语音。提供多种语言和语音可选，语速、音高等参数均可调节。

eSpeak 适用于无障碍访问、自动播报，以及需要语音合成但不想依赖庞大语音数据库的应用。

# CAVEATS

与神经网络 TTS 相比语音质量偏机械。部分语言的支持有限。发音可能需要调校。SSML 支持不完整。

# HISTORY

eSpeak 由 **Jonathan Duddington** 创建并以开源方式发布。其共振峰合成方案优先考虑体积小巧和多语言支持，而非自然逼真的音质。原版 eSpeak 的开发在 2015 年前后停止；活跃维护的分支 **espeak-ng** 现在是推荐使用的版本，并且在许多发行版上 `espeak` 只是围绕它的兼容包装器。

# INSTALL

```apt: sudo apt install espeak```

```dnf: sudo dnf install espeak```

```apk: sudo apk add espeak```

```zypper: sudo zypper install espeak```

```brew: brew install espeak```

```nix: nix profile install nixpkgs#espeak```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[espeak-ng](/man/espeak-ng)(1), [festival](/man/festival)(1), [pico2wave](/man/pico2wave)(1)

# RESOURCES

```[Homepage](https://espeak.sourceforge.net/)```

```[Source code](https://sourceforge.net/projects/espeak/files/espeak/)```

<!-- verified: 2026-07-14 -->
