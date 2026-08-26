# TAGLINE

将文本转换为可听的语音

# TLDR

**朗读文本**

```say "[Hello, world]"```

**使用指定的嗓音朗读**

```say -v [Alex] "[Hello]"```

**列出所有可用嗓音**

```say -v "?"```

**朗读文件中的文本**

```say -f [input.txt]```

**将语音保存为音频文件**

```say -o [output.aiff] "[Hello, world]"```

**以指定语速朗读**（每分钟词数）

```say -r [200] "[Speaking faster now]"```

**向指定音频设备输出语音**

```say -a "[Built-in Output]" "[Hello]"```

**朗读时交互式高亮显示单词**

```say -i "[Hello, this highlights each word]"```

**将语音保存为 WAVE 文件**

```say --file-format=WAVE -o [output.wav] "[Hello, world]"```

# SYNOPSIS

**say** [_-v voice_] [_-r rate_] [_-o outfile_] [_-f infile_] [_-a device_] [_text..._]

# PARAMETERS

**-v** _voice_
> 使用指定的嗓音而非系统默认。使用 '?' 列出所有可用嗓音。

**-r** _rate_
> 语音语速，以每分钟词数表示。

**-f** _file_
> 从指定文件读取文本。使用 '-' 表示标准输入。

**-o** _file_
> 将语音保存到音频文件（默认 AIFF；格式取决于 **--file-format**）。

**-a** _device_
> 按 ID 或名称前缀指定音频输出设备。使用 '?' 列出设备。

**-n** _name:port_
> 通过 AUNetSend 将语音输出重定向到远程音频服务器。

**-i**, **--interactive**
> 合成期间逐行打印文本，并高亮正在朗读的单词。

**--progress**
> 合成期间显示进度：完成百分比、已用时间和字节数。

**--file-format** _FORMAT_
> 输出文件格式：AIFF、caff、m4af 或 WAVE。

**--data-format** _FORMAT_
> 音频数据格式（如 aac、alac、LEI16）。

**--bit-rate** _RATE_
> AAC 等压缩格式的比特率。使用 '?' 列出有效值。

**--quality** _LEVEL_
> 音频转换器质量级别，范围从 0（最低）到 127（最高）。

**--channels** _N_
> 输出音频声道数。

# DESCRIPTION

**say** 使用 macOS 语音合成管理器将文本转换为可听的语音。它可以朗读以参数形式提供的文本、来自文件的文本或标准输入的内容，既可通过音频输出播放，也可保存到文件。

有多种嗓音可选，具有不同的口音、语言和风格。默认嗓音和语音设置可在系统设置的"辅助功能 > 朗读内容"中配置。

输出可保存为 AIFF、WAVE、m4af 或 caff 音频格式，供以后播放或处理。

# CAVEATS

不支持直接输出 MP3；请使用 **--file-format** 指定 AIFF、WAVE、caff 或 m4af，必要时再进行转换。可用嗓音取决于 macOS 中已安装的内容；更多嗓音可从系统设置下载。

# HISTORY

**say** 自 Mac OS X 早期就包含在 macOS 中，其基础是 Apple 可追溯到 **20 世纪 80 年代** MacinTalk 的文字转语音技术。该命令提供了对整个操作系统所用同一套语音合成的终端访问方式。

# INSTALL

```apt: sudo apt install gnustep-gui-runtime```

```apk: sudo apk add shelli-opinionated```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[espeak](/man/espeak)(1), [spd-say](/man/spd-say)(1), [pico2wave](/man/pico2wave)(1)
