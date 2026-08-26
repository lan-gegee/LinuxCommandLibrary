# TAGLINE

经过优化的 Whisper 语音识别引擎

# TLDR

**转写音频文件**

```faster-whisper [audio.mp3]```

**使用指定模型转写**

```faster-whisper [audio.mp3] --model [large-v3]```

**带语言提示转写**

```faster-whisper [audio.mp3] --language [en]```

**输出为 SRT 字幕**

```faster-whisper [audio.mp3] --output_format srt```

**翻译成英语**

```faster-whisper [audio.mp3] --task translate```

**将输出保存到目录**

```faster-whisper [audio.mp3] --output_dir [/path/to/output]```

**带词级时间戳转写**

```faster-whisper [audio.mp3] --word_timestamps true```

# SYNOPSIS

**faster-whisper** _audio_ [_--model size_] [_--language lang_] [_--task task_] [_options_]

# PARAMETERS

**--model** _SIZE_
> 模型大小：tiny、base、small、medium、large-v1、large-v2、large-v3（默认：small）。

**--language** _LANG_
> 语言代码（en、de、fr 等）或自动检测。

**--task** _TASK_
> 任务：transcribe 或 translate。

**--output_format** _FORMAT_
> 输出格式：txt、vtt、srt、tsv、json、all。

**--output_dir** _DIR_
> 结果输出目录。

**--word_timestamps** _BOOL_
> 包含词级时间戳。

**--device** _DEVICE_
> 设备：cpu、cuda、auto（默认：auto）。

**--compute_type** _TYPE_
> 计算类型：int8、float16、float32（CPU 上默认：int8）。

**--beam_size** _N_
> 束搜索宽度（默认：5）。

**--vad_filter** _BOOL_
> 启用语音活动检测过滤（使用 Silero VAD）。

**--initial_prompt** _TEXT_
> 可选文本，作为解码器的初始提示。

**--threads** _N_
> CPU 线程数。

# DESCRIPTION

**faster-whisper** 是 OpenAI Whisper 的重新实现，基于 **CTranslate2**——一种面向 Transformer 模型的快速推理引擎。它比原版 Whisper 的转写速度最高快 4 倍，同时占用更少内存。

该工具支持所有 Whisper 模型尺寸。模型越大越准确但越慢。compute type 参数控制精度：int8 最快且最省内存，float16 在 GPU 上是良好折衷，float32 精度最高。

语音活动检测（VAD）过滤会跳过静音片段，同时提升速度和准确性。语言检测是自动的，但显式指定语言可避免检测开销。

基础库通过 `pip install faster-whisper` 安装（仅 Python API）。如需命令行用法，请安装封装工具，例如 `pip install faster-whisper-cli` 或 `pip install whisper-ctranslate2`。CTranslate2 会自动处理模型转换。GPU 加速需要 CUDA 工具包。

# CAVEATS

大模型需要大量内存。GPU 需要 CUDA 工具包。首次运行会下载并转换模型。准确性因音频质量而异。CLI 不支持说话人分离（可通过 API 使用）。

# HISTORY

**faster-whisper** 由 **Guillaume Klein**（SYSTRAN）于 **2023 年**创建，使用 CTranslate2 优化 Whisper 推理。凭借速度和内存优势，它成为生产环境中首选的 Whisper 实现。该项目在转写工作流中得到了广泛采用。

# SEE ALSO

[whisper](/man/whisper)(1), [deepspeech](/man/deepspeech)(1), [ffmpeg](/man/ffmpeg)(1)
