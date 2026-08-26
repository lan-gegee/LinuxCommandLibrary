# TAGLINE

从视频 URL 或本地媒体离线进行 CPU 语音转文字

# TLDR

将本地音频或视频文件**转写**为纯文本

```yapsnap [path/to/file.mp4]```

从 URL **转写**视频（YouTube、X、TikTok 等）

```yapsnap "[https://www.youtube.com/watch?v=...]"```

在输出中**包含时间戳**

```yapsnap [input.mp4] --timestamps```

将转写文本**写入**指定路径

```yapsnap [input.mp4] -o [path/to/transcript.txt]```

URL 转写后**保留下载的音频**

```yapsnap "[url]" --keep-audio```

**禁用音频加速**预处理

```yapsnap [input.mp4] --speed 1.0```

**使用自定义模型目录**

```yapsnap [input.mp4] --model [path/to/model_dir]```

# SYNOPSIS

**yapsnap** _input_ [_options_]

同时也会安装别名 **transcribe**，行为完全相同。

# PARAMETERS

**-o**, **--output** _PATH_
> 将转写文本写入 _PATH_ 而不是默认的 **./transcripts/<input>_transcript.txt**。

**--timestamps**
> 每行输出一句话并以 **[MM:SS]** 作为前缀，而不是单个段落。

**--speed** _FACTOR_
> 转写前将音频加速 _FACTOR_ 倍（默认 **1.5**，保持音调不变）。设为 **1.0** 可禁用。

**--keep-audio**
> 转写 URL 后保留提取出的音频文件。

**--model** _DIR_
> 覆盖模型目录；若未指定则回退到环境变量 **KROKO_MODEL**，再回退到缓存的默认模型。

**--help**
> 显示完整的选项列表并退出。

# DESCRIPTION

**yapsnap** 是一个单命令语音转文字工具，可将本地文件或远程视频 URL 中的音频转写为纯文本。它完全在 CPU 上运行，使用流式 **Zipformer** 转导模型（Kroko English），首次运行时会下载约 80 MB 的模型，之后便可完全离线工作，无需任何 API 密钥，音频也不会离开本机。

URL 输入通过 **yt-dlp** 抓取并用 **ffmpeg** 解码，因此凡是这些工具能处理的内容都可以使用（YouTube、YouTube Shorts、X/Twitter、TikTok、Instagram Reels、直链媒体 URL 等）。本地文件则涵盖常见的容器和编码格式（**mp3**、**mp4**、**m4a**、**wav**、**webm**、**mov**、**mkv** 等）。

默认情况下音频会在转写前加速 1.5 倍（保持音调不变），这既能保持可用的质量，又能把实际耗时大幅压缩到实时以下（在笔记本电脑上）。输出是单个纯文本段落；**--timestamps** 可切换为逐句布局。

# CAVEATS

需要在 **PATH** 中有 **ffmpeg**；安装程序不会捆绑它。默认模型仅支持英语，不过也有法语、德语、西班牙语、意大利语、葡萄牙语、荷兰语、瑞典语、瑞士德语、希伯来语和土耳其语等额外模型（可通过 **--model** 选择）。准确度取决于输入的清晰程度：嘈杂的音频、浓重的口音或说话人重叠都会降低输出质量。首次运行时会因一次性下载模型而阻塞。

# HISTORY

**yapsnap** 于 **2025 年**由 GitHub 用户 **kouhxp** 发布，是基于开源 **Kroko** Zipformer 模型构建的极简、本地优先的云语音转文字 API 替代品。仓库地址为 **github.com/kouhxp/yapsnap**。

# SEE ALSO

[yt-dlp](/man/yt-dlp)(1), [ffmpeg](/man/ffmpeg)(1), [whisper](/man/whisper)(1)
