# TAGLINE

开源语音转文字引擎

# TLDR

**转录音频文件**

```deepspeech --model [model.pbmm] --audio [audio.wav]```

**配合 scorer 转录**（语言模型）

```deepspeech --model [model.pbmm] --scorer [scorer.scorer] --audio [audio.wav]```

**以扩展输出转录**

```deepspeech --model [model.pbmm] --audio [audio.wav] --extended```

**使用 TFLite 模型转录**

```deepspeech --model [model.tflite] --audio [audio.wav]```

**为 CTC 解码器设置束宽**

```deepspeech --model [model.pbmm] --audio [audio.wav] --beam_width [500]```

# SYNOPSIS

**deepspeech** **--model** _model_ **--audio** _audio_ [_options_]

# PARAMETERS

**--model** _file_
> 模型文件路径（.pbmm 或 .tflite）。

**--scorer** _file_
> 外部 scorer/语言模型路径。

**--audio** _file_
> 要转录的音频文件（16kHz、16 位、单声道 WAV）。

**--extended**
> 输出单词时间戳和置信度。

**--json**
> 以 JSON 格式输出结果。

**--beam_width** _n_
> CTC 解码器的束宽。

**--lm_alpha** _value_
> 语言模型权重。未指定时使用 scorer 包中的默认值。

**--lm_beta** _value_
> 单词插入奖励。未指定时使用 scorer 包中的默认值。

**--candidate_transcripts** _n_
> JSON 输出中包含的候选转写数量（默认：3）。

**--hot_words** _words_
> 热词及其概率提升值。

**--version**
> 打印版本并退出。

# DESCRIPTION

**DeepSpeech** 是一个基于深度学习的开源语音转文字引擎。它采用端到端神经网络架构将音频转换为文本转写。

该系统需要训练好的模型，还可选配外部 scorer（语言模型）以提高准确率。官方提供预训练的英文模型，该工具包也支持为其他语言或领域训练自定义模型。

音频输入必须是 16kHz、16 位、单声道的 WAV 格式。该工具既支持批量转录文件，也支持通过其 API 进行实时流式转录。

# PYTHON API

```python
import deepspeech
import wave

model = deepspeech.Model('model.pbmm')
model.enableExternalScorer('scorer.scorer')

with wave.open('audio.wav', 'rb') as w:
    audio = w.readframes(w.getnframes())

text = model.stt(audio)
print(text)
```

# CAVEATS

准确率取决于音频质量以及与训练数据的声学相似度。模型体积较大（数百 MB）。GPU 加速需要特定版本的 TensorFlow 构建。项目开发已放缓；新项目可以考虑 Whisper 等替代方案。

# HISTORY

DeepSpeech 由 **Mozilla** 自 **2017 年**起开发，是其创建开源语音技术的 Common Voice 项目的一部分。它基于百度的研究成果，采用循环神经网络进行语音识别。Mozilla 在 **2020 年**裁员后停止了积极开发，但该项目由社区 fork 并以 **Coqui STT** 的名义继续发展。

# INSTALL

```aur: yay -S deepspeech```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vosk](/man/vosk)(1), [whisper](/man/whisper)(1)
