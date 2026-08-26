# TAGLINE

离线语音识别工具包

# TLDR

**将音频转录为文本文件**

```vosk-transcriber -i [audio.mp4] -o [output.txt]```

**生成 SRT 字幕**

```vosk-transcriber -i [video.mp4] -t srt -o [subtitles.srt]```

**以指定语言转录**

```vosk-transcriber -l [fr] -i [audio.m4a] -o [output.txt]```

**列出可用语言**

```vosk-transcriber --list-languages```

**从麦克风转录（vosk-cli）**

```vosk mic -o [output.txt] -t english```

**转录音频文件（vosk-cli）**

```vosk rec -c english [audio.mp3]```

# SYNOPSIS

**vosk-transcriber** [_options_] -i _input_ -o _output_

**vosk** _command_ [_options_]

# PARAMETERS

**-i** _file_
> 输入的音频或视频文件。

**-o** _file_
> 转录结果的输出文件。

**-t** _format_
> 输出格式：txt、srt、vtt。

**-l** _lang_
> 语言代码（en、fr、de、es、ru 等）。

**--list-languages**
> 显示可用的语言模型。

**--model** _path_
> 使用自定义的模型目录。

**--show-words**
> 包含词级时间戳。

**--server**
> 启动 WebSocket 识别服务器。

# DESCRIPTION

**vosk** 是一个离线语音识别工具包，支持包括英语、德语、法语、西班牙语、中文、俄语在内的 20 多种语言。它提供无需互联网连接的自动语音识别。

vosk-transcriber 命令行工具可处理音频和视频文件，并在首次使用时自动下载相应的语言模型。输出格式包括纯文本和带时间戳的字幕格式（SRT、VTT）。该工具包还可以作为 WebSocket 服务器运行，实现实时流式识别。

模型规模从面向移动/嵌入式设备的小型模型（50MB）到追求最高精度的大型模型不等。底层引擎支持连续转录、说话人识别和自定义词汇表。

# CAVEATS

首次运行会下载语言模型（50MB 至 1GB，取决于语言和模型大小）。需要 Python 3.6+ 以及处理视频所需的 ffmpeg。识别精度因模型大小和音频质量而异。部分语言的可用模型有限。

# HISTORY

**Vosk** 由 Alpha Cephei 开发，是一个开源的离线语音识别方案。它基于 Kaldi ASR 技术，提供适合移动和嵌入式设备的轻量模型。该项目作为云端识别服务的替代方案而广受欢迎，兼具隐私性和离线能力。

# SEE ALSO

[ffmpeg](/man/ffmpeg)(1), [whisper](/man/whisper)(1), [sox](/man/sox)(1)
