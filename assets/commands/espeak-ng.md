# TAGLINE

基于共振峰的下一代语音合成

# TLDR

**朗读文本**

```espeak-ng "[Hello world]"```

**使用指定语音**

```espeak-ng -v [en-gb] "[Hello]"```

**从文件读取**

```espeak-ng -f [document.txt]```

**输出到 WAV**

```espeak-ng -w [output.wav] "[Hello]"```

**调整语速**

```espeak-ng -s [175] "[Hello]"```

**列出语音**

```espeak-ng --voices```

**使用音素输入**

```espeak-ng -x "[h@l'oU]"```

# SYNOPSIS

**espeak-ng** [_options_] [_words_]

# PARAMETERS

_WORDS_
> 要朗读的文本。

**-v** _VOICE_
> 选择语音/语言。

**-f** _FILE_
> 从文件读取。

**-w** _FILE_
> 写入 WAV 文件。

**-s** _SPEED_
> 每分钟单词数。

**-p** _PITCH_
> 音高调整。

**-p** _PITCH_
> 音高调整（0 到 99，默认 50）。

**-a** _AMPLITUDE_
> 振幅/音量（0 到 200，默认 100）。

**-g** _GAP_
> 单词间隔，以 10 毫秒为单位。

**-x**
> 将转换后的音素助记符写到标准输出，而不是朗读出来。

**--ipa**
> 使用国际音标（IPA）写出音素。

**--stdout**
> 将音频以 WAV 数据形式写到标准输出。

**--voices**[=_lang_]
> 列出可用的语音，可按语言过滤。

**--help**
> 显示帮助信息。

# DESCRIPTION

**espeak-ng**（eSpeak New Generation）是 eSpeak 的一个分支，保持活跃开发，具有更多功能和更好的语音质量。它是一个基于共振峰的语音合成器，支持 100 多种语言。

该工具为无障碍访问、语音助手和各类应用提供文本转语音能力。与原版 eSpeak 相比，它在发音规则、语言支持和音素处理方面都有改进。

espeak-ng 是许多 Linux 发行版和语音合成框架中的默认 TTS 引擎。

# CAVEATS

听感仍然偏机械（共振峰合成）。部分高级 SSML 功能不受支持。语音质量因语言而异。输出格式选项有限。

# HISTORY

espeak-ng 由 **Reece H. Dunn** 从 eSpeak 分支而来，以便在原项目停止维护后继续开发。它现在是大多数 Linux 发行版中使用的活跃维护版本。

# INSTALL

```apt: sudo apt install espeak-ng```

```dnf: sudo dnf install espeak-ng```

```pacman: sudo pacman -S espeak-ng```

```apk: sudo apk add espeak-ng```

```zypper: sudo zypper install espeak-ng```

```brew: brew install espeak-ng```

```nix: nix profile install nixpkgs#espeak-ng```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[espeak](/man/espeak)(1), [festival](/man/festival)(1), [mimic](/man/mimic)(1), [pico2wave](/man/pico2wave)(1)

# RESOURCES

```[Source code](https://github.com/espeak-ng/espeak-ng)```

```[Documentation](https://github.com/espeak-ng/espeak-ng/blob/master/docs/guide.md)```

<!-- verified: 2026-07-14 -->
