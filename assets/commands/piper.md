# TAGLINE

快速的本地神经文本转语音引擎

# TLDR

**合成语音**

```echo "Hello world" | piper --model [en_US-lessac-medium] --output_file [output.wav]```

**列出模型**

```piper --list-models```

**使用特定模型**

```piper -m [model.onnx] -c [model.json] < [input.txt] > [output.wav]```

**设置说话人**

```piper --model [model.onnx] --speaker [0] < [input.txt]```

**调整语速**

```piper --model [model.onnx] --length_scale [1.5] < [input.txt]```

**JSON 输入模式**

```echo '{"text": "Hello"}' | piper --model [model.onnx] --json-input```

# SYNOPSIS

**piper** [_--model file_] [_--output_file file_] [_options_]

# PARAMETERS

**-m**, **--model** _FILE_
> ONNX 模型文件。

**-c**, **--config** _FILE_
> JSON 配置文件。

**--output_file** _FILE_
> 输出的 WAV 文件。

**--output_dir** _DIR_
> 输出目录。

**--speaker** _ID_
> 多说话人模型的说话人 ID。

**--length_scale** _FLOAT_
> 语速（越高越慢）。

**--noise_scale** _FLOAT_
> 语音的变化程度。

**--json-input**
> JSON 输入格式。

**--list-models**
> 显示可用模型。

# DESCRIPTION

**piper** 是一个快速、本地化的神经文本转语音系统，使用基于 ONNX 的语音模型从文本生成自然听感的语音。模型下载后完全离线运行，不需要互联网连接或云 API。

每个模型针对特定的语言和音色进行训练。多说话人模型支持通过说话人 ID 选择不同的声音变体。length_scale 和 noise_scale 参数控制语速和变化程度，可以对输出特性进行微调。

输入从 stdin 读取，输出为 WAV 音频。JSON 输入模式支持结构化文本处理和逐话语设置。通过 Piper 项目的模型仓库可获得多种语言的模型。

# CAVEATS

模型必须在使用前下载（每个通常 15-75 MB）。不同模型和语言之间的语音质量差异很大。通过 CUDA 进行 GPU 加速是可选的，但能提升批量处理的性能。输出始终是 WAV 格式；如需其他格式请用 ffmpeg 转换。

# HISTORY

**Piper** 由 **Michael Hansen**（rhasspy）为离线语音助手而创建，提供适合嵌入式和边缘设备的快速高质量 TTS。

# INSTALL

```dnf: sudo dnf install piper```

```pacman: sudo pacman -S piper```

```apk: sudo apk add piper```

```zypper: sudo zypper install piper```

```nix: nix profile install nixpkgs#piper```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[espeak](/man/espeak)(1), [festival](/man/festival)(1), [mimic](/man/mimic)(1), [say](/man/say)(1)
