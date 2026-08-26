# TAGLINE

eSpeak NG 文字转语音合成器

# TLDR

**朗读文本**

```speak-ng "[Hello world]"```

**从文件朗读**

```speak-ng -f [file.txt]```

**列出嗓音**

```speak-ng --voices```

**使用指定嗓音**

```speak-ng -v [en-us] "[text]"```

**输出到文件**

```speak-ng -w [output.wav] "[text]"```

**调整语速**

```speak-ng -s [150] "[text]"```

# SYNOPSIS

**speak-ng** [_-v voice_] [_-s speed_] [_-w file_] [_options_] [_text_]

# PARAMETERS

**-v** _VOICE_
> 嗓音/语言。

**-s** _SPEED_
> 每分钟词数。

**-f** _FILE_
> 从文件读取。

**-w** _FILE_
> 写入 WAV 文件。

**-p** _PITCH_
> 音调调整。

**--voices**
> 列出嗓音。

**-q**
> 静默（无声音）。

# DESCRIPTION

**speak-ng** 是 eSpeak NG 的命令行界面。eSpeak NG 是一款紧凑的开源文字转语音合成器，支持超过 100 种语言和口音。它使用共振峰合成（formant synthesis），基于音素规则生成语音，占用资源少且输出清晰可懂。

该工具从命令行参数、文件或 stdin 读取文本，并通过系统声音设备输出音频，或保存为 WAV 文件。语速（每分钟词数）、音调和音量等嗓音特性均可调节。支持 SSML（语音合成标记语言）输入，以便对发音和韵律进行精细控制。

eSpeak NG 广泛应用于无障碍工具和嵌入式系统，并作为 Speech Dispatcher 的后端。其紧凑的体积和广泛的语言支持使其成为许多 Linux 发行版上的默认语音合成器。

# CAVEATS

嗓音质量参差不齐。声音带有机器感。资源占用适中。

# HISTORY

**speak-ng** 是 **eSpeak NG** 的一部分，后者是 eSpeak 的分支，提供多语言的语音合成。

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

[espeak](/man/espeak)(1), [festival](/man/festival)(1), [pico2wave](/man/pico2wave)(1)
