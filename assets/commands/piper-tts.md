# TAGLINE

快速的本地神经文本转语音 CLI

# TLDR

**下载**语音模型

```python3 -m piper.download_voices [en_US-lessac-medium]```

将 stdin 的文本**合成为** WAV 文件

```echo "[Hello world.]" | piper --model [en_US-lessac-medium] --output-file [out.wav]```

**合成**内联给定的文本

```piper --model [en_US-lessac-medium] --output-file [greeting.wav] -- "[This is a test.]"```

将原始音频流直接**输出到**播放器

```echo "[Hi there.]" | piper --model [en_US-lessac-medium] --output-raw | aplay -r [22050] -f S16_LE -t raw -```

在多说话人模型中**选择说话人**

```piper --model [de_DE-thorsten-medium] --speaker [0] --output-file [de.wav] -- "[Guten Tag.]"```

**使用 GPU 加速**

```piper --model [en_US-lessac-medium] --cuda --output-file [gpu.wav] -- "[Running on GPU.]"```

# SYNOPSIS

**piper** **--model** _voice_ [**--output-file** _file_ | **--output-raw**] [_options_]

# PARAMETERS

**-m**, **--model** _voice_
> 语音模型标识符（例如 _en_US-lessac-medium_）或 ONNX 文件路径。

**-f**, **--output-file** _file_
> 将合成好的 WAV 音频写入 _file_。

**--output-raw**
> 将原始 16 位 PCM 音频写到 stdout（便于管道传给播放器）。

**--input-file** _file_
> 从 _file_ 而不是 stdin 读取输入文本。

**--data-dir** _dir_
> 存储已下载语音文件的目录。

**--speaker** _n_
> 为多说话人语音选择说话人索引。

**--sentence-silence** _seconds_
> 句子之间插入的静音秒数。

**--volume** _factor_
> 输出音量倍率（1.0 表示不变）。

**--cuda**
> 使用 CUDA 执行提供程序（需要 onnxruntime-gpu）。

**--json-input**
> 从 stdin 读取 JSON 对象而不是纯文本。

# DESCRIPTION

**piper** 是一个离线神经文本转语音引擎，运行导出为 ONNX 格式的 VITS 语音模型。安装 **piper-tts** Python 软件包后会提供 **piper** 二进制文件，它从标准输入（或 **--input-file** 指定的文件）读取文本，并将 16 位 PCM WAV 音频写入文件或标准输出以供流式处理。

语音模型单独分发，可通过 **python3 -m piper.download_voices** 下载。模型涵盖多种语言和口音，其中一些是多说话人模型——使用 **--speaker** 选择音色。音素化通过内置的 **espeak-ng** 完成，并且接受写在双方括号中的内联覆盖写法（例如 `[[ bˈætmæn ]]`），以实现细粒度的发音控制。

输出质量和延迟取决于模型变体（_x_low_、_low_、_medium_、_high_）。对于交互式使用场景，通常会将 piper 封装为守护进程，使模型只加载一次而不是每次调用都加载。

# CAVEATS

加载 ONNX 模型的启动开销明显；对低延迟应用而言，应将 piper 作为流式服务运行而不是逐句调用。输出采样率由所选语音决定（通常为 22050 Hz），使用 **--output-raw** 时必须与播放器的设置匹配。各语音模型有各自的许可证。

# HISTORY

**piper** 由 **Michael Hansen** 于 **2022 年 11 月**在 **Rhasspy** 项目下创建，用于离线语音助手，目前在 **Nabu Casa / Open Home Foundation** 下作为 GPL-3.0 的 **piper1-gpl** 项目继续开发。它为 **Home Assistant**、**NVDA** 屏幕阅读器和 **LocalAI** 提供语音合成能力。

# INSTALL

```nix: nix profile install nixpkgs#piper-tts```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[espeak-ng](/man/espeak-ng)(1), [festival](/man/festival)(1), [flite](/man/flite)(1)
