# TAGLINE

具备表现力语音的 AI 文本转音频合成工具。

# TLDR

**从文本生成语音**

```python -m bark --text "[Hello, how are you?]" --output_filename [output.wav]```

**使用指定的说话人预设**

```python -m bark --text "[Hello]" --output_filename [output.wav] --history_prompt [v2/en_speaker_6]```

**带情感/音效生成**

```python -m bark --text "[laughs] Oh that's funny! [sighs]" --output_filename [output.wav]```

**用其他语言生成**

```python -m bark --text "[Bonjour le monde]" --output_filename [output.wav] --history_prompt [v2/fr_speaker_1]```

**带乐谱记号生成**

```python -m bark --text "[♪ La la la ♪]" --output_filename [output.wav]```

# SYNOPSIS

**python** **-m** **bark** **--text** _text_ **--output_filename** _file_ [_options_]

# PARAMETERS

**--text** _TEXT_
> 要合成的输入文本。

**--output_filename** _FILE_
> 输出音频文件路径（.wav）。

**--history_prompt** _PRESET_
> 说话人语音预设（如 v2/en_speaker_0 至 v2/en_speaker_9）。

**--text_temp** _FLOAT_
> 文本生成温度（默认：0.7）。

**--waveform_temp** _FLOAT_
> 波形生成温度（默认：0.7）。

# DESCRIPTION

**Bark** 是 **Suno AI** 推出的基于 Transformer 的文本转音频模型。与传统 TTS 不同，Bark 可以生成极具表现力的语音，包括笑声、叹息、呼吸、哭声甚至音乐。

文本中的特殊标记控制非语音声音：`[laughter]`、`[laughs]`、`[sighs]`、`[gasps]`、`[clears throat]` 和 `[music]`。用 `♪` 符号标记的乐谱可以生成歌唱。将单词大写可加强调语气，`...` 表示迟疑。`[MAN]` 和 `[WOMAN]` 标记会影响说话人的性别倾向。

说话人预设决定嗓音特征。预设覆盖多种语言：英语、德语、西班牙语、法语、印地语、意大利语、日语、韩语、波兰语、葡萄牙语、俄语、土耳其语和中文。

直接从仓库安装：`pip install git+https://github.com/suno-ai/bark.git`（不要使用 `pip install bark`，那是另一个无关的软件包）。模型在首次使用时自动下载。强烈建议使用 GPU（CUDA）以获得合理的生成速度。

# CAVEATS

CPU 上速度缓慢（强烈建议使用 GPU）。模型下载体积大（约 5GB）。输出质量参差不齐。长文本应拆分为句子。不适合实时合成。可能产生意外的音频瑕疵。

# HISTORY

**Bark** 由 **Suno AI** 于 **2023 年 4 月**发布，是一个开源的文本转音频模型。它能生成带有情感和非语言声音的表现力语音，这一点使其有别于传统 TTS 系统。它在创意音频生成领域迅速走红。

# INSTALL

```nix: nix profile install nixpkgs#bark```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[piper](/man/piper)(1), [tts](/man/tts)(1), [espeak](/man/espeak)(1)

# RESOURCES

```[Source code](https://github.com/suno-ai/bark)```

<!-- verified: 2026-06-19 -->
