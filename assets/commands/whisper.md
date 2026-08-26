# TAGLINE

AI 驱动的语音识别与转录工具

# TLDR

**转录音频文件**

```whisper [audio.mp3]```

**使用指定模型转录**

```whisper --model [medium] [audio.mp3]```

**带语言提示转录**

```whisper --language [en] [audio.mp3]```

**输出指定格式**

```whisper --output_format [srt] [audio.mp3]```

**翻译成英语**

```whisper --task translate [audio.mp3]```

**输出到指定目录**

```whisper --output_dir [/path/to/output] [audio.mp3]```

**转录多个文件**

```whisper [audio1.mp3] [audio2.wav]```

**在 GPU 上使用 float16**

```whisper --device cuda --fp16 True [audio.mp3]```

# SYNOPSIS

**whisper** [_--model size_] [_--language lang_] [_--task task_] [_--output_format fmt_] [_options_] _files_

# PARAMETERS

**--model** _SIZE_
> 模型大小：tiny、base、small、medium、large、turbo（默认：turbo）。仅英语变体：tiny.en、base.en、small.en、medium.en。

**--language** _LANG_
> 语言代码（en、de、fr 等）或 auto。

**--task** _TASK_
> 任务：transcribe（转录）或 translate（翻译）。

**--output_format** _FORMAT_
> 输出格式：txt、vtt、srt、tsv、json、all。

**--output_dir** _DIR_
> 输出目录。

**--device** _DEVICE_
> 设备：cpu、cuda。

**--fp16** / **--no-fp16**
> 使用 float16（GPU）或 float32。

**--temperature** _TEMP_
> 采样温度。

**--best_of** _NUM_
> 候选数量。

**--beam_size** _NUM_
> 束搜索宽度。

**--word_timestamps** _BOOL_
> 包含词级时间戳。

**--condition_on_previous_text** _BOOL_
> 将之前的输出作为上下文。

**--verbose** _BOOL_
> 显示进度和转录内容。

**--threads** _NUM_
> CPU 线程数。

**--model_dir** _DIR_
> 保存和加载模型的目录（默认：~/.cache/whisper）。

**--initial_prompt** _TEXT_
> 可选文本，作为第一个窗口的提示词。

**--clip_timestamps** _TIMESTAMPS_
> 逗号分隔的起止时间戳，用于处理特定音频片段。

# DESCRIPTION

**Whisper** 是 OpenAI 的自动语音识别（ASR）系统。它可以转录多种语言的音频，并能翻译成英语。

模型大小在精度和速度之间权衡：tiny 运行最快，large 精度最高。turbo 模型（默认）提供了良好的平衡，速度比 large 快约 8 倍而质量损失很小。.en 后缀（tiny.en、base.en）表示仅英语模型，对英语的效果略好。turbo 模型没有针对翻译任务进行训练。

语言检测是自动的，但也可以手动指定。对于非英语音频，指定语言可以提高准确率。翻译模式可将任何语言转录为英文文本。

输出格式包括纯文本、字幕（SRT、VTT）以及带时间数据的 JSON。词级时间戳可实现卡拉 OK 式的高亮显示。

处理时如果可用则使用 GPU（CUDA），比 CPU 快得多。--fp16 标志可在兼容的 GPU 上启用半精度运算。

音频预处理通过 FFmpeg 支持多种格式。长文件分段处理，并在各段之间保持上下文。

# CAVEATS

大模型需要大量显存（large 需要 10GB 以上）。CPU 推理速度慢。准确率因音频质量和口音而异。在静音或嘈杂片段上可能出现幻觉。不支持说话人分离。首次使用需下载模型。

# HISTORY

**Whisper** 由 **OpenAI** 于 **2022 年 9 月**发布。它基于 68 万小时的多语言音频训练而成，达到了接近人类的转录准确率。开源发布使本地部署成为可能，催生了众多社区项目和集成方案。2024 年 9 月新增了 large-v3-turbo 模型，推理速度显著提升而质量损失极小。

# SEE ALSO

[ffmpeg](/man/ffmpeg)(1), [vosk](/man/vosk)(1), [deepspeech](/man/deepspeech)(1)
