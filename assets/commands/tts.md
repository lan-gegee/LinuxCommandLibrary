# TAGLINE

神经文本转语音合成

# TLDR

**合成语音**

```tts --text "[Hello world]"```

**保存到文件**

```tts --text "[Hello]" --out_path [output.wav]```

**列出模型**

```tts --list_models```

**使用指定模型**

```tts --text "[text]" --model_name [tts_models/en/ljspeech/tacotron2-DDC]```

**列出说话人**

```tts --model_name [model] --list_speakers```

# SYNOPSIS

**tts** [_--text text_] [_--out_path file_] [_--model_name model_] [_options_]

# PARAMETERS

**--text** _TEXT_
> 输入文本。

**--out_path** _FILE_
> 输出音频文件。

**--model_name** _MODEL_
> TTS 模型。

**--list_models**
> 显示模型列表。

**--speaker_idx** _ID_
> 选择说话人。

# DESCRIPTION

**tts** 是 Coqui TTS 的命令行界面。Coqui TTS 是一个开源深度学习文本转语音工具包，使用神经网络模型将文本输入转换为自然流畅的语音，支持多种语言和声音风格。

该工具自带多种预训练模型，可通过名称列出和选择。多说话人模型允许通过说话人索引选择不同的声音特征。音频输出可以保存为 WAV 文件或直接播放。

模型在首次使用时自动下载并缓存到本地。虽然支持 CPU 推理，但建议使用 GPU 以加快合成速度，尤其是较大的模型。

# CAVEATS

需要 Python。模型下载体积较大。建议使用 GPU。

# HISTORY

**TTS**（Coqui TTS）是一个包含多种模型的开源深度学习文本转语音工具包。

# INSTALL

```nix: nix profile install nixpkgs#tts```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[espeak](/man/espeak)(1), [festival](/man/festival)(1), [piper](/man/piper)(1)
