# TAGLINE

macOS 音频文件格式转换工具

# TLDR

**将音频文件转换为 AAC**

```afconvert -f m4af -d aac [input.wav] [output.m4a]```

转换为 **ALAC**（Apple Lossless）

```afconvert -f m4af -d alac [input.wav] [output.m4a]```

转换为 **AIFF**

```afconvert -f AIFF -d BEI16 [input.mp3] [output.aiff]```

为 AAC 编码设置**比特率**

```afconvert -f m4af -d aac -b [128000] [input.wav] [output.m4a]```

以 VBR **策略**转换

```afconvert -f m4af -d aac -s 3 -b [128000] [input.wav] [output.m4a]```

列出支持的**格式**

```afconvert -hf```

# SYNOPSIS

**afconvert** [_options_] _input_ [_output_]

# DESCRIPTION

**afconvert** 是 macOS 上用于在各音频文件格式之间转换的命令行工具。它支持 Core Audio 能处理的所有音频格式，包括 WAV、AIFF、MP3、AAC、ALAC、CAF 等。如果未指定输出文件，文件名会自动生成并保存在与输入相同的目录中。

该工具可调用 Apple 的音频编解码器，并在格式转换的同时执行采样率转换、位深转换和声道重映射。

# PARAMETERS

**-f**, **--file** _format_
> 输出文件格式（m4af、WAVE、AIFF、caff 等）。

**-d**, **--data** _format_
> 音频数据格式（aac、alac、BEI16、LEF32 等）。可附带采样率和格式标志。

**-b**, **--bitrate** _rate_
> 压缩格式的总比特率（单位：比特/秒）。

**-c**, **--channels** _number_
> 输出声道数。

**-l**, **--channellayout** _tag_
> 声道布局标签。

**-q**, **--quality** _quality_
> 编解码器质量（0-127，越高越好）。

**-r**, **--src-quality** _quality_
> 采样率转换器质量（0-127，默认：127）。

**--src-complexity** _complexity_
> 采样率转换器的复杂度（line、norm、bats）。

**-s**, **--strategy** _strategy_
> 比特率分配策略（0=CBR、1=ABR、2=VBR_constrained、3=VBR）。

**-o** _filename_
> 指定输出文件路径。

**--dither** _algorithm_
> 抖动（dither）算法（1 或 2）。

**--mix**
> 启用声道下混。

**-v**, **--verbose**
> 显示进度信息。

**-h**, **--help**
> 显示帮助信息。

**-hf**, **--help-formats**
> 列出所有受支持的文件格式和数据格式。

# CAVEATS

此工具仅限 macOS。某些格式转换可能是有损的。AAC 编码质量随比特率设置而变化。并非所有格式组合都有效。使用 **-hf** 可以查看你的系统支持哪些格式。

# HISTORY

**afconvert** 自 Mac OS X 时代起便是 macOS 的一部分，让用户能通过命令行使用与 iTunes 及其他 Apple 应用相同的音频转换能力。

# SEE ALSO

[ffmpeg](/man/ffmpeg)(1), [sox](/man/sox)(1), [lame](/man/lame)(1)
