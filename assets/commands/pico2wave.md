# TAGLINE

基于 SVOX Pico 引擎的语音合成器

# TLDR

**使用默认语言（en-US）将文本转换为 WAV 文件**

```pico2wave -w [output.wav] "[Hello world]"```

**指定合成语言**

```pico2wave --lang [de-DE] -w [output.wav] "[Hallo Welt]"```

**合成法语**

```pico2wave -l fr-FR -w [output.wav] "[Bonjour le monde]"```

**合成从文件读取的文本**

```pico2wave -w [output.wav] "$(cat [input.txt])"```

**合成后立即播放**

```pico2wave -w /tmp/speech.wav "[text]" && aplay /tmp/speech.wav```

# SYNOPSIS

**pico2wave** [_options_] **-w** _wavfile_ _text_

# PARAMETERS

**-w**, **--wave** _file_
> 输出的 WAV 文件路径（必需）。

**-l**, **--lang** _lang_
> 语言代码（默认：en-US）。支持的取值见 LANGUAGES 一节。

# DESCRIPTION

**pico2wave** 是一个使用 SVOX Pico 引擎的语音合成器。它将命令行提供的文本转换为 WAV 音频文件。输出始终为 16 kHz 的 16 位单声道 PCM。支持六种语言。

# LANGUAGES

```
en-US  - English (US)
en-GB  - English (UK)
de-DE  - German
es-ES  - Spanish
fr-FR  - French
it-IT  - Italian
```

# CAVEATS

仅支持六种语言。只能输出 WAV 格式；可使用 ffmpeg 或 sox 转换为其他格式。属于 libttspico-utils 软件包。文本必须作为命令行参数传入，不能通过 stdin。

# HISTORY

Pico TTS 由 **SVOX** 开发并以开源形式发布给 Android，后来被打包移植到 Linux。

# INSTALL

```apk: sudo apk add picotts```

```nix: nix profile install nixpkgs#picotts```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[espeak](/man/espeak)(1), [espeak-ng](/man/espeak-ng)(1), [flite](/man/flite)(1), [festival](/man/festival)(1), [aplay](/man/aplay)(1), [sox](/man/sox)(1)
