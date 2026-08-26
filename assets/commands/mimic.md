# TAGLINE

Mycroft AI 的开源文本转语音引擎

# TLDR

**朗读文本**

```mimic -t "[Hello world]"```

**从文件朗读**

```mimic -f [input.txt]```

**列出可用语音**

```mimic -lv```

**使用指定语音**

```mimic -voice [slt] -t "[text]"```

**保存到音频文件**

```mimic -t "[text]" -o [output.wav]```

**调整语速**

```mimic -t "[text]" --setf duration_stretch=[1.5]```

# SYNOPSIS

**mimic** [_options_] -t _text_|-f _file_

# PARAMETERS

**-t** _text_
> 要朗读的文本。

**-f** _file_
> 输入文本文件。

**-o** _file_
> 输出音频文件。

**-voice** _name_
> 要使用的语音。

**-lv**
> 列出语音。

**--setf** _param=val_
> 设置浮点参数。

**-ssml**
> 输入为 SSML。

# DESCRIPTION

**Mimic** 是 Mycroft AI 的开源文本转语音引擎。它是一个基于卡内基梅隆 Flite 的轻量级快速 TTS 系统，提供自然听感的语音合成。

Mimic 支持多种语音，可以离线运行而无需云服务。

# VOICE OPTIONS

```
slt   - US English female
awb   - Scottish male
rms   - US English male
kal   - US English male (diphone)
```

# CAVEATS

与云端 TTS 相比语音选择有限。质量因语音而异。自定义语音可能需要自行编译。

# HISTORY

Mimic 由 **Mycroft AI** 作为 CMU Flite 的分支开发，于 **2016 年**首次发布，为 Mycroft 语音助手提供离线 TTS。

# INSTALL

```apt: sudo apt install mimic```

```apk: sudo apk add mimic1```

```brew: brew install mimic```

```nix: nix profile install nixpkgs#mimic```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[espeak](/man/espeak)(1), [festival](/man/festival)(1), [pico2wave](/man/pico2wave)(1), [flite](/man/flite)(1)
